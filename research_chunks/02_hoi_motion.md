# Human-Object Interaction (HOI) Motion Generation & Object-Aware Human Motion Synthesis

Curated paper list (2022-2026, priority on 2024-2026). Code status verified via GitHub/project pages where possible.

---

- title: HOI-Diff: Text-Driven Synthesis of 3D Human-Object Interactions using Diffusion Models
  authors: Xiaogang Peng, Yiming Xie, Zizhao Wu, Varun Jampani, Deqing Sun, Huaizu Jiang
  year: 2023
  venue: arXiv 2023.12 / CVPRW 2025 (HuMoGen)
  arxiv_id: 2312.06553
  paper_url: https://arxiv.org/abs/2312.06553
  project_url: https://neu-vi.github.io/HOI-Diff/
  code_url: https://github.com/neu-vi/HOI-Diff
  dataset_url: BEHAVE (annotated with text)
  category: HOI-Motion-Gen
  task_tags: [diffusion, text-conditioned, dual-branch, affordance, contact]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Dual-branch diffusion model for text-driven 3D HOI generation with cross-attention and affordance prediction.
  why_it_matters: Foundational text-to-HOI baseline with public code; widely benchmarked on BEHAVE/OMOMO.

- title: CHOIS: Controllable Human-Object Interaction Synthesis
  authors: Jiaman Li, Alexander Clegg, Roozbeh Mottaghi, Jiajun Wu, Xavier Puig, C. Karen Liu
  year: 2024
  venue: ECCV 2024 (Oral)
  arxiv_id: 2312.03913
  paper_url: https://arxiv.org/abs/2312.03913
  project_url: https://lijiaman.github.io/projects/chois/
  code_url: https://github.com/lijiaman/chois_release
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, language-conditioned, waypoints, contact, planning]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Conditional diffusion that generates joint human-object motion from text and sparse object waypoints.
  why_it_matters: Bridges high-level path planning with HOI synthesis; oral at ECCV 2024.

- title: OMOMO: Object Motion Guided Human Motion Synthesis
  authors: Jiaman Li, Jiajun Wu, C. Karen Liu
  year: 2023
  venue: SIGGRAPH Asia 2023 (TOG)
  arxiv_id: 2309.16237
  paper_url: https://arxiv.org/abs/2309.16237
  project_url: https://lijiaman.github.io/projects/omomo/
  code_url: https://github.com/lijiaman/omomo_release
  dataset_url: OMOMO dataset (in repo)
  category: Object-Aware-Motion
  task_tags: [diffusion, object-conditioned, manipulation, hand-contact]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Two-stage conditional diffusion that generates full-body manipulation motion from object trajectory.
  why_it_matters: Standard benchmark dataset and method; predicts hands first, then full body conditioned on hands.

- title: InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation
  authors: Sirui Xu, Dongting Li, Yucheng Zhang, Xiyan Xu, Haoxiu Du, Yilun Du, Liang-Yan Gui, Yu-Xiong Wang
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2509.09555
  paper_url: https://arxiv.org/abs/2509.09555
  project_url: https://sirui-xu.github.io/InterAct/
  code_url: https://github.com/wzyabcas/InterAct
  dataset_url: InterAct (21.81h consolidated, expanded to 30.70h)
  category: HOI-Motion-Gen
  task_tags: [benchmark, diffusion, multi-task, dataset]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Large-scale unified HOI benchmark consolidating six tasks with a multi-task generative model.
  why_it_matters: Most comprehensive HOI benchmark to date; standardizes evaluation across tasks.

- title: TRUMANS: Scaling Up Dynamic Human-Scene Interaction Modeling
  authors: Nan Jiang, Zhiyuan Zhang, Hongjie Li, Xiaoxuan Ma, Zan Wang, Yixin Chen, Tengyu Liu, Yixin Zhu, Siyuan Huang
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2403.08629
  paper_url: https://arxiv.org/abs/2403.08629
  project_url: https://jnnan.github.io/trumans/
  code_url: https://github.com/jnnan/trumans_utils
  dataset_url: TRUMANS (15h, 100 scenes)
  category: Object-Aware-Motion
  task_tags: [diffusion, autoregressive, scene, dataset, mocap]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Largest mocap HSI dataset and diffusion-based autoregressive HSI synthesis.
  why_it_matters: Standard benchmark for scene-aware human motion; carefully aligned with scene geometry.

- title: CIRCLE: Capture in Rich Contextual Environments
  authors: Joao Pedro Araujo, Jiaman Li, Karthik Vetrivel, Rishi Agarwal, Deepak Gopinath, Jiajun Wu, Alexander Clegg, C. Karen Liu
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2303.17912
  paper_url: https://arxiv.org/abs/2303.17912
  project_url: https://stanford-tml.github.io/circle_dataset/
  code_url: https://github.com/Stanford-TML/circle_dataset
  dataset_url: CIRCLE
  category: Object-Aware-Motion
  task_tags: [reaching, scene, dataset, mocap, transformer]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: VR-captured reaching motions in cluttered scenes with scene-aware refinement.
  why_it_matters: Established benchmark for scene-conditioned reaching/avoidance.

- title: COUCH: Towards Controllable Human-Chair Interactions
  authors: Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Vladimir Guzov, Gerard Pons-Moll
  year: 2022
  venue: ECCV 2022
  arxiv_id: 2205.00541
  paper_url: https://arxiv.org/abs/2205.00541
  project_url: https://virtualhumans.mpi-inf.mpg.de/couch/
  code_url: https://github.com/xiaohangzhan/couch
  dataset_url: COUCH dataset
  category: Object-Aware-Motion
  task_tags: [chair, contact, control, dataset]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Controllable contact-driven human-chair interaction synthesis with hand-contact specification.
  why_it_matters: Early controllable HOI baseline focused on chair sitting with explicit contacts.

- title: SAMP: Stochastic Scene-Aware Motion Prediction
  authors: Mohamed Hassan, Duygu Ceylan, Ruben Villegas, Jun Saito, Jimei Yang, Yi Zhou, Michael J. Black
  year: 2021
  venue: ICCV 2021
  arxiv_id: 2108.08284
  paper_url: https://arxiv.org/abs/2108.08284
  project_url: https://samp.is.tue.mpg.de/
  code_url: https://github.com/mohamedhassanmus/SAMP
  dataset_url: SAMP mocap (100 min)
  category: Object-Aware-Motion
  task_tags: [cVAE, scene, sitting, walking, dataset]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: cVAE-based scene-aware motion prediction with goal location and path planning.
  why_it_matters: One of the earliest scene-aware motion baselines used widely as comparison.

- title: HIMO: A New Benchmark for Full-Body Human Interacting with Multiple Objects
  authors: Xintao Lv, Liang Xu, Yichao Yan, Xin Jin, Congsheng Xu, Shuwen Wu, Yifan Liu, Lincheng Li, Mengxiao Bi, Wenjun Zeng, Xiaokang Yang
  year: 2024
  venue: ECCV 2024
  arxiv_id: 2407.12371
  paper_url: https://arxiv.org/abs/2407.12371
  project_url: https://lvxintao.github.io/himo/
  code_url: https://github.com/LvXinTao/HIMO_dataset
  dataset_url: HIMO (3.3K seqs, 4.08M frames)
  category: HOI-Motion-Gen
  task_tags: [multi-object, dataset, fine-grained, text-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Large-scale mocap dataset for full-body interactions with multiple objects, text-conditioned synthesis.
  why_it_matters: Pushes HOI from single-object to multi-object; fine-grained timeline control.

- title: OakInk2: A Dataset of Bimanual Hands-Object Manipulation in Complex Task Completion
  authors: Xinyu Zhan, Lixin Yang, Yifei Zhao, Kangrui Mao, Hanlin Xu, Zenan Lin, Kailin Li, Cewu Lu
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2403.19417
  paper_url: https://arxiv.org/abs/2403.19417
  project_url: https://oakink.net/v2/
  code_url: https://github.com/oakink/OakInk2
  dataset_url: OakInk2
  category: HOI-Motion-Gen
  task_tags: [bimanual, dataset, task-completion, hand-object]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Bimanual hand-object manipulation dataset for complex multi-step tasks.
  why_it_matters: Key benchmark for dexterous bimanual HOI; covers complete task sequences.

- title: GRAB: A Dataset of Whole-Body Human Grasping of Objects
  authors: Omid Taheri, Nima Ghorbani, Michael J. Black, Dimitrios Tzionas
  year: 2020
  venue: ECCV 2020
  arxiv_id: 2008.11200
  paper_url: https://arxiv.org/abs/2008.11200
  project_url: https://grab.is.tue.mpg.de/
  code_url: https://github.com/otaheri/GRAB
  dataset_url: GRAB (10 subjects, 51 objects)
  category: Object-Aware-Motion
  task_tags: [grasping, SMPL-X, dataset, mocap]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Whole-body grasping mocap dataset using SMPL-X with detailed contacts.
  why_it_matters: Foundational dataset for grasping motion synthesis; basis for GOAL/SAGA/GRIP.

- title: BEHAVE: Dataset and Method for Tracking Human Object Interactions
  authors: Bharat Lal Bhatnagar, Xianghui Xie, Ilya A. Petrov, Cristian Sminchisescu, Christian Theobalt, Gerard Pons-Moll
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2204.06950
  paper_url: https://arxiv.org/abs/2204.06950
  project_url: https://virtualhumans.mpi-inf.mpg.de/behave/
  code_url: https://github.com/xiexh20/behave-dataset
  dataset_url: BEHAVE
  category: HOI-Motion-Gen
  task_tags: [dataset, tracking, multi-view-RGBD]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Multi-view RGB-D dataset of body-object interactions with 3D meshes.
  why_it_matters: Most cited dataset for body-object interaction; basis for HOI-Diff/CG-HOI/InterDiff.

- title: IMoS: Intent-Driven Full-Body Motion Synthesis for Human-Object Interactions
  authors: Anindita Ghosh, Rishabh Dabral, Vladislav Golyanik, Christian Theobalt, Philipp Slusallek
  year: 2023
  venue: Eurographics 2023
  arxiv_id: 2212.07555
  paper_url: https://arxiv.org/abs/2212.07555
  project_url: https://vcai.mpi-inf.mpg.de/projects/IMoS/
  code_url: https://github.com/anindita127/IMoS
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [cVAE, intent, language-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Intent-driven cVAE for action+object text-to-HOI motion with arm/body decoupling.
  why_it_matters: Early text-conditioned HOI generator; decouples arm and body.

- title: NIFTY: Neural Object Interaction Fields for Guided Human Motion Synthesis
  authors: Nilesh Kulkarni, Davis Rempe, Kyle Genova, Abhijit Kundu, Justin Johnson, David Fouhey, Leonidas Guibas
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2307.07511
  paper_url: https://arxiv.org/abs/2307.07511
  project_url: https://nileshkulkarni.github.io/nifty/
  code_url: https://github.com/nileshkulkarni/nifty
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, neural-field, contact, affordance, synthetic-data]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Object-attached neural interaction field guides motion diffusion toward valid contacts.
  why_it_matters: Neural-field guidance enables few-shot HOI for new objects via synthetic pipeline.

- title: Object Pop-Up: Can we infer 3D objects and their poses from human interactions alone?
  authors: Ilya A. Petrov, Riccardo Marin, Julian Chibane, Gerard Pons-Moll
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2306.00777
  paper_url: https://arxiv.org/abs/2306.00777
  project_url: https://virtualhumans.mpi-inf.mpg.de/object_popup/
  code_url: https://github.com/ptrvilya/object-popup
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [object-inference, contact, point-cloud]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Predicts 3D object pose and shape conditioned on human interaction pose alone.
  why_it_matters: Inverse perspective on HOI: derive object from human; useful for AR/XR.

- title: InterDiff: Generating 3D Human-Object Interactions with Physics-Informed Diffusion
  authors: Sirui Xu, Zhengyuan Li, Yu-Xiong Wang, Liang-Yan Gui
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2308.16905
  paper_url: https://arxiv.org/abs/2308.16905
  project_url: https://sirui-xu.github.io/InterDiff/
  code_url: https://github.com/Sirui-Xu/InterDiff
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, prediction, physics, interaction-correction]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Physics-informed diffusion for whole-body HOI prediction with interaction correction.
  why_it_matters: Established physics-aware HOI prediction baseline; widely cited.

- title: InterCap: Joint Markerless 3D Tracking of Humans and Objects in Interaction
  authors: Yinghao Huang, Omid Taheri, Michael J. Black, Dimitrios Tzionas
  year: 2022
  venue: GCPR 2022 / IJCV 2024
  arxiv_id: 2209.12354
  paper_url: https://arxiv.org/abs/2209.12354
  project_url: https://intercap.is.tue.mpg.de/
  code_url: https://github.com/YinghaoHuang91/InterCap
  dataset_url: InterCap (10 subjects, 10 objects)
  category: HOI-Motion-Gen
  task_tags: [tracking, dataset, multi-view-RGBD, SMPL-X]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Markerless multi-view tracking and dataset of full-body HOI with SMPL-X.
  why_it_matters: Captures hands+body+object jointly; widely used companion to BEHAVE.

- title: CG-HOI: Contact-Guided 3D Human-Object Interaction Generation
  authors: Christian Diller, Angela Dai
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2311.16097
  paper_url: https://arxiv.org/abs/2311.16097
  project_url: https://www.christian-diller.de/projects/cg-hoi/
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, contact-guided, text-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Joint diffusion of human, object, and contact with cross-attention; contacts guide inference.
  why_it_matters: Influential contact-as-guidance framing for text-driven HOI.

- title: HOIAnimator: Generating Text-prompt Human-object Animations using Novel Perceptive Diffusion Models
  authors: Weilin Wan, Yiming Huang, Shutong Wu, Taku Komura, Wenping Wang, Dinesh Jayaraman, Lingjie Liu
  year: 2024
  venue: CVPR 2024
  arxiv_id: null
  paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Song_HOIAnimator_Generating_Text-prompt_Human-object_Animations_using_Novel_Perceptive_Diffusion_Models_CVPR_2024_paper.pdf
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, text-conditioned, perceptive-message-passing]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Dual perceptive diffusion with cross-modality message passing and Interaction Contact Field.
  why_it_matters: Strong CVPR 2024 baseline showing benefit of perceptive cross-talk between branches.

- title: Move as You Say, Interact as You Can (AffordMotion)
  authors: Zan Wang, Yixin Chen, Baoxiong Jia, Puhao Li, Jinlu Zhang, Jingze Zhang, Tengyu Liu, Yixin Zhu, Wei Liang, Siyuan Huang
  year: 2024
  venue: CVPR 2024 (Highlight)
  arxiv_id: 2403.18036
  paper_url: https://arxiv.org/abs/2403.18036
  project_url: https://afford-motion.github.io/
  code_url: https://github.com/afford-motion/afford-motion
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [affordance, diffusion, language-conditioned, scene]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Scene affordance map as intermediate; cascaded ADM (affordance) + AMDM (motion) diffusion.
  why_it_matters: Strong scene-aware text-to-motion baseline on HUMANISE/HumanML3D.

- title: HUMANISE: Language-conditioned Human Motion Generation in 3D Scenes
  authors: Zan Wang, Yixin Chen, Tengyu Liu, Yixin Zhu, Wei Liang, Siyuan Huang
  year: 2022
  venue: NeurIPS 2022
  arxiv_id: 2210.09729
  paper_url: https://arxiv.org/abs/2210.09729
  project_url: https://silvester.wang/HUMANISE/
  code_url: https://github.com/Silverster98/HUMANISE
  dataset_url: HUMANISE (synthetic)
  category: Object-Aware-Motion
  task_tags: [scene, language-conditioned, cVAE, dataset]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Aligns mocap with scanned scenes to create large language-conditioned scene-motion dataset.
  why_it_matters: Standard benchmark for language+scene-conditioned motion; widely compared.

- title: SceneDiffuser: Diffusion-based Generation, Optimization, and Planning in 3D Scenes
  authors: Siyuan Huang, Zan Wang, Puhao Li, Baoxiong Jia, Tengyu Liu, Yixin Zhu, Wei Liang, Song-Chun Zhu
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2301.06015
  paper_url: https://arxiv.org/abs/2301.06015
  project_url: https://scenediffuser.github.io/
  code_url: https://github.com/scenediffuser/Scene-Diffuser
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [diffusion, scene, planning, dexterous-grasp]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Unified diffusion for scene-conditioned generation, optimization, and planning.
  why_it_matters: Generic backbone covering motion, grasps, and planning in 3D scenes.

- title: SAGA: Stochastic Whole-Body Grasping with Contact
  authors: Yan Wu, Jiahao Wang, Yan Zhang, Siwei Zhang, Otmar Hilliges, Fisher Yu, Siyu Tang
  year: 2022
  venue: ECCV 2022
  arxiv_id: 2112.10103
  paper_url: https://arxiv.org/abs/2112.10103
  project_url: https://jiahaoplus.github.io/SAGA/saga.html
  code_url: https://github.com/JiahaoPlus/SAGA
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [grasping, contact, infilling, cVAE]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Stochastic whole-body grasping pose generation with motion infilling.
  why_it_matters: Standard whole-body grasping baseline trained on GRAB.

- title: GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping
  authors: Omid Taheri, Vasileios Choutas, Michael J. Black, Dimitrios Tzionas
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2112.11454
  paper_url: https://arxiv.org/abs/2112.11454
  project_url: https://goal.is.tue.mpg.de/
  code_url: https://github.com/otaheri/GOAL
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [grasping, autoregressive, VAE, motion-infilling]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: VAE + autoregressive infilling for 4D full-body grasping motion.
  why_it_matters: Pioneering full-body grasping motion baseline.

- title: GRIP: Generating Interaction Poses Using Spatial Cues and Latent Consistency
  authors: Omid Taheri, Yi Zhou, Dimitrios Tzionas, Yang Zhou, Duygu Ceylan, Soren Pirk, Michael J. Black
  year: 2024
  venue: 3DV 2024
  arxiv_id: 2308.11617
  paper_url: https://arxiv.org/abs/2308.11617
  project_url: https://grip.is.tue.mpg.de/
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [hand-object, latent-consistency, spatial-cues]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Upgrades noisy body+object motion with realistic before/during/after hand interactions.
  why_it_matters: Generalizes to unseen objects across mocap datasets.

- title: ManipNet: Neural Manipulation Synthesis with a Hand-Object Spatial Representation
  authors: He Zhang, Yuting Ye, Takaaki Shiratori, Taku Komura
  year: 2021
  venue: SIGGRAPH 2021 (TOG)
  arxiv_id: null
  paper_url: https://dl.acm.org/doi/10.1145/3450626.3459830
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [hand-object, spatial-representation, dexterous]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Spatial-representation neural manipulation synthesis for dexterous hand-object motion.
  why_it_matters: Influential pre-diffusion baseline for hand manipulation.

- title: ContactGen: Generative Contact Modeling for Grasp Generation
  authors: Shaowei Liu, Yang Zhou, Jimei Yang, Saurabh Gupta, Shenlong Wang
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2310.03740
  paper_url: https://arxiv.org/abs/2310.03740
  project_url: https://stevenlsw.github.io/contactgen/
  code_url: https://github.com/stevenlsw/contactgen
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [contact, grasping, hierarchical-CVAE]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Object-centric contact representation (contact, part, direction maps) with hierarchical CVAE.
  why_it_matters: Key contact-modeling primitive used by downstream HOI methods.

- title: DECO: Dense Estimation of 3D Human-Scene Contact In The Wild
  authors: Shashank Tripathi, Agniv Chatterjee, Jean-Claude Passy, Hongwei Yi, Dimitrios Tzionas, Michael J. Black
  year: 2023
  venue: ICCV 2023
  arxiv_id: 2309.15273
  paper_url: https://arxiv.org/abs/2309.15273
  project_url: https://deco.is.tue.mpg.de/
  code_url: https://github.com/sha2nkt/deco
  dataset_url: DAMON
  category: Object-Aware-Motion
  task_tags: [contact, dense, perception]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Estimates dense vertex-level body-scene contacts from in-the-wild RGB.
  why_it_matters: Provides contact estimates that downstream HOI generators rely on.

- title: FORCE: Physics-aware Human-Object Interaction
  authors: Xiaohan Zhang, Bharat Lal Bhatnagar, Sebastian Starke, Ilya Petrov, Vladimir Guzov, Helisa Dhamo, Eduardo Pérez-Pellitero, Gerard Pons-Moll
  year: 2025
  venue: 3DV 2025
  arxiv_id: 2403.11237
  paper_url: https://arxiv.org/abs/2403.11237
  project_url: https://virtualhumans.mpi-inf.mpg.de/force/
  code_url: https://github.com/xz6014/FORCE_dataset
  dataset_url: FORCE (450 sequences)
  category: HOI-Motion-Gen
  task_tags: [physics, force, resistance, dataset]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 📦 Dataset
  one_line: Models physical force/resistance interplay for nuanced HOI like push/pull/carry.
  why_it_matters: Brings intuitive physics into HOI motion synthesis with a dedicated dataset.

- title: HOI-M3: Capture Multiple Humans and Objects Interaction within Contextual Environment
  authors: Juze Zhang, Jingyan Zhang, Zining Song, Zhanhe Shi, Chengfeng Zhao, Ye Shi, Jingyi Yu, Lan Xu, Jingya Wang
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2404.00299
  paper_url: https://arxiv.org/abs/2404.00299
  project_url: https://juzezhang.github.io/HOIM3_ProjectPage/
  code_url: null
  dataset_url: HOI-M3
  category: HOI-Motion-Gen
  task_tags: [multi-human, multi-object, dataset, mocap]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: First real-world 3D mocap dataset of multiple humans and multiple objects interacting.
  why_it_matters: Scales HOI to multi-agent settings; 181M frames, 42 cameras.

- title: ParaHome: Parameterizing Everyday Home Activities Towards 3D Generative Modeling of HOIs
  authors: Jeonghwan Kim, Jisoo Kim, Jeonghyeon Na, Hanbyul Joo
  year: 2024
  venue: arXiv 2024.01
  arxiv_id: 2401.10232
  paper_url: https://arxiv.org/abs/2401.10232
  project_url: https://jlogkim.github.io/parahome/
  code_url: https://github.com/snuvclab/ParaHome
  dataset_url: ParaHome
  category: HOI-Motion-Gen
  task_tags: [home, multi-object, dataset, hand-body-object]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Parameterized home activities dataset capturing 3D body, hand, and object motion together.
  why_it_matters: Realistic multi-object home setting with concurrent object usage.

- title: CORE4D: A 4D Human-Object-Human Interaction Dataset for Collaborative Object REarrangement
  authors: Yun Liu, Chengwen Zhang, Ruofan Xing, Bingda Tang, Bowen Yang, Li Yi
  year: 2024
  venue: arXiv 2024.06 / CVPR 2025 (extended)
  arxiv_id: 2406.19353
  paper_url: https://arxiv.org/abs/2406.19353
  project_url: https://core4d.github.io/
  code_url: https://github.com/leolyliu/CORE4D-Instructions
  dataset_url: CORE4D (1K real + 11K retargeted)
  category: HOI-Motion-Gen
  task_tags: [collaboration, multi-human, dataset, retargeting]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Two-human collaborative object rearrangement mocap dataset with retargeting augmentation.
  why_it_matters: Enables collaborative HOI synthesis; benchmarks forecasting and synthesis.

- title: PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction
  authors: Yinhuai Wang, Jing Lin, Ailing Zeng, Zhengyi Luo, Jian Zhang, Lei Zhang
  year: 2023
  venue: arXiv 2023.12
  arxiv_id: 2312.04393
  paper_url: https://arxiv.org/abs/2312.04393
  project_url: https://wyhuai.github.io/physhoi-page/
  code_url: https://github.com/wyhuai/PhysHOI
  dataset_url: BallPlay
  category: HOI-Motion-Gen
  task_tags: [physics, RL, contact-graph, basketball]
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Physics-based HOI imitation with explicit contact-graph reward; no task-specific reward design.
  why_it_matters: First whole-body physics HOI imitation framework; useful for humanoid control.

- title: UniHSI: Unified Human-Scene Interaction via Prompted Chain-of-Contacts
  authors: Zeqi Xiao, Tai Wang, Jingbo Wang, Jinkun Cao, Wenwei Zhang, Bo Dai, Dahua Lin, Jiangmiao Pang
  year: 2024
  venue: ICLR 2024
  arxiv_id: 2309.07918
  paper_url: https://arxiv.org/abs/2309.07918
  project_url: https://xizaoqu.github.io/unihsi/
  code_url: https://github.com/OpenRobotLab/UniHSI
  dataset_url: ScenePlan
  category: Object-Aware-Motion
  task_tags: [physics, RL, LLM, scene, language]
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: LLM planner emits Chain-of-Contacts; unified controller executes physics-based HSI.
  why_it_matters: Bridges language commands and physics-based HSI control.

- title: TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization
  authors: Liang Pan, Zeshi Yang, Zhiyang Dou, Wenjia Wang, Buzhen Huang, Bo Dai, Taku Komura, Jingbo Wang
  year: 2025
  venue: CVPR 2025 (Oral)
  arxiv_id: 2503.19901
  paper_url: https://arxiv.org/abs/2503.19901
  project_url: https://liangpan99.github.io/TokenHSI/
  code_url: https://github.com/liangpan99/TokenHSI
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [physics, transformer, multi-task, RL, tokenization]
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified transformer policy with proprio + task tokens for multi-skill physical HSI.
  why_it_matters: CVPR 2025 oral; demonstrates skill composition (sit while carrying).

- title: PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System
  authors: Huayi Wang, Wentao Zhang, Runyi Yu, Tao Huang, Junli Ren, Feiyu Jia, Zirui Wang, Xiaojie Niu, Xiu Li, Jiangmiao Pang
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.11072
  paper_url: https://arxiv.org/abs/2510.11072
  project_url: https://why618188.github.io/physhsi/
  code_url: https://github.com/InternRobotics/PhysHSI
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [humanoid, RL, AMP, real-world, LiDAR]
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Sim-to-real humanoid HSI system with AMP and LiDAR+camera localization for box/sit/lie.
  why_it_matters: One of the first real-world deployable humanoid HSI systems.

- title: HumanPlus: Humanoid Shadowing and Imitation from Humans
  authors: Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, Chelsea Finn
  year: 2024
  venue: CoRL 2024
  arxiv_id: 2406.10454
  paper_url: https://arxiv.org/abs/2406.10454
  project_url: https://humanoid-ai.github.io/
  code_url: https://github.com/MarkFzp/humanplus
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [humanoid, shadowing, imitation, RL, real-world]
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Real-time RGB shadowing of humanoid from human + imitation learning of HOI tasks.
  why_it_matters: Connects HOI motion priors to real humanoid hardware via shadowing.

- title: AvatarGO: Zero-shot 4D Human-Object Interaction Generation and Animation
  authors: Yukang Cao, Liang Pan, Kai Han, Kwan-Yee K. Wong, Ziwei Liu
  year: 2025
  venue: ICLR 2025
  arxiv_id: 2410.07164
  paper_url: https://arxiv.org/abs/2410.07164
  project_url: https://yukangcao.github.io/AvatarGO/
  code_url: https://github.com/yukangcao/AvatarGO
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [zero-shot, 4D, text-driven, SDS, LLM]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Zero-shot 4D HOI scenes from text via LLM-guided contact retargeting and SDS.
  why_it_matters: Enables animatable 4D HOI without paired data via diffusion priors.

- title: MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations
  authors: Heyuan Yao, Zhenhua Song, Baoquan Chen, Libin Liu
  year: 2024
  venue: SIGGRAPH 2024 (TOG)
  arxiv_id: 2310.10198
  paper_url: https://arxiv.org/abs/2310.10198
  project_url: https://moconvq.github.io/
  code_url: https://github.com/heyuanYao-pku/MoConVQ
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [physics, VQ-VAE, RL, LLM, control]
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: VQ-VAE motion embedding for unified physics-based control + LLM in-context generation.
  why_it_matters: Unified motion-control backbone applicable to HOI tasks.

- title: InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction
  authors: Sirui Xu, Ziyin Wang, Yu-Xiong Wang, Liang-Yan Gui
  year: 2024
  venue: NeurIPS 2024
  arxiv_id: 2403.19652
  paper_url: https://arxiv.org/abs/2403.19652
  project_url: https://sirui-xu.github.io/InterDreamer/
  code_url: https://github.com/Sirui-Xu/InterDreamer
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [zero-shot, LLM, world-model, decoupled-semantics-dynamics]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Zero-shot text-to-HOI via LLM planning + text-to-motion + learned world model.
  why_it_matters: Decouples semantics and dynamics; reduces reliance on paired text-HOI data.

- title: SyncDiff: Synchronized Motion Diffusion for Multi-Body HOI Synthesis
  authors: Wenkun He, Yun Liu, Ruitao Liu, Li Yi
  year: 2025
  venue: ICCV 2025
  arxiv_id: 2412.20104
  paper_url: https://arxiv.org/abs/2412.20104
  project_url: https://syncdiff.github.io/
  code_url: https://github.com/WenkunHe/SyncDiff
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, multi-body, synchronization, frequency-decomposition]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Single diffusion captures joint multi-body distribution with explicit synchronization.
  why_it_matters: Generalizes HOI to arbitrary numbers of humans/hands/objects.

- title: HOIDiNi: Human-Object Interaction through Diffusion Noise Optimization
  authors: Roey Ron, Guy Tevet, Haim Sawdayee, Amit H. Bermano
  year: 2025
  venue: arXiv 2025.06
  arxiv_id: 2506.15625
  paper_url: https://arxiv.org/abs/2506.15625
  project_url: https://hoidini.github.io/
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, noise-optimization, test-time, contact]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Test-time diffusion noise optimization for HOI satisfying tight contact constraints.
  why_it_matters: Operates on the manifold of a pretrained motion diffusion; no retraining.

- title: ChainHOI: Joint-based Kinematic Chain Modeling for HOI Generation
  authors: Ling-An Zeng, Guohong Huang, Yi-Lin Wei, Shengbo Gu, Yu-Ming Tang, Jingke Meng, Wei-Shi Zheng
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2503.13130
  paper_url: https://arxiv.org/abs/2503.13130
  project_url: null
  code_url: https://github.com/qingtian5/ChainHOI
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, kinematic-chain, GCN, text-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Models HOI at joint and kinematic-chain levels with spatiotemporal GCN.
  why_it_matters: Brings biomechanical structure into HOI diffusion; SOTA on BEHAVE/OMOMO.

- title: ROG: Guiding Human-Object Interactions with Rich Geometry and Relations
  authors: Mengqing Xue, Yifei Liu, Ling Guo, Shaoli Huang, Changxing Ding, Mingyuan Zhang
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2503.20118
  paper_url: https://arxiv.org/abs/2503.20118
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, geometry, IDF, text-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Diffusion with boundary keypoints and Interactive Distance Field for richer HOI dynamics.
  why_it_matters: Geometry-aware object representation improves text-driven HOI realism.

- title: Auto-Regressive Diffusion for Generating 3D HOIs (ARDHOI)
  authors: Zichen Geng, Zeeshan Hayder, Wei Liu, Ajmal Saeed Mian
  year: 2025
  venue: AAAI 2025
  arxiv_id: 2503.16801
  paper_url: https://arxiv.org/abs/2503.16801
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [autoregressive, diffusion, mamba, cVAE]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Continuous-token autoregressive diffusion with Mamba context encoder for long HOI sequences.
  why_it_matters: Addresses long-horizon HOI consistency; outperforms on OMOMO/BEHAVE.

- title: HOI-Dyn: Learning Interaction Dynamics for Human-Object Motion Diffusion
  authors: Lin Wu, Zhixiang Chen, Jianglin Lan
  year: 2025
  venue: arXiv 2025.07
  arxiv_id: 2507.01737
  paper_url: https://arxiv.org/abs/2507.01737
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, dynamics, residual-loss, transformer]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Lightweight transformer dynamics predicts object reaction; residual dynamics loss.
  why_it_matters: Explicit object-reaction modeling reduces physics violations.

- title: LatentHOI: On the Generalizable Hand Object Motion Generation with Latent Hand Diffusion
  authors: Yifei Li, Sammy Christen, Christoph Gebhardt, Jie Song, Otmar Hilliges
  year: 2025
  venue: CVPR 2025
  arxiv_id: null
  paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_LatentHOI_On_the_Generalizable_Hand_Object_Motion_Generation_with_Latent_CVPR_2025_paper.pdf
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [latent-diffusion, GraspVAE, generalization, hand-object]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Decouples temporal motion from fine-grained spatial hand-object via latent diffusion + GraspVAE.
  why_it_matters: Generalizes hand-object interaction to unseen objects.

- title: DiffH2O: Diffusion-Based Synthesis of Hand-Object Interactions from Textual Descriptions
  authors: Sammy Christen, Shreyas Hampali, Fadime Sener, Edoardo Remelli, Tomas Hodan, Eric Sauser, Shugao Ma, Bugra Tekin
  year: 2024
  venue: SIGGRAPH Asia 2024
  arxiv_id: 2403.17827
  paper_url: https://arxiv.org/abs/2403.17827
  project_url: https://diffh2o.github.io/
  code_url: https://github.com/facebookresearch/diffh2o
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, hand-object, text-conditioned, two-stage]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Two-stage hand-object diffusion (grasp + manipulation) from text with object geometry.
  why_it_matters: Generalizes to unseen objects with fine-grained text control.

- title: Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction
  authors: Junuk Cha, Jihyeon Kim, Jae Shin Yoon, Seungryul Baek
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2404.00562
  paper_url: https://arxiv.org/abs/2404.00562
  project_url: null
  code_url: https://github.com/JunukCha/Text2HOI
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [hand-object, text-conditioned, motion-generation]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Text-guided generation of 3D hand-object motion using contact-aware modeling.
  why_it_matters: Direct text-to-hand-object pipeline used as benchmark in DiffH2O/LatentHOI.

- title: DiffGrasp: Whole-Body Grasping Synthesis Guided by Object Motion Using a Diffusion Model
  authors: Yonghao Zhang, Qiang He, Yanguang Wan, Yinda Zhang, Xiaoming Deng, Cuixia Ma, Hongan Wang
  year: 2025
  venue: AAAI 2025
  arxiv_id: 2412.20657
  paper_url: https://arxiv.org/abs/2412.20657
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [diffusion, whole-body-grasp, contact, two-hand]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Whole-body grasping diffusion conditioned on object motion with contact-aware losses.
  why_it_matters: Joint body+hands grasping diffusion with stability guidance.

- title: GraspXL: Generating Grasping Motions for Diverse Objects at Scale
  authors: Hui Zhang, Sammy Christen, Zicong Fan, Otmar Hilliges, Jie Song
  year: 2024
  venue: ECCV 2024
  arxiv_id: 2403.19649
  paper_url: https://arxiv.org/abs/2403.19649
  project_url: https://eth-ait.github.io/graspxl/
  code_url: https://github.com/zdchan/graspxl
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [RL, grasping, dexterous, diverse-morphologies]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Unified RL policy for grasping motions across diverse hand morphologies and objects.
  why_it_matters: Scale and morphology generalization without paired HOI data.

- title: ARCTIC: A Dataset for Dexterous Bimanual Hand-Object Manipulation
  authors: Zicong Fan, Omid Taheri, Dimitrios Tzionas, Muhammed Kocabas, Manuel Kaufmann, Michael J. Black, Otmar Hilliges
  year: 2023
  venue: CVPR 2023
  arxiv_id: 2204.13662
  paper_url: https://arxiv.org/abs/2204.13662
  project_url: https://arctic.is.tue.mpg.de/
  code_url: https://github.com/zc-alexfan/arctic
  dataset_url: ARCTIC
  category: HOI-Motion-Gen
  task_tags: [dataset, bimanual, articulated, dynamic-contact]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: 2.1M frames of bi-manual articulated object manipulation with dense contact.
  why_it_matters: Premier benchmark for dexterous bimanual HOI.

- title: HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction
  authors: Yunze Liu, Yun Liu, Che Jiang, Kangbo Lyu, Weikang Wan, Hao Shen, Boqiang Liang, Zhoujie Fu, He Wang, Li Yi
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2203.01577
  paper_url: https://arxiv.org/abs/2203.01577
  project_url: https://hoi4d.github.io/
  code_url: https://github.com/leolyliu/HOI4D-Instructions
  dataset_url: HOI4D (2.4M frames)
  category: HOI-Motion-Gen
  task_tags: [dataset, egocentric, 4D, category-level]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Large 4D egocentric dataset for category-level HOI segmentation/tracking/action.
  why_it_matters: Foundational egocentric HOI benchmark.

- title: EgoChoir: Capturing 3D Human-Object Interaction Regions from Egocentric Views
  authors: Yuhang Yang, Wei Zhai, Chengfeng Wang, Chengjun Yu, Yang Cao, Zheng-Jun Zha
  year: 2024
  venue: NeurIPS 2024
  arxiv_id: 2405.13659
  paper_url: https://arxiv.org/abs/2405.13659
  project_url: https://yyvhang.github.io/EgoChoir/
  code_url: https://github.com/yyvhang/EgoChoir_release
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [egocentric, affordance, contact, perception]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Predicts 3D affordance and human contact regions from egocentric video.
  why_it_matters: Bridges egocentric perception and HOI region understanding.

- title: HOIMotion: Forecasting Human Motion During HOIs Using Egocentric 3D Object Bounding Boxes
  authors: Zhiming Hu, Zheming Yin, Daniel Häufle, Syn Schmitt, Andreas Bulling
  year: 2024
  venue: ISMAR 2024
  arxiv_id: 2407.00270
  paper_url: https://arxiv.org/abs/2407.00270
  project_url: null
  code_url: https://github.com/zhiminghu/HOIMotion
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [egocentric, forecasting, bounding-box]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Forecasts body motion conditioned on egocentric 3D object bounding boxes.
  why_it_matters: Practical AR/VR motion forecasting from egocentric object cues.

- title: I'M HOI: Inertia-aware Monocular Capture of 3D Human-Object Interactions
  authors: Chengfeng Zhao, Juze Zhang, Jiashen Du, Ziwei Shan, Junye Wang, Jingyi Yu, Jingya Wang, Lan Xu
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2312.08869
  paper_url: https://arxiv.org/abs/2312.08869
  project_url: null
  code_url: https://github.com/AfterJourney00/IMHD-Dataset
  dataset_url: IMHD2
  category: HOI-Motion-Gen
  task_tags: [monocular, IMU, dataset, capture]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Monocular HOI capture using inertia (IMU) cues; new IMHD2 dataset.
  why_it_matters: Bridges capture and synthesis with inertia-aware data.

- title: HUMOTO: A 4D Dataset of Mocap Human Object Interactions
  authors: Jiaxin Lu, Hsin-Ying Lee, Chia-Yu Chen, Stylianos Moschoglou, Yannis Panagakis, others
  year: 2025
  venue: ICCV 2025
  arxiv_id: 2504.10414
  paper_url: https://arxiv.org/abs/2504.10414
  project_url: https://jiaxin-lu.github.io/humoto/
  code_url: null
  dataset_url: HUMOTO (736 sequences)
  category: HOI-Motion-Gen
  task_tags: [dataset, mocap, LLM-scripting, daily-tasks]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: 4D HOI mocap dataset with LLM-scripted scene-driven tasks across diverse daily activities.
  why_it_matters: Curated, artist-cleaned HOI sequences with new evaluation metrics.

- title: HOI-PAGE: Zero-Shot HOI Generation with Part Affordance Guidance
  authors: Lei Li, Angela Dai
  year: 2025
  venue: arXiv 2025.06
  arxiv_id: 2506.07209
  paper_url: https://arxiv.org/abs/2506.07209
  project_url: https://hoipage.github.io/
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [zero-shot, 4D, LLM, part-affordance]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Part Affordance Graphs from LLMs guide zero-shot 4D HOI synthesis from text.
  why_it_matters: Multi-object, multi-person zero-shot HOI; flexible composition.

- title: InteractAnything: Zero-shot HOI Synthesis via LLM Feedback and Object Affordance Parsing
  authors: Jinlu Zhang, Yixin Chen, Zan Wang, Jie Yang, Yizhou Wang, Siyuan Huang
  year: 2025
  venue: CVPR 2025
  arxiv_id: 2505.24315
  paper_url: https://arxiv.org/abs/2505.24315
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [zero-shot, LLM-feedback, affordance, open-set]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Open-set 3D HOI synthesis using LLM feedback for relations and 2D diffusion for contacts.
  why_it_matters: Generates novel interactions with arbitrary text+mesh; no training on HOI data.

- title: InterPose: Learning to Generate HOIs from Large-Scale Web Videos
  authors: (anonymized)
  year: 2025
  venue: arXiv 2025.09
  arxiv_id: 2509.00767
  paper_url: https://arxiv.org/abs/2509.00767
  project_url: null
  code_url: null
  dataset_url: InterPose (73.8K seqs from 45.8K videos)
  category: HOI-Motion-Gen
  task_tags: [dataset, web-videos, LLM-agent, zero-shot]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Web-video pipeline producing 73.8K HOI sequences; LLM agent enables zero-shot animation.
  why_it_matters: Largest in-the-wild HOI motion dataset extracted from internet videos.

- title: AnchorHOI: Zero-shot Generation of 4D HOI via Anchor-based Prior Distillation
  authors: (see paper)
  year: 2026
  venue: AAAI 2026
  arxiv_id: 2512.14095
  paper_url: https://arxiv.org/abs/2512.14095
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [zero-shot, 4D, video-diffusion, NeRF, keypoint]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Anchor NeRFs + anchor keypoints distill image and video diffusion priors for 4D HOI.
  why_it_matters: Combines image and video priors for higher-fidelity 4D HOI.

- title: OnlineHOI: Towards Online Human-Object Interaction Generation and Perception
  authors: Yihong Lin, others
  year: 2025
  venue: ACM MM 2025
  arxiv_id: 2509.12250
  paper_url: https://arxiv.org/abs/2509.12250
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [online, mamba, memory, streaming]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Mamba-based online HOI generation and perception with memory mechanism.
  why_it_matters: Streaming setting (CORE4D, OAKINK2, HOI4D); critical for AR/VR/robotics.

- title: PA-HOI: A Physics-Aware Human and Object Interaction Dataset
  authors: (see paper)
  year: 2025
  venue: arXiv 2025.08
  arxiv_id: 2508.06205
  paper_url: https://arxiv.org/abs/2508.06205
  project_url: null
  code_url: null
  dataset_url: PA-HOI
  category: HOI-Motion-Gen
  task_tags: [dataset, physics, mass, friction]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 📦 Dataset
  one_line: Physics-aware HOI dataset with object mass/friction for realistic motion nuance.
  why_it_matters: Adds physical attributes to HOI mocap to enable physics-aware learning.

- title: SViMo: Synchronized Diffusion for Video and Motion Generation in Hand-object Scenarios
  authors: (see paper)
  year: 2025
  venue: NeurIPS 2025
  arxiv_id: 2506.02444
  paper_url: https://arxiv.org/abs/2506.02444
  project_url: https://droliven.github.io/SViMo_project/
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [video, diffusion, hand-object, joint-generation]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Joint diffusion for video and motion in hand-object interaction with synchronization.
  why_it_matters: Bridges video generation and motion synthesis for HOI.

- title: SceneMI: Motion In-betweening for Modeling Human-Scene Interactions
  authors: Inwoo Hwang, Bing Zhou, Young Min Kim, Jian Wang, Chuan Guo
  year: 2025
  venue: arXiv 2025.03
  arxiv_id: 2503.16289
  paper_url: https://arxiv.org/abs/2503.16289
  project_url: https://inwoohwang.me/SceneMI/
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [in-betweening, scene, diffusion]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Frames HSI as motion in-betweening between scene-aware keyframes.
  why_it_matters: Practical interface for editable scene-conditioned motion.

- title: Generating Human Interaction Motions in Scenes with Text Control (TeSMo)
  authors: Hongwei Yi, Justus Thies, Michael J. Black, Xue Bin Peng, Davis Rempe
  year: 2024
  venue: ECCV 2024
  arxiv_id: 2404.10685
  paper_url: https://arxiv.org/abs/2404.10685
  project_url: https://research.nvidia.com/labs/toronto-ai/tesmo/
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [diffusion, scene, text-conditioned, navigation]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Two-stage diffusion: scene-aware navigation + interaction with text control.
  why_it_matters: Long-horizon scene HOI from a single text prompt.

- title: DreamHOI: Subject-Driven Generation of 3D HOI with Diffusion Priors
  authors: Thomas Hanwen Zhu, Ruining Li, Tomas Jakab
  year: 2024
  venue: arXiv 2024.09
  arxiv_id: 2409.08278
  paper_url: https://arxiv.org/abs/2409.08278
  project_url: https://dreamhoi.github.io/
  code_url: https://github.com/hanwenzhu/dreamhoi
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [SDS, subject-driven, zero-shot, NeRF]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Score-distillation HOI generation with implicit + explicit subject-driven hybrid.
  why_it_matters: Enables custom-character HOI from a few images with text.

- title: Human-Object Interaction from Human-Level Instructions (HOI-HLI)
  authors: Zhen Wu, Jiaman Li, Pei Xu, C. Karen Liu
  year: 2024
  venue: arXiv 2024.06
  arxiv_id: 2406.17840
  paper_url: https://arxiv.org/abs/2406.17840
  project_url: https://hoifhli.github.io/
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [LLM-planning, HOI, long-horizon, scene]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: LLM decomposes high-level instructions into sub-task HOIs and waypoints feeding CHOIS.
  why_it_matters: Scales HOI from short clips to long instruction-driven sequences.

- title: HOIDiffusion: Generating Realistic 3D Hand-Object Interaction Data
  authors: Mengqi Zhang, Yang Fu, Zheng Ding, Sifei Liu, Zhuowen Tu, Xiaolong Wang
  year: 2024
  venue: CVPR 2024
  arxiv_id: 2403.12011
  paper_url: https://arxiv.org/abs/2403.12011
  project_url: https://mq-zhang1.github.io/HOIDiffusion/
  code_url: https://github.com/Mq-Zhang1/HOIDiffusion
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [diffusion, image-synthesis, hand-object, data-aug]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Diffusion image generator for realistic 3D-conditioned hand-object data augmentation.
  why_it_matters: Closes data gap by synthesizing controllable HOI training images.

- title: NL2Contact: Natural Language Guided 3D Hand-Object Contact Modeling
  authors: Zhongqun Zhang, Hengfei Wang, Ziwei Yu, Yihua Cheng, Angela Yao, Hyung Jin Chang
  year: 2024
  venue: ECCV 2024
  arxiv_id: 2407.12727
  paper_url: https://arxiv.org/abs/2407.12727
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [language, contact, hand-object, diffusion]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Language-conditioned hand-object contact modeling with stratified generation.
  why_it_matters: Adds linguistic control to fine-grained contact prediction.

- title: HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos
  authors: (see paper)
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.02473
  paper_url: https://arxiv.org/abs/2602.02473
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [humanoid, video-imitation, RL, real-world]
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: XGen synthesizes humanoid HOI data from monocular videos; XMimic learns interaction skills.
  why_it_matters: 8x higher generalization than priors for humanoid HOI from web videos.

- title: DeVI: Physics-based Dexterous HOI via Synthetic Video Imitation
  authors: (see paper)
  year: 2026
  venue: arXiv 2026.04
  arxiv_id: 2604.20841
  paper_url: https://arxiv.org/abs/2604.20841
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [humanoid, dexterous, video-imitation, sim-to-real]
  uses_real_robot: true
  uses_humanoid: true
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Hybrid 3D-human + 2D-object imitation targets train physics-based dexterous HOI policy.
  why_it_matters: Connects HOI motion priors to dexterous humanoid control.

- title: Motion-X / Motion-X++: Large-scale 3D Expressive Whole-body Motion Dataset
  authors: Jing Lin, Ailing Zeng, Shunlin Lu, Yuanhao Cai, Ruimao Zhang, Haoqian Wang, Lei Zhang
  year: 2023 / 2025
  venue: NeurIPS 2023 / arXiv 2025.01
  arxiv_id: 2307.00818
  paper_url: https://arxiv.org/abs/2307.00818
  project_url: https://motion-x-dataset.github.io/
  code_url: https://github.com/IDEA-Research/Motion-X
  dataset_url: Motion-X / Motion-X++
  category: Object-Aware-Motion
  task_tags: [dataset, whole-body, multimodal, text]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: Largest 3D expressive whole-body motion-language dataset; many HOI subsets.
  why_it_matters: Foundational for whole-body motion generation; widely used as pretraining.

- title: HumanML3D: Generating Diverse and Natural 3D Human Motions from Texts
  authors: Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, Li Cheng
  year: 2022
  venue: CVPR 2022
  arxiv_id: 2203.13270
  paper_url: https://arxiv.org/abs/2203.13270
  project_url: https://ericguo5513.github.io/text-to-motion/
  code_url: https://github.com/EricGuo5513/HumanML3D
  dataset_url: HumanML3D
  category: Object-Aware-Motion
  task_tags: [dataset, text-to-motion, foundation]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⭐ Code
  one_line: 14,616 motions / 44,970 text descriptions; standard text-to-motion benchmark.
  why_it_matters: Backbone dataset that most HOI generators rely on for motion priors.

- title: Purposer: Putting Human Motion Generation in Context
  authors: Nicolas Ugrinovic, Thomas Lucas, Fabien Baradel, Philippe Weinzaepfel, Gregory Rogez, Francesc Moreno-Noguer
  year: 2024
  venue: 3DV 2024
  arxiv_id: 2404.12942
  paper_url: https://arxiv.org/abs/2404.12942
  project_url: https://europe.naverlabs.com/research/publications/purposer-putting-human-motion-generation-in-context/
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [scene, navigation, contact, sparse-cues]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Generates motions in 3D scenes from sparse goals/keyframes/contact cues.
  why_it_matters: Unified context-aware motion generation across multiple input modalities.

- title: Multimodal priors-augmented text-driven 3D HOI generation
  authors: (Science China Information Sciences)
  year: 2025
  venue: Science China Information Sciences 2025
  arxiv_id: 2602.10659
  paper_url: https://arxiv.org/abs/2602.10659
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [multimodal, priors, text-driven, 3D]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Augments text-driven 3D HOI generation with multimodal priors.
  why_it_matters: Demonstrates value of multimodal pretrained priors in HOI synthesis.

- title: CoopDiff: Anticipating 3D HOIs via Contact-consistent Decoupled Diffusion
  authors: (see paper)
  year: 2025
  venue: arXiv 2025.08
  arxiv_id: 2508.07162
  paper_url: https://arxiv.org/abs/2508.07162
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [forecasting, diffusion, contact, decoupled]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Contact-consistent decoupled diffusion for 3D HOI anticipation.
  why_it_matters: Addresses temporal anticipation with explicit contact alignment.

- title: SceMoS: Scene-Aware 3D Human Motion Synthesis with Geometry-Grounded Tokens
  authors: (see paper)
  year: 2026
  venue: arXiv 2026.02
  arxiv_id: 2602.20476
  paper_url: https://arxiv.org/abs/2602.20476
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [scene, planning, tokenization, diffusion]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Scene-aware motion synthesis via geometry-grounded planning tokens; SOTA on TRUMANS.
  why_it_matters: Tighter scene grounding and contact accuracy than prior cVAE/diffusion baselines.

- title: SceneAdapt: Scene-Aware Adaptation of Human Motion Diffusion
  authors: (see paper)
  year: 2025
  venue: arXiv 2025.10
  arxiv_id: 2510.13044
  paper_url: https://arxiv.org/abs/2510.13044
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [adaptation, diffusion, scene, fine-tuning-free]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Adapts pretrained motion diffusion to scene-conditioned generation without retraining.
  why_it_matters: Test-time scene adaptation; reusable across motion-diffusion backbones.

- title: InterPhys: Physics-aware Human Motion Synthesis in a Dynamic Scene
  authors: (see paper)
  year: 2026
  venue: arXiv 2026.05
  arxiv_id: 2605.01036
  paper_url: https://arxiv.org/abs/2605.01036
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [physics, contact-force, diffusion, dynamic-scene]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Two-stage diffusion with differentiable contact-force model for physically consistent HSI.
  why_it_matters: Physics constraints generalize to arbitrary surfaces in cluttered dynamic scenes.

- title: UniHM: Universal Human Motion Generation with Object Interactions in Indoor Scenes
  authors: (see paper)
  year: 2025
  venue: arXiv 2025.05
  arxiv_id: 2505.12774
  paper_url: https://arxiv.org/abs/2505.12774
  project_url: null
  code_url: null
  dataset_url: null
  category: Object-Aware-Motion
  task_tags: [scene, indoor, diffusion, object-interaction]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Unified motion generation in indoor scenes with object interactions and waypoints.
  why_it_matters: Single backbone covering navigation, interaction, and manipulation indoors.

- title: Decoupled Generative Modeling for HOI Synthesis
  authors: (see paper)
  year: 2025
  venue: arXiv 2025.12
  arxiv_id: 2512.19049
  paper_url: https://arxiv.org/abs/2512.19049
  project_url: null
  code_url: null
  dataset_url: null
  category: HOI-Motion-Gen
  task_tags: [decoupled, diffusion, text-conditioned]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Decoupled generative modeling separates body, object, and contact for HOI synthesis.
  why_it_matters: Recent decomposed-design HOI synthesizer with improved generalization.

- title: MOCHI: Motion Enhancement of Collaborative Human-object Interactions
  authors: Jiye Lee; Yonghun Choi; Jungdam Won
  year: 2026
  venue: SIGGRAPH 2026 / ACM TOG
  arxiv_id: 2606.18243
  paper_url: https://arxiv.org/abs/2606.18243
  project_url: https://jiyewise.github.io/projects/MOCHI/
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [collaborative-HOI, motion-enhancement, contact, multi-human-object]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Enhances noisy collaborative multi-human object-interaction captures by improving contact alignment, hand articulation, and temporal consistency.
  why_it_matters: Supplies a clean-up stage for MHOI data that downstream HOI generators and humanoid imitation pipelines need.

- title: DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects
  authors: Tianshan Zhang; Yijia Duan; Yanjun Li; Zeyu Zhang; Hao Tang
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.15133
  paper_url: https://arxiv.org/abs/2606.15133
  project_url: https://aigeeksgroup.github.io/DragMesh-2
  code_url: https://github.com/AIGeeksGroup/DragMesh-2
  dataset_url: https://huggingface.co/datasets/AIGeeksGroup/DragMesh-2
  category: HOI-Motion-Gen
  task_tags: [dexterous-HOI, articulated-objects, physical-plausibility, hand-object-contact]
  uses_real_robot: false
  uses_humanoid: true
  uses_simulation: true
  code_status: ⭐ Code
  one_line: Generates and trains physically plausible dexterous hand-object interactions with articulated objects using contact-aware simulation assets and RL code.
  why_it_matters: Extends HOI generation toward articulated-object contact dynamics that humanoid hands must eventually execute.

- title: IMAGIN-4D: Image-Guided Controllable Interaction Generation
  authors: Sai Kumar Dwivedi; Federica Bogo; Bugra Tekin; Chenhongyi Yang; Nadine Bertsch; Tomas Hodan; Michael J. Black; Dimitrios Tzionas
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.23675
  paper_url: https://arxiv.org/abs/2606.23675
  project_url: https://imagin4d.github.io
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [image-conditioned-HOI, diffusion, contact, controllable-generation]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⏳ Code Coming Soon
  one_line: Diffusion-based HOI generator uses a reference image to specify body pose, object pose, contacts, and spatial layout for a target interaction frame.
  why_it_matters: Adds visual snapshot control to text/object/waypoint-conditioned HOI synthesis, tightening contact and layout specification for downstream imitation data.

- title: Policy-as-Data: Learning Generalizable HOI Diffusion Models from Simulated Physics
  authors: Shujia Li; Jianshu Hu; Haiyu Zhang; Yunpeng Jiang; Haoyuan Jin; Xinyuan Chen; Yaohui Wang; Yutong Ban
  year: 2026
  venue: arXiv 2026.06
  arxiv_id: 2606.22806
  paper_url: https://arxiv.org/abs/2606.22806
  project_url: ""
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [physics-simulation, diffusion, retargeting, long-horizon-HOI]
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: true
  code_status: ❌ No Code Found
  one_line: Uses task policies trained in physics simulation as a scalable data source for training generalizable HOI diffusion models.
  why_it_matters: Directly attacks the mocap scarcity bottleneck for physically plausible long-horizon HOI generation.

- title: JointHOI: Jointly Generating Contact Maps Enhances Hand Object Interaction Generation
  authors: Mingyeong Song; Jungbin Cho; Jisoo Kim; Ananya Bal; Kartik Sharma; Youngjae Yu; Laszlo A. Jeni; Junhyug Noh
  year: 2026
  venue: arXiv 2026.07
  arxiv_id: 2607.01768
  paper_url: https://arxiv.org/abs/2607.01768
  project_url: ""
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [hand-object-interaction, contact-maps, diffusion, text-to-HOI]
  robot_platform: dexterous hand-object interaction
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Single-stage text-driven diffusion model jointly generates hand-object motion and temporally evolving contact maps to reduce penetration and floating.
  why_it_matters: Improves physical contact consistency in generated HOI clips, a key prerequisite for turning hand-object motion into robot-executable references.

- title: HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis
  authors: Lingwei Dang; Juntong Li; Zonghan Li; Hongwen Zhang; Liang An; Wei Min; Yebin Liu; Qingyao Wu
  year: 2026
  venue: arXiv 2026.07
  arxiv_id: 2607.17097
  paper_url: https://arxiv.org/abs/2607.17097
  project_url: https://droliven.github.io/HarmoHOI_project/
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [hand-object-interaction, multi-view-video, 3D-point-tracks, diffusion]
  robot_platform: hand-object interaction synthesis
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ⏳ Code Coming Soon
  one_line: Joint diffusion framework synthesizes synchronized multi-view HOI videos together with globally aligned 3D point tracks.
  why_it_matters: Adds explicit multi-view geometric motion consistency to HOI generation, reducing hallucinated contact and floating artifacts that limit robot-useful video priors.

- title: PhotoHOI: Synthesizing 3D Hand-Object Interactions from a Single RGB Photograph
  authors: Zhenhao Zhang; Jiajun Zhang; Wei Min; Yebin Liu
  year: 2026
  venue: arXiv 2026.08
  arxiv_id: 2608.01905
  paper_url: https://arxiv.org/abs/2608.01905
  project_url: ""
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [photo-conditioned-HOI, open-vocabulary, contact-priors, hand-object-motion]
  robot_platform: hand-object interaction synthesis
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: ❌ No Code Found
  one_line: Synthesizes 3D hand-object interaction sequences from one RGB photograph and an open-vocabulary instruction by planning object motion and contact-conditioned hand motion.
  why_it_matters: Moves HOI generation toward natural image inputs where object geometry, support relations, and task targets must be inferred rather than pre-specified.

- title: Surface Keypoint Representation for Multi-Object and Articulated Human-Object Interaction Generation
  authors: Xiaogang Peng; Zeyu Han; Zichong Meng; Yiming Xie; Jihua Zhu; Gang Hua; Huaizu Jiang
  year: 2026
  venue: arXiv 2026.08
  arxiv_id: 2608.03158
  paper_url: https://arxiv.org/abs/2608.03158
  project_url: https://neu-vi.github.io/SK-HOI/
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [surface-keypoints, multi-object-HOI, articulated-objects, contact-distance-field]
  robot_platform: human-object interaction synthesis
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Represents object motion with surface keypoint trajectories and generates whole-body HOI for multi-object and articulated-object settings through contact-field guidance.
  why_it_matters: Extends HOI synthesis beyond single rigid objects, which is closer to household interaction tasks involving drawers, appliances, furniture, and multiple movable items.

- title: MAD-HOI: Masked Autoregressive Diffusion for Generating Articulated Hand Object Interactions from Text
  authors: Ananya Bal; Kartik Sharma; Ethan Lai; Samyak Tiwari; Liza Dahiya; Chaitanya Chawla; Laszlo A. Jeni
  year: 2026
  venue: arXiv 2026.08
  arxiv_id: 2608.10162
  paper_url: https://arxiv.org/abs/2608.10162
  project_url: https://ananyabal.github.io/MAD-HOI_supplementary_3D_visualizations/visualize_hoi_motions.html
  code_url: ""
  dataset_url: ""
  category: HOI-Motion-Gen
  task_tags: [text-to-HOI, masked-autoregression, flow-matching, articulated-objects, contact]
  robot_platform: hand-object interaction synthesis
  uses_real_robot: false
  uses_humanoid: false
  uses_simulation: false
  code_status: 🌐 Project Page
  one_line: Uses masked autoregression with a continuous diffusion/flow head to generate, complete, infill, and terminate articulated hand-object interaction sequences from text.
  why_it_matters: Adds variable-length and compositional control to text-driven HOI generation without quantizing away contact-sensitive motion details.

---

## Summary

Total papers: 60. Verified (⭐ Code) repos: ~36. Project pages with no released code (🌐): ~10. Dataset-only releases (📦): 2. Coming soon (⏳): 1. No code found (❌): ~11.

The list spans foundational datasets (GRAB 2020, BEHAVE 2022, HumanML3D 2022, HUMANISE 2022, OakInk2 2024, ParaHome 2024, HIMO 2024, HOI-M3 2024, CORE4D 2024, ARCTIC 2023, HOI4D 2022, HUMOTO 2025, FORCE 2025), seminal motion synthesis methods (SAMP 2021, ManipNet 2021, COUCH 2022, GOAL 2022, SAGA 2022, IMoS 2023, OMOMO 2023, InterDiff 2023, GRIP 2024), and the modern wave of HOI diffusion / zero-shot generators (HOI-Diff, CHOIS, CG-HOI, NIFTY, AffordMotion, HOIAnimator, Text2HOI, DiffH2O, InterDreamer, AvatarGO, SyncDiff, ChainHOI, ROG, ARDHOI, LatentHOI, DiffGrasp, HOI-PAGE, InteractAnything, AnchorHOI, HOIDiNi, OnlineHOI, SceneMI, TeSMo, DreamHOI, HOI-HLI). Physics-based / humanoid lines (PhysHOI, UniHSI, TokenHSI, MoConVQ, PhysHSI, HumanPlus, HumanX, DeVI) connect HOI motion priors to humanoid robot control. Roughly 60% of papers are 2024-2026, with strong representation at CVPR/ECCV/ICCV/NeurIPS/SIGGRAPH and top arXiv preprints. Code verification was done via GitHub URL lookups; uncertain entries downgraded to project-page or no-code-found.
