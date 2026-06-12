# Whole-Body Control & Loco-Manipulation (Humanoid) — 2022-2026

Curated list of ~50 papers on humanoid whole-body control (WBC) and loco-manipulation, with priority on 2024-2026.

Code-status legend: ⭐ Code | 🧩 Partial Code | 📦 Dataset | 🌐 Project Page | ⏳ Code Coming Soon | 🔁 Unofficial Code | ❌ No Code Found

---

- title: HumanPlus: Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  category: WBC
  task_tags: [shadowing, imitation, whole-body, manipulation]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Full-stack humanoid system that learns whole-body shadowing in sim from MoCap and trains autonomous skills via teleop demos.
  why_it_matters: Foundational open-source baseline for humanoid whole-body imitation; defines low-level shadowing + high-level skill (HIT) split widely reused since.

- title: H2O — Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  authors: Tairan He, Zhengyi Luo, Wenli Xiao, et al.
  year: 2024
  venue: IROS 2024
  arxiv_id: 2403.04436
  paper_url: https://arxiv.org/abs/2403.04436
  project_url: https://human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: WBC
  task_tags: [teleoperation, motion-tracking, whole-body]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Real-time whole-body teleop using a single RGB camera with sim-to-real RL motion tracking.
  why_it_matters: First scalable RGB-only human-to-humanoid teleop pipeline; backbone for OmniH2O and HOVER lineage.

- title: OmniH2O — Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
  authors: Tairan He, Zhengyi Luo, Xialin He, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.08858
  paper_url: https://arxiv.org/abs/2406.08858
  project_url: https://omni.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: WBC
  task_tags: [teleop, dexterous, whole-body, autonomy]
  robot_platform: Unitree H1 + dexterous hands
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Universal kinematic-pose interface enabling VR, language, and RGB-driven full-body humanoid control plus autonomy.
  why_it_matters: Establishes pose-based universal command space adopted by HOVER/HumanPlus successors.

- title: HOVER — Versatile Neural Whole-Body Controller for Humanoid Robots
  authors: Tairan He, Wenli Xiao, Toru Lin, et al.
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2410.21229
  paper_url: https://arxiv.org/abs/2410.21229
  project_url: https://hover-versatile-humanoid.github.io/
  code_url: https://github.com/NVlabs/HOVER
  category: WBC
  task_tags: [multi-mode, whole-body, motion-tracking]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Distills a motion-imitation teacher with command/proprio masking into a unified multi-mode whole-body controller.
  why_it_matters: Unifies joint, root, keypoint and SE(3) tracking modes in one policy; foundation of NVIDIA GR00T WBC stack.

- title: ExBody — Expressive Whole-Body Control for Humanoid Robots
  authors: Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: RSS 2024
  arxiv_id: 2402.16796
  paper_url: https://arxiv.org/abs/2402.16796
  project_url: https://expressive-humanoid.github.io/
  code_url: https://github.com/chengxuxin/expressive-humanoid
  category: WBC
  task_tags: [expressive, motion-tracking, dance]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Decouples upper-body imitation from lower-body locomotion to produce expressive yet stable real-world humanoid behavior.
  why_it_matters: Earliest open RL recipe for expressive whole-body humanoid control; widely used baseline.

- title: ExBody2 — Advanced Expressive Humanoid Whole-Body Control
  authors: Mazeyu Ji, Xuanbin Peng, Fangchen Liu, Jialong Li, Ge Yang, Xuxin Cheng, Xiaolong Wang
  year: 2024
  venue: arXiv 2024
  arxiv_id: 2412.13196
  paper_url: https://arxiv.org/abs/2412.13196
  project_url: https://exbody2.github.io/
  code_url: ❌
  category: WBC
  task_tags: [motion-tracking, expressive, teacher-student]
  robot_platform: Unitree H1, Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Decouples velocity from keypoint tracking and uses a privileged teacher to produce high-fidelity dynamic whole-body motions.
  why_it_matters: Dramatically improves dynamic motion fidelity (running, crouching, dancing) over ExBody on multiple platforms.

- title: ASAP — Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  authors: Tairan He, Jiawei Gao, Wenli Xiao, et al.
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.01143
  paper_url: https://arxiv.org/abs/2502.01143
  project_url: https://agile.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/ASAP
  category: WBC
  task_tags: [sim-to-real, agile, residual-dynamics]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Two-stage delta-action residual model that aligns sim and real physics for agile humanoid whole-body skills.
  why_it_matters: Sets sim-to-real SOTA for agile motions; influential residual-dynamics paradigm.

- title: HoST — Learning Humanoid Standing-up Control across Diverse Postures
  authors: Tao Huang, Junli Ren, Huayi Wang, et al.
  year: 2025
  venue: RSS 2025 (Best Systems Paper Finalist)
  arxiv_id: 2502.08378
  paper_url: https://arxiv.org/abs/2502.08378
  project_url: https://taohuang13.github.io/humanoid-standingup.github.io/
  code_url: https://github.com/InternRobotics/HoST
  category: WBC
  task_tags: [standing-up, recovery, contact-rich]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Multi-critic RL with motion regularization that learns posture-adaptive standing-up from arbitrary fallen postures.
  why_it_matters: Solves a critical robustness gap (getting up) overlooked by motion-tracking work.

- title: HOMIE — Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit
  authors: Qingwei Ben, et al. (InternRobotics / Shanghai AI Lab)
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2502.13013
  paper_url: https://arxiv.org/abs/2502.13013
  project_url: https://homietele.github.io/
  code_url: https://github.com/OpenRobotLab/OpenHomie
  category: Loco-Manip
  task_tags: [teleop, exoskeleton, loco-manipulation, height-tracking]
  robot_platform: Unitree H1, G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: $500 isomorphic exoskeleton cockpit + RL height-tracking lower-body policy enabling efficient humanoid loco-manipulation.
  why_it_matters: Open hardware+software combo that drastically lowers teleop barrier; data-flywheel pipeline.

- title: FALCON — Learning Force-Adaptive Humanoid Loco-Manipulation
  authors: Yuanhang Zhang, Yifu Yuan, Prajwal Gurunath, Tairan He, Shayegan Omidshafiei, Ali-akbar Agha-mohammadi, Marco Pavone, Yue Wang, Wenhao Yu, Guanya Shi
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2505.06776
  paper_url: https://arxiv.org/abs/2505.06776
  project_url: https://lecar-lab.github.io/falcon-humanoid/
  code_url: https://github.com/LeCAR-Lab/FALCON
  category: Loco-Manip
  task_tags: [force-adaptive, dual-agent, pushing, pulling]
  robot_platform: Unitree G1, Booster T1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Dual-agent RL with 3D force curriculum that decouples lower- and upper-body for force-robust humanoid loco-manipulation.
  why_it_matters: Best-in-class force-adaptive policy; cross-platform generalization (G1 + T1).

- title: AMO — Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control
  authors: Jialong Li, Xuxin Cheng, Tianshu Huang, Shiqi Yang, Ri-Zhao Qiu, Xiaolong Wang
  year: 2025
  venue: RSS 2025
  arxiv_id: 2505.03738
  paper_url: https://arxiv.org/abs/2505.03738
  project_url: https://amo-humanoid.github.io/
  code_url: https://github.com/OpenTeleVision/AMO
  category: WBC
  task_tags: [whole-body, trajectory-optimization, dexterous]
  robot_platform: Unitree H1-2
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Hybrid sim-to-real RL + trajectory optimization for adaptive whole-body humanoid control with extreme reach.
  why_it_matters: Pushes WBC workspace beyond previous limits; integrates classical TO with learned policies.

- title: TWIST — Teleoperated Whole-Body Imitation System
  authors: Yanjie Ze, Zixuan Chen, João Pedro Araújo, Zi-ang Cao, Xue Bin Peng, Jiajun Wu, C. Karen Liu
  year: 2025
  venue: CoRL 2025
  arxiv_id: 2505.02833
  paper_url: https://arxiv.org/abs/2505.02833
  project_url: https://yanjieze.com/TWIST/
  code_url: https://github.com/YanjieZe/TWIST
  category: WBC
  task_tags: [teleoperation, whole-body, imitation, RL+BC]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Single neural controller combining RL+BC with privileged future frames for full-spectrum teleop on G1.
  why_it_matters: Fully open WBC + manipulation system; unifies expressive, locomotion, and manipulation skills.

- title: ALMI — Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning
  authors: Hong Zhang, et al.
  year: 2025
  venue: NeurIPS 2025
  arxiv_id: 2504.14305
  paper_url: https://arxiv.org/abs/2504.14305
  project_url: https://almi-humanoid.github.io/
  code_url: https://github.com/TeleHuman/ALMI-Open
  category: WBC
  task_tags: [adversarial, upper-lower decoupling, dataset]
  robot_platform: Unitree H1-2
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Adversarial training between upper and lower body policies plus the ALMI-X language-trajectory dataset.
  why_it_matters: First language-trajectory aligned WBC dataset; introduces adversarial upper/lower decomposition.

- title: KungfuBot — Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills
  authors: Weiji Xie, Jinrui Han, Jiakun Zheng, et al.
  year: 2025
  venue: NeurIPS 2025
  arxiv_id: 2506.12851
  paper_url: https://arxiv.org/abs/2506.12851
  project_url: https://kungfu-bot.github.io/
  code_url: https://github.com/TeleHuman/PBHC
  category: WBC
  task_tags: [highly-dynamic, kungfu, dance, motion-tracking]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Physics-aware motion processing + adaptive curriculum for kungfu/dance-level dynamic humanoid skills.
  why_it_matters: Enables kicks/spins/tai-chi previously infeasible; bi-level optimization for adaptive tracking tolerance.

- title: SkillBlender — Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending
  authors: Yuxuan Kuang, Haoran Geng, Amine Elhafsi, Tan-Dzung Do, Pieter Abbeel, Jitendra Malik, Marco Pavone, Yue Wang
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2506.09366
  paper_url: https://arxiv.org/abs/2506.09366
  project_url: https://usc-gvl.github.io/SkillBlender/
  code_url: https://github.com/Humanoid-SkillBlender/SkillBlender
  category: Loco-Manip
  task_tags: [hierarchical, skill-blending, benchmark]
  robot_platform: Unitree H1, G1, Fourier GR1
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Hierarchical RL pretraining of primitive skills, dynamically blended for diverse loco-manip tasks plus SkillBench benchmark.
  why_it_matters: Cross-embodiment WBC benchmark + reusable primitive skill library.

- title: VisualMimic — Visual Humanoid Loco-Manipulation via Motion Tracking and Generation
  authors: Shaofeng Yin, Yanjie Ze, Hong-Xing Yu, C. Karen Liu, Jiajun Wu
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2509.20322
  paper_url: https://arxiv.org/abs/2509.20322
  project_url: https://visualmimic.github.io/
  code_url: https://github.com/visualmimic/VisualMimic
  category: Loco-Manip
  task_tags: [vision, hierarchical, kicking, dribbling, box-lifting]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Egocentric vision + low-level keypoint tracker + high-level keypoint generator for visual humanoid loco-manipulation.
  why_it_matters: Demonstrates outdoor box-lifting, dribbling, and kicking with zero-shot sim-to-real.

- title: VIRAL — Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
  authors: Anonymous (NVIDIA / collaborators)
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2511.15200
  paper_url: https://arxiv.org/abs/2511.15200
  project_url: https://viral-humanoid.github.io/
  code_url: ⏳
  category: Loco-Manip
  task_tags: [vision, sim-to-real, large-scale, RGB]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Teacher-student delta-action framework that distills RGB visuomotor policies from massive simulation tiles.
  why_it_matters: 54-cycle continuous loco-manipulation; near-teleoperator level pure-vision performance.

- title: WholeBodyVLA — Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control
  authors: OpenDriveLab team
  year: 2025
  venue: ICLR 2026
  arxiv_id: 2512.11047
  paper_url: https://arxiv.org/abs/2512.11047
  project_url: https://opendrivelab.com/WholeBodyVLA/
  code_url: https://github.com/OpenDriveLab/WholebodyVLA
  category: Loco-Manip
  task_tags: [VLA, latent-action, large-space, egocentric-video]
  robot_platform: AgiBot X2
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified latent VLA framework learning loco-manipulation from action-free egocentric videos for large-space mobility.
  why_it_matters: One of the first large-space humanoid loco-manip VLAs; +21-24% over prior baselines.

- title: OmniRetarget — Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
  authors: Lujie Yang, Xiaoyu Huang, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2509.26633
  paper_url: https://arxiv.org/abs/2509.26633
  project_url: https://omniretarget.github.io/
  code_url: https://github.com/OmniRetarget/OmniRetarget
  category: Loco-Manip
  task_tags: [retargeting, dataset, scene-interaction, parkour]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code & 📦 Dataset
  one_line: Interaction-mesh based retargeting that preserves contact relationships, enabling 30-second parkour and loco-manip on G1.
  why_it_matters: Dataset+method combo unlocking long-horizon humanoid skills with simple rewards; HF dataset release.

- title: BeyondMimic — From Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  authors: Takara Truong, Michael Liu, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2508.08241
  paper_url: https://arxiv.org/abs/2508.08241
  project_url: https://beyondmimic.github.io/
  code_url: https://github.com/HybridRobotics/whole_body_tracking
  category: WBC
  task_tags: [diffusion-policy, agile, cartwheel, sprinting]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Guided-diffusion policy that goes beyond motion mimicry to zero-shot task-conditioned humanoid control.
  why_it_matters: Single setup masters cartwheels, flip-kicks, sprints; SOTA agile motion quality.

- title: DreamControl — Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion
  authors: Wenshuai Zhao, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2509.14353
  paper_url: https://arxiv.org/abs/2509.14353
  project_url: https://dreamcontrol-humanoid.github.io/
  code_url: ⏳
  category: Loco-Manip
  task_tags: [diffusion-prior, scene-interaction, drawer, button]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Diffusion prior on human motion guides RL to discover whole-body scene-interaction skills (drawer, button, kick, jump, sit).
  why_it_matters: 11-task scene-interaction suite combining lower+upper body manipulation.

- title: ULC — A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation
  authors: Wandong Sun, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2507.06905
  paper_url: https://arxiv.org/abs/2507.06905
  project_url: https://ulc-humanoid.github.io/
  code_url: ❌
  category: Loco-Manip
  task_tags: [unified-controller, fine-grained, end-effector]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Single unified controller jointly tracking root velocity, height, base orientation, and 6D end-effector pose.
  why_it_matters: Replaces multi-policy decomposition with one fine-grained controller for loco-manipulation.

- title: R2S2 — Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space
  authors: Zhikai Zhang, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2505.10918
  paper_url: https://arxiv.org/abs/2505.10918
  project_url: https://zzk273.github.io/R2S2/
  code_url: ❌
  category: Loco-Manip
  task_tags: [skill-space, VLM-planner, reaching]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Real-world-ready skill space with VLM-driven modular planner sequencing locomotion and manipulation primitives.
  why_it_matters: Greatly expanded humanoid reaching workspace through learned skill space.

- title: GR00T N1 — An Open Foundation Model for Generalist Humanoid Robots
  authors: NVIDIA GEAR Lab
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2503.14734
  paper_url: https://arxiv.org/abs/2503.14734
  project_url: https://research.nvidia.com/labs/gear/gr00t-n1/
  code_url: https://github.com/NVIDIA/Isaac-GR00T
  category: Loco-Manip
  task_tags: [VLA, foundation-model, cross-embodiment]
  robot_platform: Fourier GR1, multiple humanoids
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Open VLA foundation model for humanoids trained on egocentric videos + sim/real trajectories + synthetic data.
  why_it_matters: First open humanoid foundation model; basis of N1.5/N1.6/N1.7 lineage.

- title: GR00T-WBC — NVIDIA GR00T Whole-Body Control
  authors: NVIDIA Robotics Research
  year: 2025
  venue: NVIDIA technical release
  arxiv_id: N/A
  paper_url: https://github.com/NVlabs/GR00T-WholeBodyControl
  project_url: https://github.com/NVlabs/GR00T-WholeBodyControl
  code_url: https://github.com/NVlabs/GR00T-WholeBodyControl
  category: WBC
  task_tags: [decoupled-WBC, VLA-integration, cross-embodiment]
  robot_platform: Multiple humanoids (Unitree, Fourier, etc.)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified open WBC platform combining decoupled controllers used by GR00T N1.5/N1.6 and GEAR-SONIC.
  why_it_matters: Production-ready open WBC stack consolidating recent humanoid control research.

- title: WoCoCo — Learning Whole-Body Humanoid Control with Sequential Contacts
  authors: Chong Zhang, Wenli Xiao, Tairan He, Guanya Shi
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.06005
  paper_url: https://arxiv.org/abs/2406.06005
  project_url: https://lecar-lab.github.io/wococo/
  code_url: ❌
  category: Loco-Manip
  task_tags: [contact-rich, parkour, box-manipulation, climbing]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Decomposes contact-rich tasks into sequential contact stages, unlocking jumping, box loco-manip, dancing, climbing.
  why_it_matters: General contact-stage framework spanning humanoid + 22-DoF dinosaur robot; pioneering loco-manip recipe.

- title: BiGym — A Demo-Driven Mobile Bi-Manual Manipulation Benchmark
  authors: Nikita Chernyadev, Nicholas Backshall, Xiao Ma, Yunfan Lu, Younggyo Seo, Stephen James
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.07788
  paper_url: https://arxiv.org/abs/2407.07788
  project_url: https://chernyadev.github.io/bigym/
  code_url: https://github.com/chernyadev/bigym
  category: Loco-Manip
  task_tags: [benchmark, bimanual, mobile-manip]
  robot_platform: Unitree H1 (sim)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: 40-task humanoid bimanual mobile manipulation benchmark with sparse rewards + 50 VR-collected demos per task.
  why_it_matters: Fills a key humanoid IL/RL benchmark gap covering whole-body & bimanual modes.

- title: HumanoidBench — Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation
  authors: Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, Pieter Abbeel
  year: 2024
  venue: RSS 2024
  arxiv_id: 2403.10506
  paper_url: https://arxiv.org/abs/2403.10506
  project_url: https://humanoid-bench.github.io/
  code_url: https://github.com/carlosferrazza/humanoid-bench
  category: WBC
  task_tags: [benchmark, simulation, whole-body, dexterous]
  robot_platform: Unitree H1, Digit (sim)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: First simulated humanoid benchmark with 27 whole-body tasks (15 manipulation + 12 locomotion) and tactile sensing.
  why_it_matters: Standard humanoid WBC benchmark adopted by many follow-up works.

- title: Mobile ALOHA — Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation
  authors: Zipeng Fu, Tony Z. Zhao, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2401.02117
  paper_url: https://arxiv.org/abs/2401.02117
  project_url: https://mobile-aloha.github.io/
  code_url: https://github.com/MarkFzp/mobile-aloha
  category: Loco-Manip
  task_tags: [bimanual, mobile-manip, teleop]
  robot_platform: Custom mobile ALOHA
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: $32k whole-body teleop platform enabling bimanual mobile manipulation with co-trained imitation policies.
  why_it_matters: Reference design for low-cost mobile bimanual data collection; spawned an entire research line.

- title: ALOHA Unleashed — A Simple Recipe for Robot Dexterity
  authors: Tony Z. Zhao, Jonathan Tompson, Danny Driess, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2410.13126
  paper_url: https://arxiv.org/abs/2410.13126
  project_url: https://aloha-unleashed.github.io/
  code_url: ❌
  category: Loco-Manip
  task_tags: [bimanual, dexterous, diffusion-policy, large-data]
  robot_platform: ALOHA 2
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: 26k+ demos + diffusion policies enable challenging bimanual deformable-object and contact-rich manipulation.
  why_it_matters: Shows scaling demos + expressive policy class is sufficient for hard bimanual dexterity.

- title: UMI on Legs — Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers
  authors: Huy Ha, Yihuai Gao, Zipeng Fu, Jie Tan, Shuran Song
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.10353
  paper_url: https://arxiv.org/abs/2407.10353
  project_url: https://umi-on-legs.github.io/
  code_url: https://github.com/real-stanford/umi-on-legs
  category: Loco-Manip
  task_tags: [quadruped, mobile-manip, sim-to-real, end-effector-tracking]
  robot_platform: Unitree B1 + arm
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Plug fixed-base UMI manipulation policies onto a quadruped via a manipulation-centric whole-body controller.
  why_it_matters: Cleanly decouples task data from embodiment; cross-embodiment zero-shot transfer.

- title: Visual Whole-Body Control for Legged Loco-Manipulation
  authors: Minghuan Liu, Zixuan Chen, Xuxin Cheng, Yandong Ji, Ri-Zhao Qiu, Ruihan Yang, Xiaolong Wang
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2403.16967
  paper_url: https://arxiv.org/abs/2403.16967
  project_url: https://wholebody-b1.github.io/
  code_url: https://github.com/Ericonaldo/visual_wholebody
  category: Loco-Manip
  task_tags: [quadruped, vision, whole-body, end-effector]
  robot_platform: Unitree B1 + Z1
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Hierarchical vision-driven whole-body control achieving >70% success on prehensile and dynamic loco-manipulation.
  why_it_matters: Reference architecture (low-level WBC + high-level visual policy) for legged loco-manipulation.

- title: Helpful DoggyBot — Open-World Object Fetching using Legged Robots and Vision-Language Models
  authors: Qi Wu, Zipeng Fu, Xuxin Cheng, Xiaolong Wang, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2410.00231
  paper_url: https://arxiv.org/abs/2410.00231
  project_url: https://helpful-doggybot.github.io/
  code_url: ❌
  category: Loco-Manip
  task_tags: [quadruped, VLM, open-world, fetching]
  robot_platform: Unitree Go2 + 1-DoF gripper
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: 1-DoF "biting" gripper + RL whole-body controller + VLM planner for zero-shot open-world fetching.
  why_it_matters: Minimal hardware + foundation models suffice for indoor mobile manipulation.

- title: Pedipulate — Enabling Manipulation Skills using a Quadruped Robot's Leg
  authors: Philip Arm, Mayank Mittal, Hendrik Kolvenbach, Marco Hutter
  year: 2024
  venue: ICRA 2024
  arxiv_id: 2402.10837
  paper_url: https://arxiv.org/abs/2402.10837
  project_url: https://sites.google.com/leggedrobotics.com/pedipulate
  code_url: ❌
  category: Loco-Manip
  task_tags: [quadruped, pedipulation, door-opening]
  robot_platform: ANYmal D
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: One-foot RL position-tracking policy enabling whole-body pedipulation (doors, sample collection, pushing) on ANYmal.
  why_it_matters: Pioneers the "leg-as-arm" pedipulation paradigm with emergent gait.

- title: Humanoid Parkour Learning
  authors: Ziwen Zhuang, Shenzhe Yao, Hang Zhao
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10759
  paper_url: https://arxiv.org/abs/2406.10759
  project_url: https://humanoid4parkour.github.io/
  code_url: https://github.com/ZiwenZhuang/parkour
  category: WBC
  task_tags: [parkour, vision, jumping]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: End-to-end vision-based whole-body parkour policy: jumping platforms, hurdles, 0.8m gaps, 1.8 m/s running.
  why_it_matters: First end-to-end perceptive humanoid parkour without motion priors.

- title: Learning Humanoid Locomotion with Perceptive Internal Model
  authors: Junfeng Long, Junli Ren, Moji Shi, Zirui Wang, Tao Huang, Ping Luo, Jiangmiao Pang
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2411.14386
  paper_url: https://arxiv.org/abs/2411.14386
  project_url: https://junfeng-long.github.io/PIM/
  code_url: https://github.com/OpenRobotLab/HIMLoco
  category: WBC
  task_tags: [locomotion, perception, elevation-map]
  robot_platform: Unitree H1, G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Perceptive Internal Model on elevation maps generalizes single-stage perceptive locomotion across humanoid platforms.
  why_it_matters: Single recipe transfers across humanoids; production-ready perceptive locomotion.

- title: Catch It! — Learning to Catch in Flight with Mobile Dexterous Hands
  authors: Yuanhang Zhang, Tianhai Liang, Zhenyang Chen, Yanjie Ze, Huazhe Xu
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2409.10319
  paper_url: https://arxiv.org/abs/2409.10319
  project_url: https://mobile-dex-catch.github.io/
  code_url: https://github.com/hang0610/Catch_It
  category: Loco-Manip
  task_tags: [catching, dynamic, mobile-base, dexterous]
  robot_platform: Mobile base + arm + 12-DoF hand
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Two-stage RL whole-body-control catching policy that achieves ~80% sim catch success on diverse trajectories.
  why_it_matters: Dynamic in-flight catch with mobile + dexterous hand; rare WBC dynamic-manip benchmark.

- title: Whole-Body Dynamic Throwing with Legged Manipulators
  authors: Humphrey Munn, et al.
  year: 2024
  venue: arXiv 2024
  arxiv_id: 2410.05681
  paper_url: https://arxiv.org/abs/2410.05681
  project_url: https://www.humphreymunn.com/whole-body-dynamic-throwing
  code_url: ❌
  category: Loco-Manip
  task_tags: [throwing, dynamic, curriculum, quadruped-arm]
  robot_platform: ANYmal + arm
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Unified RL controller for base+arm leveraging curriculum to fuse locomotion and manipulation advantages for throwing.
  why_it_matters: Demonstrates whole-body throwing with extended workspace via locomotion assist.

- title: Open-TeleVision — Teleoperation with Immersive Active Visual Feedback
  authors: Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.01512
  paper_url: https://arxiv.org/abs/2407.01512
  project_url: https://robot-tv.github.io/
  code_url: https://github.com/OpenTeleVision/TeleVision
  category: WBC
  task_tags: [teleop, VR, stereoscopic, bimanual]
  robot_platform: Unitree H1, Fourier GR1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: ⭐ Code
  one_line: VR-based stereoscopic teleop with active head tracking, validated on H1 + GR1 with imitation learning.
  why_it_matters: Open-source VR teleop foundation enabling humanoid manipulation data collection at scale.

- title: ACE — A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation
  authors: Shiqi Yang, Minghuan Liu, Yuzhe Qin, Runyu Ding, Jialong Li, Xuxin Cheng, Ruihan Yang, Sha Yi, Xiaolong Wang
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2408.11805
  paper_url: https://arxiv.org/abs/2408.11805
  project_url: https://ace-teleop.github.io/
  code_url: https://github.com/ACETeleop/ACETeleop
  category: WBC
  task_tags: [teleop, exoskeleton, cross-embodiment]
  robot_platform: H1 + Inspire, Xarm + Ability, GR-1, Franka, B1+Z1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Cross-platform visual-exoskeleton teleop generalizing to humanoid hands, arms, grippers, and quadruped-grippers.
  why_it_matters: Defines the low-cost cross-embodiment teleop standard.

- title: OKAMI — Teaching Humanoid Robots Manipulation Skills through Single Video Imitation
  authors: Jinhan Li, Yifeng Zhu, Yuqi Xie, Zhenyu Jiang, Mingyo Seo, Georgios Pavlakos, Yuke Zhu
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2410.11792
  paper_url: https://arxiv.org/abs/2410.11792
  project_url: https://ut-austin-rpl.github.io/OKAMI/
  code_url: ❌
  category: WBC
  task_tags: [video-imitation, object-aware, retargeting]
  robot_platform: Fourier GR1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Two-stage single-video imitation: open-world plan + object-aware retargeting + closed-loop visuomotor policy (~79%).
  why_it_matters: Low-data humanoid manipulation pipeline avoiding teleop demos.

- title: Generalizable Humanoid Manipulation with 3D Diffusion Policies (iDP3)
  authors: Yanjie Ze, Zixuan Chen, Wenhao Yu, Tony Z. Zhao, Jiajun Wu, C. Karen Liu, Jia Deng, Jiajun Wu
  year: 2024
  venue: IROS 2025
  arxiv_id: 2410.10803
  paper_url: https://arxiv.org/abs/2410.10803
  project_url: https://humanoid-manipulation.github.io/
  code_url: https://github.com/YanjieZe/Improved-3D-Diffusion-Policy
  category: Loco-Manip
  task_tags: [3D-diffusion, manipulation, humanoid]
  robot_platform: Fourier GR1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Improved 3D Diffusion Policy enabling generalizable humanoid manipulation from a small set of demonstrations.
  why_it_matters: Strong open baseline for humanoid manipulation policies; widely adopted.

- title: π0.5 — A Vision-Language-Action Model with Open-World Generalization
  authors: Physical Intelligence team
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2504.16054
  paper_url: https://arxiv.org/abs/2504.16054
  project_url: https://www.pi.website/blog/pi05
  code_url: https://github.com/Physical-Intelligence/openpi
  category: Loco-Manip
  task_tags: [VLA, mobile-manip, open-world, generalization]
  robot_platform: Mobile bimanual platforms
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: false
  code_status: 🧩 Partial Code
  one_line: VLA with broad cross-task co-training enabling 10-15-min mobile manipulation in unseen homes.
  why_it_matters: Sets the bar for open-world generalist manipulation; available openpi weights/runtime.

- title: Pi0 — A Vision-Language-Action Flow Model for General Robot Control
  authors: Kevin Black, Noah Brown, Danny Driess, et al. (Physical Intelligence)
  year: 2024
  venue: arXiv 2024
  arxiv_id: 2410.24164
  paper_url: https://arxiv.org/abs/2410.24164
  project_url: https://www.pi.website/blog/pi0
  code_url: https://github.com/Physical-Intelligence/openpi
  category: Loco-Manip
  task_tags: [VLA, flow-matching, generalist]
  robot_platform: 7 platforms / 68 tasks
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: VLA flow-matching policy delivering generalist dexterous robot control across 7 robots / 68 tasks.
  why_it_matters: Most influential general robot policy of 2024-25; open weights via openpi.

- title: COLA — Learning Human-Humanoid Coordination for Collaborative Object Carrying
  authors: Yanwen Zou, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2510.14293
  paper_url: https://arxiv.org/abs/2510.14293
  project_url: https://collaborative-cola.github.io/
  code_url: ❌
  category: Loco-Manip
  task_tags: [collaboration, carrying, human-robot]
  robot_platform: Unitree H1-2
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Coordination policy for human-humanoid collaborative object carrying along straight/curved trajectories.
  why_it_matters: Real user study (23 participants) showing humanoids as physical partners.

- title: Kinematics-Aware Multi-Policy RL for Force-Capable Humanoid Loco-Manipulation
  authors: Anonymous
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2511.21169
  paper_url: https://arxiv.org/abs/2511.21169
  project_url: https://hugging-physics.github.io/KAMP/
  code_url: ❌
  category: Loco-Manip
  task_tags: [force, cart-pushing, multi-policy]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Three-stage decoupled training (upper / lower / delta-command) enabling 4 kg carry and 112.8 kg cart-push on G1.
  why_it_matters: Achieves heavy-payload loco-manipulation by explicitly modeling kinematic feedback.

- title: StageACT — Stage-Conditioned Imitation for Robust Humanoid Door Opening
  authors: Anonymous
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2509.13200
  paper_url: https://arxiv.org/abs/2509.13200
  project_url: https://stageact.github.io/
  code_url: ❌
  category: Loco-Manip
  task_tags: [door-opening, IL, stage-conditioned]
  robot_platform: Humanoid (office)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Stage-conditioned imitation learning that more than doubles door-opening success on unseen doors (55%).
  why_it_matters: Tackles partial observability in real office humanoid loco-manipulation.

- title: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer
  authors: Anonymous
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2512.01061
  paper_url: https://arxiv.org/abs/2512.01061
  project_url: ❌
  code_url: ❌
  category: Loco-Manip
  task_tags: [door-opening, RGB, GRPO, articulated]
  robot_platform: Humanoid (RGB)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌
  one_line: Teacher-student-bootstrap + GRPO yielding RGB-only zero-shot diverse door-opening, beating teleop by 31.7%.
  why_it_matters: First humanoid sim-to-real RGB policy for diverse articulated loco-manipulation.

- title: Human2LocoMan — Learning Versatile Quadrupedal Manipulation with Human Pretraining
  authors: Yaru Niu, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2506.16475
  paper_url: https://arxiv.org/abs/2506.16475
  project_url: https://human2bots.github.io/
  code_url: https://github.com/Hi-DAVID/Human2LocoMan
  category: Loco-Manip
  task_tags: [quadruped, human-pretraining, cross-embodiment]
  robot_platform: LocoMan (Unitree Go1 + arm)
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Cross-embodiment data collection + learning that pretrains on humans before transferring to a quadruped manipulator.
  why_it_matters: Demonstrates human data scaling for quadruped loco-manipulation.

- title: LocoMan — Advancing Versatile Quadrupedal Dexterity with Lightweight Loco-Manipulators
  authors: Changyi Lin, et al.
  year: 2024
  venue: IROS 2024
  arxiv_id: 2403.18197
  paper_url: https://arxiv.org/abs/2403.18197
  project_url: https://linchangyi1.github.io/LocoMan/
  code_url: https://github.com/linchangyi1/LocoMan
  category: Loco-Manip
  task_tags: [quadruped, manipulator, loco-manip]
  robot_platform: Unitree Go1 + light arms
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Open quadruped + lightweight arms platform with multi-mode loco-manipulation skills.
  why_it_matters: De facto open hardware for quadruped manipulation research.

- title: MoMa-LLM — Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation
  authors: Daniel Honerkamp, Martin Büchner, Fabien Despinoy, Tim Welschehold, Abhinav Valada
  year: 2024
  venue: RA-L 2024
  arxiv_id: 2403.08605
  paper_url: https://arxiv.org/abs/2403.08605
  project_url: https://moma-llm.cs.uni-freiburg.de/
  code_url: https://github.com/robot-learning-freiburg/MoMa-LLM
  category: Loco-Manip
  task_tags: [LLM, mobile-manip, scene-graph, search]
  robot_platform: Mobile manipulator (sim/real)
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: LLM-grounded dynamic scene graphs for open-vocabulary interactive object search with mobile manipulation.
  why_it_matters: Practical LLM-driven mobile manipulation baseline; open code.

- title: HumanoidExo — Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton
  authors: Anonymous
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2510.03022
  paper_url: https://arxiv.org/abs/2510.03022
  project_url: https://humanoidexo.github.io/
  code_url: ❌
  category: WBC
  task_tags: [exoskeleton, data-collection, whole-body]
  robot_platform: Humanoid (general)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Wearable exoskeleton enabling scalable humanoid whole-body manipulation data collection.
  why_it_matters: Lower-cost path to large-scale whole-body humanoid demos.

- title: BumbleBee (BB) — Expert-Generalist Whole-Body Humanoid Control
  authors: BeingBeyond team
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2510.25241
  paper_url: https://arxiv.org/abs/2510.25241
  project_url: https://beingbeyond.github.io/BumbleBee/
  code_url: ❌
  category: WBC
  task_tags: [generalist, expert-distillation, sim-to-real]
  robot_platform: Humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Motion-cluster experts distilled into a unified generalist whole-body controller with delta-action sim-to-real.
  why_it_matters: Combines clustering, residual sim-to-real, and expert-generalist distillation in one stack.

- title: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  authors: Anonymous
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2506.22827
  paper_url: https://arxiv.org/abs/2506.22827
  project_url: ❌
  code_url: ❌
  category: Loco-Manip
  task_tags: [VLM, planning, multi-step, humanoid]
  robot_platform: Humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌
  one_line: Hierarchical VLM planner that orchestrates multi-step humanoid manipulation primitives.
  why_it_matters: Pairs VLM-level planning with low-level WBC for long-horizon tasks.

- title: Humanoid Locomotion and Manipulation: Current Progress and Challenges
  authors: Zhaoyuan Gu, Junheng Li, Wenlan Shen, et al.
  year: 2025
  venue: arXiv 2025 (Survey)
  arxiv_id: 2501.02116
  paper_url: https://arxiv.org/abs/2501.02116
  project_url: ❌
  code_url: ❌
  category: WBC
  task_tags: [survey, locomotion, manipulation]
  robot_platform: N/A
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: false
  code_status: ❌
  one_line: Comprehensive 2025 survey of humanoid locomotion and manipulation control, planning, and learning.
  why_it_matters: Authoritative reference and roadmap for the loco-manip field.

- title: ARMOR — Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning
  authors: Daehwa Kim, et al.
  year: 2024
  venue: arXiv 2024
  arxiv_id: 2412.00396
  paper_url: https://arxiv.org/abs/2412.00396
  project_url: https://arxiv.org/abs/2412.00396
  code_url: ❌
  category: WBC
  task_tags: [egocentric-perception, motion-planning, collision]
  robot_platform: Humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌
  one_line: Distributed wearable depth sensors + transformer policy for humanoid collision-aware whole-body motion.
  why_it_matters: Tackles dense-environment safe whole-body motion planning.

- title: PARC — Physics-based Augmentation with RL for Character Controllers
  authors: Michael Xu, Yi Shi, KangKang Yin, Xue Bin Peng
  year: 2025
  venue: SIGGRAPH 2025
  arxiv_id: 2505.04002
  paper_url: https://arxiv.org/abs/2505.04002
  project_url: https://michaelx.io/parc/
  code_url: https://github.com/michaelx-research/parc
  category: WBC
  task_tags: [character-control, terrain, augmentation]
  robot_platform: Simulated character / humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Iterative ML+physics augmentation expanding terrain traversal repertoire of physics-based humanoid characters.
  why_it_matters: Bridge between graphics character control and humanoid robot terrain skills.

- title: Visual Imitation Enables Contextual Humanoid Control (VideoMimic)
  authors: Arthur Allshire, Hongsuk Choi, Junyi Zhang, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2505.03729
  paper_url: https://arxiv.org/abs/2505.03729
  project_url: https://www.videomimic.net/
  code_url: https://github.com/HybridRobotics/VideoMimic
  category: WBC
  task_tags: [video-imitation, terrain, contextual]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Reconstructs human motion + terrain from video to train context-aware humanoid policies (stair-climb, sit, terrain).
  why_it_matters: Couples vision-based environment reconstruction with whole-body policy learning.

- title: Learning Getting-Up Policies for Real-World Humanoid Robots
  authors: Xialin He, Runpei Dong, Zixuan Chen, Saurabh Gupta
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.12152
  paper_url: https://arxiv.org/abs/2502.12152
  project_url: https://humanoid-getup.github.io/
  code_url: ❌
  category: WBC
  task_tags: [getting-up, contact-rich, two-stage RL]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Two-stage curriculum + posture-conditioned RL learning robust real-world humanoid getting-up.
  why_it_matters: Complementary view to HoST; rigorous outdoor + indoor evaluation.

- title: SigLoMa — Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
  authors: Shiyi Chen; Haiyi Liu; Mingye Yang; Jiaqi Zhang; Debing Zhang
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.03846
  paper_url: https://arxiv.org/abs/2605.03846
  project_url: https://11chens.github.io/SigLoMa/
  code_url: ""
  category: Loco-Manipulation
  task_tags: [quadruped, ego-centric, sigma-points, kalman-filter, active-sampling, open-vocabulary]
  robot_platform: quadruped
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Sigma-Points geometric representation + ego-centric Kalman filter and active-sampling curriculum for open-world pick-and-place from 5Hz detector.
  why_it_matters: Tsinghua quadrupedal loco-manipulation that approaches expert teleop performance using only ego-centric vision; methodology likely transfers to humanoid arms.

- title: BifrostUMI — Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation
  authors: Chenhao Yu; Hongwu Wang; Youhao Hu; Jiachen Zhang; Yuanyuan Li; Shaqi Luo
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.03452
  paper_url: https://arxiv.org/abs/2605.03452
  project_url: ""
  code_url: ""
  category: Loco-Manipulation
  task_tags: [robot-free-data, VR, keypoint-trajectories, wrist-camera, whole-body-manipulation, retargeting]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Lightweight VR + wrist-camera demo-collection pipeline that predicts future keypoint trajectories and retargets them to humanoid whole-body control.
  why_it_matters: Pushes humanoid manipulation data scaling beyond teleoperation by using portable VR-only capture; complements UMI / Humanoid Manipulation Interface line.

- title: WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning
  authors: Jaehwi Jang; Zhaoyuan Gu; Alfred Cueva; Zimeng Chai; Junjie Sheng; Thong Nguyen; Himank Galundia; Yifan Wu; Huishu Xue; Isaac Legene; Ojas Mediratta; Davin Doan
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.13232
  paper_url: https://arxiv.org/abs/2606.13232
  project_url: https://wt-umi.github.io/WTUMI/
  code_url: ""
  category: Loco-Manipulation
  task_tags: [tactile, force-supervised, contact-aware, teleoperation, whole-body-manipulation]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Wearable tactile interface and force-conditioned target-pose correction for whole-body manipulation of bulky or shared-load objects.
  why_it_matters: Makes contact force a first-class signal for humanoid whole-body imitation instead of an implicit side effect.

- title: GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training
  authors: Zhihai Bi; Qiang Zhang; Guoyang Zhao; Jiahang Cao; Xueyin Luo; Yushan Zhang; Jinglan Xu; Ruoyu Geng; Yulin Li; Andrew F. Luo; Jun Ma
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.12995
  paper_url: https://arxiv.org/abs/2606.12995
  project_url: ""
  code_url: ""
  category: Loco-Manipulation
  task_tags: [humanoid-object-interaction, generated-video, contact-aware, zero-shot]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Zero-shot humanoid-object interaction pipeline that imitates generated task videos and extracts contact events without task-specific training.
  why_it_matters: Directly connects generative video priors to deployable humanoid HOI.

- title: Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation
  authors: Mehmet Turan Yardımcı
  year: 2026
  venue: ICRA 2026 Workshop RL4IL
  arxiv_id: 2606.11891
  paper_url: https://arxiv.org/abs/2606.11891
  project_url: ""
  code_url: ""
  category: Loco-Manipulation
  task_tags: [dual-critic, reinforcement-learning, reaching, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Controlled IsaacLab study showing dual critics outperform unified critics for humanoid reaching and loco-manipulation curricula.
  why_it_matters: Small but actionable architecture result for multi-objective humanoid RL.

- title: VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands
  authors: Dongting Li; Qianyang Wu; Xingyu Chen; Liang Li; Yuhang Lin; Sikai Wu; Guoyao Zhang; Mingliang Zhou; Diyun Xiang; Qiang Zhang; Renjing Xu; Jianzhu Ma
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.09286
  paper_url: https://arxiv.org/abs/2606.09286
  project_url: https://vaic-humanoid.github.io/
  code_url: ""
  category: Loco-Manipulation
  task_tags: [vision-guided, agile-object-interaction, decoupled-commands, whole-body]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Decoupled command framework for vision-guided agile humanoid object interaction under imperfect observability.
  why_it_matters: Moves loco-manipulation beyond privileged object state and dense reference trajectories.

- title: OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation
  authors: Zehao Yu; Jiakun Zheng; Weiji Xie; Jiyuan Shi; Chenyun Zhang; Chenjia Bai; Xuelong Li
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.08548
  paper_url: https://arxiv.org/abs/2606.08548
  project_url: https://oasis-humanoid.github.io/
  code_url: https://github.com/TeleHuman/OASIS
  category: Loco-Manipulation
  task_tags: [simulation-data, teleoperation, data-collection, loco-manipulation]
  robot_platform: Unitree G1 / humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Open simulation-to-real data pipeline for humanoid loco-manipulation with embodiment-aligned demonstrations.
  why_it_matters: Provides a reproducible route around slow real-world teleop collection.

- title: SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation
  authors: Songlin Wei; Zhenhao Ni; Jie Liu; Zhenyu Zhao; Junjie Ye; Hongyi Jing; Junkai Xia; Xiawei Liu; Michael Leong; Liang Heng; Di Huang; Yue Wang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.08278
  paper_url: https://arxiv.org/abs/2606.08278
  project_url: https://github.com/physical-superintelligence-lab/SIMPLE
  code_url: https://github.com/physical-superintelligence-lab/SIMPLE
  category: Loco-Manipulation
  task_tags: [benchmark, MuJoCo, simulation, humanoid-foundation-models]
  robot_platform: humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Full-stack simulation environment and benchmark for policy learning and evaluation in humanoid loco-manipulation.
  why_it_matters: Gives the field a reproducible alternative to expensive real-world evaluation.

- title: MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation
  authors: Ilyass Taouil; Michal Ciebelski; Shafeef Omar; Haizhou Zhao; Angela Dai; Aaron M. Johnson; Majid Khadiv
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.06139
  paper_url: https://arxiv.org/abs/2606.06139
  project_url: ""
  code_url: ""
  category: Loco-Manipulation
  task_tags: [motion-discovery, LLM-search, contact-rich, long-horizon]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: LLM-guided evolutionary search discovers long-horizon contact-rich loco-manipulation motions without teleop or human retargeting.
  why_it_matters: Explores a third path between demonstration collection and hand-designed rewards.

- title: HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
  authors: Lizhi Yang; Junheng Li; Nehar Poddar; Yiling Hou; Gio Huh; Robert Griffin; Georgia Gkioxari; Aaron Ames
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.06493
  paper_url: https://arxiv.org/abs/2606.06493
  project_url: https://lzyang2000.github.io/HANDOFF/
  code_url: https://github.com/lzyang2000/HANDOFF
  category: Loco-Manipulation
  task_tags: [task-space-control, distilled-teachers, agentic-control, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Distills complementary teachers into a task-space whole-body command interface for diverse humanoid loco-manipulation skills.
  why_it_matters: Offers a compact control interface that planners can actually synthesize.

- title: Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
  authors: Junheng Li; Liang Wu; Sergio A. Esteban; Lizhi Yang; Jan Drgona; Aaron D. Ames
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.05687
  paper_url: https://arxiv.org/abs/2606.05687
  project_url: https://github.com/junhengl/mpc-rl
  code_url: https://github.com/junhengl/mpc-rl
  category: Loco-Manipulation
  task_tags: [MPC-guided-RL, centroidal-MPC, locomotion, manipulation]
  robot_platform: humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Efficient training-time MPC guidance for humanoid locomotion and manipulation policies.
  why_it_matters: Makes model-based structure practical inside large-scale RL training loops.

- title: GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors
  authors: Tianyi Xie; Haotian Zhang; Jinhyung Park; Zi Wang; Bowen Wen; Jiefeng Li; Xueting Li; Qingwei Ben; Haoyang Weng; Yufei Ye; David Minor; Tingwu Wang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.05160
  paper_url: https://arxiv.org/abs/2606.05160
  project_url: https://research.nvidia.com/labs/dair/grail/
  code_url: https://github.com/NVlabs/GRAIL
  dataset_url: https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL
  category: Loco-Manipulation
  task_tags: [data-generation, 3D-assets, video-priors, sim-to-real]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Fully virtual generation pipeline composing 3D assets, simulator scenes, and video priors into robot-compatible loco-manipulation data.
  why_it_matters: Strong NVIDIA data engine for scaling humanoid manipulation without physical teleop bottlenecks.

- title: SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation
  authors: Jeonguk Kang; Hanbyel Cho; Sanghyun Kang; Donghan Koo
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.03297
  paper_url: https://arxiv.org/abs/2606.03297
  project_url: ""
  code_url: ""
  category: Loco-Manipulation
  task_tags: [load-aware, factorized-adaptation, sim-to-real, object-mass]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Factorizes load variation and dynamics mismatch into separate adapters for robust humanoid pickup and placement.
  why_it_matters: Attacks a core sim-to-real pain point in payload-changing loco-manipulation.
