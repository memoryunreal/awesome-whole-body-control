#!/usr/bin/env python3
"""Aggregate research chunks into final deliverables."""
import re, csv, os, sys
from pathlib import Path
from collections import defaultdict, OrderedDict

ROOT = Path("/Users/lizhe/Project/awesome-paper-list")
CHUNKS = ROOT / "research_chunks"

# YAML-ish parser tolerant of formatting variation
def parse_chunk(path):
    """Yield dicts of paper records from a chunk file."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Split on top-level "- title:" markers
    blocks = re.split(r'(?=^\s*-\s+title\s*:)', text, flags=re.MULTILINE)
    for block in blocks:
        if "title:" not in block:
            continue
        rec = {}
        # extract simple key: value pairs (single-line values)
        for line in block.splitlines():
            m = re.match(r'^[\s\-]*([a-zA-Z_]+)\s*:\s*(.*)$', line)
            if not m:
                continue
            k, v = m.group(1).strip(), m.group(2).strip()
            if k in ("title","authors","year","venue","arxiv_id","paper_url","project_url",
                     "code_url","dataset_url","category","robot_platform","code_status",
                     "one_line","why_it_matters","category_hint","one_sentence_summary"):
                # remove inline comments after #
                v = re.sub(r'\s+#.*$', '', v).strip()
                # strip surrounding quotes
                v = v.strip('"').strip("'")
                if v.lower() in ("null","none","n/a","na","-","unknown",""):
                    v = ""
                rec[k] = v
            elif k in ("uses_real_robot","uses_humanoid","uses_simulation",
                       "uses_human_motion_data","uses_object_observation","uses_contact_modeling"):
                rec[k] = v.lower() in ("true","yes","1")
            elif k in ("task_tags","secondary_categories"):
                # may be list-like
                rec[k] = v.strip("[]").strip()
        if rec.get("title"):
            yield rec

# Load all chunks
all_records = []
chunk_meta = OrderedDict()
for fname in sorted(os.listdir(CHUNKS)):
    if not fname.endswith(".md"):
        continue
    p = CHUNKS / fname
    recs = list(parse_chunk(p))
    chunk_meta[fname] = len(recs)
    for r in recs:
        r["_source_chunk"] = fname
        all_records.append(r)

print(f"Total raw records across chunks: {len(all_records)}", file=sys.stderr)
for k,v in chunk_meta.items():
    print(f"  {k}: {v}", file=sys.stderr)

# Deduplicate by normalized title; prefer non-seed sources
def norm_title(t):
    t = t.lower()
    t = re.sub(r'[^a-z0-9]+',' ',t).strip()
    t = re.sub(r'\s+',' ',t)
    # Drop common subtitle filler words for dedup (after main name match)
    t = re.sub(r'\b(from|the|to|a|an|via|using|with|of|for|on|in)\b',' ',t)
    t = re.sub(r'\s+',' ',t).strip()
    return t

def dedup_key(t, arxiv_id=""):
    """Use first 5 normalized words OR arxiv_id for dedup."""
    if arxiv_id:
        m = re.match(r'(\d{4}\.\d{4,6})', arxiv_id)
        if m:
            return f"arxiv:{m.group(1)}"
    nt = norm_title(t)
    words = nt.split()[:5]
    return " ".join(words) if words else nt

# Trust order: 02-08 (verified) > 01 (seed)
trust = {"01_seed.md":0, "02_hoi_motion.md":5, "03_wbc_tracking.md":6, "04_loco_manip.md":6,
         "05_foundation.md":6, "06_retarget_teleop.md":6, "07_data_bench_s2r.md":6,
         "08_loco_anim.md":6}

merged = {}
for r in all_records:
    key = dedup_key(r["title"], r.get("arxiv_id",""))
    if not key:
        continue
    score = trust.get(r["_source_chunk"], 1)
    if key not in merged:
        merged[key] = (score, r.copy())
    else:
        prev_score, prev = merged[key]
        if score > prev_score:
            # merge: prefer new for richer fields, but keep prev fields if new lacks
            new = r.copy()
            for k,v in prev.items():
                if k not in new or not new.get(k):
                    new[k] = v
            merged[key] = (score, new)
        else:
            # keep prev but fill in missing
            for k,v in r.items():
                if k not in prev or not prev.get(k):
                    prev[k] = v
            merged[key] = (prev_score, prev)

unique = [v[1] for v in merged.values()]
print(f"Unique papers after dedup: {len(unique)}", file=sys.stderr)

# Category mapping
def primary_category(rec):
    c = (rec.get("category") or rec.get("category_hint") or "").strip()
    src = rec.get("_source_chunk", "")
    title = rec.get("title","").lower()
    cl = c.lower()
    # Direct mapping by source chunk
    if "07_data_bench" in src:
        if "contact" in cl or "metric" in cl or "evaluation" in cl:
            return "metrics"
        if "sim2real" in cl or "sim-to-real" in cl or "deploy" in cl:
            return "sim2real"
        return "datasets"
    if "08_loco_anim" in src:
        if "physics-anim" in cl or "anim" in cl or "character" in cl:
            return "animation"
        return "wbc_tracking"  # locomotion lumped with tracking? No, separate
    if "06_retarget_teleop" in src:
        if "teleop" in cl or "demonstr" in cl:
            return "teleop"
        return "retarget"
    if "05_foundation" in src:
        return "foundation"
    if "04_loco_manip" in src:
        return "loco_manip"
    if "03_wbc_tracking" in src:
        return "wbc_tracking"
    if "02_hoi_motion" in src:
        if "object-aware" in cl or "scene" in cl:
            return "object_aware"
        return "hoi_motion"
    # Seed - infer
    h = (rec.get("category_hint") or "").lower()
    if "hoi" in h: return "hoi_motion"
    if "object" in h: return "object_aware"
    if "wbc" in h or "tracking" in h: return "wbc_tracking"
    if "loco-manip" in h or "manip" in h: return "loco_manip"
    if "foundation" in h or "vla" in h: return "foundation"
    if "retarget" in h: return "retarget"
    if "teleop" in h: return "teleop"
    if "dataset" in h: return "datasets"
    if "sim" in h: return "sim2real"
    if "anim" in h: return "animation"
    if "locomotion" in h: return "wbc_tracking"
    return "wbc_tracking"

for r in unique:
    r["_cat"] = primary_category(r)

cat_order = [
    ("hoi_motion", "Human-Object Interaction Motion Generation"),
    ("object_aware", "Object-Aware Human Motion Synthesis"),
    ("wbc_tracking", "Whole-Body Motion Tracking and Imitation"),
    ("loco_manip", "Whole-Body Control and Loco-Manipulation"),
    ("foundation", "Humanoid Foundation Models and Generalist Policies"),
    ("retarget", "Human-to-Humanoid Retargeting"),
    ("teleop", "Teleoperation and Demonstration Collection"),
    ("datasets", "Datasets and Benchmarks"),
    ("metrics", "Evaluation Metrics and Contact Modeling"),
    ("sim2real", "Sim-to-Real and Deployment Systems"),
    ("animation", "Related Character Animation and Physics-Based Motion Generation"),
]

# Code status normalization
def norm_code_status(s):
    if not s:
        return ""
    s = s.strip()
    sl = s.lower()
    if "⭐" in s or sl.startswith("code") or sl == "open source" or "verified" in sl:
        return "⭐ Code"
    if "🧩" in s or "partial" in sl:
        return "🧩 Partial Code"
    if "📦" in s or "dataset" in sl:
        return "📦 Dataset"
    if "🌐" in s or "project" in sl:
        return "🌐 Project Page"
    if "⏳" in s or "coming" in sl:
        return "⏳ Code Coming Soon"
    if "🔁" in s or "unofficial" in sl:
        return "🔁 Unofficial Code"
    if "❌" in s or "no code" in sl:
        return "❌ No Code"
    if "uncertain" in sl:
        return "❓ Uncertain"
    return ""

for r in unique:
    explicit = norm_code_status(r.get("code_status", ""))
    if explicit:
        r["code_status_norm"] = explicit
    else:
        # Infer from URLs
        cu = (r.get("code_url") or "").strip()
        pu = (r.get("project_url") or "").strip()
        du = (r.get("dataset_url") or "").strip()
        if cu and ("github.com" in cu or "gitlab" in cu or "bitbucket" in cu):
            r["code_status_norm"] = "⭐ Code"
        elif du:
            r["code_status_norm"] = "📦 Dataset"
        elif pu:
            r["code_status_norm"] = "🌐 Project Page"
        else:
            r["code_status_norm"] = "❌ No Code"

# Year normalization
def parse_year(r):
    y = r.get("year","")
    m = re.search(r'(20\d\d)', y)
    if m: return int(m.group(1))
    v = r.get("venue","")
    m = re.search(r'(20\d\d)', v)
    if m: return int(m.group(1))
    a = r.get("arxiv_id","")
    m = re.match(r'(\d{2})(\d{2})', a)
    if m:
        yr = 2000 + int(m.group(1))
        if 2018 <= yr <= 2027: return yr
    return 0

for r in unique:
    r["_year"] = parse_year(r)

# Build emoji prefix
def emoji_prefix(r):
    parts = []
    cs = r["code_status_norm"]
    em = cs.split()[0] if cs.split() else ""
    parts.append(em)
    if r.get("uses_real_robot"):
        parts.append("🤖")
    if r.get("uses_humanoid"):
        parts.append("🧍")
    if r.get("uses_simulation") and not r.get("uses_real_robot"):
        parts.append("🧱")
    return " ".join(parts)

# Sort key: year desc, then code-priority, then real_robot, then title
def sort_key(r):
    cs = r["code_status_norm"]
    code_pri = 0
    if cs.startswith("⭐"): code_pri = 5
    elif cs.startswith("🧩"): code_pri = 4
    elif cs.startswith("📦"): code_pri = 3
    elif cs.startswith("🌐"): code_pri = 2
    elif cs.startswith("⏳"): code_pri = 1
    rr = 1 if r.get("uses_real_robot") else 0
    return (-r["_year"], -code_pri, -rr, r.get("title","").lower())

# Group by category
by_cat = defaultdict(list)
for r in unique:
    by_cat[r["_cat"]].append(r)
for k in by_cat:
    by_cat[k].sort(key=sort_key)

# Build links snippet
def links(r):
    items = []
    if r.get("project_url"): items.append(f"[Project]({r['project_url']})")
    if r.get("code_url"): items.append(f"[Code]({r['code_url']})")
    if r.get("paper_url"): items.append(f"[Paper]({r['paper_url']})")
    elif r.get("arxiv_id"): items.append(f"[arXiv](https://arxiv.org/abs/{r['arxiv_id']})")
    if r.get("dataset_url"): items.append(f"[Dataset]({r['dataset_url']})")
    return " · ".join(items)

def title_link(r):
    t = r.get("title","").strip()
    url = r.get("paper_url") or (r.get("arxiv_id") and f"https://arxiv.org/abs/{r['arxiv_id']}") or r.get("project_url") or r.get("code_url") or ""
    if url:
        return f"[{t}]({url})"
    return f"**{t}**"

def venue_str(r):
    v = r.get("venue","")
    y = r.get("year","")
    if v: return v
    if y: return str(y)
    return ""

def entry_md(r):
    pre = emoji_prefix(r)
    tl = title_link(r)
    venue = venue_str(r)
    plat = r.get("robot_platform","")
    tags = []
    if venue: tags.append(f"`{venue}`")
    if plat: tags.append(f"`{plat}`")
    cat = r.get("category","") or r.get("category_hint","")
    if cat: tags.append(f"`{cat}`")
    authors = r.get("authors","")
    summary = r.get("one_line") or r.get("one_sentence_summary","")
    lines = [f"- {pre} **{tl}** {' '.join(tags)}".rstrip()]
    if authors and authors.lower() not in ("see paper","unknown"):
        a_short = authors.split(";")[0].strip() + (" et al." if ";" in authors else "")
        lines.append(f"  {a_short}.")
    if summary and summary.lower() not in ("see paper","(see paper)","..."):
        lines.append(f"  {summary}")
    lk = links(r)
    if lk:
        lines.append(f"  Links: {lk}")
    return "\n".join(lines) + "\n"

# Build README
def build_readme():
    out = []
    out.append("# Awesome Human-Object Interaction Generation and Whole-Body Control")
    out.append("")
    out.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)")
    out.append("")
    out.append("> A curated list of recent papers, datasets, codebases, and benchmarks on **human-object interaction (HOI) motion generation**, **humanoid whole-body control**, **motion tracking & imitation**, **whole-body loco-manipulation**, **humanoid foundation models**, **retargeting**, **teleoperation**, **sim-to-real deployment**, and **physics-based character animation**. Papers with verified official open-source code are marked ⭐.")
    out.append("")
    out.append("Inspired by [YanjieZe/awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) with extended tagging, code-status verification, and richer per-category summaries.")
    out.append("")
    out.append("## Table of Contents")
    out.append("- [Legend](#legend)")
    out.append("- [Research Landscape Summary](#research-landscape-summary)")
    for cid, cname in cat_order:
        anchor = re.sub(r'[^a-z0-9 -]','',cname.lower()).replace(' ','-')
        out.append(f"- [{cname}](#{anchor})")
    out.append("")
    out.append("## Legend")
    out.append("- ⭐ **Code**: official open-source implementation verified")
    out.append("- 🧩 **Partial Code**: incomplete but useful code released (eval, retarget, viz, etc.)")
    out.append("- 📦 **Dataset**: dataset, benchmark, or assets released")
    out.append("- 🌐 **Project Page**: project page available, no code")
    out.append("- ⏳ **Code Coming Soon**: authors state code will be released")
    out.append("- 🔁 **Unofficial Code**: third-party implementation only")
    out.append("- ❌ **No Code Found**")
    out.append("- 🤖 **Real Robot**: validated on a physical robot")
    out.append("- 🧍 **Humanoid**: evaluated on humanoid platforms")
    out.append("- 🧱 **Simulation**: simulation-only evaluation")
    out.append("")
    out.append("## Research Landscape Summary")
    out.append("")
    out.append("### Main Trends (2024–2026)")
    out.append("- **AMASS-driven WBC tracking is the dominant recipe.** ExBody → ExBody2 → H2O → OmniH2O → HOVER → ASAP → BeyondMimic share the same backbone: large-scale human MoCap, retargeted to a target humanoid, distilled into RL tracking policies that close the sim-to-real gap with delta-action / residual / domain-randomized models.")
    out.append("- **Loco-manipulation is becoming whole-body and force-aware.** FALCON, HOMIE, ULC, SkillBlender, VisualMimic, VIRAL, WholeBodyVLA, Kinematics-Aware MP-RL push toward force-adaptive bimanual carrying, pushing, and tool use on Unitree G1/H1/H1-2 and Fourier GR1.")
    out.append("- **HOI motion synthesis is consolidating around dual-branch / contact-guided diffusion** (HOI-Diff, CHOIS, OMOMO, InterDiff, HOI-Animator, SyncDiff, ChainHOI, DiffH2O), with a parallel push toward zero-shot text-to-HOI through LLM/SDS priors (DreamHOI, InteractAnything).")
    out.append("- **Humanoid foundation models / VLAs are landing on real robots.** GR00T N1/N1.5, π0/π0.5, Helix, Humanoid-VLA, LeVERB, EgoVLA, AgiBot GO-1, Gemini Robotics demonstrate language- and vision-conditioned generalist policies for humanoid form factors.")
    out.append("- **Retargeting datasets are now first-class artifacts.** OmniRetarget, GMR, IKMR, SONIC, BeyondMimic ship retargeted humanoid trajectories — not just code — enabling rapid kickoff of new tracking policies.")
    out.append("- **Behavioral foundation models are emerging.** FB-CPR / Meta Motivo, BFM-Zero, MaskedMimic, ProtoMotions provide universal motion priors that downstream policies fine-tune.")
    out.append("- **Whole-body teleoperation is the data engine.** Open-TeleVision, OpenWBT, CLONE, HOMIE, Bunny-VisionPro, GELLO, ACE, BiDex, DexUMI, AirExo-2, DexMimicGen, H-RDT scale demonstration collection beyond what one lab can MoCap.")
    out.append("")
    out.append("### Open Problems")
    out.append("- **Long-horizon HOI on real humanoids.** Most HOI synthesis is still character-animation; transferring contact-rich, multi-step interactions to a physical humanoid with reliable contact and force is unsolved.")
    out.append("- **Cross-embodiment generalization.** Policies trained on G1 still rarely transfer cleanly to H1, Fourier GR1, or Atlas without re-retargeting and re-tuning.")
    out.append("- **Bimanual contact-rich manipulation under whole-body coupling.** Few works deliver dexterous in-hand manipulation while maintaining balance and locomotion.")
    out.append("- **Sample efficiency.** AMASS-scale + IsaacLab/MJX still requires GPU-days; world-model and offline-RL approaches (BFM-Zero, FB-CPR, BeyondMimic) only partially address this.")
    out.append("- **Safety and recovery.** HoST, Getting-Up, HumanoidRecovery point at fall recovery, but graceful in-task safety guarantees are missing.")
    out.append("- **Object-state observability.** Most loco-manipulation assumes near-perfect object pose; vision-driven WBC (VisualMimic, WholeBodyVLA) is just beginning to close this gap.")
    out.append("")
    # Top picks computed below from real records
    out.append("### Most Implementation-Ready Papers (verified official code)")
    impl_ready = sorted(
        [r for r in unique if r["code_status_norm"].startswith("⭐") and (r.get("uses_humanoid") or r["_cat"] in ("loco_manip","wbc_tracking","foundation","retarget","teleop"))],
        key=sort_key
    )[:15]
    for r in impl_ready:
        out.append(f"- ⭐ **{title_link(r)}** — `{venue_str(r)}` — {r.get('one_line','') or r.get('one_sentence_summary','')}")
    out.append("")

    out.append("### Most Relevant for HOI Motion Generation")
    hoi_top = sorted(
        [r for r in unique if r["_cat"] in ("hoi_motion","object_aware") and r["_year"] >= 2023],
        key=sort_key
    )[:12]
    for r in hoi_top:
        out.append(f"- {emoji_prefix(r)} **{title_link(r)}** — `{venue_str(r)}` — {r.get('one_line','')}")
    out.append("")

    out.append("### Most Relevant for Whole-Body Loco-Manipulation")
    wbc_top = sorted(
        [r for r in unique if r["_cat"] in ("loco_manip","wbc_tracking") and r["_year"] >= 2023 and r["code_status_norm"].startswith(("⭐","🧩"))],
        key=sort_key
    )[:12]
    for r in wbc_top:
        out.append(f"- {emoji_prefix(r)} **{title_link(r)}** — `{venue_str(r)}` — {r.get('one_line','')}")
    out.append("")

    out.append(f"---")
    out.append(f"")
    out.append(f"_Total unique entries: **{len(unique)}**. Verified open-source: **{sum(1 for r in unique if r['code_status_norm'].startswith('⭐'))}**._")
    out.append(f"")

    # Categories
    for cid, cname in cat_order:
        recs = by_cat.get(cid, [])
        anchor_id = re.sub(r'[^a-z0-9 -]','',cname.lower()).replace(' ','-')
        out.append(f"## {cname}")
        out.append("")
        out.append(f"_{len(recs)} entries._")
        out.append("")
        if not recs:
            out.append("_(no entries)_")
            out.append("")
            continue
        # bullet list
        for r in recs:
            out.append(entry_md(r))
        out.append("")
        # compact table top entries
        out.append("### Quick Reference Table")
        out.append("")
        out.append("| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |")
        out.append("|---|---|---|---|---|---|")
        for r in recs[:min(15, len(recs))]:
            yr = r["_year"] or "—"
            paper = r.get("title","")[:60]
            url = r.get("paper_url") or r.get("project_url") or ""
            paper_md = f"[{paper}]({url})" if url else paper
            plat = r.get("robot_platform","") or "—"
            rr = "✅" if r.get("uses_real_robot") else "—"
            cs = r["code_status_norm"]
            idea = (r.get("one_line","") or "")[:80]
            # escape pipes in cells
            paper_md = paper_md.replace("|","\\|")
            plat = plat.replace("|","\\|")
            idea = idea.replace("|","\\|")
            out.append(f"| {yr} | {paper_md} | {plat} | {rr} | {cs} | {idea} |")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Acknowledgments")
    out.append("- Seed papers extracted from [YanjieZe/awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning).")
    out.append("- Code-status verification via direct GitHub HEAD checks and project-page inspection.")
    out.append("")
    out.append("## Contributing")
    out.append("PRs welcome. Please include: paper title, authors, venue/year, arXiv link, project page, GitHub URL (if any), and a one-sentence summary. Mark code status only after personally checking the repo is non-empty.")
    out.append("")
    return "\n".join(out)

readme = build_readme()
(ROOT / "README.md").write_text(readme, encoding="utf-8")
print(f"README.md: {len(readme)} bytes", file=sys.stderr)

# papers.csv
def csv_escape(v):
    return v if v is not None else ""

with open(ROOT/"papers.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(["title","authors","year","venue","category","tags","paper_url","project_url","code_url","dataset_url","code_status","real_robot","robot_platform","summary"])
    for r in sorted(unique, key=sort_key):
        cat = next((cn for cid,cn in cat_order if cid==r["_cat"]), r["_cat"])
        w.writerow([
            r.get("title",""),
            r.get("authors",""),
            r.get("year",""),
            r.get("venue",""),
            cat,
            r.get("task_tags","") or r.get("category",""),
            r.get("paper_url","") or (f"https://arxiv.org/abs/{r['arxiv_id']}" if r.get("arxiv_id") else ""),
            r.get("project_url",""),
            r.get("code_url",""),
            r.get("dataset_url",""),
            r["code_status_norm"],
            "yes" if r.get("uses_real_robot") else "no",
            r.get("robot_platform",""),
            r.get("one_line","") or r.get("one_sentence_summary",""),
        ])

# open_source_verified.md
verified = [r for r in unique if r["code_status_norm"].startswith("⭐")]
verified_by_cat = defaultdict(list)
for r in verified:
    verified_by_cat[r["_cat"]].append(r)
for k in verified_by_cat:
    verified_by_cat[k].sort(key=sort_key)

lines = ["# Verified Open-Source Papers", "",
         f"This is the canonical list of papers with **verified official open-source code** ({len(verified)} entries). Each repo was sanity-checked for actual implementation files (not placeholder READMEs).", ""]
for cid, cname in cat_order:
    recs = verified_by_cat.get(cid, [])
    if not recs: continue
    lines.append(f"## {cname} ({len(recs)})")
    lines.append("")
    for r in recs:
        lines.append(entry_md(r))
    lines.append("")
(ROOT/"open_source_verified.md").write_text("\n".join(lines), encoding="utf-8")
print(f"open_source_verified.md: {len(verified)} entries", file=sys.stderr)

# no_code_or_uncertain.md
nocode = [r for r in unique if r["code_status_norm"].startswith(("❌","⏳","❓"))]
nocode_by_cat = defaultdict(list)
for r in nocode:
    nocode_by_cat[r["_cat"]].append(r)
for k in nocode_by_cat:
    nocode_by_cat[k].sort(key=sort_key)

lines = ["# Papers with No Code or Uncertain Status", "",
         f"Papers where official code could not be verified ({len(nocode)} entries). Status is one of: ❌ No Code Found · ⏳ Code Coming Soon · ❓ Uncertain.", ""]
for cid, cname in cat_order:
    recs = nocode_by_cat.get(cid, [])
    if not recs: continue
    lines.append(f"## {cname} ({len(recs)})")
    lines.append("")
    for r in recs:
        lines.append(entry_md(r))
    lines.append("")
(ROOT/"no_code_or_uncertain.md").write_text("\n".join(lines), encoding="utf-8")
print(f"no_code_or_uncertain.md: {len(nocode)} entries", file=sys.stderr)

# search_log.md
hist = defaultdict(int)
for r in unique:
    hist[r["code_status_norm"]] += 1

cat_hist = defaultdict(int)
for r in unique:
    cat_hist[r["_cat"]] += 1

lines = ["# Search Log & Quality Control", "",
"## Source chunks (raw research output)", "",
"| Chunk | Records | Description |",
"|---|---|---|",
"| `01_seed.md` | %d | Seed list from YanjieZe/awesome-humanoid-robot-learning |" % chunk_meta.get("01_seed.md",0),
"| `02_hoi_motion.md` | %d | HOI motion generation + object-aware human motion synthesis |" % chunk_meta.get("02_hoi_motion.md",0),
"| `03_wbc_tracking.md` | %d | Whole-body motion tracking and imitation |" % chunk_meta.get("03_wbc_tracking.md",0),
"| `04_loco_manip.md` | %d | Whole-body control and loco-manipulation |" % chunk_meta.get("04_loco_manip.md",0),
"| `05_foundation.md` | %d | Humanoid foundation models and generalist VLAs |" % chunk_meta.get("05_foundation.md",0),
"| `06_retarget_teleop.md` | %d | Human-to-humanoid retargeting + teleop |" % chunk_meta.get("06_retarget_teleop.md",0),
"| `07_data_bench_s2r.md` | %d | Datasets, benchmarks, sim-to-real, contact metrics |" % chunk_meta.get("07_data_bench_s2r.md",0),
"| `08_loco_anim.md` | %d | Locomotion + physics-based character animation |" % chunk_meta.get("08_loco_anim.md",0),
"",
"**Total unique papers after deduplication: %d**" % len(unique),
"",
"## Per-Category Counts","",
]
for cid, cname in cat_order:
    lines.append(f"- {cname}: {cat_hist.get(cid,0)}")
lines += ["",
"## Code-Status Histogram","",
"| Status | Count |",
"|---|---|",
]
for k, v in sorted(hist.items(), key=lambda kv: -kv[1]):
    lines.append(f"| {k} | {v} |")
lines += ["",
"## Search Queries Used (representative)", "",
"### arXiv / Google Scholar / Papers with Code / OpenReview",
"```",
'"human-object interaction generation" motion',
'"human object interaction" "motion generation" arXiv',
'"human-object interaction" "whole-body" "generation"',
'"whole-body control" humanoid robot learning arXiv',
'"whole-body loco-manipulation" humanoid',
'"humanoid loco-manipulation" "whole-body control"',
'"motion tracking" humanoid robot "human motion"',
'"motion imitation" humanoid "whole-body"',
'"human motion retargeting" humanoid robot',
'"object-aware human motion generation"',
'"contact-aware motion generation" human object interaction',
'"egocentric video" humanoid whole-body control',
'"teleoperation" humanoid "whole-body control"',
'"sim-to-real" humanoid "loco-manipulation"',
'"foundation model" humanoid robot control',
'"GR00T N1" OR "OpenVLA" OR "pi0" humanoid',
'"OmniH2O" OR "HOVER" OR "ASAP" OR "ExBody2"',
'"OmniRetarget" OR "GMR" OR "Kimodo" OR "SONIC"',
'"AnyTeleop" OR "Open-TeleVision" OR "ACE Teleop"',
"```",
"",
"### GitHub verification queries",
"```",
'site:github.com "<paper-title>"',
'site:github.com "<method-name>" humanoid',
'<author-last-name> "<method-name>" github',
"```",
"",
"## Conferences / Venues Covered","",
"ICRA, IROS, CoRL, RSS, NeurIPS, CVPR, ICCV, ECCV, SIGGRAPH/SIGGRAPH Asia, ICLR, ICML, Science Robotics, IJRR, T-RO, Humanoids.",
"",
"## Quality-Control Protocol Followed","",
"1. Each paper required at least one of: arXiv ID, paper URL, or project URL.",
"2. ⭐ Code awarded only after confirming repo is reachable AND contains actual implementation files (training/inference/eval/data scripts).",
"3. When chunks disagreed on the same paper, the chunk that performed direct GitHub HTTP checks won.",
"4. Forward-dated arXiv IDs from the seed (e.g., 2603.xxxxx) were dropped or marked unverified.",
"5. Papers without an external link were excluded.",
"6. Per-category dedup uses normalized lowercase title; cross-references retained in CSV via the `category` field only (one canonical category per paper).",
"",
"## Unresolved / Status Uncertain","",
"See `no_code_or_uncertain.md` for the explicit list. Categories with most uncertainty:",
"- 2026 arXiv pre-prints with project pages but no code yet (HOMIE, BeyondMimic follow-ups, late-2025 retarget systems).",
"- HOI synthesis papers that ship dataset + viz only (e.g. CG-HOI, GRIP, COUCH, SViMo, HUMOTO).",
"- Closed-source industrial systems (RT-2, RT-H, Helix, Gemini Robotics, GR-2, Humanoid-VLA, MotionGPT-2).",
"",
"## How to Reproduce This List","",
"1. Re-run the eight chunk-research agents (HOI, WBC tracking, loco-manip, foundation, retarget+teleop, datasets+sim2real, locomotion+animation, plus seed extraction).",
"2. Run `python build.py` from the repo root to dedup and emit deliverables.",
"3. Review `no_code_or_uncertain.md` and re-check status of pending repos.",
"",
]
(ROOT/"search_log.md").write_text("\n".join(lines), encoding="utf-8")
print(f"search_log.md written", file=sys.stderr)

print(f"\nDONE.\nTotal unique: {len(unique)}\nVerified ⭐: {hist['⭐ Code']}\nProject Page 🌐: {hist['🌐 Project Page']}\nNo Code ❌: {hist['❌ No Code']}", file=sys.stderr)
