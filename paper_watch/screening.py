"""Conservative, explainable relevance screening without a model dependency."""

from __future__ import annotations

import re
import unicodedata
from typing import Any

SCREENING_VERSION = "scope-rules-v2"


def _normalise(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"[\s_\-–—]+", " ", text).strip()


def _matches(text: str, term: str) -> bool:
    term = _normalise(term)
    if not term:
        return False
    # Latin short words such as "arm" must not match "charm".
    if re.search(r"[a-z0-9]", term):
        plural = r"s?" if re.search(r"[a-z]$", term) and not term.endswith("s") else ""
        return bool(re.search(r"(?<!\w)" + re.escape(term) + plural + r"(?!\w)", text))
    return term in text


def _terms(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    return list(dict.fromkeys(_normalise(term) for term in values if isinstance(term, str) and term.strip()))


def _threshold(value: Any, default: int) -> float:
    try:
        return max(0.0, min(100.0, float(value)))
    except (TypeError, ValueError):
        return float(default)


def screen_paper(paper: dict, config: dict) -> dict:
    """Return an auditable scope decision; a citation alone is not relevance.

    Each distinct positive term contributes 20 points and a title match another
    10; configured priority terms add 20, capped at 100. Negatives subtract 25. Metadata-poor records and
    conflicts always require review. Thresholds use this same 0–100 scale.
    """
    scope = config.get("scope", {})
    title = _normalise(paper.get("title"))
    abstract = _normalise(paper.get("abstract"))
    text = title + " " + abstract
    priorities = _terms(scope.get("priority_terms"))
    positives = list(dict.fromkeys(_terms(scope.get("positive_terms")) + priorities))
    negatives = _terms(scope.get("negative_terms"))
    positive_matches = [term for term in positives if _matches(text, term)]
    negative_matches = [term for term in negatives if _matches(text, term)]
    title_matches = [term for term in positive_matches if _matches(title, term)]
    priority_matches = [term for term in positive_matches if term in priorities]
    score = max(0, min(100, 20 * len(positive_matches) + 10 * len(title_matches) + 20 * len(priority_matches) - 25 * len(negative_matches)))
    evidence = []
    for polarity, matches in (("positive", positive_matches), ("negative", negative_matches)):
        for term in matches:
            field = "title" if _matches(title, term) else "abstract"
            original = str(paper.get(field) or "")
            # Return a bounded original excerpt alongside the actual matched term.
            position = _normalise(original).find(term)
            excerpt = original[max(0, position - 80): max(0, position - 80) + 240]
            evidence.append({"term": term, "polarity": polarity, "priority": term in priorities, "field": field, "excerpt": excerpt})

    target_threshold = _threshold(scope.get("target_threshold"), 45)
    review_threshold = min(target_threshold, _threshold(scope.get("review_threshold"), 15))
    if not title or len(abstract) < 80:
        decision, reason = "review", "标题或摘要信息不足，等待补全后再判断。"
    elif not positives:
        decision, reason = "review", "尚未配置研究范围的正向关键词，不能自动认定目标论文。"
    elif positive_matches and negative_matches:
        decision, reason = "review", "同时命中研究范围和排除关键词，需要人工确认语境。"
    elif len(positive_matches) >= 2 and score >= target_threshold:
        decision, reason = "target", "标题和摘要与配置的研究范围有多项匹配。"
    elif positive_matches or score >= review_threshold:
        decision, reason = "review", "与研究范围存在部分关联，证据不足以自动纳入。"
    else:
        decision, reason = "excluded", "完整摘要未命中配置的研究范围关键词。"

    return {
        "decision": decision,
        "score": score,
        "reason": reason,
        "evidence": evidence,
        "method": SCREENING_VERSION,
    }
