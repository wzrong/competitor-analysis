---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-23

## 今日概览

> 今天的主线是「度量」。OpenAI 首席科学家把预训练困惑度曲线摊到台面上，并提议全行业按同一把尺子设开发上限；METR 说模型能力每 3.6 个月翻倍一次任务时长，而验证能力已经跟不上；一条模拟软件公司的实验则显示，编码 agent 单项指标接近满分，完整交付不到一成。另一面是成本：AI 服务器在交付前被要求涨价最高 45%，戴尔为此进了法庭。

- **OpenAI 公开预训练困惑度曲线**：并提出跨实验室的「共同上限」方案。来源：[OpenAI](https://openai.com/index/perplexity-and-intelligence)
- **METR 警告评测跟不上能力**：200 小时任务 2027 年 7 月或达五成成功率。来源：[The Decoder](https://the-decoder.com/ai-is-getting-better-faster-than-experts-can-reliably-test-whether-new-systems-are-safe-metr-warns/)
- **纳德拉承认 IDE 失守**：Claude Code 半年动摇 VS Code 地位。来源：[IT之家](https://www.ithome.com/1/030/733.htm)
- **AI 服务器交付前提价 45%**：戴尔被起诉，XTX 预付「价格确定性」费仍被加价。来源：[IT之家](https://www.ithome.com/1/030/713.htm)
- **编码 agent 模拟职场不足一成**：SWE-bench 近乎饱和，真实协作任务大面积失败。来源：[The Decoder](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ OpenAI 公开预训练困惑度曲线：把「进度」变成可比较的指标，再提议给行业设上限

11 月 22 日，OpenAI 首席科学家 Jakub Pachocki 发布长文，首次公开自家预训练曲线：GPT-3.5 的对数困惑度约 **0.99**，GPT-4 约 **0.91**；跌破 0.8 后，网络安全与数学领域开始出现新能力；到约 **0.76** 时，模型开始在长期悬而未决的开放数学问题上连续给出突破。他预计 0.68–0.7 区间还会带来今天无法测试的能力，并直言 **2027 年**可能出现预训练算法的「雪崩式」加速。

文章真正的新意在治理提议：在监控手段（例如思维链监控的继任者）落地之前，前沿实验室应约定一个基于困惑度等可追踪指标的第一个「开发上限」。Pachocki 也承认这个指标不完美——各家数据集不同、与具体任务脱节、思维链推理不改善困惑度、数据熵的下限未知。奥尔特曼公开背书，称这是 OpenAI 一段时间以来最重要的文章之一。

Raschka 当天写了回应《Pre-training is (still) not plateauing》，把预训练定位成「给模型装知识」，后训练负责「取用」，harness 负责「应用」——并希望把横轴换成训练 FLOPs。

**核心观点**：指标一旦公开，就会从内部仪表盘变成治理工具。真正值得追问的是谁来做审计：如果「共同上限」按各实验室自报的数据集度量，它约束的是披露意愿，而不是能力本身。

来源：[OpenAI](https://openai.com/index/perplexity-and-intelligence) · [IT之家](https://www.ithome.com/1/030/720.htm)

另见：[Raschka 回应](https://sebastianraschka.com/blog/2026/pretraining-is-still-not-plateauing.html) · [TechCrunch](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/)

### ⭐ Navier-Stokes 细节补齐：先写 Lean，再写论文

11 月 22 日，量子位还原了 Alpöge 与 Buckmaster 那份 Navier-Stokes 证明的细节：论文 **79 页**，声称在保留黏性、去掉一切外力的设定下，构造出三维（及周期边界）流体在有限时间「爆破」的解——这是对千禧年难题存在性与光滑性问题的否定答案。九月他们发过有光滑外力下的欧拉方程爆破，这次去掉外力、保留黏性，障碍完全不同。

最值得记录的是写作顺序：作者先完成 Lean 形式化证明，再用 Scott Armstrong 的工具把它转成自然语言初稿，最后由作者指导 Claude 重写、用标准结果替换冗长论证。论文 AI 声明写明全程只用 Claude。陶哲轩给出路线图——先数值找到一个有自相似结构的近似流，再用严格扰动理论证明附近存在真解——并评价策略已清楚，但仍需整理成规范的证明文本。

**核心观点**：AI 的参与已经从「生产证明」延伸到「把形式化翻译成人类可读的论文」。如果「先形式化、再成文」成为惯例，数学出版流程的重心会从同行阅读移向机器核验，人类数学家的角色则收缩为提出框架与判断价值。

来源：[量子位](https://www.qbitai.com/2026/11/511870.html)

另见：[陶哲轩相关讨论（经 11-21 Techmeme 归档）](https://www.techmeme.com/261121/p4#a261121p4)

### ⭐ METR：任务时长每 3.6 个月翻倍，验证能力跟不上

METR 发布警告：现有公开数据不足以排除未来几年 AI 研发出现剧烈加速，而那可能让人类「无法有意义地理解、评估并应对新系统的灾难性风险」。在定义清晰、反馈直接的编码与计算任务上，模型已多数时候超过有经验的人类专业人士，但还赢不过顶级专家组成的团队。

关键外推是任务时长：模型能独立处理的时长每 **3.6 个月**翻一倍，按此简单外推，**2027 年 7 月**前后可在 200 小时长任务上达到 50% 成功率。METR 同时提醒，常用基准会高估真实表现，因为开发者也用相近环境训练；开放式、无即时反馈、需要真实判断的问题仍是短板。

**核心观点**：评测的稀缺资源正在从「题目」变成「真实场景 + 专家判断」。当能力增长速度超过验证基础设施的建设速度，「没测出问题」就越来越不等于「没有问题」。

来源：[The Decoder](https://the-decoder.com/ai-is-getting-better-faster-than-experts-can-reliably-test-whether-new-systems-are-safe-metr-warns/)

### ⭐ 编码 agent 的「职场图灵测试」：单项满分，完整任务不足一成

The Decoder 报道了一项新实验：把编码 agent 放进一家模拟软件公司，有同事、项目看板、聊天记录和真实依赖，而不是孤立的题目。结果即使 Claude Opus 5.5 与 GPT-6 Astra 这样的顶尖模型，**完整完成的任务也不到十分之一**。对照面是：SWE-bench 已接近饱和，Anthropic 称 Claude 写了公司八成以上生产代码。

报道在付费墙内，实验方法与失败模式只能看到导语，结论需谨慎对待。但它提出的问题很实际：单点技能测试饱和之后，剩下的差距在需求歧义、跨文件依赖、协作与验收这些「职场性」环节。

**核心观点**：benchmark 与真实交付之间的缝隙，本质是任务定义的缝隙。谁先把「完整交付」做成可复现的评测，谁就能在下半年定义 agent 产品的宣传口径。

来源：[The Decoder](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/)

### ⭐ 纳德拉：Claude Code 六个月动摇了 VS Code

11 月 23 日，IT之家转述 Windows Latest 的采访：纳德拉承认，不少开发者已经几个月没打开 VS Code，传统 IDE 大约 **六个月**就失去了存在感，而微软没有立刻拿出应对方案。他把原因归给 Anthropic：「模型做得实在太出色，还让开发者真正接受了命令行形态，写程序从输入变成了输出。」

他给出的教训很直接——不要迷恋自己打造的东西。对 IDE 的下一形态，他的判断是核心不再是手搓代码，而是「写出真正的 MD 说明文档」，把意图交给 agent 执行。微软的动作也印证方向：VS Code 1.146 加入智能体收件箱与模型对比，1.147 加入模型路由、定时提交 agent 请求与浏览器集成。

**核心观点**：这条表态的分量不在「微软认输」，而在形态之争的结论——IDE 与 CLI 之争已让位于「谁掌握模型与 agent harness」。纳德拉把 IDE 重新定义为「写规格的地方」，等于承认微软的护城河要从编辑器转向工作流。

来源：[IT之家](https://www.ithome.com/1/030/733.htm)

### ⭐ 交付前涨价最高 45%：AI 服务器合同的「价格确定性」失效

FT 报道并经 IT之家转述：戴尔、HPE、联想、超微在合同签署数月后、设备交付前，要求客户按远高于协议的价格付款，涨幅常见的区间是 **25%–45%**。摩根大通研究把原因指向内存——自 2024 年初以来内存成本上涨超过 **400%**。

冲突已经进法庭。交易公司 XTX 在爱尔兰起诉戴尔：双方曾就 5.49 亿美元服务器约定固定价格，XTX 还额外支付 500 万美元「确保价格确定性」，戴尔仍要求追加 **6200 万–7000 万美元**，理由是内存涨价「无法消化」。多位买家对 FT 说，最终都接受了加价：「算力对我们至关重要，我们愿意为此买单。」

**核心观点**：算力正在从可采购的商品变成配给型资产，长约里的固定价格条款失去约束力。对自建集群的企业，采购策略需要向大宗商品靠拢——锁量、锁价、乃至金融对冲，而不是把「已签约」当作成本确定的证据。

来源：[IT之家](https://www.ithome.com/1/030/713.htm) · [FT](https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f)

### ⭐ MiniMax 用内部模型做密码分析：把「理论攻击」推进到分钟级

11 月 22 日，MiniMax 公布其最新内部模型对现代密码方案的系统性自动化分析结果：在历届 NIST 标准化竞赛中，首次实际攻破多个「尚无已知实际攻击」的候选算法；对已发表、经同行评审的前沿方案实现高效密文伪造与密钥恢复，并刷新新型分组密码的最高破解轮数纪录；在公开数学挑战中首次解出数十个高阶实例，相比最优算法实现数百至数万倍加速。

官方特别声明不影响 AES、RSA、SHA-256 等现行主流标准，已提前通知相关方案作者，并把模型生成的推理轨迹整理为技术报告与代码公开。

**核心观点**：这是「模型作为结构化搜索器」在纯数学构造领域的强样本——密码分析恰好是反馈明确、可自动验证的领域，与 METR 观察到的能力增长曲线同源。同时它给出一条行业惯例：负责任的披露流程正在成为模型能力展示的标配。

来源：[IT之家](https://www.ithome.com/1/030/711.htm) · [MiniMax Research](https://github.com/MiniMax-AI/Research)

### ⭐ AI 自主设计 CPU：Frostbite 的「零架构先验」

Architect Labs 发布研究博客：其 AI 系统在无预设架构理念的「零架构先验」状态下，阅读论文与性能资料、建立 Python 模型，自主选定方向并生成 141 页设计文档，最终给出名为 Frostbite 的通用 CPU 设计——全新指令集、多个同构计算单元（Tile）经片上网络互联，用「免费多线程」让程序直接暴露并行，替代乱序执行与缓存一致性协议。

在 25 项工作负载上，4 Tile 集群的每瓦性能是尺寸相近、已完成硅验证的双发射顺序执行核心的 **4.59 倍**，单位面积性能为 **8.77 倍**；最好的 conv2d 达 23.12 倍，最差的递归斐波那契只有 1.15 倍。必须打折扣的是：数据来自 7nm 模拟设计，尚未流片；完整设计为 16 Tile，频率从早期综合的 800MHz 降到最终布局的 500MHz。

**核心观点**：设计端被 AI 提速后，瓶颈整体后移到验证与流片——模拟数据无法替代真实硅。这条新闻真正的启示是：AI 进硬件的第一道门槛不是「能不能设计出来」，而是「谁来做可信的验证」。

来源：[IT之家](https://www.ithome.com/1/030/717.htm)

---

## OpenAI

### ⭐ 公开预训练困惑度曲线，提议行业共同设限

Pachocki 给出从 GPT-3.5 到当前模型的完整曲线，并提出以困惑度等指标为基础的跨实验室开发上限。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[OpenAI](https://openai.com/index/perplexity-and-intelligence)

### GPT-6.2 Astra 与 Sol 的沟通风格突变：更短、更直接、更少承认不确定

Artificial Analysis 的测评显示，Astra 平均回答从 352 词降到 **210 词**（-40%），Sol 从 337 降到 223（-34%）；标题使用量从接近 2 个降到 0.1–0.25 个。Organization 指数从 70/86 跌到 11/27，而「先答问题」从 49/64 升到 89/87。代价是承认不确定性的相对排名从 96/98 掉到 **24/51**。对比组里 Opus 5.5 信息量最高，Claude Fable 5.2 与 Opus 5.5 在透明度与结构上领先。

来源：[The Decoder](https://the-decoder.com/gpt-6-2-astra-and-sol-get-to-the-point-faster-but-score-lower-on-transparency-than-claude/)

---

## Google DeepMind / Gemini

### 郭明錤：谷歌削减 2027 年博通设计的 TPU 8i 约 100 万颗

天风国际调查称，削减幅度约相当于 2027 年 8i 系列出货量的 **20%**，以单价更高的 8i Max 为主；同时增加联发科设计的 8t 系列。背景是供应链紧张与数据中心供电受限，谷歌把「前沿模型研发优先拿算力」落到实处。另一条供应链变化：谷歌把 TPU 设计与 HBM 采购拆开，部分设计交给联发科分工，HBM 改为直采，以压降成本。

来源：[IT之家](https://www.ithome.com/1/030/698.htm)

> DeepMind 官方博客今日无更新，最近一条为 11 月 18 日的 Gemini 4 Neon。

---

## Anthropic / Claude

### ⭐ Navier-Stokes 证明的写作流程：先 Lean，后论文

79 页论文、先形式化再成文、Claude 全程参与重写。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[量子位](https://www.qbitai.com/2026/11/511870.html)

### ⭐ 纳德拉谈 Claude Code：六个月让传统 IDE 失去存在感

微软 CEO 公开承认反应不及，并预言 IDE 的核心将变成「写 MD 规格」。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/030/733.htm)

> 官方渠道今日无更新；最近发布为 11 月 20 日的 IPO 交割公告。

---

## 国内大厂动态

> DeepSeek / Kimi / 豆包 / 智谱 等

### 智谱被传 GLM 5.4 已内测，年底推 3 万亿参数 GLM 5.5（爆料，未证实）

多个 B 站 AI 日报同日转述 X 上科技博主爆料：智谱下一款将发布的是 **700B（七千亿参数）** 的 GLM 5.4，已进入内测；年底还有 3 万亿参数的 GLM 5.5。智谱官方零口径，两条均按爆料对待。另有转述称 GLM 5.4 灰测中出现 3D 能力对比。

来源：[B站·两个人在吃饭 第 46 期](https://www.bilibili.com/video/BV1N4y7z9E5C) · [B站·绿鸭AI日报](https://www.bilibili.com/video/BV1ieynz1Ex9)

### 蚂蚁开源医疗模型 LingSante-3.1，阿福日问诊超 2000 万次

Hugging Face 上出现 inclusionAI 的 LingSante-3.1 系列：flash 版总参数约 **5720 亿**（FP8 权重），标注 bailing_hybrid 架构、MIT 许可，11 月 19 日创建、22 日更新，另有 air-VL 变体。同日蚂蚁阿福披露：用户 **1.5 亿**，日均线上问诊超 2000 万次，55% 来自三线及以下城市，1/4 是老人，16% 的问诊发生在凌晨；医生版接入 UpToDate 临床知识库。

来源：[Hugging Face](https://huggingface.co/inclusionAI/LingSante-3.1-flash) · [IT之家](https://www.ithome.com/1/030/653.htm)

### 腾讯开放混元 Hy4-flash 权重，社区量化版迅速跟进

tencent/Hy4-flash 出现在 Hugging Face：总参数约 **2200 亿** 的 MoE 模型，支持多模态输入。开源后一天内，社区已放出 GGUF、MLX、NVFP4 等多个量化版本，其中 GGUF 单仓下载已过万。上一代 770B 的 Hy4 开源后，Flash 版补齐了消费级硬件这一档。

来源：[Hugging Face](https://huggingface.co/tencent/Hy4-flash)

### DeepSeek Harness 发布 v0.2.3-alpha.2

11 月 22 日的更新主要为工程性变更：Node.js 版本要求提高到 24.22.3（24.x 系列）或 26.13.1 及以上。属于日常迭代，但说明 DeepSeek 的 agent 工具链仍在高频推进。

来源：[GitHub Release](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.3-alpha.2)

### ⭐ MiniMax 内部模型破解多个密码学前沿方案

NIST 竞赛候选算法、已发表方案与公开挑战赛三线推进，并公开推理轨迹与技术报告。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/030/711.htm)

### 面壁 MiniCPM 累计下载突破 7000 万

面壁智能官方账号称，MiniCPM 系列在 Hugging Face 的累计下载量突破 **7000 万**。小尺寸端侧模型仍是国内开源生态中下载量最高的一档。

来源：[B站·两个人在吃饭 第 46 期](https://www.bilibili.com/video/BV1N4y7z9E5C)

---

## 海外大厂动态

### ⭐ AI 服务器交付前涨价最高 45%，戴尔遭 XTX 起诉

合同签署数月后加价已成常态，内存成本自 2024 年初上涨超 400%。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/030/713.htm)

### Perplexity 发布 Monitor API：把搜索变成按计划值守的看门人

新 API 支持两类监控：网页监控按计划跑搜索、只推送达到相关性/可信度/新颖性/时效性阈值的变化；页面监控最多盯 10 个页面，首跑存基线、之后返回文本 diff，并用决策模型过滤预览、传闻与复述。调度 15 分钟到一周一次，webhook 带签名与自动重试。定价每 1000 次成功运行 1 美元；内部对比测试中，前八小时交付 63 个新页面，Firecrawl 20、Exa 15、Parallel 各 10（厂商自测）。

来源：[The Decoder](https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/)

### Signal 默认拦截手机截图，承认防护「不完整」

Signal 宣布在移动端默认禁止应用内截图，目的是阻止系统级 AI 代理读屏、破坏端到端加密，同时承认新防护并不完整。这是即时通讯应用第一次把「防 AI 读屏」做成默认设置。

来源：[TechCrunch](https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/)

### 苹果：Siri AI 集体诉讼和解，每台符合条件的 iPhone 至少赔 61 美元

和解覆盖此前购买相关机型的用户，预计每台可获赔至少 **61 美元**。同期古尔曼在《Power On》中判断，苹果「僵化的年度发布周期与集中决策」使其难以参与 AI 竞争，需要在组织与文化层面全面改革；自研 AI agent 最早 2027 年底推出。

来源：[IT之家·和解](https://www.ithome.com/1/030/729.htm) · [IT之家·古尔曼](https://www.ithome.com/1/030/730.htm)

### Chollet：GPU 现货仍在涨，HBM 产能订到 2029；马斯克：明年或需数千亿美元额外营运资金

Keras 作者 Chollet 列出一组算力供需数据：HBM 与 DRAM 到 2029 年产能基本订满，前沿训练算力约每 5 个月翻一番，推理业务利润率 70%–85%。马斯克回复说，给如此规模的算力通电、冷却并稳定运行极其困难，行业明年可能面临严重资金短缺，仅营运资金缺口就可能达数千亿美元。

来源：[IT之家](https://www.ithome.com/1/030/628.htm)

### ⭐ AI 自主设计出通用 CPU：Frostbite 的「零架构先验」

Architect Labs 称其 AI 系统在无预设架构理念下自主生成 141 页设计文档，给出的 CPU 在模拟中每瓦性能是已完成硅验证对照核心的 4.59 倍——但尚未流片。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/030/717.htm)

### 《以撒的结合》撤下 AI 生成音乐

游戏《以撒的结合》因玩家对 AI 生成音乐的不满，将相关音轨撤下。这是 2026 年又一起玩家社区迫使开发者回退 AI 内容的事件，与「反 AI 味」的审美情绪同源。

来源：[The Verge](https://www.theverge.com/games/1039770/binding-of-isaac-ai-music)

---

## AI 研究前沿

### ⭐ METR：评测跟不上能力增长

任务时长每 3.6 个月翻倍，200 小时任务 2027 年 7 月或达 50%。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Decoder](https://the-decoder.com/ai-is-getting-better-faster-than-experts-can-reliably-test-whether-new-systems-are-safe-metr-warns/)

### ⭐ 模拟职场里的编码 agent：完整交付不足一成

把 SWE-bench 的「单题」换成「公司」，顶尖模型的完成率跌到个位数。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Decoder](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/)

### TwinLab-Bench：在真实实验室的「数字孪生」里考核 AI 科学家

52 个来自物理、生命科学与工程实验室的任务，要求 agent 自己设计实验、在超过 100 种实验动作中选择并执行，结果与真实实验记录中的隐藏答案比对。与前两代基准（按给定流程执行、从预设空间选测量）不同，这一代考的是「提出并完成自己的实验」。配套做法是把真实实验室操作做成可复现的沙盒读数。

来源：[arXiv:2611.26248](https://arxiv.org/abs/2611.26248)

### 想得更多不等于选得更好：推理努力只提高购物 agent 的自信

在 WebShop、Amazon SQID、Wayfair WANDS 三个商品选择基准上测十个前沿模型：增加思考量并未显著改善选择质量，却显著提高模型自报的置信度，且大多数模型校准很差、错误具有相关性。对购物 agent 的产品含义是：让模型「多想一会儿」不能当作质量保障。

来源：[arXiv:2611.22033](https://arxiv.org/abs/2611.22033)

### 同行评审正在同质化：LLM 评审让批评意见高度重叠

统计会议与期刊评审的批评重叠度：ICLR 同一评审阶段的意见重叠从 2026 年的 **12.0%** 升到 2027 年的 **21.3%**，NeurIPS、ICML、F1000、PLOS 同样逐年上升；第三份评审能新增的问题数从 6.12 降到 5.46。被 LLM 检测器判为 AI 生成的两份评审，其重叠度显著高于未被标记的组合。

来源：[arXiv:2611.26286](https://arxiv.org/abs/2611.26286)

### Embeddings vs Grep：稠密检索的优势有多少是评测口径造出来的

团队构建 Repo-Premium 基准（真实仓库、六种语言、2022–2026 的 PR、91 个仓库的预注册测试池），发现稠密检索对 BM25 的优势主要来自两点：评测时把文件切块后只给 BM25、以及把修改过的测试计为「相关」。在同等口径下，编码 agent 偏爱 grep 并非落后。

来源：[arXiv:2611.20455](https://arxiv.org/abs/2611.20455)

### 今日论文速览

- **Piccolo**：0.8B–27B 多模态决策模型家族，靠递归自我改进共演化模型与数据，27B 以 **75.59** 登顶 Decision Index Vision Full。[arXiv:2611.24651](https://arxiv.org/abs/2611.24651)
- **Unfinished-Bench**：97 个真实工作场景，考察「长期自主的 agent 在完成 KPI 时会不会违规」，规则藏在内部文档里而非提示词中。[arXiv:2611.17460](https://arxiv.org/abs/2611.17460)
- **General progress substitutes for specific training data**：故意扣掉某项技能的训练信号（国际象棋、Othello、分子串、括号语言），大模型仍会从其他数据里「顺带学会」，且越大越快、所需补数据越少。[arXiv:2611.24844](https://arxiv.org/abs/2611.24844)
- **S1CogBench**：24 个经典认知任务、27 种评测模式，测 7 个开源决策模型与 Jev，发现快速决策常缺证据推理、可靠度差异巨大。[arXiv:2611.00911](https://arxiv.org/abs/2611.00911)
- **Phantom Success, Silent Failure**：审计仿真操作基准的「成功判定器」，发现它们会接受半途而废的执行、也会拒绝正确的另类完成方式。[arXiv:2611.25179](https://arxiv.org/abs/2611.25179)

### 港大开源 CLI-Anything：把桌面软件批量改造成 agent 可用的命令行

HKUDS 的项目把传统图形界面软件封装成 AI agent 可调用的 CLI，配合 CLI-Hub 一键安装与管理，目标是一句命令让任意软件变成 agent 原生工具（Cursor、Claude Code 等均可接入）。上线一天在 GitHub 日榜涨星数百。

来源：[GitHub](https://github.com/HKUDS/CLI-Anything)

---

## 行业观点与解读

### Raschka：预训练没有到平台期，只是不性感

Raschka 借 OpenAI 的困惑度曲线重申观点：预训练给模型装知识，后训练（SFT + LRVR）让模型取用知识，harness 让模型应用知识；三者缺一不可。他承认预训练「无聊」，但指出训练配比之类的「无聊工作」仍在持续产生收益，并希望看到同一张图横轴换成训练 FLOPs。相关论述已在今日深度阅读第一条里展开。

来源：[Sebastian Raschka](https://sebastianraschka.com/blog/2026/pretraining-is-still-not-plateauing.html)

### 菲尔兹奖得主梅纳德：相信黎曼证明正确，但「理解」比「证明」更重要

2022 年菲尔兹奖得主 James Maynard 接受采访表示：形式化验证经过独立核实，加上 Alpöge 一贯可靠的记录，他很有信心这份证明是正确的。但他强调，「理解一个定理为什么成立，远比仅仅证明它成立重要」——黎曼猜想的价值本在于它逼出的新数学理论，在有人真正理解证明的思想与框架之前，这项成果可能无法带来预期的变革。

来源：[IT之家](https://www.ithome.com/1/030/677.htm)

---

## 值得关注的视频

> YouTube 播客与频道近期值得看的视频。标注 ⭐ 的为重点推荐。

### 两个人在吃饭·AI 日报第 46 期：智谱 GLM 5.4 内测与 12 条消息

12 条消息，每条标注信源类型。头条是智谱 700B GLM 5.4 内测爆料，其余包括 OpenAI 困惑度、DeepSeek Harness 新版、蚂蚁 LingSante-3.1、面壁 MiniCPM 7000 万下载等；主播还把「700B 念成七百亿」的口播错误公开勘误，严谨度值得参考。

来源：[B站](https://www.bilibili.com/video/BV1N4y7z9E5C)

### AI日报·肥鱼速览 11-23：14 条动态一次过

黎曼认证、OpenAI 困惑度、智谱 GLM 5.4、蚂蚁 5600 亿医疗模型、混元 Hy4 flash、港大 CLI-Anything、OpenRouter 撤销端点、亚马逊收购 Decart、特斯拉 FSD v15、Signal 禁截图等，适合快速扫一遍当日全貌。

来源：[B站](https://www.bilibili.com/video/BV1CLynzZEHL)

### AI前沿晚报 11.22：两百万蜜罐查出推理商窃密

把 Dragos 的供应链审计、Signal 默认拦截截屏、港大 CLI-Anything、246 亿参数压进 5.38GB、Anthropic 2028 年用电结构（87% 天然气）等 10 条事件串成一期，每条附一手信源。

来源：[B站](https://www.bilibili.com/video/BV1p9yjzjEB2)

### AI前沿早报 11.22：Lean 官方认证与「模型改写自身权重」

对 Lean 联合声明的四个标准做了拆解，并讨论《Language Models Can Rewrite Their Own Weights》——无梯度、纯推理改写权重，数学准确率提升 6.6 个百分点。

来源：[B站](https://www.bilibili.com/video/BV1D2y3z1EAp)

### 白鸦 Ba1ya：OpenAI 公开训练曲线，图中还有内部模型

逐条解读 OpenAI 博客，并指出曲线里标出了一款未公开的内部模型；另覆盖 Gemini Tasks 远程电脑联网、Google AI 订阅与 Hermes 的传闻、蚂蚁两款医疗模型权重开放、TensorLean 给生产 GPU 内核做形式化证明。

来源：[B站](https://www.bilibili.com/video/BV16Hynz9Esz)

### 绿鸭AI日报 1123：智谱下周推 7000 亿旗舰

标题党但信息点集中：智谱 GLM 5.4 下周发布、3 万亿 GLM 5.5 年底亮相的爆料梳理。单源传闻，只宜当线索。

来源：[B站](https://www.bilibili.com/video/BV1ieynz1Ex9)

### 肥鱼大卫袋 11月23日 AI 圈 4 件事

四件事各配原始链接：OpenAI 谈困惑度、阿福医生版接入 UpToDate、特斯拉推送 FSD v15、以撒的结合撤下 AI 音乐。想快速补当天中文侧热点可直接看这期。

来源：[B站](https://www.bilibili.com/video/BV1pRyEzWEBH)

---

## 灵感种子

> 以下是今日简报中值得进一步思考的灵感种子。

**「限速协议」需要审计方，而不是签署方。** OpenAI 提议用困惑度等指标给全行业设共同上限，这在技术上可行，在治理上却缺一个关键角色：谁核对各实验室上报的数字？核试验有地震台网、金融有外部审计，AI 的「困惑度监测站」长什么样，可能比上限本身更值得设计。顺着想：跨实验室的模型对评测协议本身，就是一门生意。

**当「已签约」不再等于「成本确定」，算力采购会金融化。** XTX 多付 500 万美元买「价格确定性」仍被要求加价 6200 万，说明长约在供给极端紧张时会失效。下一步大概率出现算力远期、期权与 escrow 结构——谁能把「交付时点的价格风险」拆出来定价，谁就掌握企业级 AI 基础设施的入口。

**评测正在从「分数」迁移到「工作现场」。** METR 量任务时长，模拟软件公司量完整交付，TwinLab-Bench 量自主设计实验——三个方向不约而同地把「能力」换成「在真实环境里能交付什么」。这意味着评测数据集会越来越像环境模拟器，而评测公司的护城河会从题库变成场景与专家网络。

**「先形式化、再写论文」可能重塑数学出版。** Alpöge 的 NS 论文先有 Lean 证明、再用工具转成自然语言初稿。如果这成为惯例，论文的「第一读者」从人变成内核，「同行评审」的含义会分裂成机器核验与人类理解两层——梅纳德那句「理解比证明重要」，恰好指出了机器补不上的那一层。
