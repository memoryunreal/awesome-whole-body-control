# Search Log & Quality Control

## Source chunks (raw research output)

| Chunk | Records | Description |
|---|---|---|
| `01_seed.md` | 201 | Seed list from YanjieZe/awesome-humanoid-robot-learning |
| `02_hoi_motion.md` | 82 | HOI motion generation + object-aware human motion synthesis |
| `03_wbc_tracking.md` | 68 | Whole-body motion tracking and imitation |
| `04_loco_manip.md` | 61 | Whole-body control and loco-manipulation |
| `05_foundation.md` | 51 | Humanoid foundation models and generalist VLAs |
| `06_retarget_teleop.md` | 52 | Human-to-humanoid retargeting + teleop |
| `07_data_bench_s2r.md` | 87 | Datasets, benchmarks, sim-to-real, contact metrics |
| `08_loco_anim.md` | 55 | Locomotion + physics-based character animation |

**Total unique papers after deduplication: 458**

## Per-Category Counts

- Human-Object Interaction Motion Generation: 43
- Object-Aware Human Motion Synthesis: 26
- Whole-Body Motion Tracking and Imitation: 113
- Whole-Body Control and Loco-Manipulation: 55
- Humanoid Foundation Models and Generalist Policies: 65
- Human-to-Humanoid Retargeting: 7
- Teleoperation and Demonstration Collection: 30
- Datasets and Benchmarks: 61
- Evaluation Metrics and Contact Modeling: 10
- Sim-to-Real and Deployment Systems: 24
- Related Character Animation and Physics-Based Motion Generation: 24

## Code-Status Histogram

| Status | Count |
|---|---|
| ⭐ Code | 208 |
| ❌ No Code | 125 |
| 🌐 Project Page | 103 |
| 📦 Dataset | 13 |
| 🧩 Partial Code | 7 |
| ⏳ Code Coming Soon | 1 |
| 🔁 Unofficial Code | 1 |

## Search Queries Used (representative)

### arXiv / Google Scholar / Papers with Code / OpenReview
```
"human-object interaction generation" motion
"human object interaction" "motion generation" arXiv
"human-object interaction" "whole-body" "generation"
"whole-body control" humanoid robot learning arXiv
"whole-body loco-manipulation" humanoid
"humanoid loco-manipulation" "whole-body control"
"motion tracking" humanoid robot "human motion"
"motion imitation" humanoid "whole-body"
"human motion retargeting" humanoid robot
"object-aware human motion generation"
"contact-aware motion generation" human object interaction
"egocentric video" humanoid whole-body control
"teleoperation" humanoid "whole-body control"
"sim-to-real" humanoid "loco-manipulation"
"foundation model" humanoid robot control
"GR00T N1" OR "OpenVLA" OR "pi0" humanoid
"OmniH2O" OR "HOVER" OR "ASAP" OR "ExBody2"
"OmniRetarget" OR "GMR" OR "Kimodo" OR "SONIC"
"AnyTeleop" OR "Open-TeleVision" OR "ACE Teleop"
```

### GitHub verification queries
```
site:github.com "<paper-title>"
site:github.com "<method-name>" humanoid
<author-last-name> "<method-name>" github
```

## Conferences / Venues Covered

ICRA, IROS, CoRL, RSS, NeurIPS, CVPR, ICCV, ECCV, SIGGRAPH/SIGGRAPH Asia, ICLR, ICML, Science Robotics, IJRR, T-RO, Humanoids.

## Quality-Control Protocol Followed

1. Each paper required at least one of: arXiv ID, paper URL, or project URL.
2. ⭐ Code awarded only after confirming repo is reachable AND contains actual implementation files (training/inference/eval/data scripts).
3. When chunks disagreed on the same paper, the chunk that performed direct GitHub HTTP checks won.
4. Forward-dated arXiv IDs from the seed (e.g., 2603.xxxxx) were dropped or marked unverified.
5. Papers without an external link were excluded.
6. Per-category dedup uses normalized lowercase title; cross-references retained in CSV via the `category` field only (one canonical category per paper).

## Unresolved / Status Uncertain

See `no_code_or_uncertain.md` for the explicit list. Categories with most uncertainty:
- 2026 arXiv pre-prints with project pages but no code yet (HOMIE, BeyondMimic follow-ups, late-2025 retarget systems).
- HOI synthesis papers that ship dataset + viz only (e.g. CG-HOI, GRIP, COUCH, SViMo, HUMOTO).
- Closed-source industrial systems (RT-2, RT-H, Helix, Gemini Robotics, GR-2, Humanoid-VLA, MotionGPT-2).

## How to Reproduce This List

1. Re-run the eight chunk-research agents (HOI, WBC tracking, loco-manip, foundation, retarget+teleop, datasets+sim2real, locomotion+animation, plus seed extraction).
2. Run `python build.py` from the repo root to dedup and emit deliverables.
3. Review `no_code_or_uncertain.md` and re-check status of pending repos.

## Weekly Digest Runs

### 2026-05-07 — 3 new, 0 updated
- Window: 2026-04-30 → 2026-05-07.
- Sources searched: arXiv listings (cs.RO, cs.CV, cs.GR), Google web search, project pages.
- Queries: "humanoid whole-body control 2026", "arxiv 2605 humanoid robot motion tracking", "human motion generation diffusion 2026", "arxiv humanoid retargeting teleoperation 2026", plus existing query bank.
- New entries (added to chunks 04 and 05):
  - MolmoAct 2 (2605.02881) — AI2/UW; 🧩 Partial Code; Foundation.
  - SigLoMa (2605.03846) — Tsinghua; 🌐 Project Page; quadrupedal Loco-Manipulation.
  - BifrostUMI (2605.03452) — affiliations unverified; ❌ No Code; humanoid Loco-Manipulation.
- Existing-paper updates: none verified (no v2/v3 revisions or new code releases observed for the 455 prior entries).
- Unresolved code-status items:
  - https://arxiv.org/abs/2605.03846 — SigLoMa "Code" link is a placeholder ("#"); recheck next week.
  - https://arxiv.org/abs/2605.03452 — BifrostUMI has no project page or repo yet.
- Notion escalations (tier-1 affiliation): MolmoAct 2, SigLoMa.
- Inspected but excluded: 2605.03363 (Reactive Dexterous Grasping, MIT — tabletop arm+hand, out of humanoid-WBC scope), 2605.02742 (Adaptive Interpolation-Synthesis, SIGGRAPH 2026 — production keyframe tooling, affiliations unverified, weak fit), 2605.02600 (CoRAL — generic tabletop manipulation), 2605.02347 (ShapeGrasp — visuo-haptic grasping). InterPhys (2605.01036) already in CSV.

