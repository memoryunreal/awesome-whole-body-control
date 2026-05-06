# Humanoid Locomotion + Physics-Based Character Animation

Time range: 2018-2026 (priority on 2024-2026). ~45 papers covering humanoid WBC, motion tracking, and physics-based character animation foundations.

---

## Humanoid Locomotion / Whole-Body Control

- title: Learning Humanoid Standing-up Control across Diverse Postures (HoST)
  authors: Tao Huang, Junli Ren, Huayi Wang, Zirui Wang, Qingwei Ben, Muning Wen, Xiao Chen, Jianan Li, Jiangmiao Pang
  year: 2025
  venue: RSS 2025 (Best Systems Paper Finalist)
  arxiv_id: 2502.08378
  paper_url: https://arxiv.org/abs/2502.08378
  project_url: https://taohuang13.github.io/humanoid-standingup.github.io/
  code_url: https://github.com/InternRobotics/HoST
  category: Locomotion
  task_tags: [humanoid, fall-recovery, RL, sim2real, multi-critic, curriculum]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Multi-critic RL with smoothness regularization for posture-adaptive humanoid stand-up across diverse falls.
  why_it_matters: Foundational stand-up/recovery primitive; tightly relevant to robust WBC and motion tracking deployment.

- title: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models (Meta Motivo / FB-CPR)
  authors: Andrea Tirinzoni, Ahmed Touati, Jesse Farebrother, Mateusz Guzek, Anssi Kanervisto, Yingchen Xu, Alessandro Lazaric, Matteo Pirotta
  year: 2025
  venue: ICLR 2025
  arxiv_id: 2504.11054
  paper_url: https://arxiv.org/abs/2504.11054
  project_url: https://metamotivo.metademolab.com/
  code_url: https://github.com/facebookresearch/metamotivo
  category: Physics-Anim
  task_tags: [behavioral-foundation-model, unsupervised-RL, zero-shot, motion-tracking, FB-representation]
  robot_platform: sim-only SMPL humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Forward-Backward + Conditional Policy Regularization yields a single zero-shot prompted whole-body humanoid controller.
  why_it_matters: Defines the "behavioral foundation model" paradigm bridging character animation and humanoid WBC.

- title: Real-World Humanoid Locomotion with Reinforcement Learning
  authors: Ilija Radosavovic, Tete Xiao, Bike Zhang, Trevor Darrell, Jitendra Malik, Koushil Sreenath
  year: 2024
  venue: Science Robotics
  arxiv_id: 2303.03381
  paper_url: https://arxiv.org/abs/2303.03381
  project_url: https://learning-humanoid-locomotion.github.io/
  code_url: n/a
  category: Locomotion
  task_tags: [humanoid, transformer, sim2real, in-context-adaptation]
  robot_platform: Digit (Agility Robotics)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Causal-transformer locomotion policy zero-shot deployed on Digit humanoid for outdoor walking.
  why_it_matters: Landmark RL humanoid locomotion result; transformer + history-conditioning has become a standard baseline.

- title: Berkeley Humanoid: A Research Platform for Learning-based Control
  authors: Qiayuan Liao, Bike Zhang, Xuanyu Huang, Xiaoyu Huang, Zhongyu Li, Koushil Sreenath
  year: 2024
  venue: arXiv / IROS 2025
  arxiv_id: 2407.21781
  paper_url: https://arxiv.org/abs/2407.21781
  project_url: https://berkeley-humanoid.com/
  code_url: n/a
  category: Locomotion
  task_tags: [humanoid-platform, sim2real, RL, hardware-design]
  robot_platform: Berkeley Humanoid (mid-scale)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: hardware design partially open
  one_line: Mid-scale low-cost humanoid platform with narrow sim-to-real gap for learning-based locomotion.
  why_it_matters: Standard reference platform now featured in MuJoCo Playground; benchmark for hardware-conditioned policies.

- title: Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible 3D-printed Humanoid
  authors: Yufeng Chi, Qiayuan Liao, Junfeng Long, et al.
  year: 2025
  venue: RSS 2025 demo
  arxiv_id: 2504.17249
  paper_url: https://arxiv.org/abs/2504.17249
  project_url: https://lite.berkeley-humanoid.com/
  code_url: https://github.com/HybridRobotics/BerkeleyHumanoidLite
  category: Locomotion
  task_tags: [open-source-hardware, 3d-printed, RL]
  robot_platform: Berkeley Humanoid Lite
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Fully open 3D-printed humanoid with end-to-end RL locomotion stack.
  why_it_matters: Accessible humanoid baseline; useful for hardware-conditioned/multi-embodiment policy research.

- title: Humanoid Parkour Learning
  authors: Ziwen Zhuang, Shenzhe Yao, Hang Zhao
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10759
  paper_url: https://arxiv.org/abs/2406.10759
  project_url: https://humanoid4parkour.github.io/
  code_url: https://github.com/ZiwenZhuang/parkour
  category: Locomotion
  task_tags: [humanoid, parkour, vision, end-to-end, whole-body]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: End-to-end vision-based whole-body parkour policy on Unitree H1 without motion priors.
  why_it_matters: Reference for perceptive humanoid agility; benchmark for parkour/terrain skills.

- title: Extreme Parkour with Legged Robots
  authors: Xuxin Cheng, Kexin Shi, Ananye Agarwal, Deepak Pathak
  year: 2023/2024
  venue: ICRA 2024
  arxiv_id: 2309.14341
  paper_url: https://arxiv.org/abs/2309.14341
  project_url: https://extreme-parkour.github.io/
  code_url: https://github.com/chengxuxin/extreme-parkour
  category: Locomotion
  task_tags: [parkour, legged, depth-image, single-policy]
  robot_platform: Unitree A1/Go1
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: released
  one_line: Single-policy parkour from depth image trained in <20h, agile high-jump and gap-leap behaviors.
  why_it_matters: Methodologically influential for humanoid parkour follow-ups (terrain curriculum, vision encoder design).

- title: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  authors: Qiayuan Liao, Takara E. Truong, Xiaoyu Huang, Yuman Gao, Guy Tevet, Koushil Sreenath, C. Karen Liu
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2508.08241
  paper_url: https://arxiv.org/abs/2508.08241
  project_url: https://beyondmimic.github.io/
  code_url: https://github.com/HybridRobotics/BeyondMimic
  category: Locomotion
  task_tags: [motion-tracking, guided-diffusion, agile-skills, sim2real]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Compact tracking + guided diffusion policy enables aerial cartwheels, spin-kicks, and zero-shot task control on Unitree G1.
  why_it_matters: Bridges motion tracking and versatile WBC; direct successor to Mimic-style methods on real humanoids.

- title: HumanPlus: Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  category: Locomotion
  task_tags: [humanoid, shadowing, imitation, whole-body, transformer-policy]
  robot_platform: Unitree H1 (with hands)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Full-stack shadowing+imitation system; low-level policy trained on massive human MoCap, enables RGB-driven humanoid control.
  why_it_matters: Influential humanoid WBC backbone via human-motion priors; shows scaling tracking to real H1.

- title: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
  authors: Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, Guanya Shi
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.08858
  paper_url: https://arxiv.org/abs/2406.08858
  project_url: https://omni.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Locomotion
  task_tags: [whole-body, teleoperation, motion-tracking, dexterous]
  robot_platform: Unitree H1 + dexterous hands
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: RL sim-to-real WBC via kinematic-pose interface; supports VR teleop, language, and RGB control of full humanoid.
  why_it_matters: Defines universal kinematic-pose interface used across many subsequent humanoid WBC papers.

- title: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O)
  authors: Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, Guanya Shi
  year: 2024
  venue: IROS 2024
  arxiv_id: 2403.04436
  paper_url: https://arxiv.org/abs/2403.04436
  project_url: https://human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Locomotion
  task_tags: [whole-body, teleoperation, RL, motion-imitator]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Sim-to-data pipeline filters retargeted human motion; trains real-time whole-body imitator on full-size H1.
  why_it_matters: Direct precursor to OmniH2O / HOVER and most modern motion-tracking humanoids.

- title: HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots
  authors: Tairan He, Wenli Xiao, Toru Lin, Zhengyi Luo, Zhenjia Xu, Zhenyu Jiang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Linxi Fan, Yuke Zhu
  year: 2024
  venue: arXiv (NVIDIA)
  arxiv_id: 2410.21229
  paper_url: https://arxiv.org/abs/2410.21229
  project_url: https://hover-versatile-humanoid.github.io/
  code_url: https://github.com/NVlabs/HOVER
  category: Locomotion
  task_tags: [whole-body-control, multi-mode, distillation, motion-imitation]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Multi-mode distillation from a kinematic-imitation oracle yields a single policy for navigation, manipulation, tabletop, and tracking.
  why_it_matters: Canonical "generalist humanoid WBC" baseline.

- title: ExBody2: Advanced Expressive Humanoid Whole-Body Control
  authors: Mazeyu Ji, Xuanbin Peng, Fangchen Liu, Jialong Li, Ge Yang, Xuxin Cheng, Xiaolong Wang
  year: 2024
  venue: arXiv 2024 / RSS 2025
  arxiv_id: 2412.13196
  paper_url: https://arxiv.org/abs/2412.13196
  project_url: https://exbody2.github.io/
  code_url: https://github.com/Expressive-Whole-Body-Control/exbody2
  category: Locomotion
  task_tags: [whole-body-tracking, expressive, teacher-student, sim2real]
  robot_platform: Unitree H1, G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Decoupled keypoint+velocity tracking with privileged-teacher distillation for high-fidelity dynamic whole-body skills.
  why_it_matters: Strong tracking baseline; demonstrates the value of teacher-student for WBC.

- title: Expressive Whole-Body Control for Humanoid Robots (ExBody)
  authors: Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: RSS 2024
  arxiv_id: 2402.16796
  paper_url: https://arxiv.org/abs/2402.16796
  project_url: https://expressive-humanoid.github.io/
  code_url: https://github.com/chengxuxin/expressive-humanoid
  category: Locomotion
  task_tags: [whole-body, expressive, motion-imitation]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: First full-size humanoid trained to track AMASS-derived expressive whole-body motions.
  why_it_matters: Initiated the "expressive WBC" line that ExBody2/HOVER/OmniH2O extend.

- title: ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  authors: Tairan He, Jiawei Gao, Wenli Xiao, Yuanhang Zhang, Zi Wang, Jiashun Wang, Zhengyi Luo, Guanya Shi, Linxi Fan, Yuke Zhu, et al.
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.01143
  paper_url: https://arxiv.org/abs/2502.01143
  project_url: https://agile.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/ASAP
  category: Locomotion
  task_tags: [sim2real, delta-action, agile-skills, residual-learning]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Two-stage pre-train + delta-action fine-tuning closes sim-real dynamics gap for agile humanoid skills.
  why_it_matters: Dominant approach for agile sim-to-real motion tracking; widely cited 2025 baseline.

- title: KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills
  authors: Weiji Xie, Jinrui Han, Jiakun Zheng, Huanyu Li, Xinzhe Liu, Jiyuan Shi, Weinan Zhang, Chenjia Bai, Xuelong Li
  year: 2025
  venue: NeurIPS 2025
  arxiv_id: 2506.12851
  paper_url: https://arxiv.org/abs/2506.12851
  project_url: https://kungfu-bot.github.io/
  code_url: https://github.com/TeleHuman/PBHC
  category: Locomotion
  task_tags: [whole-body, kungfu, motion-tracking, adaptive-curriculum]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Bi-level adaptive tracking-tolerance curriculum enables kungfu/dance-level dynamic skills on G1.
  why_it_matters: State-of-the-art highly-dynamic motion tracking; reference for agility benchmarks.

- title: Hybrid Internal Model: Learning Agile Legged Locomotion with Simulated Robot Response (HIMLoco)
  authors: Junfeng Long, Zirui Wang, Quanyi Li, Liu Cao, Jiawei He, Jiangmiao Pang
  year: 2024
  venue: ICLR 2024
  arxiv_id: 2312.11460
  paper_url: https://arxiv.org/abs/2312.11460
  project_url: https://junfeng-long.github.io/HIMLoco/
  code_url: https://github.com/OpenRobotLab/HIMLoco
  category: Locomotion
  task_tags: [legged, hybrid-internal-model, contrastive, state-estimation]
  robot_platform: Unitree A1/Go1/Go2
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: released
  one_line: Estimates external states implicitly via contrastive embedding aligned with successor robot response.
  why_it_matters: Strong proprioceptive-only locomotion baseline used in many humanoid follow-ups.

- title: Learning Humanoid Locomotion with Perceptive Internal Model (PIM)
  authors: Junfeng Long, Junli Ren, Moji Shi, Zirui Wang, Tao Huang, Ping Luo, Jiangmiao Pang
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2411.14386
  paper_url: https://arxiv.org/abs/2411.14386
  project_url: https://junfeng-long.github.io/PIM/
  code_url: https://github.com/OpenRobotLab/HIMLoco
  category: Locomotion
  task_tags: [humanoid, perception, internal-model, terrain]
  robot_platform: Unitree H1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Extends HIM with depth-perception internal model for humanoid traversal of challenging terrain.
  why_it_matters: Influential perceptive humanoid locomotion baseline.

- title: Learning Humanoid Locomotion over Challenging Terrain
  authors: Ilija Radosavovic, Sarthak Kamat, Trevor Darrell, Jitendra Malik
  year: 2024
  venue: arXiv (Berkeley)
  arxiv_id: 2410.03654
  paper_url: https://arxiv.org/abs/2410.03654
  project_url: https://humanoid-challenging-terrain.github.io/
  code_url: n/a
  category: Locomotion
  task_tags: [humanoid, terrain, transformer, in-context]
  robot_platform: Digit
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Transformer policy for humanoid locomotion over rough/sloped/stair terrain via large-scale RL.
  why_it_matters: Direct successor to Real-World Humanoid Locomotion (Science Robotics) showing perceptive scaling.

- title: Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots (Cassie)
  authors: Zhongyu Li, Xuxin Cheng, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, Koushil Sreenath
  year: 2021
  venue: ICRA 2021
  arxiv_id: 2103.14295
  paper_url: https://arxiv.org/abs/2103.14295
  project_url: https://xbpeng.github.io/projects/Cassie_Walking/index.html
  code_url: n/a
  category: Locomotion
  task_tags: [bipedal, sim2real, parameterized-policy, domain-randomization]
  robot_platform: Cassie
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: not released
  one_line: Domain-randomized RL for parameterized bipedal walking transferred zero-shot to Cassie.
  why_it_matters: Foundational sim-to-real bipedal RL paper widely cited as baseline.

- title: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control (Cassie)
  authors: Zhongyu Li, Xue Bin Peng, Pieter Abbeel, Sergey Levine, Glen Berseth, Koushil Sreenath
  year: 2024
  venue: IJRR 2024
  arxiv_id: 2401.16889
  paper_url: https://arxiv.org/abs/2401.16889
  project_url: https://hybrid-robotics.berkeley.edu/biped/
  code_url: n/a
  category: Locomotion
  task_tags: [bipedal, dynamic, jumping, running]
  robot_platform: Cassie
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: not released
  one_line: Comprehensive RL framework for versatile dynamic bipedal skills (running, jumping, hopping) on Cassie.
  why_it_matters: Premier bipedal RL reference; spans walking through jumping with one approach.

- title: Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition (Cassie)
  authors: Jonah Siekmann, Yesh Godse, Alan Fern, Jonathan Hurst
  year: 2021
  venue: ICRA 2021
  arxiv_id: 2011.01387
  paper_url: https://arxiv.org/abs/2011.01387
  project_url: n/a
  code_url: n/a
  category: Locomotion
  task_tags: [bipedal, periodic-reward, gait-composition]
  robot_platform: Cassie
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: not released
  one_line: Periodic reward composition learns walking, running, hopping and skipping gaits transferred to Cassie.
  why_it_matters: Influential reward-design paradigm for periodic gaits, reused in humanoid locomotion.

- title: Robust Feedback Motion Policy Design Using Reinforcement Learning on a 3D Digit Bipedal Robot
  authors: Guillermo A. Castillo, Bowen Weng, Wei Zhang, Ayonga Hereid
  year: 2021
  venue: IROS 2021
  arxiv_id: 2103.15309
  paper_url: https://arxiv.org/abs/2103.15309
  project_url: n/a
  code_url: n/a
  category: Locomotion
  task_tags: [bipedal, Digit, RL, hierarchical]
  robot_platform: Digit (Agility Robotics)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: First learning-based locomotion policy zero-shot transferred to Digit hardware.
  why_it_matters: Reference Digit RL baseline; predecessor to Berkeley/MIT humanoid follow-ups.

- title: Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning
  authors: Nikita Rudin, David Hoeller, Philipp Reist, Marco Hutter
  year: 2021
  venue: CoRL 2021
  arxiv_id: 2109.11978
  paper_url: https://arxiv.org/abs/2109.11978
  project_url: https://leggedrobotics.github.io/legged_gym/
  code_url: https://github.com/leggedrobotics/legged_gym
  category: Locomotion
  task_tags: [legged, parallel-RL, IsaacGym, ANYmal]
  robot_platform: ANYmal C
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: released (legged_gym)
  one_line: GPU-parallel IsaacGym RL trains ANYmal to walk in minutes; foundational legged_gym codebase.
  why_it_matters: Backbone training framework used by nearly every humanoid/quadruped RL paper since.

- title: Learning Quadrupedal Locomotion over Challenging Terrain (ANYmal)
  authors: Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, Marco Hutter
  year: 2020
  venue: Science Robotics
  arxiv_id: 2010.11251
  paper_url: https://arxiv.org/abs/2010.11251
  project_url: https://leggedrobotics.github.io/rl-blindloco/
  code_url: n/a
  category: Locomotion
  task_tags: [legged, blind, robust-RL, ANYmal, terrain]
  robot_platform: ANYmal C
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: not released
  one_line: Proprioceptive-only RL controller drives ANYmal across challenging natural terrain.
  why_it_matters: Landmark sim-to-real legged RL paper; foundational for humanoid RL by analogy.

- title: MuJoCo Playground
  authors: Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, Mustafa Haiderbhai, Samuel Holt, Jing Yuan Luo, Arthur Allshire, Erik Frey, Koushil Sreenath, Lueder A. Kahrs, Carmelo Sferrazza, Yuval Tassa, Pieter Abbeel
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2502.08844
  paper_url: https://arxiv.org/abs/2502.08844
  project_url: https://playground.mujoco.org/
  code_url: https://github.com/google-deepmind/mujoco_playground
  category: Locomotion
  task_tags: [benchmark, MJX, sim2real, humanoid, quadruped]
  robot_platform: Berkeley Humanoid, Unitree H1/G1, Booster T1, Spot, Go1, Barkour
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: GPU-accelerated MJX-based open-source RL benchmark spanning DM Control, locomotion, and manipulation with sim2real demos.
  why_it_matters: Standard locomotion training/eval framework; central to upcoming humanoid benchmark work.

- title: GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
  authors: NVIDIA GR00T Team (Bjorck, Wang, Yang, Fan, Zhu, et al.)
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2503.14734
  paper_url: https://arxiv.org/abs/2503.14734
  project_url: https://research.nvidia.com/labs/gear/gr00t-n1/
  code_url: https://github.com/NVIDIA/Isaac-GR00T
  category: Locomotion
  task_tags: [foundation-model, VLA, dual-system, humanoid]
  robot_platform: Fourier GR-1 (also others)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released (Apache 2.0)
  one_line: Open VLA foundation model with VLM+diffusion-transformer dual-system for generalist humanoid behavior.
  why_it_matters: Industry-standard humanoid foundation model; central to high-level locomotion+manipulation stacks.

- title: Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer
  authors: Xinyang Gu, Yen-Jen Wang, Jianyu Chen
  year: 2024
  venue: arXiv (RobotEra)
  arxiv_id: 2404.05695
  paper_url: https://arxiv.org/abs/2404.05695
  project_url: https://sites.google.com/view/humanoid-gym/
  code_url: https://github.com/roboterax/humanoid-gym
  category: Locomotion
  task_tags: [humanoid, sim2sim, sim2real, IsaacGym]
  robot_platform: RobotEra XBot-S/L (also Unitree H1)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Open IsaacGym-based humanoid locomotion training framework with built-in sim-to-sim Mujoco verification.
  why_it_matters: Widely used humanoid locomotion baseline framework, especially in Chinese humanoid ecosystem.

- title: Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking (GMR)
  authors: João Araújo, Yanjie Ze, et al.
  year: 2025
  venue: ICRA 2026
  arxiv_id: 2510.02252
  paper_url: https://arxiv.org/abs/2510.02252
  project_url: https://jaraujo98.github.io/retargeting_matters/
  code_url: https://github.com/YanjieZe/GMR
  category: Locomotion
  task_tags: [retargeting, motion-tracking, humanoid]
  robot_platform: multiple humanoids (G1, H1, etc.)
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Open retargeter that fixes foot sliding/penetration/self-intersection across humanoid embodiments in real time.
  why_it_matters: Foundational tooling for whole-body tracking pipelines; quality of retargeting bounds tracking quality.

- title: Coordinated Humanoid Locomotion with Symmetry Equivariant RL Policy (Symmetry-Aware)
  authors: Buqing Nie, Yangqing Fu, Jingtian Ji, Yanjie Ze, Xuxin Cheng, Yue Gao
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2508.01247
  paper_url: https://arxiv.org/abs/2508.01247
  project_url: n/a
  code_url: n/a
  category: Locomotion
  task_tags: [symmetry-equivariant, humanoid, policy-architecture]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Strict symmetry-equivariant actor and symmetry-invariant critic improve velocity tracking up to 40% on G1.
  why_it_matters: Architectural inductive bias improves humanoid coordination; relevant to symmetric WBC.

- title: PhysHSI: Towards Real-World Generalizable and Natural Humanoid-Scene Interaction
  authors: Huayi Wang, Wentao Zhang, Runyi Yu, et al.
  year: 2025
  venue: arXiv 2025
  arxiv_id: 2510.11072
  paper_url: https://arxiv.org/abs/2510.11072
  project_url: https://physhsi.github.io/
  code_url: n/a
  category: Locomotion
  task_tags: [humanoid-scene-interaction, sit-down, climb, motion-tracking]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Real-world generalizable humanoid-scene interaction (sitting, climbing, manipulating) via tracking + adversarial priors.
  why_it_matters: Closes the gap between physics-based scene-interaction (InterPhys/SceneIM) and real humanoids.

---

## Physics-Based Character Animation

- title: DeepMimic: Example-Guided Deep RL of Physics-Based Character Skills
  authors: Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne
  year: 2018
  venue: SIGGRAPH 2018
  arxiv_id: 1804.02717
  paper_url: https://arxiv.org/abs/1804.02717
  project_url: https://xbpeng.github.io/projects/DeepMimic/index.html
  code_url: https://github.com/xbpeng/DeepMimic
  category: Physics-Anim
  task_tags: [motion-imitation, RL, reference-tracking, foundational]
  robot_platform: sim-only humanoid (PyBullet)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Reference-guided RL imitates motion clips with robust recovery; defines the motion-tracking paradigm.
  why_it_matters: Single most foundational physics-based character paper; underlies all subsequent humanoid motion tracking.

- title: AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control
  authors: Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
  year: 2021
  venue: SIGGRAPH 2021
  arxiv_id: 2104.02180
  paper_url: https://arxiv.org/abs/2104.02180
  project_url: https://xbpeng.github.io/projects/AMP/index.html
  code_url: https://github.com/xbpeng/DeepMimic (AMP branch)
  category: Physics-Anim
  task_tags: [adversarial-imitation, motion-prior, GAIL, style-reward]
  robot_platform: sim-only humanoid (Isaac/PyBullet)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released (IsaacGymEnvs port available)
  one_line: GAIL-style discriminator provides style reward over unstructured motion clips for physics characters.
  why_it_matters: Standard motion-prior backbone; reused in AMP-LMP, AMP-Loco, ASE, etc., on real humanoids.

- title: ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters
  authors: Xue Bin Peng, Yunrong Guo, Lina Halper, Sergey Levine, Sanja Fidler
  year: 2022
  venue: SIGGRAPH 2022
  arxiv_id: 2205.01906
  paper_url: https://arxiv.org/abs/2205.01906
  project_url: https://xbpeng.github.io/projects/ASE/index.html
  code_url: https://github.com/nv-tlabs/ASE
  category: Physics-Anim
  task_tags: [skill-embedding, unsupervised-RL, latent-space, downstream-tasks]
  robot_platform: sim-only humanoid (IsaacGym)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Reusable latent skill embedding via adversarial imitation+unsupervised RL for downstream task control.
  why_it_matters: Defines reusable humanoid skill priors used as building block in many WBC works.

- title: CALM: Conditional Adversarial Latent Models for Directable Virtual Characters
  authors: Chen Tessler, Yoni Kasten, Yunrong Guo, Shie Mannor, Gal Chechik, Xue Bin Peng
  year: 2023
  venue: SIGGRAPH 2023
  arxiv_id: 2305.02195
  paper_url: https://arxiv.org/abs/2305.02195
  project_url: https://research.nvidia.com/labs/par/calm/
  code_url: https://github.com/NVlabs/CALM
  category: Physics-Anim
  task_tags: [skill-embedding, directable, motion-encoder]
  robot_platform: sim-only humanoid (IsaacGym)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Joint motion encoder + control policy yields semantic latent space for directable character skills.
  why_it_matters: Bridge between AMP/ASE and downstream task control; used in NVIDIA character pipelines.

- title: MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting
  authors: Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, Xue Bin Peng
  year: 2024
  venue: SIGGRAPH Asia 2024
  arxiv_id: 2409.14393
  paper_url: https://arxiv.org/abs/2409.14393
  project_url: https://research.nvidia.com/labs/par/maskedmimic/
  code_url: https://github.com/NVlabs/ProtoMotions
  category: Physics-Anim
  task_tags: [motion-inpainting, unified-control, masked-tracking]
  robot_platform: sim-only humanoid (IsaacGym/IsaacLab via ProtoMotions)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released (in ProtoMotions)
  one_line: Single unified policy controls full-body humanoid by inpainting masked keyframes/text/objects.
  why_it_matters: State-of-the-art unified character controller; the recipe being transferred to real humanoid robots.

- title: Perpetual Humanoid Control for Real-time Simulated Avatars (PHC)
  authors: Zhengyi Luo, Jinkun Cao, Alexander Winkler, Kris Kitani, Weipeng Xu
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2305.06456
  paper_url: https://arxiv.org/abs/2305.06456
  project_url: https://www.zhengyiluo.com/PHC-Site/
  code_url: https://github.com/ZhengyiLuo/PHC
  category: Physics-Anim
  task_tags: [motion-imitation, fail-recovery, scaling, AMASS]
  robot_platform: sim-only SMPL humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Progressive Multiplicative Control Policy scales motion imitation to 10K AMASS clips with fail-state recovery.
  why_it_matters: Reference oracle imitator used to generate teacher data for many real-humanoid WBC pipelines.

- title: Universal Humanoid Motion Representations for Physics-Based Control (PULSE)
  authors: Zhengyi Luo, Jinkun Cao, Josh Merel, Alexander Winkler, Jing Huang, Kris Kitani, Weipeng Xu
  year: 2024
  venue: ICLR 2024 (spotlight)
  arxiv_id: 2310.04582
  paper_url: https://arxiv.org/abs/2310.04582
  project_url: https://www.zhengyiluo.com/PULSE-Site/
  code_url: https://github.com/ZhengyiLuo/PULSE
  category: Physics-Anim
  task_tags: [motion-representation, latent-space, distillation, downstream]
  robot_platform: sim-only SMPL humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Distills PHC into a variational latent skill space spanning all human motor skills.
  why_it_matters: Universal motion latent reused as prior across tracking, VR avatars, grasping, locomotion.

- title: MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control
  authors: Nolan Wagener, Andrey Kolobov, Felipe Vieira Frujeri, Ricky Loynd, Ching-An Cheng, Matthew Hausknecht
  year: 2022
  venue: NeurIPS 2022 D&B
  arxiv_id: 2208.07363
  paper_url: https://arxiv.org/abs/2208.07363
  project_url: https://microsoft.github.io/MoCapAct/
  code_url: https://github.com/microsoft/MoCapAct
  category: Physics-Anim
  task_tags: [dataset, dm_control, expert-rollouts, hierarchical-policy]
  robot_platform: dm_control humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Released ~3.5h of CMU MoCap experts + rollouts in dm_control for downstream humanoid learning.
  why_it_matters: Standard dataset for hierarchical humanoid skill learning; basis for follow-up GPT motion-completion work.

- title: ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters
  authors: Heyuan Yao, Zhenhua Song, Baoquan Chen, Libin Liu
  year: 2022
  venue: SIGGRAPH Asia 2022
  arxiv_id: 2210.06063
  paper_url: https://arxiv.org/abs/2210.06063
  project_url: https://heyuanyao-pku.github.io/Control-VAE/
  code_url: https://github.com/heyuanYao-pku/Control-VAE
  category: Physics-Anim
  task_tags: [VAE, model-based, generative-controller]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: World-model + VAE learns skill-conditioned generative controllers for diverse character behaviors.
  why_it_matters: Influential model-based alternative to AMP/ASE for character control.

- title: Physics-based Character Controllers Using Conditional VAEs (PhysicsVAE)
  authors: Jungdam Won, Deepak Gopinath, Jessica Hodgins
  year: 2022
  venue: SIGGRAPH 2022
  arxiv_id: n/a
  paper_url: https://research.facebook.com/publications/physics-based-character-controllers-using-conditional-vaes/
  project_url: n/a
  code_url: https://github.com/facebookresearch/PhysicsVAE
  category: Physics-Anim
  task_tags: [conditional-VAE, character-control]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Conditional VAE physics-based character controller mapping kinematic guidance to PD targets.
  why_it_matters: Concurrent latent-space skill controller; companion to ControlVAE.

- title: Neural Categorical Priors for Physics-Based Character Control (NCP)
  authors: Qingxu Zhu, He Zhang, Mengting Lan, Lei Han
  year: 2023
  venue: SIGGRAPH Asia 2023
  arxiv_id: 2308.07200
  paper_url: https://arxiv.org/abs/2308.07200
  project_url: https://tencent-roboticsx.github.io/NCP/
  code_url: https://github.com/Tencent-RoboticsX/NCP
  category: Physics-Anim
  task_tags: [VQ-VAE, categorical-prior, motion-imitation, sword-shield]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: VQ-VAE discrete motion prior + curiosity-shifted categorical prior yields high-quality diverse skills.
  why_it_matters: Notable improvement over AMP/ASE in motion quality and diversity; uses discrete latent.

- title: A Scalable Approach to Control Diverse Behaviors for Physically Simulated Characters (ScaDiver)
  authors: Jungdam Won, Deepak Gopinath, Jessica Hodgins
  year: 2020
  venue: SIGGRAPH 2020
  arxiv_id: n/a
  paper_url: https://dl.acm.org/doi/10.1145/3386569.3392381
  project_url: n/a
  code_url: https://github.com/facebookresearch/ScaDiver
  category: Physics-Anim
  task_tags: [diverse-behaviors, scalable, motion-imitation]
  robot_platform: sim-only humanoid (PyBullet)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Scalable mixture-of-experts framework imitating large unstructured motion clips.
  why_it_matters: Early scalable character imitation method; precursor to PHC scaling ideas.

- title: DReCon: Data-Driven Responsive Control of Physics-Based Characters
  authors: Kevin Bergamin, Simon Clavet, Daniel Holden, James Forbes
  year: 2019
  venue: SIGGRAPH Asia 2019
  arxiv_id: n/a
  paper_url: https://dl.acm.org/doi/10.1145/3355089.3356536
  project_url: https://www.ubisoft.com/en-us/studio/laforge/news/VjEIwquaIyEZZSw5RZI0V/drecon-datadriven-responsive-control-of-physicsbased-characters
  code_url: n/a
  category: Physics-Anim
  task_tags: [motion-matching, RL, responsive-control]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Couples motion-matching kinematic generator with DRL physics tracker for responsive game characters.
  why_it_matters: Influential commercial-grade character animation pipeline; informs hybrid kinematic+physics designs.

- title: PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction
  authors: Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian Zhang, Lei Zhang
  year: 2023
  venue: arXiv 2023
  arxiv_id: 2312.04393
  paper_url: https://arxiv.org/abs/2312.04393
  project_url: https://wyhuai.github.io/physhoi-page/
  code_url: https://github.com/wyhuai/PhysHOI
  category: Physics-Anim
  task_tags: [HOI, contact-graph, basketball, physics-imitation]
  robot_platform: sim-only humanoid (IsaacGym)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Contact-graph reward enables physics-based imitation of full-body human-object interactions (basketball).
  why_it_matters: First reward-free HOI physics imitator; basis for InterMimic and HOI WBC follow-ups.

- title: InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions
  authors: Sirui Xu, Hung Yu Ling, Yu-Xiong Wang, Liang-Yan Gui
  year: 2025
  venue: CVPR 2025 (Highlight)
  arxiv_id: 2502.20390
  paper_url: https://arxiv.org/abs/2502.20390
  project_url: https://sirui-xu.github.io/InterMimic/
  code_url: https://github.com/Sirui-Xu/InterMimic
  category: Physics-Anim
  task_tags: [HOI, whole-body, curriculum, teacher-student, generative]
  robot_platform: sim-only SMPL-X / Unitree G1
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Per-subject teacher distillation + RL fine-tuning yields a universal HOI WBC policy spanning hours of MoCap.
  why_it_matters: State-of-the-art whole-body HOI controller; explicitly compatible with G1 robot embodiment.

- title: Synthesizing Physical Character-Scene Interactions (InterPhys 2023)
  authors: Mohamed Hassan, Yunrong Guo, Tingwu Wang, Michiel van de Panne, Sanja Fidler, Xue Bin Peng
  year: 2023
  venue: SIGGRAPH 2023
  arxiv_id: 2302.00883
  paper_url: https://arxiv.org/abs/2302.00883
  project_url: https://xbpeng.github.io/projects/InterPhys/index.html
  code_url: n/a
  category: Physics-Anim
  task_tags: [scene-interaction, adversarial-imitation, sit-down, carry]
  robot_platform: sim-only humanoid (IsaacGym)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: AMP-style adversarial imitation learns sit/lie/carry/move scene-interaction skills from unannotated MoCap.
  why_it_matters: Reference for scene-interaction WBC; informs PhysHSI/HumanoidVerse on real robots.

- title: Omnigrasp: Grasping Diverse Objects with Simulated Humanoids
  authors: Zhengyi Luo, Jinkun Cao, Sammy Christen, Alexander Winkler, Kris Kitani, Weipeng Xu
  year: 2024
  venue: NeurIPS 2024
  arxiv_id: 2407.11385
  paper_url: https://arxiv.org/abs/2407.11385
  project_url: https://www.zhengyiluo.com/Omnigrasp-Site/
  code_url: https://github.com/ZhengyiLuo/Omnigrasp
  category: Physics-Anim
  task_tags: [whole-body-grasping, dexterous, motion-prior, hierarchical-RL]
  robot_platform: sim-only SMPL-X humanoid with hands
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: Hierarchical RL on PULSE motion prior enables a humanoid to grasp 1200+ objects on diverse trajectories.
  why_it_matters: State-of-the-art whole-body humanoid grasping; reference for loco-manipulation priors.

- title: PhysDiff: Physics-Guided Human Motion Diffusion Model
  authors: Ye Yuan, Jiaming Song, Umar Iqbal, Arash Vahdat, Jan Kautz
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2212.02500
  paper_url: https://arxiv.org/abs/2212.02500
  project_url: https://nvlabs.github.io/PhysDiff/
  code_url: n/a
  category: Physics-Anim
  task_tags: [motion-diffusion, physics-projection, motion-imitator]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Physics-based projection module corrects motion-diffusion outputs for plausibility (>78% improvement).
  why_it_matters: Bridges generative motion models and physics-based characters; foundational for diffusion+physics line.

- title: PhysCap: Physically Plausible Monocular 3D Motion Capture in Real Time
  authors: Soshi Shimada, Vladislav Golyanik, Weipeng Xu, Christian Theobalt
  year: 2020
  venue: SIGGRAPH Asia 2020
  arxiv_id: 2008.08880
  paper_url: https://arxiv.org/abs/2008.08880
  project_url: https://vcai.mpi-inf.mpg.de/projects/PhysCap/
  code_url: n/a
  category: Physics-Anim
  task_tags: [motion-capture, physics-aware, monocular, RGB]
  robot_platform: physics-based human (rigid body)
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: First real-time physics-plausible monocular 3D motion capture with contact and balance constraints.
  why_it_matters: Foundational physics-aware mocap; supplies clean reference motions for downstream WBC.

- title: PDP: Physics-Based Character Animation via Diffusion Policy
  authors: Takara Truong, Michael Piseno, Zhaoming Xie, C. Karen Liu
  year: 2024
  venue: SIGGRAPH Asia 2024
  arxiv_id: 2406.00960
  paper_url: https://arxiv.org/abs/2406.00960
  project_url: https://stanford-tml.github.io/PDP.github.io/
  code_url: n/a
  category: Physics-Anim
  task_tags: [diffusion-policy, behavior-cloning, perturbation-recovery]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Diffusion policy trained on noisy-state/clean-action pairs yields robust physics character control.
  why_it_matters: Establishes diffusion as a viable physics-character backbone, used by BeyondMimic on real robots.

- title: ProtoMotions
  authors: Chen Tessler, Yunrong Guo, et al. (NVIDIA)
  year: 2024
  venue: code release / framework
  arxiv_id: n/a
  paper_url: n/a
  project_url: https://nvlabs.github.io/ProtoMotions/
  code_url: https://github.com/NVlabs/ProtoMotions
  category: Physics-Anim
  task_tags: [framework, IsaacLab, IsaacGym, retargeting, terrain]
  robot_platform: SMPL humanoid + Unitree G1 retargeting
  uses_real_robot: true (zero-shot G1)
  uses_humanoid: true
  uses_simulation: true
  code_status: released
  one_line: GPU-accelerated open framework spanning Newton/IsaacGym/IsaacLab/Genesis backends for humanoid character+robot RL.
  why_it_matters: Reference codebase for MaskedMimic, BFM-Zero, and many recent humanoid+animation papers.

- title: AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning
  authors: Lucas Stadler, et al.
  year: 2025
  venue: SIGGRAPH 2025
  arxiv_id: 2505.23708
  paper_url: https://arxiv.org/abs/2505.23708
  project_url: n/a
  code_url: n/a
  category: Physics-Anim
  task_tags: [multi-objective-RL, adaptive-character-control]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Multi-objective RL adapts character behaviors across reward trade-offs at deployment time.
  why_it_matters: Recent improvement in adaptive physics character control.

- title: ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators
  authors: Ziyu Zhang, Sergey Bashkirov, Dun Yang, Michael Taylor, Xue Bin Peng
  year: 2025
  venue: SIGGRAPH 2025
  arxiv_id: 2505.04961
  paper_url: https://arxiv.org/abs/2505.04961
  project_url: https://add-imitation.github.io/
  code_url: n/a
  category: Physics-Anim
  task_tags: [adversarial, motion-imitation, single-objective]
  robot_platform: sim-only humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: not released
  one_line: Differential discriminator that operates on state differences enables high-quality single-objective imitation.
  why_it_matters: Improves AMP-family discriminators for tracking quality; useful for humanoid WBC.

- title: PhysMotion: Physics-Grounded Dynamics From a Single Image
  authors: Tianyi Xie, Yiwei Zhao, Ying Jiang, Chenfanfu Jiang
  year: 2024
  venue: arXiv 2024
  arxiv_id: 2411.17189
  paper_url: https://arxiv.org/abs/2411.17189
  project_url: https://supertan0204.github.io/physmotion_website/
  code_url: n/a
  category: Physics-Anim
  task_tags: [MPM, image-to-video, physics-simulation]
  robot_platform: differentiable MPM (continuum)
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: true
  code_status: not released
  one_line: Single-image to physics-grounded video using differentiable MPM + diffusion refinement.
  why_it_matters: Generative physics counterpart to character animation; useful for object/scene priors.

---

(End of slice. ~46 entries.)
