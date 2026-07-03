# Chunk 07: Datasets & Benchmarks, Evaluation Metrics & Contact Modeling, Sim-to-Real & Deployment

Coverage: 2022-2026 (priority on 2024-2026). Combines (1) datasets & benchmarks for HOI / humanoid WBC / motion tracking, (2) evaluation metrics & contact modeling, (3) sim-to-real & deployment systems.

---

## A. Human Motion / Mocap Datasets (used as kinematic priors for humanoid WBC)

- title: AMASS - Archive of Motion Capture as Surface Shapes
  authors: Naureen Mahmood, Nima Ghorbani, Nikolaus F. Troje, Gerard Pons-Moll, Michael J. Black
  year: 2019
  venue: ICCV 2019
  arxiv_id: 1904.03278
  paper_url: https://arxiv.org/abs/1904.03278
  project_url: https://amass.is.tue.mpg.de/
  code_url: https://github.com/nghorbani/amass
  dataset_url: https://amass.is.tue.mpg.de/
  category: Dataset
  task_tags: [mocap, SMPL-H, motion-priors, retargeting]
  robot_platform: N/A (human SMPL)
  uses_real_robot: no
  uses_humanoid: no
  uses_simulation: no
  code_status: open
  one_line: Unifies 15 mocap datasets (>40 hrs, 300+ subjects, 11k motions) into SMPL-H with MoSh++.
  why_it_matters: De facto motion-prior corpus for nearly every humanoid WBC / motion tracking pipeline (H2O, OmniH2O, ExBody2, ASAP, BeyondMimic).

- title: HumanML3D - 3D Human Motion-Language Dataset
  authors: Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, et al.
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2207.01696
  paper_url: https://arxiv.org/abs/2207.01696
  project_url: https://github.com/EricGuo5513/HumanML3D
  code_url: https://github.com/EricGuo5513/HumanML3D
  dataset_url: https://github.com/EricGuo5513/HumanML3D
  category: Dataset
  task_tags: [text-to-motion, motion-language]
  uses_real_robot: no
  uses_humanoid: no
  uses_simulation: no
  code_status: open
  one_line: 14,616 motions, 44,970 textual descriptions paired (resampled from AMASS+HumanAct12).
  why_it_matters: Standard text-conditioned motion-generation benchmark; commonly distilled into humanoid WBC priors.

- title: Motion-X - Large-scale 3D Expressive Whole-body Human Motion Dataset
  authors: Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, et al.
  year: 2023
  venue: NeurIPS 2023
  arxiv_id: 2307.00818
  paper_url: https://arxiv.org/abs/2307.00818
  project_url: https://motion-x-dataset.github.io/
  code_url: https://github.com/IDEA-Research/Motion-X
  dataset_url: https://github.com/IDEA-Research/Motion-X
  category: Dataset
  task_tags: [whole-body, SMPL-X, text-motion, expressive]
  uses_humanoid: no
  uses_simulation: no
  code_status: open
  one_line: 15.6M whole-body 3D poses + 81K sequences with text + facial/hand annotations.
  why_it_matters: First large-scale SMPL-X dataset; foundation for whole-body motion generation, used by humanoid retargeting work.

- title: Motion-X++ - Large-Scale Multimodal 3D Whole-body Human Motion Dataset
  authors: Yuhong Zhang, Jing Lin, Ailing Zeng, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2501.05098
  paper_url: https://arxiv.org/abs/2501.05098
  project_url: https://motion-x-dataset.github.io/
  code_url: https://github.com/IDEA-Research/Motion-X
  category: Dataset
  task_tags: [multimodal, audio, RGB, whole-body]
  code_status: open
  one_line: 19.5M whole-body pose annotations across 120.5K sequences + audio + per-frame text.
  why_it_matters: Multimodal extension of Motion-X; useful for audio/text-conditioned humanoid WBC training.

- title: KIT Motion-Language Dataset
  authors: Matthias Plappert, Christian Mandery, Tamim Asfour
  year: 2016
  venue: Big Data Journal
  arxiv_id: 1607.03827
  paper_url: https://arxiv.org/abs/1607.03827
  dataset_url: https://motion-annotation.humanoids.kit.edu/dataset/
  category: Dataset
  task_tags: [text-to-motion, motion-language]
  code_status: open
  one_line: 3,911 motion sequences with 6,278 text descriptions on 21-joint skeleton.
  why_it_matters: Earlier motion-language benchmark widely used as evaluation set for text-to-motion models.

- title: CMU Motion Capture Database
  authors: Carnegie Mellon University Graphics Lab
  year: 2003
  venue: CMU online dataset
  paper_url: https://mocap.cs.cmu.edu/
  dataset_url: https://mocap.cs.cmu.edu/
  category: Dataset
  task_tags: [mocap, BVH, locomotion]
  code_status: open
  one_line: Free CMU mocap database covering walking, running, jumping, acrobatics.
  why_it_matters: Original substrate for many later datasets (incl. AMASS); still cited as raw mocap source.

- title: LAFAN1 - Ubisoft La Forge Animation Dataset
  authors: F. G. Harvey, M. Yurick, D. Nowrouzezahrai, C. Pal
  year: 2020
  venue: SIGGRAPH 2020
  paper_url: https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1txNTAqAGya2sjQVWQUsKE/d317e852512cbc9fec6dafc8b61f4a4e/RobustMotionInbetweening.pdf
  code_url: https://github.com/ubisoft/ubisoft-laforge-animation-dataset
  dataset_url: https://github.com/ubisoft/ubisoft-laforge-animation-dataset
  category: Dataset
  task_tags: [mocap, animation, in-betweening, BVH]
  code_status: open
  one_line: 5 subjects, 77 sequences, ~496K frames @ 30 fps in BVH format.
  why_it_matters: Clean studio-grade mocap; staple for motion in-betweening and humanoid retargeting baselines.

- title: GTA-Human - Playing for 3D Human Recovery
  authors: Zhongang Cai, Mingyuan Zhang, Jiawei Ren, et al.
  year: 2021
  venue: TPAMI
  arxiv_id: 2110.07588
  paper_url: https://arxiv.org/abs/2110.07588
  project_url: https://caizhongang.github.io/projects/GTA-Human/
  dataset_url: https://huggingface.co/datasets/caizhongang/GTA-Human
  category: Dataset
  task_tags: [synthetic, GTA-V, SMPL, mesh-recovery]
  code_status: open
  one_line: Large-scale synthetic 3D human dataset rendered in GTA-V game engine.
  why_it_matters: Demonstrates synthetic mocap can train robust 3D mesh recovery, relevant for vision-based teleop.

- title: MOYO - Yoga Poses with Pressure Mat
  authors: Sai Kumar Dwivedi, Cordelia Schmid, Hongwei Yi, Michael J. Black, Dimitrios Tzionas
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2303.18246
  paper_url: https://arxiv.org/abs/2303.18246
  project_url: https://ipman.is.tue.mpg.de/
  dataset_url: https://moyo.is.tue.mpg.de/
  category: Dataset
  task_tags: [yoga, contact, pressure, CoP, CoM]
  code_status: open
  one_line: Multi-view yoga mocap with floor pressure, ground-truth CoM and CoP.
  why_it_matters: Provides physical-plausibility ground-truth (contact + CoP) used for evaluating humanoid balance.

---

## B. Human-Object Interaction (HOI) Datasets

- title: BEHAVE - Tracking Human-Object Interactions
  authors: Bharat Lal Bhatnagar, Xianghui Xie, Ilya Petrov, Cristian Sminchisescu, Christian Theobalt, Gerard Pons-Moll
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2204.06950
  paper_url: https://arxiv.org/abs/2204.06950
  project_url: https://virtualhumans.mpi-inf.mpg.de/behave/
  dataset_url: https://virtualhumans.mpi-inf.mpg.de/behave/
  category: Dataset
  task_tags: [HOI, RGBD, multi-view, contact]
  code_status: open
  one_line: First full-body HOI dataset with RGBD multi-view + 3D SMPL + object fits + contact.
  why_it_matters: Canonical HOI benchmark for humanoid loco-manipulation pretraining.

- title: GRAB - Whole-Body Human Grasping of Objects
  authors: Omid Taheri, Nima Ghorbani, Michael J. Black, Dimitrios Tzionas
  year: 2020
  venue: ECCV 2020
  arxiv_id: 2008.11200
  paper_url: https://arxiv.org/abs/2008.11200
  project_url: https://grab.is.tue.mpg.de/
  dataset_url: https://grab.is.tue.mpg.de/
  category: Dataset
  task_tags: [grasping, SMPL-X, hand-object]
  code_status: open
  one_line: Whole-body MoCap of dexterous grasping with SMPL-X bodies and 51 objects.
  why_it_matters: Reference grasping dataset for hand-object contact modeling and dex grasp synthesis.

- title: ARCTIC - Dexterous Bimanual Hand-Object Manipulation
  authors: Zicong Fan, Omid Taheri, Dimitrios Tzionas, et al.
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2204.13662
  paper_url: https://arxiv.org/abs/2204.13662
  project_url: https://arctic.is.tue.mpg.de/
  dataset_url: https://arctic.is.tue.mpg.de/
  code_url: https://github.com/zc-alexfan/arctic
  category: Dataset
  task_tags: [bimanual, articulated-objects, contact]
  code_status: open
  one_line: 2.1M video frames of bimanual articulated-object manipulation with 3D meshes and contact.
  why_it_matters: Strong bimanual benchmark with dynamic contact ground truth; rare for humanoid bimanual policies.

- title: OakInk2 - Bimanual Hand-Object Manipulation in Complex Tasks
  authors: Xinyu Zhan, Lixin Yang, Yifei Zhao, et al.
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2403.19417
  paper_url: https://arxiv.org/abs/2403.19417
  project_url: https://oakink.net/v2/
  dataset_url: https://oakink.net/v2/
  category: Dataset
  task_tags: [bimanual, daily-tasks, primitive-tasks, complex-tasks]
  code_status: open
  one_line: Bimanual hand-object manipulation organized as Affordance/Primitive/Complex hierarchy.
  why_it_matters: Hierarchical task decomposition useful for long-horizon humanoid manipulation.

- title: HIMO - Full-Body Human Interacting with Multiple Objects
  authors: Xintao Lv, Liang Xu, Yichao Yan, et al.
  year: 2024
  venue: ECCV 2024
  arxiv_id: 2407.12371
  paper_url: https://arxiv.org/abs/2407.12371
  project_url: https://lvxintao.github.io/himo/
  dataset_url: https://lvxintao.github.io/himo/
  category: Dataset
  task_tags: [HOI, multi-object, text-driven]
  code_status: open
  one_line: 3.3K HOI sequences, 4.08M frames, 53 objects, 34 subjects with detailed text.
  why_it_matters: First large-scale multi-object HOI dataset, useful for sequential humanoid loco-manipulation.

- title: OMOMO - Object Motion Guided Human Motion Synthesis
  authors: Jiaman Li, Jiajun Wu, C. Karen Liu
  year: 2023
  venue: SIGGRAPH Asia 2023
  arxiv_id: 2309.16237
  paper_url: https://arxiv.org/abs/2309.16237
  project_url: https://lijiaman.github.io/projects/omomo/
  code_url: https://github.com/lijiaman/omomo_release
  dataset_url: https://github.com/lijiaman/omomo_release
  category: Dataset
  task_tags: [HOI, large-objects, motion-synthesis]
  code_status: open
  one_line: ~10 hours of paired human-object MoCap with 15 large everyday objects.
  why_it_matters: Object-conditioned full-body motion generation; basis for follow-ups (CHOIS).

- title: InterAct - Large-Scale Versatile 3D HOI Generation
  authors: Wenyu Zhang, et al.
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2509.09555
  paper_url: https://arxiv.org/abs/2509.09555
  code_url: https://github.com/wzyabcas/InterAct
  category: Dataset
  task_tags: [HOI, generation, large-scale]
  code_status: open
  one_line: Unified large-scale HOI dataset and benchmark advancing versatile interaction generation.
  why_it_matters: Aggregates HOI sources into a large benchmark for HOI generative modeling.

- title: TRUMANS - Scaling Up Dynamic Human-Scene Interaction Modeling
  authors: Nan Jiang, Zhiyuan Zhang, Hongjie Li, et al.
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2403.08629
  paper_url: https://arxiv.org/abs/2403.08629
  project_url: https://jnnan.github.io/trumans/
  dataset_url: https://jnnan.github.io/trumans/
  category: Dataset
  task_tags: [HSI, scenes, contact-aware]
  code_status: open
  one_line: 15+ hours of mocap human-scene interaction across 100 indoor scenes with part-level dynamics.
  why_it_matters: Largest real mocap HSI dataset; key for scene-aware humanoid navigation/manipulation.

- title: CIRCLE - Capture In Rich Contextual Environments
  authors: Joao Pedro Araujo, Jiaman Li, et al.
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2303.17912
  paper_url: https://arxiv.org/abs/2303.17912
  project_url: https://stanford-tml.github.io/circle_dataset/
  dataset_url: https://stanford-tml.github.io/circle_dataset/
  category: Dataset
  task_tags: [HSI, reaching, scenes]
  code_status: open
  one_line: 10 hours of full-body reaching motion with rich VR scene geometry context.
  why_it_matters: High-quality reaching/scene dataset; used to train scene-aware reaching policies.

- title: COUCH - Towards Controllable Human-Chair Interactions
  authors: Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Vladimir Guzov, Gerard Pons-Moll
  year: 2022
  venue: ECCV 2022
  arxiv_id: 2205.00541
  paper_url: https://arxiv.org/abs/2205.00541
  project_url: https://virtualhumans.mpi-inf.mpg.de/couch/
  dataset_url: https://virtualhumans.mpi-inf.mpg.de/couch/
  category: Dataset
  task_tags: [HSI, sitting, chair]
  code_status: open
  one_line: Controllable human-chair sitting interactions with hand-contact priors.
  why_it_matters: Targeted dataset for sitting/chair interaction synthesis.

- title: SAMP - Stochastic Scene-Aware Motion Prediction
  authors: Mohamed Hassan, Duygu Ceylan, Ruben Villegas, Jun Saito, Jimei Yang, Yi Zhou, Michael J. Black
  year: 2021
  venue: ICCV 2021
  arxiv_id: 2108.08284
  paper_url: https://arxiv.org/abs/2108.08284
  project_url: https://samp.is.tue.mpg.de/
  dataset_url: https://samp.is.tue.mpg.de/
  category: Dataset
  task_tags: [HSI, sitting, lying, locomotion]
  code_status: open
  one_line: 100 minutes of mocap covering walking, sitting, lying with scene context.
  why_it_matters: Pioneering scene-aware motion dataset; basis for COUCH and follow-ups.

- title: HOI-M3 - Multi-Human Multi-Object Interaction in Context
  authors: Juze Zhang, Jingyan Zhang, Zining Song, et al.
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2404.00299
  paper_url: https://arxiv.org/abs/2404.00299
  project_url: https://juzezhang.github.io/HOIM3_ProjectPage/
  dataset_url: https://juzezhang.github.io/HOIM3_ProjectPage/
  category: Dataset
  task_tags: [multi-human, HOI, multi-object]
  code_status: open
  one_line: 199 sequences, 181M frames of multiple humans + multiple objects via dense RGB and IMU.
  why_it_matters: Rare multi-human multi-object HOI; relevant for collaborative humanoid scenarios.

- title: ParaHome - Parameterizing Everyday Home Activities
  authors: Jeonghwan Kim, Jisoo Kim, Jeonghyeon Na, Hanbyul Joo
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2401.10232
  paper_url: https://arxiv.org/abs/2401.10232
  project_url: https://jlogkim.github.io/parahome/
  code_url: https://github.com/snuvclab/ParaHome
  category: Dataset
  task_tags: [HOI, home, articulated, hand-finger]
  code_status: open
  one_line: 38 subjects, 22 objects, 486 minutes of body+hand+object dynamics in studio apartment.
  why_it_matters: Home-scale articulated HOI capture; rich training source for household humanoid skills.

- title: Ego4D - Around the World in 3,000 Hours of Egocentric Video
  authors: Kristen Grauman, Andrew Westbury, et al. (FAIR consortium)
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2110.07058
  paper_url: https://arxiv.org/abs/2110.07058
  project_url: https://ego4d-data.org/
  code_url: https://github.com/facebookresearch/Ego4d
  dataset_url: https://ego4d-data.org/
  category: Dataset
  task_tags: [egocentric, video, daily-activities]
  code_status: open
  one_line: 3,670 hours of egocentric video from 923 wearers worldwide.
  why_it_matters: Massive egocentric corpus underlying VLA pretraining and ego-conditioned humanoid controllers.

- title: Ego-Exo4D - First and Third-Person Skilled Activity
  authors: Kristen Grauman, Andrew Westbury, Lorenzo Torresani, et al.
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2311.18259
  paper_url: https://arxiv.org/abs/2311.18259
  project_url: https://ego-exo4d-data.org/
  dataset_url: https://ego-exo4d-data.org/
  category: Dataset
  task_tags: [egocentric, exocentric, multimodal, skilled-activity]
  code_status: open
  one_line: 1,286 hours of synchronized ego+exo video with audio, gaze, IMU, point clouds.
  why_it_matters: Cross-view skilled activity benchmark; supports humanoid imitation from ego view.

---

## C. Robot Manipulation / Whole-Body Benchmarks

- title: HumanoidBench - Simulated Whole-Body Locomotion and Manipulation
  authors: Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, Pieter Abbeel
  year: 2024
  venue: RSS 2024
  arxiv_id: 2403.10506
  paper_url: https://arxiv.org/abs/2403.10506
  project_url: https://humanoid-bench.github.io/
  code_url: https://github.com/carlosferrazza/humanoid-bench
  category: Benchmark
  task_tags: [WBC, manipulation, locomotion]
  robot_platform: Unitree H1 + Shadow Hands
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open
  one_line: 31 whole-body humanoid tasks (14 loco + 17 manipulation) in MuJoCo MJX.
  why_it_matters: First widely adopted humanoid WBC benchmark; reveals hierarchical RL outperforms flat RL.

- title: BiGym - Demo-Driven Mobile Bi-Manual Humanoid Benchmark
  authors: Nikita Chernyadev, Nicholas Backshall, Xiao Ma, Yunfan Lu, Younggyo Seo, Stephen James
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2407.07788
  paper_url: https://arxiv.org/abs/2407.07788
  project_url: https://chernyadev.github.io/bigym/
  code_url: https://github.com/chernyadev/bigym
  category: Benchmark
  task_tags: [bimanual, mobile-manip, IL, sparse-reward]
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open
  one_line: 40 visual mobile bimanual humanoid tasks with 50 demos each (sparse rewards).
  why_it_matters: Demo-driven IL/RL benchmark for mobile humanoid manipulation.

- title: LocoMuJoCo - Imitation Learning Benchmark for Locomotion
  authors: Firas Al-Hafez, Guoping Zhao, Jan Peters, Davide Tateo
  year: 2023
  venue: NeurIPS 2023 Workshop
  arxiv_id: 2311.02496
  paper_url: https://arxiv.org/abs/2311.02496
  code_url: https://github.com/robfiras/loco-mujoco
  category: Benchmark
  task_tags: [imitation, locomotion, humanoid, quadruped]
  uses_simulation: yes
  code_status: open
  one_line: 12 environments / 27 tasks for IL across humanoids and quadrupeds.
  why_it_matters: Standardized IL evaluation across legged morphologies.

- title: Humanoid-Gym - RL Framework for Zero-Shot Sim2Real
  authors: Xinyang Gu, Yen-Jen Wang, Jianyu Chen
  year: 2024
  venue: arXiv / IROS-W
  arxiv_id: 2404.05695
  paper_url: https://arxiv.org/abs/2404.05695
  code_url: https://github.com/roboterax/humanoid-gym
  category: Benchmark
  task_tags: [RL, sim2real, locomotion, sim-to-sim]
  robot_platform: RobotEra XBot-S/L (also Unitree H1, G1 forks)
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Isaac Gym RL framework with sim-to-sim (MuJoCo) and zero-shot real deployment.
  why_it_matters: Most-forked humanoid sim2real codebase; baseline for many follow-up policies.

- title: LIBERO - Lifelong Robot Learning Benchmark
  authors: Bo Liu, Yifeng Zhu, Chongkai Gao, et al.
  year: 2023
  venue: NeurIPS 2023
  arxiv_id: 2306.03310
  paper_url: https://arxiv.org/abs/2306.03310
  code_url: https://github.com/Lifelong-Robot-Learning/LIBERO
  category: Benchmark
  task_tags: [VLA, lifelong, manipulation]
  uses_simulation: yes
  code_status: open
  one_line: Lifelong manipulation benchmark; de facto VLA evaluation suite.
  why_it_matters: Standard for evaluating VLA generalization (used by OpenVLA, pi0, RT-X variants).

- title: RoboCasa - Large-Scale Simulation of Everyday Tasks
  authors: Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, et al.
  year: 2024
  venue: RSS 2024
  arxiv_id: 2406.02523
  paper_url: https://arxiv.org/abs/2406.02523
  project_url: https://robocasa.ai/
  code_url: https://github.com/robocasa/robocasa
  category: Benchmark
  task_tags: [kitchen, generative-scenes, manipulation]
  uses_simulation: yes
  code_status: open
  one_line: 100 kitchen tasks (25 atomic + 75 composite) in generative diverse scenes.
  why_it_matters: Largest realistic kitchen benchmark; widely used for VLA + skills evaluation.

- title: ManiSkill3 - GPU Parallelized Robotics Simulation
  authors: Stone Tao, Fanbo Xiang, Arth Shukla, et al.
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2410.00425
  paper_url: https://arxiv.org/abs/2410.00425
  project_url: https://www.maniskill.ai/
  code_url: https://github.com/haosulab/ManiSkill
  category: Benchmark
  task_tags: [GPU-sim, manipulation, dex, mobile, humanoid]
  uses_simulation: yes
  code_status: open
  one_line: Open-source GPU-parallel simulator (SAPIEN) hitting 30K+ FPS across 12 task domains.
  why_it_matters: Open alternative to Isaac Lab; supports humanoids and dex hands at scale.

- title: Open X-Embodiment - Robotic Learning Datasets and RT-X Models
  authors: Open X-Embodiment Collaboration
  year: 2023
  venue: ICRA 2024
  arxiv_id: 2310.08864
  paper_url: https://arxiv.org/abs/2310.08864
  project_url: https://robotics-transformer-x.github.io/
  code_url: https://github.com/google-deepmind/open_x_embodiment
  dataset_url: https://robotics-transformer-x.github.io/
  category: Dataset
  task_tags: [cross-embodiment, manipulation, VLA]
  code_status: open
  one_line: 1M+ trajectories, 22 embodiments, 60 datasets pooled across 21 institutions.
  why_it_matters: Foundation pretraining dataset for cross-embodiment VLA models (RT-X, Octo, OpenVLA).

- title: AgiBot World Colosseo
  authors: AgiBot World Team (OpenDriveLab)
  year: 2025
  venue: arXiv / IROS 2025
  arxiv_id: 2503.06669
  paper_url: https://arxiv.org/abs/2503.06669
  code_url: https://github.com/OpenDriveLab/AgiBot-World
  dataset_url: https://github.com/OpenDriveLab/AgiBot-World
  category: Dataset
  task_tags: [manipulation, large-scale, dual-arm]
  code_status: open
  one_line: 1M+ trajectories across 217 tasks in 5 deployment scenarios from 100 real robots.
  why_it_matters: Order-of-magnitude scale-up over OpenX; +30% transfer over OpenX-pretrained policies.

- title: RH20T - One-Shot Robot Manipulation Skills Dataset
  authors: Hao-Shu Fang, Hongjie Fang, Zhenyu Tang, Jirong Liu, et al.
  year: 2023
  venue: ICRA 2024
  arxiv_id: 2307.00595
  paper_url: https://arxiv.org/abs/2307.00595
  project_url: https://rh20t.github.io/
  dataset_url: https://rh20t.github.io/
  category: Dataset
  task_tags: [contact-rich, manipulation, multi-modal]
  code_status: open
  one_line: 110K+ contact-rich manipulation sequences (40+ TB) for one-shot skill learning.
  why_it_matters: Major contact-rich manipulation corpus with vision, force, audio.

- title: BridgeData V2 - Robot Learning at Scale
  authors: Homer Walke, Kevin Black, Tony Zhao, et al.
  year: 2023
  venue: CoRL 2023
  arxiv_id: 2308.12952
  paper_url: https://arxiv.org/abs/2308.12952
  project_url: https://rail-berkeley.github.io/bridgedata/
  dataset_url: https://rail-berkeley.github.io/bridgedata/
  category: Dataset
  task_tags: [WidowX, multi-task, IL]
  code_status: open
  one_line: 60,096 trajectories / 13 skills / 24 environments on low-cost WidowX arm.
  why_it_matters: Standard cross-environment generalization training set; used in Octo / OpenVLA.

- title: RoboMimic - Imitation Learning Study and Benchmark
  authors: Ajay Mandlekar, Danfei Xu, Josiah Wong, et al.
  year: 2021
  venue: CoRL 2021
  arxiv_id: 2108.03298
  paper_url: https://arxiv.org/abs/2108.03298
  project_url: https://robomimic.github.io/
  code_url: https://github.com/ARISE-Initiative/robomimic
  category: Benchmark
  task_tags: [IL, manipulation, study]
  code_status: open
  one_line: Reference IL benchmark + study with multiple proficiency-level demos.
  why_it_matters: Foundational IL study; canonical baselines (BC, BC-RNN, IQL) for manipulation.

- title: Mobile-ALOHA - Bimanual Mobile Whole-Body Teleop
  authors: Zipeng Fu, Tony Z. Zhao, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2401.02117
  paper_url: https://arxiv.org/abs/2401.02117
  project_url: https://mobile-aloha.github.io/
  code_url: https://github.com/MarkFzp/mobile-aloha
  dataset_url: https://github.com/MarkFzp/mobile-aloha
  category: Dataset
  task_tags: [mobile-manip, teleop, bimanual]
  uses_real_robot: yes
  code_status: open
  one_line: Low-cost mobile bimanual teleop platform + dataset for whole-body kitchen-scale tasks.
  why_it_matters: Key open-source whole-body teleop dataset; staple for IL on mobile humanoids.

- title: Habitat 3.0 - Co-Habitat for Humans, Avatars and Robots
  authors: Xavi Puig, Eric Undersander, Andrew Szot, et al.
  year: 2024
  venue: ICLR 2024
  arxiv_id: 2310.13724
  paper_url: https://arxiv.org/abs/2310.13724
  project_url: https://aihabitat.org/
  code_url: https://github.com/facebookresearch/habitat-sim
  category: Benchmark
  task_tags: [HRI, social-nav, social-rearrangement]
  uses_simulation: yes
  code_status: open
  one_line: Simulator with humanoid avatars + robots for social navigation/rearrangement.
  why_it_matters: First Habitat release with avatar humanoids; supports HRI policy evaluation.

- title: ALFWorld - Aligning Text and Embodied Environments
  authors: Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Cote, et al.
  year: 2021
  venue: ICLR 2021
  arxiv_id: 2010.03768
  paper_url: https://arxiv.org/abs/2010.03768
  code_url: https://github.com/alfworld/alfworld
  category: Benchmark
  task_tags: [language, embodied, planning]
  code_status: open
  one_line: Pairs ALFRED (3D) with TextWorld for cross-modality language-conditioned planning.
  why_it_matters: Common testbed for LLM/VLM agent planning research used alongside humanoid stacks.

- title: Isaac Lab (and Isaac Sim)
  authors: NVIDIA Robotics
  year: 2024
  venue: NVIDIA technical release
  project_url: https://isaac-sim.github.io/IsaacLab/
  code_url: https://github.com/isaac-sim/IsaacLab
  category: Benchmark
  task_tags: [GPU-sim, locomotion, manipulation, humanoid]
  uses_simulation: yes
  code_status: open
  one_line: Successor to Isaac Gym; PhysX-GPU framework with humanoid/manip task suites.
  why_it_matters: Default training environment for most 2024-2026 humanoid RL papers.

- title: Isaac Gym - High Performance GPU-Based Robot Learning
  authors: Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo, et al.
  year: 2021
  venue: NeurIPS 2021 D&B
  arxiv_id: 2108.10470
  paper_url: https://arxiv.org/abs/2108.10470
  code_url: https://github.com/isaac-sim/IsaacGymEnvs
  category: Benchmark
  task_tags: [GPU-sim, RL, legged]
  code_status: open
  one_line: Original GPU-parallelized PhysX simulator that enabled massive RL parallelism.
  why_it_matters: Backbone of nearly every legged-locomotion RL paper 2021-2024; predecessor to Isaac Lab.

- title: SAPIEN - Simulation Environment for Generic Articulated Tasks
  authors: Fanbo Xiang, Yuzhe Qin, Kaichun Mo, et al.
  year: 2020
  venue: CVPR 2020
  arxiv_id: 2003.08515
  paper_url: https://arxiv.org/abs/2003.08515
  project_url: https://sapien.ucsd.edu/
  code_url: https://github.com/haosulab/SAPIEN
  category: Benchmark
  task_tags: [articulated, manipulation, simulator]
  uses_simulation: yes
  code_status: open
  one_line: Articulated-object physical simulator powering ManiSkill series.
  why_it_matters: Open-source backbone for many manipulation simulators.

- title: Genesis - Universal Robotics Simulation Platform
  authors: Genesis Authors (Open collaboration)
  year: 2024
  venue: open release
  project_url: https://genesis-embodied-ai.github.io/
  code_url: https://github.com/Genesis-Embodied-AI/Genesis
  category: Benchmark
  task_tags: [GPU-sim, multi-physics, generative]
  uses_simulation: yes
  code_status: open
  one_line: Universal multi-physics simulator unifying rigid, soft, fluid, generative scenes.
  why_it_matters: New generation simulator with very high parallel throughput for embodied AI.

- title: MuJoCo Playground
  authors: Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, et al. (Google DeepMind)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.08844
  paper_url: https://arxiv.org/abs/2502.08844
  project_url: https://playground.mujoco.org/
  code_url: https://github.com/google-deepmind/mujoco_playground
  category: Benchmark
  task_tags: [MJX, JAX, sim2real, locomotion, dex]
  uses_simulation: yes
  code_status: open
  one_line: MJX/JAX-based open RL framework with zero-shot sim2real on 6+ robot platforms.
  why_it_matters: Open, fast MuJoCo-XLA stack with verified sim2real on Berkeley Humanoid, G1, T1.

- title: Brax - Differentiable Physics in JAX
  authors: C. Daniel Freeman, Erik Frey, Anton Raichuk, et al.
  year: 2021
  venue: NeurIPS 2021 D&B
  arxiv_id: 2106.13281
  paper_url: https://arxiv.org/abs/2106.13281
  code_url: https://github.com/google/brax
  category: Benchmark
  task_tags: [JAX, RL, GPU/TPU, locomotion]
  code_status: open
  one_line: JAX-native differentiable rigid-body simulator with TPU/GPU parallelism.
  why_it_matters: Used for massively parallel velocity-based humanoid RL.

- title: RoboHive - Unified Framework for Robot Learning
  authors: Vikash Kumar, Rutav Shah, Gaoyue Zhou, et al.
  year: 2023
  venue: NeurIPS 2023 D&B
  arxiv_id: 2310.06828
  paper_url: https://arxiv.org/abs/2310.06828
  code_url: https://github.com/vikashplus/robohive
  category: Benchmark
  task_tags: [unified-API, manipulation, dex, hardware]
  code_status: open
  one_line: Unified MuJoCo-based environments + hardware drivers for robot learning research.
  why_it_matters: One-stop simulator/hardware abstraction widely used for dex manipulation research.

---

## D. Sim-to-Real & Deployment Systems for Humanoid WBC

- title: H2O - Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  authors: Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, Guanya Shi
  year: 2024
  venue: IROS 2024
  arxiv_id: 2403.04436
  paper_url: https://arxiv.org/abs/2403.04436
  project_url: https://human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Sim2Real
  task_tags: [teleop, WBC, RGB]
  robot_platform: Unitree H1
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: First RL-based real-time whole-body humanoid teleop from a single RGB camera.
  why_it_matters: Demonstrates sim-trained WBC policies deployable from RGB; influential teleop baseline.

- title: OmniH2O - Universal Dexterous Human-to-Humanoid Whole-Body Teleop
  authors: Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.08858
  paper_url: https://arxiv.org/abs/2406.08858
  project_url: https://omni.human2humanoid.com/
  code_url: https://github.com/LeCAR-Lab/human2humanoid
  category: Sim2Real
  task_tags: [teleop, dex-hands, VR, autonomy]
  robot_platform: Unitree H1 + dex hands
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Sim2real dexterous WBC + OmniH2O-6 dataset; teleop via VR/voice/RGB.
  why_it_matters: One of the strongest open WBC + dex teleop pipelines; sets benchmark for sim2real WBC.

- title: HumanPlus - Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  category: Sim2Real
  task_tags: [shadowing, imitation, WBC]
  robot_platform: Unitree H1
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Sim2real shadowing policy + imitation pipeline on Unitree H1 from RGB human video.
  why_it_matters: Shows full-stack sim2real WBC autonomy bootstrapped from internet human data.

- title: ExBody - Expressive Whole-Body Control for Humanoid Robots
  authors: Xuxin Cheng, Yandong Ji, Junming Chen, Ruihan Yang, Ge Yang, Xiaolong Wang
  year: 2024
  venue: RSS 2024
  arxiv_id: 2402.16796
  paper_url: https://arxiv.org/abs/2402.16796
  project_url: https://expressive-humanoid.github.io/
  code_url: https://github.com/chengxuxin/expressive-humanoid
  category: Sim2Real
  task_tags: [WBC, expressive, AMASS]
  robot_platform: Unitree H1
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Sim2real expressive whole-body control imitating AMASS while preserving locomotion.
  why_it_matters: Established the AMASS-conditioned WBC paradigm now used widely.

- title: ExBody2 - Advanced Expressive Humanoid Whole-Body Control
  authors: Mazeyu Ji, Xuanbin Peng, Fangchen Liu, Jialong Li, Ge Yang, Xuxin Cheng, Xiaolong Wang
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2412.13196
  paper_url: https://arxiv.org/abs/2412.13196
  project_url: https://exbody2.github.io/
  category: Sim2Real
  task_tags: [WBC, teacher-student, sim2real]
  robot_platform: Unitree H1, G1
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: partial
  one_line: Decouples keypoint tracking and velocity control; teacher distillation for high-fidelity dynamic motions.
  why_it_matters: SOTA expressive WBC sim2real; jumps, dance, crouch, run on multi-platform humanoids.

- title: ASAP - Aligning Simulation and Real-World Physics for Agile Humanoid WBC
  authors: Tairan He, Jiawei Gao, Wenli Xiao, Yuanhang Zhang, Zi Wang, Jiashun Wang, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.01143
  paper_url: https://arxiv.org/abs/2502.01143
  project_url: https://agile.human2humanoid.com/
  category: Sim2Real
  task_tags: [delta-action, residual-dynamics, agile-WBC]
  robot_platform: Unitree G1
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: open
  one_line: Two-stage pretrain + delta-action residual model that compensates sim-real dynamics mismatch.
  why_it_matters: Beats SysID/DR for agile humanoid skills; defines new strong sim2real baseline.

- title: BeyondMimic - Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  authors: Takara Truong, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2508.08241
  paper_url: https://arxiv.org/abs/2508.08241
  project_url: https://beyondmimic.github.io/
  code_url: https://github.com/HybridRobotics/whole_body_tracking
  category: Sim2Real
  task_tags: [motion-tracking, diffusion-policy, WBC]
  robot_platform: Unitree G1
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: open
  one_line: Sim2real motion tracking + unified diffusion policy enabling zero-shot test-time tasks.
  why_it_matters: First framework distilling tracked motions into a single steerable diffusion policy on hardware.

- title: MOSAIC - Bridging Sim2Real with Rapid Residual Adaptation
  authors: Tairan He, et al.
  year: 2026
  venue: arXiv preprint
  arxiv_id: 2602.08594
  paper_url: https://arxiv.org/abs/2602.08594
  category: Sim2Real
  task_tags: [residual-adaptation, generalist, motion-tracking]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Generalist humanoid motion-tracking with rapid residual adaptation for sim-to-real gap.
  why_it_matters: Combines RMA-style fast adaptation with generalist tracking; complementary to ASAP.

- title: VIRAL - Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
  authors: VIRAL Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2511.15200
  paper_url: https://arxiv.org/abs/2511.15200
  category: Sim2Real
  task_tags: [vision, loco-manip, scale]
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: pending
  one_line: Vision-based humanoid loco-manipulation trained entirely in sim; zero-shot to hardware.
  why_it_matters: Scale-driven visual sim2real recipe for humanoids.

- title: PolySim - Multi-Simulator Dynamics Randomization for Humanoid Sim2Real
  authors: PolySim Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2510.01708
  paper_url: https://arxiv.org/abs/2510.01708
  category: Sim2Real
  task_tags: [multi-sim, randomization, robustness]
  uses_humanoid: yes
  uses_simulation: yes
  code_status: pending
  one_line: Trains across multiple simulators to randomize dynamics and shrink sim-to-real gap.
  why_it_matters: Novel multi-simulator angle on DR specifically for humanoids.

- title: VR-Robo - Real-to-Sim-to-Real for Visual Navigation
  authors: VR-Robo Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.01536
  paper_url: https://arxiv.org/abs/2502.01536
  category: Sim2Real
  task_tags: [real2sim, photorealistic, navigation]
  uses_real_robot: yes
  uses_simulation: yes
  code_status: pending
  one_line: Builds photoreal interactive digital twins for visual navigation/locomotion sim2real.
  why_it_matters: Real-to-sim-to-real loop with photo-realistic Gaussians; relevant to humanoid navigation.

- title: Sim-to-Real RL for Vision-Based Dexterous Manipulation on Humanoids
  authors: Toru Lin, Kartik Sachdev, Linxi Fan, Jitendra Malik, Yuke Zhu
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.20396
  paper_url: https://arxiv.org/abs/2502.20396
  category: Sim2Real
  task_tags: [dex-manip, vision, RL]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Sim2real recipe for grasp-and-reach, lift, bimanual handover on a real humanoid.
  why_it_matters: Concrete dex sim2real recipe for humanoid hands; ablations on key design decisions.

- title: Humanoid Parkour Learning
  authors: Ziwen Zhuang, Shenzhe Yao, Hang Zhao
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10759
  paper_url: https://arxiv.org/abs/2406.10759
  project_url: https://humanoid4parkour.github.io/
  category: Sim2Real
  task_tags: [parkour, vision, WBC]
  robot_platform: Unitree H1
  uses_humanoid: yes
  uses_real_robot: yes
  uses_simulation: yes
  code_status: partial
  one_line: End-to-end vision WBC parkour policy: 0.42m platform, 0.8m gap, 1.8m/s running.
  why_it_matters: Pioneering humanoid parkour without motion priors; pure RL+vision.

- title: Hiking in the Wild - Scalable Perceptive Parkour for Humanoids
  authors: Hiking Authors
  year: 2026
  venue: arXiv preprint
  arxiv_id: 2601.07718
  paper_url: https://arxiv.org/abs/2601.07718
  category: Sim2Real
  task_tags: [parkour, perception, outdoor]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Scalable perceptive parkour framework deployed in outdoor wild environments.
  why_it_matters: Pushes humanoid parkour to unstructured terrain.

- title: Crocoddyl - Multi-Contact Optimal Control Framework
  authors: Carlos Mastalli, Rohan Budhiraja, et al.
  year: 2020
  venue: ICRA 2020
  arxiv_id: 1909.04947
  paper_url: https://arxiv.org/abs/1909.04947
  code_url: https://github.com/loco-3d/crocoddyl
  category: Sim2Real
  task_tags: [trajectory-optimization, DDP, multi-contact]
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open
  one_line: Efficient analytical-derivative DDP solver for multi-contact humanoid optimal control.
  why_it_matters: Reference TrajOpt library underlying many MPC humanoid stacks; ms-scale jumps and flips.

- title: Opt2Skill - Imitating Whole-Body Trajectories for Humanoid Loco-Manip
  authors: Wenli Xiao, et al.
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2409.20514
  paper_url: https://arxiv.org/abs/2409.20514
  category: Sim2Real
  task_tags: [TrajOpt, loco-manip, imitation]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Pairs trajectory-optimization references with RL imitation for versatile humanoid loco-manip.
  why_it_matters: Bridges model-based TrajOpt and learning for sim2real WBC.

- title: WoCoCo - Whole-Body Humanoid Control with Sequential Contacts
  authors: Chong Zhang, et al.
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.06005
  paper_url: https://arxiv.org/abs/2406.06005
  category: Sim2Real
  task_tags: [contacts, WBC, sequential]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Whole-body control formulation built around explicit sequential contact specifications.
  why_it_matters: Contact-centric WBC that reasons over contact schedules, better for manip + loco.

- title: RMA - Rapid Motor Adaptation for Legged Robots
  authors: Ashish Kumar, Zipeng Fu, Deepak Pathak, Jitendra Malik
  year: 2021
  venue: RSS 2021
  arxiv_id: 2107.04034
  paper_url: https://arxiv.org/abs/2107.04034
  project_url: https://ashish-kmr.github.io/rma-legged-robots/
  category: Sim2Real
  task_tags: [adaptation, base-policy, A1]
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Two-stage base-policy + adaptation module enabling online sim2real adaptation in <1s.
  why_it_matters: Foundational adaptation paradigm reused by humanoid sim2real (MOSAIC, ASAP, ExBody2).

- title: Adversarial Motion Priors (AMP) - Stylistic Motor Skills
  authors: Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
  year: 2021
  venue: SIGGRAPH 2021
  arxiv_id: 2104.02180
  paper_url: https://arxiv.org/abs/2104.02180
  project_url: https://xbpeng.github.io/projects/AMP/
  category: Sim2Real
  task_tags: [GAIL, style-rewards, mocap]
  uses_simulation: yes
  code_status: open
  one_line: Adversarial style reward enabling motion-prior-conditioned RL on physics characters.
  why_it_matters: Backbone of dozens of humanoid AMP-based locomotion sim2real papers.

- title: Multi-AMP - Advanced Skills with Multiple Motion Priors
  authors: Eric Vollenweider, Marko Bjelonic, Victor Klemm, et al.
  year: 2022
  venue: ICRA 2023
  arxiv_id: 2203.14912
  paper_url: https://arxiv.org/abs/2203.14912
  category: Sim2Real
  task_tags: [multi-prior, AMP, sim2real]
  uses_simulation: yes
  code_status: pending
  one_line: Multiple motion priors in AMP for richer skill repertoire on legged robots.
  why_it_matters: Important AMP extension; precursor to multi-prior humanoid policies.

- title: Sampling-Based System ID with Active Exploration (SPI-Active)
  authors: Tairan He, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2505.14266
  paper_url: https://arxiv.org/abs/2505.14266
  project_url: https://lecar-lab.github.io/spi-active_/
  category: Sim2Real
  task_tags: [system-id, active-exploration, legged]
  uses_real_robot: yes
  uses_simulation: yes
  code_status: pending
  one_line: Active sampling-based system identification improves sim2real over plain DR.
  why_it_matters: Modern alternative to DR; targets accurate dynamics models for legged sim2real.

- title: Dynamics Randomization Revisited - Quadrupedal Locomotion Case Study
  authors: Ananye Agarwal, et al.
  year: 2020
  venue: ICRA 2021
  arxiv_id: 2011.02404
  paper_url: https://arxiv.org/abs/2011.02404
  category: Sim2Real
  task_tags: [DR, quadruped, sim2real]
  uses_real_robot: yes
  uses_simulation: yes
  code_status: open
  one_line: Argues for selective, principled DR rather than blanket randomization.
  why_it_matters: Influential study informing DR practice in humanoid stacks today.

- title: Robot Learning from Randomized Simulations - Survey
  authors: Fabio Muratore, Fabio Ramos, Greg Turk, Wenhao Yu, Michael Gienger, Jan Peters
  year: 2021
  venue: Frontiers in Robotics and AI
  arxiv_id: 2111.00956
  paper_url: https://arxiv.org/abs/2111.00956
  category: Sim2Real
  task_tags: [survey, DR, sim2real]
  code_status: n/a
  one_line: Comprehensive survey of randomized-simulation methods for sim2real transfer.
  why_it_matters: Standard reference for DR taxonomy and methodology.

- title: MoCapAct - Multi-Task Dataset for Simulated Humanoid Control
  authors: Nolan Wagener, Andrey Kolobov, Felipe Vieira Frujeri, Ricky Loynd, Ching-An Cheng, Matthew Hausknecht
  year: 2022
  venue: NeurIPS 2022 D&B
  arxiv_id: 2208.07363
  paper_url: https://arxiv.org/abs/2208.07363
  project_url: https://microsoft.github.io/MoCapAct/
  code_url: https://github.com/microsoft/MoCapAct
  category: Dataset
  task_tags: [MuJoCo, expert-policies, mocap]
  uses_humanoid: yes
  uses_simulation: yes
  code_status: open
  one_line: 2,500+ MoCap-tracking expert policies + rollouts for the dm_control humanoid.
  why_it_matters: Large simulated humanoid behavioral dataset for offline RL / IL pretraining.

- title: Mobile-TeleVision - Predictive Motion Priors for Humanoid WBC
  authors: Mobile TeleVision Authors
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2412.07773
  paper_url: https://arxiv.org/abs/2412.07773
  category: Sim2Real
  task_tags: [teleop, WBC, predictive-priors]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Predictive motion priors used for humanoid WBC during teleoperation.
  why_it_matters: Latency-tolerant prior-based teleop strategy on humanoid hardware.

- title: Denoising World Model Learning for Humanoid Locomotion
  authors: Xinyang Gu, et al.
  year: 2024
  venue: arXiv preprint
  arxiv_id: 2408.14472
  paper_url: https://arxiv.org/abs/2408.14472
  category: Sim2Real
  task_tags: [world-model, terrain, locomotion]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Denoising world-model RL pushes humanoid locomotion onto challenging terrains.
  why_it_matters: World-model approach to humanoid sim2real on non-flat terrain.

- title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  authors: Anonymous (arXiv preprint)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2512.01996
  paper_url: https://arxiv.org/abs/2512.01996
  category: Sim2Real
  task_tags: [fast-training, sim2real, locomotion]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: 15-minute training pipeline for deployable humanoid locomotion policies.
  why_it_matters: Demonstrates dramatic compute reduction for humanoid sim2real.

- title: Pixel-to-Action Sim2Real for Humanoid
  authors: Anonymous
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2512.01061
  paper_url: https://arxiv.org/abs/2512.01061
  category: Sim2Real
  task_tags: [vision, end-to-end, sim2real]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: End-to-end pixel-to-action humanoid policy transferred sim-to-real.
  why_it_matters: Visuomotor humanoid sim2real without intermediate state estimation.

- title: From Experts to a Generalist - General Whole-Body Control for Humanoid Robots
  authors: Anonymous
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2506.12779
  paper_url: https://arxiv.org/abs/2506.12779
  category: Sim2Real
  task_tags: [generalist, distillation, WBC]
  uses_humanoid: yes
  uses_real_robot: yes
  code_status: pending
  one_line: Distills many specialist humanoid skills into a single generalist WBC policy.
  why_it_matters: Generalist WBC paradigm; complementary to BeyondMimic's diffusion approach.

---

## E. Evaluation Metrics & Contact Modeling

- title: ContactPose - Dataset of Grasps with Object Contact and Hand Pose
  authors: Samarth Brahmbhatt, Chengcheng Tang, Christopher D. Twigg, Charles C. Kemp, James Hays
  year: 2020
  venue: ECCV 2020
  arxiv_id: 2007.09545
  paper_url: https://arxiv.org/abs/2007.09545
  project_url: https://contactpose.cc.gatech.edu/
  dataset_url: https://contactpose.cc.gatech.edu/
  category: Contact-Model
  task_tags: [thermal-contact, grasping, RGB-D]
  code_status: open
  one_line: 2,306 grasps of 25 objects with thermal-imaging-derived contact maps + RGB-D + hand pose.
  why_it_matters: First large hand-object contact dataset; benchmark for contact prediction.

- title: ContactOpt - Optimizing Contact to Improve Grasps
  authors: Patrick Grady, Chengcheng Tang, Christopher D. Twigg, Minh Vo, Samarth Brahmbhatt, Charles C. Kemp
  year: 2021
  venue: CVPR 2021
  paper_url: https://openaccess.thecvf.com/content/CVPR2021/papers/Grady_ContactOpt_Optimizing_Contact_To_Improve_Grasps_CVPR_2021_paper.pdf
  code_url: https://github.com/facebookresearch/ContactOpt
  category: Contact-Model
  task_tags: [grasp-refinement, differentiable-contact]
  code_status: open
  one_line: Predicts desired contact then differentiably optimizes hand pose to achieve it.
  why_it_matters: Standard hand-grasp-refinement baseline; contact-driven optimization paradigm.

- title: ContactGen - Generative Contact Modeling for Grasp Generation
  authors: Shaowei Liu, Yang Zhou, Jimei Yang, Saurabh Gupta, Shenlong Wang
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2310.03740
  paper_url: https://arxiv.org/abs/2310.03740
  project_url: https://stevenlsw.github.io/contactgen/
  code_url: https://github.com/stevenlsw/contactgen
  category: Contact-Model
  task_tags: [generative, contact-map, part-map, direction-map]
  code_status: open
  one_line: Object-centric (contact, part, direction) representation + conditional generative grasp model.
  why_it_matters: Diverse, geometrically feasible grasp generation; common evaluation target.

- title: COAP - Compositional Articulated Occupancy
  authors: Marko Mihajlovic, Shunsuke Saito, Aayush Bansal, Michael Zollhoefer, Siyu Tang
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2204.06184
  paper_url: https://arxiv.org/abs/2204.06184
  project_url: https://neuralbodies.github.io/COAP/
  code_url: https://github.com/markomih/COAP
  category: Contact-Model
  task_tags: [neural-implicit, body-occupancy, collision]
  code_status: open
  one_line: Neural implicit articulated body occupancy enabling fast self/scene collision queries.
  why_it_matters: Standard penetration / scene-collision metric backbone in HSI/HOI evaluation.

- title: GRIP - Robotic Incremental Potential Contact Simulation Dataset
  authors: Hongyu Wei, et al.
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2503.05020
  paper_url: https://arxiv.org/abs/2503.05020
  project_url: https://bell0o.github.io/GRIP/
  category: Contact-Model
  task_tags: [IPC, deformable, soft-grippers]
  code_status: open
  one_line: 100K grasps with IPC-based deformable+rigid contact simulation; UMI + LEAP hand.
  why_it_matters: First large-scale soft-rigid coupled grasp dataset; benchmark for compliant gripper learning.

- title: IPMAN - 3D Human Pose Estimation via Intuitive Physics
  authors: Shashank Tripathi, Lea Mueller, Chun-Hao P. Huang, Omid Taheri, Michael J. Black, Dimitrios Tzionas
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2303.18246
  paper_url: https://arxiv.org/abs/2303.18246
  project_url: https://ipman.is.tue.mpg.de/
  category: Evaluation-Metric
  task_tags: [physics, CoP, CoM, stability]
  code_status: open
  one_line: Pressure heatmap + CoP + CoM regularization yielding physically plausible 3D bodies.
  why_it_matters: Defines CoM/CoP physical-plausibility metrics adopted across humanoid pose work.

- title: Measuring Physical Plausibility via Physics Simulation
  authors: Authors of the metric paper
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2502.04483
  paper_url: https://arxiv.org/abs/2502.04483
  category: Evaluation-Metric
  task_tags: [plausibility, physics-sim, CoM-distance, stability-duration]
  code_status: pending
  one_line: Proposes CoM-distance and Pose Stability Duration as physics-based plausibility metrics.
  why_it_matters: Introduces standardized physical-plausibility evaluation procedure.

- title: PhysHMR - Physically Plausible Human Motion Reconstruction via Humanoid Control
  authors: PhysHMR Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2510.02566
  paper_url: https://arxiv.org/abs/2510.02566
  category: Evaluation-Metric
  task_tags: [HMR, humanoid-control, vision]
  uses_humanoid: yes
  uses_simulation: yes
  code_status: pending
  one_line: Learns vision-driven humanoid control policy yielding physically plausible motion reconstruction.
  why_it_matters: Bridges vision-based HMR and simulated humanoid control; redefines plausibility evaluation.

- title: PhySIC - Physically Plausible 3D HSI and Contact from a Single Image
  authors: PhySIC Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2510.11649
  paper_url: https://arxiv.org/abs/2510.11649
  category: Evaluation-Metric
  task_tags: [HSI, contact, single-image]
  code_status: pending
  one_line: Reconstructs metrically aligned human + scene with vertex-level contact maps.
  why_it_matters: Joint contact + plausibility from a single RGB; a useful evaluation reference.

- title: Hand-Object Contact Detection using Grasp Quality Metrics
  authors: Anonymous (arXiv preprint)
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2501.06987
  paper_url: https://arxiv.org/abs/2501.06987
  category: Evaluation-Metric
  task_tags: [grasp-quality, contact-detection]
  code_status: pending
  one_line: Uses grasp-quality (Q1, Ferrari-Canny) measures as contact-detection signals.
  why_it_matters: Connects classical grasp-quality wrench metrics to learning-based contact detection.

- title: Penetration / Float / Skate Metrics (HMR Plausibility Suite)
  authors: Multiple (formalized in IPMAN, GRAB, BEHAVE, OMOMO)
  year: 2020-2024
  venue: Cumulative
  paper_url: https://ipman.is.tue.mpg.de/
  category: Evaluation-Metric
  task_tags: [penetration, foot-skate, ground-floating]
  code_status: open
  one_line: Standard suite: ground penetration depth, unsupported floating distance, foot-skating percentage.
  why_it_matters: De facto physical-plausibility metrics for motion generation and humanoid imitation.

- title: PA-HOI - Physics-Aware Human-Object Interaction Dataset
  authors: PA-HOI Authors
  year: 2025
  venue: arXiv preprint
  arxiv_id: 2508.06205
  paper_url: https://arxiv.org/abs/2508.06205
  category: Dataset
  task_tags: [HOI, physics, contact-aware]
  code_status: pending
  one_line: HOI dataset captured/annotated with explicit physics-aware contact and force labels.
  why_it_matters: New evaluation substrate emphasizing physical correctness in HOI.

- title: HumanoidArena: Benchmarking Egocentric Hierarchical Whole-Body Learning
  authors: Taowen Wang; Zikang Xie; Bin Yang; Yunheng Wang; Zizhao Yuan; Yuetong Fang; Yixiao Feng; Yichi Wang; Xingyu Chen; Haodong Chen; Qiwei Wu; Weisheng Xu; Lihan Chen; Lusong Li; Zecui Zeng; Renjing Xu
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.17833
  paper_url: https://arxiv.org/abs/2606.17833
  project_url: https://humanoidarena.github.io
  code_url: ""
  category: Dataset
  task_tags: [benchmark, egocentric-control, hierarchical-policy, whole-body-learning]
  robot_platform: humanoid
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Simulation-first benchmark evaluating whether high-level egocentric policies produce intermediate whole-body actions that trackers can execute.
  why_it_matters: Separates task reasoning from tracker feasibility, a key failure mode in hierarchical humanoid control stacks.

- title: Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI
  authors: Xianda Guo; Bohao Zhang; Chenwei Huang; Shiyuan Chen; Ruilin Wang; Yiqun Duan; Cong Yang; Qin Zou; Wei Sui
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.22971
  paper_url: https://arxiv.org/abs/2606.22971
  project_url: https://d-robotics-ai-lab.github.io/humanoid-omniocc
  code_url: ""
  dataset_url: ""
  category: Dataset
  task_tags: [occupancy-prediction, stereo, humanoid-perception, Real2Sim2Real]
  robot_platform: humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⏳ Code Coming Soon
  one_line: Full-view panoramic stereo occupancy dataset and model for humanoid perception, built around real sensor specs, simulated annotation, and real-world evaluation.
  why_it_matters: Gives humanoid navigation/manipulation stacks a perception dataset shaped around body-mounted stereo coverage rather than autonomous-driving assumptions.

- title: Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory
  authors: Yuhan Wu; Zhao Jin; Tao Li; Yuheng Zhang; Zhichao Wang; Shuo Wang; Jun Jiang; Xiaobo Li; Yanyong Zhang; Jian Tang; Zhengping Che; Yan Xia
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.31037
  paper_url: https://arxiv.org/abs/2606.31037
  project_url: https://labimus.github.io/
  code_url: ""
  dataset_url: ""
  category: Dataset
  task_tags: [benchmark, humanoid-dexterous-manipulation, chemistry-lab, precision-evaluation]
  robot_platform: humanoid dexterous hands
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: 🌐 Project Page
  one_line: Reconstructs organic-chemistry workstations and defines precision-critical humanoid manipulation tasks with instrument readouts and quantitative tolerances.
  why_it_matters: Benchmarks whether humanoid manipulation succeeds at scientific-process validity, not just coarse task completion.

- title: RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation
  authors: Xinyi Wang; Donghan Li; Zi'Ang Chen; Chong Yu; Chen Xin; Peng Ye; Yingkai Sun; Tao Chen
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.31836
  paper_url: https://arxiv.org/abs/2606.31836
  project_url: ""
  code_url: ""
  dataset_url: ""
  category: Dataset
  task_tags: [visual-tactile-action-data, humanoid-manipulation, Unitree-G1, dexterous-hands]
  robot_platform: Unitree G1
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: false
  code_status: ⏳ Code Coming Soon
  one_line: Collects 6k Unitree G1 dexterous-manipulation trajectories across 19 tasks with multi-view RGB-D, tactile feedback, and semantic annotations.
  why_it_matters: Adds tactile and synchronized multi-camera supervision to humanoid hand manipulation datasets, but the dataset was only announced as forthcoming.

- title: Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning
  authors: Satoshi Yamamori; Koji Ishihara; Kentaro Minamikawa; Kiyoharu Ohomori; Taiyo Yazaki; Norikazu Sugimoto; Jun Morimoto
  year: 2026
  venue: arXiv 2026.07
  arxiv_id: 2607.02205
  paper_url: https://arxiv.org/abs/2607.02205
  project_url: ""
  code_url: ""
  dataset_url: ""
  category: Sim2Real
  task_tags: [actuator-modeling, sim-to-real, zero-shot-transfer, humanoid-walking]
  robot_platform: single-joint servo / 7-DoF arm / wheeled-legged robot / humanoid
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Shapes real actuator closed-loop dynamics to match idealized simulation reference dynamics, enabling zero-shot policies across arms, wheeled-legged robots, and humanoid walking.
  why_it_matters: Offers a hardware-interface alternative to learned actuator models or heavier simulator randomization for humanoid sim-to-real deployment.

---

## Notes

- "code_status" values: open / partial / pending / n/a.
- arxiv_id "2602.xxxxx", "2601.xxxxx", "2603.xxxxx" entries reflect very-recent (2026) preprints surfaced during search; treat IDs/dates with light caution.
- AMP, RMA, Crocoddyl pre-date 2022 but are foundational for humanoid sim2real and intentionally retained.
- HumanML3D-X / "MoCapAct" / "Multi-AMP" included as related siblings to dataset/method requests.
- "HumanoidVerse benchmark" did not surface as a stable, widely-cited benchmark - HumanoidBench, BiGym, LocoMujoco, Humanoid-Gym, and MuJoCo Playground listed as the canonical humanoid WBC benchmark stack instead.
