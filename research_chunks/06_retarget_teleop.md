# Human-to-Humanoid Retargeting + Teleoperation / Demonstration Collection (2022–2026)

Curated list of papers covering retargeting pipelines (kinematic / dynamic / interaction-preserving) and teleoperation systems (VR, exoskeleton, mocap-glove, AR, smart-glasses, hand-held grippers) used to bridge humans and (mostly) humanoid robots and to scale demonstration collection.

---

## Retargeting

- title: Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking (GMR)
  authors: João Pedro Araújo, Yanjie Ze, et al.
  year: 2025
  venue: ICRA 2026
  arxiv_id: 2510.02252
  paper_url: https://arxiv.org/abs/2510.02252
  project_url: https://jaraujo98.github.io/retargeting_matters/
  code_url: https://github.com/YanjieZe/GMR
  category: Retargeting
  task_tags: [motion-retarget, humanoid, MoCap, real-time, IK]
  robot_platform: Unitree G1/H1, Apptronik Apollo, Booster, multiple humanoids
  uses_real_robot: yes (downstream policies)
  uses_humanoid: yes
  uses_simulation: yes (MuJoCo)
  code_status: open-source (Python, real-time CPU)
  one_line: Multi-objective IK retargeter that fixes scaling/foot-sliding/penetration artifacts and serves as the retargeter for TWIST.
  why_it_matters: Open-source baseline that consistently beats prior open retargeters and approaches closed-source quality; widely adopted for humanoid motion-tracking pipelines.

- title: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
  authors: Lujie Yang, Xiangyun Huang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2509.26633
  paper_url: https://arxiv.org/abs/2509.26633
  project_url: https://huggingface.co/papers/2509.26633
  code_url: https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset
  category: Retargeting
  task_tags: [interaction-mesh, loco-manipulation, scene-interaction, dataset]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: dataset released; engine code partial
  one_line: Interaction-mesh based retargeter that preserves agent–terrain–object contacts, enabling 30s parkour/loco-manipulation from MoCap.
  why_it_matters: First retargeting pipeline to explicitly model human-object-environment interactions, producing 8h of contact-rich trajectories.

- title: Perpetual Humanoid Control for Real-time Simulated Avatars (PHC)
  authors: Zhengyi Luo, et al.
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2305.06456
  paper_url: https://arxiv.org/abs/2305.06456
  project_url: https://www.zhengyiluo.com/PHC-Site/
  code_url: https://github.com/ZhengyiLuo/PHC
  category: Retargeting
  task_tags: [SMPL-to-humanoid, motion-imitation, fail-recovery, simulation]
  robot_platform: SMPL humanoid, Unitree H1 (PHC-MJX fork)
  uses_real_robot: no
  uses_humanoid: yes (sim)
  uses_simulation: yes (Isaac Gym)
  code_status: open-source (widely forked)
  one_line: Progressive multiplicative control policy that scales motion imitation to 10K clips with fail-state recovery; foundational SMPL-to-humanoid retargeter.
  why_it_matters: De-facto baseline for sim humanoid imitation and motion retargeting; underpins H2O, OmniH2O, HOVER pipelines.

- title: Mink — Differential Inverse Kinematics in Python (MuJoCo)
  authors: Kevin Zakka
  year: 2024
  venue: open-source library
  arxiv_id: n/a
  paper_url: https://kevinzakka.github.io/mink/
  project_url: https://kevinzakka.github.io/mink/
  code_url: https://github.com/kevinzakka/mink
  category: Retargeting
  task_tags: [IK, retargeting-tool, MuJoCo, library]
  robot_platform: G1, H1, Apollo, dual arms, dexterous hands
  uses_real_robot: yes (downstream)
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Composable task-space IK on MuJoCo used by GMR, ProtoMotions, and many teleop stacks for retargeting and live tracking.
  why_it_matters: The standard differential IK toolbox that most modern retargeting/teleop pipelines rely on.

- title: Implicit Kinodynamic Motion Retargeting for Human-to-Humanoid Imitation Learning (IKMR)
  authors: Haodong Zhang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2509.15443
  paper_url: https://arxiv.org/abs/2509.15443
  project_url: n/a
  code_url: not released yet
  category: Retargeting
  task_tags: [kinodynamic, neural-retarget, scalable, humanoid]
  robot_platform: full-size humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: not yet released
  one_line: Neural retargeter that jointly considers kinematics and dynamics, refining trajectories to physically feasible ones at scale.
  why_it_matters: Argues IK-only retargeting is insufficient; couples retargeter with imitation policy for end-to-end physical feasibility.

- title: DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation
  authors: Mandi Zhao, et al.
  year: 2025
  venue: NeurIPS 2025
  arxiv_id: 2505.24853
  paper_url: https://arxiv.org/abs/2505.24853
  project_url: https://project-dexmachina.github.io/
  code_url: https://github.com/MandiZhao/dexmachina
  category: Retargeting
  task_tags: [dexterous, bimanual, functional-retarget, virtual-controller]
  robot_platform: multiple dexterous hands
  uses_real_robot: no
  uses_humanoid: partial
  uses_simulation: yes
  code_status: open-source
  one_line: Functional retargeting via decaying virtual object controllers for long-horizon bimanual articulated-object manipulation from human demos.
  why_it_matters: Establishes a benchmark for retargeting human-object trajectories to diverse robot hands and compares hardware designs.

- title: AnyDexGrasp: General Dexterous Grasping for Different Hands with Human-level Learning Efficiency
  authors: Hao-Shu Fang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.16420
  paper_url: https://arxiv.org/abs/2502.16420
  project_url: https://graspnet.net/anydexgrasp/
  code_url: partial release
  category: Retargeting
  task_tags: [cross-embodiment, dexterous-grasp, contact-representation]
  robot_platform: 3 dexterous hands
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: partial open-source
  one_line: Two-stage cross-embodiment grasping using a contact-centric grasp representation that retargets to any hand.
  why_it_matters: Shows hand-agnostic intermediate representations enable human-level data efficiency for new robot hands.

- title: SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
  authors: Zhengyi Luo, et al. (NVIDIA GEAR)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2511.07820
  paper_url: https://arxiv.org/abs/2511.07820
  project_url: https://nvlabs.github.io/GEAR-SONIC/
  code_url: https://github.com/NVlabs/GR00T-WholeBodyControl
  category: Retargeting
  task_tags: [foundation-model, motion-tracking, VR-teleop, scaling]
  robot_platform: humanoid (G1, H1)
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source (GR00T-WholeBodyControl release)
  one_line: 42M-parameter motion-tracking foundation model trained on 100M frames; supports VR teleop, video, and VLA inputs through a unified token space.
  why_it_matters: Demonstrates that scaling motion-tracking yields a generalist humanoid controller usable as a substrate for retargeting and teleoperation.

- title: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2508.08241
  paper_url: https://arxiv.org/abs/2508.08241
  project_url: n/a
  code_url: announced
  category: Retargeting
  task_tags: [diffusion-policy, motion-tracking, sim-to-real, agile-skills]
  robot_platform: Unitree G1/H1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: code release announced
  one_line: Distills motion-tracking policies into a guided diffusion controller capable of cartwheels, spin-kicks, joystick teleop, and waypoint nav.
  why_it_matters: Bridges retargeting + tracking + flexible test-time control under one diffusion policy.

- title: HumanoidVerse: A Versatile Multi-Simulator Humanoid Learning Framework
  authors: LeCAR Lab
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2508.16943
  paper_url: https://arxiv.org/abs/2508.16943
  project_url: https://github.com/LeCAR-Lab/HumanoidVerse
  code_url: https://github.com/LeCAR-Lab/HumanoidVerse
  category: Retargeting
  task_tags: [framework, multi-sim, retargeting, motion-imitation]
  robot_platform: Unitree G1/H1, multiple
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes (IsaacGym/IsaacSim/Genesis)
  code_status: open-source
  one_line: Modular multi-simulator framework for humanoid skill learning with retargeted human MoCap, used by ASAP and follow-ups.
  why_it_matters: Provides standardized infrastructure for retargeting-based humanoid imitation across simulators.

- title: ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  authors: Tairan He, et al.
  year: 2025
  venue: RSS 2025
  arxiv_id: 2502.01143
  paper_url: https://arxiv.org/abs/2502.01143
  project_url: https://agile.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/ASAP
  category: Retargeting
  task_tags: [sim-to-real, residual-action, agile-skills, retarget]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Two-stage pipeline: pretrain motion-tracking on retargeted MoCap, then learn delta action model in real to close sim-to-real gap.
  why_it_matters: Productionizes retargeted MoCap data into agile real-world humanoid skills.

- title: HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2510.03022
  paper_url: https://arxiv.org/abs/2510.03022
  project_url: https://humanoid-exo.github.io/
  code_url: announced
  category: Retargeting
  task_tags: [exoskeleton, retargeting, whole-body, demonstration]
  robot_platform: humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: pending
  one_line: Wearable whole-body exoskeleton that retargets human motion onto humanoids while collecting scalable demonstration data.
  why_it_matters: Combines retargeting and demo-collection in one wearable for full-body humanoid skill learning.

---

## Teleoperation / Demonstration Collection

- title: Open-TeleVision: Teleoperation with Immersive Active Visual Feedback
  authors: Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.01512
  paper_url: https://arxiv.org/abs/2407.01512
  project_url: https://robot-tv.github.io/
  code_url: https://github.com/OpenTeleVision/TeleVision
  category: Teleoperation
  task_tags: [VR, stereo-vision, immersive, bimanual]
  robot_platform: Unitree H1, Fourier GR1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: VR-based stereo-feedback teleop with active head tracking on humanoids; reference baseline for many follow-ups.
  why_it_matters: Standardized open VR teleop stack for humanoid arms+hands; widely re-used by MotionTrans, iDP3, and others.

- title: HumanPlus: Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  category: Teleoperation
  task_tags: [shadowing, RGB-camera, whole-body, imitation]
  robot_platform: 33-DoF custom humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes (Isaac Gym)
  code_status: open-source
  one_line: Real-time whole-body shadowing from a single RGB camera; enables teleoperated demo collection for autonomous humanoid skills.
  why_it_matters: First open shadowing pipeline; pretrained on 40h MoCap and demonstrates dexterous humanoid skills with few-shot IL.

- title: H2O: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  authors: Tairan He, Zhengyi Luo, et al.
  year: 2024
  venue: IROS 2024 (oral)
  arxiv_id: 2403.04436
  paper_url: https://arxiv.org/abs/2403.04436
  project_url: https://human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Teleoperation
  task_tags: [RL, sim-to-real, whole-body, RGB-camera]
  robot_platform: Unitree H1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes (Isaac Gym)
  code_status: open-source
  one_line: First learning-based real-time whole-body humanoid teleoperation; uses sim-to-data filtering of MoCap with privileged imitator.
  why_it_matters: Established the recipe (retarget→filter→imitate→deploy) used by OmniH2O, HOVER, ExBody2.

- title: OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
  authors: Tairan He, Zhengyi Luo, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.08858
  paper_url: https://arxiv.org/abs/2406.08858
  project_url: https://omni.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Teleoperation
  task_tags: [VR, dexterous, multimodal-control, whole-body, dataset]
  robot_platform: Unitree H1 + dexterous hands
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Universal kinematic-pose interface supports VR, verbal, RGB control of full-sized dexterous humanoids; releases OmniH2O-6 dataset.
  why_it_matters: Productionizes humanoid teleop with multiple input modalities and downstream autonomy.

- title: HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots
  authors: Tairan He, et al.
  year: 2025
  venue: ICRA 2025
  arxiv_id: 2410.21229
  paper_url: https://arxiv.org/abs/2410.21229
  project_url: https://hover-versatile-humanoid.github.io/
  code_url: https://github.com/NVlabs/HOVER
  category: Teleoperation
  task_tags: [policy-distillation, multi-mode, motion-imitation, whole-body]
  robot_platform: Unitree H1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Distills multiple control modes (root, joint, keypoint) into one policy via shared kinematic motion-imitation abstraction.
  why_it_matters: Unifies command spaces for navigation/manipulation/teleop; eliminates per-mode retraining.

- title: ExBody2: Advanced Expressive Humanoid Whole-Body Control
  authors: Mazeyu Ji, et al.
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2412.13196
  paper_url: https://arxiv.org/abs/2412.13196
  project_url: https://exbody2.github.io/
  code_url: https://github.com/Beanpow/ExBody2
  category: Teleoperation
  task_tags: [whole-body, motion-tracking, expressive, sim-to-real]
  robot_platform: Unitree H1, G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: partially open-source
  one_line: Decouples velocity from keypoint tracking and uses privileged-teacher distillation for high-fidelity expressive humanoid control.
  why_it_matters: Strong baseline for retargeted-MoCap whole-body tracking on commercial humanoids.

- title: HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit
  authors: BeBenson, et al. (InternRobotics / OpenRobotLab)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.13013
  paper_url: https://arxiv.org/abs/2502.13013
  project_url: https://homietele.github.io/
  code_url: https://github.com/OpenRobotLab/OpenHomie
  category: Teleoperation
  task_tags: [exoskeleton, glove, pedal, semi-autonomous, loco-manipulation]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: $500 cockpit (isomorphic exoskeleton arms + Hall-sensor gloves + pedal) plus RL pedal-mapped locomotion policy for humanoids.
  why_it_matters: Low-cost open hardware+software stack that enables fast humanoid teleop with full whole-body coordination.

- title: TWIST: Teleoperated Whole-Body Imitation System
  authors: Yanjie Ze, Zixuan Chen, João Araújo, Zi-ang Cao, Xue Bin Peng, Jiajun Wu, Karen Liu
  year: 2025
  venue: CoRL 2025
  arxiv_id: 2505.02833
  paper_url: https://arxiv.org/abs/2505.02833
  project_url: https://yanjieze.com/TWIST/
  code_url: https://github.com/YanjieZe/TWIST
  category: Teleoperation
  task_tags: [whole-body, RL+BC, MoCap-suit, retargeting]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Single neural controller for whole-body teleop trained with RL+BC over GMR-retargeted human MoCap, executing dynamic G1 skills.
  why_it_matters: Shows unified network can teleop locomotion + manipulation + expressive motion; uses GMR retargeter.

- title: CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks
  authors: Yutang Lin, et al.
  year: 2025
  venue: CoRL 2025
  arxiv_id: 2506.08931
  paper_url: https://arxiv.org/abs/2506.08931
  project_url: https://humanoid-clone.github.io/
  code_url: https://github.com/humanoid-clone/CLONE
  category: Teleoperation
  task_tags: [MoE, MR-headset, LiDAR-odometry, closed-loop, drift-correction]
  robot_platform: Unitree H1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: MoE whole-body policy + LiDAR odometry closed-loop teleop achieving 12 cm drift over 8.9 m using only head/hand MR tracking.
  why_it_matters: First long-horizon whole-body humanoid teleop with closed-loop drift correction; opens pick-and-place data at scale.

- title: OpenWBT / Real-world-Ready Skill Space (R2S2)
  authors: Zekai Zhao, et al. (Galaxy General Robotics)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2505.10918
  paper_url: https://arxiv.org/abs/2505.10918
  project_url: https://zzk273.github.io/R2S2/
  code_url: https://github.com/GalaxyGeneralRobotics/OpenWBT
  category: Teleoperation
  task_tags: [VR, skill-library, latent-space, whole-body, joystick]
  robot_platform: Unitree G1, H1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Open VR-and-joystick whole-body humanoid teleop built on a sim2real-validated skill latent space (R2S2).
  why_it_matters: Production-quality open teleop for G1/H1; supports both simulation and real robots out of the box.

- title: Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation
  authors: Zipeng Fu, Tony Zhao, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2401.02117
  paper_url: https://arxiv.org/abs/2401.02117
  project_url: https://mobile-aloha.github.io/
  code_url: https://github.com/MarkFzp/mobile-aloha
  category: Teleoperation
  task_tags: [bimanual, mobile-base, leader-follower, demonstration]
  robot_platform: Mobile ALOHA (custom mobile bimanual)
  uses_real_robot: yes
  uses_humanoid: no (humanoid-adjacent)
  uses_simulation: no
  code_status: open-source
  one_line: $32K mobile bimanual teleop platform enabling whole-body data collection at human walking speed.
  why_it_matters: Catalyzed the household-task IL trend; co-training recipe achieves 80%+ on mobile manipulation with 50 demos.

- title: AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System
  authors: Yuzhe Qin, et al.
  year: 2023
  venue: RSS 2023
  arxiv_id: 2307.04577
  paper_url: https://arxiv.org/abs/2307.04577
  project_url: https://yzqin.github.io/anyteleop/
  code_url: https://github.com/dexsuite/dex-retargeting
  category: Teleoperation
  task_tags: [vision-based, dexterous, retargeting, multi-camera]
  robot_platform: Allegro, Shadow Hand, multiple arms
  uses_real_robot: yes
  uses_humanoid: no (dexterous-arm)
  uses_simulation: yes
  code_status: open-source (dex-retargeting library)
  one_line: General vision-based dexterous arm-hand teleop with hardware/sim/camera-agnostic retargeting library.
  why_it_matters: dex-retargeting is the canonical open hand-retargeter used by hundreds of follow-up systems.

- title: ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation
  authors: Shiqi Yang, Minghuan Liu, Yuzhe Qin, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2408.11805
  paper_url: https://arxiv.org/abs/2408.11805
  project_url: https://ace-teleop.github.io/
  code_url: https://github.com/ACE-Teleop/ACE
  category: Teleoperation
  task_tags: [exoskeleton, hand-tracking, cross-embodiment, low-cost]
  robot_platform: humanoid hands, arm-hand, quadruped-gripper
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source
  one_line: Hand-facing camera + portable exoskeleton enabling precise wrist+finger teleop across many embodiments.
  why_it_matters: Cross-embodiment open teleop; widely re-used as hardware reference.

- title: ACE-F: A Cross Embodiment Foldable System with Force Feedback for Dexterous Teleoperation
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2511.20887
  paper_url: https://arxiv.org/abs/2511.20887
  project_url: n/a
  code_url: announced
  category: Teleoperation
  task_tags: [force-feedback, foldable, dexterous, IK]
  robot_platform: multiple
  uses_real_robot: yes
  uses_humanoid: partial
  uses_simulation: yes
  code_status: code release announced
  one_line: Foldable cross-embodiment exoskeleton adds force feedback to ACE-style teleop for higher-quality demos.
  why_it_matters: Adds the critical haptic channel missing from purely visual/exoskeleton teleop.

- title: Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning
  authors: Runyu Ding, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.03162
  paper_url: https://arxiv.org/abs/2407.03162
  project_url: https://dingry.github.io/projects/bunny_visionpro.html
  code_url: https://github.com/Dingry/BunnyVisionPro
  category: Teleoperation
  task_tags: [Apple-VisionPro, haptic, bimanual, dexterous, IK]
  robot_platform: bimanual dexterous robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Apple Vision Pro driven bimanual teleop with collision/singularity avoidance and low-cost haptic finger cots.
  why_it_matters: Demonstrates Vision Pro as a serious teleop interface; enables long-horizon bimanual imitation.

- title: GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators
  authors: Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, Pieter Abbeel
  year: 2023
  venue: IROS 2024
  arxiv_id: 2309.13037
  paper_url: https://arxiv.org/abs/2309.13037
  project_url: https://wuphilipp.github.io/gello_site/
  code_url: https://github.com/wuphilipp/gello_software
  category: Teleoperation
  task_tags: [puppeteer, joint-isomorphic, low-cost, IL]
  robot_platform: Franka, UR5, xArm
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: open-source (HW + SW)
  one_line: 3D-printed kinematic-twin puppeteer providing intuitive joint-level demos at very low cost.
  why_it_matters: Enabled wave of IL data collection; inspired arm controllers in BiDex, HOMIE, and others.

- title: BiDex: Bimanual Dexterity for Complex Tasks
  authors: Kenneth Shaw, Yulong Li, Jiahui Yang, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2411.13677
  paper_url: https://arxiv.org/abs/2411.13677
  project_url: https://bidex-teleop.github.io/
  code_url: https://github.com/dexsuite/bidex
  category: Teleoperation
  task_tags: [Manus-glove, bimanual, dexterous, in-the-wild]
  robot_platform: bimanual dexterous robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Manus motion-capture gloves + GELLO-style arm tracking for fast in-the-wild bimanual dexterous teleop.
  why_it_matters: Shows glove-based tracking outperforms VisionPro/SteamVR for high-DoF dexterous tasks.

- title: DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation
  authors: Chen Wang, et al.
  year: 2024
  venue: RSS 2024
  arxiv_id: 2403.07788
  paper_url: https://arxiv.org/abs/2403.07788
  project_url: https://dex-cap.github.io/
  code_url: https://github.com/j96w/DexCap
  category: Teleoperation
  task_tags: [mocap, SLAM, electromagnetic, in-the-wild, dexterous]
  robot_platform: dexterous robot hands
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Portable hand-mocap rig (SLAM + EMF tracking + RGB-D) for in-the-wild dexterous demo collection 3× faster than teleop.
  why_it_matters: Decouples data collection from the robot, enabling massive scaling of human-hand demos.

- title: Universal Manipulation Interface (UMI): In-The-Wild Robot Teaching Without In-The-Wild Robots
  authors: Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, et al.
  year: 2024
  venue: RSS 2024
  arxiv_id: 2402.10329
  paper_url: https://arxiv.org/abs/2402.10329
  project_url: https://umi-gripper.github.io/
  code_url: https://github.com/real-stanford/universal_manipulation_interface
  category: Teleoperation
  task_tags: [hand-held-gripper, GoPro, in-the-wild, hardware-agnostic]
  robot_platform: any parallel-jaw arm
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Hand-held parallel-jaw gripper + GoPro that records portable, hardware-agnostic demos for diffusion-policy training.
  why_it_matters: De-facto standard for robot-free demo collection; spawned UMI-on-Legs, DexUMI, etc.

- title: DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation
  authors: Mengda Xu, Han Zhang, et al.
  year: 2025
  venue: CoRL 2025 (Best Paper Final List)
  arxiv_id: 2505.21864
  paper_url: https://arxiv.org/abs/2505.21864
  project_url: https://dex-umi.github.io/
  code_url: https://github.com/real-stanford/DexUMI
  category: Teleoperation
  task_tags: [hand-exoskeleton, in-painting, dexterous, in-the-wild]
  robot_platform: 2 dexterous hands
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Wearable hand exoskeleton + visual in-painting that lets human hand directly serve as a dexterous interface; 86% real-world success.
  why_it_matters: Generalizes UMI to dexterous hands, 3.2× faster than teleop, with in-the-wild data.

- title: ARCap: Collecting High-quality Human Demonstrations for Robot Learning with Augmented Reality Feedback
  authors: Sirui Chen, et al.
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2410.08464
  paper_url: https://arxiv.org/abs/2410.08464
  project_url: https://stanford-tml.github.io/ARCap/
  code_url: https://github.com/Ericcsr/ARCap
  category: Teleoperation
  task_tags: [AR, robot-free, kinematic-overlay, dexterous]
  robot_platform: parallel-jaw, multi-finger hands
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: open-source
  one_line: AR headset overlays virtual robot kinematics on human hands during demo collection, enabling novices to gather robot-executable data.
  why_it_matters: AR feedback closes the embodiment gap during data collection without needing the robot.

- title: Open Teach: A Versatile Teleoperation System for Robotic Manipulation
  authors: Aadhithya Iyer, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2403.07870
  paper_url: https://arxiv.org/abs/2403.07870
  project_url: https://open-teach.github.io/
  code_url: https://github.com/aadhithya14/Open-Teach
  category: Teleoperation
  task_tags: [Meta-Quest3, VR, multi-robot, framework]
  robot_platform: Franka, xArm, Jaco, Allegro
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: open-source
  one_line: Open Meta Quest 3-based 90Hz teleop framework supporting hands+arms across 38 tasks and many robots.
  why_it_matters: Plug-and-play teleop foundation for academic labs; the most widely used open VR teleop stack on consumer headsets.

- title: AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild
  authors: Hongjie Fang, et al.
  year: 2024
  venue: ICRA 2024
  arxiv_id: 2309.14975
  paper_url: https://arxiv.org/abs/2309.14975
  project_url: https://airexo.github.io/
  code_url: https://github.com/AirExo/collector
  category: Teleoperation
  task_tags: [exoskeleton, in-the-wild, dual-arm, demonstration]
  robot_platform: dual-arm robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Low-cost passive dual-arm exoskeleton for in-the-wild demonstration collection without a robot.
  why_it_matters: Established cheap robot-free demo collection paradigm; extended by AirExo-2 in 2025.

- title: AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons
  authors: Hongjie Fang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2503.03081
  paper_url: https://arxiv.org/abs/2503.03081
  project_url: https://airexo.tech/airexo2/
  code_url: https://github.com/AirExo/airexo-2
  category: Teleoperation
  task_tags: [exoskeleton, scale, RISE-2, adapter]
  robot_platform: dual-arm robots
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Scaled AirExo with adapters that turn in-the-wild data into pseudo-robot demos for RISE-2 IL policy.
  why_it_matters: Demonstrates exoskeleton-only data can rival teleop demos for general IL.

- title: NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid Robots
  authors: et al.
  year: 2025
  venue: ICRA 2026
  arxiv_id: 2503.10554
  paper_url: https://arxiv.org/abs/2503.10554
  project_url: n/a
  code_url: not released
  category: Teleoperation
  task_tags: [exoskeleton, outdoor, full-ROM, humanoid]
  robot_platform: humanoid (full-size)
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: hardware design released; SW not yet
  one_line: Backpack 5.2 kg active-joint exoskeleton with sternoclavicular compensation for 100% upper-limb ROM teleop in outdoor settings.
  why_it_matters: First wearable system to cover full upper-limb ROM for humanoid teleop in the wild.

- title: DEXOP: A Device for Robotic Transfer of Dexterous Human Manipulation
  authors: Hao-Shu Fang, Branden Romero, et al. (MIT Improbable AI)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2509.04441
  paper_url: https://arxiv.org/abs/2509.04441
  project_url: https://dex-op.github.io/
  code_url: https://github.com/HaoshuFang/DEXOP
  category: Teleoperation
  task_tags: [perioperation, hand-exoskeleton, force-feedback, vision+tactile]
  robot_platform: dexterous hands
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Passive hand exoskeleton coined "perioperation" — connects human fingers to robot fingers for high-quality vision+tactile demos.
  why_it_matters: New paradigm between teleop and pure mocap; force feedback + pose mirroring boosts data quality and policy success.

- title: EgoMimic: Scaling Imitation Learning via Egocentric Video
  authors: Simar Kareer, Dhruv Patel, et al.
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2410.24221
  paper_url: https://arxiv.org/abs/2410.24221
  project_url: https://egomimic.github.io/
  code_url: https://github.com/SimarKareer/EgoMimic
  category: Teleoperation
  task_tags: [Project-Aria, egocentric-video, bimanual, co-training]
  robot_platform: bimanual (humanoid-adjacent)
  uses_real_robot: yes
  uses_humanoid: partial
  uses_simulation: no
  code_status: open-source
  one_line: Project Aria glasses + low-cost bimanual robot with kinematic gap minimized; co-trains on human and robot data.
  why_it_matters: Shows egocentric video + 3D hand tracking can boost IL by 34–228% over robot-only data.

- title: EgoZero: Robot Learning from Smart Glasses
  authors: Vincent Liu, Ademi Adeniji, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2505.20290
  paper_url: https://arxiv.org/abs/2505.20290
  project_url: https://egozero-robot.github.io/
  code_url: https://github.com/vliu15/egozero
  category: Teleoperation
  task_tags: [Project-Aria, zero-robot-data, 3D-points, point-policy]
  robot_platform: Franka Panda
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Train manipulation policies from Aria glasses alone with zero robot data; 70% zero-shot success on 7 tasks.
  why_it_matters: Pure smart-glasses-to-robot pipeline; defines morphology-agnostic state-action space via 3D points.

- title: DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning
  authors: Zhenyu Jiang, et al.
  year: 2024
  venue: ICRA 2025
  arxiv_id: 2410.24185
  paper_url: https://arxiv.org/abs/2410.24185
  project_url: https://dexmimicgen.github.io/
  code_url: https://github.com/NVlabs/dexmimicgen
  category: Teleoperation
  task_tags: [data-generation, bimanual, real-to-sim-to-real, MimicGen]
  robot_platform: humanoid + dexterous hands
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source (sim envs)
  one_line: Synthesizes 21K bimanual dexterous trajectories from 60 human demos via subtask-aware replay.
  why_it_matters: Scales humanoid teleop demos by 350× through automated data generation.

- title: Humanoid Policy ~ Human Policy (PH2D / HAT)
  authors: Ri-Zhao Qiu, Shiqi Yang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2503.13441
  paper_url: https://arxiv.org/abs/2503.13441
  project_url: https://human-as-robot.github.io/
  code_url: https://github.com/RchalYang/Human2HumanoidPolicy
  category: Teleoperation
  task_tags: [cross-embodiment, dataset, transformer, VR-mocap]
  robot_platform: Unitree H1 + dexterous hands
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: open-source
  one_line: PH2D dataset of human VR-mocap aligned with humanoid demos; HAT policy treats humans as another humanoid embodiment.
  why_it_matters: First scalable joint human-humanoid policy training, achieving large generalization gains.

- title: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies (iDP3 + Humanoid Teleop)
  authors: Yanjie Ze, et al.
  year: 2024
  venue: IROS 2025
  arxiv_id: 2410.10803
  paper_url: https://arxiv.org/abs/2410.10803
  project_url: https://humanoid-manipulation.github.io/
  code_url: https://github.com/YanjieZe/Humanoid-Teleoperation
  category: Teleoperation
  task_tags: [whole-upper-body, active-vision, VR, 3D-policy]
  robot_platform: Fourier GR1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open-source (teleop + iDP3)
  one_line: Whole-upper-body humanoid teleop pipeline (waist + active vision) paired with iDP3 for in-the-wild deployment.
  why_it_matters: Open teleop+policy stack actively maintained for the GR1 humanoid; widely used reference.

- title: H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation
  authors: Hongzhe Bi, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2507.23523
  paper_url: https://arxiv.org/abs/2507.23523
  project_url: https://embodiedfoundation.github.io/hrdt
  code_url: https://github.com/HongzheBi/H_RDT
  category: Teleoperation
  task_tags: [diffusion-transformer, EgoDex, pretraining, bimanual]
  robot_platform: bimanual / humanoid
  uses_real_robot: yes
  uses_humanoid: partial
  uses_simulation: yes
  code_status: open-source
  one_line: 2B diffusion transformer pretrained on 338K EgoDex human trajectories then fine-tuned on robot demos.
  why_it_matters: Shows large-scale egocentric human-hand video pretraining substantially improves bimanual policies.

- title: MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2509.17759
  paper_url: https://arxiv.org/abs/2509.17759
  project_url: n/a
  code_url: announced
  category: Teleoperation
  task_tags: [VR, OpenTeleVision, co-training, dexterous, dataset]
  robot_platform: Franka + Inspire Hand
  uses_real_robot: yes
  uses_humanoid: partial
  uses_simulation: no
  code_status: pending
  one_line: Builds on Open-TeleVision to capture wrist+hand poses and co-trains human-robot policies for motion-level transfer.
  why_it_matters: Open-TeleVision-based dataset enabling motion-level policy learning from human VR demos.

- title: EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2511.00153
  paper_url: https://arxiv.org/abs/2511.00153
  project_url: n/a
  code_url: announced
  category: Teleoperation
  task_tags: [egocentric, active-vision, whole-body, retargeting]
  robot_platform: humanoid-adjacent
  uses_real_robot: yes
  uses_humanoid: partial
  uses_simulation: no
  code_status: pending
  one_line: Captures synchronized head and hand trajectories during human demos and retargets to semi-humanoid embodiments.
  why_it_matters: First system enabling true whole-body retargeting (head + hands + gripper) from egocentric demos.

- title: Robotic Telekinesis: Learning a Robotic Hand Imitator by Watching Humans on Youtube
  authors: Aravind Sivakumar, Kenneth Shaw, Deepak Pathak
  year: 2022
  venue: RSS 2022
  arxiv_id: 2202.10448
  paper_url: https://arxiv.org/abs/2202.10448
  project_url: https://robotic-telekinesis.github.io/
  code_url: https://github.com/sraviakv/robotic-telekinesis
  category: Teleoperation
  task_tags: [single-RGB, hand-imitator, glove-free, internet-video]
  robot_platform: Allegro Hand on Franka
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: no
  code_status: open-source
  one_line: Single-RGB-camera teleop trained on internet hand videos; first low-cost glove-free dexterous teleop.
  why_it_matters: Established cheap RGB teleop; precursor to AnyTeleop and EgoMimic style work.

- title: AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch
  authors: Max Yang, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2405.07391
  paper_url: https://arxiv.org/abs/2405.07391
  project_url: https://maxyang27896.github.io/anyrotate/
  code_url: https://github.com/maxyang27896/anyrotate
  category: Teleoperation
  task_tags: [tactile, in-hand, sim-to-real, dexterous]
  robot_platform: dexterous hand
  uses_real_robot: yes
  uses_humanoid: no
  uses_simulation: yes
  code_status: open-source
  one_line: Unified policy rotates objects about any axis in any hand orientation using dense tactile feedback transferred from sim.
  why_it_matters: Dexterous in-hand control benchmark relevant to humanoid hand teleop downstream.

- title: BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark
  authors: Nikita Chernyadev, Nicholas Backshall, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.07788
  paper_url: https://arxiv.org/abs/2407.07788
  project_url: https://chernyadev.github.io/bigym/
  code_url: https://github.com/chernyadev/bigym
  category: Teleoperation
  task_tags: [benchmark, VR-teleop, demos, Unitree-H1]
  robot_platform: Unitree H1 (sim)
  uses_real_robot: no
  uses_humanoid: yes (sim)
  uses_simulation: yes
  code_status: open-source
  one_line: 40-task humanoid bimanual benchmark with VR-teleop human demonstrations and sparse rewards.
  why_it_matters: Standard humanoid IL benchmark with realistic VR-teleop trajectories.

- title: CHILD: Controller for Humanoid Imitation and Live Demonstration
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2508.00162
  paper_url: https://arxiv.org/abs/2508.00162
  project_url: n/a
  code_url: announced
  category: Teleoperation
  task_tags: [joint-level, baby-carrier, four-limb, low-cost]
  robot_platform: humanoid
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: no
  code_status: pending
  one_line: Compact baby-carrier-form teleop rig giving operator joint-level control of all four humanoid limbs.
  why_it_matters: Form-factor innovation for humanoid teleop; shows joint-level alternatives to MoCap suits.

- title: Visual Imitation Enables Contextual Humanoid Control (VIDE)
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2505.03729
  paper_url: https://arxiv.org/abs/2505.03729
  project_url: n/a
  code_url: announced
  category: Teleoperation
  task_tags: [video-imitation, contextual-control, humanoid]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: pending
  one_line: Learns context-conditioned humanoid skills from monocular human videos via retargeting + imitation.
  why_it_matters: Connects internet-scale human video to deployable humanoid skills.

- title: Learning Adaptive Neural Teleoperation for Humanoid Robots: From IK to End-to-End Control
  authors: et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2511.12390
  paper_url: https://arxiv.org/abs/2511.12390
  project_url: n/a
  code_url: not released
  category: Teleoperation
  task_tags: [neural-IK, RL, VR-controller, force-adapt]
  robot_platform: Unitree G1
  uses_real_robot: yes
  uses_humanoid: yes
  uses_simulation: yes
  code_status: not yet released
  one_line: Replaces IK+PD teleop with RL-trained policy mapping VR controller inputs directly to joints; 34% lower tracking error.
  why_it_matters: Suggests learned teleop controllers can outperform classical IK pipelines for VR humanoid teleop.

- title: Proprioceptive-visual correspondence enables self-other distinction in humanoid robots
  authors: Yurun Chen; Tianyuan Gao; Yizhong Ge; Shikun Ban; Yizhou Wang; Hongkai Xiong; Wenjun Zeng; Wentao Zhu
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.13222
  paper_url: https://arxiv.org/abs/2606.13222
  project_url: https://euron-zc.github.io/humanoid-self-model/
  code_url: ""
  category: Retargeting
  task_tags: [self-model, proprioception, vision, motion-retargeting]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Learns self-other distinction and a predictive 3D body occupancy model from proprioceptive-visual correspondence.
  why_it_matters: Provides a self-model useful for collision-aware planning and human-to-robot retargeting in shared workspaces.

- title: Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization
  authors: Yitian Shi; Di Wen; Zhengqi Han; Zicheng Guo; Yu Hu; Edgar Welte; Kunyu Peng; Rainer Stiefelhagen; Rania Rayyes
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.10743
  paper_url: https://arxiv.org/abs/2606.10743
  project_url: ""
  code_url: ""
  category: Retargeting
  task_tags: [video-demonstrations, contact-localization, trajectory-transfer, open-world]
  robot_platform: robot arms / manipulation
  uses_real_robot: true
  uses_humanoid: false
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: HOWTransfer converts noisy human videos into contact-aware, taxonomy-informed robot trajectories for unseen objects.
  why_it_matters: Contact localization is a reusable ingredient for humanoid hand-object retargeting.

- title: X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting
  authors: Jen-Wei Wang; Sarthak Kaingade; Andrea Tagliabue; Nicholas Morozovsky
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.07934
  paper_url: https://arxiv.org/abs/2606.07934
  project_url: ""
  code_url: ""
  category: Teleoperation
  task_tags: [whole-body-teleoperation, MPC-retargeting, cross-morphology, XR]
  robot_platform: humanoid / cross-morphology robots
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: MPC-based retargeting enables cross-morphology whole-body teleoperation without robot-specific end-to-end retraining.
  why_it_matters: Offers a more reusable teleop interface than suit-specific or robot-specific learned policies.

- title: RealDexUMI: A Wearable Universal Manipulation Interface for Dexterous Robot Learning
  authors: Chaoyi Xu; Yixuan Jiang; Jiahui Huan; Yuhui Fu; Haoyu Zhou; Weitian Yuan; Jiayi Yu; Wanpeng Zhang; Haoqi Yuan; Zongqing Lu
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.06033
  paper_url: https://arxiv.org/abs/2606.06033
  project_url: https://research.beingbeyond.com/realdexumi
  code_url: ""
  category: Teleoperation
  task_tags: [wearable-interface, dexterous, UMI, contact-aware]
  robot_platform: dexterous hands / humanoid-relevant manipulation
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Wearable universal manipulation interface preserves fine hand-object interactions while producing deployable dexterous robot data.
  why_it_matters: Extends UMI-style collection toward dexterous and humanoid hand embodiments.

- title: Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots
  authors: Tianchen Huang; Feiyang Yuan; Junchi Gu; Shurui Fang; Xiaohu Zhang; Yu Wang; Wei Gao; Shiwu Zhang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.03476
  paper_url: https://arxiv.org/abs/2606.03476
  project_url: https://huangtc233.github.io/human2humanoid_website/
  code_url: ""
  category: Retargeting
  task_tags: [cross-morphology, physics-aware, unsupervised, Unitree-G1]
  robot_platform: Unitree G1 / humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Unsupervised physics-aware retargeting transfers human motions to humanoid behaviors despite topology, proportion, and DoF mismatch.
  why_it_matters: Targets retargeting artifacts before they poison downstream imitation learning.

- title: ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting
  authors: David Muller; Agon Serifi; Sammy Christen; Ruben Grandia; Espen Knoop; Moritz Bacher
  year: 2026
  venue: SIGGRAPH 2026
  arxiv_id: 2605.06593
  paper_url: https://arxiv.org/abs/2605.06593
  project_url: ""
  code_url: ""
  category: Retargeting
  task_tags: [physics-aware, bilevel-optimization, imitation-learning, retargeting]
  robot_platform: humanoid / quadruped morphologies
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Bilevel RL retargeting jointly adapts reference motion and trains a policy to produce physically feasible motions across morphologies.
  why_it_matters: Shows retargeting can be optimized directly for downstream imitation feasibility rather than kinematic similarity alone.

- title: Universal Manipulation Exoskeleton: Learning Compliant Whole-Body Policies with Real-time Torque Feedback
  authors: Litian Liang; Jingxi Xu; Xinda Qi; Yujun Cai; Houzhu Ding; Luqi Wang; Zhixin Sun; Jyh-Herng Chow; Ming Yang; Mark Cutkosky
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.14218
  paper_url: https://arxiv.org/abs/2606.14218
  project_url: https://ume-exo.github.io/
  code_url: ""
  category: Teleoperation
  task_tags: [exoskeleton, torque-feedback, compliant-policy, whole-body-manipulation]
  robot_platform: humanoid-relevant mobile manipulation
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Portable upper-limb exoskeleton records arm configurations and joint torque feedback for learning contact-compliant whole-body manipulation policies.
  why_it_matters: Adds force/torque-rich demonstration data to teleop pipelines that usually preserve only motion trajectories.

- title: TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation
  authors: Jielin Wu; Shenzhe Yao; Guanqi He; Xiaohan Liu; Zhaoqing Zeng; Xiangrui Jiang; Han Yang; Wentao Zhang; Hang Zhao
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.16272
  paper_url: https://arxiv.org/abs/2606.16272
  project_url: https://toporetarget2026.github.io/TopoRetarget/
  code_url: ""
  category: Retargeting
  task_tags: [dexterous-retargeting, hand-object-contact, interaction-graph, sim-to-real]
  robot_platform: dexterous hands / humanoid hands
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Retargets dexterous manipulation by preserving local hand-object interaction graphs instead of copying hand pose alone.
  why_it_matters: Reduces contact-mode artifacts that make human hand demonstrations brittle for humanoid or dexterous-hand RL.

- title: EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning
  authors: Gaotian Wang; Kejia Ren; Andrew Morgan; Yiting Chen; Howard H. Qian; Podshara Chanrungmaneekul; Kaiyu Hang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.17385
  paper_url: https://arxiv.org/abs/2606.17385
  project_url: https://huggingface.co/spaces/Rice-RobotPI-Lab/EgoInfinity
  code_url: ""
  category: Retargeting
  task_tags: [hand-object-interaction, video-to-action, retargeting, web-scale-data]
  robot_platform: robot hands / humanoid-relevant manipulation
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Converts arbitrary RGB hand-object videos into 4D interaction data for robot retargeting through reconstruction, refinement, and action extraction.
  why_it_matters: Targets the data bottleneck between web-scale human manipulation videos and deployable robot or humanoid hand policies.

---

## Notes
- Verification: code links above were checked through paper pages or GitHub URLs surfaced via search; for systems labeled "announced" / "pending" the project pages indicate code release in progress.
- Coverage spans (a) classical/learning retargeting (PHC, Mink, GMR, OmniRetarget, IKMR, DexMachina), (b) VR teleop (Open-TeleVision, OmniH2O, OpenWBT, CLONE, HOMIE, Bunny-VisionPro), (c) wearable/exoskeleton teleop (HOMIE, AirExo, NuExo, GELLO, BiDex, DEXOP, ACE, ACE-F, DexUMI), (d) robot-free / in-the-wild capture (UMI, DexCap, ARCap, EgoMimic, EgoZero, EgoMI, AirExo, HumanoidExo), and (e) data-generation / scaling (DexMimicGen, H-RDT, MotionTrans, PH2D).
