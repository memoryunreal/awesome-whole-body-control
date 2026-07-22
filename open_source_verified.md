# Verified Open-Source Papers

This is the canonical list of papers with **verified official open-source code** (225 entries). Each repo was sanity-checked for actual implementation files (not placeholder READMEs).

## Human-Object Interaction Motion Generation (18)

- ⭐ 🧍 🧱 **[DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects](https://arxiv.org/abs/2606.15133)** `arXiv 2026.06` `HOI-Motion-Gen`
  Tianshan Zhang et al..
  Generates and trains physically plausible dexterous hand-object interactions with articulated objects using contact-aware simulation assets and RL code.
  Links: [Project](https://aigeeksgroup.github.io/DragMesh-2) · [Code](https://github.com/AIGeeksGroup/DragMesh-2) · [Paper](https://arxiv.org/abs/2606.15133) · [Dataset](https://huggingface.co/datasets/AIGeeksGroup/DragMesh-2)

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


## Object-Aware Human Motion Synthesis (13)

- ⭐ 🧍 🧱 **[TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization](https://arxiv.org/abs/2503.19901)** `CVPR 2025 (Oral)` `Object-Aware-Motion`
  Liang Pan, Zeshi Yang, Zhiyang Dou, Wenjia Wang, Buzhen Huang, Bo Dai, Taku Komura, Jingbo Wang.
  Unified transformer policy with proprio + task tokens for multi-skill physical HSI.
  Links: [Project](https://liangpan99.github.io/TokenHSI/) · [Code](https://github.com/liangpan99/TokenHSI) · [Paper](https://arxiv.org/abs/2503.19901)

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


## Whole-Body Motion Tracking and Imitation (53)

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

- ⭐ 🧍 🧱 **[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)** `SIGGRAPH 2018 (TOG)` `SMPL/Mujoco humanoid` `Motion-Imitation`
  Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne.
  Foundational RL framework for imitating mocap clips on simulated characters with reference state initialization and early termination.
  Links: [Project](https://xbpeng.github.io/projects/DeepMimic/index.html) · [Code](https://github.com/xbpeng/DeepMimic) · [Paper](https://arxiv.org/abs/1804.02717)


## Whole-Body Control and Loco-Manipulation (30)

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


## Humanoid Foundation Models and Generalist Policies (37)

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


## Human-to-Humanoid Retargeting (4)

- ⭐ 🤖 🧍 **[Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](https://arxiv.org/abs/2606.22136)** `arXiv 2026.06` `dexterous hands / humanoid-relevant manipulation` `Retargeting`
  Yangtao Chen et al..
  Uses generative video world models to synthesize egocentric human-object manipulation videos and converts them into robot-trainable supervision.
  Links: [Project](https://chenyt31.github.io/wh0.github.io/) · [Code](https://github.com/chenyt31/Wh0) · [Paper](https://arxiv.org/abs/2606.22136)

- ⭐ 🤖 🧍 **[HumanoidVerse: A Versatile Multi-Simulator Humanoid Learning Framework](https://arxiv.org/abs/2508.16943)** `arXiv preprint` `Unitree G1/H1, multiple` `Retargeting`
  LeCAR Lab.
  Modular multi-simulator framework for humanoid skill learning with retargeted human MoCap, used by ASAP and follow-ups.
  Links: [Project](https://github.com/LeCAR-Lab/HumanoidVerse) · [Code](https://github.com/LeCAR-Lab/HumanoidVerse) · [Paper](https://arxiv.org/abs/2508.16943)

- ⭐ 🧱 **[DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2505.24853)** `NeurIPS 2025` `multiple dexterous hands` `Retargeting`
  Mandi Zhao, et al..
  Functional retargeting via decaying virtual object controllers for long-horizon bimanual articulated-object manipulation from human demos.
  Links: [Project](https://project-dexmachina.github.io/) · [Code](https://github.com/MandiZhao/dexmachina) · [Paper](https://arxiv.org/abs/2505.24853)

- ⭐ 🧍 🧱 **[Mink — Differential Inverse Kinematics in Python (MuJoCo)](https://kevinzakka.github.io/mink/)** `open-source library` `G1, H1, Apollo, dual arms, dexterous hands` `Retargeting`
  Kevin Zakka.
  Composable task-space IK on MuJoCo used by GMR, ProtoMotions, and many teleop stacks for retargeting and live tracking.
  Links: [Project](https://kevinzakka.github.io/mink/) · [Code](https://github.com/kevinzakka/mink) · [Paper](https://kevinzakka.github.io/mink/)


## Teleoperation and Demonstration Collection (21)

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

- ⭐ 🤖 **[Robotic Telekinesis: Learning a Robotic Hand Imitator by Watching Humans on Youtube](https://arxiv.org/abs/2202.10448)** `RSS 2022` `Allegro Hand on Franka` `Teleoperation`
  Aravind Sivakumar, Kenneth Shaw, Deepak Pathak.
  Single-RGB-camera teleop trained on internet hand videos; first low-cost glove-free dexterous teleop.
  Links: [Project](https://robotic-telekinesis.github.io/) · [Code](https://github.com/sraviakv/robotic-telekinesis) · [Paper](https://arxiv.org/abs/2202.10448)

- ⭐ **[iCub3 Avatar System - Enabling Remote Fully-Immersive Embodiment of Humanoid Robots](https://arxiv.org/abs/2203.06972)** `arXiv 2022.03 / Science Robotics` `Teleop`
  Fully-immersive remote embodiment with iCub3 avatar.
  Links: [Project](https://www.science.org/doi/10.1126/scirobotics.adh3834) · [Code](https://github.com/ami-iit/paper_dafarra_2024_science-robotics_icub3-avatar-system) · [Paper](https://arxiv.org/abs/2203.06972)


## Datasets and Benchmarks (36)

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


## Evaluation Metrics and Contact Modeling (3)

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


## Sim-to-Real and Deployment Systems (1)

- ⭐ 🧍 🧱 **[Crocoddyl - Multi-Contact Optimal Control Framework](https://arxiv.org/abs/1909.04947)** `ICRA 2020` `Sim2Real`
  Carlos Mastalli, Rohan Budhiraja, et al..
  Efficient analytical-derivative DDP solver for multi-contact humanoid optimal control.
  Links: [Code](https://github.com/loco-3d/crocoddyl) · [Paper](https://arxiv.org/abs/1909.04947)


## Related Character Animation and Physics-Based Motion Generation (9)

- ⭐ 🧍 🧱 **[WaveSync: Constrained Wavefront Optimization for Synchronized Co-Speech Gestures in Humanoid Robots](https://arxiv.org/abs/2606.16600)** `arXiv 2026.06` `COMAN humanoid` `Physics-Anim`
  Thang Tran Viet et al..
  Converts speech emphasis into hardware-safe humanoid gesture trajectories using constrained wavefront optimization and robot models.
  Links: [Project](https://github.com/pairs-lab/WaveSync) · [Code](https://github.com/pairs-lab/WaveSync) · [Paper](https://arxiv.org/abs/2606.16600)

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

- ⭐ 🧍 🧱 **[Omnigrasp: Grasping Diverse Objects with Simulated Humanoids](https://arxiv.org/abs/2407.11385)** `NeurIPS 2024` `sim-only SMPL-X humanoid with hands` `Physics-Anim`
  Zhengyi Luo, Jinkun Cao, Sammy Christen, Alexander Winkler, Kris Kitani, Weipeng Xu.
  Hierarchical RL on PULSE motion prior enables a humanoid to grasp 1200+ objects on diverse trajectories.
  Links: [Project](https://www.zhengyiluo.com/Omnigrasp-Site/) · [Code](https://github.com/ZhengyiLuo/Omnigrasp) · [Paper](https://arxiv.org/abs/2407.11385)

- ⭐ 🧍 🧱 **[PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction](https://arxiv.org/abs/2312.04393)** `arXiv 2023` `sim-only humanoid (IsaacGym)` `Physics-Anim`
  Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian Zhang, Lei Zhang.
  Contact-graph reward enables physics-based imitation of full-body human-object interactions (basketball).
  Links: [Project](https://wyhuai.github.io/physhoi-page/) · [Code](https://github.com/wyhuai/PhysHOI) · [Paper](https://arxiv.org/abs/2312.04393) · [Dataset](BallPlay)

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

