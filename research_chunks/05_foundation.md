# Humanoid Foundation Models & Generalist Policies

Curated list of papers on humanoid foundation models, generalist robot policies, and Vision-Language-Action (VLA) systems applicable to humanoid whole-body control and HOI tasks. 2023-2026 with priority on 2024-2026.

Code-status legend:
- ⭐ Code (full repo committed)
- 🧩 Partial Code (subset / inference-only)
- 📦 Dataset released
- 🌐 Project Page only
- ⏳ Code Coming Soon
- 🔁 Unofficial / community re-implementation
- ❌ No Code Found

---

- title: GR00T N1 / N1.5 — An Open Foundation Model for Generalist Humanoid Robots
  authors: Johan Bjorck, Fernando Castaneda, Nikita Cherniadev, ... NVIDIA GEAR Team
  year: 2025
  venue: arXiv (Mar 2025); NVIDIA Tech Report
  arxiv_id: 2503.14734
  paper_url: https://arxiv.org/abs/2503.14734
  project_url: https://research.nvidia.com/labs/gear/gr00t-n1_5/
  code_url: https://github.com/NVIDIA/Isaac-GR00T
  category: Foundation
  task_tags: [VLA, humanoid, dual-system, flow-matching, large-scale-pretrain, manipulation]
  robot_platform: Fourier GR-1 (humanoid), bimanual arms, single-arm
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Pretrained weights (HF) — N1, N1.5, N1.7 released
  one_line: NVIDIA's open dual-system (VLM + diffusion transformer) VLA pre-trained on real robot, human video, and synthetic data; the reference open humanoid foundation model.
  why_it_matters: First open humanoid foundation model with full code/weights; baseline that virtually every subsequent humanoid VLA paper compares to.

- title: π0 — A Vision-Language-Action Flow Model for General Robot Control
  authors: Kevin Black, Noah Brown, Danny Driess, ... Sergey Levine (Physical Intelligence)
  year: 2024
  venue: arXiv (Oct 2024)
  arxiv_id: 2410.24164
  paper_url: https://arxiv.org/abs/2410.24164
  project_url: https://www.physicalintelligence.company/blog/pi0
  code_url: https://github.com/Physical-Intelligence/openpi
  category: Foundation / VLA
  task_tags: [VLA, flow-matching, generalist, dexterous, mobile-manipulation, 50Hz-control]
  robot_platform: Single-arm, dual-arm, mobile manipulators (multi-embodiment)
  uses_real_robot: yes
  uses_humanoid: no (upper-body humanoid-style bimanual)
  uses_simulation: yes
  code_status: ⭐ Code (openpi) + 📦 Weights (pi0, pi0-FAST, pi0.5)
  why_it_matters: Established the flow-matching action-expert paradigm now adopted by GR00T, X-VLA, π0.5; backbone of many humanoid policies.

- title: π0.5 — A VLA with Open-World Generalization
  authors: Physical Intelligence Team
  year: 2025
  venue: arXiv (Apr 2025)
  arxiv_id: 2504.16054
  paper_url: https://arxiv.org/abs/2504.16054
  project_url: https://www.pi.website/blog/pi05
  code_url: https://github.com/Physical-Intelligence/openpi
  category: Foundation / VLA
  task_tags: [VLA, open-world, mobile-manipulation, knowledge-insulation, co-training]
  robot_platform: Mobile manipulators in unseen real homes (kitchens, bedrooms)
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no (real-home eval)
  code_status: ⭐ Code (in openpi) + 📦 Weights
  why_it_matters: Demonstrates that heterogeneous co-training enables real open-world deployment, a target for humanoid generalists.

- title: OpenVLA — An Open-Source Vision-Language-Action Model
  authors: Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, ... Chelsea Finn, Sergey Levine
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.09246
  paper_url: https://arxiv.org/abs/2406.09246
  project_url: https://openvla.github.io/
  code_url: https://github.com/openvla/openvla
  category: VLA / Generalist-Policy
  task_tags: [VLA, 7B-LLaMA2, open-source, OXE-pretrain, manipulation]
  robot_platform: WidowX, Franka, multi-arm (29 OXE tasks)
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (MIT)
  why_it_matters: Reference open-source VLA; near-universal baseline; backbone of many follow-ups (OFT, ECoT, NORA).

- title: OpenVLA-OFT / OFT+ — Fine-Tuning VLAs: Optimizing Speed and Success
  authors: Moo Jin Kim, Chelsea Finn, Percy Liang
  year: 2025
  venue: arXiv (Feb 2025)
  arxiv_id: 2502.19645
  paper_url: https://arxiv.org/abs/2502.19645
  project_url: https://openvla-oft.github.io/
  code_url: https://github.com/moojink/openvla-oft
  category: VLA
  task_tags: [parallel-decoding, action-chunking, L1-regression, FiLM, bimanual-ALOHA, LIBERO]
  robot_platform: ALOHA bimanual, LIBERO sim
  uses_real_robot: yes
  uses_humanoid: yes (bimanual humanoid-style)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Beats π0 / RDT-1B / ACT / Diffusion Policy on bimanual ALOHA; the recipe-of-choice for fine-tuning VLAs to humanoid arms.

- title: RT-1 — Robotics Transformer for Real-World Control at Scale
  authors: Anthony Brohan, Noah Brown, Justice Carbajal, ... (Google)
  year: 2022
  venue: RSS 2023
  arxiv_id: 2212.06817
  paper_url: https://arxiv.org/abs/2212.06817
  project_url: https://robotics-transformer1.github.io/
  code_url: https://github.com/google-research/robotics_transformer
  category: Generalist-Policy
  task_tags: [transformer, EfficientNet+TokenLearner, multi-task, 130k-episodes]
  robot_platform: Everyday Robots mobile manipulators
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: 🧩 Partial Code (training infra released)
  why_it_matters: First large-scale transformer manipulation policy; foundational ancestor of all VLAs.

- title: RT-2 — Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
  authors: Brohan et al. (Google DeepMind)
  year: 2023
  venue: CoRL 2023
  arxiv_id: 2307.15818
  paper_url: https://arxiv.org/abs/2307.15818
  project_url: https://robotics-transformer2.github.io/
  code_url: ""
  category: VLA
  task_tags: [VLA, web-knowledge, co-fine-tuning, PaLI-X, PaLM-E]
  robot_platform: Everyday Robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ❌ No Code Found (closed; 🔁 community re-implementations exist)
  why_it_matters: Coined the "VLA" term; canonical reference even though closed-source.

- title: RT-X / Open X-Embodiment — Robotic Learning Datasets and RT-X Models
  authors: Open X-Embodiment Collaboration (21 institutions)
  year: 2023
  venue: ICRA 2024
  arxiv_id: 2310.08864
  paper_url: https://arxiv.org/abs/2310.08864
  project_url: https://robotics-transformer-x.github.io/
  code_url: https://github.com/google-deepmind/open_x_embodiment
  category: Generalist-Policy / Dataset
  task_tags: [cross-embodiment, OXE, 22-robots, 527-skills, dataset]
  robot_platform: 22 different robot embodiments
  uses_real_robot: yes
  uses_humanoid: no (mostly arms)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Dataset (OXE)
  why_it_matters: The de-facto pre-training dataset for nearly every VLA / humanoid foundation model.

- title: RT-H — Action Hierarchies Using Language
  authors: Suneel Belkhale, Ted Xiao, Pierre Sermanet, ... (Google DeepMind)
  year: 2024
  venue: arXiv (Mar 2024)
  arxiv_id: 2403.01823
  paper_url: https://arxiv.org/abs/2403.01823
  project_url: https://rt-hierarchy.github.io/
  code_url: ""
  category: VLA
  task_tags: [language-motions, hierarchy, intervention, RT-2-based]
  robot_platform: Everyday Robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: ❌ No Code Found
  why_it_matters: Introduces "language motions" hierarchy — influential pattern for humanoid skill libraries.

- title: Octo — An Open-Source Generalist Robot Policy
  authors: Octo Model Team — Dibya Ghosh, Homer Walke, Karl Pertsch, ... Sergey Levine
  year: 2024
  venue: RSS 2024
  arxiv_id: 2405.12213
  paper_url: https://arxiv.org/abs/2405.12213
  project_url: https://octo-models.github.io/
  code_url: https://github.com/octo-models/octo
  category: Generalist-Policy
  task_tags: [transformer, diffusion-head, OXE-pretrain, language+goal-image]
  robot_platform: 9 robotic platforms (single+dual arm)
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (Octo-Small 27M, Octo-Base 93M)
  why_it_matters: Open generalist policy that fine-tunes in hours; a workhorse baseline.

- title: RoboFlamingo — Vision-Language Foundation Models as Effective Robot Imitators
  authors: Xinghang Li, Minghuan Liu, Hanbo Zhang, ... Tao Kong
  year: 2023
  venue: ICLR 2024
  arxiv_id: 2311.01378
  paper_url: https://arxiv.org/abs/2311.01378
  project_url: https://roboflamingo.github.io/
  code_url: https://github.com/RoboFlamingo/RoboFlamingo
  category: VLA
  task_tags: [OpenFlamingo-backbone, imitation, CALVIN, single-GPU]
  robot_platform: CALVIN sim, Franka
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Early influential demonstration that frozen open VLMs can drive manipulation.

- title: GR-1 — Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation
  authors: Hongtao Wu, Ya Jing, Chilam Cheang, ... Tao Kong (ByteDance)
  year: 2023
  venue: ICLR 2024
  arxiv_id: 2312.13139
  paper_url: https://arxiv.org/abs/2312.13139
  project_url: https://gr1-manipulation.github.io/
  code_url: https://github.com/bytedance/GR-1
  category: Foundation
  task_tags: [video-pretrain, GPT-style, visual-prediction, CALVIN]
  robot_platform: Franka, CALVIN sim
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Established video pre-training as a route to manipulation generalization.

- title: GR-2 — A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation
  authors: Chilam Cheang, Sijin Chen, Zhongren Cui, ... (ByteDance Research)
  year: 2024
  venue: arXiv (Oct 2024)
  arxiv_id: 2410.06158
  paper_url: https://arxiv.org/abs/2410.06158
  project_url: https://gr2-manipulation.github.io/
  code_url: ""
  category: Foundation
  task_tags: [38M-videos, generative-VLA, multi-task, dual-arm]
  robot_platform: Dual-arm setups
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: 🌐 Project Page only
  why_it_matters: Scales GR-1's video pre-training 50× to 38M clips; 97.7% avg over 100+ tasks.

- title: GR-3 Technical Report
  authors: ByteDance Seed Team
  year: 2025
  venue: arXiv (Jul 2025)
  arxiv_id: 2507.15493
  paper_url: https://arxiv.org/abs/2507.15493
  project_url: https://seed.bytedance.com/GR3
  code_url: ""
  category: Foundation
  task_tags: [VLA, VR-human-data, mobile-bimanual, ByteMini, long-horizon]
  robot_platform: ByteMini bimanual mobile robot
  uses_real_robot: yes
  uses_humanoid: yes (mobile humanoid-style)
  uses_simulation: no
  code_status: 🌐 Project Page only
  why_it_matters: Outperforms π0 on dexterous long-horizon tasks; integrates web VLM, VR-collected human data, and robot data.

- title: RDT-1B — A Diffusion Foundation Model for Bimanual Manipulation
  authors: Songming Liu, Lingxuan Wu, Bangguo Yu, ... Jun Zhu (Tsinghua)
  year: 2024
  venue: ICLR 2025
  arxiv_id: 2410.07864
  paper_url: https://arxiv.org/abs/2410.07864
  project_url: https://rdt-robotics.github.io/
  code_url: https://github.com/thu-ml/RoboticsDiffusionTransformer
  category: Foundation
  task_tags: [diffusion-transformer, 1.2B-params, bimanual, 46-datasets-pretrain]
  robot_platform: ALOHA bimanual + others (46 datasets)
  uses_real_robot: yes
  uses_humanoid: yes (bimanual)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (HF)
  why_it_matters: Largest open diffusion-based VLA; standard bimanual humanoid baseline.

- title: HPT — Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers
  authors: Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He
  year: 2024
  venue: NeurIPS 2024 (Spotlight)
  arxiv_id: 2409.20537
  paper_url: https://arxiv.org/abs/2409.20537
  project_url: https://liruiw.github.io/hpt/
  code_url: https://github.com/liruiw/HPT
  category: Foundation
  task_tags: [stem-trunk-head, 50-datasets, cross-embodiment, scaling-laws]
  robot_platform: 50+ datasets / many embodiments
  uses_real_robot: yes
  uses_humanoid: yes (in mixture)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Demonstrates clean scaling laws for cross-embodiment policy backbones.

- title: SpatialVLA — Exploring Spatial Representations for Visual-Language-Action Model
  authors: Delin Qu, Haoming Song, Qizhi Chen, ... (Shanghai AI Lab)
  year: 2025
  venue: RSS 2025
  arxiv_id: 2501.15830
  paper_url: https://arxiv.org/abs/2501.15830
  project_url: https://spatialvla.github.io/
  code_url: https://github.com/SpatialVLA/SpatialVLA
  category: VLA
  task_tags: [Ego3D-PE, adaptive-action-grids, 1.1M-episodes, spatial]
  robot_platform: WidowX, Franka, multi-platform
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Inject 3D priors into VLA; strong out-of-distribution spatial generalization.

- title: NORA — A Small Open-Sourced Generalist Vision Language Action Model
  authors: Chia-Yu Hung, Qi Sun, Pengfei Hong, ... Soujanya Poria (DeCLaRe Lab)
  year: 2025
  venue: arXiv (Apr 2025)
  arxiv_id: 2504.19854
  paper_url: https://arxiv.org/abs/2504.19854
  project_url: https://declare-lab.github.io/nora
  code_url: https://github.com/declare-lab/nora
  category: VLA
  task_tags: [3B-Qwen2.5VL, FAST+-tokenizer, edge-friendly]
  robot_platform: WidowX, real-world tasks
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (MIT)
  why_it_matters: Compact 3B VLA — practical for low-power on-board humanoid deployment.

- title: AgiBot World Colosseo + GO-1 — Large-scale Manipulation Platform
  authors: AgiBot Team / OpenDriveLab
  year: 2025
  venue: IROS 2025 / IEEE T-RO 2026
  arxiv_id: 2503.06669
  paper_url: https://arxiv.org/abs/2503.06669
  project_url: https://agibot-world.com/
  code_url: https://github.com/OpenDriveLab/AgiBot-World
  category: Foundation / Dataset
  task_tags: [1M-trajectories, 217-tasks, ViLLA, latent-action, humanoid]
  robot_platform: AgiBot mobile humanoid (whole-body, dexterous hands, tactile)
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Dataset (CC BY-NC-SA) + GO-1 weights
  why_it_matters: Largest open humanoid manipulation dataset; GO-1 ViLLA framework beats RDT by 32%.

- title: X-VLA — Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model
  authors: Jinliang Zheng, Jianxiong Li, ... (2toinf)
  year: 2025
  venue: ICLR 2026
  arxiv_id: 2510.10274
  paper_url: https://arxiv.org/abs/2510.10274
  project_url: https://2toinf.github.io/X-VLA/
  code_url: https://github.com/2toinf/X-VLA
  category: VLA
  task_tags: [flow-matching, soft-prompts, cross-embodiment, 290K-episodes]
  robot_platform: 7 platforms incl. Droid, Robomind, AgiBot
  uses_real_robot: yes
  uses_humanoid: yes (AgiBot)
  uses_simulation: yes
  code_status: ⭐ Code (ICLR 2026)
  why_it_matters: Won AgiBot World Challenge @ IROS 2025; minimal-parameter cross-embodiment recipe.

- title: WholeBodyVLA — Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control
  authors: OpenDriveLab Team
  year: 2025
  venue: ICLR 2026
  arxiv_id: 2512.11047
  paper_url: https://arxiv.org/abs/2512.11047
  project_url: https://opendrivelab.com/WholeBodyVLA/
  code_url: https://github.com/OpenDriveLab/WholebodyVLA
  category: Foundation
  task_tags: [whole-body, loco-manipulation, latent-action, RL-low-level, action-free-video]
  robot_platform: AgiBot X2 humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ⭐ Code (ICLR 2026)
  why_it_matters: Among the first unified VLA frameworks for humanoid loco-manipulation (push 50kg cart, squat-grasp).

- title: Humanoid-VLA — Towards Universal Humanoid Control with Visual Integration
  authors: Pengxiang Ding, Jianfei Ma, ... (multi-institution)
  year: 2025
  venue: arXiv (Feb 2025)
  arxiv_id: 2502.14795
  paper_url: https://arxiv.org/abs/2502.14795
  project_url: ""
  code_url: ""
  category: Foundation
  task_tags: [language-motion-pretrain, egocentric-video, humanoid, motion-control]
  robot_platform: Humanoid (paper-described)
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ❌ No Code Found
  why_it_matters: Multi-stage humanoid VLA recipe: language-motion pre-align → egocentric vision tuning.

- title: LeVERB — Humanoid Whole-Body Control with Latent Vision-Language Instruction
  authors: Haoru Xue, Xiaoyu Huang, ... S. Shankar Sastry, Koushil Sreenath (UC Berkeley)
  year: 2025
  venue: arXiv (Jun 2025) — CoRL 2025
  arxiv_id: 2506.13751
  paper_url: https://arxiv.org/abs/2506.13751
  project_url: https://ember-lab-berkeley.github.io/LeVERB-Webpage/
  code_url: https://github.com/EmberLab/LeVERB
  category: Foundation
  task_tags: [hierarchical, latent-verbs, sim-to-real, RL-WBC, benchmark]
  robot_platform: Humanoid (Unitree H1-style sim-to-real ready)
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: 🧩 Partial Code + 🌐 Project Page (benchmark released)
  why_it_matters: First sim-to-real-ready closed-loop vision-language WBC benchmark for humanoids.

- title: Humanoid Policy ~ Human Policy (HAT / PH2D)
  authors: Ri-Zhao Qiu, Shiqi Yang, Xuxin Cheng, ... Xiaolong Wang
  year: 2025
  venue: arXiv (Mar 2025)
  arxiv_id: 2503.13441
  paper_url: https://arxiv.org/abs/2503.13441
  project_url: https://human-as-robot.github.io/
  code_url: https://github.com/RogerQi/human-policy
  category: Generalist-Policy
  task_tags: [VR-egocentric, human-data, HAT-transformer, cross-embodiment]
  robot_platform: Unitree H1 humanoid + dexterous hands; human VR data
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: ⭐ Code + 📦 Dataset (PH2D)
  why_it_matters: Human and humanoid trained as a single embodiment via shared state-action space.

- title: EgoVLA — Learning VLA Models from Egocentric Human Videos
  authors: Ruihan Yang, Qinxi Yu, Yecheng Jason Ma, Xiaolong Wang
  year: 2025
  venue: arXiv (Jul 2025)
  arxiv_id: 2507.12440
  paper_url: https://arxiv.org/abs/2507.12440
  project_url: https://rchalyang.github.io/EgoVLA/
  code_url: ""
  category: VLA
  task_tags: [egocentric, IK-retargeting, Ego-Humanoid-Manipulation-Benchmark]
  robot_platform: Unitree H1 + Inspire dexterous hands
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: 🌐 Project Page (benchmark + dataset planned)
  why_it_matters: Builds humanoid VLA directly from internet-scale egocentric human video.

- title: EgoZero — Robot Learning from Smart Glasses
  authors: Vincent Liu, Ademi Adeniji, Haotian Fu, Lerrel Pinto
  year: 2025
  venue: arXiv (May 2025)
  arxiv_id: 2505.20290
  paper_url: https://arxiv.org/abs/2505.20290
  project_url: https://egozero-robot.github.io/
  code_url: https://github.com/vliu15/egozero
  category: Generalist-Policy
  task_tags: [Project-Aria, zero-robot-data, 3D-points, morphology-agnostic]
  robot_platform: Franka Panda gripper
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: ⭐ Code
  why_it_matters: Learns deployable policies from smart-glasses human demos with zero robot data.

- title: Robotic Control via Embodied Chain-of-Thought Reasoning (ECoT)
  authors: Michał Zawalski, William Chen, Karl Pertsch, ... Sergey Levine
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.08693
  paper_url: https://arxiv.org/abs/2407.08693
  project_url: https://embodied-cot.github.io/
  code_url: https://github.com/MichalZawalski/embodied-CoT
  category: VLA
  task_tags: [chain-of-thought, OpenVLA, plans+bbox+motion-primitives]
  robot_platform: WidowX (BridgeData V2)
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Dataset (HF)
  why_it_matters: +28% absolute success on OpenVLA via interleaved embodied reasoning.

- title: RoboBrain — A Unified Brain Model for Robotic Manipulation
  authors: Yuheng Ji, Huajie Tan, ... (BAAI / FlagOpen)
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2502.21257
  paper_url: https://arxiv.org/abs/2502.21257
  project_url: https://superrobobrain.github.io/
  code_url: https://github.com/FlagOpen/RoboBrain
  category: Foundation
  task_tags: [planning, affordance, trajectory, ShareRobot-dataset]
  robot_platform: Multi-platform manipulation
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights + 📦 Dataset
  why_it_matters: Unified MLLM-based "robotic brain" for high-level planning, affordance and trajectory prediction.

- title: NaVILA — Legged Robot VLA Model for Navigation
  authors: An-Chieh Cheng, Yandong Ji, ... Xiaolong Wang (NVIDIA + UCSD)
  year: 2024
  venue: RSS 2025
  arxiv_id: 2412.04453
  paper_url: https://arxiv.org/abs/2412.04453
  project_url: https://navila-bot.github.io/
  code_url: https://github.com/AnjieCheng/NaVILA
  category: VLA
  task_tags: [VLN, mid-level-action, locomotion-RL, humanoid+quadruped]
  robot_platform: Unitree humanoid + quadruped
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ⭐ Code (NaVILA)
  why_it_matters: Foundational navigation VLA for both humanoids and quadrupeds.

- title: Helix — A VLA Model for Generalist Humanoid Control
  authors: Figure AI Research Team
  year: 2025
  venue: Figure AI Tech Report (Feb 2025)
  arxiv_id: ""
  paper_url: https://www.figure.ai/news/helix
  project_url: https://www.figure.ai/helix
  code_url: ""
  category: Foundation
  task_tags: [System1+System2, 35-DoF, 200Hz, on-device, dual-robot]
  robot_platform: Figure 02 humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: ❌ No Code Found (proprietary)
  why_it_matters: First commercial humanoid upper-body VLA running fully on-board low-power GPUs.

- title: 1X World Model — Evaluating Bits, Not Atoms
  authors: 1X Technologies World Model Team
  year: 2024
  venue: 1X Tech Report; 2024–2026 release cycle
  arxiv_id: ""
  paper_url: https://www.1x.tech/1x-world-model.pdf
  project_url: https://www.1x.tech/discover/1x-world-model
  code_url: https://github.com/1x-technologies/1xgpt
  category: Foundation (World Model)
  task_tags: [world-model, video-prediction, EVE, NEO, evaluation-platform]
  robot_platform: 1X EVE / NEO humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: 🧩 Partial Code (1xgpt challenge code) + 📦 Dataset
  why_it_matters: First contact-rich whole-body humanoid world model with public evaluation challenge.

- title: Cosmos World Foundation Model Platform for Physical AI
  authors: NVIDIA Cosmos Team
  year: 2025
  venue: arXiv (Jan 2025)
  arxiv_id: 2501.03575
  paper_url: https://arxiv.org/abs/2501.03575
  project_url: https://www.nvidia.com/en-us/ai/cosmos/
  code_url: https://github.com/nvidia-cosmos/cosmos-predict2.5
  category: Foundation (World Model)
  task_tags: [world-foundation-model, video-diffusion, autoregressive, tokenizers]
  robot_platform: Multi-domain physical AI (robots, AVs)
  uses_real_robot: yes
  uses_humanoid: yes (humanoid use cases)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (NVIDIA Open Model License)
  why_it_matters: Backbone world model for synthetic data and policy evaluation in humanoid pipelines.

- title: Cosmos-Reason1 — From Physical Common Sense to Embodied Reasoning
  authors: NVIDIA Cosmos Team
  year: 2025
  venue: arXiv (Mar 2025)
  arxiv_id: 2503.15558
  paper_url: https://arxiv.org/abs/2503.15558
  project_url: https://research.nvidia.com/labs/dir/cosmos-reason1/
  code_url: https://github.com/nvidia-cosmos/cosmos-reason1
  category: Foundation
  task_tags: [physical-common-sense, embodied-reasoning, 7B+56B, CoT, RL]
  robot_platform: General physical AI agents
  uses_real_robot: no (reasoning model)
  uses_humanoid: yes (downstream)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Pluggable physical-AI System-2 reasoning model used inside Cosmos-Predict2.5 and many humanoid stacks.

- title: Cosmos-Predict2 / 2.5 — World Simulation with Video Foundation Models for Physical AI
  authors: NVIDIA Cosmos Team
  year: 2025
  venue: arXiv (Nov 2025)
  arxiv_id: 2511.00062
  paper_url: https://arxiv.org/abs/2511.00062
  project_url: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1/
  code_url: https://github.com/nvidia-cosmos/cosmos-predict2.5
  category: Foundation (World Model)
  task_tags: [text2world, image2world, video2world, flow-matching, 2B+14B]
  robot_platform: Generic physical AI
  uses_real_robot: yes (eval)
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Latest unified video world-model used as humanoid policy evaluator and synthetic-data engine.

- title: Cosmos Policy — Fine-Tuning Video Models for Visuomotor Control and Planning
  authors: NVIDIA Research
  year: 2026
  venue: arXiv (Jan 2026)
  arxiv_id: 2601.16163
  paper_url: https://arxiv.org/abs/2601.16163
  project_url: ""
  code_url: https://github.com/nv-tlabs/cosmos-policy
  category: Generalist-Policy
  task_tags: [video-foundation-model, LIBERO, RoboCasa, visuomotor]
  robot_platform: LIBERO, RoboCasa simulators
  uses_real_robot: no
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Demonstrates Cosmos video models fine-tuned directly into actionable robot policies.

- title: ALOHA Unleashed — A Simple Recipe for Robot Dexterity
  authors: Tony Z. Zhao, Jonathan Tompson, Danny Driess, ... Pierre Sermanet
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2410.13126
  paper_url: https://arxiv.org/abs/2410.13126
  project_url: https://aloha-unleashed.github.io/
  code_url: https://github.com/google-deepmind/aloha_unleashed
  category: Generalist-Policy
  task_tags: [diffusion, transformer, ALOHA-2, 26k-demos, deformables]
  robot_platform: ALOHA 2 bimanual
  uses_real_robot: yes
  uses_humanoid: yes (bimanual)
  uses_simulation: yes
  code_status: 🧩 Partial (sim envs released)
  why_it_matters: Strong dexterous bimanual baseline (shoe-tying, shirt-hanging) for humanoid arm benchmarks.

- title: ACT — Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA)
  authors: Tony Z. Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn
  year: 2023
  venue: RSS 2023
  arxiv_id: 2304.13705
  paper_url: https://arxiv.org/abs/2304.13705
  project_url: https://tonyzhaozh.github.io/aloha/
  code_url: https://github.com/tonyzhaozh/act
  category: Generalist-Policy
  task_tags: [action-chunking, CVAE, bimanual, low-cost]
  robot_platform: ALOHA bimanual
  uses_real_robot: yes
  uses_humanoid: yes (bimanual)
  uses_simulation: no
  code_status: ⭐ Code
  why_it_matters: Foundational action-chunking architecture used in nearly every bimanual humanoid VLA.

- title: Diffusion Policy — Visuomotor Policy Learning via Action Diffusion
  authors: Cheng Chi, Siyuan Feng, Yilun Du, ... Shuran Song
  year: 2023
  venue: RSS 2023; IJRR 2024
  arxiv_id: 2303.04137
  paper_url: https://arxiv.org/abs/2303.04137
  project_url: https://diffusion-policy.cs.columbia.edu/
  code_url: https://github.com/real-stanford/diffusion_policy
  category: Generalist-Policy
  task_tags: [diffusion, multimodal, visuomotor, foundation-baseline]
  robot_platform: Multiple manipulation platforms
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: The diffusion-policy foundation that underpins π0, RDT, ALOHA-Unleashed, OFT.

- title: TinyVLA — Towards Fast, Data-Efficient Vision-Language-Action Models
  authors: Junjie Wen, Yichen Zhu, ... (Midea Group / SJTU)
  year: 2024
  venue: RA-L 2025
  arxiv_id: 2409.12514
  paper_url: https://arxiv.org/abs/2409.12514
  project_url: https://tiny-vla.github.io/
  code_url: https://github.com/lesjie-wen/tinyvla
  category: VLA
  task_tags: [<1B-VLM, diffusion-head, edge, fast]
  robot_platform: Franka, real-world tasks
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Compact VLA (>5× smaller than OpenVLA) with higher success — practical humanoid edge deployment.

- title: DexVLA — Vision-Language Model with Plug-In Diffusion Expert
  authors: Junjie Wen, Yichen Zhu, ... (Midea Group)
  year: 2025
  venue: arXiv (Feb 2025)
  arxiv_id: 2502.05855
  paper_url: https://arxiv.org/abs/2502.05855
  project_url: https://dex-vla.github.io/
  code_url: https://github.com/juruobenruo/DexVLA
  category: VLA
  task_tags: [diffusion-expert, 1B-action, cross-embodiment, dexterous]
  robot_platform: Multiple bimanual / dexterous platforms
  uses_real_robot: yes
  uses_humanoid: yes (bimanual)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Plug-in 1B diffusion expert into VLM — directly relevant for humanoid bimanual dexterity.

- title: DexGraspVLA — A VLA Framework Towards General Dexterous Grasping
  authors: Yifan Zhong, Xuchuan Huang, Ruochong Li, ... (Psi-Robot)
  year: 2025
  venue: AAAI 2026 Oral
  arxiv_id: 2502.20900
  paper_url: https://arxiv.org/abs/2502.20900
  project_url: https://dexgraspvla.github.io/
  code_url: https://github.com/Psi-Robot/DexGraspVLA
  category: VLA
  task_tags: [hierarchical, dexterous-hand, zero-shot, cluttered-scenes]
  robot_platform: Dexterous hands (relevant to humanoid)
  uses_real_robot: yes
  uses_humanoid: yes (hands)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: 90+% zero-shot dexterous grasping on thousands of unseen cluttered scenes.

- title: GraspVLA — A Grasping Foundation Model Pre-trained on Billion-Scale Synthetic Action Data
  authors: GalaxeaAI
  year: 2025
  venue: arXiv (May 2025)
  arxiv_id: 2505.03233
  paper_url: https://arxiv.org/abs/2505.03233
  project_url: https://pku-epic.github.io/GraspVLA-web/
  code_url: https://github.com/PKU-EPIC/GraspVLA
  category: Foundation
  task_tags: [SynGrasp-1B, flow-matching, progressive-action-generation]
  robot_platform: Multi-arm, multi-gripper
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights + 📦 Dataset (synthetic)
  why_it_matters: Demonstrates billion-scale synthetic-action pretraining is sufficient for grasping foundation models.

- title: WorldVLA — Towards Autoregressive Action World Model
  authors: Jun Cen, Chaohui Yu, Hangjie Yuan, ...
  year: 2025
  venue: arXiv (Jun 2025)
  arxiv_id: 2506.21539
  paper_url: https://arxiv.org/abs/2506.21539
  project_url: https://github.com/alibaba-damo-academy/WorldVLA
  code_url: https://github.com/alibaba-damo-academy/WorldVLA
  category: Foundation
  task_tags: [autoregressive, world-model+VLA, image+action-tokens]
  robot_platform: LIBERO + real
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code
  why_it_matters: Unifies action prediction and world prediction in one autoregressive transformer.

- title: Dita — Scaling Diffusion Transformer for Generalist VLA Policy
  authors: Zhi Hou, Tianyi Zhang, ... (Shanghai AI Lab)
  year: 2025
  venue: ICCV 2025
  arxiv_id: 2503.19757
  paper_url: https://arxiv.org/abs/2503.19757
  project_url: https://robodita.github.io/
  code_url: https://github.com/RoboDita/Dita
  category: Generalist-Policy
  task_tags: [diffusion-transformer, in-context-conditioning, 334M, OXE-pretrain]
  robot_platform: Multiple OXE platforms
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Lightweight (334M) but scalable DiT-style generalist VLA — strong long-horizon performance.

- title: InternVLA-M1 — A Spatially Guided VLA Framework for Generalist Robot Policy
  authors: InternRobotics Team (Shanghai AI Lab)
  year: 2025
  venue: arXiv (Oct 2025)
  arxiv_id: 2510.13778
  paper_url: https://arxiv.org/abs/2510.13778
  project_url: https://internrobotics.github.io/internvla-m1.github.io/
  code_url: https://github.com/InternRobotics/InternVLA-M1
  category: VLA
  task_tags: [spatial-grounding, 2.3M-spatial-data, language+action-heads]
  robot_platform: SimplerEnv, WidowX, LIBERO Franka, real
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Spatial grounding as the bridge between instructions and embodiment-aware actions.

- title: MoManipVLA — Transferring VLA Models for General Mobile Manipulation
  authors: Zhenyu Wu, Yuheng Zhou, ... (BUPT / NTU / Tsinghua)
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2503.13446
  paper_url: https://arxiv.org/abs/2503.13446
  project_url: https://gary3410.github.io/momanipVLA/
  code_url: ""
  category: VLA
  task_tags: [mobile-manipulation, bilevel-optimization, OVMM]
  robot_platform: Mobile manipulators (humanoid-relevant)
  uses_real_robot: yes
  uses_humanoid: yes (mobile)
  uses_simulation: yes
  code_status: 🌐 Project Page
  why_it_matters: Adapts fixed-base VLAs to mobile humanoid loco-manipulation via bilevel waypoint optimization.

- title: MotionGPT — Human Motion as a Foreign Language
  authors: Biao Jiang, Xin Chen, Wen Liu, ... (Fudan / Tencent)
  year: 2023
  venue: NeurIPS 2023
  arxiv_id: 2306.14795
  paper_url: https://arxiv.org/abs/2306.14795
  project_url: https://motion-gpt.github.io/
  code_url: https://github.com/OpenMotionLab/MotionGPT
  category: Foundation (Motion)
  task_tags: [VQ-VAE, motion-tokens, T5, generation+understanding]
  robot_platform: Human motion (retargettable to humanoid)
  uses_real_robot: no
  uses_humanoid: yes (motion)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights
  why_it_matters: Foundational motion-language model used by retargeting pipelines feeding humanoid VLAs.

- title: MotionGPT-2 — A General-Purpose Motion-Language Model for Motion Generation and Understanding
  authors: Yuan Wang, Di Huang, ... (Fudan)
  year: 2024
  venue: arXiv (Oct 2024)
  arxiv_id: 2410.21747
  paper_url: https://arxiv.org/abs/2410.21747
  project_url: ""
  code_url: ""
  category: Foundation (Motion)
  task_tags: [Part-Aware-VQVAE, holistic-3D-motion, multimodal]
  robot_platform: Human motion
  uses_real_robot: no
  uses_humanoid: yes (motion)
  uses_simulation: yes
  code_status: ❌ No Code Found
  why_it_matters: Holistic body+hand motion-language model — input modality for humanoid skill libraries.

- title: FAST — Efficient Action Tokenization for Vision-Language-Action Models
  authors: Karl Pertsch, Kyle Stachowicz, Brian Ichter, ... Sergey Levine (Physical Intelligence)
  year: 2025
  venue: arXiv (Jan 2025)
  arxiv_id: 2501.09747
  paper_url: https://arxiv.org/abs/2501.09747
  project_url: https://www.pi.website/research/fast
  code_url: https://github.com/Physical-Intelligence/openpi
  category: VLA (component)
  task_tags: [DCT, BPE, action-tokenizer, autoregressive]
  robot_platform: Multi-platform (used as universal tokenizer)
  uses_real_robot: yes
  uses_humanoid: yes (downstream)
  uses_simulation: yes
  code_status: ⭐ Code + 📦 Weights (FAST+ universal tokenizer on HF)
  why_it_matters: Drop-in tokenizer used by NORA, π0-FAST, GR00T, and many subsequent VLAs.

- title: Gemini Robotics — Bringing AI into the Physical World (incl. Robotics-ER, 1.5, On-Device)
  authors: Google DeepMind Robotics Team
  year: 2025
  venue: arXiv (Mar 2025)
  arxiv_id: 2503.20020
  paper_url: https://arxiv.org/abs/2503.20020
  project_url: https://deepmind.google/models/gemini-robotics/
  code_url: ""
  category: Foundation
  task_tags: [Gemini-2.0-VLA, ER-reasoning, multi-embodiment, Apptronik-Apollo]
  robot_platform: Apollo humanoid (Apptronik), bimanual arms
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: ❌ No Code Found (closed)
  why_it_matters: Frontier closed humanoid VLA from DeepMind — partner for Apptronik Apollo.

- title: MolmoAct 2 — Action Reasoning Models for Real-world Deployment
  authors: Haoquan Fang; Jiafei Duan; Donovan Clay; Sam Wang; Shuo Liu; Weikai Huang; Xiang Fan; Wei-Chuan Tsai; Shirui Chen; Yi Ru Wang; Shanli Xing; Jaemin Cho; Jae Sung Park; Ainaz Eftekhar; Peter Sushko; Karen Farley; Angad Wadhwa; Cole Harrison; Winson Han; Ying-Chun Lee; Eli VanderBilt; Rose Hendrix; Suveen Ellawela; Lucas Ngoo; Joyce Chai; Zhongzheng Ren; Ali Farhadi; Dieter Fox; Ranjay Krishna
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.02881
  paper_url: https://arxiv.org/abs/2605.02881
  project_url: https://allenai.org/blog/molmoact2
  code_url: https://github.com/allenai/molmoact2
  category: Foundation
  task_tags: [action-reasoning, VLA, MolmoER, OpenFAST, MolmoThink, bimanual, LIBERO, DROID]
  robot_platform: Franka, SO100/SO101, bimanual YAM
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: 🧩 Partial Code
  one_line: Open VLA stack with MolmoER backbone, OpenFAST action tokenizer, MolmoThink adaptive-reasoning variant, and 720h bimanual dataset.
  why_it_matters: AI2/UW fully-open follow-up to MolmoAct competing with Pi-05 and Gemini Robotics ER-1.5; weights and datasets released, training code staged.

---

## Quick stats
- 41 papers covered (target was 25–40).
- 28 papers with ⭐ full code; 5 partial; 4 project-page only; 4 closed.
- Years: 2022 (1), 2023 (4), 2024 (10), 2025 (24), 2026 (2 — Cosmos Policy, ICLR/AAAI 2026 entries).
- Humanoid-specific (whole-body / bimanual): GR00T, Helix, AgiBot World+GO-1, WholeBodyVLA, Humanoid-VLA, LeVERB, EgoVLA, Humanoid Policy~Human Policy, NaVILA, Gemini Robotics, ALOHA Unleashed, ACT, RDT-1B, DexVLA, DexGraspVLA, MoManipVLA, OFT+, MotionGPT(-2), 1X World Model, GR-3.
