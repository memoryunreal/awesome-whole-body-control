# Paper Watch：每日论文引用追踪

将原有 743 篇论文清单接入可重复运行的文献工作流：**Gmail 提醒 → 去重与补全 → 研究范围筛选 → 全文深读 → 引用图谱 → 清单更新**。界面参考 [Human Video Citation Network](https://citation.thomasyht.top/reports/INTAKE-103) 的入口组织；没有复制该站的报告或把它当成论文证据。

## 外部访问与每周更新

公开工作台：<https://memoryunreal.github.io/awesome-whole-body-control/>

网页由 GitHub Pages 托管，访问不需要 Gmail、API key 或登录。现有每周任务更新 `papers.csv` / `research_chunks` 并推送 `main` 后，`.github/workflows/pages.yml` 自动验证、构建和部署，地址保持不变。

发布构建读取 `data/paper-watch.json` 中的公开引用和报告快照，再应用最新 `papers.csv` 的新增论文、摘要、代码状态及分类；不读取本地 `.env`、邮箱或私有运行状态。网页为只读，公开访问者不能触发本地任务或修改数据。Gmail 接入不影响网页发布。

```bash
python3 -m paper_watch.publish --output _site
```

若需要把本地新生成的报告或引用也加入公开站点，先通过 `public_state` 导出到 `data/paper-watch.json`，再提交该文件；不要提交 `.paper-watch/state.json`。仅更新每周清单时不需要手工改快照。构建命令不会访问网络、调用模型或修改本地状态。

## 本地启动

Python 3.10+。清单、界面、邮件解析和元数据查询仅依赖标准库。

```bash
python3 -m paper_watch init
python3 -m paper_watch serve
```

访问 <http://127.0.0.1:8765>。概览、候选收件箱、论文库、引用网络、深读报告、订阅设置共享同一份状态。网页只有在本地服务运行时允许添加候选和触发任务；静态导出只读。

PDF 全文回退需要可选依赖，建议安装到虚拟环境：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-watch.txt
cp .env.example .env
```

在编辑器中填写 `.env`：`IMAP_USER`、`IMAP_PASSWORD`、`OPENAI_API_KEY`；可用 `OPENAI_MODEL` / `OPENAI_BASE_URL` 指定兼容接口。**不要把密码发到聊天、写进 config、命令参数或 Git。** `.env` 按字面读取，不执行其中的 shell 语句。

## Gmail 与 Google Scholar

1. Gmail 开启两步验证，在 Google 账户创建[应用专用密码](https://support.google.com/accounts/answer/185833)，填入 `IMAP_PASSWORD`。受组织策略限制、没有应用密码的账户可先用 `.eml` 导入。
2. 在 Scholar 分别搜索 [VITRA](https://scholar.google.com/scholar?q=Scalable+Vision-Language-Action+Model+Pretraining+for+Robotic+Manipulation+with+Real-Life+Human+Activity+Videos)、[EgoScale](https://scholar.google.com/scholar?q=EgoScale+Scaling+Dexterous+Manipulation+with+Diverse+Egocentric+Human+Data)、[EgoMimic](https://scholar.google.com/scholar?q=EgoMimic+Scaling+Imitation+Learning+via+Egocentric+Video)。选择准确论文，点击 **Cited by / 被引用**，再创建邮件提醒，收件地址填写这个 Gmail。不能用标题搜索提醒代替“被引用”提醒。
3. Scholar 会在新增索引后自行发送邮件；**每天 08:00 是我们的处理时间，不是 Scholar 的投递时间**。[官方说明](https://scholar.google.com/intl/en/scholar/help.html#alerts)
4. 运行：

```bash
.venv/bin/python -m paper_watch run --imap
```

IMAP 以只读方式读取 Scholar 邮件，使用 `BODY.PEEK[]`，不标记已读，不移动或删除邮件。默认回看 14 天、最多读取 50 封，可通过 `IMAP_LOOKBACK_DAYS`、`IMAP_MAX_MESSAGES`、`IMAP_SINCE=YYYY-MM-DD` 调整。数据库按论文身份去重，重复读取可恢复失败任务。

可先下载 Gmail「显示原始邮件 → 下载原始邮件」的 `.eml` 测试：

```bash
python3 -m paper_watch run --eml /absolute/path/alert.eml --no-network
```

这只执行本地解析和规则筛选，不生成深读报告。`.eml` 文件和原始邮箱内容不会进入站点导出。

## 筛选、深读与引用证据

初始种子使用作者论文原始信息：

| 种子 | 论文 |
|---|---|
| VITRA | [arXiv:2510.21571](https://arxiv.org/abs/2510.21571) |
| EgoScale | [arXiv:2602.16710](https://arxiv.org/abs/2602.16710) |
| EgoMimic | [arXiv:2410.24221](https://arxiv.org/abs/2410.24221) |

`config/paper-watch.json` 定义种子、正负关键词、阈值、采集上限和显示时间。默认沿用 HOI、WBC、loco-manipulation、重定向、遥操作、VLA，并关注 egocentric、human video、human demonstration、cross-embodiment。第一版筛选采用可解释规则：多项关键词命中才自动纳入；缺少摘要、只有弱关联或正负项冲突进入人工复核。**分数不是概率或论文质量评分。**

`target` / `review` / `excluded` 三种结果都保存理由和命中证据。论文被种子引用检索命中，并不自动成为 target。人工结果可覆盖规则：

```bash
python3 -m paper_watch decide arxiv:2602.16710 target --reason '与当前跨本体模仿学习实验直接相关'
```

深读从 arXiv HTML、PDF 或公开出版页面获取全文，再向模型请求结构化报告。报告覆盖核心结论、方法、训练数据、机器人平台、实验、基线、消融、失败案例、复现、与本组关系、种子引用语境。每个事实要求全文段落编号和原文片段；本地核查引文与数值，再进行独立蕴含审核。模型审核仍可能出错，重要实验结论需回到原文复核。

缺少 API key、只有摘要、全文不可访问、证据校验失败时显示 `blocked` / `failed`，不生成假报告。重跑会重试这些 target；已有有效报告不重复调用模型。PDF/HTML 提取范围、截断情况和未报告字段显示在报告中。

箭头方向是 **引用方 → 被引用方**。只有可核验的 Semantic Scholar citing-paper 数据、明确的 Scholar citation alert 或逐条核对的论文参考文献创建 `cites` 边；关键词命中和普通提醒不创建引用边。所有状态的候选可保留已核验关系，图谱中的边不代表推荐。Semantic Scholar 是补充来源，索引有延迟、结果受时间窗口和上限约束；采集失败和截断不会被描述为“没有新论文”。

### 人形全身移动操作子集

[移动操作精选](https://memoryunreal.github.io/awesome-whole-body-control/#/focus) 从公开库 781 篇中选择 39 篇，并完成其中 8 篇精读。名单、阅读顺序、主题、入选理由和来源在 `web/focus.json`；详细口径见 [选集说明](humanoid-loco-manipulation.md)。主线覆盖控制与力交互、视觉自主、人类示范、合成交互；支撑控制器和基准单独标注。完整论文库和原有报告保留。

网站默认在精选入口展示 8 篇阅读路线，可切换 39 篇清单、按主题筛选与搜索。占比按当前公开库自动重算；每周清单刷新后复核名单与精读版本，使用经过来源核查的替换条目，不用关键词自动填充。发布构建校验去重身份、预算、来源链接和精读就绪状态；未完成的报告不会计为完成。每日引用追踪和既有每周检索继续保留。

### 精选论文讲解

`reports/curated/` 保存 EgoMimic、VITRA、EgoScale、GRAIL 的 AI 辅助精读，重点比较方法、指标定义、基线、消融、复现条件和本组研究价值。各报告明确区分原文结果与分析意见，附论文版本和官方来源；未运行复现实验。

`index.json` 记录机构、入选理由、来源核查日期、全文 SHA-256 和已核对的引用。修改正文后须重新检查受影响的事实，并更新清单中的哈希。`python3 -m paper_watch.publish` 在离线构建时载入这些报告，哈希不符或尚未核查时停止发布，不需要邮箱或模型 API。每周清单刷新会保留这些报告；公开站点的“深读报告”支持目录、实验表格和 Markdown 导出。

只有通过全文报告校验的 target 自动写入 `research_chunks/09_watch.md`，再运行 `build.py` 更新 README、CSV 和分类清单。不修改人工维护的原有八个 chunk；不自动声称代码开源，也不自动 commit 或 push。

## 状态与静态导出

- `.paper-watch/state.json`：本地持久状态，包含论文、来源、筛选、报告、引用边和最近运行。原子写入、进程锁，避免任务相互覆盖。
- `.paper-watch/reports/`：已校验报告及来源记录。
- `.paper-watch/site/`：可部署静态网站，带公开论文数据，不包含原始邮件、邮箱身份、密钥或本地路径。
- `papers.csv` / `research_chunks/`：原有清单继续有效。

```bash
python3 -m paper_watch status
python3 -m paper_watch build-site --output /absolute/path/site
python3 -m unittest discover -s tests -v
```

网页采用 JSON 和 hash 路由，静态主机不需要 URL rewrite。可将导出的目录部署到 GitHub Pages 或已有静态主机。仅在本机服务中允许写入操作。

## 每日执行

本次已在 Codex 中创建“每日论文引用追踪”，每天北京时间 08:00 在当前任务运行本地流程；现有每周检索保留。任务优先使用 `.venv/bin/python`，否则使用 `python3`，自动读取本仓库 `.env`。需要本机与 Codex 可运行；任务状态在 Codex 的自动化界面管理。其他机器部署时需要自行创建调度，配置文件中的时间不会安装系统定时器。

未配置 Gmail 时，命令使用公共引用来源。需要补全 `.env` 才能真正收邮件和生成报告。手动强制检查 Gmail 可使用 `python3 -m paper_watch run --imap`。默认公共引用窗口为过去 30 天（`CITATION_LOOKBACK_DAYS`）；需补历史时可设置 `SEMANTIC_SCHOLAR_SINCE=YYYY-MM-DD`，同时增大检索上限。缺少出版日期的结果可能不在日期窗口内，邮箱提醒可补足一部分遗漏。

另提供 `.github/workflows/paper-watch.yml`，适合机器不常在线的情况。在仓库配置 `PAPER_WATCH_ENABLED=true`、Gmail 和模型 Secrets 后，GitHub Actions 每天 UTC 00:00（北京时间 08:00）执行并上传静态网站 artifact。未开启变量时不会读取邮箱。GitHub 调度可能延迟；缓存状态是尽力保留，长期可靠部署应使用持久磁盘或保管状态备份。[GitHub 调度说明](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

不要同时启用多个执行器处理同一流程。默认使用本地执行；Actions 是备用部署方式。现有每周全领域人工检索可继续保留，作为 Scholar 引用提醒的补充。
