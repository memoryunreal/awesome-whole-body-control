# Whole-Body Motion Tracking and Imitation (Humanoid Robots & Physics-Based Characters)

Curated 2022-2026 with priority on 2024-2026.
Code-status legend: ⭐ Code | 🧩 Partial Code | 📦 Dataset | 🌐 Project Page | ⏳ Code Coming Soon | 🔁 Unofficial Code | ❌ No Code Found.

---

## Foundational Physics-Based Character Animation (2018-2023)

- title: DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills
  authors: Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne
  year: 2018
  venue: SIGGRAPH 2018 (TOG)
  arxiv_id: 1804.02717
  paper_url: https://arxiv.org/abs/1804.02717
  project_url: https://xbpeng.github.io/projects/DeepMimic/index.html
  code_url: https://github.com/xbpeng/DeepMimic
  category: Motion-Imitation
  task_tags: [RL, motion-imitation, character-anim, PPO, reference-state-init]
  robot_platform: SMPL/Mujoco humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Foundational RL framework for imitating mocap clips on simulated characters with reference state initialization and early termination.
  why_it_matters: Established the dominant motion-tracking RL recipe used by virtually all later humanoid-tracking papers.

- title: AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control
  authors: Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
  year: 2021
  venue: SIGGRAPH 2021 (TOG)
  arxiv_id: 2104.02180
  paper_url: https://arxiv.org/abs/2104.02180
  project_url: https://xbpeng.github.io/projects/AMP/index.html
  code_url: https://github.com/xbpeng/MimicKit
  category: Motion-Imitation
  task_tags: [adversarial-imitation, GAN-style, character-anim, motion-prior]
  robot_platform: simulated character
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Replaces hand-crafted imitation rewards with an adversarial discriminator that scores motion realism vs. an unstructured mocap dataset.
  why_it_matters: Foundational style/motion prior used as a building block in countless humanoid RL pipelines (incl. legged locomotion).

- title: ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters
  authors: Xue Bin Peng, Yunrong Guo, Lina Halper, Sergey Levine, Sanja Fidler
  year: 2022
  venue: SIGGRAPH 2022 (TOG)
  arxiv_id: 2205.01906
  paper_url: https://arxiv.org/abs/2205.01906
  project_url: https://research.nvidia.com/labs/toronto-ai/ASE/
  code_url: https://github.com/nv-tlabs/ASE
  category: Motion-Imitation
  task_tags: [skill-embedding, adversarial, character-anim, hierarchical-RL]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Learns a reusable latent skill embedding from large unstructured mocap that downstream tasks can sample for diverse behaviors.
  why_it_matters: Cornerstone of the "skill latent" paradigm; directly inspired CALM, NCP, PULSE, MaskedMimic.

- title: CALM: Conditional Adversarial Latent Models for Directable Virtual Characters
  authors: Chen Tessler, Yoni Kasten, Yunrong Guo, Shie Mannor, Gal Chechik, Xue Bin Peng
  year: 2023
  venue: SIGGRAPH 2023
  arxiv_id: 2305.02195
  paper_url: https://arxiv.org/abs/2305.02195
  project_url: https://research.nvidia.com/labs/par/calm/
  code_url: https://github.com/NVlabs/CALM
  category: Motion-Imitation
  task_tags: [skill-latent, character-anim, directable, adversarial]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Learns a conditional latent that lets a user direct character style and motion while preserving diversity.
  why_it_matters: Bridge between ASE-style skill embeddings and modern controllable generative motion controllers.

- title: PHC: Perpetual Humanoid Control for Real-time Simulated Avatars
  authors: Zhengyi Luo, Jinkun Cao, Alexander Winkler, Kris Kitani, Weipeng Xu
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2305.06456
  paper_url: https://arxiv.org/abs/2305.06456
  project_url: https://www.zhengyiluo.com/PHC-Site/
  code_url: https://github.com/ZhengyiLuo/PHC
  category: Motion-Imitation
  task_tags: [motion-imitation, AMASS, fail-recovery, progressive-policy, character-anim]
  robot_platform: SMPL humanoid (Isaac Gym)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: A single physics-based controller that imitates ~10K AMASS motions and recovers from arbitrary fail states without external forces.
  why_it_matters: Pre-trained PHC checkpoints became a de-facto teacher for almost every humanoid sim2real tracking paper (H2O, OmniH2O, HOVER, ASAP, ExBody2).

- title: PULSE: Universal Humanoid Motion Representations for Physics-Based Control
  authors: Zhengyi Luo, Jinkun Cao, Josh Merel, Alexander Winkler, Jing Huang, Kris Kitani, Weipeng Xu
  year: 2024
  venue: ICLR 2024 (Spotlight)
  arxiv_id: 2310.04582
  paper_url: https://arxiv.org/abs/2310.04582
  project_url: http://www.zhengyiluo.com/PULSE/
  code_url: https://github.com/ZhengyiLuo/PULSE
  category: Motion-Imitation
  task_tags: [motion-latent, VAE, hierarchical-RL, character-anim]
  robot_platform: SMPL humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Distills PHC into a 32-D variational motion latent that covers 99.8% of AMASS and serves as a foundation prior for downstream hierarchical RL.
  why_it_matters: The "GPT for motor control" baseline; widely reused as a frozen prior for downstream humanoid tasks.

- title: Universal Humanoid Controller (UHC) — Kinpoly / EmbodiedPose
  authors: Zhengyi Luo, Ryo Hachiuma, Ye Yuan, Kris Kitani
  year: 2021/2022
  venue: NeurIPS 2021 / NeurIPS 2022
  arxiv_id: 2106.05969
  paper_url: https://arxiv.org/abs/2106.05969
  project_url: https://zhengyiluo.github.io/projects/kin_poly/
  code_url: https://github.com/ZhengyiLuo/UHC
  category: Motion-Imitation
  task_tags: [motion-imitation, mujoco, ego-pose, character-anim]
  robot_platform: Mujoco humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Task-agnostic motion imitator that takes only reference frames as input; precursor to PHC.
  why_it_matters: Set the template for "single network tracks any AMASS clip" before PHC scaled it.

- title: NCP: Neural Categorical Priors for Physics-Based Character Control
  authors: Qingxu Zhu, He Zhang, Mengting Lan, Lei Han
  year: 2023
  venue: SIGGRAPH Asia 2023
  arxiv_id: 2308.07200
  paper_url: https://arxiv.org/abs/2308.07200
  project_url: https://tencent-roboticsx.github.io/NCP/
  code_url: https://github.com/Tencent-RoboticsX/NCP
  category: Motion-Imitation
  task_tags: [skill-latent, VQ-VAE, discrete-prior, character-anim]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Compresses motion clips into a discrete VQ codebook with a learned categorical prior for generation and downstream RL.
  why_it_matters: Strong alternative to ASE/CALM continuous latents; influential on later VQ-based humanoid controllers.

- title: MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control
  authors: Nolan Wagener, Andrey Kolobov, Felipe Vieira Frujeri, Ricky Loynd, Ching-An Cheng, Matthew Hausknecht
  year: 2022
  venue: NeurIPS 2022 (Datasets)
  arxiv_id: 2208.07363
  paper_url: https://arxiv.org/abs/2208.07363
  project_url: https://microsoft.github.io/MoCapAct/
  code_url: https://github.com/microsoft/MoCapAct
  category: Motion-Imitation
  task_tags: [dataset, dm_control, multi-task, character-anim]
  robot_platform: dm_control humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: 3+ hours of expert tracking rollouts for 2,000+ MoCap clips on the dm_control humanoid.
  why_it_matters: Enables downstream policy/VAE work without retraining low-level trackers.

- title: H-GAP: Humanoid Control with a Generalist Planner
  authors: Zhengyi Jiang, Yueh-Hua Wu, Yi Wu, Pieter Abbeel
  year: 2024
  venue: ICLR 2024
  arxiv_id: 2312.02682
  paper_url: https://arxiv.org/abs/2312.02682
  project_url: https://ycxia.github.io/H-GAP/
  code_url: https://github.com/facebookresearch/hgap
  category: Motion-Imitation
  task_tags: [generative-planner, MPC, dm_control, transformer]
  robot_platform: 56-DoF dm_control humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Trajectory-level autoencoding planner trained on MoCapAct, used with MPC at test time to solve novel tasks zero-shot.
  why_it_matters: Demonstrates planning over learned motion priors as an alternative to hierarchical RL.

- title: VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters
  authors: Agon Serifi et al. (Disney Research)
  year: 2024
  venue: SCA 2024 (Computer Graphics Forum)
  arxiv_id: ""
  paper_url: https://la.disneyresearch.com/wp-content/uploads/VMP_paper.pdf
  project_url: https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/
  code_url: ""
  category: Motion-Imitation
  task_tags: [VAE, motion-prior, sim2real, bipedal]
  robot_platform: simulated character + bipedal robot
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Two-stage VAE+policy framework that produces a versatile motion prior transferable to a real bipedal robot.
  why_it_matters: One of the first physics-based-character priors validated on hardware (Disney bipedal).

- title: MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting
  authors: Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, Xue Bin Peng
  year: 2024
  venue: SIGGRAPH Asia 2024
  arxiv_id: 2409.14393
  paper_url: https://arxiv.org/abs/2409.14393
  project_url: https://research.nvidia.com/labs/par/maskedmimic/
  code_url: https://github.com/NVlabs/ProtoMotions
  category: Motion-Imitation
  task_tags: [unified-control, masked-motion, inpainting, multi-modal, character-anim]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Single transformer controller that solves tracking, joystick, keyframe, text, and object-interaction control via masked motion inpainting.
  why_it_matters: State-of-the-art unified character controller; ships inside ProtoMotions and used as humanoid-robot teacher.

- title: ProtoMotions
  authors: NVIDIA Spatial Intelligence Lab (NVlabs)
  year: 2024-2026
  venue: Open-source framework
  arxiv_id: ""
  paper_url: https://nvlabs.github.io/ProtoMotions/
  project_url: https://github.com/NVlabs/ProtoMotions
  code_url: https://github.com/NVlabs/ProtoMotions
  category: Motion-Imitation
  task_tags: [framework, IsaacGym, IsaacLab, Genesis, Newton, AMP, ASE, MaskedMimic]
  robot_platform: SMPL / G1 / multi-robot
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: GPU-accelerated framework unifying physics-based character animation, digital humans, and humanoid robotics with shared infra.
  why_it_matters: Reference codebase for AMP/ASE/MaskedMimic + zero-shot transfer of MaskedMimic policy to Unitree G1.

- title: SkillMimic: Learning Reusable Basketball Skills from Demonstrations
  authors: Yinhuai Wang, Qihan Zhao, Runyi Yu, Hok Wai Tsui, Ying Shan, Jianbo Liu
  year: 2024
  venue: arXiv 2024.08
  arxiv_id: 2408.15270
  paper_url: https://arxiv.org/abs/2408.15270
  project_url: https://ingrid789.github.io/SkillMimic/
  code_url: https://github.com/wyhuai/SkillMimic
  category: Motion-Imitation
  task_tags: [object-interaction, sports, character-anim, skill-reuse]
  robot_platform: simulated humanoid + ball
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified config to learn dribbling/layups/shooting from demonstrations; high-level controller composes acquired skills.
  why_it_matters: Motion-imitation extended to physical object interaction; precursor to MaskedManipulator and SkillMimic-V2.

- title: SkillMimic-V2: Learning Robust and Generalizable Interaction Skills from Sparse and Noisy Demonstrations
  authors: Runyi Yu, Yinhuai Wang, Qihan Zhao, Hok Wai Tsui, Jingbo Wang, Ping Tan, Qifeng Chen
  year: 2025
  venue: SIGGRAPH 2025
  arxiv_id: 2505.02094
  paper_url: https://arxiv.org/abs/2505.02094
  project_url: https://ingrid789.github.io/SkillMimicV2/
  code_url: https://github.com/wyhuai/SkillMimic-V2
  category: Motion-Imitation
  task_tags: [interaction, robustness, sparse-demos, character-anim]
  robot_platform: simulated humanoid + ball
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Robust interaction-skill learning from few/noisy demonstrations through stitched trajectory expansion.
  why_it_matters: Pushes motion-imitation toward usable demos rather than perfect mocap.

- title: SuperPADL: Scaling Language-Directed Physics-Based Control with Progressive Supervised Distillation
  authors: Jordan Juravsky, Yunrong Guo, Sanja Fidler, Xue Bin Peng
  year: 2024
  venue: SIGGRAPH 2024
  arxiv_id: 2407.10481
  paper_url: https://arxiv.org/abs/2407.10481
  project_url: https://xbpeng.github.io/projects/SuperPADL/index.html
  code_url: ""
  category: Motion-Imitation
  task_tags: [text-to-motion, distillation, character-anim]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Scales language-directed physics control to 5K+ skills via progressive RL→supervised distillation.
  why_it_matters: Largest text-to-motion physics controller; reference for scaling.

- title: MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations
  authors: Heyuan Yao, Zhenhua Song, Yuyang Zhou, Tenglong Ao, Baoquan Chen, Libin Liu
  year: 2024
  venue: SIGGRAPH 2024 (TOG)
  arxiv_id: 2310.10198
  paper_url: https://arxiv.org/abs/2310.10198
  project_url: https://moconvq.github.io/
  code_url: https://github.com/heyuanYao-PKU/MoConVQ
  category: Motion-Imitation
  task_tags: [VQ-VAE, model-based-RL, character-anim, language]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: VQ-VAE + model-based RL motion controller scalable to tens of hours of data; integrates with LLMs.
  why_it_matters: Strong VQ baseline for unified character control with language interfaces.

- title: FB-CPR / Meta Motivo: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models
  authors: Andrea Tirinzoni, Ahmed Touati, Jesse Farebrother, et al. (Meta FAIR)
  year: 2024
  venue: NeurIPS 2024 (workshop) / Meta AI release
  arxiv_id: 2412.09858
  paper_url: https://arxiv.org/abs/2412.09858
  project_url: https://metamotivo.metademolab.com/
  code_url: https://github.com/facebookresearch/metamotivo
  category: Motion-Imitation
  task_tags: [behavioral-foundation-model, forward-backward, unsupervised-RL, character-anim]
  robot_platform: SMPL humanoid (Mujoco)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: First behavioral foundation model that prompts a single humanoid policy to track motions, reach goals, or optimize rewards zero-shot.
  why_it_matters: Forward-Backward representations + policy regularization on mocap; new paradigm for promptable control.

- title: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised RL
  authors: Tairan He, Yi Chen, Wenli Xiao, et al. (CMU LeCAR Lab)
  year: 2025
  venue: ICLR 2026
  arxiv_id: 2511.04131
  paper_url: https://arxiv.org/abs/2511.04131
  project_url: https://lecar-lab.github.io/BFM-Zero/
  code_url: https://github.com/LeCAR-Lab/BFM-Zero
  category: Motion-Imitation / WBC-Tracking
  task_tags: [behavioral-foundation-model, unsupervised-RL, sim2real, Unitree-G1, FB-representation]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Brings the FB-CPR behavioral foundation paradigm to a real Unitree G1 with reward-shaping, DR, and asymmetric history-conditioned learning.
  why_it_matters: First real-world deployment of a promptable behavioral foundation model on a humanoid robot.

---

## Humanoid Whole-Body Tracking on Real Robots (2024-2026)

- title: Expressive Whole-Body Control for Humanoid Robots (ExBody)
  authors: Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: RSS 2024
  arxiv_id: 2402.16796
  paper_url: https://arxiv.org/abs/2402.16796
  project_url: https://expressive-humanoid.github.io/
  code_url: https://github.com/chengxuxin/expressive-humanoid
  category: WBC-Tracking
  task_tags: [RL, sim2real, humanoid, expressive, decoupled-upper-lower]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Decouples upper-body imitation from lower-body velocity tracking to imitate AMASS on a real H1.
  why_it_matters: Seminal work showing real humanoids can imitate large-scale mocap; baseline for nearly every later WBC paper.

- title: H2O: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  authors: Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, Guanya Shi
  year: 2024
  venue: IROS 2024
  arxiv_id: 2403.04436
  paper_url: https://arxiv.org/abs/2403.04436
  project_url: https://human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: WBC-Tracking
  task_tags: [RL, teleoperation, sim2real, RGB, sim-to-data, Unitree-H1]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Learns a robust whole-body tracker via PHC-filtered AMASS, enabling RGB-camera teleop on a real H1 zero-shot.
  why_it_matters: First learning-based real-time WB humanoid teleop; established the "sim-to-data" pipeline.

- title: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
  authors: Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, Guanya Shi
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.08858
  paper_url: https://arxiv.org/abs/2406.08858
  project_url: https://omni.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: WBC-Tracking
  task_tags: [teleoperation, dexterous, VR, autonomy, GPT-4, Unitree-H1]
  robot_platform: Unitree H1 + dexterous hands
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Universal pose-as-interface humanoid control supporting VR teleop, language, RGB, and learned autonomy from demos.
  why_it_matters: Defines the "kinematic pose as universal interface" paradigm now standard in humanoid research.

- title: HumanPlus: Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  category: WBC-Tracking
  task_tags: [RL, transformer, imitation, RGB, sim2real, 33-DoF-humanoid]
  robot_platform: Custom 33-DoF humanoid (Unitree H1 base)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: HST shadowing policy + HIT imitation transformer let a humanoid mimic humans from RGB and learn whole-body manipulation tasks.
  why_it_matters: Full-stack open-source humanoid imitation system from Stanford; widely reproduced.

- title: HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots
  authors: Tairan He, Wenli Xiao, Toru Lin, Zhengyi Luo, Zhenjia Xu, Zhenyu Jiang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Yuke Zhu, Linxi Fan
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2410.21229
  paper_url: https://arxiv.org/abs/2410.21229
  project_url: https://hover-versatile-humanoid.github.io/
  code_url: https://github.com/NVlabs/HOVER
  category: WBC-Tracking
  task_tags: [policy-distillation, multi-mode, command-masking, sim2real, Unitree-H1, NVIDIA]
  robot_platform: Unitree H1 (19-DoF)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Distills a kinematic-tracking oracle into a 1.5M-param student via proprioception+command masking, unifying 15+ control modes.
  why_it_matters: Established multi-mode policy distillation as the recipe for versatile humanoid controllers; integrated in NVIDIA GR00T.

- title: ExBody2: Advanced Expressive Humanoid Whole-Body Control
  authors: Mazeyu Ji, Xuanbin Peng, Fangchen Liu, Jialong Li, Ge Yang, Xuxin Cheng, Xiaolong Wang
  year: 2024
  venue: arXiv 2024.12 (RSS 2025 sub.)
  arxiv_id: 2412.13196
  paper_url: https://arxiv.org/abs/2412.13196
  project_url: https://exbody2.github.io/
  code_url: ""
  category: WBC-Tracking
  task_tags: [decoupled-velocity, teacher-student, dataset-curation, Unitree-H1, Unitree-G1]
  robot_platform: Unitree H1, Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Generalized whole-body tracker with automatic motion-feasibility curation and decoupled velocity/landmark tracking on H1 and G1.
  why_it_matters: Sets pretraining-then-finetuning recipe and reveals diversity-vs-feasibility principle for WBC datasets.

- title: ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  authors: Tairan He, Jiawei Gao, Wenli Xiao, Yuanhang Zhang, Zi Wang, Jiashun Wang, Zhengyi Luo, Guanzhi Wang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Linxi Fan, Yuke Zhu
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.01143
  paper_url: https://arxiv.org/abs/2502.01143
  project_url: https://agile.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/ASAP
  category: WBC-Tracking
  task_tags: [delta-action, sim2real, residual, agile, Unitree-G1, two-stage]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Learns a delta-action residual that compensates sim2real dynamics gap, enabling extreme agile skills (jumps, spins, kicks) on G1.
  why_it_matters: Most cited 2025 paper for closing the agile humanoid sim2real gap; reference baseline for residual-action methods.

- title: TWIST: Teleoperated Whole-Body Imitation System
  authors: Yanjie Ze, Zixuan Chen, João Pedro Araújo, Zi-ang Cao, Xue Bin Peng, Jiajun Wu, C. Karen Liu
  year: 2025
  venue: CoRL 2025
  arxiv_id: 2505.02833
  paper_url: https://arxiv.org/abs/2505.02833
  project_url: https://yanjieze.com/TWIST/
  code_url: https://github.com/YanjieZe/TWIST
  category: WBC-Tracking
  task_tags: [teleoperation, mocap, teacher-student, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: End-to-end teleop pipeline (mocap → retargeting → tracker) achieving high-quality whole-body imitation on real G1.
  why_it_matters: Open-source teleop reference frequently combined with GMR retargeting.

- title: TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System
  authors: Yanjie Ze et al. (Amazon FAR)
  year: 2025
  venue: arXiv 2025.11
  arxiv_id: 2511.02832
  paper_url: https://arxiv.org/abs/2511.02832
  project_url: https://yanjieze.com/TWIST2/
  code_url: https://github.com/amazon-far/TWIST2
  category: WBC-Tracking
  task_tags: [teleoperation, mocap-free, VR, data-collection, Unitree-G1]
  robot_platform: Unitree G1 + 2-DoF neck
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Mocap-free, PICO4U-VR-based portable WBC teleop collecting 100 demos in 15 min at near-100% success.
  why_it_matters: Solves the data-collection bottleneck for whole-body humanoid imitation learning.

- title: GMT: General Motion Tracking for Humanoid Whole-Body Control
  authors: Zixuan Chen, Mazeyu Ji, Xuxin Cheng, Xuanbin Peng, Xue Bin Peng, Xiaolong Wang
  year: 2025
  venue: arXiv 2025.06
  arxiv_id: 2506.14770
  paper_url: https://arxiv.org/abs/2506.14770
  project_url: https://gmt-humanoid.github.io/
  code_url: https://github.com/zixuan417/humanoid-general-motion-tracking
  category: WBC-Tracking
  task_tags: [mixture-of-experts, adaptive-sampling, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Single tracker with motion-MoE + adaptive sampling that handles diverse motions on a real G1.
  why_it_matters: Strong open baseline for general (non-specialized) humanoid trackers.

- title: GMR: General Motion Retargeting (Retargeter for TWIST)
  authors: Yanjie Ze et al.
  year: 2026 (arXiv 2025)
  venue: ICRA 2026
  arxiv_id: ""
  paper_url: https://github.com/YanjieZe/GMR
  project_url: https://github.com/YanjieZe/GMR
  code_url: https://github.com/YanjieZe/GMR
  category: WBC-Tracking
  task_tags: [retargeting, real-time, CPU, multi-robot]
  robot_platform: Unitree H1, H1-2, G1, multi-robot
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Real-time CPU motion retargeting library handling SMPL→multi-humanoid mapping with foot-sliding/penetration fixes.
  why_it_matters: De-facto open-source retargeting standard now used by TWIST, BeyondMimic, and others.

- title: Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking
  authors: João Pedro Araújo et al.
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.02252
  paper_url: https://arxiv.org/abs/2510.02252
  project_url: https://jaraujo98.github.io/retargeting_matters/
  code_url: ""
  category: WBC-Tracking
  task_tags: [retargeting, evaluation, ablation, humanoid]
  robot_platform: multi-humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Systematic study showing retargeting quality dominates downstream tracking performance.
  why_it_matters: Establishes retargeting as a first-class research topic, not preprocessing.

- title: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
  authors: Anonymous (project page authors); arXiv 2025.09
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.26633
  paper_url: https://arxiv.org/abs/2509.26633
  project_url: https://omniretarget.github.io/
  code_url: ""
  category: WBC-Tracking
  task_tags: [retargeting, interaction-mesh, parkour, loco-manipulation, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Interaction-mesh-based retargeter that preserves agent-terrain-object contact, enabling 30s parkour on G1 with 5 reward terms.
  why_it_matters: Shows retargeting for scene interaction, not just free-space motion.

- title: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills
  authors: Tencent ARC / TeleHuman Group
  year: 2025
  venue: arXiv 2025.06 (NeurIPS 2025 sub.)
  arxiv_id: 2506.12851
  paper_url: https://arxiv.org/abs/2506.12851
  project_url: https://kungfu-bot.github.io/
  code_url: https://github.com/TeleHuman/PBHC
  category: WBC-Tracking
  task_tags: [highly-dynamic, kungfu, dance, adaptive-tolerance, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Bi-level adaptive tolerance curriculum that lets a humanoid learn kungfu and dance from a single mocap clip.
  why_it_matters: Reference for highly-dynamic humanoid skills with adaptive curriculum.

- title: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  authors: Takara Truong, Qiayuan Liao, Xiaoyu Huang, Guy Tevet, Koushil Sreenath, C. Karen Liu
  year: 2025
  venue: arXiv 2025.08
  arxiv_id: 2508.08241
  paper_url: https://arxiv.org/abs/2508.08241
  project_url: https://beyondmimic.github.io/
  code_url: https://github.com/HybridRobotics/whole_body_tracking
  category: WBC-Tracking
  task_tags: [guided-diffusion, agile, cartwheel, sprint, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Guided diffusion at inference time turns a tracker into a versatile controller doing aerial cartwheels, spin-kicks, and sprinting.
  why_it_matters: Top-tier 2025 open-source agile humanoid; new baseline for human-likeness on hardware.

- title: UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots
  authors: Kangning Yin et al.
  year: 2025
  venue: CoRL 2025
  arxiv_id: 2507.07356
  paper_url: https://arxiv.org/abs/2507.07356
  project_url: https://yinkangning0124.github.io/Humanoid-UniTracker/
  code_url: https://github.com/yinkangning0124/Humanoid-UniTracker
  category: WBC-Tracking
  task_tags: [CVAE, three-stage, partial-observation, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: CVAE-based universal policy with privileged-teacher → CVAE-student → adaptation pipeline; tracks under partial observations.
  why_it_matters: Strong reference for partial-observation generalist humanoid tracking.

- title: SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
  authors: NVIDIA GEAR
  year: 2025
  venue: arXiv 2025.11
  arxiv_id: 2511.07820
  paper_url: https://arxiv.org/abs/2511.07820
  project_url: https://nvlabs.github.io/SONIC/
  code_url: https://github.com/NVlabs/GR00T-WholeBodyControl
  category: WBC-Tracking
  task_tags: [foundation-model, scaling, kinematic-planner, GR00T, multi-robot]
  robot_platform: Multi-humanoid (GR00T)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Scales motion tracking to 42M params, 700h data, 9k GPU-hr; ships universal kinematic planner unifying VR / video / VLA inputs.
  why_it_matters: Largest WBC foundation model to date; backbone of NVIDIA GR00T N1.5 / N1.6 controllers.

- title: MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation
  authors: BAAI Humanoid Team
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.08594
  paper_url: https://arxiv.org/abs/2602.08594
  project_url: https://github.com/BAAI-Humanoid/MOSAIC
  code_url: https://github.com/BAAI-Humanoid/MOSAIC
  category: WBC-Tracking
  task_tags: [residual-adaptation, teleoperation, multi-source-data, sim2real]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Trains a generalist tracker then rapidly adapts to specific teleop interfaces via additive residuals.
  why_it_matters: Open-source full-stack sim2real teleop with multi-source motion bank.

- title: ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning
  authors: Siheng Zhao, Yanjie Ze, Yue Wang, C. Karen Liu, Pieter Abbeel, Guanya Shi, Rocky Duan
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.05070
  paper_url: https://arxiv.org/abs/2510.05070
  project_url: https://resmimic.github.io/
  code_url: ""
  category: WBC-Tracking
  task_tags: [residual, GMT-base, object-interaction, point-cloud-reward, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Two-stage residual on top of a frozen GMT base policy adds object interaction with contact and point-cloud rewards.
  why_it_matters: Bridges WBC tracking with whole-body manipulation via residual learning.

- title: VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation
  authors: Shaofeng Yin, Yanjie Ze, Hong-Xing Yu, C. Karen Liu, Jiajun Wu
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.20322
  paper_url: https://arxiv.org/abs/2509.20322
  project_url: https://visualmimic.github.io/
  code_url: https://github.com/visualmimic/VisualMimic
  category: WBC-Tracking
  task_tags: [hierarchical, visual, sim2real, loco-manipulation, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Low-level keypoint tracker + high-level vision policy delivering box lifting, pushing, soccer dribble/kick on real G1 zero-shot.
  why_it_matters: Demonstrates that motion-tracking primitives compose into vision-driven manipulation.

- title: JAEGER: Dual-Level Humanoid Whole-Body Controller
  authors: Ziluo Ding, Haobin Jiang, Yuxuan Wang, Zhenguo Sun, Yu Zhang, Xiaojie Niu, Ming Yang, Weishuai Zeng, Xinrun Xu, Zongqing Lu
  year: 2025
  venue: arXiv 2025.05
  arxiv_id: 2505.06584
  paper_url: https://arxiv.org/abs/2505.06584
  project_url: https://beingbeyond.github.io/Jaeger/
  code_url: https://github.com/BeingBeyond/Jaeger
  category: WBC-Tracking
  task_tags: [dual-controller, upper-lower-decoupled, AMASS, sim2real]
  robot_platform: Two humanoid platforms (incl. Unitree)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Decouples upper- and lower-body controllers and supports both root-velocity and joint-angle commands.
  why_it_matters: Clean dual-controller baseline for fault-tolerant whole-body command spaces.

- title: HugWBC: A Unified and General Humanoid Whole-Body Controller for Versatile Locomotion
  authors: Yufei Xue, Wentao Dong, Minghuan Liu, Weinan Zhang, Jiangmiao Pang
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.03206
  paper_url: https://arxiv.org/abs/2502.03206
  project_url: https://hugwbc.github.io/
  code_url: ""
  category: WBC-Tracking
  task_tags: [unified-command, gait-control, intervention, sim2real, Unitree-H1]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Single policy producing customizable gaits (frequency, swing, height, pitch) plus real-time upper-body teleop intervention.
  why_it_matters: Strong fine-grained command-space baseline; unifies WBC with loco-manipulation interventions.

- title: I-CTRL: Imitation to Control Humanoid Robots Through Bounded Residual RL
  authors: Yashuai Yan, Esteve Valls Mascaro, Tobias Egle, Dongheui Lee
  year: 2024
  venue: IEEE RAM 2024 (Special Issue on Humanoids)
  arxiv_id: 2405.08726
  paper_url: https://arxiv.org/abs/2405.08726
  project_url: https://evm7.github.io/I-CTRL/
  code_url: https://github.com/Evm7/I-CTRL
  category: WBC-Tracking
  task_tags: [bounded-residual, constrained-RL, four-robots, retargeting]
  robot_platform: 4 humanoids (sim)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Constrained residual RL on top of kinematic retargeting; one agent imitates large-scale data across 4 robots.
  why_it_matters: Lightweight reproducible baseline for cross-embodiment imitation.

- title: FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation
  authors: Yuanhang Zhang, Yifu Yuan, Wenli Xiao, Tairan He, Guanqi He, Mingxi Lin, Changliu Liu, Guanya Shi
  year: 2025
  venue: L4DC 2026
  arxiv_id: 2505.06776
  paper_url: https://arxiv.org/abs/2505.06776
  project_url: https://lecar-lab.github.io/falcon-humanoid/
  code_url: https://github.com/LeCAR-Lab/FALCON
  category: WBC-Tracking
  task_tags: [force-adaptive, dual-agent, loco-manipulation, multi-humanoid]
  robot_platform: Multiple humanoids
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Dual-agent RL achieving 2× more accurate upper-body tracking under heavy external forces (cart-pull 100N, payload 20N, door 40N).
  why_it_matters: WBC under contact/force disturbances on real hardware.

- title: Any2Track / OpenTrack: Track Any Motions under Any Disturbances
  authors: Galaxy General Robotics team
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.13833
  paper_url: https://arxiv.org/abs/2509.13833
  project_url: https://zzk273.github.io/Any2Track/
  code_url: https://github.com/GalaxyGeneralRobotics/OpenTrack
  category: WBC-Tracking
  task_tags: [foundation-tracker, history-adapter, disturbance, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: AnyTracker (general policy) + AnyAdapter (online history-conditioned dynamics adaptation) for robust tracking under disturbances.
  why_it_matters: Open-source foundation tracker emphasizing real-world robustness.

- title: RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking
  authors: Yunshen Chen et al.
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.20717
  paper_url: https://arxiv.org/abs/2509.20717
  project_url: https://arxiv.org/html/2509.20717
  code_url: ""
  category: WBC-Tracking
  task_tags: [residual-action, single-stage-RL, long-horizon, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: One-stage residual-action RL pipeline tracking multi-minute high-energy dance on G1 zero-shot.
  why_it_matters: Demonstrates simplified single-stage training competitive with two-stage ASAP-style pipelines.

- title: Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking
  authors: Yun Liu et al.
  year: 2024
  venue: arXiv 2024.12
  arxiv_id: 2412.17730
  paper_url: https://arxiv.org/abs/2412.17730
  project_url: https://mimicking-bench.github.io/
  code_url: ""
  category: WBC-Tracking
  task_tags: [benchmark, humanoid-scene, retargeting, IsaacGym, dataset]
  robot_platform: UniH1 (sim)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 📦 Dataset
  one_line: First benchmark for retargeting + tracking + imitation across 6 household scene-interaction tasks (11K objects, 23K motions).
  why_it_matters: Standard benchmark for WBC + scene interaction.

- title: HumanoidVerse: Multi-Simulator Framework for Humanoid Sim-to-Real Learning
  authors: CMU LeCAR Lab
  year: 2025
  venue: open-source release
  arxiv_id: ""
  paper_url: https://github.com/LeCAR-Lab/HumanoidVerse
  project_url: https://github.com/LeCAR-Lab/HumanoidVerse
  code_url: https://github.com/LeCAR-Lab/HumanoidVerse
  category: WBC-Tracking
  task_tags: [framework, IsaacGym, IsaacSim, Genesis, MuJoCo, Unitree-H1, Unitree-G1]
  robot_platform: Unitree H1, G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified multi-simulator (IsaacGym/IsaacSim/Genesis/MuJoCo) humanoid RL training framework underpinning ASAP, FALCON, BFM-Zero.
  why_it_matters: Reference infra used in many flagship humanoid WBC papers.

- title: GentleHumanoid: Whole-Body Motion Tracking with Compliance
  authors: Anonymous (project page)
  year: 2025
  venue: arXiv 2025
  arxiv_id: ""
  paper_url: https://github.com/Axellwppr/gentle-humanoid
  project_url: https://github.com/Axellwppr/gentle-humanoid
  code_url: https://github.com/Axellwppr/gentle-humanoid
  category: WBC-Tracking
  task_tags: [compliance, deployment, sim2real]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Inference + deploy code for compliant whole-body motion tracking.
  why_it_matters: Open compliance-aware tracker for safe interaction.

- title: PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking
  authors: arXiv 2026.03
  year: 2026
  venue: arXiv 2026.03
  arxiv_id: 2603.05410
  paper_url: https://arxiv.org/abs/2603.05410
  project_url: https://arxiv.org/abs/2603.05410
  code_url: ""
  category: WBC-Tracking
  task_tags: [VLA, flow-matching, multi-brain, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Physics-aware whole-body VLA combining multi-brain latent flow matching with a robust tracker on G1.
  why_it_matters: Recent VLA-tracking integration target.

- title: CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation
  authors: arXiv 2026.02
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.15060
  paper_url: https://arxiv.org/abs/2602.15060
  project_url: https://arxiv.org/abs/2602.15060
  code_url: ""
  category: WBC-Tracking
  task_tags: [closed-loop, transformer, teleoperation, drift-free, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Closed-loop high-frequency localization feedback for drift-free long-horizon humanoid teleoperation; transformer trained 1.3K GPU-hr.
  why_it_matters: Tackles long-horizon drift, the main failure mode of open-loop trackers.

- title: Robust and Generalized Humanoid Motion Tracking
  authors: arXiv 2026.01
  year: 2026
  venue: arXiv 2026.01
  arxiv_id: 2601.23080
  paper_url: https://arxiv.org/abs/2601.23080
  project_url: https://arxiv.org/abs/2601.23080
  code_url: ""
  category: WBC-Tracking
  task_tags: [robustness, dynamics-conditioned, fall-recovery, breakdance]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Dynamics-conditioned command aggregation + fall-recovery curriculum tracking even at 1500% noise; breakdance-class motions.
  why_it_matters: Pushes tracker robustness to extreme contact/recovery regimes.

- title: Towards Adaptable Humanoid Control via Adaptive Motion Tracking
  authors: arXiv 2025.10
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.14454
  paper_url: https://arxiv.org/abs/2510.14454
  project_url: https://arxiv.org/abs/2510.14454
  code_url: ""
  category: WBC-Tracking
  task_tags: [adaptive, online-adaptation, humanoid]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Adaptive motion tracking for humanoid control across novel conditions.
  why_it_matters: Online-adaptation angle complements ASAP-style pre-deployment fixes.

- title: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  authors: arXiv 2026.02
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.21599
  paper_url: https://arxiv.org/abs/2602.21599
  project_url: https://arxiv.org/abs/2602.21599
  code_url: ""
  category: WBC-Tracking
  task_tags: [synthetic-data, prompt-refinement, multi-domain, RL-scaling]
  robot_platform: humanoid (sim/real)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Closed-loop synthesis pipeline that grows tracker repertoire across martial-arts/dance/combat/sports/gymnastics.
  why_it_matters: Suggests data-synthesis-as-curriculum for unbounded skill scaling.

- title: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
  authors: arXiv 2026.04
  year: 2026
  venue: arXiv 2026.04
  arxiv_id: 2604.17335
  paper_url: https://arxiv.org/abs/2604.17335
  project_url: https://arxiv.org/abs/2604.17335
  code_url: ""
  category: WBC-Tracking
  task_tags: [motion-generation, closed-loop-finetuning, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Couples a frozen motion generator with a finetuned tracker in a closed loop for real-time deployment.
  why_it_matters: Tightens generator-tracker coupling for online robustness.

- title: Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching
  authors: arXiv 2026.02
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.15827
  paper_url: https://arxiv.org/abs/2602.15827
  project_url: https://arxiv.org/abs/2602.15827
  code_url: ""
  category: WBC-Tracking
  task_tags: [parkour, perception, motion-matching, DAgger, distillation]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Train RL experts per motion, distill to a depth-image multi-skill student via DAgger+RL for vision-based parkour.
  why_it_matters: Brings exteroceptive parkour to motion-tracking pipelines.

- title: Deep Whole-Body Parkour
  authors: arXiv 2026.01
  year: 2026
  venue: arXiv 2026.01
  arxiv_id: 2601.07701
  paper_url: https://arxiv.org/abs/2601.07701
  project_url: https://arxiv.org/abs/2601.07701
  code_url: ""
  category: WBC-Tracking
  task_tags: [parkour, exteroception, multi-contact, dynamic-motion]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Single policy for vault, dive-roll, and other multi-contact dynamic motions on unstructured terrain.
  why_it_matters: Pushes WBC tracking beyond flat-ground locomotion.

- title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes (FastSAC / FastTD3)
  authors: Younggyo Seo et al.
  year: 2025
  venue: arXiv 2025.12
  arxiv_id: 2512.01996
  paper_url: https://arxiv.org/abs/2512.01996
  project_url: https://arxiv.org/abs/2512.01996
  code_url: ""
  category: WBC-Tracking
  task_tags: [fast-RL, off-policy, sim2real, single-GPU, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: FastSAC/FastTD3 train humanoid locomotion and motion-tracking policies in 15 min on a single RTX 4090.
  why_it_matters: Drastically lowers compute barrier for humanoid WBC research.

- title: From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots
  authors: arXiv 2025.06
  year: 2025
  venue: arXiv 2025.06
  arxiv_id: 2506.12779
  paper_url: https://arxiv.org/abs/2506.12779
  project_url: https://arxiv.org/abs/2506.12779
  code_url: ""
  category: WBC-Tracking
  task_tags: [generalist, expert-distillation, multi-skill]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Distills multiple skill-specific experts into a single generalist whole-body controller.
  why_it_matters: Useful complement to HOVER's command-masking distillation.

- title: RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control
  authors: arXiv 2025.06
  year: 2025
  venue: arXiv 2025.06
  arxiv_id: 2506.12769
  paper_url: https://arxiv.org/abs/2506.12769
  project_url: https://arxiv.org/abs/2506.12769
  code_url: ""
  category: Motion-Imitation
  task_tags: [RLPF, motion-model-alignment, sim2real, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Uses physics-based reward feedback to align large motion models with humanoid hardware capabilities.
  why_it_matters: Bridges generative motion models and tracker training via RL alignment.

- title: From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance
  authors: arXiv 2025.10
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.14952
  paper_url: https://arxiv.org/abs/2510.14952
  project_url: https://arxiv.org/abs/2510.14952
  code_url: ""
  category: WBC-Tracking
  task_tags: [language, motion-latent, retargeting-free, Unitree]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Skips explicit retargeting by guiding humanoid policy with a learned motion latent from language.
  why_it_matters: Alternative to retargeting-heavy pipelines (GMR/OmniRetarget).

- title: ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation
  authors: arXiv 2025.07
  year: 2025
  venue: arXiv 2025.07
  arxiv_id: 2507.06905
  paper_url: https://arxiv.org/abs/2507.06905
  project_url: https://arxiv.org/abs/2507.06905
  code_url: ""
  category: WBC-Tracking
  task_tags: [unified-controller, fine-grained, loco-manipulation]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Single policy with fine-grained command space for combined locomotion and manipulation.
  why_it_matters: Continues HugWBC-style unified controller agenda toward manipulation.

- title: Visual Imitation Enables Contextual Humanoid Control (VIEW)
  authors: arXiv 2025.05
  year: 2025
  venue: arXiv 2025.05
  arxiv_id: 2505.03729
  paper_url: https://arxiv.org/abs/2505.03729
  project_url: https://arxiv.org/abs/2505.03729
  code_url: ""
  category: Motion-Imitation
  task_tags: [visual-imitation, contextual, humanoid]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Visual imitation framework providing contextual humanoid control from videos.
  why_it_matters: Connects WBC tracking with video-conditioned policies.

- title: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space
  authors: arXiv 2025.05
  year: 2025
  venue: arXiv 2025.05
  arxiv_id: 2505.10918
  paper_url: https://arxiv.org/abs/2505.10918
  project_url: https://arxiv.org/abs/2505.10918
  code_url: ""
  category: WBC-Tracking
  task_tags: [skill-space, reaching, real-world-ready]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Builds a real-world-ready skill space for humanoid reaching with whole-body coordination.
  why_it_matters: Skill-space approach to constrained whole-body tasks.

- title: HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model
  authors: arXiv 2026.02
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.11758
  paper_url: https://arxiv.org/abs/2602.11758
  project_url: https://arxiv.org/abs/2602.11758
  code_url: ""
  category: WBC-Tracking
  task_tags: [world-model, agile-interaction, dynamics-aware]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Dynamics-aware world model for agile humanoid object interaction with whole-body control.
  why_it_matters: Combines model-based RL with WBC tracking for contact-rich tasks.

- title: WholebodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control
  authors: OpenDriveLab
  year: 2026
  venue: ICLR 2026
  arxiv_id: ""
  paper_url: https://github.com/OpenDriveLab/WholebodyVLA
  project_url: https://github.com/OpenDriveLab/WholebodyVLA
  code_url: https://github.com/OpenDriveLab/WholebodyVLA
  category: WBC-Tracking
  task_tags: [VLA, whole-body, loco-manipulation, latent]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified latent VLA architecture for whole-body humanoid loco-manipulation with tracking primitives.
  why_it_matters: Open-source VLA wrapper around motion-tracking primitives.

- title: DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion
  authors: arXiv 2025.09
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.14353
  paper_url: https://arxiv.org/abs/2509.14353
  project_url: https://genrobo.github.io/DreamControl/
  code_url: ""
  category: WBC-Tracking
  task_tags: [guided-diffusion, scene-interaction, RL-prior, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Diffusion prior trained on human motion provides reward signal that guides RL to discover scene-interaction skills on G1.
  why_it_matters: Diffusion-as-reward complements diffusion-as-policy approaches like BeyondMimic.

- title: MimicKit
  authors: Xue Bin Peng
  year: 2024-2025
  venue: open-source toolkit
  arxiv_id: ""
  paper_url: https://github.com/xbpeng/MimicKit
  project_url: https://github.com/xbpeng/MimicKit
  code_url: https://github.com/xbpeng/MimicKit
  category: Motion-Imitation
  task_tags: [framework, AMP, DeepMimic, character-anim]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Lightweight unified suite implementing DeepMimic, AMP, and friends for motion imitation training.
  why_it_matters: Maintained reference implementation of classic motion-imitation algorithms.

- title: NCP / Tencent RoboticsX motion control suite
  authors: Tencent RoboticsX
  year: 2023-2024
  venue: open-source
  arxiv_id: ""
  paper_url: https://github.com/Tencent-RoboticsX/NCP
  project_url: https://tencent-roboticsx.github.io/NCP/
  code_url: https://github.com/Tencent-RoboticsX/NCP
  category: Motion-Imitation
  task_tags: [skill-latent, VQ, character-anim]
  robot_platform: simulated humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Reference implementation of Neural Categorical Priors for character control.
  why_it_matters: Open VQ-latent baseline for skill reuse.

- title: Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids
  authors: Xiao Ren; Yuhui Yang; Zongbiao Weng; Zhijie Liu; He Kong
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.12814
  paper_url: https://arxiv.org/abs/2606.12814
  project_url: https://aislab-sustech.github.io/Stubborn/
  code_url: ""
  category: Motion-Imitation
  task_tags: [motion-tracking, fall-recovery, asymmetric-actor-critic, humanoid]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Unified RL framework that keeps failed states in training and learns robust motion tracking plus fall recovery in one policy.
  why_it_matters: Connects tracking and recovery instead of treating falls as terminal failures.

- title: RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning
  authors: Yichao Zhong; Yidan Lu; Yuhang Lu; Tianyang Tang; Haoguang Mai; Yixuan Pan; Tianyu Li; Li Chen; Jingbo Wang; Zhongyu Li; Peng Lu; Hongyang Li
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.11092
  paper_url: https://arxiv.org/abs/2606.11092
  project_url: https://opendrivelab.com/RoboNaldo
  code_url: ""
  category: Motion-Imitation
  task_tags: [soccer, shooting, curriculum-rl, whole-body, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Three-stage motion-guided curriculum RL for stable, accurate high-impulse humanoid soccer shooting.
  why_it_matters: Stress-tests whole-body balance and timing under ballistic object interaction.

- title: PTDL: Multi-Terrain Fall Recovery via Phase-Terrain Decoupled Learning
  authors: Xiaoyu Xu; Zhiming Chen; Yuenan Zhao; Ran Song; Wei Zhang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.08922
  paper_url: https://arxiv.org/abs/2606.08922
  project_url: ""
  code_url: ""
  category: Motion-Imitation
  task_tags: [fall-recovery, terrain, proprioception, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Phase-terrain decoupled policy recovers from falls on slopes, gravel, and uneven terrain before resuming walking.
  why_it_matters: Extends getting-up controllers beyond flat-ground quasi-static recovery.

- title: EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control
  authors: Haoyang Ge; Peng Ren; Yukun Shi; Cong Huang; Kun Li; Kai Chen
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.08495
  paper_url: https://arxiv.org/abs/2606.08495
  project_url: ""
  code_url: ""
  category: Motion-Imitation
  task_tags: [egocentric, motion-prior, interactive-control, whole-body]
  robot_platform: Unitree humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Learns an egocentric motion prior that maps human-view observations and intent into adaptive whole-body humanoid behaviors.
  why_it_matters: Bridges motion tracking and VLA-style semantic interfaces for interactive humanoid control.

- title: Mind Your Steps: A General Learning Framework for Accurate Humanoid Foothold Tracking
  authors: Alessandro Montenegro; Shihao Li; Puze Liu; Alberto Maria Metelli; Jan Peters
  year: 2026
  venue: RSS 2026
  arxiv_id: 2606.08253
  paper_url: https://arxiv.org/abs/2606.08253
  project_url: https://github.com/MontenegroAlessandro/mind-your-steps
  code_url: ""
  category: Motion-Imitation
  task_tags: [foothold-tracking, locomotion, navigation, humanoid]
  robot_platform: Booster T1 / humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Learning framework for accurate foothold placement on humanoids, improving safe navigation before manipulation.
  why_it_matters: Precise stepping is a missing primitive for cluttered loco-manipulation.

- title: Predictive Style Matching: Natural and Robust Humanoid Locomotion
  authors: Simeon Nedelchev; Ekaterina Chaikovskaia; Egor Davydenko; Eduard Zaliaev; Roman Gorbachev
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.07083
  paper_url: https://arxiv.org/abs/2606.07083
  project_url: ""
  code_url: ""
  category: Motion-Imitation
  task_tags: [locomotion, style-matching, robustness, humanoid]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Predictive style-matching objective improves natural humanoid gait while preserving disturbance recovery.
  why_it_matters: Targets the common tradeoff between imitation aesthetics and robust locomotion.

- title: LIMMT: Less is More for Motion Tracking
  authors: Yu Guan; Zekun Qi; Chenghuai Lin; Xuchuan Chen; Dairu Liu; Wenyao Zhang; Jilong Wang; Xinqiang Yu; He Wang; Li Yi
  year: 2026
  venue: ICML 2026
  arxiv_id: 2606.06953
  paper_url: https://arxiv.org/abs/2606.06953
  project_url: https://github.com/GalaxyGeneralRobotics/Humanoid-GPT
  code_url: https://github.com/GalaxyGeneralRobotics/Humanoid-GPT
  category: Motion-Imitation
  task_tags: [data-centric, motion-quality, motion-tracking, humanoid]
  robot_platform: Unitree G1 / humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Data-centric motion-tracking study showing that carefully filtered high-quality motions can outperform much larger noisy corpora.
  why_it_matters: Gives a practical recipe for curating tracking datasets before expensive RL training.

- title: LadderMan: Learning Humanoid Perceptive Ladder Climbing
  authors: Siheng Zhao; Yuanhang Zhang; Ziqi Lu; Pieter Abbeel; Rocky Duan; Koushil Sreenath; Yue Wang; C. Karen Liu; Guanya Shi
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.05873
  paper_url: https://arxiv.org/abs/2606.05873
  project_url: https://ladderman-robot.github.io
  code_url: ""
  category: Motion-Imitation
  task_tags: [ladder-climbing, perceptive-control, sim-to-real, whole-body]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Two-stage perceptive policy lets humanoids climb diverse ladders and manipulate in constrained vertical terrain.
  why_it_matters: Expands agile humanoid control from floor locomotion to sparse hand-foot contact structures.

- title: M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking
  authors: Zuxing Lu; Ziang Zheng; Yao Lyu; Jingyu Liu; Feihong Zhang; Song Lu; Xin Yuan; Changyin Sun; Xingxing Zuo; Shengbo Eben Li
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.04829
  paper_url: https://arxiv.org/abs/2606.04829
  project_url: https://github.com/Renforce-Dynamics/MultiModalWBC
  code_url: https://github.com/Renforce-Dynamics/MultiModalWBC
  category: Motion-Imitation
  task_tags: [multimodal-tracking, joint-trajectory, end-effector, whole-body]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Open IsaacLab-based WBC framework unifying joint, root, and end-effector reference modalities for humanoid motion mimicking.
  why_it_matters: Practical open baseline for downstream locomotion and loco-manipulation controllers.

- title: Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots
  authors: Tianchen Huang; Mingkuan Zhao; Yang Gao; Feiyang Yuan; Junchi Gu; Xiaohu Zhang; Dongdong Zhao; Shi Yan; Yu Wang; Wei Gao; Shiwu Zhang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.03536
  paper_url: https://arxiv.org/abs/2606.03536
  project_url: https://huangtc233.github.io/bionic-style-transfer/
  code_url: ""
  category: Motion-Imitation
  task_tags: [style-transfer, diffusion, whole-body, Unitree-G1]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Physics-aware diffusion transfers exemplar human motion style onto executable humanoid whole-body references.
  why_it_matters: Adds controllable expressive style to otherwise task-focused WBC pipelines.

- title: MIND: Multi-Scale Intent Diffusion for Text-Driven Physics-Based Humanoid Control
  authors: Bin Li; Ruichi Zhang; Han Liang; Jingyan Zhang; Juze Zhang; Xin Chen; Jingya Wang
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.26006
  paper_url: https://arxiv.org/abs/2605.26006
  project_url: https://binlee26.github.io/MIND_page/
  code_url: ""
  category: Motion-Imitation
  task_tags: [text-driven-control, intent-diffusion, physics-based, humanoid]
  robot_platform: physics-based humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Multi-scale intent diffusion bridges text semantics and low-level physics-based humanoid control.
  why_it_matters: Strengthens the text-to-control path without relying on a separate kinematic generator.

- title: SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-based Humanoid Control
  authors: Jingyan Zhang; Han Liang; Ruichi Zhang; Bin Li; Juze Zhang; Xin Chen; Jingya Wang; Lan Xu; Jingyi Yu
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.22894
  paper_url: https://arxiv.org/abs/2605.22894
  project_url: https://zhanglele12138.github.io/SCRIPT/
  code_url: ""
  category: Motion-Imitation
  task_tags: [language-driven-control, diffusion-policy, physics-based, humanoid]
  robot_platform: physics-based humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Joint action-state-text diffusion transformer for long-horizon language-driven physics-based humanoid control.
  why_it_matters: A scalable alternative to two-stage text-to-motion plus tracking stacks.

---

## Notes on Verification

GitHub repos verified to exist (HTTP 200) at time of writing:
ASAP, human2humanoid (H2O+OmniH2O), PHC, PULSE, ProtoMotions, TWIST, GMR, PBHC (KungfuBot), metamotivo (FB-CPR/Meta Motivo), MoCapAct, DeepMimic, MimicKit, TWIST2, GMT, gentle-humanoid, expressive-humanoid (ExBody), NVlabs/HOVER, NVlabs/CALM, NVlabs/GR00T-WholeBodyControl (SONIC), wyhuai/SkillMimic, wyhuai/SkillMimic-V2, ZhengyiLuo/UHC, Tencent-RoboticsX/NCP, heyuanYao-PKU/MoConVQ, MarkFzp/humanplus, BeingBeyond/Jaeger, LeCAR-Lab/BFM-Zero, LeCAR-Lab/FALCON, Evm7/I-CTRL, GalaxyGeneralRobotics/OpenTrack (Any2Track), HybridRobotics/whole_body_tracking (BeyondMimic), yinkangning0124/Humanoid-UniTracker, BAAI-Humanoid/MOSAIC, LeCAR-Lab/HumanoidVerse, visualmimic/VisualMimic, OpenDriveLab/WholebodyVLA, zixuan417/humanoid-general-motion-tracking (GMT).

ExBody2, ResMimic, OmniRetarget, HugWBC, MaskedMimic (NVIDIA), and several 2026 arXiv papers (CLOT, MOSAIC, Robust-Generalized-Tracking, Iterative-Closed-Loop, Perceptive-Parkour, Deep-Parkour, PhysiFlow) currently have project pages or paper-only releases. MaskedMimic's official code now ships inside NVlabs/ProtoMotions.
