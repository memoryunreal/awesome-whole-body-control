# Search Log & Quality Control

## Source chunks (raw research output)

| Chunk | Records | Description |
|---|---|---|
| `01_seed.md` | 201 | Seed list from YanjieZe/awesome-humanoid-robot-learning |
| `02_hoi_motion.md` | 88 | HOI motion generation + object-aware human motion synthesis |
| `03_wbc_tracking.md` | 96 | Whole-body motion tracking and imitation |
| `04_loco_manip.md` | 83 | Whole-body control and loco-manipulation |
| `05_foundation.md` | 63 | Humanoid foundation models and generalist VLAs |
| `06_retarget_teleop.md` | 67 | Human-to-humanoid retargeting + teleop |
| `07_data_bench_s2r.md` | 93 | Datasets, benchmarks, sim-to-real, contact metrics |
| `08_loco_anim.md` | 60 | Locomotion + physics-based character animation |

**Total unique papers after deduplication: 552**

## Per-Category Counts

- Human-Object Interaction Motion Generation: 49
- Object-Aware Human Motion Synthesis: 26
- Whole-Body Motion Tracking and Imitation: 141
- Whole-Body Control and Loco-Manipulation: 77
- Humanoid Foundation Models and Generalist Policies: 77
- Human-to-Humanoid Retargeting: 15
- Teleoperation and Demonstration Collection: 37
- Datasets and Benchmarks: 66
- Evaluation Metrics and Contact Modeling: 10
- Sim-to-Real and Deployment Systems: 25
- Related Character Animation and Physics-Based Motion Generation: 29

## Code-Status Histogram

| Status | Count |
|---|---|
| ⭐ Code | 226 |
| ❌ No Code | 162 |
| 🌐 Project Page | 129 |
| 📦 Dataset | 14 |
| ⏳ Code Coming Soon | 12 |
| 🧩 Partial Code | 8 |
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

### 2026-07-24 — 5 new, 0 updated
- Window: 2026-07-17 → 2026-07-24.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, and cs.GR filtered by submittedDate; arXiv API lastUpdatedDate pass over known chunk arXiv IDs; arXiv abstract/HTML pages; project pages; GitHub search results; GitHub `ls-remote`; GitHub tree/content checks for implementation files.
- Query focus: humanoid whole-body control, general motion tracking, humanoid VLA post-training, retail humanoid deployment, miniature humanoid tele-loco-manipulation, embodied foundation models, recovery from human demonstrations, biped navigation, bimanual object interaction, and HOI generation.
- New entries by source chunk:
  - `03_wbc_tracking.md` — 2 entries: What Matters in Humanoid General Motion Tracking? (2607.19903), Extreme-RGMT (2607.20110).
  - `05_foundation.md` — 2 entries: RynnBrain 1.1 (2607.17977), Closing the Lab-to-Store Gap (2607.20345).
  - `06_retarget_teleop.md` — 1 entry: Towards Miniature Humanoid Tele-Loco-Manipulation (2607.20399).
- Verified official code repos:
  - https://github.com/hucebot/yahmp
  - https://github.com/alibaba-damo-academy/RynnBrain
  - https://github.com/alibaba-damo-academy/RynnScale
- Existing-paper updates: none verified. A lastUpdatedDate pass over existing arXiv IDs in cs.RO/cs.CV/cs.LG/cs.GR found only v1 records already added in the 2026-07-22 run, with no new revisions or code-status changes.
- Unresolved code-status items:
  - https://zeonsunlightyu.github.io/Extreme-RGMT.github.io/ — project page is reachable, but the surfaced GitHub repository is website/media only.
  - https://arxiv.org/abs/2607.20345 — no project page or code repository found for DEED / Closing the Lab-to-Store Gap.
  - https://arxiv.org/abs/2607.20399 — no project page or code repository found for the miniature humanoid tele-loco-manipulation stack.
  - https://github.com/EgoRecovery/EgoRecovery — linked from the arXiv HTML for EgoRecovery, but returned 404 during inspection.
- Inspected but excluded: EgoRecovery (2607.19745, recovery from egocentric human demonstrations but no humanoid or whole-body-control specificity found, and linked repo returned 404), ZONDA (2607.21025, biped object navigation but not humanoid WBC/loco-manipulation), URF (2607.20912, generic contact-aware manipulation), BiCompoDiff (2607.21341, bimanual manipulation without humanoid/HOI-motion-generation focus), AXIS (2607.21588, broad manipulation data engine), Emergent Compositional Skills in MoE VLAs (2607.20771, generic VLA), StreamHOI (2607.20174, HOI video generation rather than 3D motion/control), Agentic Real2Sim (2607.19190, broad real2sim world modeling), Koopman DCM (2607.18760, biped balancing primitive rather than whole-body humanoid list fit), NICO sim-to-real and gesture-imitation papers (2607.18210, 2607.18197), Motion Primitive Discovery in NICO (2607.18737), and broad navigation, manipulation, driving, UAV, medical, remote-sensing, and foundation-model papers matched only by generic keywords.
- Notion escalations: not run in this repo-only update.

### 2026-07-22 — 9 new, 0 updated
- Window: 2026-07-15 → 2026-07-22.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, and cs.GR filtered by submittedDate; arXiv API lastUpdatedDate pass for existing-paper revisions; arXiv abstract/HTML pages; project pages; GitHub search results; GitHub `ls-remote` and GitHub contents checks for implementation files.
- Query focus: humanoid whole-body control, humanoid behavior foundation models, humanoid VLA loco-manipulation, humanoid navigation with MPC/RL, humanoid teleoperation/retargeting, reconfigurable dexterous humanoid hardware, terrain-traversal datasets, and multi-view HOI synthesis.
- New entries by source chunk:
  - `02_hoi_motion.md` — 1 entry: HarmoHOI (2607.17097).
  - `03_wbc_tracking.md` — 2 entries: Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control (2607.14182), RAVEN (2607.15701).
  - `04_loco_manip.md` — 2 entries: Handroid (2607.16187), FARO (2607.18362).
  - `05_foundation.md` — 2 entries: Scaling Behavior Foundation Model for Humanoid Robots (2607.15163), Closing the Loop in Humanoid VLA (2607.18016).
  - `06_retarget_teleop.md` — 1 entry: From Sign Language Generation to Humanoid Execution (2607.17769).
  - `07_data_bench_s2r.md` — 1 entry: EgoHTR (2607.13472).
- Verified official code repos:
  - https://github.com/Lab-RoCoCo-Sapienza/semantic-WBC
- Existing-paper updates: none verified. A lastUpdatedDate pass over existing arXiv IDs in cs.RO/cs.CV/cs.LG/cs.GR found no previously tracked paper with a new revision in the 2026-07-15 → 2026-07-22 window.
- Unresolved code-status items:
  - https://egohtr.github.io — project page has placeholder Dataset and Code buttons marked coming soon, so EgoHTR is `⏳ Code Coming Soon`.
  - https://droliven.github.io/HarmoHOI_project/ — project page links https://github.com/Droliven/HarmoHOI_project, but that repository is website-only and says models/dataset are coming soon.
  - https://handroid.org/ — project page exposes CAD/BOM links, but no method code repository was reachable.
  - https://github.com/Atarilab/faro.io — reachable official FARO webpage repository, not a method implementation.
  - https://arxiv.org/abs/2607.15163 — no project page or code repository found for Scaling Behavior Foundation Model.
  - https://arxiv.org/abs/2607.18016 — no project page or code repository found for POT-VLA / Closing the Loop in Humanoid VLA.
  - https://arxiv.org/abs/2607.15701 — no project page or code repository found for RAVEN.
  - https://arxiv.org/abs/2607.17769 — no project page or code repository found for the sign-language-to-humanoid retargeting system.
- Inspected but excluded: Let the Body Follow (2607.16095, whole-body teleoperation on a TIAGo mobile manipulator rather than humanoid WBC), Human4K (2607.13646, whole-body human reconstruction dataset without robot-control or HOI-generation focus), EgoExoMoCap (2607.15868, general HMD mocap rather than humanoid retarget/control), Reverse to Advance (2607.13455, generic teleoperation-cost reduction for manipulation), Open-AoE (2607.14183, broad egocentric manipulation dataset/toolchain without humanoid specificity), AHEAD (2607.15172, generic hand-driven teleoperation), MIDAS Hand (2607.14487), VTAP Gripper (2607.15448), Optimization of sim-to-real transfer in NICO (2607.18210, semi-humanoid tabletop grasping calibration rather than whole-body control), Imitation of Arm Gestures by NICO (2607.18197), Motion Primitive Discovery in a Humanoid Robot (2607.18737, phase recognition/HRI rather than control), Agentic Real2Sim (2607.19190, broad real2sim world modeling), World Translation (2607.18154, broad sim-to-real dynamics transfer), Safe Execution of RL Policies via Acc-CBF-QP (2607.14488, general safety filter), Human-object Centric Video Personalization (2607.18217, video personalization), HOI detection / activity-recognition papers such as 2607.13881 and 2607.14350, broad VLA manipulation/driving/UAV papers, and medical/remote-sensing/foundation-model papers matched only by generic keywords.
- Notion escalations: not run in this repo-only update.

### 2026-07-03 — 14 new, 0 updated
- Window: 2026-06-27 → 2026-07-03.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, cs.GR filtered by submittedDate; arXiv API listings filtered by lastUpdatedDate for existing-paper revisions; arXiv abstract metadata and comments; project pages; GitHub repository search; GitHub `ls-remote` and GitHub tree checks for implementation files.
- Query focus: humanoid whole-body control, free-form keypoint tracking, reactive humanoid BFMs, humanoid loco-manipulation, human-video transfer, humanoid VLA data conversion, whole-body retargeting, heavy-payload teleoperation, humanoid dexterous datasets, sim-to-real actuator interfaces, HOI contact generation, and physics-based character imitation.
- New entries by source chunk:
  - `02_hoi_motion.md` — 1 entry: JointHOI (2607.01768).
  - `03_wbc_tracking.md` — 4 entries: AnyBody (2606.29209), ReactiveBFM (2606.30362), FastDSAC (2606.31691), Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot (2606.31807).
  - `04_loco_manip.md` — 2 entries: Human2Any (2606.28813), VLK (2606.30645).
  - `05_foundation.md` — 1 entry: Human-as-Humanoid (2606.32009).
  - `06_retarget_teleop.md` — 1 entry: HEFT (2607.02332).
  - `07_data_bench_s2r.md` — 3 entries: Labimus (2606.31037), RoboTacDex (2606.31836), Actuator Reality Shaping (2607.02205).
  - `08_loco_anim.md` — 2 entries: GPC (2606.29148), ComplexMimic (2607.02034).
- Verified official code repos:
  - https://github.com/luge66/FastDSAC
- Existing-paper updates: none verified. A lastUpdatedDate pass over existing arXiv IDs in cs.RO/cs.CV/cs.LG/cs.GR found no previously tracked paper with a new revision in the 2026-06-27 → 2026-07-03 window.
- Unresolved code-status items:
  - https://xiao-chen.tech/reactivebfm/ — project page links https://github.com/zjwzcx/ReactiveBFM, but the repository only contained a README/TODO at inspection time, so status is `⏳ Code Coming Soon`.
  - https://vision-language-kinematics.github.io/ — project page says code coming soon; only the website repository was visible.
  - https://zgc-embodyai.github.io/Human-as-Humanoid — linked GitHub repository contains website/media assets only, so status remains `🌐 Project Page`.
  - https://github.com/LuPan23/ComplexMimic — repository reachable, but only README/LICENSE were present at inspection time, so status remains `🌐 Project Page`.
  - https://human2any.github.io/ — project page still contains placeholder GitHub/dataset URLs.
  - https://heft.axell.top/ — project page found, but no code repository surfaced.
  - https://labimus.github.io/ — project page found, but no dataset/code release link surfaced.
  - https://arxiv.org/abs/2606.29209 — no project or code repository found for AnyBody.
  - https://arxiv.org/abs/2606.31807 — result video found, but no code repository found for the inline-skating humanoid controller.
  - https://arxiv.org/abs/2606.31836 — paper says the RoboTacDex dataset will be open-sourced soon, but no dataset URL was available.
  - https://arxiv.org/abs/2607.01768 — no project or code repository found for JointHOI.
  - https://arxiv.org/abs/2606.29148 — no project or code repository found for GPC.
  - https://arxiv.org/abs/2607.02205 — no project or code repository found for Actuator Reality Shaping.
- Inspected but excluded: CoGS (2606.28820, human-object scene reconstruction rather than HOI generation/control), WARP (2606.29940, whole-body mobile-manipulation retargeting but not humanoid), X-Morph (2606.30290, cross-morphology transfer primarily to non-humanoid legged robots), KYON (2606.30243, quadruped/wheel-legged platform rather than humanoid), ViDiHand (2606.30308, hand-motion reconstruction code promised but no robot-action or HOI-generation target), EPIC-Contact (2606.30598, hand-object pose estimation/perception), From Grasps to Dexterity (2606.30749, dexterous tool-use pretraining but not humanoid/HOI generation), VT-WAM (2607.02503), H-Tac (2607.01067), UniTacVLA (2606.31723), TAP-VLA (2606.29089), FurnitureVLA (2607.01212), and other broad tactile/VLA/mobile-manipulation/navigation/aerial/medical/remote-sensing/world-model papers matched only by generic manipulation or embodied-AI terms.
- Notion escalations: not run in this manual repo-only update.

### 2026-06-27 — 20 new, 1 updated
- Window: 2026-06-20 → 2026-06-27.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, cs.GR filtered by submittedDate; arXiv abstract pages for external project links; project pages; GitHub repository search; GitHub `git/trees/HEAD` checks for implementation files; Hugging Face dataset/model landing pages linked from project pages.
- Query focus: humanoid whole-body control, humanoid loco-manipulation, controller-aware humanoid motion generation, humanoid VLA locomotion, HOI generation, dexterous hand-object retargeting, robot-free humanoid demonstration collection, humanoid perception datasets, physics-based motion tracking.
- New entries by source chunk:
  - `02_hoi_motion.md` — 2 entries: IMAGIN-4D (2606.23675), Policy-as-Data (2606.22806).
  - `03_wbc_tracking.md` — 5 entries: TEXEDO (2606.22998), LP-NavOA (2606.23249), RGB (2606.25123), Asynchronous Upper-body Tracking (2606.25706), PressMimic (2606.26741).
  - `04_loco_manip.md` — 6 entries: OpenHLM (2606.22174), CoorDex (2606.23680), OmniContact (2606.26201), TaskNPoint (2606.26215), A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots (2606.26425), Humanoid-DART (2606.26855).
  - `05_foundation.md` — 1 entry: WOLF-VLA (2606.25591).
  - `06_retarget_teleop.md` — 3 entries: Wh0 (2606.22136), DexTeleop-0 (2606.23431), HumanoidUMI (2606.27239).
  - `07_data_bench_s2r.md` — 1 entry: Humanoid-OmniOcc (2606.22971).
  - `08_loco_anim.md` — 2 entries: BFMTrack (2606.25056), ICMPG (2606.26981).
- Verified official code repos:
  - https://github.com/JianuoCao/TEXEDO
  - https://github.com/Skevinci/CoorDex
  - https://github.com/chenyt31/Wh0
- Existing-paper updates:
  - TopoRetarget (2606.16272) — arXiv revised to `v2` on 2026-06-22; project page still surfaced only the paper/project assets, so code status remains `🌐 Project Page`.
- Unresolved code-status items:
  - https://imagin4d.github.io — project page says code/models will be released, but no repository was available at inspection time.
  - https://openhlm-project.github.io/ — dataset and checkpoint links are live, but the Code button was still a placeholder (`#`) and GitHub search did not surface a method repo.
  - https://d-robotics-ai-lab.github.io/humanoid-omniocc — project page says code/data coming soon.
  - https://toporetarget2026.github.io/TopoRetarget/ — still project-page only after the v2 arXiv revision.
  - https://arxiv.org/abs/2606.22806 — no project or code repository found for Policy-as-Data.
  - https://arxiv.org/abs/2606.23249 — no project or code repository found for LP-NavOA.
  - https://arxiv.org/abs/2606.25123 — no project or code repository found for RGB.
  - https://arxiv.org/abs/2606.25706 — no project or code repository found for asynchronous upper-body tracking.
  - https://arxiv.org/abs/2606.26741 — no project or code repository found for PressMimic.
  - https://arxiv.org/abs/2606.26201 — no project, dataset, or code repository found for OmniContact.
  - https://arxiv.org/abs/2606.26215 — no project or code repository found for TaskNPoint.
  - https://arxiv.org/abs/2606.26425 — dissertation links a video playlist, but no code repository was found.
  - https://arxiv.org/abs/2606.26855 — no project or code repository found for Humanoid-DART.
  - https://arxiv.org/abs/2606.25591 — WOLF-VLA promises open dataset/model/benchmark release, but no project or repository was found.
  - https://arxiv.org/abs/2606.23431 — no project or code repository found for DexTeleop-0.
  - https://arxiv.org/abs/2606.27239 — no project or code repository found for HumanoidUMI.
  - https://arxiv.org/abs/2606.25056 — no project or code repository found for BFMTrack.
  - https://arxiv.org/abs/2606.26981 — no project or code repository found for ICMPG.
- Inspected but excluded: Scalable Behavior Cloning / ABC (2606.27375, broad manipulation stack without humanoid WBC/HOI focus), VibeAct (2606.27344, dexterous tactile manipulation but not humanoid or HOI generation), FT-WBC (2606.24466, legged manipulator fault tolerance rather than humanoid WBC), HoloAgent-0 (2606.23565, broad agent framework with only loose humanoid-control coupling), LIBERO-Safety (2606.23686, broad VLA safety benchmark), LaST-HD (2606.23685, generic hand-to-robot reasoning outside humanoid/HOI generation scope), AutoDex (2606.23689, dexterous grasp data collection), APR Pianist (2606.23848, dexterous piano-playing hand control), Social Structure HHI (2606.24255, human-human interaction rather than human-object/humanoid control), MANGO (2606.24815, VLA testing/oracle generation), DynaMOMA (2606.25295, mobile manipulation without humanoid focus), Supervise What Survives (2606.24448, broad VLA adaptation from generated robot videos), ABC/WatchAct/SSI-Policy/Play2Perfect and other generic manipulation, medical, remote-sensing, traffic, and world-model papers matched only by generic terms.
- Notion escalations: not run in this manual repo-only update.

### 2026-06-18 — 12 new, 0 updated
- Window: 2026-06-11 → 2026-06-18.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, cs.GR filtered by submittedDate; arXiv HTML/abstract pages for project links; project pages; GitHub `ls-remote` and GitHub tree checks for implementation files; targeted web search for missing project/code pages.
- Query focus: humanoid whole-body control, humanoid locomotion robustness, loco-manipulation, humanoid VLA/motion generation, HOI motion generation, hand-object retargeting, teleoperation/data collection, egocentric humanoid benchmarks, physics-based robot gesture generation.
- New entries by source chunk:
  - `02_hoi_motion.md` — 2 entries: MOCHI (2606.18243), DragMesh-2 (2606.15133).
  - `03_wbc_tracking.md` — 3 entries: ADAPT (2606.16542), VENOM (2606.16696), Whole-Body Impedance MPC (2606.14617).
  - `04_loco_manip.md` — 1 entries: ROVE (2606.17011).
  - `05_foundation.md` — 1 entries: MotionVLA (2606.15142).
  - `06_retarget_teleop.md` — 3 entries: Universal Manipulation Exoskeleton (2606.14218), TopoRetarget (2606.16272), EgoInfinity (2606.17385).
  - `07_data_bench_s2r.md` — 1 entries: HumanoidArena (2606.17833).
  - `08_loco_anim.md` — 1 entries: WaveSync (2606.16600).
- Verified official code repos:
  - https://github.com/AIGeeksGroup/DragMesh-2
  - https://github.com/AIGeeksGroup/MotionVLA
  - https://github.com/pairs-lab/WaveSync
- Existing-paper updates: none verified. No existing arXiv IDs in the current window had a new post-2026-06-12 revision or confirmed new code release that changed repository status.
- Unresolved code-status items:
  - https://jiyewise.github.io/projects/MOCHI/ — project page links https://github.com/jiyewise/MOCHI, but the repo contained only README/assets at inspection time, so status is `🌐 Project Page`.
  - https://xpeng-robotics.github.io/rove — project page and arXiv link found, but no code repository found.
  - https://blyu413.github.io/adapt-locomotion/ — project page found, but no method code repository found.
  - https://humanoidarena.github.io — project page repository is website/media assets only, so status is `🌐 Project Page`.
  - https://toporetarget2026.github.io/TopoRetarget/ — project page found; only web-page repository surfaced, so status is `🌐 Project Page`.
  - https://huggingface.co/spaces/Rice-RobotPI-Lab/EgoInfinity — arXiv-linked Space returned unauthorized in unauthenticated check; no separate code repo verified.
  - https://ume-exo.github.io/ — project page found, but no method code repository found.
  - https://arxiv.org/abs/2606.16696 — no project or code repository found for VENOM.
  - https://arxiv.org/abs/2606.14617 — no project or code repository found for Whole-Body Impedance MPC.
- Inspected but excluded: ORCA (2606.14561, dexterous-hand platform rather than HOI generation or humanoid WBC), Mana (2606.13677, articulated-tool dexterous manipulation but not humanoid whole-body), GeoHAT (2606.13394, mobile-base manipulation without humanoid focus), SimWeaver (2606.15338, deformable manipulation VLA outside humanoid/HOI scope), SAPS (2606.15568, generic VLA steering), V2P-Manip (2606.16436, dexterous manipulation from video without whole-body humanoid focus), MimicIK (2606.15148, useful IK/teleop primitive but no project/code and weaker fit), HATS (2606.16491, multi-arm data collection outside humanoid WBC), EBench (2606.18239, mobile manipulation benchmark), Qwen-RobotManip (2606.17846, broad manipulation foundation model), GeneralVLA-2 (2606.17480, broad VLA planning), GASE/MagicSim/AnnotateAnything (2606.17520/2606.17511/2606.17446, general simulation infrastructure), and broad medical/remote-sensing/world-model/security papers matched only by generic terms.
- Notion escalations: not run in this manual repo-only update.

### 2026-06-12 — 34 new, 1 updated
- Window: 2026-05-07 → 2026-06-12.
- Sources searched: arXiv API listings for cs.RO, cs.CV, cs.LG, cs.GR filtered by submittedDate; project pages from arXiv comments; GitHub repository HEAD/tree checks; targeted web search for missing code links.
- Query focus: humanoid, whole-body control, loco-manipulation, humanoid-object interaction, motion tracking/imitation, fall recovery, retargeting, teleoperation, egocentric humanoid control, humanoid VLA, WAM, sim-to-real.
- New entries by source chunk:
  - `03_wbc_tracking.md` — 12 entries: Stubborn (2606.12814), RoboNaldo (2606.11092), PTDL (2606.08922), EgoPriMo (2606.08495), Mind Your Steps (2606.08253), Predictive Style Matching (2606.07083), LIMMT (2606.06953), LadderMan (2606.05873), M3imic (2606.04829), Bionic Style Transfer (2606.03536), MIND (2605.26006), SCRIPT (2605.22894).
  - `04_loco_manip.md` — 11 entries: WT-UMI (2606.13232), GenHOI (2606.12995), Critic Architecture Matters (2606.11891), VAIC (2606.09286), OASIS (2606.08548), SIMPLE (2606.08278), MotionDisco (2606.06139), HANDOFF (2606.06493), MPC-RL (2606.05687), GRAIL (2606.05160), SplitAdapter (2606.03297).
  - `05_foundation.md` — 5 entries: OMG (2606.10340), MotionWAM (2606.09215), Ego-Pi (2606.08107), Perceptive Behavior Foundation Model (2606.08059), Humanoid-GPT (2606.03985).
  - `06_retarget_teleop.md` — 6 entries: humanoid self-model (2606.13222), HOWTransfer (2606.10743), X-OP (2606.07934), RealDexUMI (2606.06033), Human2Humanoid (2606.03476), ReActor (2605.06593).
- Verified official code repos:
  - https://github.com/Tsinghua-MARS-Lab/OMG
  - https://github.com/GalaxyGeneralRobotics/Humanoid-GPT
  - https://github.com/Renforce-Dynamics/MultiModalWBC
  - https://github.com/TeleHuman/OASIS
  - https://github.com/physical-superintelligence-lab/SIMPLE
  - https://github.com/lzyang2000/HANDOFF
  - https://github.com/junhengl/mpc-rl
  - https://github.com/NVlabs/GRAIL
- Existing-paper updates:
  - RoboNaldo (2606.11092) — arXiv revised from `v1` to `v3` on 2026-06-11; project page still points to a GitHub repo URL that returns `Repository not found`, so code status remains `🌐 Project Page`.
- Unresolved code-status items:
  - https://wt-umi.github.io/WTUMI/ — project page says code coming soon.
  - https://aislab-sustech.github.io/Stubborn/ — project page says code coming soon.
  - https://huangtc233.github.io/human2humanoid_website/ — project page says code coming soon.
  - https://huangtc233.github.io/bionic-style-transfer/ — project page says code coming soon.
  - https://binlee26.github.io/MIND_page/ — project page says code coming soon.
  - https://ladderman-robot.github.io — GitHub repo reachable but only README/assets at inspection time, so not marked code.
  - https://opendrivelab.com/RoboNaldo — project page links GitHub, but the repo returned "Repository not found" at inspection time.
- Inspected but excluded: broad tabletop/mobile/autonomous-driving VLA papers from 2026-06-08 to 2026-06-11 (DAM-VLA, TacCoRL, InDex, World Pilot, APT, CHORUS, muVLA, DuoBench, ERVLA, PHASER, OpenEAI-Platform, TTT-VLA, etc.) unless explicitly humanoid / whole-body / egocentric-humanoid / loco-manipulation relevant.
- Notion escalations: not run in this manual repo-only update.

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