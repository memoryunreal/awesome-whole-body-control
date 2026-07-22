# Awesome Human-Object Interaction Generation and Whole-Body Control

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

> A curated list of recent papers, datasets, codebases, and benchmarks on **human-object interaction (HOI) motion generation**, **humanoid whole-body control**, **motion tracking & imitation**, **whole-body loco-manipulation**, **humanoid foundation models**, **retargeting**, **teleoperation**, **sim-to-real deployment**, and **physics-based character animation**. Papers with verified official open-source code are marked ⭐.

Inspired by [YanjieZe/awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) with extended tagging, code-status verification, and richer per-category summaries.

## Table of Contents
- [Legend](#legend)
- [Research Landscape Summary](#research-landscape-summary)
- [Last Week Updates](#last-week-updates)
- [Human-Object Interaction Motion Generation](#human-object-interaction-motion-generation)
- [Object-Aware Human Motion Synthesis](#object-aware-human-motion-synthesis)
- [Whole-Body Motion Tracking and Imitation](#whole-body-motion-tracking-and-imitation)
- [Whole-Body Control and Loco-Manipulation](#whole-body-control-and-loco-manipulation)
- [Humanoid Foundation Models and Generalist Policies](#humanoid-foundation-models-and-generalist-policies)
- [Human-to-Humanoid Retargeting](#human-to-humanoid-retargeting)
- [Teleoperation and Demonstration Collection](#teleoperation-and-demonstration-collection)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Evaluation Metrics and Contact Modeling](#evaluation-metrics-and-contact-modeling)
- [Sim-to-Real and Deployment Systems](#sim-to-real-and-deployment-systems)
- [Related Character Animation and Physics-Based Motion Generation](#related-character-animation-and-physics-based-motion-generation)

## Legend
- ⭐ **Code**: official open-source implementation verified
- 🧩 **Partial Code**: incomplete but useful code released (eval, retarget, viz, etc.)
- 📦 **Dataset**: dataset, benchmark, or assets released
- 🌐 **Project Page**: project page available, no code
- ⏳ **Code Coming Soon**: authors state code will be released
- 🔁 **Unofficial Code**: third-party implementation only
- ❌ **No Code Found**
- 🤖 **Real Robot**: validated on a physical robot
- 🧍 **Humanoid**: evaluated on humanoid platforms
- 🧱 **Simulation**: simulation-only evaluation

## Research Landscape Summary

### Main Trends (2024–2026)
- **AMASS-driven WBC tracking is the dominant recipe.** ExBody → ExBody2 → H2O → OmniH2O → HOVER → ASAP → BeyondMimic share the same backbone: large-scale human MoCap, retargeted to a target humanoid, distilled into RL tracking policies that close the sim-to-real gap with delta-action / residual / domain-randomized models.
- **Loco-manipulation is becoming whole-body and force-aware.** FALCON, HOMIE, ULC, SkillBlender, VisualMimic, VIRAL, WholeBodyVLA, Kinematics-Aware MP-RL push toward force-adaptive bimanual carrying, pushing, and tool use on Unitree G1/H1/H1-2 and Fourier GR1.
- **HOI motion synthesis is consolidating around dual-branch / contact-guided diffusion** (HOI-Diff, CHOIS, OMOMO, InterDiff, HOI-Animator, SyncDiff, ChainHOI, DiffH2O), with a parallel push toward zero-shot text-to-HOI through LLM/SDS priors (DreamHOI, InteractAnything).
- **Humanoid foundation models / VLAs are landing on real robots.** GR00T N1/N1.5, π0/π0.5, Helix, Humanoid-VLA, LeVERB, EgoVLA, AgiBot GO-1, Gemini Robotics demonstrate language- and vision-conditioned generalist policies for humanoid form factors.
- **Retargeting datasets are now first-class artifacts.** OmniRetarget, GMR, IKMR, SONIC, BeyondMimic ship retargeted humanoid trajectories — not just code — enabling rapid kickoff of new tracking policies.
- **Behavioral foundation models are emerging.** FB-CPR / Meta Motivo, BFM-Zero, MaskedMimic, ProtoMotions provide universal motion priors that downstream policies fine-tune.
- **Whole-body teleoperation is the data engine.** Open-TeleVision, OpenWBT, CLONE, HOMIE, Bunny-VisionPro, GELLO, ACE, BiDex, DexUMI, AirExo-2, DexMimicGen, H-RDT scale demonstration collection beyond what one lab can MoCap.

### Open Problems
- **Long-horizon HOI on real humanoids.** Most HOI synthesis is still character-animation; transferring contact-rich, multi-step interactions to a physical humanoid with reliable contact and force is unsolved.
- **Cross-embodiment generalization.** Policies trained on G1 still rarely transfer cleanly to H1, Fourier GR1, or Atlas without re-retargeting and re-tuning.
- **Bimanual contact-rich manipulation under whole-body coupling.** Few works deliver dexterous in-hand manipulation while maintaining balance and locomotion.
- **Sample efficiency.** AMASS-scale + IsaacLab/MJX still requires GPU-days; world-model and offline-RL approaches (BFM-Zero, FB-CPR, BeyondMimic) only partially address this.
- **Safety and recovery.** HoST, Getting-Up, HumanoidRecovery point at fall recovery, but graceful in-task safety guarantees are missing.
- **Object-state observability.** Most loco-manipulation assumes near-perfect object pose; vision-driven WBC (VisualMimic, WholeBodyVLA) is just beginning to close this gap.

## Last Week Updates

_Latest digest: **2026-07-22** — **9 new**, **0 updated**._

### Added by Section

- `02_hoi_motion`: 1 entry — HarmoHOI (2607.17097).
- `03_wbc_tracking`: 2 entries — Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control (2607.14182), RAVEN (2607.15701).
- `04_loco_manip`: 2 entries — Handroid (2607.16187), FARO (2607.18362).
- `05_foundation`: 2 entries — Scaling Behavior Foundation Model for Humanoid Robots (2607.15163), Closing the Loop in Humanoid VLA (2607.18016).
- `06_retarget_teleop`: 1 entry — From Sign Language Generation to Humanoid Execution (2607.17769).
- `07_data_bench_s2r`: 1 entry — EgoHTR (2607.13472).

### New Entries

#### Human-Object Interaction Motion Generation

- ⏳ **[HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis](https://arxiv.org/abs/2607.17097)** — `arXiv 2026.07` — Joint diffusion framework synthesizes synchronized multi-view HOI videos together with globally aligned 3D point tracks.

#### Whole-Body Motion Tracking and Imitation

- ⭐ 🤖 🧍 **[Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control](https://arxiv.org/abs/2607.14182)** — `RoboCup Symposium 2026 / arXiv 2026.07` — Routes live music and speech through semantic audio branches that select and schedule imitation-learned whole-body skills on a G1.
- ❌ 🧍 🧱 **[RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC](https://arxiv.org/abs/2607.15701)** — `arXiv 2026.07` — Hierarchical planner uses RL to adapt visibility-graph geometry while a constrained MPC tracks collision-free humanoid navigation trajectories.

#### Whole-Body Control and Loco-Manipulation

- 🌐 🤖 🧍 **[Handroid: Bridging Dexterous Hand and Humanoid](https://arxiv.org/abs/2607.16187)** — `arXiv 2026.07` — Reconfigurable 27-DoF desktop robot switches between anthropomorphic hand and humanoid embodiments for manipulation, locomotion, and motion authoring.
- 🌐 🤖 🧍 **[FARO: Feasibility-Aware Robot Motion Optimization](https://arxiv.org/abs/2607.18362)** — `arXiv 2026.07` — Nested kinodynamic optimizer checks candidate contact sequences, guides LLM-sampled contact plans, and generates humanoid loco-manipulation trajectories trackable by RL controllers.

#### Humanoid Foundation Models and Generalist Policies

- ❌ 🤖 🧍 **[Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163)** — `arXiv 2026.07` — Studies the scaling recipe for humanoid BFMs by coordinating global-frame motion tracking, reference diversity, rollout volume, and a Humanoid Transformer architecture.
- ❌ 🤖 🧍 **[Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](https://arxiv.org/abs/2607.18016)** — `arXiv 2026.07` — POT-VLA maintains role-indexed 3D object records that both condition whole-body action generation and verify geometric task predicates during execution.

#### Human-to-Humanoid Retargeting

- ❌ 🤖 🧍 **[From Sign Language Generation to Humanoid Execution: Vision-Language Guided Retargeting with Collision Mitigation](https://arxiv.org/abs/2607.17769)** — `arXiv 2026.07` — Converts generated sign-language body motions into humanoid joint execution through SMPL-X collision mitigation and VLM-guided retargeting corrections.

#### Datasets and Benchmarks

- ⏳ 🤖 🧍 **[EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal](https://arxiv.org/abs/2607.13472)** — `arXiv 2026.07` — Captures 55 scene-aligned egocentric human-terrain sequences and uses them to train perceptive locomotion policies deployed on a Unitree G1.

### Most Implementation-Ready Papers (verified official code)
- ⭐ **[CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.23680)** — `arXiv 2026.06` — Coordinates body and dexterous-hand latent priors with residual RL so a G1 can manipulate objects continuously while walking.
- ⭐ **[GMR: General Motion Retargeting (Retargeter for TWIST)](https://github.com/YanjieZe/GMR)** — `ICRA 2026` — Real-time CPU motion retargeting library handling SMPL→multi-humanoid mapping with foot-sliding/penetration fixes.
- ⭐ **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — `arXiv 2026.06` — Fully virtual generation pipeline composing 3D assets, simulator scenes, and video priors into robot-compatible loco-manipulation data.
- ⭐ **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** — `arXiv 2026.06` — Distills complementary teachers into a task-space whole-body command interface for diverse humanoid loco-manipulation skills.
- ⭐ **[Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985)** — `CVPR 2026` — GPT-style causal Transformer trained on a two-billion-frame retargeted motion corpus for zero-shot whole-body tracking.
- ⭐ **[LIMMT: Less is More for Motion Tracking](https://arxiv.org/abs/2606.06953)** — `ICML 2026` — Data-centric motion-tracking study showing that carefully filtered high-quality motions can outperform much larger noisy corpora.
- ⭐ **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** — `arXiv 2026.06` — Open IsaacLab-based WBC framework unifying joint, root, and end-effector reference modalities for humanoid motion mimicking.
- ⭐ **[MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation](https://arxiv.org/abs/2602.08594)** — `arXiv 2026.02` — Trains a generalist tracker then rapidly adapts to specific teleop interfaces via additive residuals.
- ⭐ **[OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.08548)** — `arXiv 2026.06` — Open simulation-to-real data pipeline for humanoid loco-manipulation with embodiment-aligned demonstrations.
- ⭐ **[OMG: Omni-Modal Motion Generation for Generalist Humanoid Control](https://arxiv.org/abs/2606.10340)** — `arXiv 2026.06` — Generalist humanoid control stack that places an omni-modal motion-generation brain above a reactive tracking controller.
- ⭐ **[Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control](https://arxiv.org/abs/2607.14182)** — `RoboCup Symposium 2026 / arXiv 2026.07` — Routes live music and speech through semantic audio branches that select and schedule imitation-learned whole-body skills on a G1.
- ⭐ **[TEXEDO: Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](https://arxiv.org/abs/2606.22998)** — `arXiv 2026.06` — Samples language-conditioned humanoid motions and selects candidates with a controller-feasibility verifier plus semantic alignment scoring.
- ⭐ **[Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](https://arxiv.org/abs/2606.22136)** — `arXiv 2026.06` — Uses generative video world models to synthesize egocentric human-object manipulation videos and converts them into robot-trainable supervision.
- ⭐ **[WholebodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](https://github.com/OpenDriveLab/WholebodyVLA)** — `ICLR 2026` — Unified latent VLA architecture for whole-body humanoid loco-manipulation with tracking primitives.
- ⭐ **[Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation](https://arxiv.org/abs/2606.05687)** — `arXiv 2026.06` — Efficient training-time MPC guidance for humanoid locomotion and manipulation policies.

### Most Relevant for HOI Motion Generation
- ⭐ 🧍 🧱 **[DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects](https://arxiv.org/abs/2606.15133)** — `arXiv 2026.06` — Generates and trains physically plausible dexterous hand-object interactions with articulated objects using contact-aware simulation assets and RL code.
- 🌐 **[HumanX - Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473)** — `arXiv 2026.02` — Agile generalizable humanoid interaction skills learned from human videos.
- 🌐 **[MOCHI: Motion Enhancement of Collaborative Human-object Interactions](https://arxiv.org/abs/2606.18243)** — `SIGGRAPH 2026 / ACM TOG` — Enhances noisy collaborative multi-human object-interaction captures by improving contact alignment, hand articulation, and temporal consistency.
- 🌐 **[WHOLE - World-Grounded Hand-Object Lifted from Egocentric Videos](https://arxiv.org/abs/2602.22209)** — `arXiv 2026.02` — World-grounded hand-object lifting from egocentric videos.
- ⏳ **[HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis](https://arxiv.org/abs/2607.17097)** — `arXiv 2026.07` — Joint diffusion framework synthesizes synchronized multi-view HOI videos together with globally aligned 3D point tracks.
- ⏳ **[IMAGIN-4D: Image-Guided Controllable Interaction Generation](https://arxiv.org/abs/2606.23675)** — `arXiv 2026.06` — Diffusion-based HOI generator uses a reference image to specify body pose, object pose, contacts, and spatial layout for a target interaction frame.
- ❌ 🤖 🧍 **[DeVI: Physics-based Dexterous HOI via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841)** — `arXiv 2026.04` — Hybrid 3D-human + 2D-object imitation targets train physics-based dexterous HOI policy.
- ❌ 🤖 🧍 **[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473)** — `arXiv 2026.02` — XGen synthesizes humanoid HOI data from monocular videos; XMimic learns interaction skills.
- ❌ **[AnchorHOI: Zero-shot Generation of 4D HOI via Anchor-based Prior Distillation](https://arxiv.org/abs/2512.14095)** — `AAAI 2026` — Anchor NeRFs + anchor keypoints distill image and video diffusion priors for 4D HOI.
- ❌ **[InterPhys: Physics-aware Human Motion Synthesis in a Dynamic Scene](https://arxiv.org/abs/2605.01036)** — `arXiv 2026.05` — Two-stage diffusion with differentiable contact-force model for physically consistent HSI.
- ❌ **[InterPrior - Scaling Generative Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2602.06035)** — `arXiv 2026.02` — Scaling generative control for physics-based HOI.
- ❌ **[JointHOI: Jointly Generating Contact Maps Enhances Hand Object Interaction Generation](https://arxiv.org/abs/2607.01768)** — `arXiv 2026.07` — Single-stage text-driven diffusion model jointly generates hand-object motion and temporally evolving contact maps to reduce penetration and floating.

### Most Relevant for Whole-Body Loco-Manipulation
- ⭐ 🤖 🧍 **[CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.23680)** — `arXiv 2026.06` — Coordinates body and dexterous-hand latent priors with residual RL so a G1 can manipulate objects continuously while walking.
- ⭐ 🤖 🧍 **[GMR: General Motion Retargeting (Retargeter for TWIST)](https://github.com/YanjieZe/GMR)** — `ICRA 2026` — Real-time CPU motion retargeting library handling SMPL→multi-humanoid mapping with foot-sliding/penetration fixes.
- ⭐ 🤖 🧍 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — `arXiv 2026.06` — Fully virtual generation pipeline composing 3D assets, simulator scenes, and video priors into robot-compatible loco-manipulation data.
- ⭐ 🤖 🧍 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** — `arXiv 2026.06` — Distills complementary teachers into a task-space whole-body command interface for diverse humanoid loco-manipulation skills.
- ⭐ 🤖 🧍 **[LIMMT: Less is More for Motion Tracking](https://arxiv.org/abs/2606.06953)** — `ICML 2026` — Data-centric motion-tracking study showing that carefully filtered high-quality motions can outperform much larger noisy corpora.
- ⭐ 🤖 🧍 **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** — `arXiv 2026.06` — Open IsaacLab-based WBC framework unifying joint, root, and end-effector reference modalities for humanoid motion mimicking.
- ⭐ 🤖 🧍 **[MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation](https://arxiv.org/abs/2602.08594)** — `arXiv 2026.02` — Trains a generalist tracker then rapidly adapts to specific teleop interfaces via additive residuals.
- ⭐ 🤖 🧍 **[OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.08548)** — `arXiv 2026.06` — Open simulation-to-real data pipeline for humanoid loco-manipulation with embodiment-aligned demonstrations.
- ⭐ 🤖 🧍 **[Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control](https://arxiv.org/abs/2607.14182)** — `RoboCup Symposium 2026 / arXiv 2026.07` — Routes live music and speech through semantic audio branches that select and schedule imitation-learned whole-body skills on a G1.
- ⭐ 🤖 🧍 **[TEXEDO: Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](https://arxiv.org/abs/2606.22998)** — `arXiv 2026.06` — Samples language-conditioned humanoid motions and selects candidates with a controller-feasibility verifier plus semantic alignment scoring.
- ⭐ 🤖 🧍 **[WholebodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](https://github.com/OpenDriveLab/WholebodyVLA)** — `ICLR 2026` — Unified latent VLA architecture for whole-body humanoid loco-manipulation with tracking primitives.
- ⭐ 🧍 🧱 **[Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation](https://arxiv.org/abs/2606.05687)** — `arXiv 2026.06` — Efficient training-time MPC guidance for humanoid locomotion and manipulation policies.

---

_Total unique entries: **547**. Verified open-source: **225**._

## Human-Object Interaction Motion Generation

_49 entries._

- ⭐ 🧍 🧱 **[DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects](https://arxiv.org/abs/2606.15133)** `arXiv 2026.06` `HOI-Motion-Gen`
  Tianshan Zhang et al..
  Generates and trains physically plausible dexterous hand-object interactions with articulated objects using contact-aware simulation assets and RL code.
  Links: [Project](https://aigeeksgroup.github.io/DragMesh-2) · [Code](https://github.com/AIGeeksGroup/DragMesh-2) · [Paper](https://arxiv.org/abs/2606.15133) · [Dataset](https://huggingface.co/datasets/AIGeeksGroup/DragMesh-2)

- 🌐 **[HumanX - Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473)** `arXiv 2026.02` `HOI`
  Agile generalizable humanoid interaction skills learned from human videos.
  Links: [Project](https://wyhuai.github.io/human-x/) · [Paper](https://arxiv.org/abs/2602.02473)

- 🌐 **[MOCHI: Motion Enhancement of Collaborative Human-object Interactions](https://arxiv.org/abs/2606.18243)** `SIGGRAPH 2026 / ACM TOG` `HOI-Motion-Gen`
  Jiye Lee et al..
  Enhances noisy collaborative multi-human object-interaction captures by improving contact alignment, hand articulation, and temporal consistency.
  Links: [Project](https://jiyewise.github.io/projects/MOCHI/) · [Paper](https://arxiv.org/abs/2606.18243)

- 🌐 **[WHOLE - World-Grounded Hand-Object Lifted from Egocentric Videos](https://arxiv.org/abs/2602.22209)** `arXiv 2026.02` `HOI`
  World-grounded hand-object lifting from egocentric videos.
  Links: [Project](https://judyye.github.io/whole-www/) · [Paper](https://arxiv.org/abs/2602.22209)

- ⏳ **[HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis](https://arxiv.org/abs/2607.17097)** `arXiv 2026.07` `hand-object interaction synthesis` `HOI-Motion-Gen`
  Lingwei Dang et al..
  Joint diffusion framework synthesizes synchronized multi-view HOI videos together with globally aligned 3D point tracks.
  Links: [Project](https://droliven.github.io/HarmoHOI_project/) · [Paper](https://arxiv.org/abs/2607.17097)

- ⏳ **[IMAGIN-4D: Image-Guided Controllable Interaction Generation](https://arxiv.org/abs/2606.23675)** `arXiv 2026.06` `HOI-Motion-Gen`
  Sai Kumar Dwivedi et al..
  Diffusion-based HOI generator uses a reference image to specify body pose, object pose, contacts, and spatial layout for a target interaction frame.
  Links: [Project](https://imagin4d.github.io) · [Paper](https://arxiv.org/abs/2606.23675)

- ❌ **[AnchorHOI: Zero-shot Generation of 4D HOI via Anchor-based Prior Distillation](https://arxiv.org/abs/2512.14095)** `AAAI 2026` `HOI-Motion-Gen`
  (see paper).
  Anchor NeRFs + anchor keypoints distill image and video diffusion priors for 4D HOI.
  Links: [Paper](https://arxiv.org/abs/2512.14095)

- ❌ **[InterPrior - Scaling Generative Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2602.06035)** `arXiv 2026.02` `HOI`
  Scaling generative control for physics-based HOI.
  Links: [Paper](https://arxiv.org/abs/2602.06035)

- ❌ **[JointHOI: Jointly Generating Contact Maps Enhances Hand Object Interaction Generation](https://arxiv.org/abs/2607.01768)** `arXiv 2026.07` `dexterous hand-object interaction` `HOI-Motion-Gen`
  Mingyeong Song et al..
  Single-stage text-driven diffusion model jointly generates hand-object motion and temporally evolving contact maps to reduce penetration and floating.
  Links: [Paper](https://arxiv.org/abs/2607.01768)

- ❌ 🧱 **[Policy-as-Data: Learning Generalizable HOI Diffusion Models from Simulated Physics](https://arxiv.org/abs/2606.22806)** `arXiv 2026.06` `HOI-Motion-Gen`
  Shujia Li et al..
  Uses task policies trained in physics simulation as a scalable data source for training generalizable HOI diffusion models.
  Links: [Paper](https://arxiv.org/abs/2606.22806)

- ⭐ **[AvatarGO: Zero-shot 4D Human-Object Interaction Generation and Animation](https://arxiv.org/abs/2410.07164)** `ICLR 2025` `HOI-Motion-Gen`
  Yukang Cao, Liang Pan, Kai Han, Kwan-Yee K. Wong, Ziwei Liu.
  Zero-shot 4D HOI scenes from text via LLM-guided contact retargeting and SDS.
  Links: [Project](https://yukangcao.github.io/AvatarGO/) · [Code](https://github.com/yukangcao/AvatarGO) · [Paper](https://arxiv.org/abs/2410.07164)

- ⭐ **[ChainHOI: Joint-based Kinematic Chain Modeling for HOI Generation](https://arxiv.org/abs/2503.13130)** `CVPR 2025` `HOI-Motion-Gen`
  Ling-An Zeng, Guohong Huang, Yi-Lin Wei, Shengbo Gu, Yu-Ming Tang, Jingke Meng, Wei-Shi Zheng.
  Models HOI at joint and kinematic-chain levels with spatiotemporal GCN.
  Links: [Code](https://github.com/qingtian5/ChainHOI) · [Paper](https://arxiv.org/abs/2503.13130)

- ⭐ **[ROG: Guiding Human-Object Interactions with Rich Geometry and Relations](https://arxiv.org/abs/2503.20118)** `CVPR 2025` `HOI-Motion-Gen`
  Mengqing Xue, Yifei Liu, Ling Guo, Shaoli Huang, Changxing Ding, Mingyuan Zhang.
  Diffusion with boundary keypoints and Interactive Distance Field for richer HOI dynamics.
  Links: [Paper](https://arxiv.org/abs/2503.20118)

- ⭐ **[SyncDiff: Synchronized Motion Diffusion for Multi-Body HOI Synthesis](https://arxiv.org/abs/2412.20104)** `ICCV 2025` `HOI-Motion-Gen`
  Wenkun He, Yun Liu, Ruitao Liu, Li Yi.
  Single diffusion captures joint multi-body distribution with explicit synchronization.
  Links: [Project](https://syncdiff.github.io/) · [Code](https://github.com/WenkunHe/SyncDiff) · [Paper](https://arxiv.org/abs/2412.20104)

- 📦 **[FORCE: Physics-aware Human-Object Interaction](https://arxiv.org/abs/2403.11237)** `3DV 2025` `HOI-Motion-Gen`
  Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Ilya Petrov, Vladimir Guzov, Helisa Dhamo, Eduardo Pérez-Pellitero, Gerard Pons-Moll.
  Models physical force/resistance interplay for nuanced HOI like push/pull/carry.
  Links: [Project](https://virtualhumans.mpi-inf.mpg.de/force/) · [Code](https://github.com/xz6014/FORCE_dataset) · [Paper](https://arxiv.org/abs/2403.11237) · [Dataset](FORCE (450 sequences))

- 🌐 **[H2-COMPACT - Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies](https://arxiv.org/pdf/2505.17627)** `arXiv 2025.05` `HOI`
  Adaptive contact trajectory policies for human-humanoid co-manipulation.
  Links: [Project](https://h2compact.github.io/h2compact/) · [Paper](https://arxiv.org/pdf/2505.17627)

- 🌐 **[HOI-PAGE: Zero-Shot HOI Generation with Part Affordance Guidance](https://arxiv.org/abs/2506.07209)** `arXiv 2025.06` `HOI-Motion-Gen`
  Lei Li, Angela Dai.
  Part Affordance Graphs from LLMs guide zero-shot 4D HOI synthesis from text.
  Links: [Project](https://hoipage.github.io/) · [Paper](https://arxiv.org/abs/2506.07209)

- 🌐 **[HOIDiNi: Human-Object Interaction through Diffusion Noise Optimization](https://arxiv.org/abs/2506.15625)** `arXiv 2025.06` `HOI-Motion-Gen`
  Roey Ron, Guy Tevet, Haim Sawdayee, Amit H. Bermano.
  Test-time diffusion noise optimization for HOI satisfying tight contact constraints.
  Links: [Project](https://hoidini.github.io/) · [Paper](https://arxiv.org/abs/2506.15625)

- 🌐 **[HUMOTO: A 4D Dataset of Mocap Human Object Interactions](https://arxiv.org/abs/2504.10414)** `ICCV 2025` `HOI-Motion-Gen`
  Jiaxin Lu, Hsin-Ying Lee, Chia-Yu Chen, Stylianos Moschoglou, Yannis Panagakis, others.
  4D HOI mocap dataset with LLM-scripted scene-driven tasks across diverse daily activities.
  Links: [Project](https://jiaxin-lu.github.io/humoto/) · [Paper](https://arxiv.org/abs/2504.10414) · [Dataset](HUMOTO (736 sequences))

- 🌐 **[InterPose: Learning to Generate HOIs from Large-Scale Web Videos](https://arxiv.org/abs/2509.00767)** `arXiv 2025.09` `HOI-Motion-Gen`
  (anonymized).
  Web-video pipeline producing 73.8K HOI sequences; LLM agent enables zero-shot animation.
  Links: [Paper](https://arxiv.org/abs/2509.00767) · [Dataset](InterPose (73.8K seqs from 45.8K videos))

- 🌐 **[SViMo: Synchronized Diffusion for Video and Motion Generation in Hand-object Scenarios](https://arxiv.org/abs/2506.02444)** `NeurIPS 2025` `HOI-Motion-Gen`
  (see paper).
  Joint diffusion for video and motion in hand-object interaction with synchronization.
  Links: [Project](https://droliven.github.io/SViMo_project/) · [Paper](https://arxiv.org/abs/2506.02444)

- ❌ **[Auto-Regressive Diffusion for Generating 3D HOIs (ARDHOI)](https://arxiv.org/abs/2503.16801)** `AAAI 2025` `HOI-Motion-Gen`
  Zichen Geng, Zeeshan Hayder, Wei Liu, Ajmal Saeed Mian.
  Continuous-token autoregressive diffusion with Mamba context encoder for long HOI sequences.
  Links: [Paper](https://arxiv.org/abs/2503.16801)

- ❌ **[CoopDiff: Anticipating 3D HOIs via Contact-consistent Decoupled Diffusion](https://arxiv.org/abs/2508.07162)** `arXiv 2025.08` `HOI-Motion-Gen`
  (see paper).
  Contact-consistent decoupled diffusion for 3D HOI anticipation.
  Links: [Paper](https://arxiv.org/abs/2508.07162)

- ❌ **[Decoupled Generative Modeling for HOI Synthesis](https://arxiv.org/abs/2512.19049)** `arXiv 2025.12` `HOI-Motion-Gen`
  (see paper).
  Decoupled generative modeling separates body, object, and contact for HOI synthesis.
  Links: [Paper](https://arxiv.org/abs/2512.19049)

- ❌ **[GentleHumanoid - Learning Upper-body Compliance for Contact-rich Human and Object Interaction](https://arxiv.org/abs/2511.04679)** `arXiv 2025.11` `HOI`
  Learns compliant upper-body humanoid behavior for contact-rich interaction.
  Links: [Paper](https://arxiv.org/abs/2511.04679)

- ❌ **[HDMI - Learning Interactive Humanoid Whole-Body Control from Human Videos](https://arxiv.org/abs/2509.16757)** `arXiv 2025.09` `HOI`
  Interactive humanoid whole-body control learned from human videos.
  Links: [Paper](https://arxiv.org/abs/2509.16757)

- ❌ **[HOI-Dyn: Learning Interaction Dynamics for Human-Object Motion Diffusion](https://arxiv.org/abs/2507.01737)** `arXiv 2025.07` `HOI-Motion-Gen`
  Lin Wu, Zhixiang Chen, Jianglin Lan.
  Lightweight transformer dynamics predicts object reaction; residual dynamics loss.
  Links: [Paper](https://arxiv.org/abs/2507.01737)

- ❌ **[InteractAnything: Zero-shot HOI Synthesis via LLM Feedback and Object Affordance Parsing](https://arxiv.org/abs/2505.24315)** `CVPR 2025` `HOI-Motion-Gen`
  Jinlu Zhang, Yixin Chen, Zan Wang, Jie Yang, Yizhou Wang, Siyuan Huang.
  Open-set 3D HOI synthesis using LLM feedback for relations and 2D diffusion for contacts.
  Links: [Paper](https://arxiv.org/abs/2505.24315)

- ❌ **[LatentHOI: On the Generalizable Hand Object Motion Generation with Latent Hand Diffusion](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_LatentHOI_On_the_Generalizable_Hand_Object_Motion_Generation_with_Latent_CVPR_2025_paper.pdf)** `CVPR 2025` `HOI-Motion-Gen`
  Yifei Li, Sammy Christen, Christoph Gebhardt, Jie Song, Otmar Hilliges.
  Decouples temporal motion from fine-grained spatial hand-object via latent diffusion + GraspVAE.
  Links: [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_LatentHOI_On_the_Generalizable_Hand_Object_Motion_Generation_with_Latent_CVPR_2025_paper.pdf)

- ❌ **[Multimodal priors-augmented text-driven 3D HOI generation](https://arxiv.org/abs/2602.10659)** `Science China Information Sciences 2025` `HOI-Motion-Gen`
  (Science China Information Sciences).
  Augments text-driven 3D HOI generation with multimodal priors.
  Links: [Paper](https://arxiv.org/abs/2602.10659)

- ❌ **[OnlineHOI: Towards Online Human-Object Interaction Generation and Perception](https://arxiv.org/abs/2509.12250)** `ACM MM 2025` `HOI-Motion-Gen`
  Yihong Lin, others.
  Mamba-based online HOI generation and perception with memory mechanism.
  Links: [Paper](https://arxiv.org/abs/2509.12250)

- ❌ **[SimGenHOI - Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL](https://arxiv.org/abs/2508.14120)** `arXiv 2025.08` `HOI`
  Generative-modeling + RL for whole-body human-object interaction.
  Links: [Paper](https://arxiv.org/abs/2508.14120)

- ⭐ **[CHOIS: Controllable Human-Object Interaction Synthesis](https://arxiv.org/abs/2312.03913)** `ECCV 2024 (Oral)` `HOI-Motion-Gen`
  Jiaman Li, Alexander Clegg, Roozbeh Mottaghi, Jiajun Wu, Xavier Puig, C. Karen Liu.
  Conditional diffusion that generates joint human-object motion from text and sparse object waypoints.
  Links: [Project](https://lijiaman.github.io/projects/chois/) · [Code](https://github.com/lijiaman/chois_release) · [Paper](https://arxiv.org/abs/2312.03913)

- ⭐ **[CORE4D: A 4D Human-Object-Human Interaction Dataset for Collaborative Object REarrangement](https://arxiv.org/abs/2406.19353)** `arXiv 2024.06 / CVPR 2025 (extended)` `HOI-Motion-Gen`
  Yun Liu, Chengwen Zhang, Ruofan Xing, Bingda Tang, Bowen Yang, Li Yi.
  Two-human collaborative object rearrangement mocap dataset with retargeting augmentation.
  Links: [Project](https://core4d.github.io/) · [Code](https://github.com/leolyliu/CORE4D-Instructions) · [Paper](https://arxiv.org/abs/2406.19353) · [Dataset](CORE4D (1K real + 11K retargeted))

- ⭐ **[DiffH2O: Diffusion-Based Synthesis of Hand-Object Interactions from Textual Descriptions](https://arxiv.org/abs/2403.17827)** `SIGGRAPH Asia 2024` `HOI-Motion-Gen`
  Sammy Christen, Shreyas Hampali, Fadime Sener, Edoardo Remelli, Tomas Hodan, Eric Sauser, Shugao Ma, Bugra Tekin.
  Two-stage hand-object diffusion (grasp + manipulation) from text with object geometry.
  Links: [Project](https://diffh2o.github.io/) · [Code](https://github.com/facebookresearch/diffh2o) · [Paper](https://arxiv.org/abs/2403.17827)

- ⭐ **[DreamHOI: Subject-Driven Generation of 3D HOI with Diffusion Priors](https://arxiv.org/abs/2409.08278)** `arXiv 2024.09` `HOI-Motion-Gen`
  Thomas Hanwen Zhu, Ruining Li, Tomas Jakab.
  Score-distillation HOI generation with implicit + explicit subject-driven hybrid.
  Links: [Project](https://dreamhoi.github.io/) · [Code](https://github.com/hanwenzhu/dreamhoi) · [Paper](https://arxiv.org/abs/2409.08278)

- ⭐ **[HOIDiffusion: Generating Realistic 3D Hand-Object Interaction Data](https://arxiv.org/abs/2403.12011)** `CVPR 2024` `HOI-Motion-Gen`
  Mengqi Zhang, Yang Fu, Zheng Ding, Sifei Liu, Zhuowen Tu, Xiaolong Wang.
  Diffusion image generator for realistic 3D-conditioned hand-object data augmentation.
  Links: [Project](https://mq-zhang1.github.io/HOIDiffusion/) · [Code](https://github.com/Mq-Zhang1/HOIDiffusion) · [Paper](https://arxiv.org/abs/2403.12011)

- ⭐ **[I'M HOI: Inertia-aware Monocular Capture of 3D Human-Object Interactions](https://arxiv.org/abs/2312.08869)** `CVPR 2024` `HOI-Motion-Gen`
  Chengfeng Zhao, Juze Zhang, Jiashen Du, Ziwei Shan, Junye Wang, Jingyi Yu, Jingya Wang, Lan Xu.
  Monocular HOI capture using inertia (IMU) cues; new IMHD2 dataset.
  Links: [Code](https://github.com/AfterJourney00/IMHD-Dataset) · [Paper](https://arxiv.org/abs/2312.08869) · [Dataset](IMHD2)

- ⭐ **[InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction](https://arxiv.org/abs/2403.19652)** `NeurIPS 2024` `HOI-Motion-Gen`
  Sirui Xu, Ziyin Wang, Yu-Xiong Wang, Liang-Yan Gui.
  Zero-shot text-to-HOI via LLM planning + text-to-motion + learned world model.
  Links: [Project](https://sirui-xu.github.io/InterDreamer/) · [Code](https://github.com/Sirui-Xu/InterDreamer) · [Paper](https://arxiv.org/abs/2403.19652)

- ⭐ **[NIFTY: Neural Object Interaction Fields for Guided Human Motion Synthesis](https://arxiv.org/abs/2307.07511)** `CVPR 2024` `HOI-Motion-Gen`
  Nilesh Kulkarni, Davis Rempe, Kyle Genova, Abhijit Kundu, Justin Johnson, David Fouhey, Leonidas Guibas.
  Object-attached neural interaction field guides motion diffusion toward valid contacts.
  Links: [Project](https://nileshkulkarni.github.io/nifty/) · [Code](https://github.com/nileshkulkarni/nifty) · [Paper](https://arxiv.org/abs/2307.07511)

- ⭐ **[Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction](https://arxiv.org/abs/2404.00562)** `CVPR 2024` `HOI-Motion-Gen`
  Junuk Cha, Jihyeon Kim, Jae Shin Yoon, Seungryul Baek.
  Text-guided generation of 3D hand-object motion using contact-aware modeling.
  Links: [Code](https://github.com/JunukCha/Text2HOI) · [Paper](https://arxiv.org/abs/2404.00562)

- 🌐 **[CG-HOI: Contact-Guided 3D Human-Object Interaction Generation](https://arxiv.org/abs/2311.16097)** `CVPR 2024` `HOI-Motion-Gen`
  Christian Diller, Angela Dai.
  Joint diffusion of human, object, and contact with cross-attention; contacts guide inference.
  Links: [Project](https://www.christian-diller.de/projects/cg-hoi/) · [Paper](https://arxiv.org/abs/2311.16097)

- 🌐 **[Human-Object Interaction from Human-Level Instructions (HOI-HLI)](https://arxiv.org/abs/2406.17840)** `arXiv 2024.06` `HOI-Motion-Gen`
  Zhen Wu, Jiaman Li, Pei Xu, C. Karen Liu.
  LLM decomposes high-level instructions into sub-task HOIs and waypoints feeding CHOIS.
  Links: [Project](https://hoifhli.github.io/) · [Paper](https://arxiv.org/abs/2406.17840)

- ❌ **[HOIAnimator: Generating Text-prompt Human-object Animations using Novel Perceptive Diffusion Models](https://openaccess.thecvf.com/content/CVPR2024/papers/Song_HOIAnimator_Generating_Text-prompt_Human-object_Animations_using_Novel_Perceptive_Diffusion_Models_CVPR_2024_paper.pdf)** `CVPR 2024` `HOI-Motion-Gen`
  Weilin Wan, Yiming Huang, Shutong Wu, Taku Komura, Wenping Wang, Dinesh Jayaraman, Lingjie Liu.
  Dual perceptive diffusion with cross-modality message passing and Interaction Contact Field.
  Links: [Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Song_HOIAnimator_Generating_Text-prompt_Human-object_Animations_using_Novel_Perceptive_Diffusion_Models_CVPR_2024_paper.pdf)

- ⭐ **[HOI-Diff: Text-Driven Synthesis of 3D Human-Object Interactions using Diffusion Models](https://arxiv.org/abs/2312.06553)** `arXiv 2023.12 / CVPRW 2025 (HuMoGen)` `HOI-Motion-Gen`
  Xiaogang Peng, Yiming Xie, Zizhao Wu, Varun Jampani, Deqing Sun, Huaizu Jiang.
  Dual-branch diffusion model for text-driven 3D HOI generation with cross-attention and affordance prediction.
  Links: [Project](https://neu-vi.github.io/HOI-Diff/) · [Code](https://github.com/neu-vi/HOI-Diff) · [Paper](https://arxiv.org/abs/2312.06553) · [Dataset](BEHAVE (annotated with text))

- ⭐ **[IMoS: Intent-Driven Full-Body Motion Synthesis for Human-Object Interactions](https://arxiv.org/abs/2212.07555)** `Eurographics 2023` `HOI-Motion-Gen`
  Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik, Christian Theobalt, Philipp Slusallek.
  Intent-driven cVAE for action+object text-to-HOI motion with arm/body decoupling.
  Links: [Project](https://vcai.mpi-inf.mpg.de/projects/IMoS/) · [Code](https://github.com/anindita127/IMoS) · [Paper](https://arxiv.org/abs/2212.07555)

- ⭐ **[InterDiff: Generating 3D Human-Object Interactions with Physics-Informed Diffusion](https://arxiv.org/abs/2308.16905)** `ICCV 2023` `HOI-Motion-Gen`
  Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, Liang-Yan Gui.
  Physics-informed diffusion for whole-body HOI prediction with interaction correction.
  Links: [Project](https://sirui-xu.github.io/InterDiff/) · [Code](https://github.com/Sirui-Xu/InterDiff) · [Paper](https://arxiv.org/abs/2308.16905)

- ⭐ **[HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction](https://arxiv.org/abs/2203.01577)** `CVPR 2022` `HOI-Motion-Gen`
  Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, Li Yi.
  Large 4D egocentric dataset for category-level HOI segmentation/tracking/action.
  Links: [Project](https://hoi4d.github.io/) · [Code](https://github.com/leolyliu/HOI4D-Instructions) · [Paper](https://arxiv.org/abs/2203.01577) · [Dataset](HOI4D (2.4M frames))

- 🌐 **[InterCap: Joint Markerless 3D Tracking of Humans and Objects in Interaction](https://arxiv.org/abs/2209.12354)** `GCPR 2022 / IJCV 2024` `HOI-Motion-Gen`
  Yinghao Huang, Omid Taheri, Michael J. Black, Dimitrios Tzionas.
  Markerless multi-view tracking and dataset of full-body HOI with SMPL-X.
  Links: [Project](https://intercap.is.tue.mpg.de/) · [Code](https://github.com/YinghaoHuang91/InterCap) · [Paper](https://arxiv.org/abs/2209.12354) · [Dataset](InterCap (10 subjects, 10 objects))


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [DragMesh-2: Physically Plausible Dexterous Hand-Object Inter](https://arxiv.org/abs/2606.15133) | — | — | ⭐ Code | Generates and trains physically plausible dexterous hand-object interactions wit |
| 2026 | [HumanX - Toward Agile and Generalizable Humanoid Interaction](https://arxiv.org/abs/2602.02473) | — | — | 🌐 Project Page | Agile generalizable humanoid interaction skills learned from human videos. |
| 2026 | [MOCHI: Motion Enhancement of Collaborative Human-object Inte](https://arxiv.org/abs/2606.18243) | — | — | 🌐 Project Page | Enhances noisy collaborative multi-human object-interaction captures by improvin |
| 2026 | [WHOLE - World-Grounded Hand-Object Lifted from Egocentric Vi](https://arxiv.org/abs/2602.22209) | — | — | 🌐 Project Page | World-grounded hand-object lifting from egocentric videos. |
| 2026 | [HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-vie](https://arxiv.org/abs/2607.17097) | hand-object interaction synthesis | — | ⏳ Code Coming Soon | Joint diffusion framework synthesizes synchronized multi-view HOI videos togethe |
| 2026 | [IMAGIN-4D: Image-Guided Controllable Interaction Generation](https://arxiv.org/abs/2606.23675) | — | — | ⏳ Code Coming Soon | Diffusion-based HOI generator uses a reference image to specify body pose, objec |
| 2026 | [AnchorHOI: Zero-shot Generation of 4D HOI via Anchor-based P](https://arxiv.org/abs/2512.14095) | — | — | ❌ No Code | Anchor NeRFs + anchor keypoints distill image and video diffusion priors for 4D  |
| 2026 | [InterPrior - Scaling Generative Control for Physics-Based Hu](https://arxiv.org/abs/2602.06035) | — | — | ❌ No Code | Scaling generative control for physics-based HOI. |
| 2026 | [JointHOI: Jointly Generating Contact Maps Enhances Hand Obje](https://arxiv.org/abs/2607.01768) | dexterous hand-object interaction | — | ❌ No Code | Single-stage text-driven diffusion model jointly generates hand-object motion an |
| 2026 | [Policy-as-Data: Learning Generalizable HOI Diffusion Models ](https://arxiv.org/abs/2606.22806) | — | — | ❌ No Code | Uses task policies trained in physics simulation as a scalable data source for t |
| 2025 | [AvatarGO: Zero-shot 4D Human-Object Interaction Generation a](https://arxiv.org/abs/2410.07164) | — | — | ⭐ Code | Zero-shot 4D HOI scenes from text via LLM-guided contact retargeting and SDS. |
| 2025 | [ChainHOI: Joint-based Kinematic Chain Modeling for HOI Gener](https://arxiv.org/abs/2503.13130) | — | — | ⭐ Code | Models HOI at joint and kinematic-chain levels with spatiotemporal GCN. |
| 2025 | [ROG: Guiding Human-Object Interactions with Rich Geometry an](https://arxiv.org/abs/2503.20118) | — | — | ⭐ Code | Diffusion with boundary keypoints and Interactive Distance Field for richer HOI  |
| 2025 | [SyncDiff: Synchronized Motion Diffusion for Multi-Body HOI S](https://arxiv.org/abs/2412.20104) | — | — | ⭐ Code | Single diffusion captures joint multi-body distribution with explicit synchroniz |
| 2025 | [FORCE: Physics-aware Human-Object Interaction](https://arxiv.org/abs/2403.11237) | — | — | 📦 Dataset | Models physical force/resistance interplay for nuanced HOI like push/pull/carry. |

## Object-Aware Human Motion Synthesis

_26 entries._

- ❌ 🤖 🧍 **[DeVI: Physics-based Dexterous HOI via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841)** `arXiv 2026.04` `Object-Aware-Motion`
  (see paper).
  Hybrid 3D-human + 2D-object imitation targets train physics-based dexterous HOI policy.
  Links: [Paper](https://arxiv.org/abs/2604.20841)

- ❌ 🤖 🧍 **[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473)** `arXiv 2026.02` `Object-Aware-Motion`
  (see paper).
  XGen synthesizes humanoid HOI data from monocular videos; XMimic learns interaction skills.
  Links: [Paper](https://arxiv.org/abs/2602.02473)

- ❌ **[InterPhys: Physics-aware Human Motion Synthesis in a Dynamic Scene](https://arxiv.org/abs/2605.01036)** `arXiv 2026.05` `Object-Aware-Motion`
  (see paper).
  Two-stage diffusion with differentiable contact-force model for physically consistent HSI.
  Links: [Paper](https://arxiv.org/abs/2605.01036)

- ❌ **[SceMoS: Scene-Aware 3D Human Motion Synthesis with Geometry-Grounded Tokens](https://arxiv.org/abs/2602.20476)** `arXiv 2026.02` `Object-Aware-Motion`
  (see paper).
  Scene-aware motion synthesis via geometry-grounded planning tokens; SOTA on TRUMANS.
  Links: [Paper](https://arxiv.org/abs/2602.20476)

- ⭐ 🧍 🧱 **[TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization](https://arxiv.org/abs/2503.19901)** `CVPR 2025 (Oral)` `Object-Aware-Motion`
  Liang Pan, Zeshi Yang, Zhiyang Dou, Wenjia Wang, Buzhen Huang, Bo Dai, Taku Komura, Jingbo Wang.
  Unified transformer policy with proprio + task tokens for multi-skill physical HSI.
  Links: [Project](https://liangpan99.github.io/TokenHSI/) · [Code](https://github.com/liangpan99/TokenHSI) · [Paper](https://arxiv.org/abs/2503.19901)

- 🌐 **[SceneMI: Motion In-betweening for Modeling Human-Scene Interactions](https://arxiv.org/abs/2503.16289)** `arXiv 2025.03` `Object-Aware-Motion`
  Inwoo Hwang, Bing Zhou, Young Min Kim, Jian Wang, Chuan Guo.
  Frames HSI as motion in-betweening between scene-aware keyframes.
  Links: [Project](https://inwoohwang.me/SceneMI/) · [Paper](https://arxiv.org/abs/2503.16289)

- ❌ **[DiffGrasp: Whole-Body Grasping Synthesis Guided by Object Motion Using a Diffusion Model](https://arxiv.org/abs/2412.20657)** `AAAI 2025` `Object-Aware-Motion`
  Yonghao Zhang, Qiang He, Yanguang Wan, Yinda Zhang, Xiaoming Deng, Cuixia Ma, Hongan Wang.
  Whole-body grasping diffusion conditioned on object motion with contact-aware losses.
  Links: [Paper](https://arxiv.org/abs/2412.20657)

- ❌ **[SceneAdapt: Scene-Aware Adaptation of Human Motion Diffusion](https://arxiv.org/abs/2510.13044)** `arXiv 2025.10` `Object-Aware-Motion`
  (see paper).
  Adapts pretrained motion diffusion to scene-conditioned generation without retraining.
  Links: [Paper](https://arxiv.org/abs/2510.13044)

- ❌ **[UniHM: Universal Human Motion Generation with Object Interactions in Indoor Scenes](https://arxiv.org/abs/2505.12774)** `arXiv 2025.05` `Object-Aware-Motion`
  (see paper).
  Unified motion generation in indoor scenes with object interactions and waypoints.
  Links: [Paper](https://arxiv.org/abs/2505.12774)

- ⭐ **[EgoChoir: Capturing 3D Human-Object Interaction Regions from Egocentric Views](https://arxiv.org/abs/2405.13659)** `NeurIPS 2024` `Object-Aware-Motion`
  Yuhang Yang, Wei Zhai, Chengfeng Wang, Chengjun Yu, Yang Cao, Zheng-Jun Zha.
  Predicts 3D affordance and human contact regions from egocentric video.
  Links: [Project](https://yyvhang.github.io/EgoChoir/) · [Code](https://github.com/yyvhang/EgoChoir_release) · [Paper](https://arxiv.org/abs/2405.13659)

- ⭐ 🧱 **[GraspXL: Generating Grasping Motions for Diverse Objects at Scale](https://arxiv.org/abs/2403.19649)** `ECCV 2024` `Object-Aware-Motion`
  Hui Zhang, Sammy Christen, Zicong Fan, Otmar Hilliges, Jie Song.
  Unified RL policy for grasping motions across diverse hand morphologies and objects.
  Links: [Project](https://eth-ait.github.io/graspxl/) · [Code](https://github.com/zdchan/graspxl) · [Paper](https://arxiv.org/abs/2403.19649)

- ⭐ **[HOIMotion: Forecasting Human Motion During HOIs Using Egocentric 3D Object Bounding Boxes](https://arxiv.org/abs/2407.00270)** `ISMAR 2024` `Object-Aware-Motion`
  Zhiming Hu, Zheming Yin, Daniel Häufle, Syn Schmitt, Andreas Bulling.
  Forecasts body motion conditioned on egocentric 3D object bounding boxes.
  Links: [Code](https://github.com/zhiminghu/HOIMotion) · [Paper](https://arxiv.org/abs/2407.00270)

- ⭐ **[Move as You Say, Interact as You Can (AffordMotion)](https://arxiv.org/abs/2403.18036)** `CVPR 2024 (Highlight)` `Object-Aware-Motion`
  Zan Wang, Yixin Chen, Baoxiong Jia, Puhao Li, Jinlu Zhang, Jingze Zhang, Tengyu Liu, Yixin Zhu, Wei Liang, Siyuan Huang.
  Scene affordance map as intermediate; cascaded ADM (affordance) + AMDM (motion) diffusion.
  Links: [Project](https://afford-motion.github.io/) · [Code](https://github.com/afford-motion/afford-motion) · [Paper](https://arxiv.org/abs/2403.18036)

- ⭐ 🧍 🧱 **[UniHSI: Unified Human-Scene Interaction via Prompted Chain-of-Contacts](https://arxiv.org/abs/2309.07918)** `ICLR 2024` `Object-Aware-Motion`
  Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei Zhang, Bo Dai, Dahua Lin, Jiangmiao Pang.
  LLM planner emits Chain-of-Contacts; unified controller executes physics-based HSI.
  Links: [Project](https://xizaoqu.github.io/unihsi/) · [Code](https://github.com/OpenRobotLab/UniHSI) · [Paper](https://arxiv.org/abs/2309.07918) · [Dataset](ScenePlan)

- 🌐 **[Generating Human Interaction Motions in Scenes with Text Control (TeSMo)](https://arxiv.org/abs/2404.10685)** `ECCV 2024` `Object-Aware-Motion`
  Hongwei Yi, Justus Thies, Michael J. Black, Xue Bin Peng, Davis Rempe.
  Two-stage diffusion: scene-aware navigation + interaction with text control.
  Links: [Project](https://research.nvidia.com/labs/toronto-ai/tesmo/) · [Paper](https://arxiv.org/abs/2404.10685)

- 🌐 **[GRIP: Generating Interaction Poses Using Spatial Cues and Latent Consistency](https://arxiv.org/abs/2308.11617)** `3DV 2024` `Object-Aware-Motion`
  Omid Taheri, Yi Zhou, Dimitrios Tzionas, Yang Zhou, Duygu Ceylan, Soren Pirk, Michael J. Black.
  Upgrades noisy body+object motion with realistic before/during/after hand interactions.
  Links: [Project](https://grip.is.tue.mpg.de/) · [Paper](https://arxiv.org/abs/2308.11617)

- ❌ **[NL2Contact: Natural Language Guided 3D Hand-Object Contact Modeling](https://arxiv.org/abs/2407.12727)** `ECCV 2024` `Object-Aware-Motion`
  Zhongqun Zhang, Hengfei Wang, Ziwei Yu, Yihua Cheng, Angela Yao, Hyung Jin Chang.
  Language-conditioned hand-object contact modeling with stratified generation.
  Links: [Paper](https://arxiv.org/abs/2407.12727)

- ❌ **[Purposer: Putting Human Motion Generation in Context](https://arxiv.org/abs/2404.12942)** `3DV 2024` `Object-Aware-Motion`
  Nicolas Ugrinovic, Thomas Lucas, Fabien Baradel, Philippe Weinzaepfel, Gregory Rogez, Francesc Moreno-Noguer.
  Generates motions in 3D scenes from sparse goals/keyframes/contact cues.
  Links: [Project](https://europe.naverlabs.com/research/publications/purposer-putting-human-motion-generation-in-context/) · [Paper](https://arxiv.org/abs/2404.12942)

- ⭐ **[DECO: Dense Estimation of 3D Human-Scene Contact In The Wild](https://arxiv.org/abs/2309.15273)** `ICCV 2023` `Object-Aware-Motion`
  Shashank Tripathi, Agniv Chatterjee, Jean-Claude Passy, Hongwei Yi, Dimitrios Tzionas, Michael J. Black.
  Estimates dense vertex-level body-scene contacts from in-the-wild RGB.
  Links: [Project](https://deco.is.tue.mpg.de/) · [Code](https://github.com/sha2nkt/deco) · [Paper](https://arxiv.org/abs/2309.15273) · [Dataset](DAMON)

- ⭐ **[Object Pop-Up: Can we infer 3D objects and their poses from human interactions alone?](https://arxiv.org/abs/2306.00777)** `CVPR 2023` `Object-Aware-Motion`
  Ilya A. Petrov, Riccardo Marin, Julian Chibane, Gerard Pons-Moll.
  Predicts 3D object pose and shape conditioned on human interaction pose alone.
  Links: [Project](https://virtualhumans.mpi-inf.mpg.de/object_popup/) · [Code](https://github.com/ptrvilya/object-popup) · [Paper](https://arxiv.org/abs/2306.00777)

- ⭐ **[SceneDiffuser: Diffusion-based Generation, Optimization, and Planning in 3D Scenes](https://arxiv.org/abs/2301.06015)** `CVPR 2023` `Object-Aware-Motion`
  Siyuan Huang, Zan Wang, Puhao Li, Baoxiong Jia, Tengyu Liu, Yixin Zhu, Wei Liang, Song-Chun Zhu.
  Unified diffusion for scene-conditioned generation, optimization, and planning.
  Links: [Project](https://scenediffuser.github.io/) · [Code](https://github.com/scenediffuser/Scene-Diffuser) · [Paper](https://arxiv.org/abs/2301.06015)

- ⭐ **[GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping](https://arxiv.org/abs/2112.11454)** `CVPR 2022` `Object-Aware-Motion`
  Omid Taheri, Vasileios Choutas, Michael J. Black, Dimitrios Tzionas.
  VAE + autoregressive infilling for 4D full-body grasping motion.
  Links: [Project](https://goal.is.tue.mpg.de/) · [Code](https://github.com/otaheri/GOAL) · [Paper](https://arxiv.org/abs/2112.11454)

- ⭐ **[HUMANISE: Language-conditioned Human Motion Generation in 3D Scenes](https://arxiv.org/abs/2210.09729)** `NeurIPS 2022` `Object-Aware-Motion`
  Zan Wang, Yixin Chen, Tengyu Liu, Yixin Zhu, Wei Liang, Siyuan Huang.
  Aligns mocap with scanned scenes to create large language-conditioned scene-motion dataset.
  Links: [Project](https://silvester.wang/HUMANISE/) · [Code](https://github.com/Silverster98/HUMANISE) · [Paper](https://arxiv.org/abs/2210.09729) · [Dataset](HUMANISE (synthetic))

- ⭐ **[HumanML3D: Generating Diverse and Natural 3D Human Motions from Texts](https://arxiv.org/abs/2203.13270)** `CVPR 2022` `Object-Aware-Motion`
  Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, Li Cheng.
  14,616 motions / 44,970 text descriptions; standard text-to-motion benchmark.
  Links: [Project](https://ericguo5513.github.io/text-to-motion/) · [Code](https://github.com/EricGuo5513/HumanML3D) · [Paper](https://arxiv.org/abs/2203.13270) · [Dataset](HumanML3D)

- ⭐ **[SAGA: Stochastic Whole-Body Grasping with Contact](https://arxiv.org/abs/2112.10103)** `ECCV 2022` `Object-Aware-Motion`
  Yan Wu, Jiahao Wang, Yan Zhang, Siwei Zhang, Otmar Hilliges, Fisher Yu, Siyu Tang.
  Stochastic whole-body grasping pose generation with motion infilling.
  Links: [Project](https://jiahaoplus.github.io/SAGA/saga.html) · [Code](https://github.com/JiahaoPlus/SAGA) · [Paper](https://arxiv.org/abs/2112.10103)

- ❌ **[ManipNet: Neural Manipulation Synthesis with a Hand-Object Spatial Representation](https://dl.acm.org/doi/10.1145/3450626.3459830)** `SIGGRAPH 2021 (TOG)` `Object-Aware-Motion`
  He Zhang, Yuting Ye, Takaaki Shiratori, Taku Komura.
  Spatial-representation neural manipulation synthesis for dexterous hand-object motion.
  Links: [Paper](https://dl.acm.org/doi/10.1145/3450626.3459830)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [DeVI: Physics-based Dexterous HOI via Synthetic Video Imitat](https://arxiv.org/abs/2604.20841) | — | ✅ | ❌ No Code | Hybrid 3D-human + 2D-object imitation targets train physics-based dexterous HOI  |
| 2026 | [HumanX: Toward Agile and Generalizable Humanoid Interaction ](https://arxiv.org/abs/2602.02473) | — | ✅ | ❌ No Code | XGen synthesizes humanoid HOI data from monocular videos; XMimic learns interact |
| 2026 | [InterPhys: Physics-aware Human Motion Synthesis in a Dynamic](https://arxiv.org/abs/2605.01036) | — | — | ❌ No Code | Two-stage diffusion with differentiable contact-force model for physically consi |
| 2026 | [SceMoS: Scene-Aware 3D Human Motion Synthesis with Geometry-](https://arxiv.org/abs/2602.20476) | — | — | ❌ No Code | Scene-aware motion synthesis via geometry-grounded planning tokens; SOTA on TRUM |
| 2025 | [TokenHSI: Unified Synthesis of Physical Human-Scene Interact](https://arxiv.org/abs/2503.19901) | — | — | ⭐ Code | Unified transformer policy with proprio + task tokens for multi-skill physical H |
| 2025 | [SceneMI: Motion In-betweening for Modeling Human-Scene Inter](https://arxiv.org/abs/2503.16289) | — | — | 🌐 Project Page | Frames HSI as motion in-betweening between scene-aware keyframes. |
| 2025 | [DiffGrasp: Whole-Body Grasping Synthesis Guided by Object Mo](https://arxiv.org/abs/2412.20657) | — | — | ❌ No Code | Whole-body grasping diffusion conditioned on object motion with contact-aware lo |
| 2025 | [SceneAdapt: Scene-Aware Adaptation of Human Motion Diffusion](https://arxiv.org/abs/2510.13044) | — | — | ❌ No Code | Adapts pretrained motion diffusion to scene-conditioned generation without retra |
| 2025 | [UniHM: Universal Human Motion Generation with Object Interac](https://arxiv.org/abs/2505.12774) | — | — | ❌ No Code | Unified motion generation in indoor scenes with object interactions and waypoint |
| 2024 | [EgoChoir: Capturing 3D Human-Object Interaction Regions from](https://arxiv.org/abs/2405.13659) | — | — | ⭐ Code | Predicts 3D affordance and human contact regions from egocentric video. |
| 2024 | [GraspXL: Generating Grasping Motions for Diverse Objects at ](https://arxiv.org/abs/2403.19649) | — | — | ⭐ Code | Unified RL policy for grasping motions across diverse hand morphologies and obje |
| 2024 | [HOIMotion: Forecasting Human Motion During HOIs Using Egocen](https://arxiv.org/abs/2407.00270) | — | — | ⭐ Code | Forecasts body motion conditioned on egocentric 3D object bounding boxes. |
| 2024 | [Move as You Say, Interact as You Can (AffordMotion)](https://arxiv.org/abs/2403.18036) | — | — | ⭐ Code | Scene affordance map as intermediate; cascaded ADM (affordance) + AMDM (motion)  |
| 2024 | [UniHSI: Unified Human-Scene Interaction via Prompted Chain-o](https://arxiv.org/abs/2309.07918) | — | — | ⭐ Code | LLM planner emits Chain-of-Contacts; unified controller executes physics-based H |
| 2024 | [Generating Human Interaction Motions in Scenes with Text Con](https://arxiv.org/abs/2404.10685) | — | — | 🌐 Project Page | Two-stage diffusion: scene-aware navigation + interaction with text control. |

## Whole-Body Motion Tracking and Imitation

_139 entries._

- ⭐ 🤖 🧍 **[GMR: General Motion Retargeting (Retargeter for TWIST)](https://github.com/YanjieZe/GMR)** `ICRA 2026` `Unitree H1, H1-2, G1, multi-robot` `WBC-Tracking`
  Yanjie Ze et al..
  Real-time CPU motion retargeting library handling SMPL→multi-humanoid mapping with foot-sliding/penetration fixes.
  Links: [Project](https://github.com/YanjieZe/GMR) · [Code](https://github.com/YanjieZe/GMR) · [Paper](https://github.com/YanjieZe/GMR)

- ⭐ 🤖 🧍 **[LIMMT: Less is More for Motion Tracking](https://arxiv.org/abs/2606.06953)** `ICML 2026` `Unitree G1 / humanoid` `Motion-Imitation`
  Yu Guan et al..
  Data-centric motion-tracking study showing that carefully filtered high-quality motions can outperform much larger noisy corpora.
  Links: [Project](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [Code](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [Paper](https://arxiv.org/abs/2606.06953)

- ⭐ 🤖 🧍 **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** `arXiv 2026.06` `humanoid` `Motion-Imitation`
  Zuxing Lu et al..
  Open IsaacLab-based WBC framework unifying joint, root, and end-effector reference modalities for humanoid motion mimicking.
  Links: [Project](https://github.com/Renforce-Dynamics/MultiModalWBC) · [Code](https://github.com/Renforce-Dynamics/MultiModalWBC) · [Paper](https://arxiv.org/abs/2606.04829)

- ⭐ 🤖 🧍 **[MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation](https://arxiv.org/abs/2602.08594)** `arXiv 2026.02` `humanoid` `WBC-Tracking`
  BAAI Humanoid Team.
  Trains a generalist tracker then rapidly adapts to specific teleop interfaces via additive residuals.
  Links: [Project](https://github.com/BAAI-Humanoid/MOSAIC) · [Code](https://github.com/BAAI-Humanoid/MOSAIC) · [Paper](https://arxiv.org/abs/2602.08594)

- ⭐ 🤖 🧍 **[Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control](https://arxiv.org/abs/2607.14182)** `RoboCup Symposium 2026 / arXiv 2026.07` `Unitree G1` `WBC`
  J. M. A. Marcelo et al..
  Routes live music and speech through semantic audio branches that select and schedule imitation-learned whole-body skills on a G1.
  Links: [Project](https://lab-rococo-sapienza.github.io/semantic-WBC/) · [Code](https://github.com/Lab-RoCoCo-Sapienza/semantic-WBC) · [Paper](https://arxiv.org/abs/2607.14182)

- ⭐ 🤖 🧍 **[TEXEDO: Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation](https://arxiv.org/abs/2606.22998)** `arXiv 2026.06` `Unitree G1` `Motion-Imitation`
  Jianuo Cao et al..
  Samples language-conditioned humanoid motions and selects candidates with a controller-feasibility verifier plus semantic alignment scoring.
  Links: [Project](https://jianuocao.github.io/TEXEDO/) · [Code](https://github.com/JianuoCao/TEXEDO) · [Paper](https://arxiv.org/abs/2606.22998) · [Dataset](https://huggingface.co/datasets/JianuoCao/TEXEDO)

- ⭐ 🤖 🧍 **[WholebodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](https://github.com/OpenDriveLab/WholebodyVLA)** `ICLR 2026` `humanoid` `WBC-Tracking`
  OpenDriveLab.
  Unified latent VLA architecture for whole-body humanoid loco-manipulation with tracking primitives.
  Links: [Project](https://github.com/OpenDriveLab/WholebodyVLA) · [Code](https://github.com/OpenDriveLab/WholebodyVLA) · [Paper](https://github.com/OpenDriveLab/WholebodyVLA)

- ⭐ **[ECO - Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking](https://arxiv.org/abs/2602.06445)** `arXiv 2026.02` `Locomotion`
  Energy-constrained RL for humanoid walking.
  Links: [Project](https://sites.google.com/view/eco-humanoid) · [Code](https://github.com/bigai-ai/ECO-humanoid) · [Paper](https://arxiv.org/abs/2602.06445)

- ⭐ 🧍 🧱 **[FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion](https://arxiv.org/abs/2606.31691)** `arXiv 2026.06` `MuJoCo Playground / HumanoidBench` `WBC`
  Guanchen Lu et al..
  Distributional actor-critic variant constrains exploratory actions to preserve policy plasticity under high-throughput humanoid locomotion training.
  Links: [Project](https://github.com/luge66/FastDSAC) · [Code](https://github.com/luge66/FastDSAC) · [Paper](https://arxiv.org/abs/2606.31691)

- 🌐 🤖 🧍 **[ADAPT: Analytical Disturbance-Aware Policy Training for Humanoid Locomotion](https://arxiv.org/abs/2606.16542)** `arXiv 2026.06` `Unitree G1` `Motion-Imitation`
  Bofan Lyu et al..
  Adds an analytical whole-body disturbance observer to humanoid locomotion policies so policies can respond to external pushes and asymmetric payloads.
  Links: [Project](https://blyu413.github.io/adapt-locomotion/) · [Paper](https://arxiv.org/abs/2606.16542)

- 🌐 🤖 🧍 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** `arXiv 2026.06` `humanoid` `Motion-Imitation`
  Siheng Zhao et al..
  Two-stage perceptive policy lets humanoids climb diverse ladders and manipulate in constrained vertical terrain.
  Links: [Project](https://ladderman-robot.github.io) · [Paper](https://arxiv.org/abs/2606.05873)

- 🌐 🤖 🧍 **[Mind Your Steps: A General Learning Framework for Accurate Humanoid Foothold Tracking](https://arxiv.org/abs/2606.08253)** `RSS 2026` `Booster T1 / humanoid` `Motion-Imitation`
  Alessandro Montenegro et al..
  Learning framework for accurate foothold placement on humanoids, improving safe navigation before manipulation.
  Links: [Project](https://github.com/MontenegroAlessandro/mind-your-steps) · [Paper](https://arxiv.org/abs/2606.08253)

- 🌐 🤖 🧍 **[Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot](https://arxiv.org/abs/2606.31807)** `IROS 2026 / arXiv 2026.06` `Booster T1` `WBC`
  Ethan Marot et al..
  Trains RL policies that transfer zero-shot to a Booster T1 humanoid wearing passive inline skates, producing edge-driven propulsion and perturbation recovery.
  Links: [Project](https://www.youtube.com/watch?v=-_APcOS7uFo) · [Paper](https://arxiv.org/abs/2606.31807)

- 🌐 🤖 🧍 **[RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning](https://arxiv.org/abs/2606.11092)** `arXiv 2026.06` `Unitree G1` `Motion-Imitation`
  Yichao Zhong et al..
  Three-stage motion-guided curriculum RL for stable, accurate high-impulse humanoid soccer shooting.
  Links: [Project](https://opendrivelab.com/RoboNaldo) · [Paper](https://arxiv.org/abs/2606.11092)

- 🌐 **[APEX - Learning Adaptive High-Platform Traversal for Humanoid Robots](https://arxiv.org/abs/2602.11143)** `arXiv 2026.02` `Locomotion`
  Adaptive high-platform traversal for humanoids.
  Links: [Project](https://apex-humanoid.github.io/) · [Paper](https://arxiv.org/abs/2602.11143)

- 🌐 **[Perceptive Humanoid Parkour - Chaining Dynamic Human Skills via Motion Matching](https://arxiv.org/abs/2602.15827)** `arXiv 2026.02` `Locomotion`
  Perceptive humanoid parkour by chaining dynamic skills via motion matching.
  Links: [Project](https://php-parkour.github.io/) · [Paper](https://arxiv.org/abs/2602.15827)

- 🌐 **[SafeFlow - Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating](https://arxiv.org/abs/2603.23983)** `arXiv 2026.03` `WBC-Tracking`
  Text-driven humanoid whole-body control using physics-guided rectified flow with safety gating.
  Links: [Project](https://hanbyelcho.info/safeflow/) · [Paper](https://arxiv.org/abs/2603.23983)

- 🌐 🧍 🧱 **[SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-based Humanoid Control](https://arxiv.org/abs/2605.22894)** `arXiv 2026.05` `physics-based humanoid` `Motion-Imitation`
  Jingyan Zhang et al..
  Joint action-state-text diffusion transformer for long-horizon language-driven physics-based humanoid control.
  Links: [Project](https://zhanglele12138.github.io/SCRIPT/) · [Paper](https://arxiv.org/abs/2605.22894)

- ⏳ 🤖 🧍 **[Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots](https://arxiv.org/abs/2606.03536)** `arXiv 2026.06` `Unitree G1` `Motion-Imitation`
  Tianchen Huang et al..
  Physics-aware diffusion transfers exemplar human motion style onto executable humanoid whole-body references.
  Links: [Project](https://huangtc233.github.io/bionic-style-transfer/) · [Paper](https://arxiv.org/abs/2606.03536)

- ⏳ 🤖 🧍 **[ReactiveBFM: Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control](https://arxiv.org/abs/2606.30362)** `arXiv 2026.06` `Unitree G1` `WBC`
  Xiao Chen et al..
  Combines a humanoid behavior foundation model with asynchronous closed-loop replanning so text-conditioned motions can react to tracking errors and moving targets.
  Links: [Project](https://xiao-chen.tech/reactivebfm/) · [Paper](https://arxiv.org/abs/2606.30362)

- ⏳ 🤖 🧍 **[Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids](https://arxiv.org/abs/2606.12814)** `arXiv 2026.06` `humanoid` `Motion-Imitation`
  Xiao Ren et al..
  Unified RL framework that keeps failed states in training and learns robust motion tracking plus fall recovery in one policy.
  Links: [Project](https://aislab-sustech.github.io/Stubborn/) · [Paper](https://arxiv.org/abs/2606.12814)

- ⏳ 🧍 🧱 **[MIND: Multi-Scale Intent Diffusion for Text-Driven Physics-Based Humanoid Control](https://arxiv.org/abs/2605.26006)** `arXiv 2026.05` `physics-based humanoid` `Motion-Imitation`
  Bin Li et al..
  Multi-scale intent diffusion bridges text semantics and low-level physics-based humanoid control.
  Links: [Project](https://binlee26.github.io/MIND_page/) · [Paper](https://arxiv.org/abs/2605.26006)

- ❌ 🤖 🧍 **[CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation](https://arxiv.org/abs/2602.15060)** `arXiv 2026.02` `Unitree G1` `WBC-Tracking`
  arXiv 2026.02.
  Closed-loop high-frequency localization feedback for drift-free long-horizon humanoid teleoperation; transformer trained 1.3K GPU-hr.
  Links: [Project](https://arxiv.org/abs/2602.15060) · [Paper](https://arxiv.org/abs/2602.15060)

- ❌ 🤖 🧍 **[Deep Whole-Body Parkour](https://arxiv.org/abs/2601.07701)** `arXiv 2026.01` `humanoid` `WBC-Tracking`
  arXiv 2026.01.
  Single policy for vault, dive-roll, and other multi-contact dynamic motions on unstructured terrain.
  Links: [Project](https://arxiv.org/abs/2601.07701) · [Paper](https://arxiv.org/abs/2601.07701)

- ❌ 🤖 🧍 **[EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control](https://arxiv.org/abs/2606.08495)** `arXiv 2026.06` `Unitree humanoid` `Motion-Imitation`
  Haoyang Ge et al..
  Learns an egocentric motion prior that maps human-view observations and intent into adaptive whole-body humanoid behaviors.
  Links: [Paper](https://arxiv.org/abs/2606.08495)

- ❌ 🤖 🧍 **[HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model](https://arxiv.org/abs/2602.11758)** `arXiv 2026.02` `humanoid` `WBC-Tracking`
  arXiv 2026.02.
  Dynamics-aware world model for agile humanoid object interaction with whole-body control.
  Links: [Project](https://arxiv.org/abs/2602.11758) · [Paper](https://arxiv.org/abs/2602.11758)

- ❌ 🤖 🧍 **[Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control](https://arxiv.org/abs/2602.21599)** `arXiv 2026.02` `humanoid (sim/real)` `WBC-Tracking`
  arXiv 2026.02.
  Closed-loop synthesis pipeline that grows tracker repertoire across martial-arts/dance/combat/sports/gymnastics.
  Links: [Project](https://arxiv.org/abs/2602.21599) · [Paper](https://arxiv.org/abs/2602.21599)

- ❌ 🤖 🧍 **[Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots](https://arxiv.org/abs/2606.25706)** `arXiv 2026.06` `Unitree G1` `WBC`
  Yumeng Liu et al..
  Tracks sparse low-rate upper-body task-space references with cached future trajectories, MPC-completed guidance, and self-guided post-training.
  Links: [Paper](https://arxiv.org/abs/2606.25706)

- ❌ 🤖 🧍 **[Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking](https://arxiv.org/abs/2604.17335)** `arXiv 2026.04` `Unitree G1` `WBC-Tracking`
  arXiv 2026.04.
  Couples a frozen motion generator with a finetuned tracker in a closed loop for real-time deployment.
  Links: [Project](https://arxiv.org/abs/2604.17335) · [Paper](https://arxiv.org/abs/2604.17335)

- ❌ 🤖 🧍 **[Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching](https://arxiv.org/abs/2602.15827)** `arXiv 2026.02` `humanoid` `WBC-Tracking`
  arXiv 2026.02.
  Train RL experts per motion, distill to a depth-image multi-skill student via DAgger+RL for vision-based parkour.
  Links: [Project](https://arxiv.org/abs/2602.15827) · [Paper](https://arxiv.org/abs/2602.15827)

- ❌ 🤖 🧍 **[PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410)** `arXiv 2026.03` `Unitree G1` `WBC-Tracking`
  arXiv 2026.03.
  Physics-aware whole-body VLA combining multi-brain latent flow matching with a robust tracker on G1.
  Links: [Project](https://arxiv.org/abs/2603.05410) · [Paper](https://arxiv.org/abs/2603.05410)

- ❌ 🤖 🧍 **[Predictive Style Matching: Natural and Robust Humanoid Locomotion](https://arxiv.org/abs/2606.07083)** `arXiv 2026.06` `humanoid` `Motion-Imitation`
  Simeon Nedelchev et al..
  Predictive style-matching objective improves natural humanoid gait while preserving disturbance recovery.
  Links: [Paper](https://arxiv.org/abs/2606.07083)

- ❌ 🤖 🧍 **[PTDL: Multi-Terrain Fall Recovery via Phase-Terrain Decoupled Learning](https://arxiv.org/abs/2606.08922)** `arXiv 2026.06` `Unitree G1` `Motion-Imitation`
  Xiaoyu Xu et al..
  Phase-terrain decoupled policy recovers from falls on slopes, gravel, and uneven terrain before resuming walking.
  Links: [Paper](https://arxiv.org/abs/2606.08922)

- ❌ 🤖 🧍 **[Robust and Generalized Humanoid Motion Tracking](https://arxiv.org/abs/2601.23080)** `arXiv 2026.01` `humanoid` `WBC-Tracking`
  arXiv 2026.01.
  Dynamics-conditioned command aggregation + fall-recovery curriculum tracking even at 1500% noise; breakdance-class motions.
  Links: [Project](https://arxiv.org/abs/2601.23080) · [Paper](https://arxiv.org/abs/2601.23080)

- ❌ 🧍 🧱 **[AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance](https://arxiv.org/abs/2606.29209)** `arXiv 2026.06` `humanoid` `WBC`
  Shuning Li et al..
  Trains a single latent whole-body controller that can follow arbitrary subsets of body keypoints for tracking, teleoperation, locomotion, and reaching.
  Links: [Paper](https://arxiv.org/abs/2606.29209)

- ❌ **[Heracles - Bridging Precise Tracking and Generative Synthesis for General Humanoid Control](https://arxiv.org/abs/2603.27756)** `arXiv 2026.03` `WBC-Tracking`
  Combines precise motion tracking with generative motion synthesis for general humanoid whole-body control.
  Links: [Paper](https://arxiv.org/abs/2603.27756)

- ❌ 🧍 🧱 **[LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception](https://arxiv.org/abs/2606.23249)** `arXiv 2026.06` `Unitree G1` `WBC`
  Yukun Luo et al..
  Distills a recurrent local planner on top of a raycast-conditioned humanoid locomotion policy for obstacle avoidance under short-range sensing.
  Links: [Paper](https://arxiv.org/abs/2606.23249)

- ❌ **[Now You See That - Learning End-to-End Humanoid Locomotion from Raw Pixels](https://arxiv.org/abs/2602.06382)** `arXiv 2026.02` `Locomotion`
  End-to-end humanoid locomotion from raw pixels.
  Links: [Paper](https://arxiv.org/abs/2602.06382)

- ❌ 🧍 🧱 **[PressMimic: Pressure-Guided Motion Capture and Control for Humanoid Robot Imitation](https://arxiv.org/abs/2606.26741)** `arXiv 2026.06` `humanoid` `Motion-Imitation`
  Yi Lu et al..
  Uses pressure as a shared physical-grounding signal for RGB-pressure human motion capture and pressure-supervised humanoid imitation policies.
  Links: [Paper](https://arxiv.org/abs/2606.26741)

- ❌ 🧍 🧱 **[RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC](https://arxiv.org/abs/2607.15701)** `arXiv 2026.07` `humanoid` `WBC`
  Ruochen Hou et al..
  Hierarchical planner uses RL to adapt visibility-graph geometry while a constrained MPC tracks collision-free humanoid navigation trajectories.
  Links: [Paper](https://arxiv.org/abs/2607.15701)

- ❌ 🧍 🧱 **[RGB: RL Guided Whole-Body MPPI for Humanoid Control](https://arxiv.org/abs/2606.25123)** `arXiv 2026.06` `Unitree G1` `WBC`
  Yunsoo Seo et al..
  Uses a pretrained RL policy as a dynamically feasible sampling prior for high-rate MPPI whole-body control on a 29-DoF G1 model.
  Links: [Paper](https://arxiv.org/abs/2606.25123)

- ❌ 🧍 🧱 **[VENOM: Versatile Embodied Network for Omni-bodied Motion Tracking](https://arxiv.org/abs/2606.16696)** `arXiv 2026.06` `multiple simulated humanoids` `Motion-Imitation`
  Siddharth Padmanabhan et al..
  Trains a GPT-style full-body motion tracker across multiple humanoid embodiments without splitting upper- and lower-body control.
  Links: [Paper](https://arxiv.org/abs/2606.16696)

- ❌ 🧍 🧱 **[Whole-Body Impedance Model Predictive Control for Safe Physical Human-Robot Interaction on Floating-Base Platforms](https://arxiv.org/abs/2606.14617)** `arXiv 2026.06` `floating-base humanoid / legged platform` `WBC`
  Yongyan Cao.
  Extends impedance MPC to floating-base robots by combining centroidal MPC, priority-driven WBC, and receding-horizon impedance allocation.
  Links: [Paper](https://arxiv.org/abs/2606.14617)

- ⭐ 🤖 🧍 **[Any2Track / OpenTrack: Track Any Motions under Any Disturbances](https://arxiv.org/abs/2509.13833)** `arXiv 2025.09` `Unitree G1` `WBC-Tracking`
  Galaxy General Robotics team.
  AnyTracker (general policy) + AnyAdapter (online history-conditioned dynamics adaptation) for robust tracking under disturbances.
  Links: [Project](https://zzk273.github.io/Any2Track/) · [Code](https://github.com/GalaxyGeneralRobotics/OpenTrack) · [Paper](https://arxiv.org/abs/2509.13833)

- ⭐ 🤖 🧍 **[ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://arxiv.org/abs/2502.01143)** `RSS 2025` `Unitree G1` `WBC-Tracking`
  Tairan He, Jiawei Gao, Wenli Xiao, Yuanhang Zhang, Zi Wang, Jiashun Wang, Zhengyi Luo, Guanzhi Wang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Linxi Fan, Yuke Zhu.
  Learns a delta-action residual that compensates sim2real dynamics gap, enabling extreme agile skills (jumps, spins, kicks) on G1.
  Links: [Project](https://agile.human2humanoid.com/) · [Code](https://github.com/LeCAR-Lab/ASAP) · [Paper](https://arxiv.org/abs/2502.01143)

- ⭐ 🤖 🧍 **[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)** `arXiv 2025.08` `Unitree G1` `WBC-Tracking`
  Takara Truong, Qiayuan Liao, Xiaoyu Huang, Guy Tevet, Koushil Sreenath, C. Karen Liu.
  Guided diffusion at inference time turns a tracker into a versatile controller doing aerial cartwheels, spin-kicks, and sprinting.
  Links: [Project](https://beyondmimic.github.io/) · [Code](https://github.com/HybridRobotics/whole_body_tracking) · [Paper](https://arxiv.org/abs/2508.08241)

- ⭐ 🤖 🧍 **[BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised RL](https://arxiv.org/abs/2511.04131)** `ICLR 2026` `Unitree G1` `Motion-Imitation / WBC-Tracking`
  Tairan He, Yi Chen, Wenli Xiao, et al. (CMU LeCAR Lab).
  Brings the FB-CPR behavioral foundation paradigm to a real Unitree G1 with reward-shaping, DR, and asymmetric history-conditioned learning.
  Links: [Project](https://lecar-lab.github.io/BFM-Zero/) · [Code](https://github.com/LeCAR-Lab/BFM-Zero) · [Paper](https://arxiv.org/abs/2511.04131)

- ⭐ 🤖 🧍 **[Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible 3D-printed Humanoid](https://arxiv.org/abs/2504.17249)** `RSS 2025 demo` `Berkeley Humanoid Lite` `Locomotion`
  Yufeng Chi, Qiayuan Liao, Junfeng Long, et al..
  Fully open 3D-printed humanoid with end-to-end RL locomotion stack.
  Links: [Project](https://lite.berkeley-humanoid.com/) · [Code](https://github.com/HybridRobotics/BerkeleyHumanoidLite) · [Paper](https://arxiv.org/abs/2504.17249)

- ⭐ 🤖 🧍 **[FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](https://arxiv.org/abs/2505.06776)** `L4DC 2026` `Multiple humanoids` `WBC-Tracking`
  Yuanhang Zhang, Yifu Yuan, Wenli Xiao, Tairan He, Guanqi He, Mingxi Lin, Changliu Liu, Guanya Shi.
  Dual-agent RL achieving 2× more accurate upper-body tracking under heavy external forces (cart-pull 100N, payload 20N, door 40N).
  Links: [Project](https://lecar-lab.github.io/falcon-humanoid/) · [Code](https://github.com/LeCAR-Lab/FALCON) · [Paper](https://arxiv.org/abs/2505.06776)

- ⭐ 🤖 🧍 **[GentleHumanoid: Whole-Body Motion Tracking with Compliance](https://github.com/Axellwppr/gentle-humanoid)** `arXiv 2025` `humanoid` `WBC-Tracking`
  Anonymous (project page).
  Inference + deploy code for compliant whole-body motion tracking.
  Links: [Project](https://github.com/Axellwppr/gentle-humanoid) · [Code](https://github.com/Axellwppr/gentle-humanoid) · [Paper](https://github.com/Axellwppr/gentle-humanoid)

- ⭐ 🤖 🧍 **[GMT: General Motion Tracking for Humanoid Whole-Body Control](https://arxiv.org/abs/2506.14770)** `arXiv 2025.06` `Unitree G1` `WBC-Tracking`
  Zixuan Chen, Mazeyu Ji, Xuxin Cheng, Xuanbin Peng, Xue Bin Peng, Xiaolong Wang.
  Single tracker with motion-MoE + adaptive sampling that handles diverse motions on a real G1.
  Links: [Project](https://gmt-humanoid.github.io/) · [Code](https://github.com/zixuan417/humanoid-general-motion-tracking) · [Paper](https://arxiv.org/abs/2506.14770)

- ⭐ 🤖 🧍 **[HumanoidVerse: Multi-Simulator Framework for Humanoid Sim-to-Real Learning](https://github.com/LeCAR-Lab/HumanoidVerse)** `open-source release` `Unitree H1, G1` `WBC-Tracking`
  CMU LeCAR Lab.
  Unified multi-simulator (IsaacGym/IsaacSim/Genesis/MuJoCo) humanoid RL training framework underpinning ASAP, FALCON, BFM-Zero.
  Links: [Project](https://github.com/LeCAR-Lab/HumanoidVerse) · [Code](https://github.com/LeCAR-Lab/HumanoidVerse) · [Paper](https://github.com/LeCAR-Lab/HumanoidVerse)

- ⭐ 🤖 🧍 **[JAEGER: Dual-Level Humanoid Whole-Body Controller](https://arxiv.org/abs/2505.06584)** `arXiv 2025.05` `Two humanoid platforms (incl. Unitree)` `WBC-Tracking`
  Ziluo Ding, Haobin Jiang, Yuxuan Wang, Zhenguo Sun, Yu Zhang, Xiaojie Niu, Ming Yang, Weishuai Zeng, Xinrun Xu, Zongqing Lu.
  Decouples upper- and lower-body controllers and supports both root-velocity and joint-angle commands.
  Links: [Project](https://beingbeyond.github.io/Jaeger/) · [Code](https://github.com/BeingBeyond/Jaeger) · [Paper](https://arxiv.org/abs/2505.06584)

- ⭐ 🤖 🧍 **[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://arxiv.org/abs/2506.12851)** `arXiv 2025.06 (NeurIPS 2025 sub.)` `Unitree G1` `WBC-Tracking`
  Tencent ARC / TeleHuman Group.
  Bi-level adaptive tolerance curriculum that lets a humanoid learn kungfu and dance from a single mocap clip.
  Links: [Project](https://kungfu-bot.github.io/) · [Code](https://github.com/TeleHuman/PBHC) · [Paper](https://arxiv.org/abs/2506.12851)

- ⭐ 🤖 🧍 **[PhysHSI: Towards Real-World Generalizable and Natural Humanoid-Scene Interaction](https://arxiv.org/abs/2510.11072)** `arXiv 2025` `Unitree G1` `Locomotion`
  Huayi Wang, Wentao Zhang, Runyi Yu, et al..
  Real-world generalizable humanoid-scene interaction (sitting, climbing, manipulating) via tracking + adversarial priors.
  Links: [Project](https://physhsi.github.io/) · [Code](https://github.com/InternRobotics/PhysHSI) · [Paper](https://arxiv.org/abs/2510.11072)

- ⭐ 🤖 🧍 **[SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820)** `arXiv 2025.11` `Multi-humanoid (GR00T)` `WBC-Tracking`
  NVIDIA GEAR.
  Scales motion tracking to 42M params, 700h data, 9k GPU-hr; ships universal kinematic planner unifying VR / video / VLA inputs.
  Links: [Project](https://nvlabs.github.io/SONIC/) · [Code](https://github.com/NVlabs/GR00T-WholeBodyControl) · [Paper](https://arxiv.org/abs/2511.07820)

- ⭐ 🤖 🧍 **[TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832)** `arXiv 2025.11` `Unitree G1 + 2-DoF neck` `WBC-Tracking`
  Yanjie Ze et al. (Amazon FAR).
  Mocap-free, PICO4U-VR-based portable WBC teleop collecting 100 demos in 15 min at near-100% success.
  Links: [Project](https://yanjieze.com/TWIST2/) · [Code](https://github.com/amazon-far/TWIST2) · [Paper](https://arxiv.org/abs/2511.02832)

- ⭐ 🤖 🧍 **[TWIST: Teleoperated Whole-Body Imitation System](https://arxiv.org/abs/2505.02833)** `CoRL 2025` `Unitree G1` `WBC-Tracking`
  Yanjie Ze, Zixuan Chen, João Pedro Araújo, Zi-ang Cao, Xue Bin Peng, Jiajun Wu, C. Karen Liu.
  End-to-end teleop pipeline (mocap → retargeting → tracker) achieving high-quality whole-body imitation on real G1.
  Links: [Project](https://yanjieze.com/TWIST/) · [Code](https://github.com/YanjieZe/TWIST) · [Paper](https://arxiv.org/abs/2505.02833)

- ⭐ 🤖 🧍 **[UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots](https://arxiv.org/abs/2507.07356)** `CoRL 2025` `Unitree G1` `WBC-Tracking`
  Kangning Yin et al..
  CVAE-based universal policy with privileged-teacher → CVAE-student → adaptation pipeline; tracks under partial observations.
  Links: [Project](https://yinkangning0124.github.io/Humanoid-UniTracker/) · [Code](https://github.com/yinkangning0124/Humanoid-UniTracker) · [Paper](https://arxiv.org/abs/2507.07356)

- ⭐ 🤖 🧍 **[VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation](https://arxiv.org/abs/2509.20322)** `arXiv 2025.09` `Unitree G1` `WBC-Tracking`
  Shaofeng Yin, Yanjie Ze, Hong-Xing Yu, C. Karen Liu, Jiajun Wu.
  Low-level keypoint tracker + high-level vision policy delivering box lifting, pushing, soccer dribble/kick on real G1 zero-shot.
  Links: [Project](https://visualmimic.github.io/) · [Code](https://github.com/visualmimic/VisualMimic) · [Paper](https://arxiv.org/abs/2509.20322)

- ⭐ 🧍 🧱 **[SkillMimic-V2: Learning Robust and Generalizable Interaction Skills from Sparse and Noisy Demonstrations](https://arxiv.org/abs/2505.02094)** `SIGGRAPH 2025` `simulated humanoid + ball` `Motion-Imitation`
  Runyi Yu, Yinhuai Wang, Qihan Zhao, Hok Wai Tsui, Jingbo Wang, Ping Tan, Qifeng Chen.
  Robust interaction-skill learning from few/noisy demonstrations through stitched trajectory expansion.
  Links: [Project](https://ingrid789.github.io/SkillMimicV2/) · [Code](https://github.com/wyhuai/SkillMimic-V2) · [Paper](https://arxiv.org/abs/2505.02094)

- 🌐 🤖 🧍 **[DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion](https://arxiv.org/abs/2509.14353)** `arXiv 2025.09` `Unitree G1` `WBC-Tracking`
  arXiv 2025.09.
  Diffusion prior trained on human motion provides reward signal that guides RL to discover scene-interaction skills on G1.
  Links: [Project](https://genrobo.github.io/DreamControl/) · [Code](⏳) · [Paper](https://arxiv.org/abs/2509.14353)

- 🌐 🤖 🧍 **[HugWBC: A Unified and General Humanoid Whole-Body Controller for Versatile Locomotion](https://arxiv.org/abs/2502.03206)** `RSS 2025` `Unitree H1` `WBC-Tracking`
  Yufei Xue, Wentao Dong, Minghuan Liu, Weinan Zhang, Jiangmiao Pang.
  Single policy producing customizable gaits (frequency, swing, height, pitch) plus real-time upper-body teleop intervention.
  Links: [Project](https://hugwbc.github.io/) · [Paper](https://arxiv.org/abs/2502.03206)

- 🌐 🤖 🧍 **[OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction](https://arxiv.org/abs/2509.26633)** `arXiv 2025.09` `Unitree G1` `WBC-Tracking`
  Anonymous (project page authors) et al..
  Interaction-mesh-based retargeter that preserves agent-terrain-object contact, enabling 30s parkour on G1 with 5 reward terms.
  Links: [Project](https://omniretarget.github.io/) · [Code](https://github.com/OmniRetarget/OmniRetarget) · [Paper](https://arxiv.org/abs/2509.26633)

- 🌐 🤖 🧍 **[ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning](https://arxiv.org/abs/2510.05070)** `arXiv 2025.10` `Unitree G1` `WBC-Tracking`
  Siheng Zhao, Yanjie Ze, Yue Wang, C. Karen Liu, Pieter Abbeel, Guanya Shi, Rocky Duan.
  Two-stage residual on top of a frozen GMT base policy adds object interaction with contact and point-cloud rewards.
  Links: [Project](https://resmimic.github.io/) · [Paper](https://arxiv.org/abs/2510.05070)

- 🌐 🤖 🧍 **[Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](https://arxiv.org/abs/2510.02252)** `arXiv 2025.10` `multi-humanoid` `WBC-Tracking`
  João Pedro Araújo et al..
  Systematic study showing retargeting quality dominates downstream tracking performance.
  Links: [Project](https://jaraujo98.github.io/retargeting_matters/) · [Code](https://github.com/YanjieZe/GMR) · [Paper](https://arxiv.org/abs/2510.02252)

- 🌐 **[BeamDojo - Learning Agile Humanoid Locomotion on Sparse Footholds](https://arxiv.org/abs/2502.10363)** `arXiv 2025.02` `Locomotion`
  Agile humanoid locomotion on sparse footholds.
  Links: [Project](https://why618188.github.io/beamdojo/) · [Paper](https://arxiv.org/abs/2502.10363)

- 🌐 **[Embrace Collisions - Humanoid Shadowing for Deployable Contact-Agnostics Motions](https://arxiv.org/abs/2502.01465)** `arXiv 2025.02` `WBC-Tracking`
  Contact-agnostic humanoid shadowing under collisions.
  Links: [Project](https://project-instinct.github.io/) · [Paper](https://arxiv.org/abs/2502.01465)

- 🌐 **[FastTD3 - Simple, Fast, and Capable Reinforcement Learning for Humanoid Control](https://arxiv.org/abs/2505.22642)** `arXiv 2025.05` `Locomotion`
  Simple fast capable RL for humanoid control.
  Links: [Project](https://younggyo.me/fast_td3/) · [Paper](https://arxiv.org/abs/2505.22642)

- 🌐 **[HuB - Learning Extreme Humanoid Balance](https://arxiv.org/abs/2505.07294)** `arXiv 2025.05` `WBC-Tracking`
  Extreme balance behaviors for humanoid robots.
  Links: [Project](https://hub-robot.github.io/) · [Paper](https://arxiv.org/abs/2505.07294)

- 🌐 **[HWC-Loco - A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion](https://arxiv.org/abs/2503.00923)** `arXiv 2025.03` `Locomotion`
  Hierarchical whole-body control for robust humanoid locomotion.
  Links: [Project](https://simonlinsx.github.io/HWC_Loco/) · [Paper](https://arxiv.org/abs/2503.00923)

- 🌐 **[MoRE - Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains](https://arxiv.org/abs/2506.08840)** `arXiv 2025.06` `Locomotion`
  Mixture of residual experts for lifelike humanoid gaits.
  Links: [Project](https://more-humanoid.github.io/) · [Paper](https://arxiv.org/abs/2506.08840)

- 🌐 **[SLAC - Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning](https://arxiv.org/abs/2506.04147)** `arXiv 2025.06` `WBC-Tracking`
  Sim-pretrained latent action space for real-world whole-body RL.
  Links: [Project](https://robo-rl.github.io/) · [Paper](https://arxiv.org/abs/2506.04147)

- 🌐 **[VB-Com - Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception](https://arxiv.org/abs/2502.14814)** `arXiv 2025.02` `Locomotion`
  Vision-blind composite humanoid locomotion under deficient perception.
  Links: [Project](https://renjunli99.github.io/vbcom.github.io/) · [Paper](https://arxiv.org/abs/2502.14814)

- ❌ 🤖 🧍 **[Coordinated Humanoid Locomotion with Symmetry Equivariant RL Policy (Symmetry-Aware)](https://arxiv.org/abs/2508.01247)** `arXiv 2025` `Unitree G1` `Locomotion`
  Buqing Nie, Yangqing Fu, Jingtian Ji, Yanjie Ze, Xuxin Cheng, Yue Gao.
  Strict symmetry-equivariant actor and symmetry-invariant critic improve velocity tracking up to 40% on G1.
  Links: [Paper](https://arxiv.org/abs/2508.01247)

- ❌ 🤖 🧍 **[From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2506.12779)** `arXiv 2025.06` `humanoid` `WBC-Tracking`
  arXiv 2025.06.
  Distills multiple skill-specific experts into a single generalist whole-body controller.
  Links: [Project](https://arxiv.org/abs/2506.12779) · [Paper](https://arxiv.org/abs/2506.12779)

- ❌ 🤖 🧍 **[From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance](https://arxiv.org/abs/2510.14952)** `arXiv 2025.10` `humanoid` `WBC-Tracking`
  arXiv 2025.10.
  Skips explicit retargeting by guiding humanoid policy with a learned motion latent from language.
  Links: [Project](https://arxiv.org/abs/2510.14952) · [Paper](https://arxiv.org/abs/2510.14952)

- ❌ 🤖 🧍 **[Learning Sim-to-Real Humanoid Locomotion in 15 Minutes (FastSAC / FastTD3)](https://arxiv.org/abs/2512.01996)** `arXiv 2025.12` `Unitree G1` `WBC-Tracking`
  Younggyo Seo et al..
  FastSAC/FastTD3 train humanoid locomotion and motion-tracking policies in 15 min on a single RTX 4090.
  Links: [Project](https://arxiv.org/abs/2512.01996) · [Paper](https://arxiv.org/abs/2512.01996)

- ❌ 🤖 🧍 **[RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control](https://arxiv.org/abs/2506.12769)** `arXiv 2025.06` `Unitree G1` `Motion-Imitation`
  arXiv 2025.06.
  Uses physics-based reward feedback to align large motion models with humanoid hardware capabilities.
  Links: [Project](https://arxiv.org/abs/2506.12769) · [Paper](https://arxiv.org/abs/2506.12769)

- ❌ 🤖 🧍 **[RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking](https://arxiv.org/abs/2509.20717)** `arXiv 2025.09` `Unitree G1` `WBC-Tracking`
  Yunshen Chen et al..
  One-stage residual-action RL pipeline tracking multi-minute high-energy dance on G1 zero-shot.
  Links: [Project](https://arxiv.org/html/2509.20717) · [Paper](https://arxiv.org/abs/2509.20717)

- ❌ 🤖 🧍 **[Towards Adaptable Humanoid Control via Adaptive Motion Tracking](https://arxiv.org/abs/2510.14454)** `arXiv 2025.10` `humanoid` `WBC-Tracking`
  arXiv 2025.10.
  Adaptive motion tracking for humanoid control across novel conditions.
  Links: [Project](https://arxiv.org/abs/2510.14454) · [Paper](https://arxiv.org/abs/2510.14454)

- ❌ 🤖 🧍 **[ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation](https://arxiv.org/abs/2507.06905)** `arXiv 2025.07` `humanoid` `WBC-Tracking`
  arXiv 2025.07.
  Single policy with fine-grained command space for combined locomotion and manipulation.
  Links: [Project](https://arxiv.org/abs/2507.06905) · [Code](❌) · [Paper](https://arxiv.org/abs/2507.06905)

- ❌ 🤖 🧍 **[Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space](https://arxiv.org/abs/2505.10918)** `arXiv 2025.05` `humanoid` `WBC-Tracking`
  arXiv 2025.05.
  Builds a real-world-ready skill space for humanoid reaching with whole-body coordination.
  Links: [Project](https://arxiv.org/abs/2505.10918) · [Code](❌) · [Paper](https://arxiv.org/abs/2505.10918)

- ❌ 🤖 🧍 **[Visual Imitation Enables Contextual Humanoid Control (VIEW)](https://arxiv.org/abs/2505.03729)** `arXiv 2025.05` `humanoid` `Motion-Imitation`
  arXiv 2025.05.
  Visual imitation framework providing contextual humanoid control from videos.
  Links: [Project](https://arxiv.org/abs/2505.03729) · [Code](https://github.com/HybridRobotics/VideoMimic) · [Paper](https://arxiv.org/abs/2505.03729)

- ❌ **[Booster Gym - An End-to-End RL Framework for Humanoid Robot Locomotion](https://arxiv.org/abs/2506.15132)** `arXiv 2025.06` `Locomotion`
  End-to-end RL framework for humanoid locomotion.
  Links: [Paper](https://arxiv.org/abs/2506.15132)

- ❌ **[DPL - Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction](https://arxiv.org/abs/2510.07152)** `arXiv 2025.10` `Locomotion`
  Depth-only perceptive humanoid locomotion.
  Links: [Paper](https://arxiv.org/abs/2510.07152)

- ❌ **[GBC - Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation](https://arxiv.org/abs/2508.09960)** `arXiv 2025.08` `WBC-Tracking`
  Generalized behavior cloning for whole-body humanoid imitation.
  Links: [Paper](https://arxiv.org/abs/2508.09960)

- ❌ **[HiFAR - Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery](https://arxiv.org/abs/2502.20061)** `arXiv 2025.02` `WBC-Tracking`
  Multi-stage curriculum for high-dynamic humanoid fall recovery.
  Links: [Paper](https://arxiv.org/abs/2502.20061)

- ❌ **[Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning](https://arxiv.org/abs/2502.17219)** `arXiv 2025.02` `Locomotion`
  Whole-body locomotion on narrow terrain via dynamic balance.
  Links: [Paper](https://arxiv.org/abs/2502.17219)

- ❌ **[It Takes Two - Learning Interactive Whole-Body Control Between Humanoid Robots](https://arxiv.org/abs/2510.10206)** `arXiv 2025.10` `WBC-Tracking`
  Interactive whole-body control between two humanoid robots.
  Links: [Paper](https://arxiv.org/abs/2510.10206)

- ❌ **[KungfuBot 2 - Learning Versatile Motion Skills for Humanoid Whole-Body Control](https://arxiv.org/abs/2509.16638)** `arXiv 2025.09` `WBC-Tracking`
  Versatile motion skills for humanoid whole-body control.
  Links: [Paper](https://arxiv.org/abs/2509.16638)

- ❌ **[Learning Perceptive Humanoid Locomotion over Challenging Terrain](https://arxiv.org/abs/2503.00692)** `arXiv 2025.03` `Locomotion`
  Perceptive humanoid locomotion on challenging terrain.
  Links: [Paper](https://arxiv.org/abs/2503.00692)

- ❌ **[Natural Humanoid Robot Locomotion with Generative Motion Prior](https://arxiv.org/abs/2503.09015)** `arXiv 2025.03` `Locomotion`
  Natural humanoid locomotion with generative motion prior.
  Links: [Paper](https://arxiv.org/abs/2503.09015)

- ❌ **[SignBot - Learning Human-to-Humanoid Sign Language Interaction](https://arxiv.org/abs/2505.24266)** `arXiv 2025.05` `WBC-Tracking`
  Sign language interaction from human to humanoid.
  Links: [Paper](https://arxiv.org/abs/2505.24266)

- ❌ **[SoftMimic - Learning Compliant Whole-body Control from Examples](https://arxiv.org/abs/2510.17792)** `arXiv 2025.10` `WBC-Tracking`
  Learns compliant whole-body humanoid control from example motions.
  Links: [Paper](https://arxiv.org/abs/2510.17792)

- ❌ **[StyleLoco - Generative Adversarial Distillation for Natural Humanoid Robot Locomotion](https://arxiv.org/abs/2503.15082)** `arXiv 2025.03` `Locomotion`
  GAN distillation for natural humanoid locomotion.
  Links: [Paper](https://arxiv.org/abs/2503.15082)

- ❌ **[Thor - Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments](https://arxiv.org/abs/2510.26280)** `arXiv 2025.10` `WBC-Tracking`
  Human-level whole-body reactions for contact-rich environments.
  Links: [Paper](https://arxiv.org/abs/2510.26280)

- ⭐ 🤖 🧍 **[Expressive Whole-Body Control for Humanoid Robots (ExBody)](https://arxiv.org/abs/2402.16796)** `RSS 2024` `Unitree H1` `WBC-Tracking`
  Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang.
  Decouples upper-body imitation from lower-body velocity tracking to imitate AMASS on a real H1.
  Links: [Project](https://expressive-humanoid.github.io/) · [Code](https://github.com/chengxuxin/expressive-humanoid) · [Paper](https://arxiv.org/abs/2402.16796)

- ⭐ 🤖 🧍 **[H2O: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://arxiv.org/abs/2403.04436)** `IROS 2024` `Unitree H1` `WBC-Tracking`
  Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, Guanya Shi.
  Learns a robust whole-body tracker via PHC-filtered AMASS, enabling RGB-camera teleop on a real H1 zero-shot.
  Links: [Project](https://human2humanoid.com/) · [Code](https://github.com/LeCAR-Lab/human2humanoid) · [Paper](https://arxiv.org/abs/2403.04436)

- ⭐ 🤖 🧍 **[HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](https://arxiv.org/abs/2410.21229)** `ICRA 2025` `Unitree H1 (19-DoF)` `WBC-Tracking`
  Tairan He, Wenli Xiao, Toru Lin, Zhengyi Luo, Zhenjia Xu, Zhenyu Jiang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Yuke Zhu, Linxi Fan.
  Distills a kinematic-tracking oracle into a 1.5M-param student via proprioception+command masking, unifying 15+ control modes.
  Links: [Project](https://hover-versatile-humanoid.github.io/) · [Code](https://github.com/NVlabs/HOVER) · [Paper](https://arxiv.org/abs/2410.21229)

- ⭐ 🤖 🧍 **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454)** `CoRL 2024` `Custom 33-DoF humanoid (Unitree H1 base)` `WBC-Tracking`
  Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn.
  HST shadowing policy + HIT imitation transformer let a humanoid mimic humans from RGB and learn whole-body manipulation tasks.
  Links: [Project](https://humanoid-ai.github.io/) · [Code](https://github.com/MarkFzp/humanplus) · [Paper](https://arxiv.org/abs/2406.10454)

- ⭐ 🤖 **[Hybrid Internal Model: Learning Agile Legged Locomotion with Simulated Robot Response (HIMLoco)](https://arxiv.org/abs/2312.11460)** `ICLR 2024` `Unitree A1/Go1/Go2` `Locomotion`
  Junfeng Long, Zirui Wang, Quanyi Li, Liu Cao, Jiawei He, Jiangmiao Pang.
  Estimates external states implicitly via contrastive embedding aligned with successor robot response.
  Links: [Project](https://junfeng-long.github.io/HIMLoco/) · [Code](https://github.com/OpenRobotLab/HIMLoco) · [Paper](https://arxiv.org/abs/2312.11460)

- ⭐ 🤖 🧍 **[OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](https://arxiv.org/abs/2406.08858)** `CoRL 2024` `Unitree H1 + dexterous hands` `WBC-Tracking`
  Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, Guanya Shi.
  Universal pose-as-interface humanoid control supporting VR teleop, language, RGB, and learned autonomy from demos.
  Links: [Project](https://omni.human2humanoid.com/) · [Code](https://github.com/LeCAR-Lab/human2humanoid) · [Paper](https://arxiv.org/abs/2406.08858)

- ⭐ 🤖 🧍 **[ProtoMotions](https://nvlabs.github.io/ProtoMotions/)** `Open-source framework` `SMPL / G1 / multi-robot` `Motion-Imitation`
  NVIDIA Spatial Intelligence Lab (NVlabs).
  GPU-accelerated framework unifying physics-based character animation, digital humans, and humanoid robotics with shared infra.
  Links: [Project](https://github.com/NVlabs/ProtoMotions) · [Code](https://github.com/NVlabs/ProtoMotions) · [Paper](https://nvlabs.github.io/ProtoMotions/)

- ⭐ 🧍 🧱 **[FB-CPR / Meta Motivo: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models](https://arxiv.org/abs/2412.09858)** `NeurIPS 2024 (workshop) / Meta AI release` `SMPL humanoid (Mujoco)` `Motion-Imitation`
  Andrea Tirinzoni, Ahmed Touati, Jesse Farebrother, et al. (Meta FAIR).
  First behavioral foundation model that prompts a single humanoid policy to track motions, reach goals, or optimize rewards zero-shot.
  Links: [Project](https://metamotivo.metademolab.com/) · [Code](https://github.com/facebookresearch/metamotivo) · [Paper](https://arxiv.org/abs/2412.09858)

- ⭐ 🧍 🧱 **[I-CTRL: Imitation to Control Humanoid Robots Through Bounded Residual RL](https://arxiv.org/abs/2405.08726)** `IEEE RAM 2024 (Special Issue on Humanoids)` `4 humanoids (sim)` `WBC-Tracking`
  Yashuai Yan, Esteve Valls Mascaro, Tobias Egle, Dongheui Lee.
  Constrained residual RL on top of kinematic retargeting; one agent imitates large-scale data across 4 robots.
  Links: [Project](https://evm7.github.io/I-CTRL/) · [Code](https://github.com/Evm7/I-CTRL) · [Paper](https://arxiv.org/abs/2405.08726)

- ⭐ **[Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies](https://arxiv.org/abs/2410.11825)** `arXiv 2024.10` `Locomotion`
  Lipschitz-constrained policies yield smooth humanoid locomotion.
  Links: [Project](https://lipschitz-constrained-policy.github.io/) · [Code](https://github.com/zixuan417/smooth-humanoid-locomotion) · [Paper](https://arxiv.org/abs/2410.11825)

- ⭐ 🧍 🧱 **[MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](https://arxiv.org/abs/2409.14393)** `SIGGRAPH Asia 2024` `simulated humanoid` `Motion-Imitation`
  Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, Xue Bin Peng.
  Single transformer controller that solves tracking, joystick, keyframe, text, and object-interaction control via masked motion inpainting.
  Links: [Project](https://research.nvidia.com/labs/par/maskedmimic/) · [Code](https://github.com/NVlabs/ProtoMotions) · [Paper](https://arxiv.org/abs/2409.14393)

- ⭐ 🧍 🧱 **[MimicKit](https://github.com/xbpeng/MimicKit)** `open-source toolkit` `simulated humanoid` `Motion-Imitation`
  Xue Bin Peng.
  Lightweight unified suite implementing DeepMimic, AMP, and friends for motion imitation training.
  Links: [Project](https://github.com/xbpeng/MimicKit) · [Code](https://github.com/xbpeng/MimicKit) · [Paper](https://github.com/xbpeng/MimicKit)

- ⭐ 🧍 🧱 **[MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations](https://arxiv.org/abs/2310.10198)** `SIGGRAPH 2024 (TOG)` `simulated humanoid` `Motion-Imitation`
  Heyuan Yao, Zhenhua Song, Yuyang Zhou, Tenglong Ao, Baoquan Chen, Libin Liu.
  VQ-VAE + model-based RL motion controller scalable to tens of hours of data; integrates with LLMs.
  Links: [Project](https://moconvq.github.io/) · [Code](https://github.com/heyuanYao-PKU/MoConVQ) · [Paper](https://arxiv.org/abs/2310.10198)

- ⭐ 🧍 🧱 **[PULSE: Universal Humanoid Motion Representations for Physics-Based Control](https://arxiv.org/abs/2310.04582)** `ICLR 2024 (Spotlight)` `SMPL humanoid` `Motion-Imitation`
  Zhengyi Luo, Jinkun Cao, Josh Merel, Alexander Winkler, Jing Huang, Kris Kitani, Weipeng Xu.
  Distills PHC into a 32-D variational motion latent that covers 99.8% of AMASS and serves as a foundation prior for downstream hierarchical RL.
  Links: [Project](http://www.zhengyiluo.com/PULSE/) · [Code](https://github.com/ZhengyiLuo/PULSE) · [Paper](https://arxiv.org/abs/2310.04582)

- ⭐ 🧍 🧱 **[SkillMimic: Learning Reusable Basketball Skills from Demonstrations](https://arxiv.org/abs/2408.15270)** `arXiv 2024.08` `simulated humanoid + ball` `Motion-Imitation`
  Yinhuai Wang, Qihan Zhao, Runyi Yu, Hok Wai Tsui, Ying Shan, Jianbo Liu.
  Unified config to learn dribbling/layups/shooting from demonstrations; high-level controller composes acquired skills.
  Links: [Project](https://ingrid789.github.io/SkillMimic/) · [Code](https://github.com/wyhuai/SkillMimic) · [Paper](https://arxiv.org/abs/2408.15270)

- 🧩 🤖 🧍 **[Berkeley Humanoid: A Research Platform for Learning-based Control](https://arxiv.org/abs/2407.21781)** `arXiv / IROS 2025` `Berkeley Humanoid (mid-scale)` `Locomotion`
  Qiayuan Liao, Bike Zhang, Xuanyu Huang, Xiaoyu Huang, Zhongyu Li, Koushil Sreenath.
  Mid-scale low-cost humanoid platform with narrow sim-to-real gap for learning-based locomotion.
  Links: [Project](https://berkeley-humanoid.com/) · [Paper](https://arxiv.org/abs/2407.21781)

- 📦 🧍 🧱 **[Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking](https://arxiv.org/abs/2412.17730)** `arXiv 2024.12` `UniH1 (sim)` `WBC-Tracking`
  Yun Liu et al..
  First benchmark for retargeting + tracking + imitation across 6 household scene-interaction tasks (11K objects, 23K motions).
  Links: [Project](https://mimicking-bench.github.io/) · [Paper](https://arxiv.org/abs/2412.17730)

- 🌐 🤖 🧍 **[ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196)** `arXiv 2024.12 (RSS 2025 sub.)` `Unitree H1, Unitree G1` `WBC-Tracking`
  Mazeyu Ji, Xuanbin Peng, Fangchen Liu, Jialong Li, Ge Yang, Xuxin Cheng, Xiaolong Wang.
  Generalized whole-body tracker with automatic motion-feasibility curation and decoupled velocity/landmark tracking on H1 and G1.
  Links: [Project](https://exbody2.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2412.13196)

- 🌐 🤖 🧍 **[Learning Humanoid Locomotion over Challenging Terrain](https://arxiv.org/abs/2410.03654)** `arXiv (Berkeley)` `Digit` `Locomotion`
  Ilija Radosavovic, Sarthak Kamat, Trevor Darrell, Jitendra Malik.
  Transformer policy for humanoid locomotion over rough/sloped/stair terrain via large-scale RL.
  Links: [Project](https://humanoid-challenging-terrain.github.io/) · [Paper](https://arxiv.org/abs/2410.03654)

- 🌐 🤖 🧍 **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** `Science Robotics` `Digit (Agility Robotics)` `Locomotion`
  Ilija Radosavovic, Tete Xiao, Bike Zhang, Trevor Darrell, Jitendra Malik, Koushil Sreenath.
  Causal-transformer locomotion policy zero-shot deployed on Digit humanoid for outdoor walking.
  Links: [Project](https://learning-humanoid-locomotion.github.io/) · [Paper](https://arxiv.org/abs/2303.03381)

- 🌐 🤖 **[Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control (Cassie)](https://arxiv.org/abs/2401.16889)** `IJRR 2024` `Cassie` `Locomotion`
  Zhongyu Li, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, Koushil Sreenath.
  Comprehensive RL framework for versatile dynamic bipedal skills (running, jumping, hopping) on Cassie.
  Links: [Project](https://hybrid-robotics.berkeley.edu/biped/) · [Paper](https://arxiv.org/abs/2401.16889)

- 🌐 🧍 🧱 **[H-GAP: Humanoid Control with a Generalist Planner](https://arxiv.org/abs/2312.02682)** `ICLR 2024` `56-DoF dm_control humanoid` `Motion-Imitation`
  Zhengyi Jiang, Yueh-Hua Wu, Yi Wu, Pieter Abbeel.
  Trajectory-level autoencoding planner trained on MoCapAct, used with MPC at test time to solve novel tasks zero-shot.
  Links: [Project](https://ycxia.github.io/H-GAP/) · [Code](https://github.com/facebookresearch/hgap) · [Paper](https://arxiv.org/abs/2312.02682)

- 🌐 🧍 🧱 **[SuperPADL: Scaling Language-Directed Physics-Based Control with Progressive Supervised Distillation](https://arxiv.org/abs/2407.10481)** `SIGGRAPH 2024` `simulated humanoid` `Motion-Imitation`
  Jordan Juravsky, Yunrong Guo, Sanja Fidler, Xue Bin Peng.
  Scales language-directed physics control to 5K+ skills via progressive RL→supervised distillation.
  Links: [Project](https://xbpeng.github.io/projects/SuperPADL/index.html) · [Paper](https://arxiv.org/abs/2407.10481)

- 🌐 **[UH-1 - Learning from Massive Human Videos for Universal Humanoid Pose Control](https://arxiv.org/abs/2412.14172)** `arXiv 2024.12` `WBC-Tracking`
  Universal humanoid pose control trained on massive human videos.
  Links: [Project](https://usc-gvl.github.io/UH-1/) · [Paper](https://arxiv.org/abs/2412.14172)

- ❌ 🤖 🧍 **[VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters](https://la.disneyresearch.com/wp-content/uploads/VMP_paper.pdf)** `SCA 2024 (Computer Graphics Forum)` `simulated character + bipedal robot` `Motion-Imitation`
  Agon Serifi et al. (Disney Research).
  Two-stage VAE+policy framework that produces a versatile motion prior transferable to a real bipedal robot.
  Links: [Project](https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/) · [Paper](https://la.disneyresearch.com/wp-content/uploads/VMP_paper.pdf)

- ❌ **[EMOTION - Expressive Motion Sequence Generation for Humanoid Robots with In-Context Learning](https://arxiv.org/abs/2410.23234)** `arXiv 2024.10` `WBC-Tracking`
  In-context expressive motion generation for humanoids.
  Links: [Paper](https://arxiv.org/abs/2410.23234)

- ❌ **[Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration](https://arxiv.org/abs/2412.15166)** `arXiv 2024.12` `WBC-Tracking`
  Cross-embodiment skill transfer via decomposed adversarial imitation.
  Links: [Paper](https://arxiv.org/abs/2412.15166)

- ⭐ 🤖 **[Extreme Parkour with Legged Robots](https://arxiv.org/abs/2309.14341)** `ICRA 2024` `Unitree A1/Go1` `Locomotion`
  Xuxin Cheng, Kexin Shi, Ananye Agarwal, Deepak Pathak.
  Single-policy parkour from depth image trained in <20h, agile high-jump and gap-leap behaviors.
  Links: [Project](https://extreme-parkour.github.io/) · [Code](https://github.com/chengxuxin/extreme-parkour) · [Paper](https://arxiv.org/abs/2309.14341)

- ⭐ 🧍 🧱 **[CALM: Conditional Adversarial Latent Models for Directable Virtual Characters](https://arxiv.org/abs/2305.02195)** `SIGGRAPH 2023` `simulated humanoid` `Motion-Imitation`
  Chen Tessler, Yoni Kasten, Yunrong Guo, Shie Mannor, Gal Chechik, Xue Bin Peng.
  Learns a conditional latent that lets a user direct character style and motion while preserving diversity.
  Links: [Project](https://research.nvidia.com/labs/par/calm/) · [Code](https://github.com/NVlabs/CALM) · [Paper](https://arxiv.org/abs/2305.02195)

- ⭐ 🧍 🧱 **[NCP / Tencent RoboticsX motion control suite](https://github.com/Tencent-RoboticsX/NCP)** `open-source` `simulated humanoid` `Motion-Imitation`
  Tencent RoboticsX.
  Reference implementation of Neural Categorical Priors for character control.
  Links: [Project](https://tencent-roboticsx.github.io/NCP/) · [Code](https://github.com/Tencent-RoboticsX/NCP) · [Paper](https://github.com/Tencent-RoboticsX/NCP)

- ⭐ 🧍 🧱 **[NCP: Neural Categorical Priors for Physics-Based Character Control](https://arxiv.org/abs/2308.07200)** `SIGGRAPH Asia 2023` `simulated humanoid` `Motion-Imitation`
  Qingxu Zhu, He Zhang, Mengting Lan, Lei Han.
  Compresses motion clips into a discrete VQ codebook with a learned categorical prior for generation and downstream RL.
  Links: [Project](https://tencent-roboticsx.github.io/NCP/) · [Code](https://github.com/Tencent-RoboticsX/NCP) · [Paper](https://arxiv.org/abs/2308.07200)

- ⭐ 🧍 🧱 **[PHC: Perpetual Humanoid Control for Real-time Simulated Avatars](https://arxiv.org/abs/2305.06456)** `ICCV 2023` `SMPL humanoid (Isaac Gym)` `Motion-Imitation`
  Zhengyi Luo, Jinkun Cao, Alexander Winkler, Kris Kitani, Weipeng Xu.
  A single physics-based controller that imitates ~10K AMASS motions and recovers from arbitrary fail states without external forces.
  Links: [Project](https://www.zhengyiluo.com/PHC-Site/) · [Code](https://github.com/ZhengyiLuo/PHC) · [Paper](https://arxiv.org/abs/2305.06456)

- ⭐ 🧍 🧱 **[ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](https://arxiv.org/abs/2205.01906)** `SIGGRAPH 2022 (TOG)` `simulated humanoid` `Motion-Imitation`
  Xue Bin Peng, Yunrong Guo, Lina Halper, Sergey Levine, Sanja Fidler.
  Learns a reusable latent skill embedding from large unstructured mocap that downstream tasks can sample for diverse behaviors.
  Links: [Project](https://research.nvidia.com/labs/toronto-ai/ASE/) · [Code](https://github.com/nv-tlabs/ASE) · [Paper](https://arxiv.org/abs/2205.01906)

- ⭐ 🧍 🧱 **[MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control](https://arxiv.org/abs/2208.07363)** `NeurIPS 2022 (Datasets)` `dm_control humanoid` `Motion-Imitation`
  Nolan Wagener, Andrey Kolobov, Felipe Vieira Frujeri, Ricky Loynd, Ching-An Cheng, Matthew Hausknecht.
  3+ hours of expert tracking rollouts for 2,000+ MoCap clips on the dm_control humanoid.
  Links: [Project](https://microsoft.github.io/MoCapAct/) · [Code](https://github.com/microsoft/MoCapAct) · [Paper](https://arxiv.org/abs/2208.07363)

- ⭐ 🤖 **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** `CoRL 2021` `ANYmal C` `Locomotion`
  Nikita Rudin, David Hoeller, Philipp Reist, Marco Hutter.
  GPU-parallel IsaacGym RL trains ANYmal to walk in minutes; foundational legged_gym codebase.
  Links: [Project](https://leggedrobotics.github.io/legged_gym/) · [Code](https://github.com/leggedrobotics/legged_gym) · [Paper](https://arxiv.org/abs/2109.11978)

- ⭐ 🧍 🧱 **[AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](https://arxiv.org/abs/2104.02180)** `SIGGRAPH 2021 (TOG)` `simulated character` `Motion-Imitation`
  Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa.
  Replaces hand-crafted imitation rewards with an adversarial discriminator that scores motion realism vs. an unstructured mocap dataset.
  Links: [Project](https://xbpeng.github.io/projects/AMP/index.html) · [Code](https://github.com/xbpeng/MimicKit) · [Paper](https://arxiv.org/abs/2104.02180)

- ⭐ 🧍 🧱 **[Universal Humanoid Controller (UHC) — Kinpoly / EmbodiedPose](https://arxiv.org/abs/2106.05969)** `NeurIPS 2021 / NeurIPS 2022` `Mujoco humanoid` `Motion-Imitation`
  Zhengyi Luo, Ryo Hachiuma, Ye Yuan, Kris Kitani.
  Task-agnostic motion imitator that takes only reference frames as input; precursor to PHC.
  Links: [Project](https://zhengyiluo.github.io/projects/kin_poly/) · [Code](https://github.com/ZhengyiLuo/UHC) · [Paper](https://arxiv.org/abs/2106.05969)

- 🌐 🤖 **[Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots (Cassie)](https://arxiv.org/abs/2103.14295)** `ICRA 2021` `Cassie` `Locomotion`
  Zhongyu Li, Xuxin Cheng, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, Koushil Sreenath.
  Domain-randomized RL for parameterized bipedal walking transferred zero-shot to Cassie.
  Links: [Project](https://xbpeng.github.io/projects/Cassie_Walking/index.html) · [Paper](https://arxiv.org/abs/2103.14295)

- ❌ 🤖 🧍 **[Robust Feedback Motion Policy Design Using Reinforcement Learning on a 3D Digit Bipedal Robot](https://arxiv.org/abs/2103.15309)** `IROS 2021` `Digit (Agility Robotics)` `Locomotion`
  Guillermo A. Castillo, Bowen Weng, Wei Zhang, Ayonga Hereid.
  First learning-based locomotion policy zero-shot transferred to Digit hardware.
  Links: [Paper](https://arxiv.org/abs/2103.15309)

- ❌ 🤖 **[Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (Cassie)](https://arxiv.org/abs/2011.01387)** `ICRA 2021` `Cassie` `Locomotion`
  Jonah Siekmann, Yesh Godse, Alan Fern, Jonathan Hurst.
  Periodic reward composition learns walking, running, hopping and skipping gaits transferred to Cassie.
  Links: [Paper](https://arxiv.org/abs/2011.01387)

- 🌐 🤖 **[Learning Quadrupedal Locomotion over Challenging Terrain (ANYmal)](https://arxiv.org/abs/2010.11251)** `Science Robotics` `ANYmal C` `Locomotion`
  Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, Marco Hutter.
  Proprioceptive-only RL controller drives ANYmal across challenging natural terrain.
  Links: [Project](https://leggedrobotics.github.io/rl-blindloco/) · [Paper](https://arxiv.org/abs/2010.11251)

- ⭐ 🧍 🧱 **[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)** `SIGGRAPH 2018 (TOG)` `SMPL/Mujoco humanoid` `Motion-Imitation`
  Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne.
  Foundational RL framework for imitating mocap clips on simulated characters with reference state initialization and early termination.
  Links: [Project](https://xbpeng.github.io/projects/DeepMimic/index.html) · [Code](https://github.com/xbpeng/DeepMimic) · [Paper](https://arxiv.org/abs/1804.02717)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [GMR: General Motion Retargeting (Retargeter for TWIST)](https://github.com/YanjieZe/GMR) | Unitree H1, H1-2, G1, multi-robot | ✅ | ⭐ Code | Real-time CPU motion retargeting library handling SMPL→multi-humanoid mapping wi |
| 2026 | [LIMMT: Less is More for Motion Tracking](https://arxiv.org/abs/2606.06953) | Unitree G1 / humanoid | ✅ | ⭐ Code | Data-centric motion-tracking study showing that carefully filtered high-quality  |
| 2026 | [M3imic: Learning a Versatile Whole-Body Controller for Multi](https://arxiv.org/abs/2606.04829) | humanoid | ✅ | ⭐ Code | Open IsaacLab-based WBC framework unifying joint, root, and end-effector referen |
| 2026 | [MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid ](https://arxiv.org/abs/2602.08594) | humanoid | ✅ | ⭐ Code | Trains a generalist tracker then rapidly adapts to specific teleop interfaces vi |
| 2026 | [Semantic Audio-driven Understanding for Dynamic Humanoid Who](https://arxiv.org/abs/2607.14182) | Unitree G1 | ✅ | ⭐ Code | Routes live music and speech through semantic audio branches that select and sch |
| 2026 | [TEXEDO: Test Time Scaling for Controller-aware Language-cond](https://arxiv.org/abs/2606.22998) | Unitree G1 | ✅ | ⭐ Code | Samples language-conditioned humanoid motions and selects candidates with a cont |
| 2026 | [WholebodyVLA: Towards Unified Latent VLA for Whole-body Loco](https://github.com/OpenDriveLab/WholebodyVLA) | humanoid | ✅ | ⭐ Code | Unified latent VLA architecture for whole-body humanoid loco-manipulation with t |
| 2026 | [ECO - Energy-Constrained Optimization with Reinforcement Lea](https://arxiv.org/abs/2602.06445) | — | — | ⭐ Code | Energy-constrained RL for humanoid walking. |
| 2026 | [FastDSAC: Enhancing Policy Plasticity via Constrained Explor](https://arxiv.org/abs/2606.31691) | MuJoCo Playground / HumanoidBench | — | ⭐ Code | Distributional actor-critic variant constrains exploratory actions to preserve p |
| 2026 | [ADAPT: Analytical Disturbance-Aware Policy Training for Huma](https://arxiv.org/abs/2606.16542) | Unitree G1 | ✅ | 🌐 Project Page | Adds an analytical whole-body disturbance observer to humanoid locomotion polici |
| 2026 | [LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873) | humanoid | ✅ | 🌐 Project Page | Two-stage perceptive policy lets humanoids climb diverse ladders and manipulate  |
| 2026 | [Mind Your Steps: A General Learning Framework for Accurate H](https://arxiv.org/abs/2606.08253) | Booster T1 / humanoid | ✅ | 🌐 Project Page | Learning framework for accurate foothold placement on humanoids, improving safe  |
| 2026 | [Reinforcement Learning-Based Control for an Inline Skating H](https://arxiv.org/abs/2606.31807) | Booster T1 | ✅ | 🌐 Project Page | Trains RL policies that transfer zero-shot to a Booster T1 humanoid wearing pass |
| 2026 | [RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Sho](https://arxiv.org/abs/2606.11092) | Unitree G1 | ✅ | 🌐 Project Page | Three-stage motion-guided curriculum RL for stable, accurate high-impulse humano |
| 2026 | [APEX - Learning Adaptive High-Platform Traversal for Humanoi](https://arxiv.org/abs/2602.11143) | — | — | 🌐 Project Page | Adaptive high-platform traversal for humanoids. |

## Whole-Body Control and Loco-Manipulation

_77 entries._

- ⭐ 🤖 🧍 **[CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.23680)** `arXiv 2026.06` `Unitree G1 + WUJI hand` `Loco-Manipulation`
  Sikai Li et al..
  Coordinates body and dexterous-hand latent priors with residual RL so a G1 can manipulate objects continuously while walking.
  Links: [Project](https://skevinci.github.io/coordex/) · [Code](https://github.com/Skevinci/CoorDex) · [Paper](https://arxiv.org/abs/2606.23680)

- ⭐ 🤖 🧍 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Tianyi Xie et al..
  Fully virtual generation pipeline composing 3D assets, simulator scenes, and video priors into robot-compatible loco-manipulation data.
  Links: [Project](https://research.nvidia.com/labs/dair/grail/) · [Code](https://github.com/NVlabs/GRAIL) · [Paper](https://arxiv.org/abs/2606.05160) · [Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL)

- ⭐ 🤖 🧍 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** `arXiv 2026.06` `Unitree G1` `Loco-Manipulation`
  Lizhi Yang et al..
  Distills complementary teachers into a task-space whole-body command interface for diverse humanoid loco-manipulation skills.
  Links: [Project](https://lzyang2000.github.io/HANDOFF/) · [Code](https://github.com/lzyang2000/HANDOFF) · [Paper](https://arxiv.org/abs/2606.06493)

- ⭐ 🤖 🧍 **[OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.08548)** `arXiv 2026.06` `Unitree G1 / humanoid` `Loco-Manipulation`
  Zehao Yu et al..
  Open simulation-to-real data pipeline for humanoid loco-manipulation with embodiment-aligned demonstrations.
  Links: [Project](https://oasis-humanoid.github.io/) · [Code](https://github.com/TeleHuman/OASIS) · [Paper](https://arxiv.org/abs/2606.08548)

- ⭐ 🧍 🧱 **[Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation](https://arxiv.org/abs/2606.05687)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Junheng Li et al..
  Efficient training-time MPC guidance for humanoid locomotion and manipulation policies.
  Links: [Project](https://github.com/junhengl/mpc-rl) · [Code](https://github.com/junhengl/mpc-rl) · [Paper](https://arxiv.org/abs/2606.05687)

- ⭐ 🧍 🧱 **[SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation](https://arxiv.org/abs/2606.08278)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Songlin Wei et al..
  Full-stack simulation environment and benchmark for policy learning and evaluation in humanoid loco-manipulation.
  Links: [Project](https://github.com/physical-superintelligence-lab/SIMPLE) · [Code](https://github.com/physical-superintelligence-lab/SIMPLE) · [Paper](https://arxiv.org/abs/2606.08278)

- 📦 🤖 🧍 **[OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.22174)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Yingdong Hu et al..
  Empirical recipe for mapping language and pixels directly to the full humanoid action space through whole-body teleop, VLA design, and heterogeneous co-training.
  Links: [Project](https://openhlm-project.github.io/) · [Paper](https://arxiv.org/abs/2606.22174) · [Dataset](https://huggingface.co/datasets/OpenHLM/OpenHLM-data)

- 🌐 🤖 🧍 **[A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots](https://arxiv.org/abs/2606.26425)** `PhD dissertation / arXiv 2026.06` `Atlas, Valkyrie, Nadia, Unitree H1-2, Alex` `Loco-Manipulation`
  Duncan William Calvert.
  Runtime-editable humanoid behavior system combining affordance templates, behavior-tree-inspired logic, perception scenes, and layered whole-body action primitives.
  Links: [Project](https://www.youtube.com/playlist?list=PLJK5CTyotYqsfgfnXb-09YNFeBose6uEY) · [Paper](https://arxiv.org/abs/2606.26425)

- 🌐 🤖 🧍 **[FARO: Feasibility-Aware Robot Motion Optimization](https://arxiv.org/abs/2607.18362)** `arXiv 2026.07` `humanoid` `Loco-Manipulation`
  Michal Ciebielski et al..
  Nested kinodynamic optimizer checks candidate contact sequences, guides LLM-sampled contact plans, and generates humanoid loco-manipulation trajectories trackable by RL controllers.
  Links: [Project](https://github.com/Atarilab/faro.io) · [Paper](https://arxiv.org/abs/2607.18362)

- 🌐 🤖 🧍 **[Handroid: Bridging Dexterous Hand and Humanoid](https://arxiv.org/abs/2607.16187)** `arXiv 2026.07` `Handroid desktop humanoid / dexterous hand` `Loco-Manipulation`
  Ruogu Li et al..
  Reconfigurable 27-DoF desktop robot switches between anthropomorphic hand and humanoid embodiments for manipulation, locomotion, and motion authoring.
  Links: [Project](https://handroid.org/) · [Paper](https://arxiv.org/abs/2607.16187) · [Dataset](CAD/BOM links on project page)

- 🌐 🤖 🧍 **[Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning](https://arxiv.org/abs/2606.28813)** `arXiv 2026.06` `Franka / RBY-1 humanoid mobile robot` `Loco-Manipulation`
  Shuo Cheng et al..
  Learns object-centric interaction priors from human videos and composes them with robot-side feasibility reasoning for Franka and RBY-1 humanoid mobile manipulation.
  Links: [Project](https://human2any.github.io/) · [Paper](https://arxiv.org/abs/2606.28813)

- 🌐 🤖 🧍 **[ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011)** `arXiv 2026.06` `XPENG humanoid / dexterous humanoid` `Loco-Manipulation`
  Wei Xiao et al..
  Uses optimistic value estimation to learn from imperfect human interventions and improve real-world humanoid VLA manipulation rollouts.
  Links: [Project](https://xpeng-robotics.github.io/rove) · [Paper](https://arxiv.org/abs/2606.17011)

- 🌐 🤖 **[SigLoMa — Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision](https://arxiv.org/abs/2605.03846)** `arXiv 2026.05` `quadruped` `Loco-Manipulation`
  Shiyi Chen et al..
  Sigma-Points geometric representation + ego-centric Kalman filter and active-sampling curriculum for open-world pick-and-place from 5Hz detector.
  Links: [Project](https://11chens.github.io/SigLoMa/) · [Paper](https://arxiv.org/abs/2605.03846)

- 🌐 🤖 🧍 **[VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands](https://arxiv.org/abs/2606.09286)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Dongting Li et al..
  Decoupled command framework for vision-guided agile humanoid object interaction under imperfect observability.
  Links: [Project](https://vaic-humanoid.github.io/) · [Paper](https://arxiv.org/abs/2606.09286)

- 🌐 **[EgoHumanoid - Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)** `arXiv 2026.02` `Loco-Manip`
  In-the-wild loco-manipulation from robot-free egocentric demonstrations.
  Links: [Project](https://opendrivelab.com/EgoHumanoid/) · [Paper](https://arxiv.org/abs/2602.10106)

- 🌐 **[HAIC - Humanoid Agile Object Interaction Control via Dynamics-Aware World Model](https://arxiv.org/abs/2602.11758)** `arXiv 2026.02` `Loco-Manip`
  Agile humanoid object interaction with dynamics-aware world model.
  Links: [Project](https://haic-humanoid.github.io/) · [Paper](https://arxiv.org/abs/2602.11758)

- 🌐 **[Humanoid Manipulation Interface - Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](https://arxiv.org/abs/2602.06643)** `arXiv 2026.02` `Loco-Manip`
  Whole-body humanoid manipulation from robot-free demonstrations.
  Links: [Project](https://humanoid-manipulation-interface.github.io) · [Paper](https://arxiv.org/abs/2602.06643)

- 🌐 **[LATENT - Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](https://zzk273.github.io/LATENT/)** `website 2026.03` `Loco-Manip`
  Learns humanoid tennis skills from imperfect human motion captures.
  Links: [Project](https://zzk273.github.io/LATENT/) · [Paper](https://zzk273.github.io/LATENT/)

- 🌐 **[ULTRA - Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)** `arXiv 2026.03` `Loco-Manip`
  Unified multimodal controller for autonomous whole-body loco-manipulation.
  Links: [Project](https://ultra-humanoid.github.io/) · [Paper](https://arxiv.org/abs/2603.03279)

- ⏳ 🤖 🧍 **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645)** `arXiv 2026.06` `Unitree G1` `Loco-Manipulation`
  Yen-Jen Wang et al..
  Generates vision-language-kinematics supervision in reconstructed indoor scenes and trains a G1 policy to predict whole-body trajectories from egocentric observations.
  Links: [Project](https://vision-language-kinematics.github.io/) · [Paper](https://arxiv.org/abs/2606.30645)

- ⏳ 🤖 🧍 **[WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning](https://arxiv.org/abs/2606.13232)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Jaehwi Jang et al..
  Wearable tactile interface and force-conditioned target-pose correction for whole-body manipulation of bulky or shared-load objects.
  Links: [Project](https://wt-umi.github.io/WTUMI/) · [Paper](https://arxiv.org/abs/2606.13232)

- ❌ 🤖 🧍 **[BifrostUMI — Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2605.03452)** `arXiv 2026.05` `humanoid` `Loco-Manipulation`
  Chenhao Yu et al..
  Lightweight VR + wrist-camera demo-collection pipeline that predicts future keypoint trajectories and retargets them to humanoid whole-body control.
  Links: [Paper](https://arxiv.org/abs/2605.03452)

- ❌ 🤖 🧍 **[GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training](https://arxiv.org/abs/2606.12995)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Zhihai Bi et al..
  Zero-shot humanoid-object interaction pipeline that imitates generated task videos and extracts contact events without task-specific training.
  Links: [Paper](https://arxiv.org/abs/2606.12995)

- ❌ 🤖 🧍 **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Ilyass Taouil et al..
  LLM-guided evolutionary search discovers long-horizon contact-rich loco-manipulation motions without teleop or human retargeting.
  Links: [Paper](https://arxiv.org/abs/2606.06139)

- ❌ 🤖 🧍 **[SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation](https://arxiv.org/abs/2606.03297)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Jeonguk Kang et al..
  Factorizes load variation and dynamics mismatch into separate adapters for robust humanoid pickup and placement.
  Links: [Paper](https://arxiv.org/abs/2606.03297)

- ❌ 🤖 🧍 **[TaskNPoint: How to Teach Your Humanoid to Hit a Backhand in Minutes](https://arxiv.org/abs/2606.26215)** `arXiv 2026.06` `Unitree G1` `Loco-Manipulation`
  Blake Werner et al..
  Teaches dynamic humanoid object-interaction skills from a coach-specified interaction window and a small set of demonstrations.
  Links: [Paper](https://arxiv.org/abs/2606.26215)

- ❌ 🧍 🧱 **[Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.11891)** `ICRA 2026 Workshop RL4IL` `Unitree G1` `Loco-Manipulation`
  Mehmet Turan Yardımcı.
  Controlled IsaacLab study showing dual critics outperform unified critics for humanoid reaching and loco-manipulation curricula.
  Links: [Paper](https://arxiv.org/abs/2606.11891)

- ❌ 🧍 🧱 **[Humanoid-DART: Humanoid Loco-Manipulation using Diffusion-guided Augmentation through Relabeling and Tracking](https://arxiv.org/abs/2606.26855)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Pranav Debbad et al..
  Bootstraps humanoid loco-manipulation from sparse demos by expanding goal-conditioned trajectories with diffusion generation and RL tracking.
  Links: [Paper](https://arxiv.org/abs/2606.26855)

- ❌ 🧍 🧱 **[OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.26201)** `arXiv 2026.06` `humanoid` `Loco-Manipulation`
  Runyi Yu et al..
  Represents long-horizon humanoid loco-manipulation with contact-flow trajectories that a low-level tracker and high-level generator can chain.
  Links: [Paper](https://arxiv.org/abs/2606.26201)

- ⭐ 🤖 🧍 **[ALMI — Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305)** `NeurIPS 2025` `Unitree H1-2` `WBC`
  Hong Zhang, et al..
  Adversarial training between upper and lower body policies plus the ALMI-X language-trajectory dataset.
  Links: [Project](https://almi-humanoid.github.io/) · [Code](https://github.com/TeleHuman/ALMI-Open) · [Paper](https://arxiv.org/abs/2504.14305)

- ⭐ 🤖 🧍 **[AMO — Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control](https://arxiv.org/abs/2505.03738)** `RSS 2025` `Unitree H1-2` `WBC`
  Jialong Li, Xuxin Cheng, Tianshu Huang, Shiqi Yang, Ri-Zhao Qiu, Xiaolong Wang.
  Hybrid sim-to-real RL + trajectory optimization for adaptive whole-body humanoid control with extreme reach.
  Links: [Project](https://amo-humanoid.github.io/) · [Code](https://github.com/OpenTeleVision/AMO) · [Paper](https://arxiv.org/abs/2505.03738)

- ⭐ 🤖 🧍 **[GR00T N1 — An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** `arXiv 2025` `Fourier GR1, multiple humanoids` `Loco-Manip`
  NVIDIA GEAR Lab.
  Open VLA foundation model for humanoids trained on egocentric videos + sim/real trajectories + synthetic data.
  Links: [Project](https://research.nvidia.com/labs/gear/gr00t-n1/) · [Code](https://github.com/NVIDIA/Isaac-GR00T) · [Paper](https://arxiv.org/abs/2503.14734)

- ⭐ 🤖 🧍 **[GR00T-WBC — NVIDIA GR00T Whole-Body Control](https://github.com/NVlabs/GR00T-WholeBodyControl)** `NVIDIA technical release` `Multiple humanoids (Unitree, Fourier, etc.)` `WBC`
  NVIDIA Robotics Research.
  Unified open WBC platform combining decoupled controllers used by GR00T N1.5/N1.6 and GEAR-SONIC.
  Links: [Project](https://github.com/NVlabs/GR00T-WholeBodyControl) · [Code](https://github.com/NVlabs/GR00T-WholeBodyControl) · [Paper](https://github.com/NVlabs/GR00T-WholeBodyControl)

- ⭐ 🤖 🧍 **[HOMIE — Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013)** `arXiv 2025` `Unitree H1, G1` `Loco-Manip`
  Qingwei Ben, et al. (InternRobotics / Shanghai AI Lab).
  $500 isomorphic exoskeleton cockpit + RL height-tracking lower-body policy enabling efficient humanoid loco-manipulation.
  Links: [Project](https://homietele.github.io/) · [Code](https://github.com/OpenRobotLab/OpenHomie) · [Paper](https://arxiv.org/abs/2502.13013)

- ⭐ 🤖 🧍 **[HoST — Learning Humanoid Standing-up Control across Diverse Postures](https://arxiv.org/abs/2502.08378)** `RSS 2025 (Best Systems Paper Finalist)` `Unitree G1` `WBC`
  Tao Huang, Junli Ren, Huayi Wang, et al..
  Multi-critic RL with motion regularization that learns posture-adaptive standing-up from arbitrary fallen postures.
  Links: [Project](https://taohuang13.github.io/humanoid-standingup.github.io/) · [Code](https://github.com/InternRobotics/HoST) · [Paper](https://arxiv.org/abs/2502.08378)

- ⭐ 🤖 **[Human2LocoMan — Learning Versatile Quadrupedal Manipulation with Human Pretraining](https://arxiv.org/abs/2506.16475)** `arXiv 2025` `LocoMan (Unitree Go1 + arm)` `Loco-Manip`
  Yaru Niu, et al..
  Cross-embodiment data collection + learning that pretrains on humans before transferring to a quadruped manipulator.
  Links: [Project](https://human2bots.github.io/) · [Code](https://github.com/Hi-DAVID/Human2LocoMan) · [Paper](https://arxiv.org/abs/2506.16475)

- ⭐ 🤖 🧍 **[WholeBodyVLA — Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)** `ICLR 2026` `AgiBot X2` `Loco-Manip`
  OpenDriveLab team.
  Unified latent VLA framework learning loco-manipulation from action-free egocentric videos for large-space mobility.
  Links: [Project](https://opendrivelab.com/WholeBodyVLA/) · [Code](https://github.com/OpenDriveLab/WholebodyVLA) · [Paper](https://arxiv.org/abs/2512.11047)

- ⭐ 🧍 🧱 **[PARC — Physics-based Augmentation with RL for Character Controllers](https://arxiv.org/abs/2505.04002)** `SIGGRAPH 2025` `Simulated character / humanoid` `WBC`
  Michael Xu, Yi Shi, KangKang Yin, Xue Bin Peng.
  Iterative ML+physics augmentation expanding terrain traversal repertoire of physics-based humanoid characters.
  Links: [Project](https://michaelx.io/parc/) · [Code](https://github.com/michaelx-research/parc) · [Paper](https://arxiv.org/abs/2505.04002)

- ⭐ 🧍 🧱 **[SkillBlender — Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending](https://arxiv.org/abs/2506.09366)** `arXiv 2025` `Unitree H1, G1, Fourier GR1` `Loco-Manip`
  Yuxuan Kuang, Haoran Geng, Amine Elhafsi, Tan-Dzung Do, Pieter Abbeel, Jitendra Malik, Marco Pavone, Yue Wang.
  Hierarchical RL pretraining of primitive skills, dynamically blended for diverse loco-manip tasks plus SkillBench benchmark.
  Links: [Project](https://usc-gvl.github.io/SkillBlender/) · [Code](https://github.com/Humanoid-SkillBlender/SkillBlender) · [Paper](https://arxiv.org/abs/2506.09366)

- 🧩 🤖 **[π0.5 — A Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** `arXiv 2025` `Mobile bimanual platforms` `Loco-Manip`
  Physical Intelligence team.
  VLA with broad cross-task co-training enabling 10-15-min mobile manipulation in unseen homes.
  Links: [Project](https://www.pi.website/blog/pi05) · [Code](https://github.com/Physical-Intelligence/openpi) · [Paper](https://arxiv.org/abs/2504.16054)

- 🌐 🤖 🧍 **[BumbleBee (BB) — Expert-Generalist Whole-Body Humanoid Control](https://arxiv.org/abs/2510.25241)** `arXiv 2025` `Humanoid` `WBC`
  BeingBeyond team.
  Motion-cluster experts distilled into a unified generalist whole-body controller with delta-action sim-to-real.
  Links: [Project](https://beingbeyond.github.io/BumbleBee/) · [Code](❌) · [Paper](https://arxiv.org/abs/2510.25241)

- 🌐 🤖 🧍 **[COLA — Learning Human-Humanoid Coordination for Collaborative Object Carrying](https://arxiv.org/abs/2510.14293)** `arXiv 2025` `Unitree H1-2` `Loco-Manip`
  Yanwen Zou, et al..
  Coordination policy for human-humanoid collaborative object carrying along straight/curved trajectories.
  Links: [Project](https://collaborative-cola.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2510.14293)

- 🌐 🤖 🧍 **[HumanoidExo — Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton](https://arxiv.org/abs/2510.03022)** `arXiv 2025` `Humanoid (general)` `WBC`
  Anonymous.
  Wearable exoskeleton enabling scalable humanoid whole-body manipulation data collection.
  Links: [Project](https://humanoidexo.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2510.03022)

- 🌐 🤖 🧍 **[Kinematics-Aware Multi-Policy RL for Force-Capable Humanoid Loco-Manipulation](https://arxiv.org/abs/2511.21169)** `arXiv 2025` `Unitree G1` `Loco-Manip`
  Anonymous.
  Three-stage decoupled training (upper / lower / delta-command) enabling 4 kg carry and 112.8 kg cart-push on G1.
  Links: [Project](https://hugging-physics.github.io/KAMP/) · [Code](❌) · [Paper](https://arxiv.org/abs/2511.21169)

- 🌐 🤖 🧍 **[Learning Getting-Up Policies for Real-World Humanoid Robots](https://arxiv.org/abs/2502.12152)** `RSS 2025` `Unitree G1` `WBC`
  Xialin He, Runpei Dong, Zixuan Chen, Saurabh Gupta.
  Two-stage curriculum + posture-conditioned RL learning robust real-world humanoid getting-up.
  Links: [Project](https://humanoid-getup.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2502.12152)

- 🌐 🤖 🧍 **[StageACT — Stage-Conditioned Imitation for Robust Humanoid Door Opening](https://arxiv.org/abs/2509.13200)** `arXiv 2025` `Humanoid (office)` `Loco-Manip`
  Anonymous.
  Stage-conditioned imitation learning that more than doubles door-opening success on unseen doors (55%).
  Links: [Project](https://stageact.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2509.13200)

- 🌐 🤖 🧍 **[VIRAL — Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](https://arxiv.org/abs/2511.15200)** `arXiv 2025` `Unitree G1` `Loco-Manip`
  Anonymous (NVIDIA / collaborators).
  Teacher-student delta-action framework that distills RGB visuomotor policies from massive simulation tiles.
  Links: [Project](https://viral-humanoid.github.io/) · [Code](⏳) · [Paper](https://arxiv.org/abs/2511.15200)

- 🌐 **[BEHAVIOR Robot Suite - Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities](https://arxiv.org/abs/2503.05652)** `arXiv 2025.03` `Loco-Manip`
  Real-world whole-body manipulation suite for household activities.
  Links: [Project](https://behavior-robot-suite.github.io/) · [Paper](https://arxiv.org/abs/2503.05652)

- 🌐 **[Ego-Vision World Model for Humanoid Contact Planning](https://arxiv.org/abs/2510.11682)** `arXiv 2025.10` `Loco-Manip`
  Egocentric vision world model for humanoid contact planning.
  Links: [Project](https://ego-vcp.github.io/) · [Paper](https://arxiv.org/abs/2510.11682)

- 🌐 **[HITTER - A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning](https://arxiv.org/abs/2508.21043)** `arXiv 2025.08` `Loco-Manip`
  Humanoid table tennis with hierarchical planning and learning.
  Links: [Project](https://humanoid-table-tennis.github.io/) · [Paper](https://arxiv.org/abs/2508.21043)

- 🌐 **[TrajBooster - Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning](https://arxiv.org/abs/2509.11839)** `arXiv 2025.09` `Loco-Manip`
  Trajectory-centric learning to boost whole-body humanoid manipulation.
  Links: [Project](https://jiachengliu3.github.io/TrajBooster/) · [Paper](https://arxiv.org/abs/2509.11839)

- ❌ 🤖 🧍 **[Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation](https://arxiv.org/abs/2506.22827)** `arXiv 2025` `Humanoid` `Loco-Manip`
  Anonymous.
  Hierarchical VLM planner that orchestrates multi-step humanoid manipulation primitives.
  Links: [Project](❌) · [Code](❌) · [Paper](https://arxiv.org/abs/2506.22827)

- ❌ 🤖 🧍 **[Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer](https://arxiv.org/abs/2512.01061)** `arXiv 2025` `Humanoid (RGB)` `Loco-Manip`
  Anonymous.
  Teacher-student-bootstrap + GRPO yielding RGB-only zero-shot diverse door-opening, beating teleop by 31.7%.
  Links: [Project](❌) · [Code](❌) · [Paper](https://arxiv.org/abs/2512.01061)

- ❌ **[DemoHLM - From One Demonstration to Generalizable Humanoid Loco-Manipulation](https://arxiv.org/abs/2510.11258)** `arXiv 2025.10` `Loco-Manip`
  Single-demo generalizable humanoid loco-manipulation policy.
  Links: [Paper](https://arxiv.org/abs/2510.11258)

- ❌ 🧍 **[Humanoid Locomotion and Manipulation: Current Progress and Challenges](https://arxiv.org/abs/2501.02116)** `arXiv 2025 (Survey)` `WBC`
  Zhaoyuan Gu, Junheng Li, Wenlan Shen, et al..
  Comprehensive 2025 survey of humanoid locomotion and manipulation control, planning, and learning.
  Links: [Project](❌) · [Code](❌) · [Paper](https://arxiv.org/abs/2501.02116)

- ❌ **[Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models](https://arxiv.org/abs/2504.16843v1)** `arXiv 2025.04` `Loco-Manip`
  Latent diffusion for physically consistent loco-manipulation.
  Links: [Paper](https://arxiv.org/abs/2504.16843v1)

- ⭐ 🤖 🧍 **[ACE — A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation](https://arxiv.org/abs/2408.11805)** `CoRL 2024` `H1 + Inspire, Xarm + Ability, GR-1, Franka, B1+Z1` `WBC`
  Shiqi Yang, Minghuan Liu, Yuzhe Qin, Runyu Ding, Jialong Li, Xuxin Cheng, Ruihan Yang, Sha Yi, Xiaolong Wang.
  Cross-platform visual-exoskeleton teleop generalizing to humanoid hands, arms, grippers, and quadruped-grippers.
  Links: [Project](https://ace-teleop.github.io/) · [Code](https://github.com/ACETeleop/ACETeleop) · [Paper](https://arxiv.org/abs/2408.11805)

- ⭐ 🤖 **[Catch It! — Learning to Catch in Flight with Mobile Dexterous Hands](https://arxiv.org/abs/2409.10319)** `ICRA 2025` `Mobile base + arm + 12-DoF hand` `Loco-Manip`
  Yuanhang Zhang, Tianhai Liang, Zhenyang Chen, Yanjie Ze, Huazhe Xu.
  Two-stage RL whole-body-control catching policy that achieves ~80% sim catch success on diverse trajectories.
  Links: [Project](https://mobile-dex-catch.github.io/) · [Code](https://github.com/hang0610/Catch_It) · [Paper](https://arxiv.org/abs/2409.10319)

- ⭐ 🤖 🧍 **[Generalizable Humanoid Manipulation with 3D Diffusion Policies (iDP3)](https://arxiv.org/abs/2410.10803)** `IROS 2025` `Fourier GR1` `Loco-Manip`
  Yanjie Ze, Zixuan Chen, Wenhao Yu, Tony Z. Zhao, Jiajun Wu, C. Karen Liu, Jia Deng, Jiajun Wu.
  Improved 3D Diffusion Policy enabling generalizable humanoid manipulation from a small set of demonstrations.
  Links: [Project](https://humanoid-manipulation.github.io/) · [Code](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) · [Paper](https://arxiv.org/abs/2410.10803)

- ⭐ 🤖 🧍 **[Humanoid Parkour Learning](https://arxiv.org/abs/2406.10759)** `CoRL 2024` `Unitree H1` `WBC`
  Ziwen Zhuang, Shenzhe Yao, Hang Zhao.
  End-to-end vision-based whole-body parkour policy: jumping platforms, hurdles, 0.8m gaps, 1.8 m/s running.
  Links: [Project](https://humanoid4parkour.github.io/) · [Code](https://github.com/ZiwenZhuang/parkour) · [Paper](https://arxiv.org/abs/2406.10759)

- ⭐ 🤖 🧍 **[Learning Humanoid Locomotion with Perceptive Internal Model](https://arxiv.org/abs/2411.14386)** `ICRA 2025` `Unitree H1, G1` `WBC`
  Junfeng Long, Junli Ren, Moji Shi, Zirui Wang, Tao Huang, Ping Luo, Jiangmiao Pang.
  Perceptive Internal Model on elevation maps generalizes single-stage perceptive locomotion across humanoid platforms.
  Links: [Project](https://junfeng-long.github.io/PIM/) · [Code](https://github.com/OpenRobotLab/HIMLoco) · [Paper](https://arxiv.org/abs/2411.14386)

- ⭐ 🤖 **[LocoMan — Advancing Versatile Quadrupedal Dexterity with Lightweight Loco-Manipulators](https://arxiv.org/abs/2403.18197)** `IROS 2024` `Unitree Go1 + light arms` `Loco-Manip`
  Changyi Lin, et al..
  Open quadruped + lightweight arms platform with multi-mode loco-manipulation skills.
  Links: [Project](https://linchangyi1.github.io/LocoMan/) · [Code](https://github.com/linchangyi1/LocoMan) · [Paper](https://arxiv.org/abs/2403.18197)

- ⭐ 🤖 **[Mobile ALOHA — Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)** `CoRL 2024` `Custom mobile ALOHA` `Loco-Manip`
  Zipeng Fu, Tony Z. Zhao, Chelsea Finn.
  $32k whole-body teleop platform enabling bimanual mobile manipulation with co-trained imitation policies.
  Links: [Project](https://mobile-aloha.github.io/) · [Code](https://github.com/MarkFzp/mobile-aloha) · [Paper](https://arxiv.org/abs/2401.02117) · [Dataset](https://github.com/MarkFzp/mobile-aloha)

- ⭐ 🤖 **[MoMa-LLM — Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](https://arxiv.org/abs/2403.08605)** `RA-L 2024` `Mobile manipulator (sim/real)` `Loco-Manip`
  Daniel Honerkamp, Martin Büchner, Fabien Despinoy, Tim Welschehold, Abhinav Valada.
  LLM-grounded dynamic scene graphs for open-vocabulary interactive object search with mobile manipulation.
  Links: [Project](https://moma-llm.cs.uni-freiburg.de/) · [Code](https://github.com/robot-learning-freiburg/MoMa-LLM) · [Paper](https://arxiv.org/abs/2403.08605)

- ⭐ 🤖 🧍 **[Open-TeleVision — Teleoperation with Immersive Active Visual Feedback](https://arxiv.org/abs/2407.01512)** `CoRL 2024` `Unitree H1, Fourier GR1` `WBC`
  Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang.
  VR-based stereoscopic teleop with active head tracking, validated on H1 + GR1 with imitation learning.
  Links: [Project](https://robot-tv.github.io/) · [Code](https://github.com/OpenTeleVision/TeleVision) · [Paper](https://arxiv.org/abs/2407.01512)

- ⭐ 🤖 **[Pi0 — A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** `arXiv 2024` `7 platforms / 68 tasks` `Loco-Manip`
  Kevin Black, Noah Brown, Danny Driess, et al. (Physical Intelligence).
  VLA flow-matching policy delivering generalist dexterous robot control across 7 robots / 68 tasks.
  Links: [Project](https://www.pi.website/blog/pi0) · [Code](https://github.com/Physical-Intelligence/openpi) · [Paper](https://arxiv.org/abs/2410.24164)

- ⭐ 🤖 **[UMI on Legs — Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers](https://arxiv.org/abs/2407.10353)** `CoRL 2024` `Unitree B1 + arm` `Loco-Manip`
  Huy Ha, Yihuai Gao, Zipeng Fu, Jie Tan, Shuran Song.
  Plug fixed-base UMI manipulation policies onto a quadruped via a manipulation-centric whole-body controller.
  Links: [Project](https://umi-on-legs.github.io/) · [Code](https://github.com/real-stanford/umi-on-legs) · [Paper](https://arxiv.org/abs/2407.10353)

- ⭐ 🤖 **[Visual Whole-Body Control for Legged Loco-Manipulation](https://arxiv.org/abs/2403.16967)** `CoRL 2024` `Unitree B1 + Z1` `Loco-Manip`
  Minghuan Liu, Zixuan Chen, Xuxin Cheng, Yandong Ji, Ri-Zhao Qiu, Ruihan Yang, Xiaolong Wang.
  Hierarchical vision-driven whole-body control achieving >70% success on prehensile and dynamic loco-manipulation.
  Links: [Project](https://wholebody-b1.github.io/) · [Code](https://github.com/Ericonaldo/visual_wholebody) · [Paper](https://arxiv.org/abs/2403.16967)

- ⭐ 🧍 🧱 **[BiGym — A Demo-Driven Mobile Bi-Manual Manipulation Benchmark](https://arxiv.org/abs/2407.07788)** `CoRL 2024` `Unitree H1 (sim)` `Loco-Manip`
  Nikita Chernyadev, Nicholas Backshall, Xiao Ma, Yunfan Lu, Younggyo Seo, Stephen James.
  40-task humanoid bimanual mobile manipulation benchmark with sparse rewards + 50 VR-collected demos per task.
  Links: [Project](https://chernyadev.github.io/bigym/) · [Code](https://github.com/chernyadev/bigym) · [Paper](https://arxiv.org/abs/2407.07788)

- ⭐ 🧍 🧱 **[HumanoidBench — Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](https://arxiv.org/abs/2403.10506)** `RSS 2024` `Unitree H1, Digit (sim)` `WBC`
  Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, Pieter Abbeel.
  First simulated humanoid benchmark with 27 whole-body tasks (15 manipulation + 12 locomotion) and tactile sensing.
  Links: [Project](https://humanoid-bench.github.io/) · [Code](https://github.com/carlosferrazza/humanoid-bench) · [Paper](https://arxiv.org/abs/2403.10506)

- 🌐 🤖 **[ALOHA Unleashed — A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126)** `CoRL 2024` `ALOHA 2` `Loco-Manip`
  Tony Z. Zhao, Jonathan Tompson, Danny Driess, et al..
  26k+ demos + diffusion policies enable challenging bimanual deformable-object and contact-rich manipulation.
  Links: [Project](https://aloha-unleashed.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2410.13126)

- 🌐 🤖 **[Helpful DoggyBot — Open-World Object Fetching using Legged Robots and Vision-Language Models](https://arxiv.org/abs/2410.00231)** `CoRL 2024` `Unitree Go2 + 1-DoF gripper` `Loco-Manip`
  Qi Wu, Zipeng Fu, Xuxin Cheng, Xiaolong Wang, Chelsea Finn.
  1-DoF "biting" gripper + RL whole-body controller + VLM planner for zero-shot open-world fetching.
  Links: [Project](https://helpful-doggybot.github.io/) · [Code](❌) · [Paper](https://arxiv.org/abs/2410.00231)

- 🌐 🤖 🧍 **[OKAMI — Teaching Humanoid Robots Manipulation Skills through Single Video Imitation](https://arxiv.org/abs/2410.11792)** `CoRL 2024` `Fourier GR1` `WBC`
  Jinhan Li, Yifeng Zhu, Yuqi Xie, Zhenyu Jiang, Mingyo Seo, Georgios Pavlakos, Yuke Zhu.
  Two-stage single-video imitation: open-world plan + object-aware retargeting + closed-loop visuomotor policy (~79%).
  Links: [Project](https://ut-austin-rpl.github.io/OKAMI/) · [Code](❌) · [Paper](https://arxiv.org/abs/2410.11792)

- 🌐 🤖 **[Pedipulate — Enabling Manipulation Skills using a Quadruped Robot's Leg](https://arxiv.org/abs/2402.10837)** `ICRA 2024` `ANYmal D` `Loco-Manip`
  Philip Arm, Mayank Mittal, Hendrik Kolvenbach, Marco Hutter.
  One-foot RL position-tracking policy enabling whole-body pedipulation (doors, sample collection, pushing) on ANYmal.
  Links: [Project](https://sites.google.com/leggedrobotics.com/pedipulate) · [Code](❌) · [Paper](https://arxiv.org/abs/2402.10837)

- 🌐 🤖 **[Whole-Body Dynamic Throwing with Legged Manipulators](https://arxiv.org/abs/2410.05681)** `arXiv 2024` `ANYmal + arm` `Loco-Manip`
  Humphrey Munn, et al..
  Unified RL controller for base+arm leveraging curriculum to fuse locomotion and manipulation advantages for throwing.
  Links: [Project](https://www.humphreymunn.com/whole-body-dynamic-throwing) · [Code](❌) · [Paper](https://arxiv.org/abs/2410.05681)

- 🌐 🤖 🧍 **[WoCoCo — Learning Whole-Body Humanoid Control with Sequential Contacts](https://arxiv.org/abs/2406.06005)** `CoRL 2024` `Unitree H1` `Loco-Manip`
  Chong Zhang, Wenli Xiao, Tairan He, Guanya Shi.
  Decomposes contact-rich tasks into sequential contact stages, unlocking jumping, box loco-manip, dancing, climbing.
  Links: [Project](https://lecar-lab.github.io/wococo/) · [Code](❌) · [Paper](https://arxiv.org/abs/2406.06005)

- ❌ 🤖 🧍 **[ARMOR — Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning](https://arxiv.org/abs/2412.00396)** `arXiv 2024` `Humanoid` `WBC`
  Daehwa Kim, et al..
  Distributed wearable depth sensors + transformer policy for humanoid collision-aware whole-body motion.
  Links: [Project](https://arxiv.org/abs/2412.00396) · [Code](❌) · [Paper](https://arxiv.org/abs/2412.00396)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [CoorDex: Coordinating Body and Hand Priors for Continuous De](https://arxiv.org/abs/2606.23680) | Unitree G1 + WUJI hand | ✅ | ⭐ Code | Coordinates body and dexterous-hand latent priors with residual RL so a G1 can m |
| 2026 | [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets ](https://arxiv.org/abs/2606.05160) | humanoid | ✅ | ⭐ Code | Fully virtual generation pipeline composing 3D assets, simulator scenes, and vid |
| 2026 | [HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via ](https://arxiv.org/abs/2606.06493) | Unitree G1 | ✅ | ⭐ Code | Distills complementary teachers into a task-space whole-body command interface f |
| 2026 | [OASIS: From Simulation Data Collection to Real-World Humanoi](https://arxiv.org/abs/2606.08548) | Unitree G1 / humanoid | ✅ | ⭐ Code | Open simulation-to-real data pipeline for humanoid loco-manipulation with embodi |
| 2026 | [Accelerating and Scaling MPC-Guided Reinforcement Learning f](https://arxiv.org/abs/2606.05687) | humanoid | — | ⭐ Code | Efficient training-time MPC guidance for humanoid locomotion and manipulation po |
| 2026 | [SIMPLE: Simulation-Based Policy Learning and Evaluation for ](https://arxiv.org/abs/2606.08278) | humanoid | — | ⭐ Code | Full-stack simulation environment and benchmark for policy learning and evaluati |
| 2026 | [OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Ma](https://arxiv.org/abs/2606.22174) | humanoid | ✅ | 📦 Dataset | Empirical recipe for mapping language and pixels directly to the full humanoid a |
| 2026 | [A System for Fast, Resilient, and Adaptable Loco-Manipulatio](https://arxiv.org/abs/2606.26425) | Atlas, Valkyrie, Nadia, Unitree H1-2, Alex | ✅ | 🌐 Project Page | Runtime-editable humanoid behavior system combining affordance templates, behavi |
| 2026 | [FARO: Feasibility-Aware Robot Motion Optimization](https://arxiv.org/abs/2607.18362) | humanoid | ✅ | 🌐 Project Page | Nested kinodynamic optimizer checks candidate contact sequences, guides LLM-samp |
| 2026 | [Handroid: Bridging Dexterous Hand and Humanoid](https://arxiv.org/abs/2607.16187) | Handroid desktop humanoid / dexterous hand | ✅ | 🌐 Project Page | Reconfigurable 27-DoF desktop robot switches between anthropomorphic hand and hu |
| 2026 | [Human2Any: Human-to-Robot Transfer via Constraint-Aware Comp](https://arxiv.org/abs/2606.28813) | Franka / RBY-1 humanoid mobile robot | ✅ | 🌐 Project Page | Learns object-centric interaction priors from human videos and composes them wit |
| 2026 | [ROVE: Unlocking Human Interventions for Humanoid Manipulatio](https://arxiv.org/abs/2606.17011) | XPENG humanoid / dexterous humanoid | ✅ | 🌐 Project Page | Uses optimistic value estimation to learn from imperfect human interventions and |
| 2026 | [SigLoMa — Learning Open-World Quadrupedal Loco-Manipulation ](https://arxiv.org/abs/2605.03846) | quadruped | ✅ | 🌐 Project Page | Sigma-Points geometric representation + ego-centric Kalman filter and active-sam |
| 2026 | [VAIC: Vision-Guided Humanoid Agile Object Interaction Contro](https://arxiv.org/abs/2606.09286) | humanoid | ✅ | 🌐 Project Page | Decoupled command framework for vision-guided agile humanoid object interaction  |
| 2026 | [EgoHumanoid - Unlocking In-the-Wild Loco-Manipulation with R](https://arxiv.org/abs/2602.10106) | — | — | 🌐 Project Page | In-the-wild loco-manipulation from robot-free egocentric demonstrations. |

## Humanoid Foundation Models and Generalist Policies

_75 entries._

- ⭐ 🤖 🧍 **[Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985)** `CVPR 2026` `Unitree G1 / humanoid` `Foundation`
  Zekun Qi et al..
  GPT-style causal Transformer trained on a two-billion-frame retargeted motion corpus for zero-shot whole-body tracking.
  Links: [Project](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [Code](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [Paper](https://arxiv.org/abs/2606.03985)

- ⭐ 🤖 🧍 **[OMG: Omni-Modal Motion Generation for Generalist Humanoid Control](https://arxiv.org/abs/2606.10340)** `arXiv 2026.06` `Unitree G1` `Foundation`
  Siqiao Huang et al..
  Generalist humanoid control stack that places an omni-modal motion-generation brain above a reactive tracking controller.
  Links: [Project](https://tsinghua-mars-lab.github.io/OMG/) · [Code](https://github.com/Tsinghua-MARS-Lab/OMG) · [Paper](https://arxiv.org/abs/2606.10340)

- ⭐ 🧱 **[Cosmos Policy — Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163)** `arXiv (Jan 2026)` `LIBERO, RoboCasa simulators` `Generalist-Policy`
  NVIDIA Research.
  Links: [Code](https://github.com/nv-tlabs/cosmos-policy) · [Paper](https://arxiv.org/abs/2601.16163)

- ⭐ **[LIFT - Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control](https://arxiv.org/abs/2601.21363)** `arXiv 2026.01` `Foundation`
  Pretraining-then-finetuning for humanoid control.
  Links: [Project](https://lift-humanoid.github.io/) · [Code](https://github.com/bigai-ai/LIFT-humanoid) · [Paper](https://arxiv.org/abs/2601.21363)

- ⭐ 🧍 🧱 **[MotionVLA: Vision-Language-Action Model for Humanoid Motion](https://arxiv.org/abs/2606.15142)** `arXiv 2026.06` `humanoid motion / HumanML3D / MBench` `Foundation`
  Nonghai Zhang et al..
  Adapts VLA-style autoregressive modeling to humanoid motion with separate low-frequency pose and high-frequency velocity streams.
  Links: [Project](https://aigeeksgroup.github.io/MotionVLA) · [Code](https://github.com/AIGeeksGroup/MotionVLA) · [Paper](https://arxiv.org/abs/2606.15142)

- 🧩 🤖 **[MolmoAct 2 — Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881)** `arXiv 2026.05` `Franka, SO100/SO101, bimanual YAM` `Foundation`
  Haoquan Fang et al..
  Open VLA stack with MolmoER backbone, OpenFAST action tokenizer, MolmoThink adaptive-reasoning variant, and 720h bimanual dataset.
  Links: [Project](https://allenai.org/blog/molmoact2) · [Code](https://github.com/allenai/molmoact2) · [Paper](https://arxiv.org/abs/2605.02881)

- 🌐 🤖 🧍 **[Ego-Pi: VLA Fine-Tuning for Ego-Centric Human and Robot Data](https://arxiv.org/abs/2606.08107)** `arXiv 2026.06` `humanoid hands / dexterous embodiments` `Foundation`
  Ji Woong Kim et al..
  Studies pi0.5 fine-tuning across egocentric human data and humanoid embodiments with dexterous five-finger hands.
  Links: [Project](https://egopipaper.github.io/) · [Paper](https://arxiv.org/abs/2606.08107)

- 🌐 🤖 🧍 **[Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments](https://arxiv.org/abs/2606.32009)** `arXiv 2026.06` `PrimeU 60-DoF upper-body humanoid` `Foundation`
  Xiaopeng Lin et al..
  Converts synchronized ego-exo human videos into controller-aligned humanoid action chunks for VLA post-training on a human-aligned 60-DoF upper-body robot.
  Links: [Project](https://zgc-embodyai.github.io/Human-as-Humanoid) · [Paper](https://arxiv.org/abs/2606.32009)

- ❌ 🤖 🧍 **[Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](https://arxiv.org/abs/2607.18016)** `arXiv 2026.07` `Unitree G1 / Being-0-aligned humanoid` `Foundation`
  Peng Ren et al..
  POT-VLA maintains role-indexed 3D object records that both condition whole-body action generation and verify geometric task predicates during execution.
  Links: [Paper](https://arxiv.org/abs/2607.18016)

- ❌ 🤖 🧍 **[MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215)** `arXiv 2026.06` `Unitree G1` `Foundation`
  Jia Zheng et al..
  Real-time world-action model for humanoid loco-manipulation that avoids slow video-action denoising loops.
  Links: [Paper](https://arxiv.org/abs/2606.09215)

- ❌ 🤖 🧍 **[Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain](https://arxiv.org/abs/2606.08059)** `arXiv 2026.06` `humanoid` `Foundation`
  Zifan Wang et al..
  Adapts broad human motion priors to robot-centric terrain constraints for reusable perceptive whole-body behavior.
  Links: [Paper](https://arxiv.org/abs/2606.08059)

- ❌ 🤖 🧍 **[Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163)** `arXiv 2026.07` `humanoid` `Foundation`
  Weishuai Zeng et al..
  Studies the scaling recipe for humanoid BFMs by coordinating global-frame motion tracking, reference diversity, rollout volume, and a Humanoid Transformer architecture.
  Links: [Paper](https://arxiv.org/abs/2607.15163)

- ❌ **[Psi0 - An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)** `arXiv 2026.03` `Foundation`
  Open foundation model targeting universal humanoid loco-manipulation.
  Links: [Paper](https://arxiv.org/abs/2603.12263)

- ❌ 🧍 🧱 **[WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning](https://arxiv.org/abs/2606.25591)** `arXiv 2026.06` `humanoid` `Foundation`
  Melya Boukheddimi et al..
  Builds a VLA training framework from whole-body optimal-control trajectories, egocentric observations, and language instructions for humanoid locomotion tasks.
  Links: [Paper](https://arxiv.org/abs/2606.25591)

- ⭐ 🤖 🧍 **[AgiBot World Colosseo + GO-1 — Large-scale Manipulation Platform](https://arxiv.org/abs/2503.06669)** `IROS 2025 / IEEE T-RO 2026` `AgiBot mobile humanoid (whole-body, dexterous hands, tactile)` `Foundation / Dataset`
  AgiBot Team / OpenDriveLab.
  1M+ trajectories across 217 tasks in 5 deployment scenarios from 100 real robots.
  Links: [Project](https://agibot-world.com/) · [Code](https://github.com/OpenDriveLab/AgiBot-World) · [Paper](https://arxiv.org/abs/2503.06669) · [Dataset](https://github.com/OpenDriveLab/AgiBot-World)

- ⭐ 🤖 **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** `arXiv (Jan 2025)` `Multi-domain physical AI (robots, AVs)` `Foundation (World Model)`
  NVIDIA Cosmos Team.
  Links: [Project](https://www.nvidia.com/en-us/ai/cosmos/) · [Code](https://github.com/nvidia-cosmos/cosmos-predict2.5) · [Paper](https://arxiv.org/abs/2501.03575)

- ⭐ 🤖 **[DexGraspVLA — A VLA Framework Towards General Dexterous Grasping](https://arxiv.org/abs/2502.20900)** `AAAI 2026 Oral` `Dexterous hands (relevant to humanoid)` `VLA`
  Yifan Zhong, Xuchuan Huang, Ruochong Li, ... (Psi-Robot).
  Links: [Project](https://dexgraspvla.github.io/) · [Code](https://github.com/Psi-Robot/DexGraspVLA) · [Paper](https://arxiv.org/abs/2502.20900)

- ⭐ 🤖 **[DexVLA — Vision-Language Model with Plug-In Diffusion Expert](https://arxiv.org/abs/2502.05855)** `arXiv (Feb 2025)` `Multiple bimanual / dexterous platforms` `VLA`
  Junjie Wen, Yichen Zhu, ... (Midea Group).
  Links: [Project](https://dex-vla.github.io/) · [Code](https://github.com/juruobenruo/DexVLA) · [Paper](https://arxiv.org/abs/2502.05855)

- ⭐ 🤖 **[Dita — Scaling Diffusion Transformer for Generalist VLA Policy](https://arxiv.org/abs/2503.19757)** `ICCV 2025` `Multiple OXE platforms` `Generalist-Policy`
  Zhi Hou, Tianyi Zhang, ... (Shanghai AI Lab).
  Links: [Project](https://robodita.github.io/) · [Code](https://github.com/RoboDita/Dita) · [Paper](https://arxiv.org/abs/2503.19757)

- ⭐ 🤖 **[EgoZero — Robot Learning from Smart Glasses](https://arxiv.org/abs/2505.20290)** `arXiv (May 2025)` `Franka Panda gripper` `Generalist-Policy`
  Vincent Liu, Ademi Adeniji, Haotian Fu, Lerrel Pinto.
  Train manipulation policies from Aria glasses alone with zero robot data; 70% zero-shot success on 7 tasks.
  Links: [Project](https://egozero-robot.github.io/) · [Code](https://github.com/vliu15/egozero) · [Paper](https://arxiv.org/abs/2505.20290)

- ⭐ 🤖 **[FAST — Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)** `arXiv (Jan 2025)` `Multi-platform (used as universal tokenizer)` `VLA (component)`
  Karl Pertsch, Kyle Stachowicz, Brian Ichter, ... Sergey Levine (Physical Intelligence).
  Links: [Project](https://www.pi.website/research/fast) · [Code](https://github.com/Physical-Intelligence/openpi) · [Paper](https://arxiv.org/abs/2501.09747)

- ⭐ 🤖 **[GraspVLA — A Grasping Foundation Model Pre-trained on Billion-Scale Synthetic Action Data](https://arxiv.org/abs/2505.03233)** `arXiv (May 2025)` `Multi-arm, multi-gripper` `Foundation`
  GalaxeaAI.
  Links: [Project](https://pku-epic.github.io/GraspVLA-web/) · [Code](https://github.com/PKU-EPIC/GraspVLA) · [Paper](https://arxiv.org/abs/2505.03233)

- ⭐ 🤖 🧍 **[Humanoid Policy ~ Human Policy (HAT / PH2D)](https://arxiv.org/abs/2503.13441)** `arXiv (Mar 2025)` `Unitree H1 humanoid + dexterous hands; human VR data` `Generalist-Policy`
  Ri-Zhao Qiu, Shiqi Yang, Xuxin Cheng, ... Xiaolong Wang.
  Treats humanoid policy and human policy unified for cross-embodiment.
  Links: [Project](https://human-as-robot.github.io/) · [Code](https://github.com/RogerQi/human-policy) · [Paper](https://arxiv.org/abs/2503.13441)

- ⭐ 🤖 **[InternVLA-M1 — A Spatially Guided VLA Framework for Generalist Robot Policy](https://arxiv.org/abs/2510.13778)** `arXiv (Oct 2025)` `SimplerEnv, WidowX, LIBERO Franka, real` `VLA`
  InternRobotics Team (Shanghai AI Lab).
  Links: [Project](https://internrobotics.github.io/internvla-m1.github.io/) · [Code](https://github.com/InternRobotics/InternVLA-M1) · [Paper](https://arxiv.org/abs/2510.13778)

- ⭐ 🤖 **[NORA — A Small Open-Sourced Generalist Vision Language Action Model](https://arxiv.org/abs/2504.19854)** `arXiv (Apr 2025)` `WidowX, real-world tasks` `VLA`
  Chia-Yu Hung, Qi Sun, Pengfei Hong, ... Soujanya Poria (DeCLaRe Lab).
  Links: [Project](https://declare-lab.github.io/nora) · [Code](https://github.com/declare-lab/nora) · [Paper](https://arxiv.org/abs/2504.19854)

- ⭐ 🤖 **[OpenVLA-OFT / OFT+ — Fine-Tuning VLAs: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645)** `arXiv (Feb 2025)` `ALOHA bimanual, LIBERO sim` `VLA`
  Moo Jin Kim, Chelsea Finn, Percy Liang.
  Links: [Project](https://openvla-oft.github.io/) · [Code](https://github.com/moojink/openvla-oft) · [Paper](https://arxiv.org/abs/2502.19645)

- ⭐ 🤖 **[RoboBrain — A Unified Brain Model for Robotic Manipulation](https://arxiv.org/abs/2502.21257)** `CVPR 2025` `Multi-platform manipulation` `Foundation`
  Yuheng Ji, Huajie Tan, ... (BAAI / FlagOpen).
  Links: [Project](https://superrobobrain.github.io/) · [Code](https://github.com/FlagOpen/RoboBrain) · [Paper](https://arxiv.org/abs/2502.21257)

- ⭐ 🤖 **[SpatialVLA — Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830)** `RSS 2025` `WidowX, Franka, multi-platform` `VLA`
  Delin Qu, Haoming Song, Qizhi Chen, ... (Shanghai AI Lab).
  Links: [Project](https://spatialvla.github.io/) · [Code](https://github.com/SpatialVLA/SpatialVLA) · [Paper](https://arxiv.org/abs/2501.15830)

- ⭐ 🤖 **[WorldVLA — Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539)** `arXiv (Jun 2025)` `LIBERO + real` `Foundation`
  Jun Cen, Chaohui Yu, Hangjie Yuan, ....
  Links: [Project](https://github.com/alibaba-damo-academy/WorldVLA) · [Code](https://github.com/alibaba-damo-academy/WorldVLA) · [Paper](https://arxiv.org/abs/2506.21539)

- ⭐ 🤖 **[X-VLA — Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model](https://arxiv.org/abs/2510.10274)** `ICLR 2026` `7 platforms incl. Droid, Robomind, AgiBot` `VLA`
  Jinliang Zheng, Jianxiong Li, ... (2toinf).
  Links: [Project](https://2toinf.github.io/X-VLA/) · [Code](https://github.com/2toinf/X-VLA) · [Paper](https://arxiv.org/abs/2510.10274)

- ⭐ **[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos](https://arxiv.org/abs/2507.15597)** `arXiv 2025.07` `Foundation`
  VLA pretraining from large-scale human videos.
  Links: [Project](https://beingbeyond.github.io/Being-H0/) · [Code](https://github.com/BeingBeyond/Being-H0) · [Paper](https://arxiv.org/abs/2507.15597)

- ⭐ 🧍 🧱 **[Cosmos-Predict2 / 2.5 — World Simulation with Video Foundation Models for Physical AI](https://arxiv.org/abs/2511.00062)** `arXiv (Nov 2025)` `Generic physical AI` `Foundation (World Model)`
  NVIDIA Cosmos Team.
  Links: [Project](https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1/) · [Code](https://github.com/nvidia-cosmos/cosmos-predict2.5) · [Paper](https://arxiv.org/abs/2511.00062)

- ⭐ 🧱 **[Cosmos-Reason1 — From Physical Common Sense to Embodied Reasoning](https://arxiv.org/abs/2503.15558)** `arXiv (Mar 2025)` `General physical AI agents` `Foundation`
  NVIDIA Cosmos Team.
  Links: [Project](https://research.nvidia.com/labs/dir/cosmos-reason1/) · [Code](https://github.com/nvidia-cosmos/cosmos-reason1) · [Paper](https://arxiv.org/abs/2503.15558)

- 🧩 🤖 🧍 **[LeVERB — Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751)** `arXiv (Jun 2025) — CoRL 2025` `Humanoid (Unitree H1-style sim-to-real ready)` `Foundation`
  Haoru Xue, Xiaoyu Huang, ... S. Shankar Sastry, Koushil Sreenath (UC Berkeley).
  Latent vision-language instructed humanoid whole-body control.
  Links: [Project](https://ember-lab-berkeley.github.io/LeVERB-Webpage/) · [Code](https://github.com/EmberLab/LeVERB) · [Paper](https://arxiv.org/abs/2506.13751)

- 📦 🤖 🧍 **[EgoVLA — Learning VLA Models from Egocentric Human Videos](https://arxiv.org/abs/2507.12440)** `arXiv (Jul 2025)` `Unitree H1 + Inspire dexterous hands` `VLA`
  Ruihan Yang, Qinxi Yu, Yecheng Jason Ma, Xiaolong Wang.
  VLA models trained on egocentric human videos.
  Links: [Project](https://rchalyang.github.io/EgoVLA/) · [Paper](https://arxiv.org/abs/2507.12440)

- 🌐 🤖 **[GR-3 Technical Report](https://arxiv.org/abs/2507.15493)** `arXiv (Jul 2025)` `ByteMini bimanual mobile robot` `Foundation`
  ByteDance Seed Team.
  Links: [Project](https://seed.bytedance.com/GR3) · [Paper](https://arxiv.org/abs/2507.15493)

- 🌐 🤖 **[MoManipVLA — Transferring VLA Models for General Mobile Manipulation](https://arxiv.org/abs/2503.13446)** `CVPR 2025` `Mobile manipulators (humanoid-relevant)` `VLA`
  Zhenyu Wu, Yuheng Zhou, ... (BUPT / NTU / Tsinghua).
  Links: [Project](https://gary3410.github.io/momanipVLA/) · [Paper](https://arxiv.org/abs/2503.13446)

- 🌐 **[Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2509.13780)** `arXiv 2025.09` `Foundation`
  A behavior foundation model for humanoid control.
  Links: [Project](https://bfm4humanoid.github.io/) · [Paper](https://arxiv.org/abs/2509.13780)

- 🌐 **[Being-0 - A Humanoid Robotic Agent with Vision-Language Models and Modular Skills](https://arxiv.org/abs/2503.12533)** `arXiv 2025.03` `Foundation`
  Humanoid agent integrating VLMs with modular skill library.
  Links: [Project](https://beingbeyond.github.io/being-0/) · [Paper](https://arxiv.org/abs/2503.12533)

- 🌐 **[Being-M0.5 - A Real-Time Controllable Vision-Language-Motion Model](https://arxiv.org/abs/2508.07863)** `arXiv 2025.08` `Foundation`
  Real-time controllable vision-language-motion model.
  Links: [Project](https://beingbeyond.github.io/Being-M0.5/) · [Paper](https://arxiv.org/abs/2508.07863)

- 🌐 **[Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation](https://arxiv.org/pdf/2504.09532)** `arXiv 2025.04` `Foundation`
  Multimodal chain-of-action reasoning for humanoid loco-manipulation.
  Links: [Project](https://humanoid-coa.github.io/) · [Paper](https://arxiv.org/pdf/2504.09532)

- 🌐 **[GENMO - A GENeralist Model for Human MOtion](https://arxiv.org/abs/2505.01425)** `arXiv 2025.05` `Foundation`
  Generalist model for human motion.
  Links: [Project](https://research.nvidia.com/labs/dair/genmo/) · [Paper](https://arxiv.org/abs/2505.01425)

- 🌐 **[Go to Zero - Towards Zero-shot Motion Generation with Million-scale Data](https://vankouf.github.io/MotionMillion/)** `arXiv 2025.07` `Foundation`
  Zero-shot motion generation with million-scale data.
  Links: [Project](https://vankouf.github.io/MotionMillion/) · [Paper](https://vankouf.github.io/MotionMillion/)

- 🌐 **[LocoFormer - Generalist Locomotion via Long-Context Adaptation](https://generalist-locomotion.github.io/)** `arXiv 2025.09` `Foundation`
  Generalist locomotion via long-context adaptation.
  Links: [Project](https://generalist-locomotion.github.io/) · [Paper](https://generalist-locomotion.github.io/)

- 🌐 **[Unified Video Action Model](https://arxiv.org/abs/2503.00200)** `arXiv 2025.03` `Foundation`
  Unified video-action model for manipulation.
  Links: [Project](https://unified-video-action-model.github.io/) · [Paper](https://arxiv.org/abs/2503.00200)

- ❌ 🤖 🧍 **[Gemini Robotics — Bringing AI into the Physical World (incl. Robotics-ER, 1.5, On-Device)](https://arxiv.org/abs/2503.20020)** `arXiv (Mar 2025)` `Apollo humanoid (Apptronik), bimanual arms` `Foundation`
  Google DeepMind Robotics Team.
  Links: [Project](https://deepmind.google/models/gemini-robotics/) · [Paper](https://arxiv.org/abs/2503.20020)

- ❌ 🤖 🧍 **[Helix — A VLA Model for Generalist Humanoid Control](https://www.figure.ai/news/helix)** `Figure AI Tech Report (Feb 2025)` `Figure 02 humanoid` `Foundation`
  Figure AI Research Team.
  Links: [Project](https://www.figure.ai/helix) · [Paper](https://www.figure.ai/news/helix)

- ❌ 🤖 🧍 **[Humanoid-VLA — Towards Universal Humanoid Control with Visual Integration](https://arxiv.org/abs/2502.14795)** `arXiv (Feb 2025)` `Humanoid (paper-described)` `Foundation`
  Pengxiang Ding, Jianfei Ma, ... (multi-institution).
  Links: [Paper](https://arxiv.org/abs/2502.14795)

- ❌ **[DreamGen - Unlocking Generalization in Robot Learning through Neural Trajectories](https://arxiv.org/abs/2505.12705)** `arXiv 2025.05` `Foundation`
  Unlocking generalization in robot learning via neural trajectories.
  Links: [Paper](https://arxiv.org/abs/2505.12705)

- ❌ **[FLAM - Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation](https://arxiv.org/abs/2503.22249)** `arXiv 2025.03` `Foundation`
  Foundation-model-based stabilization for humanoid locomotion and manipulation.
  Links: [Paper](https://arxiv.org/abs/2503.22249)

- ❌ **[Generative World Modelling for Humanoids - 1X World Model Challenge Technical Report](https://arxiv.org/abs/2510.07092)** `arXiv 2025.10` `Foundation`
  Generative world modelling for humanoids tech report.
  Links: [Paper](https://arxiv.org/abs/2510.07092)

- ❌ **[Humanoid World Models - Open World Foundation Models for Humanoid Robotics](https://arxiv.org/abs/2506.01182)** `arXiv 2025.06` `Foundation`
  Open-world foundation models for humanoid robotics.
  Links: [Paper](https://arxiv.org/abs/2506.01182)

- ❌ **[LangWBC - Language-directed Humanoid Whole-Body Control via End-to-end Learning](https://arxiv.org/abs/2504.21738)** `arXiv 2025.04` `Foundation`
  Language-directed end-to-end whole-body humanoid control.
  Links: [Paper](https://arxiv.org/abs/2504.21738)

- ⭐ 🤖 **[HPT — Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](https://arxiv.org/abs/2409.20537)** `NeurIPS 2024 (Spotlight)` `50+ datasets / many embodiments` `Foundation`
  Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He.
  Links: [Project](https://liruiw.github.io/hpt/) · [Code](https://github.com/liruiw/HPT) · [Paper](https://arxiv.org/abs/2409.20537)

- ⭐ 🤖 🧍 **[NaVILA — Legged Robot VLA Model for Navigation](https://arxiv.org/abs/2412.04453)** `RSS 2025` `Unitree humanoid + quadruped` `VLA`
  An-Chieh Cheng, Yandong Ji, ... Xiaolong Wang (NVIDIA + UCSD).
  VLA model for legged robot navigation.
  Links: [Project](https://navila-bot.github.io/) · [Code](https://github.com/AnjieCheng/NaVILA) · [Paper](https://arxiv.org/abs/2412.04453)

- ⭐ 🤖 **[Octo — An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)** `RSS 2024` `9 robotic platforms (single+dual arm)` `Generalist-Policy`
  Octo Model Team — Dibya Ghosh, Homer Walke, Karl Pertsch, ... Sergey Levine.
  Links: [Project](https://octo-models.github.io/) · [Code](https://github.com/octo-models/octo) · [Paper](https://arxiv.org/abs/2405.12213)

- ⭐ 🤖 **[OpenVLA — An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** `CoRL 2024` `WidowX, Franka, multi-arm (29 OXE tasks)` `VLA / Generalist-Policy`
  Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, ... Chelsea Finn, Sergey Levine.
  Links: [Project](https://openvla.github.io/) · [Code](https://github.com/openvla/openvla) · [Paper](https://arxiv.org/abs/2406.09246)

- ⭐ 🤖 **[RDT-1B — A Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** `ICLR 2025` `ALOHA bimanual + others (46 datasets)` `Foundation`
  Songming Liu, Lingxuan Wu, Bangguo Yu, ... Jun Zhu (Tsinghua).
  Links: [Project](https://rdt-robotics.github.io/) · [Code](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [Paper](https://arxiv.org/abs/2410.07864)

- ⭐ 🤖 **[Robotic Control via Embodied Chain-of-Thought Reasoning (ECoT)](https://arxiv.org/abs/2407.08693)** `CoRL 2024` `WidowX (BridgeData V2)` `VLA`
  Michał Zawalski, William Chen, Karl Pertsch, ... Sergey Levine.
  Links: [Project](https://embodied-cot.github.io/) · [Code](https://github.com/MichalZawalski/embodied-CoT) · [Paper](https://arxiv.org/abs/2407.08693)

- ⭐ 🤖 **[TinyVLA — Towards Fast, Data-Efficient Vision-Language-Action Models](https://arxiv.org/abs/2409.12514)** `RA-L 2025` `Franka, real-world tasks` `VLA`
  Junjie Wen, Yichen Zhu, ... (Midea Group / SJTU).
  Links: [Project](https://tiny-vla.github.io/) · [Code](https://github.com/lesjie-wen/tinyvla) · [Paper](https://arxiv.org/abs/2409.12514)

- 🧩 🤖 🧍 **[1X World Model — Evaluating Bits, Not Atoms](https://www.1x.tech/1x-world-model.pdf)** `1X Tech Report; 2024–2026 release cycle` `1X EVE / NEO humanoid` `Foundation (World Model)`
  1X Technologies World Model Team.
  Links: [Project](https://www.1x.tech/discover/1x-world-model) · [Code](https://github.com/1x-technologies/1xgpt) · [Paper](https://www.1x.tech/1x-world-model.pdf)

- 🌐 🤖 **[GR-2 — A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](https://arxiv.org/abs/2410.06158)** `arXiv (Oct 2024)` `Dual-arm setups` `Foundation`
  Chilam Cheang, Sijin Chen, Zhongren Cui, ... (ByteDance Research).
  Links: [Project](https://gr2-manipulation.github.io/) · [Paper](https://arxiv.org/abs/2410.06158)

- 🌐 **[Harmon - Whole-Body Motion Generation of Humanoid Robots from Language Descriptions](https://arxiv.org/abs/2410.12773)** `arXiv 2024.10` `Foundation`
  Whole-body humanoid motion generation from language.
  Links: [Project](https://ut-austin-rpl.github.io/Harmon/) · [Paper](https://arxiv.org/abs/2410.12773)

- 🌐 **[Humanoid Locomotion as Next Token Prediction](https://arxiv.org/abs/2402.19469)** `arXiv 2024.02` `Foundation`
  Treats humanoid locomotion as next-token prediction.
  Links: [Project](https://humanoid-next-token-prediction.github.io/) · [Paper](https://arxiv.org/abs/2402.19469)

- ❌ 🤖 **[RT-H — Action Hierarchies Using Language](https://arxiv.org/abs/2403.01823)** `arXiv (Mar 2024)` `Everyday Robots` `VLA`
  Suneel Belkhale, Ted Xiao, Pierre Sermanet, ... (Google DeepMind).
  Links: [Project](https://rt-hierarchy.github.io/) · [Paper](https://arxiv.org/abs/2403.01823)

- ❌ 🧱 **[MotionGPT-2 — A General-Purpose Motion-Language Model for Motion Generation and Understanding](https://arxiv.org/abs/2410.21747)** `arXiv (Oct 2024)` `Human motion` `Foundation (Motion)`
  Yuan Wang, Di Huang, ... (Fudan).
  Links: [Paper](https://arxiv.org/abs/2410.21747)

- ❌ **[Scaling Large Motion Models with Million-Level Human Motions](https://arxiv.org/abs/2410.03311)** `arXiv 2024.10` `Foundation`
  Scaling large motion models with million-level human motion data.
  Links: [Paper](https://arxiv.org/abs/2410.03311)

- ⭐ 🤖 **[ACT — Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA)](https://arxiv.org/abs/2304.13705)** `RSS 2023` `ALOHA bimanual` `Generalist-Policy`
  Tony Z. Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn.
  Links: [Project](https://tonyzhaozh.github.io/aloha/) · [Code](https://github.com/tonyzhaozh/act) · [Paper](https://arxiv.org/abs/2304.13705)

- ⭐ 🤖 **[Diffusion Policy — Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** `RSS 2023; IJRR 2024` `Multiple manipulation platforms` `Generalist-Policy`
  Cheng Chi, Siyuan Feng, Yilun Du, ... Shuran Song.
  Links: [Project](https://diffusion-policy.cs.columbia.edu/) · [Code](https://github.com/real-stanford/diffusion_policy) · [Paper](https://arxiv.org/abs/2303.04137)

- ⭐ 🤖 **[GR-1 — Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](https://arxiv.org/abs/2312.13139)** `ICLR 2024` `Franka, CALVIN sim` `Foundation`
  Hongtao Wu, Ya Jing, Chilam Cheang, ... Tao Kong (ByteDance).
  Links: [Project](https://gr1-manipulation.github.io/) · [Code](https://github.com/bytedance/GR-1) · [Paper](https://arxiv.org/abs/2312.13139)

- ⭐ 🤖 **[RoboFlamingo — Vision-Language Foundation Models as Effective Robot Imitators](https://arxiv.org/abs/2311.01378)** `ICLR 2024` `CALVIN sim, Franka` `VLA`
  Xinghang Li, Minghuan Liu, Hanbo Zhang, ... Tao Kong.
  Links: [Project](https://roboflamingo.github.io/) · [Code](https://github.com/RoboFlamingo/RoboFlamingo) · [Paper](https://arxiv.org/abs/2311.01378)

- ⭐ 🤖 **[RT-X / Open X-Embodiment — Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** `ICRA 2024` `22 different robot embodiments` `Generalist-Policy / Dataset`
  Open X-Embodiment Collaboration (21 institutions).
  1M+ trajectories, 22 embodiments, 60 datasets pooled across 21 institutions.
  Links: [Project](https://robotics-transformer-x.github.io/) · [Code](https://github.com/google-deepmind/open_x_embodiment) · [Paper](https://arxiv.org/abs/2310.08864) · [Dataset](https://robotics-transformer-x.github.io/)

- ⭐ 🧱 **[MotionGPT — Human Motion as a Foreign Language](https://arxiv.org/abs/2306.14795)** `NeurIPS 2023` `Human motion (retargettable to humanoid)` `Foundation (Motion)`
  Biao Jiang, Xin Chen, Wen Liu, ... (Fudan / Tencent).
  Links: [Project](https://motion-gpt.github.io/) · [Code](https://github.com/OpenMotionLab/MotionGPT) · [Paper](https://arxiv.org/abs/2306.14795)

- 🔁 🤖 **[RT-2 — Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** `CoRL 2023` `Everyday Robots` `VLA`
  Brohan et al. (Google DeepMind).
  Links: [Project](https://robotics-transformer2.github.io/) · [Paper](https://arxiv.org/abs/2307.15818)

- 🧩 🤖 **[RT-1 — Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** `RSS 2023` `Everyday Robots mobile manipulators` `Generalist-Policy`
  Anthony Brohan, Noah Brown, Justice Carbajal, ... (Google).
  Links: [Project](https://robotics-transformer1.github.io/) · [Code](https://github.com/google-research/robotics_transformer) · [Paper](https://arxiv.org/abs/2212.06817)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motio](https://arxiv.org/abs/2606.03985) | Unitree G1 / humanoid | ✅ | ⭐ Code | GPT-style causal Transformer trained on a two-billion-frame retargeted motion co |
| 2026 | [OMG: Omni-Modal Motion Generation for Generalist Humanoid Co](https://arxiv.org/abs/2606.10340) | Unitree G1 | ✅ | ⭐ Code | Generalist humanoid control stack that places an omni-modal motion-generation br |
| 2026 | [Cosmos Policy — Fine-Tuning Video Models for Visuomotor Cont](https://arxiv.org/abs/2601.16163) | LIBERO, RoboCasa simulators | — | ⭐ Code |  |
| 2026 | [LIFT - Towards Bridging the Gap between Large-Scale Pretrain](https://arxiv.org/abs/2601.21363) | — | — | ⭐ Code | Pretraining-then-finetuning for humanoid control. |
| 2026 | [MotionVLA: Vision-Language-Action Model for Humanoid Motion](https://arxiv.org/abs/2606.15142) | humanoid motion / HumanML3D / MBench | — | ⭐ Code | Adapts VLA-style autoregressive modeling to humanoid motion with separate low-fr |
| 2026 | [MolmoAct 2 — Action Reasoning Models for Real-world Deployme](https://arxiv.org/abs/2605.02881) | Franka, SO100/SO101, bimanual YAM | ✅ | 🧩 Partial Code | Open VLA stack with MolmoER backbone, OpenFAST action tokenizer, MolmoThink adap |
| 2026 | [Ego-Pi: VLA Fine-Tuning for Ego-Centric Human and Robot Data](https://arxiv.org/abs/2606.08107) | humanoid hands / dexterous embodiments | ✅ | 🌐 Project Page | Studies pi0.5 fine-tuning across egocentric human data and humanoid embodiments  |
| 2026 | [Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from](https://arxiv.org/abs/2606.32009) | PrimeU 60-DoF upper-body humanoid | ✅ | 🌐 Project Page | Converts synchronized ego-exo human videos into controller-aligned humanoid acti |
| 2026 | [Closing the Loop in Humanoid VLA: Persistent 3D Object Token](https://arxiv.org/abs/2607.18016) | Unitree G1 / Being-0-aligned humanoid | ✅ | ❌ No Code | POT-VLA maintains role-indexed 3D object records that both condition whole-body  |
| 2026 | [MotionWAM: Towards Foundation World Action Models for Real-T](https://arxiv.org/abs/2606.09215) | Unitree G1 | ✅ | ❌ No Code | Real-time world-action model for humanoid loco-manipulation that avoids slow vid |
| 2026 | [Perceptive Behavior Foundation Model: Adapting Human Motion ](https://arxiv.org/abs/2606.08059) | humanoid | ✅ | ❌ No Code | Adapts broad human motion priors to robot-centric terrain constraints for reusab |
| 2026 | [Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163) | humanoid | ✅ | ❌ No Code | Studies the scaling recipe for humanoid BFMs by coordinating global-frame motion |
| 2026 | [Psi0 - An Open Foundation Model Towards Universal Humanoid L](https://arxiv.org/abs/2603.12263) | — | — | ❌ No Code | Open foundation model targeting universal humanoid loco-manipulation. |
| 2026 | [WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework f](https://arxiv.org/abs/2606.25591) | humanoid | — | ❌ No Code | Builds a VLA training framework from whole-body optimal-control trajectories, eg |
| 2025 | [AgiBot World Colosseo + GO-1 — Large-scale Manipulation Plat](https://arxiv.org/abs/2503.06669) | AgiBot mobile humanoid (whole-body, dexterous hands, tactile) | ✅ | ⭐ Code | 1M+ trajectories across 217 tasks in 5 deployment scenarios from 100 real robots |

## Human-to-Humanoid Retargeting

_15 entries._

- ⭐ 🤖 🧍 **[Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](https://arxiv.org/abs/2606.22136)** `arXiv 2026.06` `dexterous hands / humanoid-relevant manipulation` `Retargeting`
  Yangtao Chen et al..
  Uses generative video world models to synthesize egocentric human-object manipulation videos and converts them into robot-trainable supervision.
  Links: [Project](https://chenyt31.github.io/wh0.github.io/) · [Code](https://github.com/chenyt31/Wh0) · [Paper](https://arxiv.org/abs/2606.22136)

- 🌐 🤖 🧍 **[EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning](https://arxiv.org/abs/2606.17385)** `arXiv 2026.06` `robot hands / humanoid-relevant manipulation` `Retargeting`
  Gaotian Wang et al..
  Converts arbitrary RGB hand-object videos into 4D interaction data for robot retargeting through reconstruction, refinement, and action extraction.
  Links: [Project](https://huggingface.co/spaces/Rice-RobotPI-Lab/EgoInfinity) · [Paper](https://arxiv.org/abs/2606.17385)

- 🌐 🤖 🧍 **[Proprioceptive-visual correspondence enables self-other distinction in humanoid robots](https://arxiv.org/abs/2606.13222)** `arXiv 2026.06` `humanoid` `Retargeting`
  Yurun Chen et al..
  Learns self-other distinction and a predictive 3D body occupancy model from proprioceptive-visual correspondence.
  Links: [Project](https://euron-zc.github.io/humanoid-self-model/) · [Paper](https://arxiv.org/abs/2606.13222)

- 🌐 🤖 🧍 **[TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation](https://arxiv.org/abs/2606.16272)** `arXiv 2026.06` `dexterous hands / humanoid hands` `Retargeting`
  Jielin Wu et al..
  Retargets dexterous manipulation by preserving local hand-object interaction graphs instead of copying hand pose alone.
  Links: [Project](https://toporetarget2026.github.io/TopoRetarget/) · [Paper](https://arxiv.org/abs/2606.16272)

- ⏳ 🤖 🧍 **[Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots](https://arxiv.org/abs/2606.03476)** `arXiv 2026.06` `Unitree G1 / humanoid` `Retargeting`
  Tianchen Huang et al..
  Unsupervised physics-aware retargeting transfers human motions to humanoid behaviors despite topology, proportion, and DoF mismatch.
  Links: [Project](https://huangtc233.github.io/human2humanoid_website/) · [Paper](https://arxiv.org/abs/2606.03476)

- ❌ 🤖 🧍 **[From Sign Language Generation to Humanoid Execution: Vision-Language Guided Retargeting with Collision Mitigation](https://arxiv.org/abs/2607.17769)** `arXiv 2026.07` `humanoid robot` `Retargeting`
  Nabeela Khan et al..
  Converts generated sign-language body motions into humanoid joint execution through SMPL-X collision mitigation and VLM-guided retargeting corrections.
  Links: [Paper](https://arxiv.org/abs/2607.17769)

- ❌ 🤖 **[Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization](https://arxiv.org/abs/2606.10743)** `arXiv 2026.06` `robot arms / manipulation` `Retargeting`
  Yitian Shi et al..
  HOWTransfer converts noisy human videos into contact-aware, taxonomy-informed robot trajectories for unseen objects.
  Links: [Paper](https://arxiv.org/abs/2606.10743)

- ❌ 🤖 🧍 **[ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting](https://arxiv.org/abs/2605.06593)** `SIGGRAPH 2026` `humanoid / quadruped morphologies` `Retargeting`
  David Muller et al..
  Bilevel RL retargeting jointly adapts reference motion and trains a policy to produce physically feasible motions across morphologies.
  Links: [Paper](https://arxiv.org/abs/2605.06593)

- ❌ **[A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation](https://arxiv.org/abs/2602.01632)** `arXiv 2026.02` `Retarget`
  Closed-form geometric retargeting solver for upper-body teleoperation.
  Links: [Paper](https://arxiv.org/abs/2602.01632)

- ⭐ 🤖 🧍 **[HumanoidVerse: A Versatile Multi-Simulator Humanoid Learning Framework](https://arxiv.org/abs/2508.16943)** `arXiv preprint` `Unitree G1/H1, multiple` `Retargeting`
  LeCAR Lab.
  Modular multi-simulator framework for humanoid skill learning with retargeted human MoCap, used by ASAP and follow-ups.
  Links: [Project](https://github.com/LeCAR-Lab/HumanoidVerse) · [Code](https://github.com/LeCAR-Lab/HumanoidVerse) · [Paper](https://arxiv.org/abs/2508.16943)

- ⭐ 🧱 **[DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2505.24853)** `NeurIPS 2025` `multiple dexterous hands` `Retargeting`
  Mandi Zhao, et al..
  Functional retargeting via decaying virtual object controllers for long-horizon bimanual articulated-object manipulation from human demos.
  Links: [Project](https://project-dexmachina.github.io/) · [Code](https://github.com/MandiZhao/dexmachina) · [Paper](https://arxiv.org/abs/2505.24853)

- 🧩 🤖 **[AnyDexGrasp: General Dexterous Grasping for Different Hands with Human-level Learning Efficiency](https://arxiv.org/abs/2502.16420)** `arXiv preprint` `3 dexterous hands` `Retargeting`
  Hao-Shu Fang, et al..
  Two-stage cross-embodiment grasping using a contact-centric grasp representation that retargets to any hand.
  Links: [Project](https://graspnet.net/anydexgrasp/) · [Code](partial release) · [Paper](https://arxiv.org/abs/2502.16420)

- ❌ 🤖 🧍 **[Implicit Kinodynamic Motion Retargeting for Human-to-Humanoid Imitation Learning (IKMR)](https://arxiv.org/abs/2509.15443)** `arXiv preprint` `full-size humanoid` `Retargeting`
  Haodong Zhang, et al..
  Neural retargeter that jointly considers kinematics and dynamics, refining trajectories to physically feasible ones at scale.
  Links: [Code](not released yet) · [Paper](https://arxiv.org/abs/2509.15443)

- ❌ **[Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation](https://arxiv.org/abs/2510.04353)** `arXiv 2025.10` `Retarget`
  Stability-aware retargeting for multi-contact teleoperation.
  Links: [Paper](https://arxiv.org/abs/2510.04353)

- ⭐ 🧍 🧱 **[Mink — Differential Inverse Kinematics in Python (MuJoCo)](https://kevinzakka.github.io/mink/)** `open-source library` `G1, H1, Apollo, dual arms, dexterous hands` `Retargeting`
  Kevin Zakka.
  Composable task-space IK on MuJoCo used by GMR, ProtoMotions, and many teleop stacks for retargeting and live tracking.
  Links: [Project](https://kevinzakka.github.io/mink/) · [Code](https://github.com/kevinzakka/mink) · [Paper](https://kevinzakka.github.io/mink/)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [Wh0: Generative World Models as Scalable Sources of Egocentr](https://arxiv.org/abs/2606.22136) | dexterous hands / humanoid-relevant manipulation | ✅ | ⭐ Code | Uses generative video world models to synthesize egocentric human-object manipul |
| 2026 | [EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Eng](https://arxiv.org/abs/2606.17385) | robot hands / humanoid-relevant manipulation | ✅ | 🌐 Project Page | Converts arbitrary RGB hand-object videos into 4D interaction data for robot ret |
| 2026 | [Proprioceptive-visual correspondence enables self-other dist](https://arxiv.org/abs/2606.13222) | humanoid | ✅ | 🌐 Project Page | Learns self-other distinction and a predictive 3D body occupancy model from prop |
| 2026 | [TopoRetarget: Interaction-Preserving Retargeting for Dextero](https://arxiv.org/abs/2606.16272) | dexterous hands / humanoid hands | ✅ | 🌐 Project Page | Retargets dexterous manipulation by preserving local hand-object interaction gra |
| 2026 | [Human2Humanoid: Physics-Aware Cross-Morphology Motion Retarg](https://arxiv.org/abs/2606.03476) | Unitree G1 / humanoid | ✅ | ⏳ Code Coming Soon | Unsupervised physics-aware retargeting transfers human motions to humanoid behav |
| 2026 | [From Sign Language Generation to Humanoid Execution: Vision-](https://arxiv.org/abs/2607.17769) | humanoid robot | ✅ | ❌ No Code | Converts generated sign-language body motions into humanoid joint execution thro |
| 2026 | [Hand-centric Human-to-Robot Trajectory Transfer from Video D](https://arxiv.org/abs/2606.10743) | robot arms / manipulation | ✅ | ❌ No Code | HOWTransfer converts noisy human videos into contact-aware, taxonomy-informed ro |
| 2026 | [ReActor: Reinforcement Learning for Physics-Aware Motion Ret](https://arxiv.org/abs/2605.06593) | humanoid / quadruped morphologies | ✅ | ❌ No Code | Bilevel RL retargeting jointly adapts reference motion and trains a policy to pr |
| 2026 | [A Closed-Form Geometric Retargeting Solver for Upper Body Hu](https://arxiv.org/abs/2602.01632) | — | — | ❌ No Code | Closed-form geometric retargeting solver for upper-body teleoperation. |
| 2025 | [HumanoidVerse: A Versatile Multi-Simulator Humanoid Learning](https://arxiv.org/abs/2508.16943) | Unitree G1/H1, multiple | ✅ | ⭐ Code | Modular multi-simulator framework for humanoid skill learning with retargeted hu |
| 2025 | [DexMachina: Functional Retargeting for Bimanual Dexterous Ma](https://arxiv.org/abs/2505.24853) | multiple dexterous hands | — | ⭐ Code | Functional retargeting via decaying virtual object controllers for long-horizon  |
| 2025 | [AnyDexGrasp: General Dexterous Grasping for Different Hands ](https://arxiv.org/abs/2502.16420) | 3 dexterous hands | ✅ | 🧩 Partial Code | Two-stage cross-embodiment grasping using a contact-centric grasp representation |
| 2025 | [Implicit Kinodynamic Motion Retargeting for Human-to-Humanoi](https://arxiv.org/abs/2509.15443) | full-size humanoid | ✅ | ❌ No Code | Neural retargeter that jointly considers kinematics and dynamics, refining traje |
| 2025 | [Stability-Aware Retargeting for Humanoid Multi-Contact Teleo](https://arxiv.org/abs/2510.04353) | — | — | ❌ No Code | Stability-aware retargeting for multi-contact teleoperation. |
| 2024 | [Mink — Differential Inverse Kinematics in Python (MuJoCo)](https://kevinzakka.github.io/mink/) | G1, H1, Apollo, dual arms, dexterous hands | — | ⭐ Code | Composable task-space IK on MuJoCo used by GMR, ProtoMotions, and many teleop st |

## Teleoperation and Demonstration Collection

_36 entries._

- 🌐 🤖 🧍 **[HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum](https://arxiv.org/abs/2607.02332)** `arXiv 2026.07` `L7 full-size humanoid` `Teleoperation`
  Chenxin Liu et al..
  Uses privileged motion guidance and a windowed payload curriculum so a full-size humanoid can track VR references while carrying up to 24 kg.
  Links: [Project](https://heft.axell.top/) · [Paper](https://arxiv.org/abs/2607.02332)

- 🌐 🤖 🧍 **[RealDexUMI: A Wearable Universal Manipulation Interface for Dexterous Robot Learning](https://arxiv.org/abs/2606.06033)** `arXiv 2026.06` `dexterous hands / humanoid-relevant manipulation` `Teleoperation`
  Chaoyi Xu et al..
  Wearable universal manipulation interface preserves fine hand-object interactions while producing deployable dexterous robot data.
  Links: [Project](https://research.beingbeyond.com/realdexumi) · [Paper](https://arxiv.org/abs/2606.06033)

- 🌐 🤖 🧍 **[Universal Manipulation Exoskeleton: Learning Compliant Whole-Body Policies with Real-time Torque Feedback](https://arxiv.org/abs/2606.14218)** `arXiv 2026.06` `humanoid-relevant mobile manipulation` `Teleoperation`
  Litian Liang et al..
  Portable upper-limb exoskeleton records arm configurations and joint torque feedback for learning contact-compliant whole-body manipulation policies.
  Links: [Project](https://ume-exo.github.io/) · [Paper](https://arxiv.org/abs/2606.14218)

- ❌ 🤖 🧍 **[DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy](https://arxiv.org/abs/2606.23431)** `arXiv 2026.06` `bimanual dexterous hands / humanoid-relevant manipulation` `Teleoperation`
  Haichao Liu et al..
  Adds tactile-driven force-compliant optimization on top of bimanual teleoperation to close embodiment gaps in contact-rich manipulation.
  Links: [Paper](https://arxiv.org/abs/2606.23431)

- ❌ 🤖 🧍 **[HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2606.27239)** `arXiv 2026.06` `humanoid` `Teleoperation`
  Hongwu Wang et al..
  Collects robot-free VR/UMI-style demonstrations and retargets sparse human keypoints into humanoid whole-body references for skill learning.
  Links: [Paper](https://arxiv.org/abs/2606.27239)

- ❌ 🤖 🧍 **[X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting](https://arxiv.org/abs/2606.07934)** `arXiv 2026.06` `humanoid / cross-morphology robots` `Teleoperation`
  Jen-Wei Wang et al..
  MPC-based retargeting enables cross-morphology whole-body teleoperation without robot-specific end-to-end retraining.
  Links: [Paper](https://arxiv.org/abs/2606.07934)

- ❌ **[CLOT - Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation](https://arxiv.org/abs/2602.15060)** `arXiv 2026.02` `Teleop`
  Closed-loop global motion tracking for whole-body teleoperation.
  Links: [Paper](https://arxiv.org/abs/2602.15060)

- ⭐ 🤖 **[ACE-F: A Cross Embodiment Foldable System with Force Feedback for Dexterous Teleoperation](https://arxiv.org/abs/2511.20887)** `arXiv preprint` `multiple` `Teleoperation`
  et al..
  Foldable cross-embodiment exoskeleton adds force feedback to ACE-style teleop for higher-quality demos.
  Links: [Code](announced) · [Paper](https://arxiv.org/abs/2511.20887)

- ⭐ 🤖 **[AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons](https://arxiv.org/abs/2503.03081)** `arXiv preprint` `dual-arm robots` `Teleoperation`
  Hongjie Fang, et al..
  Scaled AirExo with adapters that turn in-the-wild data into pseudo-robot demos for RISE-2 IL policy.
  Links: [Project](https://airexo.tech/airexo2/) · [Code](https://github.com/AirExo/airexo-2) · [Paper](https://arxiv.org/abs/2503.03081)

- ⭐ 🤖 🧍 **[CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks](https://arxiv.org/abs/2506.08931)** `CoRL 2025` `Unitree H1` `Teleoperation`
  Yutang Lin, et al..
  MoE whole-body policy + LiDAR odometry closed-loop teleop achieving 12 cm drift over 8.9 m using only head/hand MR tracking.
  Links: [Project](https://humanoid-clone.github.io/) · [Code](https://github.com/humanoid-clone/CLONE) · [Paper](https://arxiv.org/abs/2506.08931)

- ⭐ 🤖 **[DEXOP: A Device for Robotic Transfer of Dexterous Human Manipulation](https://arxiv.org/abs/2509.04441)** `arXiv preprint` `dexterous hands` `Teleoperation`
  Hao-Shu Fang, Branden Romero, et al. (MIT Improbable AI).
  Passive hand exoskeleton coined "perioperation" — connects human fingers to robot fingers for high-quality vision+tactile demos.
  Links: [Project](https://dex-op.github.io/) · [Code](https://github.com/HaoshuFang/DEXOP) · [Paper](https://arxiv.org/abs/2509.04441)

- ⭐ 🤖 **[DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation](https://arxiv.org/abs/2505.21864)** `CoRL 2025 (Best Paper Final List)` `2 dexterous hands` `Teleoperation`
  Mengda Xu, Han Zhang, et al..
  Wearable hand exoskeleton + visual in-painting that lets human hand directly serve as a dexterous interface; 86% real-world success.
  Links: [Project](https://dex-umi.github.io/) · [Code](https://github.com/real-stanford/DexUMI) · [Paper](https://arxiv.org/abs/2505.21864)

- ⭐ 🤖 **[H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation](https://arxiv.org/abs/2507.23523)** `arXiv preprint` `bimanual / humanoid` `Teleoperation`
  Hongzhe Bi, et al..
  2B diffusion transformer pretrained on 338K EgoDex human trajectories then fine-tuned on robot demos.
  Links: [Project](https://embodiedfoundation.github.io/hrdt) · [Code](https://github.com/HongzheBi/H_RDT) · [Paper](https://arxiv.org/abs/2507.23523)

- 🌐 🤖 🧍 **[CHILD: Controller for Humanoid Imitation and Live Demonstration](https://arxiv.org/abs/2508.00162)** `arXiv preprint` `humanoid` `Teleoperation`
  et al..
  Compact baby-carrier-form teleop rig giving operator joint-level control of all four humanoid limbs.
  Links: [Project](https://uiuckimlab.github.io/CHILD-pages/) · [Code](announced) · [Paper](https://arxiv.org/abs/2508.00162)

- 🌐 **[SPARK - A Toolbox for Safe Humanoid Autonomy and Teleoperation](https://arxiv.org/abs/2502.03132)** `arXiv 2025.02` `Teleop`
  Safety toolbox for humanoid autonomy and teleoperation.
  Links: [Project](https://intelligent-control-lab.github.io/spark/) · [Paper](https://arxiv.org/abs/2502.03132)

- ❌ 🤖 **[EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations](https://arxiv.org/abs/2511.00153)** `arXiv preprint` `humanoid-adjacent` `Teleoperation`
  et al..
  Captures synchronized head and hand trajectories during human demos and retargets to semi-humanoid embodiments.
  Links: [Code](announced) · [Paper](https://arxiv.org/abs/2511.00153)

- ❌ 🤖 🧍 **[Learning Adaptive Neural Teleoperation for Humanoid Robots: From IK to End-to-End Control](https://arxiv.org/abs/2511.12390)** `arXiv preprint` `Unitree G1` `Teleoperation`
  et al..
  Replaces IK+PD teleop with RL-trained policy mapping VR controller inputs directly to joints; 34% lower tracking error.
  Links: [Code](not released) · [Paper](https://arxiv.org/abs/2511.12390)

- ❌ 🤖 **[MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies](https://arxiv.org/abs/2509.17759)** `arXiv preprint` `Franka + Inspire Hand` `Teleoperation`
  et al..
  Builds on Open-TeleVision to capture wrist+hand poses and co-trains human-robot policies for motion-level transfer.
  Links: [Code](announced) · [Paper](https://arxiv.org/abs/2509.17759)

- ❌ 🤖 🧍 **[NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid Robots](https://arxiv.org/abs/2503.10554)** `ICRA 2026` `humanoid (full-size)` `Teleoperation`
  et al..
  Backpack 5.2 kg active-joint exoskeleton with sternoclavicular compensation for 100% upper-limb ROM teleop in outdoor settings.
  Links: [Code](not released) · [Paper](https://arxiv.org/abs/2503.10554)

- ⭐ 🤖 **[AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild](https://arxiv.org/abs/2309.14975)** `ICRA 2024` `dual-arm robots` `Teleoperation`
  Hongjie Fang, et al..
  Low-cost passive dual-arm exoskeleton for in-the-wild demonstration collection without a robot.
  Links: [Project](https://airexo.github.io/) · [Code](https://github.com/AirExo/collector) · [Paper](https://arxiv.org/abs/2309.14975)

- ⭐ 🤖 **[AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch](https://arxiv.org/abs/2405.07391)** `CoRL 2024` `dexterous hand` `Teleoperation`
  Max Yang, et al..
  Unified policy rotates objects about any axis in any hand orientation using dense tactile feedback transferred from sim.
  Links: [Project](https://maxyang27896.github.io/anyrotate/) · [Code](https://github.com/maxyang27896/anyrotate) · [Paper](https://arxiv.org/abs/2405.07391)

- ⭐ 🤖 **[ARCap: Collecting High-quality Human Demonstrations for Robot Learning with Augmented Reality Feedback](https://arxiv.org/abs/2410.08464)** `ICRA 2025` `parallel-jaw, multi-finger hands` `Teleoperation`
  Sirui Chen, et al..
  AR headset overlays virtual robot kinematics on human hands during demo collection, enabling novices to gather robot-executable data.
  Links: [Project](https://stanford-tml.github.io/ARCap/) · [Code](https://github.com/Ericcsr/ARCap) · [Paper](https://arxiv.org/abs/2410.08464)

- ⭐ 🤖 **[BiDex: Bimanual Dexterity for Complex Tasks](https://arxiv.org/abs/2411.13677)** `CoRL 2024` `bimanual dexterous robots` `Teleoperation`
  Kenneth Shaw, Yulong Li, Jiahui Yang, et al..
  Manus motion-capture gloves + GELLO-style arm tracking for fast in-the-wild bimanual dexterous teleop.
  Links: [Project](https://bidex-teleop.github.io/) · [Code](https://github.com/dexsuite/bidex) · [Paper](https://arxiv.org/abs/2411.13677)

- ⭐ 🤖 **[Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning](https://arxiv.org/abs/2407.03162)** `CoRL 2024` `bimanual dexterous robots` `Teleoperation`
  Runyu Ding, et al..
  Apple Vision Pro driven bimanual teleop with collision/singularity avoidance and low-cost haptic finger cots.
  Links: [Project](https://dingry.github.io/projects/bunny_visionpro.html) · [Code](https://github.com/Dingry/BunnyVisionPro) · [Paper](https://arxiv.org/abs/2407.03162)

- ⭐ 🤖 **[DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788)** `RSS 2024` `dexterous robot hands` `Teleoperation`
  Chen Wang, et al..
  Portable hand-mocap rig (SLAM + EMF tracking + RGB-D) for in-the-wild dexterous demo collection 3× faster than teleop.
  Links: [Project](https://dex-cap.github.io/) · [Code](https://github.com/j96w/DexCap) · [Paper](https://arxiv.org/abs/2403.07788)

- ⭐ 🤖 🧍 **[DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/abs/2410.24185)** `ICRA 2025` `humanoid + dexterous hands` `Teleoperation`
  Zhenyu Jiang, et al..
  Synthesizes 21K bimanual dexterous trajectories from 60 human demos via subtask-aware replay.
  Links: [Project](https://dexmimicgen.github.io/) · [Code](https://github.com/NVlabs/dexmimicgen) · [Paper](https://arxiv.org/abs/2410.24185)

- ⭐ 🤖 **[EgoMimic: Scaling Imitation Learning via Egocentric Video](https://arxiv.org/abs/2410.24221)** `ICRA 2025` `bimanual (humanoid-adjacent)` `Teleoperation`
  Simar Kareer, Dhruv Patel, et al..
  Project Aria glasses + low-cost bimanual robot with kinematic gap minimized; co-trains on human and robot data.
  Links: [Project](https://egomimic.github.io/) · [Code](https://github.com/SimarKareer/EgoMimic) · [Paper](https://arxiv.org/abs/2410.24221)

- ⭐ 🤖 **[Open Teach: A Versatile Teleoperation System for Robotic Manipulation](https://arxiv.org/abs/2403.07870)** `CoRL 2024` `Franka, xArm, Jaco, Allegro` `Teleoperation`
  Aadhithya Iyer, et al..
  Open Meta Quest 3-based 90Hz teleop framework supporting hands+arms across 38 tasks and many robots.
  Links: [Project](https://open-teach.github.io/) · [Code](https://github.com/aadhithya14/Open-Teach) · [Paper](https://arxiv.org/abs/2403.07870)

- ⭐ 🤖 **[Universal Manipulation Interface (UMI): In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** `RSS 2024` `any parallel-jaw arm` `Teleoperation`
  Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, et al..
  Hand-held parallel-jaw gripper + GoPro that records portable, hardware-agnostic demos for diffusion-policy training.
  Links: [Project](https://umi-gripper.github.io/) · [Code](https://github.com/real-stanford/universal_manipulation_interface) · [Paper](https://arxiv.org/abs/2402.10329)

- ❌ **[High-Speed and Impact Resilient Teleoperation of Humanoid Robots](https://arxiv.org/abs/2409.04639v1)** `arXiv 2024.09` `Teleop`
  High-speed impact-resilient humanoid teleoperation.
  Links: [Paper](https://arxiv.org/abs/2409.04639v1)

- ⭐ 🤖 **[AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System](https://arxiv.org/abs/2307.04577)** `RSS 2023` `Allegro, Shadow Hand, multiple arms` `Teleoperation`
  Yuzhe Qin, et al..
  General vision-based dexterous arm-hand teleop with hardware/sim/camera-agnostic retargeting library.
  Links: [Project](https://yzqin.github.io/anyteleop/) · [Code](https://github.com/dexsuite/dex-retargeting) · [Paper](https://arxiv.org/abs/2307.04577)

- ⭐ 🤖 **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://arxiv.org/abs/2309.13037)** `IROS 2024` `Franka, UR5, xArm` `Teleoperation`
  Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, Pieter Abbeel.
  3D-printed kinematic-twin puppeteer providing intuitive joint-level demos at very low cost.
  Links: [Project](https://wuphilipp.github.io/gello_site/) · [Code](https://github.com/wuphilipp/gello_software) · [Paper](https://arxiv.org/abs/2309.13037)

- ⭐ **[TRILL - Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation](https://arxiv.org/abs/2309.01952)** `arXiv 2023.09` `Teleop`
  Deep imitation learning for loco-manipulation via human teleoperation.
  Links: [Project](https://ut-austin-rpl.github.io/TRILL/) · [Code](https://github.com/UT-Austin-RPL/TRILL) · [Paper](https://arxiv.org/abs/2309.01952)

- 🌐 **[Teleoperation of Humanoid Robots - A Survey](https://arxiv.org/abs/2301.04317)** `arXiv 2023.01` `Teleop`
  A survey of humanoid robot teleoperation.
  Links: [Project](https://humanoid-teleoperation.github.io/) · [Paper](https://arxiv.org/abs/2301.04317)

- ⭐ 🤖 **[Robotic Telekinesis: Learning a Robotic Hand Imitator by Watching Humans on Youtube](https://arxiv.org/abs/2202.10448)** `RSS 2022` `Allegro Hand on Franka` `Teleoperation`
  Aravind Sivakumar, Kenneth Shaw, Deepak Pathak.
  Single-RGB-camera teleop trained on internet hand videos; first low-cost glove-free dexterous teleop.
  Links: [Project](https://robotic-telekinesis.github.io/) · [Code](https://github.com/sraviakv/robotic-telekinesis) · [Paper](https://arxiv.org/abs/2202.10448)

- ⭐ **[iCub3 Avatar System - Enabling Remote Fully-Immersive Embodiment of Humanoid Robots](https://arxiv.org/abs/2203.06972)** `arXiv 2022.03 / Science Robotics` `Teleop`
  Fully-immersive remote embodiment with iCub3 avatar.
  Links: [Project](https://www.science.org/doi/10.1126/scirobotics.adh3834) · [Code](https://github.com/ami-iit/paper_dafarra_2024_science-robotics_icub3-avatar-system) · [Paper](https://arxiv.org/abs/2203.06972)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Pr](https://arxiv.org/abs/2607.02332) | L7 full-size humanoid | ✅ | 🌐 Project Page | Uses privileged motion guidance and a windowed payload curriculum so a full-size |
| 2026 | [RealDexUMI: A Wearable Universal Manipulation Interface for ](https://arxiv.org/abs/2606.06033) | dexterous hands / humanoid-relevant manipulation | ✅ | 🌐 Project Page | Wearable universal manipulation interface preserves fine hand-object interaction |
| 2026 | [Universal Manipulation Exoskeleton: Learning Compliant Whole](https://arxiv.org/abs/2606.14218) | humanoid-relevant mobile manipulation | ✅ | 🌐 Project Page | Portable upper-limb exoskeleton records arm configurations and joint torque feed |
| 2026 | [DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation wi](https://arxiv.org/abs/2606.23431) | bimanual dexterous hands / humanoid-relevant manipulation | ✅ | ❌ No Code | Adds tactile-driven force-compliant optimization on top of bimanual teleoperatio |
| 2026 | [HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid](https://arxiv.org/abs/2606.27239) | humanoid | ✅ | ❌ No Code | Collects robot-free VR/UMI-style demonstrations and retargets sparse human keypo |
| 2026 | [X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Reta](https://arxiv.org/abs/2606.07934) | humanoid / cross-morphology robots | ✅ | ❌ No Code | MPC-based retargeting enables cross-morphology whole-body teleoperation without  |
| 2026 | [CLOT - Closed-Loop Global Motion Tracking for Whole-Body Hum](https://arxiv.org/abs/2602.15060) | — | — | ❌ No Code | Closed-loop global motion tracking for whole-body teleoperation. |
| 2025 | [ACE-F: A Cross Embodiment Foldable System with Force Feedbac](https://arxiv.org/abs/2511.20887) | multiple | ✅ | ⭐ Code | Foldable cross-embodiment exoskeleton adds force feedback to ACE-style teleop fo |
| 2025 | [AirExo-2: Scaling up Generalizable Robotic Imitation Learnin](https://arxiv.org/abs/2503.03081) | dual-arm robots | ✅ | ⭐ Code | Scaled AirExo with adapters that turn in-the-wild data into pseudo-robot demos f |
| 2025 | [CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Lon](https://arxiv.org/abs/2506.08931) | Unitree H1 | ✅ | ⭐ Code | MoE whole-body policy + LiDAR odometry closed-loop teleop achieving 12 cm drift  |
| 2025 | [DEXOP: A Device for Robotic Transfer of Dexterous Human Mani](https://arxiv.org/abs/2509.04441) | dexterous hands | ✅ | ⭐ Code | Passive hand exoskeleton coined "perioperation" — connects human fingers to robo |
| 2025 | [DexUMI: Using Human Hand as the Universal Manipulation Inter](https://arxiv.org/abs/2505.21864) | 2 dexterous hands | ✅ | ⭐ Code | Wearable hand exoskeleton + visual in-painting that lets human hand directly ser |
| 2025 | [H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipula](https://arxiv.org/abs/2507.23523) | bimanual / humanoid | ✅ | ⭐ Code | 2B diffusion transformer pretrained on 338K EgoDex human trajectories then fine- |
| 2025 | [CHILD: Controller for Humanoid Imitation and Live Demonstrat](https://arxiv.org/abs/2508.00162) | humanoid | ✅ | 🌐 Project Page | Compact baby-carrier-form teleop rig giving operator joint-level control of all  |
| 2025 | [SPARK - A Toolbox for Safe Humanoid Autonomy and Teleoperati](https://arxiv.org/abs/2502.03132) | — | — | 🌐 Project Page | Safety toolbox for humanoid autonomy and teleoperation. |

## Datasets and Benchmarks

_66 entries._

- 🌐 **[ComFree-Sim - A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and Control](https://arxiv.org/abs/2603.12185)** `arXiv 2026.03` `Dataset`
  GPU-parallel analytical contact physics engine.
  Links: [Project](https://irislab.tech/comfree-sim/) · [Paper](https://arxiv.org/abs/2603.12185)

- 🌐 🧍 🧱 **[HumanoidArena: Benchmarking Egocentric Hierarchical Whole-Body Learning](https://arxiv.org/abs/2606.17833)** `arXiv 2026.06` `humanoid` `Dataset`
  Taowen Wang et al..
  Simulation-first benchmark evaluating whether high-level egocentric policies produce intermediate whole-body actions that trackers can execute.
  Links: [Project](https://humanoidarena.github.io) · [Paper](https://arxiv.org/abs/2606.17833)

- 🌐 🧍 🧱 **[Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory](https://arxiv.org/abs/2606.31037)** `arXiv 2026.06` `humanoid dexterous hands` `Dataset`
  Yuhan Wu et al..
  Reconstructs organic-chemistry workstations and defines precision-critical humanoid manipulation tasks with instrument readouts and quantitative tolerances.
  Links: [Project](https://labimus.github.io/) · [Paper](https://arxiv.org/abs/2606.31037)

- ⏳ 🤖 🧍 **[EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal](https://arxiv.org/abs/2607.13472)** `arXiv 2026.07` `Unitree G1` `Dataset`
  Alex Brandes et al..
  Captures 55 scene-aligned egocentric human-terrain sequences and uses them to train perceptive locomotion policies deployed on a Unitree G1.
  Links: [Project](https://egohtr.github.io) · [Paper](https://arxiv.org/abs/2607.13472)

- ⏳ 🤖 🧍 **[Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI](https://arxiv.org/abs/2606.22971)** `arXiv 2026.06` `humanoid` `Dataset`
  Xianda Guo et al..
  Full-view panoramic stereo occupancy dataset and model for humanoid perception, built around real sensor specs, simulated annotation, and real-world evaluation.
  Links: [Project](https://d-robotics-ai-lab.github.io/humanoid-omniocc) · [Paper](https://arxiv.org/abs/2606.22971)

- ⏳ 🤖 🧍 **[RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation](https://arxiv.org/abs/2606.31836)** `arXiv 2026.06` `Unitree G1` `Dataset`
  Xinyi Wang et al..
  Collects 6k Unitree G1 dexterous-manipulation trajectories across 19 tasks with multi-view RGB-D, tactile feedback, and semantic annotations.
  Links: [Paper](https://arxiv.org/abs/2606.31836)

- ❌ **[EmbodMocap - In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents](https://arxiv.org/abs/2602.23205)** `arXiv 2026.02` `Dataset`
  In-the-wild 4D human-scene reconstruction for embodied agents.
  Links: [Paper](https://arxiv.org/abs/2602.23205)

- ❌ **[RoboCasa365 - A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://openreview.net/forum?id=tQJYKwc3n4)** `ICLR 2026` `Dataset`
  Large-scale simulation framework for generalist robot benchmarks.
  Links: [Paper](https://openreview.net/forum?id=tQJYKwc3n4)

- ❌ **[Towards Motion Turing Test - Evaluating Human-Likeness in Humanoid Robots](https://arxiv.org/abs/2603.06181)** `arXiv 2026.03` `Dataset`
  Motion-Turing-test evaluation of humanoid human-likeness.
  Links: [Paper](https://arxiv.org/abs/2603.06181)

- ⭐ 🤖 🧍 **[MuJoCo Playground](https://arxiv.org/abs/2502.08844)** `arXiv preprint` `Berkeley Humanoid, Unitree H1/G1, Booster T1, Spot, Go1, Barkour` `Benchmark`
  Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, et al. (Google DeepMind).
  MJX/JAX-based open RL framework with zero-shot sim2real on 6+ robot platforms.
  Links: [Project](https://playground.mujoco.org/) · [Code](https://github.com/google-deepmind/mujoco_playground) · [Paper](https://arxiv.org/abs/2502.08844)

- ⭐ **[InterAct - Large-Scale Versatile 3D HOI Generation](https://arxiv.org/abs/2509.09555)** `CVPR 2025` `Dataset`
  Wenyu Zhang, et al..
  Unified large-scale HOI dataset and benchmark advancing versatile interaction generation.
  Links: [Project](https://sirui-xu.github.io/InterAct/) · [Code](https://github.com/wzyabcas/InterAct) · [Paper](https://arxiv.org/abs/2509.09555) · [Dataset](InterAct (21.81h consolidated, expanded to 30.70h))

- ⭐ **[Motion-X++ - Large-Scale Multimodal 3D Whole-body Human Motion Dataset](https://arxiv.org/abs/2501.05098)** `arXiv preprint` `Dataset`
  Yuhong Zhang, Jing Lin, Ailing Zeng, et al..
  19.5M whole-body pose annotations across 120.5K sequences + audio + per-frame text.
  Links: [Project](https://motion-x-dataset.github.io/) · [Code](https://github.com/IDEA-Research/Motion-X) · [Paper](https://arxiv.org/abs/2501.05098)

- ⭐ **[MuJoCo Playground](https://playground.mujoco.org/)** `2025.01` `Dataset`
  MuJoCo Playground for simulated robotics tasks.
  Links: [Project](https://playground.mujoco.org/) · [Code](https://github.com/google-deepmind/mujoco_playground) · [Paper](https://playground.mujoco.org/)

- 📦 **[PA-HOI - Physics-Aware Human-Object Interaction Dataset](https://arxiv.org/abs/2508.06205)** `arXiv preprint` `Dataset`
  PA-HOI Authors.
  HOI dataset captured/annotated with explicit physics-aware contact and force labels.
  Links: [Paper](https://arxiv.org/abs/2508.06205) · [Dataset](PA-HOI)

- 🌐 **[ActiveUMI - Robotic Manipulation with Active Perception from Robot-Free Human Demonstrations](https://activeumi.github.io/)** `arXiv 2025.10` `Dataset`
  Active-perception robot-free demonstrations for manipulation.
  Links: [Project](https://activeumi.github.io/) · [Paper](https://activeumi.github.io/)

- 🌐 **[DexUMI - Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation](https://dex-umi.github.io/)** `arXiv 2025.05` `Dataset`
  Human hand as universal manipulation interface.
  Links: [Project](https://dex-umi.github.io/) · [Paper](https://dex-umi.github.io/)

- 🌐 **[Humanoid Everyday - A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation](https://arxiv.org/abs/2510.08807)** `arXiv 2025.10` `Dataset`
  Comprehensive open-world humanoid manipulation dataset.
  Links: [Project](https://humanoideveryday.github.io/) · [Paper](https://arxiv.org/abs/2510.08807)

- 🌐 **[HumanoidGen - Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://arxiv.org/abs/2507.00833)** `arXiv 2025.07` `Dataset`
  LLM-driven data generation for bimanual dexterous manipulation.
  Links: [Project](https://openhumanoidgen.github.io/) · [Paper](https://arxiv.org/abs/2507.00833)

- 🌐 **[TeleOpBench - A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation](https://arxiv.org/abs/2505.12748)** `arXiv 2025.05` `Dataset`
  Simulator-centric benchmark for dual-arm dexterous teleoperation.
  Links: [Project](https://gorgeous2002.github.io/TeleOpBench/) · [Paper](https://arxiv.org/abs/2505.12748)

- ❌ **[Benchmarking Humanoid Imitation Learning with Motion Difficulty](https://arxiv.org/abs/2512.07248)** `arXiv 2025.12` `Dataset`
  Benchmark for humanoid imitation across motion difficulty.
  Links: [Paper](https://arxiv.org/abs/2512.07248)

- ❌ **[DualTHOR - A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning](https://arxiv.org/abs/2506.16012)** `arXiv 2025.06` `Dataset`
  Dual-arm humanoid simulation for contingency-aware planning.
  Links: [Paper](https://arxiv.org/abs/2506.16012)

- ❌ **[EgoDex - Learning Dexterous Manipulation from Large-Scale Egocentric Video](https://arxiv.org/abs/2505.11709)** `arXiv 2025.05` `Dataset`
  Large-scale egocentric video dataset for dexterous manipulation.
  Links: [Paper](https://arxiv.org/abs/2505.11709)

- ❌ **[PHUMA - Physically-Grounded Humanoid Locomotion Dataset](https://arxiv.org/abs/2510.26236)** `arXiv 2025.10` `Dataset`
  Physically-grounded humanoid locomotion dataset.
  Links: [Paper](https://arxiv.org/abs/2510.26236)

- ⭐ 🤖 🧍 **[Humanoid-Gym - RL Framework for Zero-Shot Sim2Real](https://arxiv.org/abs/2404.05695)** `arXiv / IROS-W` `RobotEra XBot-S/L (also Unitree H1, G1 forks)` `Benchmark`
  Xinyang Gu, Yen-Jen Wang, Jianyu Chen.
  Isaac Gym RL framework with sim-to-sim (MuJoCo) and zero-shot real deployment.
  Links: [Project](https://sites.google.com/view/humanoid-gym/) · [Code](https://github.com/roboterax/humanoid-gym) · [Paper](https://arxiv.org/abs/2404.05695)

- ⭐ **[Genesis - A Generative and Universal Physics Engine for Robotics and Beyond](https://genesis-embodied-ai.github.io/)** `arXiv 2024.12` `Dataset`
  Generative universal physics engine for robotics.
  Links: [Project](https://genesis-embodied-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/Genesis) · [Paper](https://genesis-embodied-ai.github.io/)

- ⭐ 🧱 **[Genesis - Universal Robotics Simulation Platform](https://genesis-embodied-ai.github.io/)** `open release` `Benchmark`
  Genesis Authors (Open collaboration).
  Universal multi-physics simulator unifying rigid, soft, fluid, generative scenes.
  Links: [Project](https://genesis-embodied-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/Genesis)

- ⭐ **[GRUtopia - Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943)** `arXiv 2024.07` `Dataset`
  City-scale dream world for general robots.
  Links: [Project](https://github.com/OpenRobotLab/GRUtopia) · [Code](https://github.com/OpenRobotLab/GRUtopia) · [Paper](https://arxiv.org/abs/2407.10943)

- ⭐ 🧱 **[Habitat 3.0 - Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724)** `ICLR 2024` `Benchmark`
  Xavi Puig, Eric Undersander, Andrew Szot, et al..
  Simulator with humanoid avatars + robots for social navigation/rearrangement.
  Links: [Project](https://aihabitat.org/) · [Code](https://github.com/facebookresearch/habitat-sim) · [Paper](https://arxiv.org/abs/2310.13724)

- ⭐ **[HIMO - Full-Body Human Interacting with Multiple Objects](https://arxiv.org/abs/2407.12371)** `ECCV 2024` `Dataset`
  Xintao Lv, Liang Xu, Yichao Yan, et al..
  3.3K HOI sequences, 4.08M frames, 53 objects, 34 subjects with detailed text.
  Links: [Project](https://lvxintao.github.io/himo/) · [Code](https://github.com/LvXinTao/HIMO_dataset) · [Paper](https://arxiv.org/abs/2407.12371) · [Dataset](https://lvxintao.github.io/himo/)

- ⭐ 🧱 **[Isaac Lab (and Isaac Sim)](https://isaac-sim.github.io/IsaacLab/)** `NVIDIA technical release` `Benchmark`
  NVIDIA Robotics.
  Successor to Isaac Gym; PhysX-GPU framework with humanoid/manip task suites.
  Links: [Project](https://isaac-sim.github.io/IsaacLab/) · [Code](https://github.com/isaac-sim/IsaacLab)

- ⭐ 🧱 **[ManiSkill3 - GPU Parallelized Robotics Simulation](https://arxiv.org/abs/2410.00425)** `arXiv preprint` `Benchmark`
  Stone Tao, Fanbo Xiang, Arth Shukla, et al..
  Open-source GPU-parallel simulator (SAPIEN) hitting 30K+ FPS across 12 task domains.
  Links: [Project](https://www.maniskill.ai/) · [Code](https://github.com/haosulab/ManiSkill) · [Paper](https://arxiv.org/abs/2410.00425)

- ⭐ **[OakInk2 - Bimanual Hand-Object Manipulation in Complex Tasks](https://arxiv.org/abs/2403.19417)** `CVPR 2024` `Dataset`
  Xinyu Zhan, Lixin Yang, Yifei Zhao, et al..
  Bimanual hand-object manipulation organized as Affordance/Primitive/Complex hierarchy.
  Links: [Project](https://oakink.net/v2/) · [Code](https://github.com/oakink/OakInk2) · [Paper](https://arxiv.org/abs/2403.19417) · [Dataset](https://oakink.net/v2/)

- ⭐ **[ParaHome - Parameterizing Everyday Home Activities](https://arxiv.org/abs/2401.10232)** `arXiv preprint` `Dataset`
  Jeonghwan Kim, Jisoo Kim, Jeonghyeon Na, Hanbyul Joo.
  38 subjects, 22 objects, 486 minutes of body+hand+object dynamics in studio apartment.
  Links: [Project](https://jlogkim.github.io/parahome/) · [Code](https://github.com/snuvclab/ParaHome) · [Paper](https://arxiv.org/abs/2401.10232) · [Dataset](ParaHome)

- ⭐ 🧱 **[RoboCasa - Large-Scale Simulation of Everyday Tasks](https://arxiv.org/abs/2406.02523)** `RSS 2024` `Benchmark`
  Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, et al..
  100 kitchen tasks (25 atomic + 75 composite) in generative diverse scenes.
  Links: [Project](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa) · [Paper](https://arxiv.org/abs/2406.02523)

- ⭐ **[TRUMANS - Scaling Up Dynamic Human-Scene Interaction Modeling](https://arxiv.org/abs/2403.08629)** `CVPR 2024` `Dataset`
  Nan Jiang, Zhiyuan Zhang, Hongjie Li, et al..
  15+ hours of mocap human-scene interaction across 100 indoor scenes with part-level dynamics.
  Links: [Project](https://jnnan.github.io/trumans/) · [Code](https://github.com/jnnan/trumans_utils) · [Paper](https://arxiv.org/abs/2403.08629) · [Dataset](https://jnnan.github.io/trumans/)

- 📦 **[Ego-Exo4D - First and Third-Person Skilled Activity](https://arxiv.org/abs/2311.18259)** `CVPR 2024` `Dataset`
  Kristen Grauman, Andrew Westbury, Lorenzo Torresani, et al..
  1,286 hours of synchronized ego+exo video with audio, gaze, IMU, point clouds.
  Links: [Project](https://ego-exo4d-data.org/) · [Paper](https://arxiv.org/abs/2311.18259) · [Dataset](https://ego-exo4d-data.org/)

- 📦 **[HOI-M3 - Multi-Human Multi-Object Interaction in Context](https://arxiv.org/abs/2404.00299)** `CVPR 2024` `Dataset`
  Juze Zhang, Jingyan Zhang, Zining Song, et al..
  199 sequences, 181M frames of multiple humans + multiple objects via dense RGB and IMU.
  Links: [Project](https://juzezhang.github.io/HOIM3_ProjectPage/) · [Paper](https://arxiv.org/abs/2404.00299) · [Dataset](https://juzezhang.github.io/HOIM3_ProjectPage/)

- 🌐 **[ARMADA - Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition](https://arxiv.org/abs/2412.10631)** `arXiv 2024.12` `Dataset`
  AR-based robot-free data acquisition for manipulation.
  Links: [Project](https://nataliya.dev/armada) · [Paper](https://arxiv.org/abs/2412.10631)

- 🌐 **[DexHub and DART - Towards Internet-Scale Robot Data Collection](https://arxiv.org/abs/2411.02214)** `arXiv 2024.11` `Dataset`
  Internet-scale robot data collection platform.
  Links: [Project](https://dexhub.ai/project) · [Paper](https://arxiv.org/abs/2411.02214)

- 🌐 **[ManiSkill-HAB - A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks](https://arxiv.org/abs/2412.13211)** `arXiv 2024.12` `Dataset`
  Benchmark for low-level manipulation in home rearrangement.
  Links: [Project](https://arth-shukla.github.io/mshab/) · [Paper](https://arxiv.org/abs/2412.13211)

- ⭐ **[ARCTIC - Dexterous Bimanual Hand-Object Manipulation](https://arxiv.org/abs/2204.13662)** `CVPR 2023` `Dataset`
  Zicong Fan, Omid Taheri, Dimitrios Tzionas, et al..
  2.1M video frames of bimanual articulated-object manipulation with 3D meshes and contact.
  Links: [Project](https://arctic.is.tue.mpg.de/) · [Code](https://github.com/zc-alexfan/arctic) · [Paper](https://arxiv.org/abs/2204.13662) · [Dataset](https://arctic.is.tue.mpg.de/)

- ⭐ **[CIRCLE - Capture In Rich Contextual Environments](https://arxiv.org/abs/2303.17912)** `CVPR 2023` `Dataset`
  Joao Pedro Araujo, Jiaman Li, et al..
  10 hours of full-body reaching motion with rich VR scene geometry context.
  Links: [Project](https://stanford-tml.github.io/circle_dataset/) · [Code](https://github.com/Stanford-TML/circle_dataset) · [Paper](https://arxiv.org/abs/2303.17912) · [Dataset](https://stanford-tml.github.io/circle_dataset/)

- ⭐ 🧱 **[LIBERO - Lifelong Robot Learning Benchmark](https://arxiv.org/abs/2306.03310)** `NeurIPS 2023` `Benchmark`
  Bo Liu, Yifeng Zhu, Chongkai Gao, et al..
  Lifelong manipulation benchmark; de facto VLA evaluation suite.
  Links: [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) · [Paper](https://arxiv.org/abs/2306.03310)

- ⭐ 🧱 **[LocoMuJoCo - Imitation Learning Benchmark for Locomotion](https://arxiv.org/abs/2311.02496)** `NeurIPS 2023 Workshop` `Benchmark`
  Firas Al-Hafez, Guoping Zhao, Jan Peters, Davide Tateo.
  12 environments / 27 tasks for IL across humanoids and quadrupeds.
  Links: [Code](https://github.com/robfiras/loco-mujoco) · [Paper](https://arxiv.org/abs/2311.02496)

- ⭐ **[Motion-X - Large-scale 3D Expressive Whole-body Human Motion Dataset](https://arxiv.org/abs/2307.00818)** `NeurIPS 2023` `Dataset`
  Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, et al..
  15.6M whole-body 3D poses + 81K sequences with text + facial/hand annotations.
  Links: [Project](https://motion-x-dataset.github.io/) · [Code](https://github.com/IDEA-Research/Motion-X) · [Paper](https://arxiv.org/abs/2307.00818) · [Dataset](https://github.com/IDEA-Research/Motion-X)

- ⭐ **[OMOMO - Object Motion Guided Human Motion Synthesis](https://arxiv.org/abs/2309.16237)** `SIGGRAPH Asia 2023` `Dataset`
  Jiaman Li, Jiajun Wu, C. Karen Liu.
  ~10 hours of paired human-object MoCap with 15 large everyday objects.
  Links: [Project](https://lijiaman.github.io/projects/omomo/) · [Code](https://github.com/lijiaman/omomo_release) · [Paper](https://arxiv.org/abs/2309.16237) · [Dataset](https://github.com/lijiaman/omomo_release)

- ⭐ **[RoboHive - Unified Framework for Robot Learning](https://arxiv.org/abs/2310.06828)** `NeurIPS 2023 D&B` `Benchmark`
  Vikash Kumar, Rutav Shah, Gaoyue Zhou, et al..
  Unified MuJoCo-based environments + hardware drivers for robot learning research.
  Links: [Code](https://github.com/vikashplus/robohive) · [Paper](https://arxiv.org/abs/2310.06828)

- 📦 **[BridgeData V2 - Robot Learning at Scale](https://arxiv.org/abs/2308.12952)** `CoRL 2023` `Dataset`
  Homer Walke, Kevin Black, Tony Zhao, et al..
  60,096 trajectories / 13 skills / 24 environments on low-cost WidowX arm.
  Links: [Project](https://rail-berkeley.github.io/bridgedata/) · [Paper](https://arxiv.org/abs/2308.12952) · [Dataset](https://rail-berkeley.github.io/bridgedata/)

- 📦 **[MOYO - Yoga Poses with Pressure Mat](https://arxiv.org/abs/2303.18246)** `CVPR 2023` `Dataset`
  Sai Kumar Dwivedi, Cordelia Schmid, Hongwei Yi, Michael J. Black, Dimitrios Tzionas.
  Multi-view yoga mocap with floor pressure, ground-truth CoM and CoP.
  Links: [Project](https://ipman.is.tue.mpg.de/) · [Paper](https://arxiv.org/abs/2303.18246) · [Dataset](https://moyo.is.tue.mpg.de/)

- 📦 **[RH20T - One-Shot Robot Manipulation Skills Dataset](https://arxiv.org/abs/2307.00595)** `ICRA 2024` `Dataset`
  Hao-Shu Fang, Hongjie Fang, Zhenyu Tang, Jirong Liu, et al..
  110K+ contact-rich manipulation sequences (40+ TB) for one-shot skill learning.
  Links: [Project](https://rh20t.github.io/) · [Paper](https://arxiv.org/abs/2307.00595) · [Dataset](https://rh20t.github.io/)

- ⭐ **[BEHAVE - Tracking Human-Object Interactions](https://arxiv.org/abs/2204.06950)** `CVPR 2022` `Dataset`
  Bharat Lal Bhatnagar, Xianghui Xie, Ilya Petrov, Cristian Sminchisescu, Christian Theobalt, Gerard Pons-Moll.
  First full-body HOI dataset with RGBD multi-view + 3D SMPL + object fits + contact.
  Links: [Project](https://virtualhumans.mpi-inf.mpg.de/behave/) · [Code](https://github.com/xiexh20/behave-dataset) · [Paper](https://arxiv.org/abs/2204.06950) · [Dataset](https://virtualhumans.mpi-inf.mpg.de/behave/)

- ⭐ **[COUCH - Towards Controllable Human-Chair Interactions](https://arxiv.org/abs/2205.00541)** `ECCV 2022` `Dataset`
  Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Vladimir Guzov, Gerard Pons-Moll.
  Controllable human-chair sitting interactions with hand-contact priors.
  Links: [Project](https://virtualhumans.mpi-inf.mpg.de/couch/) · [Code](https://github.com/xiaohangzhan/couch) · [Paper](https://arxiv.org/abs/2205.00541) · [Dataset](https://virtualhumans.mpi-inf.mpg.de/couch/)

- ⭐ **[Ego4D - Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058)** `CVPR 2022` `Dataset`
  Kristen Grauman, Andrew Westbury, et al. (FAIR consortium).
  3,670 hours of egocentric video from 923 wearers worldwide.
  Links: [Project](https://ego4d-data.org/) · [Code](https://github.com/facebookresearch/Ego4d) · [Paper](https://arxiv.org/abs/2110.07058) · [Dataset](https://ego4d-data.org/)

- ⭐ **[HumanML3D - 3D Human Motion-Language Dataset](https://arxiv.org/abs/2207.01696)** `CVPR 2022` `Dataset`
  Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, et al..
  14,616 motions, 44,970 textual descriptions paired (resampled from AMASS+HumanAct12).
  Links: [Project](https://github.com/EricGuo5513/HumanML3D) · [Code](https://github.com/EricGuo5513/HumanML3D) · [Paper](https://arxiv.org/abs/2207.01696) · [Dataset](https://github.com/EricGuo5513/HumanML3D)

- ⭐ **[ALFWorld - Aligning Text and Embodied Environments](https://arxiv.org/abs/2010.03768)** `ICLR 2021` `Benchmark`
  Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Cote, et al..
  Pairs ALFRED (3D) with TextWorld for cross-modality language-conditioned planning.
  Links: [Code](https://github.com/alfworld/alfworld) · [Paper](https://arxiv.org/abs/2010.03768)

- ⭐ **[Brax - Differentiable Physics in JAX](https://arxiv.org/abs/2106.13281)** `NeurIPS 2021 D&B` `Benchmark`
  C. Daniel Freeman, Erik Frey, Anton Raichuk, et al..
  JAX-native differentiable rigid-body simulator with TPU/GPU parallelism.
  Links: [Code](https://github.com/google/brax) · [Paper](https://arxiv.org/abs/2106.13281)

- ⭐ **[Isaac Gym - High Performance GPU-Based Robot Learning](https://arxiv.org/abs/2108.10470)** `NeurIPS 2021 D&B` `Benchmark`
  Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, et al..
  Original GPU-parallelized PhysX simulator that enabled massive RL parallelism.
  Links: [Code](https://github.com/isaac-sim/IsaacGymEnvs) · [Paper](https://arxiv.org/abs/2108.10470)

- ⭐ **[RoboMimic - Imitation Learning Study and Benchmark](https://arxiv.org/abs/2108.03298)** `CoRL 2021` `Benchmark`
  Ajay Mandlekar, Danfei Xu, Josiah Wong, et al..
  Reference IL benchmark + study with multiple proficiency-level demos.
  Links: [Project](https://robomimic.github.io/) · [Code](https://github.com/ARISE-Initiative/robomimic) · [Paper](https://arxiv.org/abs/2108.03298)

- ⭐ **[SAMP - Stochastic Scene-Aware Motion Prediction](https://arxiv.org/abs/2108.08284)** `ICCV 2021` `Dataset`
  Mohamed Hassan, Duygu Ceylan, Ruben Villegas, Jun Saito, Jimei Yang, Yi Zhou, Michael J. Black.
  100 minutes of mocap covering walking, sitting, lying with scene context.
  Links: [Project](https://samp.is.tue.mpg.de/) · [Code](https://github.com/mohamedhassanmus/SAMP) · [Paper](https://arxiv.org/abs/2108.08284) · [Dataset](https://samp.is.tue.mpg.de/)

- 📦 **[GTA-Human - Playing for 3D Human Recovery](https://arxiv.org/abs/2110.07588)** `TPAMI` `Dataset`
  Zhongang Cai, Mingyuan Zhang, Jiawei Ren, et al..
  Large-scale synthetic 3D human dataset rendered in GTA-V game engine.
  Links: [Project](https://caizhongang.github.io/projects/GTA-Human/) · [Paper](https://arxiv.org/abs/2110.07588) · [Dataset](https://huggingface.co/datasets/caizhongang/GTA-Human)

- ⭐ **[GRAB - Whole-Body Human Grasping of Objects](https://arxiv.org/abs/2008.11200)** `ECCV 2020` `Dataset`
  Omid Taheri, Nima Ghorbani, Michael J. Black, Dimitrios Tzionas.
  Whole-body MoCap of dexterous grasping with SMPL-X bodies and 51 objects.
  Links: [Project](https://grab.is.tue.mpg.de/) · [Code](https://github.com/otaheri/GRAB) · [Paper](https://arxiv.org/abs/2008.11200) · [Dataset](https://grab.is.tue.mpg.de/)

- ⭐ **[LAFAN1 - Ubisoft La Forge Animation Dataset](https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1txNTAqAGya2sjQVWQUsKE/d317e852512cbc9fec6dafc8b61f4a4e/RobustMotionInbetweening.pdf)** `SIGGRAPH 2020` `Dataset`
  F. G. Harvey, M. Yurick, D. Nowrouzezahrai, C. Pal.
  5 subjects, 77 sequences, ~496K frames @ 30 fps in BVH format.
  Links: [Code](https://github.com/ubisoft/ubisoft-laforge-animation-dataset) · [Paper](https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1txNTAqAGya2sjQVWQUsKE/d317e852512cbc9fec6dafc8b61f4a4e/RobustMotionInbetweening.pdf) · [Dataset](https://github.com/ubisoft/ubisoft-laforge-animation-dataset)

- ⭐ 🧱 **[SAPIEN - Simulation Environment for Generic Articulated Tasks](https://arxiv.org/abs/2003.08515)** `CVPR 2020` `Benchmark`
  Fanbo Xiang, Yuzhe Qin, Kaichun Mo, et al..
  Articulated-object physical simulator powering ManiSkill series.
  Links: [Project](https://sapien.ucsd.edu/) · [Code](https://github.com/haosulab/SAPIEN) · [Paper](https://arxiv.org/abs/2003.08515)

- ⭐ **[AMASS - Archive of Motion Capture as Surface Shapes](https://arxiv.org/abs/1904.03278)** `ICCV 2019` `N/A (human SMPL)` `Dataset`
  Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard Pons-Moll, Michael J. Black.
  Unifies 15 mocap datasets (>40 hrs, 300+ subjects, 11k motions) into SMPL-H with MoSh++.
  Links: [Project](https://amass.is.tue.mpg.de/) · [Code](https://github.com/nghorbani/amass) · [Paper](https://arxiv.org/abs/1904.03278) · [Dataset](https://amass.is.tue.mpg.de/)

- 📦 **[KIT Motion-Language Dataset](https://arxiv.org/abs/1607.03827)** `Big Data Journal` `Dataset`
  Matthias Plappert, Christian Mandery, Tamim Asfour.
  3,911 motion sequences with 6,278 text descriptions on 21-joint skeleton.
  Links: [Paper](https://arxiv.org/abs/1607.03827) · [Dataset](https://motion-annotation.humanoids.kit.edu/dataset/)

- 📦 **[CMU Motion Capture Database](https://mocap.cs.cmu.edu/)** `CMU online dataset` `Dataset`
  Carnegie Mellon University Graphics Lab.
  Free CMU mocap database covering walking, running, jumping, acrobatics.
  Links: [Paper](https://mocap.cs.cmu.edu/) · [Dataset](https://mocap.cs.cmu.edu/)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [ComFree-Sim - A GPU-Parallelized Analytical Contact Physics ](https://arxiv.org/abs/2603.12185) | — | — | 🌐 Project Page | GPU-parallel analytical contact physics engine. |
| 2026 | [HumanoidArena: Benchmarking Egocentric Hierarchical Whole-Bo](https://arxiv.org/abs/2606.17833) | humanoid | — | 🌐 Project Page | Simulation-first benchmark evaluating whether high-level egocentric policies pro |
| 2026 | [Labimus: A Simulation and Benchmark for Humanoid Dexterous M](https://arxiv.org/abs/2606.31037) | humanoid dexterous hands | — | 🌐 Project Page | Reconstructs organic-chemistry workstations and defines precision-critical human |
| 2026 | [EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traver](https://arxiv.org/abs/2607.13472) | Unitree G1 | ✅ | ⏳ Code Coming Soon | Captures 55 scene-aligned egocentric human-terrain sequences and uses them to tr |
| 2026 | [Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset f](https://arxiv.org/abs/2606.22971) | humanoid | ✅ | ⏳ Code Coming Soon | Full-view panoramic stereo occupancy dataset and model for humanoid perception,  |
| 2026 | [RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Hu](https://arxiv.org/abs/2606.31836) | Unitree G1 | ✅ | ⏳ Code Coming Soon | Collects 6k Unitree G1 dexterous-manipulation trajectories across 19 tasks with  |
| 2026 | [EmbodMocap - In-the-Wild 4D Human-Scene Reconstruction for E](https://arxiv.org/abs/2602.23205) | — | — | ❌ No Code | In-the-wild 4D human-scene reconstruction for embodied agents. |
| 2026 | [RoboCasa365 - A Large-Scale Simulation Framework for Trainin](https://openreview.net/forum?id=tQJYKwc3n4) | — | — | ❌ No Code | Large-scale simulation framework for generalist robot benchmarks. |
| 2026 | [Towards Motion Turing Test - Evaluating Human-Likeness in Hu](https://arxiv.org/abs/2603.06181) | — | — | ❌ No Code | Motion-Turing-test evaluation of humanoid human-likeness. |
| 2025 | [MuJoCo Playground](https://arxiv.org/abs/2502.08844) | Berkeley Humanoid, Unitree H1/G1, Booster T1, Spot, Go1, Barkour | ✅ | ⭐ Code | MJX/JAX-based open RL framework with zero-shot sim2real on 6+ robot platforms. |
| 2025 | [InterAct - Large-Scale Versatile 3D HOI Generation](https://arxiv.org/abs/2509.09555) | — | — | ⭐ Code | Unified large-scale HOI dataset and benchmark advancing versatile interaction ge |
| 2025 | [Motion-X++ - Large-Scale Multimodal 3D Whole-body Human Moti](https://arxiv.org/abs/2501.05098) | — | — | ⭐ Code | 19.5M whole-body pose annotations across 120.5K sequences + audio + per-frame te |
| 2025 | [MuJoCo Playground](https://playground.mujoco.org/) | — | — | ⭐ Code | MuJoCo Playground for simulated robotics tasks. |
| 2025 | [PA-HOI - Physics-Aware Human-Object Interaction Dataset](https://arxiv.org/abs/2508.06205) | — | — | 📦 Dataset | HOI dataset captured/annotated with explicit physics-aware contact and force lab |
| 2025 | [ActiveUMI - Robotic Manipulation with Active Perception from](https://activeumi.github.io/) | — | — | 🌐 Project Page | Active-perception robot-free demonstrations for manipulation. |

## Evaluation Metrics and Contact Modeling

_10 entries._

- 🌐 **[GRIP - Robotic Incremental Potential Contact Simulation Dataset](https://arxiv.org/abs/2503.05020)** `arXiv preprint` `Contact-Model`
  Hongyu Wei, et al..
  100K grasps with IPC-based deformable+rigid contact simulation; UMI + LEAP hand.
  Links: [Project](https://bell0o.github.io/GRIP/) · [Paper](https://arxiv.org/abs/2503.05020)

- ❌ **[Hand-Object Contact Detection using Grasp Quality Metrics](https://arxiv.org/abs/2501.06987)** `arXiv preprint` `Evaluation-Metric`
  Anonymous (arXiv preprint).
  Uses grasp-quality (Q1, Ferrari-Canny) measures as contact-detection signals.
  Links: [Paper](https://arxiv.org/abs/2501.06987)

- ❌ **[Measuring Physical Plausibility via Physics Simulation](https://arxiv.org/abs/2502.04483)** `arXiv preprint` `Evaluation-Metric`
  Authors of the metric paper.
  Proposes CoM-distance and Pose Stability Duration as physics-based plausibility metrics.
  Links: [Paper](https://arxiv.org/abs/2502.04483)

- ❌ 🧍 🧱 **[PhysHMR - Physically Plausible Human Motion Reconstruction via Humanoid Control](https://arxiv.org/abs/2510.02566)** `arXiv preprint` `Evaluation-Metric`
  PhysHMR Authors.
  Learns vision-driven humanoid control policy yielding physically plausible motion reconstruction.
  Links: [Paper](https://arxiv.org/abs/2510.02566)

- ❌ **[PhySIC - Physically Plausible 3D HSI and Contact from a Single Image](https://arxiv.org/abs/2510.11649)** `arXiv preprint` `Evaluation-Metric`
  PhySIC Authors.
  Reconstructs metrically aligned human + scene with vertex-level contact maps.
  Links: [Paper](https://arxiv.org/abs/2510.11649)

- ⭐ **[ContactGen - Generative Contact Modeling for Grasp Generation](https://arxiv.org/abs/2310.03740)** `ICCV 2023` `Contact-Model`
  Shaowei Liu, Yang Zhou, Jimei Yang, Saurabh Gupta, Shenlong Wang.
  Object-centric (contact, part, direction) representation + conditional generative grasp model.
  Links: [Project](https://stevenlsw.github.io/contactgen/) · [Code](https://github.com/stevenlsw/contactgen) · [Paper](https://arxiv.org/abs/2310.03740)

- ⭐ **[COAP - Compositional Articulated Occupancy](https://arxiv.org/abs/2204.06184)** `CVPR 2022` `Contact-Model`
  Marko Mihajlovic, Shunsuke Saito, Aayush Bansal, Michael Zollhoefer, Siyu Tang.
  Neural implicit articulated body occupancy enabling fast self/scene collision queries.
  Links: [Project](https://neuralbodies.github.io/COAP/) · [Code](https://github.com/markomih/COAP) · [Paper](https://arxiv.org/abs/2204.06184)

- ⭐ **[ContactOpt - Optimizing Contact to Improve Grasps](https://openaccess.thecvf.com/content/CVPR2021/papers/Grady_ContactOpt_Optimizing_Contact_To_Improve_Grasps_CVPR_2021_paper.pdf)** `CVPR 2021` `Contact-Model`
  Patrick Grady, Chengcheng Tang, Christopher D. Twigg, Minh Vo, Samarth Brahmbhatt, Charles C. Kemp.
  Predicts desired contact then differentiably optimizes hand pose to achieve it.
  Links: [Code](https://github.com/facebookresearch/ContactOpt) · [Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Grady_ContactOpt_Optimizing_Contact_To_Improve_Grasps_CVPR_2021_paper.pdf)

- 📦 **[ContactPose - Dataset of Grasps with Object Contact and Hand Pose](https://arxiv.org/abs/2007.09545)** `ECCV 2020` `Contact-Model`
  Samarth Brahmbhatt, Chengcheng Tang, Christopher D. Twigg, Charles C. Kemp, James Hays.
  2,306 grasps of 25 objects with thermal-imaging-derived contact maps + RGB-D + hand pose.
  Links: [Project](https://contactpose.cc.gatech.edu/) · [Paper](https://arxiv.org/abs/2007.09545) · [Dataset](https://contactpose.cc.gatech.edu/)

- ❌ **[Penetration / Float / Skate Metrics (HMR Plausibility Suite)](https://ipman.is.tue.mpg.de/)** `Cumulative` `Evaluation-Metric`
  Multiple (formalized in IPMAN, GRAB, BEHAVE, OMOMO).
  Standard suite: ground penetration depth, unsupported floating distance, foot-skating percentage.
  Links: [Paper](https://ipman.is.tue.mpg.de/)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2025 | [GRIP - Robotic Incremental Potential Contact Simulation Data](https://arxiv.org/abs/2503.05020) | — | — | 🌐 Project Page | 100K grasps with IPC-based deformable+rigid contact simulation; UMI + LEAP hand. |
| 2025 | [Hand-Object Contact Detection using Grasp Quality Metrics](https://arxiv.org/abs/2501.06987) | — | — | ❌ No Code | Uses grasp-quality (Q1, Ferrari-Canny) measures as contact-detection signals. |
| 2025 | [Measuring Physical Plausibility via Physics Simulation](https://arxiv.org/abs/2502.04483) | — | — | ❌ No Code | Proposes CoM-distance and Pose Stability Duration as physics-based plausibility  |
| 2025 | [PhysHMR - Physically Plausible Human Motion Reconstruction v](https://arxiv.org/abs/2510.02566) | — | — | ❌ No Code | Learns vision-driven humanoid control policy yielding physically plausible motio |
| 2025 | [PhySIC - Physically Plausible 3D HSI and Contact from a Sing](https://arxiv.org/abs/2510.11649) | — | — | ❌ No Code | Reconstructs metrically aligned human + scene with vertex-level contact maps. |
| 2023 | [ContactGen - Generative Contact Modeling for Grasp Generatio](https://arxiv.org/abs/2310.03740) | — | — | ⭐ Code | Object-centric (contact, part, direction) representation + conditional generativ |
| 2022 | [COAP - Compositional Articulated Occupancy](https://arxiv.org/abs/2204.06184) | — | — | ⭐ Code | Neural implicit articulated body occupancy enabling fast self/scene collision qu |
| 2021 | [ContactOpt - Optimizing Contact to Improve Grasps](https://openaccess.thecvf.com/content/CVPR2021/papers/Grady_ContactOpt_Optimizing_Contact_To_Improve_Grasps_CVPR_2021_paper.pdf) | — | — | ⭐ Code | Predicts desired contact then differentiably optimizes hand pose to achieve it. |
| 2020 | [ContactPose - Dataset of Grasps with Object Contact and Hand](https://arxiv.org/abs/2007.09545) | — | — | 📦 Dataset | 2,306 grasps of 25 objects with thermal-imaging-derived contact maps + RGB-D + h |
| 2020 | [Penetration / Float / Skate Metrics (HMR Plausibility Suite)](https://ipman.is.tue.mpg.de/) | — | — | ❌ No Code | Standard suite: ground penetration depth, unsupported floating distance, foot-sk |

## Sim-to-Real and Deployment Systems

_25 entries._

- ❌ 🤖 🧍 **[Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning](https://arxiv.org/abs/2607.02205)** `arXiv 2026.07` `single-joint servo / 7-DoF arm / wheeled-legged robot / humanoid` `Sim2Real`
  Satoshi Yamamori et al..
  Shapes real actuator closed-loop dynamics to match idealized simulation reference dynamics, enabling zero-shot policies across arms, wheeled-legged robots, and humanoid walking.
  Links: [Paper](https://arxiv.org/abs/2607.02205)

- ❌ 🤖 🧍 **[Hiking in the Wild - Scalable Perceptive Parkour for Humanoids](https://arxiv.org/abs/2601.07718)** `arXiv preprint` `Sim2Real`
  Hiking Authors.
  Scalable perceptive parkour framework deployed in outdoor wild environments.
  Links: [Paper](https://arxiv.org/abs/2601.07718)

- ❌ **[MOSAIC - Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation](https://arxiv.org/abs/2602.08594)** `arXiv 2026.02` `SimToReal`
  Closes sim-to-real gap for generalist humanoid tracking via residual adaptation.
  Links: [Paper](https://arxiv.org/abs/2602.08594)

- ❌ **[RAPT - Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots](https://arxiv.org/abs/2602.01515)** `arXiv 2026.02` `SimToReal`
  OOD detection and failure diagnosis for sim-to-real humanoids.
  Links: [Paper](https://arxiv.org/abs/2602.01515)

- ❌ **[ZEST - Zero-shot Embodied Skill Transfer for Athletic Robot Control](https://arxiv.org/abs/2602.00401)** `arXiv 2026.02` `SimToReal`
  Zero-shot embodied skill transfer for athletic control.
  Links: [Paper](https://arxiv.org/abs/2602.00401)

- 🌐 🤖 **[Sampling-Based System ID with Active Exploration (SPI-Active)](https://arxiv.org/abs/2505.14266)** `arXiv preprint` `Sim2Real`
  Tairan He, et al..
  Active sampling-based system identification improves sim2real over plain DR.
  Links: [Project](https://lecar-lab.github.io/spi-active_/) · [Paper](https://arxiv.org/abs/2505.14266)

- 🌐 **[ASAP - Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://agile.human2humanoid.com/)** `arXiv 2025.02` `SimToReal`
  Aligns simulation and real-world physics for agile whole-body skills.
  Links: [Project](https://agile.human2humanoid.com/) · [Paper](https://agile.human2humanoid.com/)

- 🌐 **[Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids](https://toruowo.github.io/recipe/)** `arXiv 2025.02` `SimToReal`
  Vision-based dexterous manipulation sim-to-real recipe.
  Links: [Project](https://toruowo.github.io/recipe/) · [Paper](https://toruowo.github.io/recipe/)

- ❌ 🤖 🧍 **[Sim-to-Real RL for Vision-Based Dexterous Manipulation on Humanoids](https://arxiv.org/abs/2502.20396)** `arXiv preprint` `Sim2Real`
  Toru Lin, Kartik Sachdev, Linxi Fan, Jitendra Malik, Yuke Zhu.
  Sim2real recipe for grasp-and-reach, lift, bimanual handover on a real humanoid.
  Links: [Paper](https://arxiv.org/abs/2502.20396)

- ❌ 🤖 **[VR-Robo - Real-to-Sim-to-Real for Visual Navigation](https://arxiv.org/abs/2502.01536)** `arXiv preprint` `Sim2Real`
  VR-Robo Authors.
  Builds photoreal interactive digital twins for visual navigation/locomotion sim2real.
  Links: [Paper](https://arxiv.org/abs/2502.01536)

- ❌ **[Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation](https://arxiv.org/abs/2502.10894)** `arXiv 2025.02` `SimToReal`
  Closes sim-to-real gap for athletic loco-manipulation.
  Links: [Paper](https://arxiv.org/abs/2502.10894)

- ❌ **[GaussGym - An open-source real-to-sim framework for learning locomotion from pixels](https://arxiv.org/abs/2510.15352)** `arXiv 2025.10` `SimToReal`
  Real-to-sim framework for learning locomotion from pixels.
  Links: [Paper](https://arxiv.org/abs/2510.15352)

- ❌ 🧍 🧱 **[PolySim - Multi-Simulator Dynamics Randomization for Humanoid Sim2Real](https://arxiv.org/abs/2510.01708)** `arXiv preprint` `Sim2Real`
  PolySim Authors.
  Trains across multiple simulators to randomize dynamics and shrink sim-to-real gap.
  Links: [Paper](https://arxiv.org/abs/2510.01708)

- ❌ **[Robot Trains Robot - Automatic Real-World Policy Adaptation and Learning for Humanoids](https://arxiv.org/abs/2508.12252)** `arXiv 2025.08` `SimToReal`
  Automatic real-world policy adaptation for humanoids.
  Links: [Paper](https://arxiv.org/abs/2508.12252)

- ❌ **[Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection](https://arxiv.org/abs/2504.06585)** `arXiv 2025.04` `SimToReal`
  Sim-to-real via joint-torque-space perturbations.
  Links: [Paper](https://arxiv.org/abs/2504.06585)

- 🌐 🤖 🧍 **[Mobile-TeleVision - Predictive Motion Priors for Humanoid WBC](https://arxiv.org/abs/2412.07773)** `arXiv preprint` `Sim2Real`
  Mobile TeleVision Authors.
  Predictive motion priors used for humanoid WBC during teleoperation.
  Links: [Project](https://mobile-tv.github.io/) · [Paper](https://arxiv.org/abs/2412.07773)

- 🌐 🤖 🧍 **[Opt2Skill - Imitating Whole-Body Trajectories for Humanoid Loco-Manip](https://arxiv.org/abs/2409.20514)** `arXiv preprint` `Sim2Real`
  Wenli Xiao, et al..
  Pairs trajectory-optimization references with RL imitation for versatile humanoid loco-manip.
  Links: [Project](https://opt2skill.github.io/) · [Paper](https://arxiv.org/abs/2409.20514)

- ❌ 🤖 🧍 **[Denoising World Model Learning for Humanoid Locomotion](https://arxiv.org/abs/2408.14472)** `arXiv preprint` `Sim2Real`
  Xinyang Gu, et al..
  Denoising world-model RL pushes humanoid locomotion onto challenging terrains.
  Links: [Paper](https://arxiv.org/abs/2408.14472)

- ❌ **[Sim-to-Real Learning for Humanoid Box Loco-Manipulation](https://arxiv.org/abs/2310.03191)** `arXiv 2023.10` `SimToReal`
  Sim-to-real learning for humanoid box loco-manipulation.
  Links: [Paper](https://arxiv.org/abs/2310.03191)

- ❌ 🧱 **[Multi-AMP - Advanced Skills with Multiple Motion Priors](https://arxiv.org/abs/2203.14912)** `ICRA 2023` `Sim2Real`
  Eric Vollenweider, Marko Bjelonic, Victor Klemm, et al..
  Multiple motion priors in AMP for richer skill repertoire on legged robots.
  Links: [Paper](https://arxiv.org/abs/2203.14912)

- 🌐 🤖 **[RMA - Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)** `RSS 2021` `Sim2Real`
  Ashish Kumar, Zipeng Fu, Deepak Pathak, Jitendra Malik.
  Two-stage base-policy + adaptation module enabling online sim2real adaptation in <1s.
  Links: [Project](https://ashish-kmr.github.io/rma-legged-robots/) · [Paper](https://arxiv.org/abs/2107.04034)

- ❌ **[Robot Learning from Randomized Simulations - Survey](https://arxiv.org/abs/2111.00956)** `Frontiers in Robotics and AI` `Sim2Real`
  Fabio Muratore, Fabio Ramos, Greg Turk, Wenhao Yu, Michael Gienger, Jan Peters.
  Comprehensive survey of randomized-simulation methods for sim2real transfer.
  Links: [Paper](https://arxiv.org/abs/2111.00956)

- ⭐ 🧍 🧱 **[Crocoddyl - Multi-Contact Optimal Control Framework](https://arxiv.org/abs/1909.04947)** `ICRA 2020` `Sim2Real`
  Carlos Mastalli, Rohan Budhiraja, et al..
  Efficient analytical-derivative DDP solver for multi-contact humanoid optimal control.
  Links: [Code](https://github.com/loco-3d/crocoddyl) · [Paper](https://arxiv.org/abs/1909.04947)

- ❌ 🤖 **[Dynamics Randomization Revisited - Quadrupedal Locomotion Case Study](https://arxiv.org/abs/2011.02404)** `ICRA 2021` `Sim2Real`
  Ananye Agarwal, et al..
  Argues for selective, principled DR rather than blanket randomization.
  Links: [Paper](https://arxiv.org/abs/2011.02404)

- ❌ **[Learning Agile and Dynamic Motor Skills for Legged Robots](https://arxiv.org/abs/1901.08652)** `arXiv 2019.01` `SimToReal`
  Foundational sim-to-real for agile legged motor skills.
  Links: [Paper](https://arxiv.org/abs/1901.08652)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Lea](https://arxiv.org/abs/2607.02205) | single-joint servo / 7-DoF arm / wheeled-legged robot / humanoid | ✅ | ❌ No Code | Shapes real actuator closed-loop dynamics to match idealized simulation referenc |
| 2026 | [Hiking in the Wild - Scalable Perceptive Parkour for Humanoi](https://arxiv.org/abs/2601.07718) | — | ✅ | ❌ No Code | Scalable perceptive parkour framework deployed in outdoor wild environments. |
| 2026 | [MOSAIC - Bridging the Sim-to-Real Gap in Generalist Humanoid](https://arxiv.org/abs/2602.08594) | — | — | ❌ No Code | Closes sim-to-real gap for generalist humanoid tracking via residual adaptation. |
| 2026 | [RAPT - Model-Predictive Out-of-Distribution Detection and Fa](https://arxiv.org/abs/2602.01515) | — | — | ❌ No Code | OOD detection and failure diagnosis for sim-to-real humanoids. |
| 2026 | [ZEST - Zero-shot Embodied Skill Transfer for Athletic Robot ](https://arxiv.org/abs/2602.00401) | — | — | ❌ No Code | Zero-shot embodied skill transfer for athletic control. |
| 2025 | [Sampling-Based System ID with Active Exploration (SPI-Active](https://arxiv.org/abs/2505.14266) | — | ✅ | 🌐 Project Page | Active sampling-based system identification improves sim2real over plain DR. |
| 2025 | [ASAP - Aligning Simulation and Real-World Physics for Learni](https://agile.human2humanoid.com/) | — | — | 🌐 Project Page | Aligns simulation and real-world physics for agile whole-body skills. |
| 2025 | [Sim-to-Real Reinforcement Learning for Vision-Based Dexterou](https://toruowo.github.io/recipe/) | — | — | 🌐 Project Page | Vision-based dexterous manipulation sim-to-real recipe. |
| 2025 | [Sim-to-Real RL for Vision-Based Dexterous Manipulation on Hu](https://arxiv.org/abs/2502.20396) | — | ✅ | ❌ No Code | Sim2real recipe for grasp-and-reach, lift, bimanual handover on a real humanoid. |
| 2025 | [VR-Robo - Real-to-Sim-to-Real for Visual Navigation](https://arxiv.org/abs/2502.01536) | — | ✅ | ❌ No Code | Builds photoreal interactive digital twins for visual navigation/locomotion sim2 |
| 2025 | [Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation](https://arxiv.org/abs/2502.10894) | — | — | ❌ No Code | Closes sim-to-real gap for athletic loco-manipulation. |
| 2025 | [GaussGym - An open-source real-to-sim framework for learning](https://arxiv.org/abs/2510.15352) | — | — | ❌ No Code | Real-to-sim framework for learning locomotion from pixels. |
| 2025 | [PolySim - Multi-Simulator Dynamics Randomization for Humanoi](https://arxiv.org/abs/2510.01708) | — | — | ❌ No Code | Trains across multiple simulators to randomize dynamics and shrink sim-to-real g |
| 2025 | [Robot Trains Robot - Automatic Real-World Policy Adaptation ](https://arxiv.org/abs/2508.12252) | — | — | ❌ No Code | Automatic real-world policy adaptation for humanoids. |
| 2025 | [Sim-to-Real of Humanoid Locomotion Policies via Joint Torque](https://arxiv.org/abs/2504.06585) | — | — | ❌ No Code | Sim-to-real via joint-torque-space perturbations. |

## Related Character Animation and Physics-Based Motion Generation

_29 entries._

- ⭐ 🧍 🧱 **[WaveSync: Constrained Wavefront Optimization for Synchronized Co-Speech Gestures in Humanoid Robots](https://arxiv.org/abs/2606.16600)** `arXiv 2026.06` `COMAN humanoid` `Physics-Anim`
  Thang Tran Viet et al..
  Converts speech emphasis into hardware-safe humanoid gesture trajectories using constrained wavefront optimization and robot models.
  Links: [Project](https://github.com/pairs-lab/WaveSync) · [Code](https://github.com/pairs-lab/WaveSync) · [Paper](https://arxiv.org/abs/2606.16600)

- 🌐 🧍 🧱 **[ComplexMimic: Human-Scene Interaction Imitation in Complex 3D Environments](https://arxiv.org/abs/2607.02034)** `arXiv 2026.07` `simulated humanoid / physics character` `Physics-Anim`
  Lu Pan et al..
  Uses dual imitation and interaction experts plus difficulty-aware distillation to imitate human-scene interactions in complex 3D environments.
  Links: [Project](https://github.com/LuPan23/ComplexMimic) · [Paper](https://arxiv.org/abs/2607.02034)

- 🌐 **[Kimodo - Scaling Controllable Human Motion Generation](https://research.nvidia.com/labs/sil/projects/kimodo/)** `NVIDIA / website 2026.03` `Animation`
  Scaling controllable human motion generation.
  Links: [Project](https://research.nvidia.com/labs/sil/projects/kimodo/) · [Paper](https://research.nvidia.com/labs/sil/projects/kimodo/)

- ❌ 🤖 🧍 **[BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with Behavioral Foundation Models](https://arxiv.org/abs/2606.25056)** `arXiv 2026.06` `humanoid / physics character` `Physics-Anim`
  Thomas Rupf et al..
  Optimizes temporally correlated latent sequences so behavioral foundation models can track dense or sparse motion sequences and deploy on a real humanoid.
  Links: [Paper](https://arxiv.org/abs/2606.25056)

- ❌ 🧍 🧱 **[GPC: Large-Scale Generative Pretraining for Transferable Motor Control](https://arxiv.org/abs/2606.29148)** `arXiv 2026.06` `physics character / humanoid-like controller` `Physics-Anim`
  Yi Shi et al..
  Learns a tokenized motor-control vocabulary and autoregressive generative controller for reusable physics-based character control across motion clips and downstream tasks.
  Links: [Paper](https://arxiv.org/abs/2606.29148)

- ❌ 🧍 🧱 **[In-Context Model Predictive Generation: Open-Vocabulary Motion Synthesis from Language Models to Physics](https://arxiv.org/abs/2606.26981)** `arXiv 2026.06` `simulated humanoid / physics character` `Physics-Anim`
  Xiaomeng Fu et al..
  Uses an LLM planner and model-predictive physical feedback loop to generate open-vocabulary human motion that balances semantic fidelity and physical realism.
  Links: [Paper](https://arxiv.org/abs/2606.26981)

- ❌ **[Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control](https://arxiv.org/abs/2602.21599)** `arXiv 2026.02` `Animation`
  Iterative closed-loop motion synthesis for humanoid control.
  Links: [Paper](https://arxiv.org/abs/2602.21599)

- ⭐ 🧍 🧱 **[InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2502.20390)** `CVPR 2025 (Highlight)` `sim-only SMPL-X / Unitree G1` `Physics-Anim`
  Sirui Xu, Hung Yu Ling, Yu-Xiong Wang, Liang-Yan Gui.
  Per-subject teacher distillation + RL fine-tuning yields a universal HOI WBC policy spanning hours of MoCap.
  Links: [Project](https://sirui-xu.github.io/InterMimic/) · [Code](https://github.com/Sirui-Xu/InterMimic) · [Paper](https://arxiv.org/abs/2502.20390)

- ⭐ **[PARC - Physics-based Augmentation with Reinforcement Learning for Character Controllers](https://michaelx.io/parc/index.html)** `SIGGRAPH 2025` `Animation`
  Physics-based augmentation with RL for character controllers.
  Links: [Project](https://michaelx.io/parc/index.html) · [Code](https://github.com/mshoe/PARC) · [Paper](https://michaelx.io/parc/index.html)

- ⭐ 🧍 🧱 **[Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models (Meta Motivo / FB-CPR)](https://arxiv.org/abs/2504.11054)** `ICLR 2025` `sim-only SMPL humanoid` `Physics-Anim`
  Andrea Tirinzoni, Ahmed Touati, Jesse Farebrother, Mateusz Guzek, Anssi Kanervisto, Yingchen Xu, Alessandro Lazaric, Matteo Pirotta.
  Forward-Backward + Conditional Policy Regularization yields a single zero-shot prompted whole-body humanoid controller.
  Links: [Project](https://metamotivo.metademolab.com/) · [Code](https://github.com/facebookresearch/metamotivo) · [Paper](https://arxiv.org/abs/2504.11054)

- 🌐 🧍 🧱 **[ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators](https://arxiv.org/abs/2505.04961)** `SIGGRAPH 2025` `sim-only humanoid` `Physics-Anim`
  Ziyu Zhang, Sergey Bashkirov, Dun Yang, Michael Taylor, Xue Bin Peng.
  Differential discriminator that operates on state differences enables high-quality single-objective imitation.
  Links: [Project](https://add-imitation.github.io/) · [Paper](https://arxiv.org/abs/2505.04961)

- 🌐 **[PDC - Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning](https://arxiv.org/abs/2505.12278)** `arXiv 2025.05` `Animation`
  Emergent active perception and dexterity from visual RL.
  Links: [Project](https://www.zhengyiluo.com/PDC-Site/) · [Paper](https://arxiv.org/abs/2505.12278)

- ❌ 🧍 🧱 **[AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2505.23708)** `SIGGRAPH 2025` `sim-only humanoid` `Physics-Anim`
  Lucas Stadler, et al..
  Multi-objective RL adapts character behaviors across reward trade-offs at deployment time.
  Links: [Paper](https://arxiv.org/abs/2505.23708)

- ❌ **[Learning to Ball - Composing Policies for Long-Horizon Basketball Moves](https://arxiv.org/abs/2509.22442)** `arXiv 2025.09` `Animation`
  Composing policies for long-horizon basketball motions.
  Links: [Paper](https://arxiv.org/abs/2509.22442)

- ❌ **[MaskedManipulator - Versatile Whole-Body Control for Loco-Manipulation](https://arxiv.org/abs/2505.19086)** `arXiv 2025.05` `Animation`
  Versatile whole-body control with masked manipulator framework.
  Links: [Paper](https://arxiv.org/abs/2505.19086)

- ❌ **[PRIMAL - Physically Reactive and Interactive Motor Model for Avatar Learning](https://arxiv.org/abs/2503.17544)** `arXiv 2025.03` `Animation`
  Physically reactive interactive motor model for avatars.
  Links: [Paper](https://arxiv.org/abs/2503.17544)

- ⭐ 🧍 🧱 **[Omnigrasp: Grasping Diverse Objects with Simulated Humanoids](https://arxiv.org/abs/2407.11385)** `NeurIPS 2024` `sim-only SMPL-X humanoid with hands` `Physics-Anim`
  Zhengyi Luo, Jinkun Cao, Sammy Christen, Alexander Winkler, Kris Kitani, Weipeng Xu.
  Hierarchical RL on PULSE motion prior enables a humanoid to grasp 1200+ objects on diverse trajectories.
  Links: [Project](https://www.zhengyiluo.com/Omnigrasp-Site/) · [Code](https://github.com/ZhengyiLuo/Omnigrasp) · [Paper](https://arxiv.org/abs/2407.11385)

- 🌐 **[CLoSD - Closing the Loop between Simulation and Diffusion for multi-task character control](https://arxiv.org/abs/2410.03441)** `arXiv 2024.10` `Animation`
  Closes the loop between simulation and diffusion for character control.
  Links: [Project](https://guytevet.github.io/CLoSD-page/) · [Paper](https://arxiv.org/abs/2410.03441)

- 🌐 🧍 🧱 **[PDP: Physics-Based Character Animation via Diffusion Policy](https://arxiv.org/abs/2406.00960)** `SIGGRAPH Asia 2024` `sim-only humanoid` `Physics-Anim`
  Takara Truong, Michael Piseno, Zhaoming Xie, C. Karen Liu.
  Diffusion policy trained on noisy-state/clean-action pairs yields robust physics character control.
  Links: [Project](https://stanford-tml.github.io/PDP.github.io/) · [Paper](https://arxiv.org/abs/2406.00960)

- 🌐 🧱 **[PhysMotion: Physics-Grounded Dynamics From a Single Image](https://arxiv.org/abs/2411.17189)** `arXiv 2024` `differentiable MPM (continuum)` `Physics-Anim`
  Tianyi Xie, Yiwei Zhao, Ying Jiang, Chenfanfu Jiang.
  Single-image to physics-grounded video using differentiable MPM + diffusion refinement.
  Links: [Project](https://supertan0204.github.io/physmotion_website/) · [Paper](https://arxiv.org/abs/2411.17189)

- ⭐ 🧍 🧱 **[PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction](https://arxiv.org/abs/2312.04393)** `arXiv 2023` `sim-only humanoid (IsaacGym)` `Physics-Anim`
  Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian Zhang, Lei Zhang.
  Contact-graph reward enables physics-based imitation of full-body human-object interactions (basketball).
  Links: [Project](https://wyhuai.github.io/physhoi-page/) · [Code](https://github.com/wyhuai/PhysHOI) · [Paper](https://arxiv.org/abs/2312.04393) · [Dataset](BallPlay)

- 🌐 🧍 🧱 **[PhysDiff: Physics-Guided Human Motion Diffusion Model](https://arxiv.org/abs/2212.02500)** `ICCV 2023` `sim-only humanoid` `Physics-Anim`
  Ye Yuan, Jiaming Song, Umar Iqbal, Arash Vahdat, Jan Kautz.
  Physics-based projection module corrects motion-diffusion outputs for plausibility (>78% improvement).
  Links: [Project](https://nvlabs.github.io/PhysDiff/) · [Paper](https://arxiv.org/abs/2212.02500)

- 🌐 🧍 🧱 **[Synthesizing Physical Character-Scene Interactions (InterPhys 2023)](https://arxiv.org/abs/2302.00883)** `SIGGRAPH 2023` `sim-only humanoid (IsaacGym)` `Physics-Anim`
  Mohamed Hassan, Yunrong Guo, Tingwu Wang, Michiel van de Panne, Sanja Fidler, Xue Bin Peng.
  AMP-style adversarial imitation learns sit/lie/carry/move scene-interaction skills from unannotated MoCap.
  Links: [Project](https://xbpeng.github.io/projects/InterPhys/index.html) · [Paper](https://arxiv.org/abs/2302.00883)

- ❌ **[AdaptNet - Policy Adaptation for Physics-Based Character Control](https://dl.acm.org/doi/abs/10.1145/3618375)** `TOG 2023` `Animation`
  Policy adaptation for physics-based character control.
  Links: [Paper](https://dl.acm.org/doi/abs/10.1145/3618375)

- ⭐ 🧍 🧱 **[ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters](https://arxiv.org/abs/2210.06063)** `SIGGRAPH Asia 2022` `sim-only humanoid` `Physics-Anim`
  Heyuan Yao, Zhenhua Song, Baoquan Chen, Libin Liu.
  World-model + VAE learns skill-conditioned generative controllers for diverse character behaviors.
  Links: [Project](https://heyuanyao-pku.github.io/Control-VAE/) · [Code](https://github.com/heyuanYao-pku/Control-VAE) · [Paper](https://arxiv.org/abs/2210.06063)

- ⭐ 🧍 🧱 **[Physics-based Character Controllers Using Conditional VAEs (PhysicsVAE)](https://research.facebook.com/publications/physics-based-character-controllers-using-conditional-vaes/)** `SIGGRAPH 2022` `sim-only humanoid` `Physics-Anim`
  Jungdam Won, Deepak Gopinath, Jessica Hodgins.
  Conditional VAE physics-based character controller mapping kinematic guidance to PD targets.
  Links: [Code](https://github.com/facebookresearch/PhysicsVAE) · [Paper](https://research.facebook.com/publications/physics-based-character-controllers-using-conditional-vaes/)

- ⭐ 🧍 🧱 **[A Scalable Approach to Control Diverse Behaviors for Physically Simulated Characters (ScaDiver)](https://dl.acm.org/doi/10.1145/3386569.3392381)** `SIGGRAPH 2020` `sim-only humanoid (PyBullet)` `Physics-Anim`
  Jungdam Won, Deepak Gopinath, Jessica Hodgins.
  Scalable mixture-of-experts framework imitating large unstructured motion clips.
  Links: [Code](https://github.com/facebookresearch/ScaDiver) · [Paper](https://dl.acm.org/doi/10.1145/3386569.3392381)

- 🌐 🧍 🧱 **[PhysCap: Physically Plausible Monocular 3D Motion Capture in Real Time](https://arxiv.org/abs/2008.08880)** `SIGGRAPH Asia 2020` `physics-based human (rigid body)` `Physics-Anim`
  Soshi Shimada, Vladislav Golyanik, Weipeng Xu, Christian Theobalt.
  First real-time physics-plausible monocular 3D motion capture with contact and balance constraints.
  Links: [Project](https://vcai.mpi-inf.mpg.de/projects/PhysCap/) · [Paper](https://arxiv.org/abs/2008.08880)

- 🌐 🧍 🧱 **[DReCon: Data-Driven Responsive Control of Physics-Based Characters](https://dl.acm.org/doi/10.1145/3355089.3356536)** `SIGGRAPH Asia 2019` `sim-only humanoid` `Physics-Anim`
  Kevin Bergamin, Simon Clavet, Daniel Holden, James Forbes.
  Couples motion-matching kinematic generator with DRL physics tracker for responsive game characters.
  Links: [Project](https://www.ubisoft.com/en-us/studio/laforge/news/VjEIwquaIyEZZSw5RZI0V/drecon-datadriven-responsive-control-of-physicsbased-characters) · [Paper](https://dl.acm.org/doi/10.1145/3355089.3356536)


### Quick Reference Table

| Year | Paper | Robot/Data | Real Robot | Code | Key Idea |
|---|---|---|---|---|---|
| 2026 | [WaveSync: Constrained Wavefront Optimization for Synchronize](https://arxiv.org/abs/2606.16600) | COMAN humanoid | — | ⭐ Code | Converts speech emphasis into hardware-safe humanoid gesture trajectories using  |
| 2026 | [ComplexMimic: Human-Scene Interaction Imitation in Complex 3](https://arxiv.org/abs/2607.02034) | simulated humanoid / physics character | — | 🌐 Project Page | Uses dual imitation and interaction experts plus difficulty-aware distillation t |
| 2026 | [Kimodo - Scaling Controllable Human Motion Generation](https://research.nvidia.com/labs/sil/projects/kimodo/) | — | — | 🌐 Project Page | Scaling controllable human motion generation. |
| 2026 | [BFMTrack: Latent Sequence Optimization for Physics-Based Mot](https://arxiv.org/abs/2606.25056) | humanoid / physics character | ✅ | ❌ No Code | Optimizes temporally correlated latent sequences so behavioral foundation models |
| 2026 | [GPC: Large-Scale Generative Pretraining for Transferable Mot](https://arxiv.org/abs/2606.29148) | physics character / humanoid-like controller | — | ❌ No Code | Learns a tokenized motor-control vocabulary and autoregressive generative contro |
| 2026 | [In-Context Model Predictive Generation: Open-Vocabulary Moti](https://arxiv.org/abs/2606.26981) | simulated humanoid / physics character | — | ❌ No Code | Uses an LLM planner and model-predictive physical feedback loop to generate open |
| 2026 | [Iterative Closed-Loop Motion Synthesis for Scaling the Capab](https://arxiv.org/abs/2602.21599) | — | — | ❌ No Code | Iterative closed-loop motion synthesis for humanoid control. |
| 2025 | [InterMimic: Towards Universal Whole-Body Control for Physics](https://arxiv.org/abs/2502.20390) | sim-only SMPL-X / Unitree G1 | — | ⭐ Code | Per-subject teacher distillation + RL fine-tuning yields a universal HOI WBC pol |
| 2025 | [PARC - Physics-based Augmentation with Reinforcement Learnin](https://michaelx.io/parc/index.html) | — | — | ⭐ Code | Physics-based augmentation with RL for character controllers. |
| 2025 | [Zero-Shot Whole-Body Humanoid Control via Behavioral Foundat](https://arxiv.org/abs/2504.11054) | sim-only SMPL humanoid | — | ⭐ Code | Forward-Backward + Conditional Policy Regularization yields a single zero-shot p |
| 2025 | [ADD: Physics-Based Motion Imitation with Adversarial Differe](https://arxiv.org/abs/2505.04961) | sim-only humanoid | — | 🌐 Project Page | Differential discriminator that operates on state differences enables high-quali |
| 2025 | [PDC - Emergent Active Perception and Dexterity of Simulated ](https://arxiv.org/abs/2505.12278) | — | — | 🌐 Project Page | Emergent active perception and dexterity from visual RL. |
| 2025 | [AMOR: Adaptive Character Control through Multi-Objective Rei](https://arxiv.org/abs/2505.23708) | sim-only humanoid | — | ❌ No Code | Multi-objective RL adapts character behaviors across reward trade-offs at deploy |
| 2025 | [Learning to Ball - Composing Policies for Long-Horizon Baske](https://arxiv.org/abs/2509.22442) | — | — | ❌ No Code | Composing policies for long-horizon basketball motions. |
| 2025 | [MaskedManipulator - Versatile Whole-Body Control for Loco-Ma](https://arxiv.org/abs/2505.19086) | — | — | ❌ No Code | Versatile whole-body control with masked manipulator framework. |

---

## Acknowledgments
- Seed papers extracted from [YanjieZe/awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning).
- Code-status verification via direct GitHub HEAD checks and project-page inspection.

## Contributing
PRs welcome. Please include: paper title, authors, venue/year, arXiv link, project page, GitHub URL (if any), and a one-sentence summary. Mark code status only after personally checking the repo is non-empty.
