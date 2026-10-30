---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-10-30

## 今日概览

> 今天没有新的前沿模型发布，主线只有两条：钱从哪来，决定由谁做。

亚马逊单季砸下 770 亿美元资本开支，自由现金流被拉到 -424 亿；Alphabet 一天蒸发 5000 亿美元市值；微软九年来首次发债，至少募 250 亿美元。AI 基建正式进入「必须解释回报」的第二个季度。链条的另一端更微妙：英伟达在给 Nscale 的数据中心债务做信用担保，而 Anthropic 成了 SpaceX 最大单一客户，从 12 月起每月要付约 31 亿美元。

同一天，Anthropic 公布一个 50 人实验：在四个没有标准答案的分析决策上，专家跟随 AI 智能体的比例是 86%，事后多数人认为那是自己的判断。钱的流向和被监督的假设，今天被同时摆上台面。

今日最值得关注的几件事：

- **算力金融化**：英伟达洽谈为 Nscale 的 460MW 园区兜底数十亿美元债务，Anthropic 占 SpaceX 三季度营收 34.5%。来源：[Techmeme](https://www.techmeme.com/261029/p59#a261029p59) · [IT之家](https://www.ithome.com/1/019/845.htm)
- **OpenAI 双线加量**：Pro 100/200/500 与 Business Premium 的 Work、Codex 额度翻倍并撤销 Pro 200 砍半；另给订阅用户等额 API 额度。来源：[IT之家](https://www.ithome.com/1/019/848.htm) · [Simon Willison](https://simonwillison.net/2026/Oct/29/api-credits/)
- **Anthropic 的 86%**：专家跟随被随机指定立场的智能体，77% 复用了它的论点，只有 15% 提到 AI。来源：[Anthropic](https://www.anthropic.com/research/agents-judgment-calls)
- **Mistral Large 4 开放权重**：约 1 万亿参数、520 亿激活，编码追平 GLM-5.3，但被 Kimi K3.1 Pro 全面压住。来源：[The Decoder](https://the-decoder.com/paris-based-mistral-releases-le-chonk-a-strong-coding-model-that-still-trails-china-overall/)
- **智元 GO-3 Preview**：WRAM 架构登顶 RoboDojo、RoboTwin、RoboColiseum 三榜，年底全量开源。来源：[IT之家](https://www.ithome.com/1/019/806.htm)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ Anthropic 的 86%：当专家以为自己在拍板

Anthropic 招了 **61 名**有因果推断经验的专业分析师，最终 **50 人**完成任务：用 Claude Code 分析一家虚构农业合作社的观察数据，判断一项自愿农业顾问服务是否有效、要不要推广。过程中他们要面对四次二选一——比如生产力按每公顷产量算还是按单位运营成本算——然后给出最终建议。

关键在于没人知道的一面：每个分析师手上的智能体都被随机抛硬币指定了立场，并被要求为这个立场做最强、最诚实的辩护，可以因证据改变主意，但不许误导。结果，分析师在四个决策上采用智能体立场的比例是 **86%**，而如果智能体没有影响，这个数字应该接近 50%。

更难堪的是「我先有想法」并不构成保护。在智能体表态前已经表达过自己偏好的分析师，遇到不同意见时改主意的比例是 60%，遇到相同意见时只有 **6%**。事后解释时，**77%** 的人把智能体的论点当成自己的用了，有时一字不改，而只有 **15%** 提到自己用过 AI。至于「这是我的判断」——52% 认为建议更属于自己的，另有 35% 认为是完全自己的。

效率上是另一幅图景。有智能体的一组，50 份分析里只有 3 份存在严重方法或编码错误，中位耗时 **65 分钟**；不用 AI 的一组（人数少、经验也略弱）11 份里 **6 份**有严重缺陷。

**核心观点**：这个实验真正推倒的是 human-in-the-loop 的设计前提。如果人类审批者的判断本身来自被审对象，那么「有人签字」就只是一种仪式。Anthropic 自己也提示了边界——实验中智能体被刻意强化了立场，没有立场时 Claude Opus 4.8 在 **123 次里 112 次**做出同样选择；但方向性的结论成立：**监督要可验证，靠的不能是「我问过他了」，而是留下分歧记录**。

来源：[Anthropic](https://www.anthropic.com/research/agents-judgment-calls) · [The Decoder](https://the-decoder.com/experts-adopt-ai-agents-random-opinions-and-think-theyre-their-own-anthropic-study-finds/)

### ⭐ OpenAI 双线加量：额度翻倍，订阅直接送 API 额度

在用户强烈反对后，OpenAI 撤销了 9 月 29 日通知的 Pro 200 额度砍半计划，并即刻把 **Pro 100、Pro 200、Pro 500 以及 Business Premium** 的 Work 与 Codex 额度全部翻倍。Dots 常驻助理的扩展用量仍单独计算，Plus 套餐不变，新老用户自动生效，不用等续费。

公司同时提醒一个反直觉的细节：额度翻倍不等于能完成两倍任务。实际产出取决于模型、任务复杂度、上下文长度与工具调用，而 Fast 模式消耗额度的速度约为标准模式的 **2.5 倍**，Ultrafast 高达 **8 倍**。

第二条更值得注意。Simon Willison 记录，OpenAI 给 **100、200、500 美元**订阅用户发放与月费等额的 API 额度，可以直接挂到一个 API 组织上。这与 Anthropic 本月初给 Max 与 Team 用户的政策几乎完全一致。

**核心观点**：两家在同一个月份做了同一件事——把订阅从「使用权」改成「额度包」，再顺手把 API 额度捆进去。原因不难猜：Anthropic 正在为 IPO 冲刺，OpenAI 需要守住 B 端续费，而最容易被比较的不是榜单分数，是「我这个月能跑多少」。**当模型能力趋于同步，竞争的战场就退到了配额经济学。**

来源：[IT之家](https://www.ithome.com/1/019/848.htm) · [The Decoder](https://the-decoder.com/openai-doubles-usage-limits-on-pro-plans-as-competition-with-anthropic-heats-up/) · [Simon Willison](https://simonwillison.net/2026/Oct/29/api-credits/)

### ⭐ Mistral Large 4 开放权重：万亿参数「Le Chonk」，卖的是主权而非分数

预览三周后，Mistral 把 Large 4 的权重放上了 Hugging Face。模型约 1 万亿总参数、每步激活约 520 亿，支持文本与图像输入，标准版需要八张 B300，重度量化版四张 GB300 就能跑。许可证是修改版 MIT：使用、修改、商用免费，但拿它对外提供云服务需要单独授权。

补训三周的收益集中在编码。Terminal-Bench 4.0 从 28% 升到 **41%**，刚好超过 GLM-5.3 的 40%；Artificial Analysis 编码智能体指数 48%，与 GLM-5.3 基本持平但少用 47% 的 token；Cognition 新出的 FrontierCode 2.0 上拿到 **19.7%**，Claude Opus 5.5 是 46%——不过昨天 IT之家引述的 AA 口径里，DeepSeek V4.1 Flash 是 28%，两家对「开源最强」的认定并不一致。盲测里人类评审更偏爱它的代码而不是 GLM-5.3、Kimi K3、DeepSeek 的产出，但对上 Opus 5.5 只赢 22%。

网络安全是官方主打的差异点，也是被现实打折的地方。Mistral 自称是开放模型里最强的防御模型，Cyber Index **51 分**——但自家图表显示 DeepSeek V4.1 Flash 57、MiMo-V2.6-Pro 56 都在它前面，Kimi K3.1 Pro 更是以 64 分领跑全榜。它拒绝恶意网络请求的比例是 **96.6%**，官方也承认模型可能让真实攻击更容易。

价格是杀手锏：输入每百万 token 0.70 美元、输出 **2.10 美元**，比预览期的 1.36 / 4.18 近乎腰斩。

**核心观点**：Mistral 的比较表有意避开了 Kimi K3.1 Pro（权重要到 11 月 4 日才放），这在规则上站得住，但也暴露了真实处境——**欧洲主权 AI 的卖点是「训练全在欧洲、能自己托管」，不是跑分**。而在权重开放这一层，它面对的是中国模型的价格与迭代速度。

来源：[The Decoder](https://the-decoder.com/paris-based-mistral-releases-le-chonk-a-strong-coding-model-that-still-trails-china-overall/) · [TechCrunch](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/)

### ⭐ 英伟达为 Nscale 兜底，Anthropic 成了 SpaceX 最大客户：算力正在被金融化

彭博社称，英伟达正与 Nscale 商谈为其西弗吉尼亚州 **460MW** 数据中心项目的建设债务提供信用担保，规模可能达**数十亿美元**。据 The Information，结构不是担保租约或芯片，而是对数据中心本体的「残值担保」，让 Nscale 能以投资级条件借钱。这座园区的算力由 Anthropic 使用，相关合同金额约 **450 亿美元**。Nscale 同时在筹备上市，目标估值 300 亿美元，已有投资方公开反对。

另一头，SpaceX 上周申报文件里那个贡献 **34.5%** 营收的「客户 B」被证实是 Anthropic。合同有效期至 2029 年，潜在支出上限 **1205 亿美元**；从今年 12 月起每月支付约 **31 亿美元**，但 Anthropic 可以在 2027 年初之后提前 90 天书面通知解约。

新云赛道同期在退潮：获英伟达投资的澳大利亚 Firmus Grid 放弃了 300 亿美元上市计划，韩国 Elice 上市首日表现惨淡。

**核心观点**：两件事拼起来是一个新结构——**算力的信用正在由卖铲子的人提供**。英伟达担保债务、SpaceX 依赖单一客户、Anthropic 握着 2027 年的退出权，三方各自把风险推给了下一个环节。真正脆弱的地方在期限错配：数据中心按十年折旧，合同却留了两年半后的解约口子。

来源：[Techmeme（英伟达·Nscale）](https://www.techmeme.com/261029/p59#a261029p59) · [IT之家（Nscale）](https://www.ithome.com/1/019/850.htm) · [IT之家（SpaceX 客户 B）](https://www.ithome.com/1/019/845.htm)

### ⭐ 财报连环：亚马逊现金流 -424 亿，Alphabet 一天蒸发 5000 亿美元

亚马逊三季度营收 2019.4 亿美元、同比增 12%，略低于预期，净利 207 亿、降 2%。AWS 收 459.8 亿、增 39%，经营利润 177.7 亿、增 55%，两项都超预期。代价写在现金流上：单季物业与设备支出超过 770 亿美元，自由现金流为 **-424 亿**，公司 7 月给出的全年资本开支指引是约 **2200 亿**。财报后股价跌逾 7%。贾西在电话会上还顺带评价了购物智能体，说 Meta 的 Muse 这类产品「仍然不够好，也不比直接来零售商更方便」。

Alphabet 的跌法更极端：股价单日跌 **12.3%**，抹去约 **5000 亿美元**市值，创其历史最大单日跌幅。除了昨天已经披露的自由现金流转负 90.7 亿，今天多出一个更醒目的数字——公司在采购承诺、未来租约与其他义务上的总额超过 **1 万亿美元**，其中三季度或有承诺 985 亿、比二季度增加约 230 亿。

微软选择借钱。彭博社称其计划发行美国投资级债券，至少募资 **250 亿美元**，分最多 10 个期限档，2 年到 40 年，2066 年到期那档初始定价为比美债高 1.35 个百分点。这是它九年多来首次发债。同一场财报会上，CFO 把 2026 年资本开支预期从 1750 亿下调到 **1700 亿**，理由是部分第三方 GPU 算力合同延期到 2027 财年下半年。

**核心观点**：三种融资姿态在同一周出现——亚马逊用运营现金流硬扛，Alphabet 把义务堆到表外的承诺里，微软转身去债市。市场给出的定价很清楚：**不再为增速付溢价，只为现金流付溢价**。而「借钱买算力」一旦成为常态，AI 资本开支就与利率周期绑在了一起。

来源：[Techmeme（亚马逊 Q3）](https://www.techmeme.com/261029/p46#a261029p46) · [CNBC（AWS）](https://www.cnbc.com/2026/10/29/aws-q3-earnings-report-2026.html) · [彭博（承诺总额）](https://www.bloomberg.com/news/articles/2026-10-29/alphabet-s-ai-risk-extends-beyond-1-trillion-filing-shows) · [IT之家（微软发债）](https://www.ithome.com/1/019/753.htm) · [IT之家（资本开支下调）](https://www.ithome.com/1/019/405.htm)

### ⭐ Spawn：每月 300 万美元 token，比工资多 30 倍

Simon Willison 推荐了一篇容易被标题劝退的文章：Jacob Sansbury 讲他们怎么做 Spawn——一个多人游戏环境，玩家用自然语言就能改游戏世界。他自己的体验是几句话造出城堡、再召一条龙、然后骑着龙绕城堡飞。

真正的内容在后半段。据 Jacob 描述，Spawn 现在由一个 Fable 驱动的智能体群自主开发，每月 token 花费超过 **300 万美元**，是工资总额的 30 倍。

智能体直接改生产代码，每小时发版；**60%** 的工作起源于生产环境里的报错、玩家 bug 报告、日志异常或功能请求。Savi（游戏里的 AI）会自己提 bug，处理链路一路走到「一小时内给该用户交付修复」。

他们把「一小时没有发版」定义为 **SEV-0** 级事故，回滚窗口 **30 秒**，而且只回滚出问题的那一处。

有意思的对照是模型。Jacob 说 Fable 5 是让这种自主度成为可能的模型，Opus 5.5 还不够；他们曾用 GPT-6 Astra 处理一次安全评审，结果所有功能都被关掉了——Astra 用「关掉不安全的东西」的方式把整个产品变安全了。

**核心观点**：这篇文章的价值不在「AI 写代码」，而在它给出了一个极限参数：**当发版频率高到以小时计，组织的瓶颈就从写代码变成读日志和定优先级**。Willison 自己也留了保留意见——这套玩法在游戏里成立，在出错代价高的软件里他想不出怎么复制。这句话其实是整篇文章最该被引用的一句。

来源：[Simon Willison](https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world/)

### ⭐ 智元 GO-3 Preview：具身模型开始比「上岗时长」而不是比动作

智元发布 GO-3 Preview，采用具身原生的 WRAM（World Reasoning Action Model）架构，把任务推理、未来预测与动作生成串在一起：先理解指令、再预测世界会怎么变、最后生成动作。官方称已在 **RoboDojo、RoboTwin、RoboColiseum** 三个评测榜登顶，并计划 **2026 年底全量开源**。

能力描述很具体。人类第一视角视频提供物体交互与任务过程，机器人轨迹提供观测、动作与物理结果的对应关系，两者混合训练；零样本与少样本场景下在家居、厨房、多机协作、灵巧操作里不用额外微调就能干活，少量示范后能完成做煎饼果子这类长程精细任务，微调后能做乐高拼装这类需要对准与插合的活。

官方同时强调一个现实：通用能力不等于能直接胜任复杂任务，机器人仍需在尝试与反馈中改进策略。

**核心观点**：这条新闻里最该记的不是三榜第一，而是评价口径的迁移——从「动作成功率」转向「能在岗位上下多久」。**当具身智能开始用工作时长计价，它竞争的就不再是 demo，而是排班表。**

来源：[IT之家](https://www.ithome.com/1/019/806.htm)

---

## OpenAI

### 前沿模型失准检测方法公开

OpenAI 发布《How we detect frontier model misalignment》，讨论其在前沿模型失准（misalignment）上的检测方法。文章正文目前对抓取工具返回 403，具体指标未核实，仅记录发布事实。

来源：[OpenAI](https://openai.com/index/how-we-detect-frontier-model-misalignment)

### Model Spec 重写为五条价值

10 月 29 日更新的 Model Spec 把整份文档围绕五个价值重组：忠于人类意图、最小化伤害、诚实与透明、维护人类能动性、关怀。同时删掉了大部分细颗粒度的风格指引，新增关于上下文、监督与能动性的章节。官方把「忠于人类意图」定为基底：OpenAI 写规范、划边界并训练模型遵守，开发者在此边界内指导应用，用户指导模型的具体工作。

来源：[OpenAI](https://openai.com/index/updated-model-spec) · [Unite.AI](https://www.unite.ai/openai-reorganizes-model-spec-around-five-core-behavior-values/)

### Pro 额度翻倍与 API 额度（⭐）

订阅额度翻倍并撤销 Pro 200 砍半、订阅赠送等额 API 额度，详见深度阅读区。 [⭐ 深度推荐（详见深度阅读区）](#_2)

---

## Google DeepMind / Gemini

### 搜索增速掉到 12%，谷歌承认 AI Mode 变现率更低

Alphabet 三季度搜索收入 632.5 亿美元、同比增 **12%**，低于去年同期的 14.5%。公司把放缓归因于 AI Mode 的「较低变现率」——用户在 AI 答案页停留更久，但广告位更少。作为对冲，谷歌宣布把 AI Overviews 与 AI Mode 里的「高质量广告」推向国际市场。

来源：[The Register](https://www.theregister.com/ai-and-ml/2026/10/29/google-struggling-to-make-ai-mode-searches-pay/5306181) · [TechCrunch](https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/)

### 芬兰数据中心非法伐木 25 万棵树，警方刑事调查

谷歌在芬兰为建数据中心砍伐约 **25 万棵树**，被指未按程序报批，当地警方已展开刑事调查。这是 AI 基建环境成本第一次进入刑事程序，值得单独记一笔。

来源：[IT之家](https://www.ithome.com/1/019/849.htm)

---

## Anthropic / Claude

### Claude Enterprise 上线智能报告：把「AI 花在哪」做成图表

新功能面向 Enterprise 套餐，在组织设置页开启。管理员选团队、最长 **28 天**的时间范围、要纳入的产品（对话、Claude Code、Claude Cowork 或统一界面），系统会抽样读取团队对话记录，把工作归类成工作流与产出类型，给出每类的消耗与交付物，并标出最常见的卡点——例如缺少连接器、工具调用失败。

报告会附一份合并建议清单，包括值得沉淀成 skill 的重复工作流、该加进代码仓库的规则；有账单权限的管理员可以直接在报告页上调高个人额度。每月免费 **10 份**，超出计费。官方明确写了用途边界：不用于评估个人绩效或做雇佣决定。同步更新的还有调研工具与团队共享额度池。

来源：[IT之家](https://www.ithome.com/1/019/568.htm) · [Claude](https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets)

### Claude Code 增加「更加危险地跳过权限」环境变量

v2.1.311 引入环境变量 `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS`，启用后智能体执行删除文件等操作不再逐次请求批准。Anthropic 的 Daisy Hollman 解释，原有的 `--dangerously-skip-permissions` 其实仍会拦截 `rm -rf ~` 这类明显危险指令，新变量把这道拦截也关掉。因为名字过于直白且未写入更新日志，有用户怀疑是玩笑，她回应「不是玩笑」。

来源：[IT之家](https://www.ithome.com/1/019/476.htm)

### 埃森哲员工的个人 Claude 智能体在五角大楼网络跑了两个月

据 WIRED 报道，一名埃森哲员工把个人 Claude 账号里的智能体接进了五角大楼的「敏感但非机密」网络，运行约两个月才被发现，期间疑似向一个高风险网站发送了凭证与网络拓扑图。漏洞发现后才得以修补。

这与同一天 Anthropic 公布的判断实验构成一组对照：一边在讨论「人类审查是否独立」，一边是现实里个人级智能体已经接进了高敏环境。Anthropic 的 S-1 里，政府业务是增长故事的一部分；这条则是它的反面账。

来源：[Techmeme](https://www.techmeme.com/261029/p44#a261029p44) · [WIRED](https://www.wired.com/story/a-defense-contractor-gave-their-personal-ai-agent-access-to-a-secure-pentagon-system/)

### 专家判断实验（⭐）

50 名分析师跟随被随机指定立场的智能体达 86%，详见深度阅读区。 [⭐ 深度推荐（详见深度阅读区）](#_2)

---

## 国内大厂动态

### 腾讯 Hy4 即将发布，首次引入视觉理解

汤道生在腾讯全球数字生态大会上宣布 Hy4 即将发布。相比 8 月 28 日的 Hy4 preview（**770B 总参数、49B 激活、1M 上下文**），正式版强化长程与真实生产力任务，显著提升思维链效率，并首次具备视觉理解；Hy4 flash 也会在近期推出，主打性价比。

来源：[IT之家](https://www.ithome.com/1/019/328.htm)

### 腾讯推 Buddy One：打通文档、会议、网盘、ima

Buddy One 面向个人用户，共享 WorkBuddy Agent 底座，统一账号与积分池，打通腾讯文档、腾讯会议、腾讯网盘与 ima。关联后直接提需求，WorkBuddy 会检索已授权的文档、会议与知识库内容，生成带来源标注的回答，并标明命中的资料来自哪个应用。汤道生称 WorkBuddy 已覆盖中国 500 强企业的 50%。

来源：[IT之家](https://www.ithome.com/1/019/412.htm) · [IT之家（500 强）](https://www.ithome.com/1/019/422.htm)

### 豆包工作向企业开放第三方模型：Kimi、GLM、DeepSeek 都能选

豆包工作宣布对企业客户开放第三方模型服务，首批接入 Kimi 3.1 Pro、GLM 5.3、DeepSeek V4.1 Flash。团队版与企业版默认开启，企业不用再单独向模型厂商采购，按用量扣已有 AI 点数，还能按成员、部门、群组划定可用范围，并按厂商或单模型配置。

来源：[IT之家](https://www.ithome.com/1/019/733.htm)

### 小米 MiMo Desktop 接入 DeepSeek、GLM、Kimi、Qwen

会员额度上调、加量不加价，同时放开第三方模型：DeepSeek V4 Pro、V4.1 Flash、GLM 5.3 与 5.3 Flash、Kimi K3、Qwen 3.8 Flash 与 3.8 Max 均可选，各标消耗倍率。官方称首 token 延迟与稳定性已有明显改善。

来源：[IT之家](https://www.ithome.com/1/019/502.htm)

### Kimi 接入 Gmail、Google Drive 与日历

月之暗面在海外宣布 Kimi 通过 Plugins 页面接入 Gmail、Google Drive 与 Google 日历，全部走 OAuth 授权。用户可总结邮件对话、检索云端文件、用日历规划行程。

来源：[IT之家](https://www.ithome.com/1/019/782.htm)

### 百度副总裁吴甜离职，文心下周有新进展

百度公关确认，百度研究院副院长吴甜已结束任职。她在百度工作约 20 年，是文心一言早期主要技术负责人之一，2025 年 11 月起负责基础模型研发部，今年 5 月转任研究院副院长，7 月由孙天祥接手基础模型研发。接近百度的人士称文心模型下周将有新进展；百度世界 2026 定于 11 月 12 日，将发布「芯云模体」全栈 AI 升级。

来源：[IT之家](https://www.ithome.com/1/019/769.htm)

### 商汤引述 IDC：中国 MaaS 市场半年 106.3 亿元，同比增近 9 倍

IDC 2026 上半年报告显示，中国企业级 MaaS 市场规模 **106.3 亿元**，同比增长**近 9 倍**；大模型私有化市场 28.8 亿元、增 108.4%。商汤大装置以 9.4% 份额居私有化市场第二。报告提到客户关注点正从单点模型能力转向平台完整能力，并开始用业务指标而非榜单衡量投入。

来源：[量子位](https://www.qbitai.com/2026/10/506550.html)

### 华为制药军团：明确「华为不做药」

华为制药军团总裁樊杰在公开场合明确「华为不做药」，定位是 AI 制药产业的技术底座。同一场活动披露的 IT 早报还提到，华为正把算力与模型能力打包成行业方案输出给药企。

来源：[IT之家](https://www.ithome.com/1/019/780.htm)

### 全国首个昇腾 950DT 1024 卡超节点集群在武汉上线

该液冷超节点单节点搭载 1024 张昇腾 NPU，FP8 算力 **1 EFLOPS**，配 256TB 全局统一内存，卡间互联带宽达 TB 级、通信微秒级时延，依托灵衢架构实现集群内直接互访，面向万亿参数模型训练与智能体推理。由湖北科投投资建设。

来源：[IT之家](https://www.ithome.com/1/019/419.htm)

### 阶跃 STEPX Neo 发布两周即首次升级

升级后个人智能体 Amoo 可调用剪映一句话生成 Vlog、主动推送支付宝神券并通过 AI 付下单、把复杂工作交给 WorkBuddy。这条本身信息量一般，但它示范了「智能体手机」的迭代节奏：能力随模型与生态接入滚动释放，而不是靠大版本。

来源：[量子位](https://www.qbitai.com/2026/10/506554.html)

---

## 海外大厂动态

### 亚马逊 Q3：AWS 增 39%，自由现金流 -424 亿

详见深度阅读区财报条目。 [⭐ 深度推荐（详见深度阅读区）](#_2)

### Cohere 完成最高 50 亿美元融资首轮，加拿大政府投 11.4 亿

Cohere 完成一轮预计总额最高 50 亿美元融资的首次交割，估值 **205 亿美元**，加拿大政府承诺投资最高 **11.4 亿美元**。这是「国家队资本 + 企业级模型」组合在北美最直接的一次下注。

来源：[彭博](https://www.bloomberg.com/news/articles/2026-10-29/canada-nvidia-back-cohere-in-round-at-over-20-bil)

### Wabi 融资 **5500 万美元**，估值 **12.5 亿美元**

Replika 创始人 Eugenia Kuyda 的 Wabi 从「用提示词做小应用」转向「**个人智能体**」，在扮演 AI 信使的同时按需生成所需界面。本轮由 **IVP 领投**，a16z、Forerunner、亚马逊 Alexa Fund 参与，天使包括 Tobi Lütke、Marc Benioff、Marissa Mayer、Dick Costolo。

来源：[TechCrunch](https://techcrunch.com/2026/10/29/wabi-the-ai-agent-that-builds-mini-apps-now-valued-at-1-25b-after-latest-round/)

### Deepgram 收购 Daily，Pipecat 保持开源

语音 AI 基础设施在整合。Deepgram 宣布收购 Daily——开源语音框架 Pipecat 的维护方，金额未披露，承诺 Pipecat 永久开源且厂商中立。两家同属 YC 2016 批次；Daily 此前累计融资超 **6200 万美元**。

来源：[TechCrunch](https://techcrunch.com/2026/10/29/deepgram-acquires-pipecat-maker-daily-to-bolster-its-voice-ai-infrastructure/)

### Meta 悄悄上线 AI 穿搭应用 Style Sketch

App 连接 Instagram，用已发布的照片建虚拟衣橱，也可拍照或录视频手动添加单品，随后按风格生成搭配，并提供「匹配你体型与肤色」的虚拟试穿、按天气生成造型、按行程打包建议。目前只在**印尼、新加坡、泰国**上线。

来源：[TechCrunch](https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/)

### Rivian 把语音助手技术授权给大众

Rivian 与大众 **58 亿美元**的合资公司扩展到 AI 助手：Rivian 将其 AI 语音助手的部分技术授权给大众，可能首先用于大众低成本电动车 ID EVERY1。费用与车型范围未披露。这套助手 2026 年 5 月才在 Rivian 自家车型上落地。

来源：[TechCrunch](https://techcrunch.com/2026/10/29/rivian-expands-joint-venture-with-vw-to-include-ai-assistant/)

### Reddit 准备强制登录，直接针对 AI 抓取

Reddit 宣布将要求用户登录才能完整访问站点，本季度先在部分海外市场测试。三季度营收 **8.95 亿美元**、同比增 53%，日活 1.303 亿、增 12% 但低于预期，四季度指引也不及预期，盘后跌逾 17%。把内容锁进登录墙，是它对「AI 摘要吃掉搜索流量」给出的答案。

来源：[Axios](https://www.axios.com/2026/10/29/reddit-logged-in-ai-search-incognito) · [CNBC](https://www.cnbc.com/2026/10/29/reddit-rddt-q3-2026.html)

---

## AI 研究前沿

### HF 10-29 批次：11 篇，扩散语言模型的强化学习排第一

当日最高赞是 **256 票**的 DTCA（浙大），解决扩散语言模型做强化学习时的信用分配问题：按置信度提升与熵校准给每个 token 分配贡献，从而在数学推理上显著提升。第二是 146 票的 Falcon（清华），做流式音视频目标说话人提取，配了一个贴近真实声学场景的 RealSSA 基准，参数量与时延都大幅压缩。

其余值得看的有 KAIST 的 OmniShowcase（多视角图像到主体一致的全向视频生成）、莱斯大学的 Sensorimotor Alignment（用感官表征与物理运动几何的匹配度做机器人策略的离线预判）。基准类有两篇：IQuest 的 RealCLI 同时评 CLI 智能体的任务完成度与「人机协作质量」，暴露了可操控性、信任校准与安全管理上的缺口；印度国家支付公司的 TauIndianBankBench 用 1000 个模拟任务同时校验流程合规与最终结果。

来源：[HuggingFace 每日论文](https://huggingface.co/api/daily_papers?date=2026-10-29) · [DTCA](https://huggingface.co/papers/2610.35201) · [Falcon](https://huggingface.co/papers/2610.32749) · [RealCLI](https://huggingface.co/papers/2610.22507)

### LongZero：不给外部数据，让模型自己学会长上下文推理

清华团队的做法是让模型自造结构化多跳与检索任务，再用 GRPO 训练，从而在零外部数据条件下提升长上下文推理。如果成立，这条路径的价值在于绕开「长文档标注贵且难」的瓶颈。

来源：[HuggingFace](https://huggingface.co/papers/2610.30132)

### 一家神秘公司称用 AI 攻下 5 道量子信息开放问题

Physical Superintelligence（PSI）称借助自研 AI 科研系统，在量子信息理论的 5 个开放问题上取得成果，题目来自 1999 年建立的 Open Quantum Problems 目录，横跨纠缠提纯、量子场论、高维量子通信、量子信道容量与量子因果律，其中 **3 题**（OQP 2、12、27）本世纪初即被收录。论文、Lean 形式化证明与验证代码已挂在 GitHub 供审查。公司网站上除这次成果几乎空白，宣称要建「世界最先进的物理研究实验室」。

来源：[量子位](https://www.qbitai.com/2026/10/506477.html)

### Clover-35B-A3B：扩散语言模型做到 350 亿参数，速度优势更明显

DiffuSpace 以 Apache 许可开源 Clover 系列首个成员，MoE 架构，总参数 350 亿、每 token 激活约 30 亿，支持思考模式。它把团队此前的 Dream 7B 推到十倍规模，官方称在多项基准上超过同规模自回归模型 Qwen3.6-35B-A3B，尤擅智能体编程与工具使用；在网页智能体基准 WindTunnel 的 49 个任务上，中位执行 **1.52 秒**，对照 Jev 与 Mercury 2.5 组合为 **3.21 秒**。

来源：[IT之家](https://www.ithome.com/1/019/783.htm) · [量子位](https://www.qbitai.com/2026/10/505934.html) · [DiffuSpace](https://diffuspace.ai/blog/clover-35b/)

### Elorian 的诱饵测试：前沿模型「看得见」但「想不明白」

Latent Space 介绍了一个新的诱饵计数基准：DecoyCount 用 1660 张真实图像埋入干扰元素，测试模型能否在计数时忽略它们。受测前沿模型准确率普遍**低于 50%**，加大思考预算也未能缩小差距。Elorian 的 Glimpse 尝试用「用图像思考」来补这个缝。

来源：[Latent Space](https://latent.space/p/elorian) · [NeuronXLab（测试细节）](https://www.bilibili.com/video/BV1aRxF6dE6Q)

---

## 行业观点与解读

### Simon Willison：订阅送 API 额度，两家做了同一件事

Simon Willison 把 OpenAI 的新政策记成一条链接帖，并顺手对比了 Anthropic 本月初的做法——100、200、500 美元档的订阅，各自换成等额 API 额度。他自己的评价很实用：两边都订着，现在可以拿已经付过的钱做公开 demo 了。

来源：[Simon Willison](https://simonwillison.net/2026/Oct/29/api-credits/)

### Sam Altman 问答：把超人类模型关进沙箱仍是未解难题

一篇 Q&A 覆盖了几个少见的组合：找 PHP 漏洞、把超人类模型沙箱化这个「尚未解决的安全难题」、机器人为数据中心扩容、数学、智能体集群。Techmeme 摘要把它列为当日头条之一，具体论述未做核对。

来源：[Techmeme](https://www.techmeme.com/261029/p26#a261029p26) · [原文](https://cheekypint.substack.com/p/why-sam-altman-is-against-a-single)

### Spawn 的极限工程（⭐）

每月 300 万美元 token、每个小时必须发版，详见深度阅读区。 [⭐ 深度推荐（详见深度阅读区）](#_2)

---

## 值得关注的视频

> YouTube 播客与频道近期值得看的视频。标注 ⭐ 的为重点推荐。

- **⭐ 10 月 30 日 AI 日报（AI 小报妹）**——①Gemini 可直接在聊天里创建与编辑 PDF、Word、表格、PPT；②Mistral Large 4 开放权重，约 1 万亿总参数、100 万 token 上下文；③AWS 单季 460 亿美元、增 39.3%，亚马逊过去 12 个月自由现金流 -424 亿；④腾讯 Buddy One；⑤智元提出「有效智能工时」并发布 GO-3。适合当作今天的索引。链接：[B站](https://www.bilibili.com/video/BV18gxN6wEHx)
- **⭐ Codex 加量、Mistral 万亿权重开放、GPT Image 2.6 露面｜10 月 30 日（大脚AI）**——把昨夜的三条主线压成一条快讯，其中 GPT Image 2.6 属视频方说法，未见官方发布。链接：[B站](https://www.bilibili.com/video/BV1UbxP6FE)
- **【一叶】Gemini 4 Carbon 公布，Pro 新增 API 额度｜AI 日报 10.29**——带来源列表与时间戳，对「额度到底加在哪」讲得比多数快讯清楚：Pro 加的是 API 额度，不是登录式 Codex 额度。链接：[B站](https://www.bilibili.com/video/BV12msf6rERx)
- **NeuronXLab：Mistral Large 4 开放权重，Copilot Fusion 以约半价逼近 Opus 5.5**——给出单任务成本的直接对照：Copilot Fusion 5.59 美元，Opus 5.5 配 Claude Code 为 11.42 美元、高 2 分。链接：[B站](https://www.bilibili.com/video/BV1aRxF6dE6Q)
- **【AI 新闻速递】10 月 29 日**——短平快的播报，作者自己标注「由智能体自动整理，指标请自行判断」，正好当交叉核对用。链接：[B站](https://www.bilibili.com/video/BV1KNsf63Ep4)
- **No Priors：把编码智能体交给企业 IT——Serval 联合创始人 Jake Stauch**——讨论用确定性审批与审计轨迹来「既让所有人成为构建者、又不放开权限」，以及嵌入客户的工程师团队模式。这是 ServiceNow 的直接挑战者叙事。链接：[No Priors](https://feeds.megaphone.fm/nopriors)

---

## 灵感种子

> 以下是今日简报中值得进一步思考的灵感种子。

**「监督」需要一个能被审计的计量单位。** 86% 这个数字最刺人的地方，不是专家容易被影响，而是他们的工作方式在逻辑上是自洽的：带 AI 的一组严重错误率从 55% 降到 6%，速度快了半小时。既然查过程不划算、结果又更好，人就必然滑向只看结论。那么真正该设计的不是「让人多看一眼」，而是把分歧留下来——智能体在哪些决策点上和你意见不同、你改了主意、改的依据是什么。**可审计的应该是分歧记录，不是批准记录。** 这也意味着一类新产品：给智能体工作流做「判断日志」的工具，而不是又一个审批弹窗。

**算力正在变成准金融资产，而风险被推给了期限。** 英伟达给数据中心的「残值」做担保，等于承认芯片会贬值、房子还在；SpaceX 靠单一客户撑起三分之一营收；Anthropic 每月付 31 亿美元却握着 2027 年初的解约权。三者拼出来的结构有个共同点：**长期资产配短期承诺**。数据中心按十年摊销，合同却只锁到 2029 年、还留了退出口。如果明年有第二家新云倒下，市场第一个要问的可能不是「谁的需求不行」，而是「谁的折旧年限写得最乐观」。

**订阅制正在退化成额度包，这不只是定价技巧。** OpenAI 和 Anthropic 在同一周把「订了就能用」改成「订了就给你这么多」，再附赠等额 API 额度。对用户是好事，对厂商是一次身份切换：从卖席位变成卖产能，收入随用量波动，毛利随推理成本波动。**这意味着下一轮财报里，「订阅收入」这个词的意义会变**——它更像电信的流量包，而不是软件的席位授权。做 AI 采购的人值得现在就把「额度折算率」写进合同条款。

**国内大模型开始互相成为货架商品。** 豆包工作接入了 Kimi、GLM、DeepSeek，小米 MiMo 接入了 DeepSeek、GLM、Kimi、Qwen，全部按消耗倍率计费。模型厂商第一次以「SKU」而不是「对手」的身份出现在别人的产品里。这背后是分发权的转移：**当模型能力差不出身位，入口（办公套件、手机、终端）就成了定价方**。对创业公司，这意味着两件事——要么做入口，要么做那个被所有入口都愿意上架的模型；中间态最难活。
