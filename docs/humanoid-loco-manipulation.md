# 人形全身移动操作精选

核查日期：2026-10-19。公开库去重后 781 篇，精选 39 篇（4.99%），其中 8 篇精读（20.51%）。

[打开精选工作台](https://memoryunreal.github.io/awesome-whole-body-control/#/focus)

## 先读这 8 篇

| 顺序 | 论文 | 核心问题 |
|---|---|---|
| 1 | [HOMIE](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2502.13013) | 如何让身体适应不断变化的上肢命令？ |
| 2 | [FALCON](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2505.06776) | 带载时，手部精度和平衡如何同时保持？ |
| 3 | [ULC](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2507.06905) | 统一全身策略的收益来自哪些训练与接口设计？ |
| 4 | [SkillBlender](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2506.09366) | 逐关节技能混合如何改变探索和接触行为？ |
| 5 | [VIRAL](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2511.15200) | 特权教师如何变成真实 RGB 闭环策略？ |
| 6 | [WholeBodyVLA](https://memoryunreal.github.io/awesome-whole-body-control/#/report/title%3Af5518c0d6c7bc3d3) | 潜在动作语义如何被下层准确执行？ |
| 7 | [GRAIL](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2606.05160) | 合成视频如何产出对象可控、身体可执行的数据？ |
| 8 | [OpenHLM](https://memoryunreal.github.io/awesome-whole-body-control/#/report/arxiv%3A2606.22174) | 示教接口、模型适配与便宜数据分别贡献什么？ |

七篇新增讲解，加上更新后的 GRAIL；原有 EgoMimic、VITRA、EgoScale 仍保留在完整报告库。精读为 AI 辅助原文分析，未执行复现实验。

## 入选规则

- 主线必须直接涉及人形全身操作、移动—操作协调或身体—物体交互。
- 只保留少量能直接支撑上述任务的控制器与评测基准，并单独标注。
- 逐条核对 arXiv 标题与摘要；精读条目另外核查全文、指标定义、消融与部署假设。
- 不按引用数或机构名机械排序；同类方法优先保留能提供互补证据的代表工作。

## 完整精选清单

| 序号 | 论文与原文 | 主题 | 定位 | 入选理由 |
|---|---|---|---|---|
| 1 | [HOMIE](https://arxiv.org/abs/2502.13013) | 全身控制与力交互 | 主线 · 已精读 | 遥操作与步态/高度协同，作为全身示教起点 |
| 2 | [FALCON](https://arxiv.org/abs/2505.06776) | 全身控制与力交互 | 主线 · 已精读 | 重点处理手端外力与上下肢耦合，适合搬运、拉车和开门 |
| 3 | [ULC](https://arxiv.org/abs/2507.06905) | 全身控制与力交互 | 主线 · 已精读 | 单策略统一根速度、高度、躯干与双臂，比较统一和解耦控制 |
| 4 | [SkillBlender](https://arxiv.org/abs/2506.09366) | 全身控制与力交互 | 主线 · 已精读 | 以技能组合学习全身任务；高层复杂任务的仿真边界需区分 |
| 5 | [VIRAL](https://arxiv.org/abs/2511.15200) | 视觉闭环与自主策略 | 主线 · 已精读 | 从特权教师蒸馏到视觉闭环，检验自主操作的 sim-to-real |
| 6 | [WholeBodyVLA](https://arxiv.org/abs/2512.11047) | 视觉闭环与自主策略 | 主线 · 已精读 | 视觉语言动作与移动操作底层控制器的接口设计 |
| 7 | [GRAIL](https://arxiv.org/abs/2606.05160) | 合成数据与交互学习 | 主线 · 已精读 | 生成数据、接触重建与 G1 物理执行的完整链路 |
| 8 | [OpenHLM](https://arxiv.org/abs/2606.22174) | 视觉闭环与自主策略 | 主线 · 已精读 | 全身遥操作、VLA 适配与异构数据的受控比较 |
| 9 | [CoorDex](https://arxiv.org/abs/2606.23680) | 全身控制与力交互 | 主线 · 摘要核查 | 移动时协调身体与灵巧手先验，突出连续操作 |
| 10 | [HANDOFF](https://arxiv.org/abs/2606.06493) | 全身控制与力交互 | 主线 · 摘要核查 | 用互补教师构造统一任务空间全身控制接口 |
| 11 | [KAMP](https://arxiv.org/abs/2511.21169) | 全身控制与力交互 | 主线 · 摘要核查 | 运动学约束与多策略训练，用于带载全身操作 |
| 12 | [COLA](https://arxiv.org/abs/2510.14293) | 全身控制与力交互 | 主线 · 摘要核查 | 人与人形机器人协同搬运，关注负载和运动协调 |
| 13 | [StageACT](https://arxiv.org/abs/2509.13200) | 视觉闭环与自主策略 | 主线 · 摘要核查 | 开门的阶段转换与移动操作闭环，适合研究长任务接口 |
| 14 | [HumanoidExo](https://arxiv.org/abs/2510.03022) | 人类示范与真实数据 | 主线 · 摘要核查 | 可穿戴外骨骼采集全身操作数据，关注数据到执行的一致性 |
| 15 | [ULTRA](https://arxiv.org/abs/2603.03279) | 视觉闭环与自主策略 | 主线 · 摘要核查 | 参考跟踪与感知条件自主行为的统一接口 |
| 16 | [VisualMimic](https://arxiv.org/abs/2509.20322) | 视觉闭环与自主策略 | 主线 · 摘要核查 | 视觉、运动生成与跟踪连接到全身操作 |
| 17 | [Opening the Sim-to-Real Door](https://arxiv.org/abs/2512.01061) | 视觉闭环与自主策略 | 主线 · 摘要核查 | 以开门为载体检查像素到动作与接触迁移 |
| 18 | [OASIS](https://arxiv.org/abs/2606.08548) | 合成数据与交互学习 | 主线 · 摘要核查 | 仿真采集到真机全身移动操作的数据流水线 |
| 19 | [ViLoMan](https://arxiv.org/abs/2609.19340) | 视觉闭环与自主策略 | 主线 · 摘要核查 | 视觉与本体感觉的部分可观测全身操作 |
| 20 | [HumanPlus](https://arxiv.org/abs/2406.10454) | 人类示范与真实数据 | 主线 · 摘要核查 | 人类全身示范与人形模仿学习的基础路线 |
| 21 | [OmniH2O](https://arxiv.org/abs/2406.08858) | 人类示范与真实数据 | 主线 · 摘要核查 | 全身遥操作与操作学习，关注运动与手部协调 |
| 22 | [Mobile-TeleVision](https://arxiv.org/abs/2412.07773) | 人类示范与真实数据 | 主线 · 摘要核查 | 面向移动操作的遥操作与运动先验 |
| 23 | [Humanoid Manipulation Interface](https://arxiv.org/abs/2602.06643) | 人类示范与真实数据 | 主线 · 摘要核查 | 无机器人采集接口怎样落到人形全身动作 |
| 24 | [EgoHumanoid](https://arxiv.org/abs/2602.10106) | 人类示范与真实数据 | 主线 · 摘要核查 | 第一视角人类示范迁移到真实移动操作 |
| 25 | [DexRoam](https://arxiv.org/abs/2609.35761) | 人类示范与真实数据 | 主线 · 摘要核查 | 第一视角全身示范用于移动双手灵巧操作 |
| 26 | [Weave](https://arxiv.org/abs/2609.16683) | 人类示范与真实数据 | 主线 · 摘要核查 | 把人-物交互转成带接触与物体约束的全身策略 |
| 27 | [WT-UMI](https://arxiv.org/abs/2606.13232) | 人类示范与真实数据 | 主线 · 摘要核查 | 触觉/力监督下的全身接触操作数据与规划 |
| 28 | [InterMimicGen](https://arxiv.org/abs/2610.06850) | 合成数据与交互学习 | 主线 · 摘要核查 | 通过生成、跟踪和执行反馈扩充移动操作数据 |
| 29 | [GenHOI](https://arxiv.org/abs/2606.12995) | 合成数据与交互学习 | 主线 · 摘要核查 | 生成视频中的接触事件如何变成可执行人形交互 |
| 30 | [VLK](https://arxiv.org/abs/2606.30645) | 合成数据与交互学习 | 主线 · 摘要核查 | 重建场景中的合成交互与视觉全身轨迹监督 |
| 31 | [SIMPLE](https://arxiv.org/abs/2606.08278) | 合成数据与交互学习 | 主线 · 摘要核查 | 仿真训练和评估全身移动操作策略的基础设施 |
| 32 | [SONIC](https://arxiv.org/abs/2511.07820) | 支撑控制器 | 支撑 · 摘要核查 | 运动跟踪底座；不能把动作跟踪等同于物体任务成功 |
| 33 | [HOVER](https://arxiv.org/abs/2410.21229) | 支撑控制器 | 支撑 · 摘要核查 | 多种命令接口统一全身控制，供上层操作策略使用 |
| 34 | [HumanoidBench](https://arxiv.org/abs/2403.10506) | 评测基准 | 支撑 · 摘要核查 | 同时考察全身运动与操作的仿真基准，辅助设计评测 |
| 35 | [BiGym](https://arxiv.org/abs/2407.07788) | 评测基准 | 支撑 · 摘要核查 | 移动双臂示范基准；不作为双足真机能力证据 |
| 36 | [HULK](https://arxiv.org/abs/2610.08970) | 全身控制与力交互 | 主线 · 摘要核查 | 面向大外力全身移动操作，作为力交互路线的新近对照 |
| 37 | [Blind Dexterity](https://arxiv.org/abs/2608.29487) | 全身控制与力交互 | 主线 · 摘要核查 | 纯本体感觉的全身操作，作为感知需求的对照路线 |
| 38 | [LAC](https://arxiv.org/abs/2608.25405) | 全身控制与力交互 | 主线 · 摘要核查 | 线性与角向柔顺控制，面向有外力的全身交互 |
| 39 | [CEER2](https://arxiv.org/abs/2609.38709) | 全身控制与力交互 | 主线 · 摘要核查 | 可调手端与根部柔顺，把扰动适应纳入全身移动操作 |

## 每周维护

每周清单更新时复核精选名单与精读版本；网站自动重算当前占比，名单和报告经证据核查后更新。

`web/focus.json` 为名单、阅读顺序与理由的来源；`reports/curated/index.json` 记录报告版本、核查日期、来源和正文 SHA-256。发布前验证去重身份、比例预算、来源和 8 篇报告均已就绪；缺少报告或报告陈旧会阻止把该版本发布为完成。

完整库仍按原流程每周更新。占比随当前库量自动重算；新论文是否替换入选，需要按任务相关性与互补证据复核，不能以关键词、机构名或引用数自动补位。

## 暂不纳入

- **EgoMimic / VITRA / EgoScale**：保留在原论文库和报告库；本轮更聚焦全身移动操作，它们的主体实验证据主要是操作数据或上肢策略。
- **现有 BumbleBee 标记条目**：所指 arXiv:2510.25241 的官方标题为 One-shot Adaptation of Humanoid Whole-body Motion with Walking Priors，名称不一致，暂不纳入。
