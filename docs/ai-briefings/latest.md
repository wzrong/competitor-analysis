---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-27

## 今日概览

> 今天的主线是「时间表被外力改写」。路透拿到智谱与月之暗面的延期细节，英伟达把停发范围从中国扩到新马泰印尼；另一边 AI 攻数学还在加速，Aaronson 写下「我第一次从骨子里觉得 P≠NP 不远了」，381 个 agent 把 P vs NP 搬上了公开直播。工程侧则出现一条反直觉的省钱路径：腾讯把草稿模型挂到目标模型已经算过的稀疏位置上，单项最高快 4.2 倍。

- **智谱 GLM-5.5 或延至 2027 年一季度，Kimi K4 或延至年中**：据路透，管制与反蒸馏正在改写发布日历。来源：[The Decoder](https://the-decoder.com/after-openai-and-anthropic-shut-the-door-on-their-data-a-chinese-ai-developer-is-turning-to-google-and-meta-instead/)
- **英伟达停止向马来西亚、新加坡、泰国、印尼发运服务器**：管制从目的地转向转口枢纽。来源：[The Decoder](https://the-decoder.com/nvidia-halts-server-shipments-to-malaysia-singapore-thailand-and-indonesia-after-tighter-us-export-controls/)
- **Aaronson：ω 被钉死之后，P≠NP 也许不远了**：并称 AI 实验室手握未公开的「密码学炸弹」。来源：[Shtetl-Optimized](https://scottaaronson.blog/?p=10379)
- **腾讯混元开源 DFly2**：不换模型权重、不改输出，Hy4 flash 单项最高提速 4.2 倍。来源：[IT之家](https://www.ithome.com/1/032/929.htm)
- **SpaceX Starmind 获 FCC 批准**：最多 100 万颗算力卫星，2040 年达标。来源：[The Verge](https://www.theverge.com/science/1042278/spacex-fcc-starmind-ai-space-data-centers)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ 下界才是分水岭：Aaronson 说「P≠NP 不远了」，还提到未公开的密码学炸弹

Scott Aaronson 11 月 26 日发博客，复盘这两周被他称为「数学末日」的一连串结果。他先讲矩阵乘法：OpenAI 给出的 ω 恰为 **9/4** 是一个下界，与 10 月的上界对上——而 ω 的正确答案居然是个有理数。更让他意外的是 AI 能证出 ω>2 这种形式的下界，他原本以为这不会比 P≠NP 容易多少。

同批还有傅里叶变换：所需线性门数的真值是 N(log N)^{1/2+o(1)}，既有上界也有匹配下界，同时超过 1960 年代以来 O(N log N) 的 FFT。他反复强调差别——上界只是刷新记录，**下界才宣告天花板在哪里**。

他还给了一个横向对照：Yupan Liu 关于 QIP(2)=PSPACE 的预印本若放在 2025 年会是年度最重要的复杂性结果，如今 AI 参与其中都没人抬头。他自己的判断写得很直白：「我现在从骨子里第一次觉得，**P≠NP 的证明不远了**。」并称从多个可靠来源听说，AI 实验室里躺着一个或多个能攻破现役密码系统的算法突破。

**核心观点**：真正的新闻不是某个常数，而是「证明」开始批量产出且自带 Lean 证书——公司连新闻稿都省了，直接把论文传上 GitHub。这让「宣称」变成了「可审计」，也让下界这种过去几十年只增几行的文体，第一次有了工业级产能。同时要留一分冷静：所有这些都是未经同行评审的预印本。

来源：[Shtetl-Optimized](https://scottaaronson.blog/?p=10379) · [The Decoder](https://the-decoder.com/former-openai-researcher-says-the-riemann-proof-matters-less-than-the-fact-that-an-ai-system-can-produce-it/)

### ⭐ 腾讯混元开源 DFly2：不换模型，把草稿模型挂到目标已算过的位置上

11 月 26 日，腾讯混元开源新一代草稿模型 DFly2，定位是挂在 Hy4 flash 旁边的加速组件：**不改权重、不改输出**，只把出字速度提上去。官方口径是在 19 个公开评测集上，接收长度与加速比整体优于 DFlash 与 DSpark；相对 DSpark，长文与 Agentic 场景的平均加速比分别高约 **12% 与 30%**，单项最高 **4.2 倍**。

机制是整套里最值得抄的部分。DFly2 让每个 draft 层直接复用目标模型稀疏注意力层的 KV cache（KV Share），并复用其 indexer 为当前 query 选出的至多 **2,048 个位置**（Index Share）。由此带来三个工程后果：每个 draft token 最多只看约 2K 个 key，注意力复杂度与上下文长度脱钩；drafter 不再单独维护 KV cache，零额外显存；PD 分离时预填充不参与，P 到 D 只多传一个末层隐状态。

配套是完整的：权重、训练代码、技术报告一并开放（arXiv **2611.34776**，GitHub 上叫 AngelSpec），并顺带为 DeepSeek-V4.1-Flash 与 GLM-5.3-Flash 各出了一个草稿模型。与开源模型自带的 DSpark 相比，Agentic 与真实任务场景的接收长度还领先 10.4%。

**核心观点**：推测解码的成本大头一直是 drafter 自己的 KV cache，DFly2 的思路是「目标模型已经为每个 query 选好了位置，草稿不要重算一遍」。这把加速从「更大的模型」转成「不再重复付费」，是今年最容易被其他推理栈复制的优化范式。

来源：[IT之家](https://www.ithome.com/1/032/929.htm) · [arXiv](https://arxiv.org/abs/2611.34776) · [GitHub](https://github.com/Tencent/AngelSpec)

### ⭐ 智谱 GLM-5.5 或延至 2027 年一季度，Kimi K4 或延至年中

路透援引知情人士称，智谱约 **3 万亿参数**的旗舰 GLM-5.5 已错过 11 月的发布窗口，可能推迟到 2027 年一季度或更晚，原因指向美国芯片管制与各家实验室的反蒸馏收紧。为填补空档，智谱本周一已发布 7,500 亿参数的 GLM-5.4，并称新设计能对标 2 到 3 万亿参数的对手。

月之暗面的处境更具体：失去境外算力后，其开发周期可能从 6 个月拉长到 12 个月，Kimi K4 或推迟到 2027 年年中；报道称该公司正转向 Google 与 Meta 的最新模型来获取训练信号，同时在欧洲寻找算力。此前已知的传导链条是：云漏洞被堵、英伟达停发东南亚四国、反蒸馏措施生效。

对立面也存在。B 站UP主「白光star」11 月 27 日的日报称「GLM-5.5 延期是老外造谣，上万张国产卡进展顺利」，这条说法**未获官方或独立信源证实**，但与路透的匿名信源形成可供对照的两端。

**核心观点**：管制的传导已经走到「发布日历」这一层。真正被削掉的不是显卡数量，而是「用美国云 + 用美国模型输出」这条低成本捷径。延期多久，取决于各家自建 RL 数据与国产卡适配的积累速度——这两件事都比囤卡慢得多。

来源：[The Decoder](https://the-decoder.com/after-openai-and-anthropic-shut-the-door-on-their-data-a-chinese-ai-developer-is-turning-to-google-and-meta-instead/) · [B站·白光star](https://www.bilibili.com/video/BV1ug1JzTEkq)

### ⭐ 英伟达停止向东南亚四国发运服务器：管制从「目的地」转向「转口枢纽」

FT 报道并经 The Verge、The Decoder 转述：英伟达已指示 **Dell、Supermicro** 等制造伙伴停止向马来西亚、新加坡、泰国与印尼发运服务器与芯片，等待收紧后的出口规则明确。此前停发的对象只有中国。

背景是 **11 月 16 日**的美国新规，试图堵住中国公司通过境外数据中心远程使用高端芯片的路径。同期有两条反向线索：CBS 调查称英伟达把最先进芯片卖给至少两家**中资背景的加州公司**，其中部分被转租或转售到亚洲；荷兰政府表示将抵制美国拟议的 Match Act（限制 ASML 对华销售），ASML CEO 也公开警告断供会加速中国自研。

**核心观点**：管制的手已经从「卖给谁」伸到「从哪里转手」，东南亚的算力中转角色被切断。但同一周盟友层面的公开反对说明，规则越细，执行摩擦越大——最终受损的可能是美国厂商自己的区域交付能力。

来源：[The Verge](https://www.theverge.com/ai-artificial-intelligence/1043079/now-nvidias-stopped-sending-chips-to-southeast-asia-too) · [The Decoder](https://the-decoder.com/nvidia-halts-server-shipments-to-malaysia-singapore-thailand-and-indonesia-after-tighter-us-export-controls/)

### ⭐ 381 个智能体公开直播攻关 P vs NP：2,400 条引理、800 条证伪、0 条指向 P=NP

11 月 22 日，设计软件公司 Brilliant 的联合创始人 Amichai Mantinband 上线 pequalnp.com，把一批 AI 智能体放进同一个公开仓库，24 小时直播攻关 P vs NP。到 25 日早 9 点：峰值 **381 个**智能体并发，累计 10,936 次会话，Lean 4 里验证通过 **2,400 多条**引理；另有 465 个外部 agent 提交、独立证明 1,659 个步骤。

组织方式值得细看。整个问题被拆成 **6 条**并行战线，由 **30 个**被称为「席位」的调度器分管，每个席位下带一组子智能体。流程是两步：思考型 agent 先检索文献、推演路线、找反例，经得起推敲的思路才交给构建型 agent 写成 Lean 4 送进沙盒编译；另设红队专门挑刺与核对语义，官网还有一页「墓地」归档被彻底证伪的 800 多条主张。

基建先撑不住了：仓库三天破 **2,000 fork**、900 多名贡献者、1,028 个开放 PR、累计关闭 4,768 个，GitHub 并发队列被堵，迁入付费组织后 Actions 每次只能跑 6 个任务。截至 25 日的看板：已验证引理 2,456，总引理却涨到 5,934；带明确倾向的有 253 条指向 P≠NP，指向 P=NP 的仍是 0 条；主线收敛到「不含 NOT 门的单调电路猜想」，暂时无法推广到一般电路。

**核心观点**：这是一次公开的「科研工程化」演示——给每条引理设 PR、超时与红队，把猜想变成流水线。它也照出了真正的瓶颈：编译器只保证形式化后的命题被证明，管不了它和自然语言命题是不是一回事；分母跑得比分子快，说明拆解本身在制造新问题。

来源：[量子位](https://www.qbitai.com/2026/11/513021.html)

### ⭐ FCC 批准 SpaceX Starmind：最多 100 万颗算力卫星，2040 年达标

FCC 周三宣布，授权 SpaceX 部署最多 **100 万颗**搭载 AI 芯片的卫星，组成「Starmind」星座，用于在轨处理 AI 数据。这是该机构首次批准完整规模的「AI 卫星星座」，Google 与 Blue Origin 也在推进类似想法。批准附带条件：2033 年前至少部署一颗，2040 年达到百万颗。

细节上，SpaceX 计划用高速激光把这些卫星接入 Starlink 回传数据，芯片在规划中的 **Terafab** 工厂生产；FCC 驳回了把 600 公里以上失效卫星送入「墓地轨道」的请求，理由是处置方案信息不足。Google 上月已发射首颗「Project Suncatcher」AI 服务器卫星，Blue Origin 将在 **2029 年**承接其首次专用重载发射。

**核心观点**：卖点是「在太空收集太阳能给地面的 AI 供电」，但被批准的实质是一条跨越 14 年的工程时间表。对算力叙事的意义在于，它试图把「能源约束」从地球上的电价与审批里挪走一部分——代价是把运维难度挪到了轨道上。

来源：[The Verge](https://www.theverge.com/science/1042278/spacex-fcc-starmind-ai-space-data-centers) · [The Decoder](https://the-decoder.com/fcc-clears-spacex-to-deploy-up-to-1-million-starmind-satellites-for-orbital-ai-data-centers-by-2040/)

### ⭐ Anthropic 开始发放 15 亿美元版权和解金：每本书约 3,000 美元

小说家 Courtney Milan 在 Bluesky 上表示，已收到 Anthropic 和解金中属于自己的部分。这笔 **15 亿美元**是去年为集体诉讼达成的和解，全额折算约为每本书 3,000 美元，还有一部分将在明年初发放。经 The Verge 与 The Decoder 转述后成为可引用的定价基准。

**核心观点**：这是第一次为「训练数据里的每一本书」标出可对标的单价。对所有仍打算「先训练、后谈判」的公司，3,000 美元/本从此就是谈判桌上的起点价；对作者而言，它把一个抽象的权利主张变成了可预期的现金流。

来源：[The Verge](https://www.theverge.com/ai-artificial-intelligence/1043087/anthropic-has-started-paying-out-its-copyright-settlement-to-authors)

### ⭐ MoonBit 1.0：为智能体设计一门语言，同一个模型少花 12% token

IDEA 研究院在第六届 IDEA 大会上发布 MoonBit 1.0。项目 2022 年 10 月立项，恰是 ChatGPT 上线前一个月，定位对标 Go 与 Java 的通用语言，但为 agent 编程做了三处专设：原生 Wasm 语言级沙箱，微秒级启动；把编程语言与形式化逻辑融合，生成代码时同时给出正确性证明，甚至可验证到编译后的汇编；编译效率在数百包的测试中约为 Rust 的 **1/10**。

最硬的证据是一组对照实验：让 Opus 5.5 分别用 MoonBit 与 Rust 写数据库引擎，三轮约 500 项测试，通过率接近，而 MoonBit 少消耗 **12%** 的 token——要知道模型里 MoonBit 的语料规模只有 Rust 的 **1%**。

生态数据也给了：近半年包下载接近 **1,000 万次**（最近一个月约 300 万），生态库从年初约 2,500 个增至 **3.6 万** 个；团队用 MoonBit 写了 88 万行的 Office 文档处理工具，体积仅 17MB，百万行级增量编译 1 到 2 秒。沈向洋在会上给了个分层判断：全球约 10 亿人用过大模型，约 2,000 万人在数学与编程里真正使用，而了解前沿 AI 有多强的可能只有 5,000 人。

**核心观点**：当写代码的主力从人变成 agent，「语言该为谁优化」第一次有了实证答案——为 agent 设计的语言能让同一个模型更省 token、更少出错。这也解释了为什么形式化验证会从研究课题变成语言特性：它同时是给机器的约束和给人的验收单。

来源：[量子位](https://www.qbitai.com/2026/11/512840.html)

---

## OpenAI

### GPT-6.2 计费修正：Astra 触顶快 40%、Sol 快 25%，补发一次额度重置

OpenAI 修复了 GPT-6.2 上线初期的计费错误——此前 Astra 与 Sol 的套餐消耗被按折扣价计算。Codex 与 ChatGPT 负责人 Thibault Sottiaux 表示，修复后完成相同工作量会消耗更多额度：Astra 触及上限的速度比上周快 **40%**，Sol 快 **25%**；但相对上一代仍更省。公司不追溯少计差额，改为向 Go、Plus、Pro、Business 用户各补发一次可留存的重置机会，并让 Business 用户在 12 月 31 日前免费用 Fast Mode。

来源：[IT之家](https://www.ithome.com/1/033/138.htm) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1042187/openai-is-combining-chatgpt-and-codex-usage-limits)

### Chat 与 Work 合并灰度：一张用量表管两种模式

OpenAI 向少量 Pro 用户开放合并后的 Chat 与 Work 界面，两者共享同一用量表。官方提示重度用户可能更早触顶。合并的目的是减少在「闲聊」与**多步 agent 任务**之间手动切换，但资源消耗差异也被摆到同一账本上。

来源：[TechCrunch](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges)

---

## Google DeepMind / Gemini

### Antigravity 缓存工程：五天把 Neon 的额度利用率提高约 75%

DeepMind 的 Varun Mohan 披露，Gemini 4 Neon 在 Antigravity 里的缓存命中率再升 **4.5%**，同样配额下能多完成 **28%** 的任务；叠加缓存与其他 harness 改进，五天内订阅额度实际可用量提高约 **75%**。他的解释是边际收益递增：命中率从 90% 到 95% 的效果，等于从 80% 到 90%，因为决定省多少的是未命中率。主要增益来自扩大缓存容量（减少长时段淘汰）与更好的路由。

来源：[TestingCatalog](https://www.testingcatalog.com/google-stretches-antigravity-neon-quota-with-caching-gains/)

### Google 开源零依赖 AI 命令行 gemini-api-cli

Google 开源了 gemini-api-cli，用 **Go** 写、无外部依赖，把 Gemini API 的常用调用收进一个终端工具。仓库 4 月创建、昨天仍在更新，已积累 **3,800 余** stars——属于「模型厂商亲自把入口铺到命令行」的一步。

来源：[GitHub](https://github.com/google-gemini/gemini-api-cli)

---

## Anthropic / Claude

### ⭐ 15 亿美元和解金开始到账

小说家已收到款项，每本书约 3,000 美元，余款明年初发放。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Verge](https://www.theverge.com/ai-artificial-intelligence/1043087/anthropic-has-started-paying-out-its-copyright-settlement-to-authors)

### 测试者称疑似 Opus 5.6 现身：SVG 与代码短片批量流出（未证实）

X 上出现一批新的代码短片与 SVG 测试输出，多名测试者认为来自未发布的 **Opus 5.6**，可能通过 Opus 5.5 Extra 路由触达，部分用户在 Claude Code、部分在 Chat。TestingCatalog 明确写道 Anthropic 未发布任何公告，也有人不给这些结果贴 Opus 5.6 的标签。可参照的历史：10 月中旬曾有一批请求疑似落到未公布模型，后来正式发布的是 Fable 5.2 与 Mythos 5.2。

来源：[TestingCatalog](https://www.testingcatalog.com/testers-share-early-results-possible-claude-opus-5-6/) · [B站·劝合](https://www.bilibili.com/video/BV1W717z9Efp)

### Anthropic 平台工程负责人：AI 让「项目耗时」不再是晋升依据

据《商业内幕》，Anthropic 平台工程负责人 Caitlin Leese 表示，AI 普及后单纯以项目完成时间判断晋升资格已不可靠——过去要几年的事现在几个月能做完，团队更看重降延迟、防事故这类实际影响。她称工作重心正从写代码转向**「协调」**：让成员与智能体配合，把一个想法转成能发布的高质量成果。招聘也在改，新面试形式包含「检查智能体写的代码」与「与智能体协作搭系统」。

来源：[IT之家](https://www.ithome.com/1/033/141.htm)

---

## 国内大厂动态

> DeepSeek / Kimi / 豆包 / 智谱 等

### ⭐ GLM-5.5 或延至 2027 年一季度，Kimi K4 或延至年中

路透：3 万亿参数旗舰错过 11 月窗口，月之暗面开发周期可能翻倍到 12 个月。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Decoder](https://the-decoder.com/after-openai-and-anthropic-shut-the-door-on-their-data-a-chinese-ai-developer-is-turning-to-google-and-meta-instead/)

### DeepSeek 灰度「本轮消耗额度」：把每轮对话的账单摆到用户面前

11 月 26 日起，部分 DeepSeek 用户在网页端与 App 看到新功能：一轮对话结束后弹出详情页，展示本次消耗的 Token 与按 API 同价估算的金额。示例拆解为三段——缓存命中的输入 0.02 元/百万 tokens，未命中 1 元，输出 4 元；一轮 18.5 万缓存命中 token 折合 0.0037 元。另新增上下文占用进度条。个人用户目前仍免费。

来源：[IT之家](https://www.ithome.com/1/033/157.htm) · [B站·两个人在吃饭](https://www.bilibili.com/video/BV1pD1pziELM)

### 蚂蚁开源 Ming-Image-0.2-Design：6B 设计向生图模型登顶开放权重榜

蚂蚁百灵开源 Ming-Image-0.2-Design，**6B** 参数的 DiT，MIT 许可。相比 0.1 版强化了复杂构图、光照与文字排版，可用于电商主图、UI 设计稿与空间渲染；这代还把上一代的分层分解细化到**角色部件**级别，方便下游编辑与动画。官方称 11 月 23 日的初步评测中，它在 Artificial Analysis 文生图总榜上是开放权重模型第一。配合 Ling-3.2-flash，可把设计概念直接转成可交互页面。

来源：[HuggingFace](https://huggingface.co/inclusionAI/Ming-Image-0.2-Design) · [B站·AI日报](https://www.bilibili.com/video/BV1Yg1WzXEsH)

### 腾讯 AI for Science 登《Nature》：AI 从零设计双靶点多肽

腾讯生命科学实验室的成果 11 月 25 日以第一单位登上《Nature》主刊：用 AI 挑战高活性双靶点治疗性多肽的从头设计。平台 ORIDTP 把扩散生成、双目标强化学习、柔性多肽亲和力建模与湿实验串成闭环，每轮实验只需测试约 **15 条**多肽，把「大库盲筛」换成「小样本精准迭代」。已在一个方向验证：肿瘤免疫模型中候选分子使肿瘤体积较对照组减少 **94.2%**；减重降糖方向在低于对照药物摩尔剂量时观察到效果。仍处临床前阶段。

来源：[IT之家](https://www.ithome.com/1/033/125.htm) · [Nature](https://www.nature.com/articles/s41586-026-11338-1)

### Sand.ai 的 MAGI-2 登顶图生视频榜：480B 参数，每秒 5 毛

量子位实测报道，Sand.ai 新发布的 **480B** 视频模型 MAGI-2 在 Artificial Analysis 图生视频榜登顶，单条 30 秒 1080p 原片生成成本约 15 元，定价约为同级闭源头部的**十分之一**。能力面：支持最长 2 万字符脚本、秒级切镜（12 次指定切镜全部命中，平均偏差 0.028 秒）、混合最多 20 份参考素材、局部定向修改。技术报告里还记录了一个「对齐税」现象：审美微调后成片更电影感，但预训练阶段的推理与泛化更难触发。官方称计划尽快开放权重。

来源：[量子位](https://www.qbitai.com/2026/11/512916.html) · [Sand.ai](https://sand.ai/)

### VAST 发布 Tripo H3.5 Preview：192 组盲评拿下 42.8% 第一

3D 生成基座模型 **Tripo H3.5 Preview** 上线 Tripo Studio 国际版。统一输入与最高几何质量、剥离贴图与法线的条件下，资深 3D 美术师对 192 组素模盲评中它拿下 82 次第一（42.8%），胜率是第二名 2.3 倍；无贴图网格的浮雕文字识别率从 H3.1 的 46.1% 提升到 90.7%。卖点是「拆掉贴图仍然站得住」——细节必须由几何本身承载。

来源：[量子位](https://www.qbitai.com/2026/11/512981.html)

### 蔚来发布世界模型 NWM 3.0 与 NOMI 4.0：训练提效 5 倍，控制时延降 50%

在第三届 NIO IN 上，蔚来把 NOMI 的九年代码整体重构为原生智能体架构。世界模型 **NWM 3.0** 引入隐式世界模型与双闭环强化学习，综合训练效率提升 5 倍，整车控制时延平均降低 50%。座舱侧 NIM 为超千亿参数 MoE，配合近 3,000 项原子级信息的情境中枢与覆盖 22 个领域的工具中枢，典型车控任务完成率从 40% 多提升到 95.3%。企业侧已上线 7,500 余个应用，研发效率提升 35%。

来源：[量子位](https://www.qbitai.com/2026/11/512897.html)

### 商汤开源 SenseNova-RoboRSI-27B：同一份权重，模拟器和两台真机都能跑

商汤开源的 **27B** 视觉语言模型，面向机器人操作：可向 VLA 策略请求动作、审阅轨迹，或用代码计算并执行夹爪目标位姿（Code as Policy），每次动作后用新的相机观测与机器人状态决定下一步。在 RoboDojo 模拟基准上平均分 34.7，此前的 Preview 为 10.0；同一个 checkpoint 可直接部署在两台真实机械臂上，无需真机数据做适配。

来源：[HuggingFace](https://huggingface.co/sensenova/SenseNova-RoboRSI-27B) · [B站·海猫AI](https://www.bilibili.com/video/BV1Cc1EzWEmy)

### 千问语音模型 Qwen-Audio-3.1 升级：识别 59 种语言、8 种方言（转述）

据 B 站日报转述，通义 Qwen-Audio-3.1 将语音识别扩展到 **59 种语言 + 8 种方言**，语音合成覆盖 **65 种语言 + 6 种方言**。官方未发公告，条目为媒体转述。

来源：[B站·海猫AI](https://www.bilibili.com/video/BV1Cc1EzWEmy)

### 爆料：DeepSeek V4.1 Pro 12 月发布，重点在「不再依赖英伟达」（未证实）

据驱动之家转述并经 B 站日报放大，DeepSeek V4.1 Pro 计划 12 月发布，重点不是参数量而是算力结构——训练侧转向国产芯片。另有传闻称其上一个版本已完成全昇腾训练。均无官方确认。

来源：[B站·白光star](https://www.bilibili.com/video/BV1ug1JzTEkq)

---

## 海外大厂动态

### SAP 计划裁员 1 万人：占总员工 9%，为 AI 时代重构软件业务

彭博报道，欧洲市值最高的软件公司 SAP 正筹备一项计划，裁减至少 **10,000 个**岗位、约占全球员工 9%，目标是把软件业务改造为 AI 原生的形态。这是本周第二家把「AI 转型」直接换算成裁员数字的大型企业软件厂商。

来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-11-26/sap-weighs-cutting-at-least-10-000-positions-in-a) · [IT之家](https://www.ithome.com/1/033/137.htm)

### 英伟达付 2.9 亿美元和解：2018 年隐瞒加密挖矿营收占比

英伟达同意支付 **2.9 亿美元**，了结 2018 年的股东集体诉讼。原告指控公司在那轮加密热潮中误导投资者，隐瞒了游戏显卡营收中来自挖矿的比例。这笔钱与本周标普的负面信用观察无关，但两条新闻共同指向「治理与披露」这个反复出现的软肋。

来源：[Reuters](https://www.reuters.com/legal/government/nvidia-agrees-settle-2018-us-investor-class-action-for-290-million-2026-11-25/)

### 戴尔单季 AI 服务器收入 220 亿美元，同比涨 291%

戴尔披露 AI 服务器单季收入约 **220 亿美元**、同比增长 **291%**，积压订单达 **1,323 亿美元**。与英伟达被停发、被列入负面观察的叙事形成对照：需求侧的钱还在往前跑，卡在中间的是政策与交付路径。

来源：[B站·一只childe](https://www.bilibili.com/video/BV1J81JzWEmw)

### 内存芯片短缺催生采购「战情室」，部分芯片一年涨 10 倍

WSJ 报道，存储芯片短缺正迫使全球公司设立专门采购战情室，部分芯片价格一年内上涨 10 倍，并开始推高消费电子售价。AI 数据中心的 HBM 需求是主要拉力，供应链的瓶颈正从算力芯片转向上游存储。

来源：[WSJ](https://www.wsj.com/tech/memory-chip-shortage-ai-electronics-prices-e58a065a)

### 42 州检察长联名：反对 Character.AI 破产期间拍卖 2,100 万账户聊天记录

Character.AI 10 月申请破产后计划出售用户聊天数据，42 位州检察长几乎同步发声明反对，称涉及 **2,100 万**美国账户、其中 **210 万**注册者为未成年人，且方案对用户无任何保护——不要求买家遵守原有隐私政策、没有删除通道、不限制二次转卖。首个竞标方 11 月 13 日才成立，无母公司或投资人信息。

来源：[The Verge](https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats)

### 瑞士五天发生五起 AI 智能体攻击，电力供水通信系统被入侵

瑞士联邦网络安全局（BACS）通报，过去几天有五起攻击者使用 AI 智能体针对企业与关键基础设施发起的入侵，其中 4 起得手。受害方包含三家关键基础设施运营主体，据 SRF 报道分别为电力、供水与通信服务商。官方未披露幕后主体。

来源：[IT之家](https://www.ithome.com/1/033/131.htm)

### a16z 拟募约 200 亿美元新基金，ElevenLabs 传 330 亿美元估值

两笔融资信号：a16z 正就下一组基金募资约 **200 亿美元**（上一组今年 1 月宣布时为 150 亿以上并已增值）；ElevenLabs 在谈 2027 年的新一轮，目标估值 **330 亿美元**，较 9 月的 220 亿再上一档。同时机构投资者正在折价抛售 2021 年高峰期的老基金份额，转投新的 AI 基金。

来源：[Axios](https://www.axios.com/pro/all-deals/2026/11/25/andreessen-horowitz-20b-fundraise) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-25/elevenlabs-in-early-talks-for-2027-funding-at-33-billion-value) · [FT](https://www.ft.com/content/0278cbea-a0b6-4a30-80f2-f31ac6657f11)

### MiniMax 数据被不明方访问，Talkie 因涉未成年人内容全球下架

Dragos 研究称，有不明方访问了用户提交给 MiniMax 的机密数据，即便用户已要求不存储。更早一日，Apple 在全球 App Store 下架 MiniMax 的聊天应用 **Talkie**，此后有媒体出示其 AI 角色对儿童进行性化对话的证据。两条新闻叠加，构成国产出海应用在数据与内容安全上的双重压力。

来源：[Reuters](https://www.reuters.com/world/data-chinese-ai-firm-minimax-accessed-by-unidentified-parties-researcher-says-2026-11-26/) · [The Bureau](https://www.thebureauinvestigates.com/stories/2026-11-24/talkie-china-chatbot-children)

---

## AI 研究前沿

> 重要论文、技术突破

### ⭐ 381 个 agent 直播攻关 P vs NP

六条战线、30 个席位、红队与「墓地」；2,400 条引理通过，0 条指向 P=NP。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[量子位](https://www.qbitai.com/2026/11/513021.html)

### Mixture-of-Loops Transformer：把 KV 当作跨层、跨循环的记忆

字节 Seed 的 HF 日榜第三（56 赞）。循环 Transformer 复用共享层提升表达力但牺牲效率，这篇追问一个更基本的问题：相邻两轮循环之间到底该传什么？MoLT 的答案是「传 KV」——MoLA 让每个循环选择性复用前序深度与循环的 key/value 作为记忆。两种变体分别走「保留残差流 + 读局部 KV」与「从嵌入重启」两条路，U 形结构在预训练效率与推理延迟上都更好。

来源：[arXiv:2611.34923](https://arxiv.org/abs/2611.34923)

### Sage-Med：医学多模态模型的 scaling 规律长什么样

上海 AI Lab（81 赞）。先给一个反直觉结论：现有医学 MLLM 在多类任务上不如前沿通用 MLLM；单纯扩大规模主要提升文本能力而非多模态感知，开推理模式也补不上视觉差距。为此推出 Sage-Med-Preview，**35B** 总参数、**3B** 激活，用来实测「医学多模态智能在实践中如何扩展」。

来源：[arXiv:2611.34575](https://arxiv.org/abs/2611.34575)

### Real2SimLab：给「真实到仿真」建一个统一考场

北大团队（99 赞，今日榜首）。coding agent 已能从视频生成仿真程序，但每个基准都有自己的输入、产物与评分流程，评估 N 个方法 × M 个基准就要做 N×M 次集成。这个平台统一按「运行 agent 写出的程序」来打分，把矩阵压回一维。

来源：[arXiv:2611.34849](https://arxiv.org/abs/2611.34849)

### VibeVideoAgent：代码生成的视频，需要一个感知闭环

快手 Kling（54 赞）。代码驱动视频生成能精确控制排版、图表、音频与多镜头，但程序正常退出也可能渲染出错位标签、跑偏的机位、断掉的物体交互——这些都不报错。把渲染帧回灌进编码会话会让长上下文爆炸，只看最终成片又太晚。这篇的做法是在中间加一层轻量感知反馈。

来源：[arXiv:2611.34237](https://arxiv.org/abs/2611.34237)

### PyRUA-Dex：不用示范数据，让 coding agent 自己写出灵巧操作策略

北大 DA 组（43 赞）。灵巧操作卡在高质示范稀缺：视频重定向不准、遥操作没有力反馈、外骨骼难规模化。这篇直接绕开示范：多个 agent 并行探索技能与组合方式，再由一个蒸馏 agent 把成功片段凝成程序化策略，最后在仿真与真机上精修。

来源：[arXiv:2611.33144](https://arxiv.org/abs/2611.33144)

### 今日论文速览

- **I2VT**：用图像编辑器训练视频编辑器，无需成对视频即可扩展视频编辑任务，在 OpenVE-Bench 与 OpenVE++ 上 SOTA（CMU）。[arXiv:2611.34941](https://arxiv.org/abs/2611.34941)
- **DyLoMo-DiT**：扩散 Transformer 的权重共享循环 + 动态 MoE，靠复用参数而非增加参数扩容量，38 赞。[arXiv:2611.30844](https://arxiv.org/abs/2611.30844)
- **DocSEAM**：多页文档理解的双向跨页编码，在多页边界补齐视觉 token 的上下文（MMLab@NTU）。[arXiv:2611.34420](https://arxiv.org/abs/2611.34420)
- **HOG-WAM**：给 world-action model 加未来 HOG 直方图做结构监督，提升视觉扰动下的鲁棒性。[arXiv:2611.34811](https://arxiv.org/abs/2611.34811)
- **AIRIS**：以第一人称流式视频为场景的社会具身智能基准（腾讯）。[arXiv:2611.34347](https://arxiv.org/abs/2611.34347)

---

## 行业观点与解读

> KOL 重要推文、深度分析文章

### Jack Despain Zhou：AI 带来的第一后果是「去个体化」

Simon Willison 摘录的一段话被广泛转发：「AI 已有的众多后果里，有一项是巨大的去个体化。我打开 YouTube，听到的是 Claude；我坐在会议演讲现场，听到的是 Claude；我打开邮箱，看到那些挂着正经机构、正经履历的人发来的提案与文章——**我也看到 Claude**。」这段引语的价值在于它描述的是一种体感，而不是指标：当生成变便宜，最先被稀释的不是内容数量，而是「这是谁说的」。

来源：[Simon Willison](https://simonwillison.net/2026/Nov/26/jack-despain-zhou/)

### Karpathy 用公开数据拼出一张「文明风」的美国地图

他把公开数据集叠成一张复古文明游戏风格的地图，展示如何用 LLM 辅助完成「数据整理—风格统一—渲染」这类过去需要几天的手工活。这类作品的传播点不在技术，而在于示范了「一个人 + 模型」能把什么样的兴趣项目做完。

来源：[X @karpathy](https://x.com/karpathy/status/2125779541952246039) · [B站·非常暴龙兽](https://www.bilibili.com/video/BV1T317zZErw)

---

## 值得关注的视频

> YouTube 侧 24 小时内无新片（OpenAI、Anthropic 官方频道与 No Priors、Lex Fridman 均无更新）。以下为 B 站与播客。

### ⭐ Latent Space：Clay 的 GTM agent，一半流量已经不在自家 harness 里

Clay 的 AI 负责人 Jeff Barg 讲了几个可引用的数字：客户用 Clay 自带 agent 与把 Claude Code 指向 Clay，两种用法流量几乎 **50/50**；用 Jev 这类分类器把你理想的客户画像跑遍库里 **4,000 万家**公司，一次约 **1,500 美元**；Clay 从约 50 人长到 **600 人**，9 月以 71 亿美元估值融资 1.15 亿。他的判断是前沿模型的价值在编排与深度研究，而非打榜——「客户讨厌选模型，所以我们要替他们选」。推荐观看。

来源：[Latent Space](https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/)

### 每日技术简报 11.27：四栏 40 条

资讯 10 / 开源 10 / GitHub 10 / HF 论文 10，每条附原始出处，并在片尾逐条写出「口径与限制」——包括哪些是转述、哪些没拿到公司原始文件。今天最省事的一份当日索引。

来源：[B站](https://www.bilibili.com/video/BV1iP1WzoEEq)

### 白光star 11-27 第 57 期：GLM-5.5 延期「是老外造谣」

与路透报道正面对撞的一期：主张上万张国产卡进展顺利，延期说法来自外部媒体。作为对立信源值得一听，但通篇未给出可核验的国产卡部署证据。

来源：[B站](https://www.bilibili.com/video/BV1ug1JzTEkq)

### Ba1ya 白鸦 2026-11-27：混元 DFly2、MiniMax H3、蚂蚁设计模型

按章节切分，每节 30 秒左右，覆盖 GPT-6.2 计量纠正、DFly2 推理加速、MiniMax H3 产品线、Ming-Image-0.2-Design、LingBot-Navi 空间记忆导航与千问语音方言。信息密度高但均为转述。

来源：[B站](https://www.bilibili.com/video/BV1HX1pzNEab)

### 大肥鱼 14 条：数字已联网核实

自述由 AI 自动剪辑生成，14 条覆盖 GPT-6.2 计费、英伟达停发、GLM-5.5 与 Kimi K4 延期、混元 DFly2、381 个 agent 攻 P vs NP、Tidal 清理 2900 万首 AI 歌。脚本里明确标注「以官方口径为准」。

来源：[B站](https://www.bilibili.com/video/BV1Vu1WzWEDH)

### 海猫 AI 日报 11-26：16 条，重点在中国模型

每条都标了信源性质（据路透 / 据 The Information / 未经官方证实），这种标注习惯值得保留。今天的增量是 DeepSeek 内部对差距「3–6 个月拉大到 9 个月」的估算、商汤 RoboRSI 开源、以及 OpenAI 研究员借 GPT-6 Astra 提量子引力方案（未经同行评审）。

来源：[B站](https://www.bilibili.com/video/BV1Cc1EzWEmy)

### 劝合 AI 晚报 11.26：8 条带原始链接

每一条都挂 x.com 或一手媒体报道的链接，包括谷歌开源零依赖 AI 命令行、0.1% 投毒后门与 AI 写码返工、密态推理内测对撞 Character.AI 破产卖对话。适合当交叉核对的底稿。

来源：[B站](https://www.bilibili.com/video/BV1W717z9Efp)

---

## 灵感种子

> 以下是今日简报中值得进一步思考的灵感种子。

**延期的单位是季度，不是版本号。** 智谱从 11 月推到 2027 年一季度，月之暗面从 6 个月拉长到 12 个月——这些数字背后的共同变量不是「卡够不够」，而是「反馈信号从哪来」。反蒸馏切断了「拿别人模型输出当老师」这条低成本路径，逼所有实验室回到自建 RL 环境的高成本路线。顺着想：如果明年的模型档期普遍由数据管线而非算力决定，那么「谁能更快造出可信的合成任务」就会成为比 GPU 库存更早暴露的领先指标。

**下界正在变成一种公关资产。** 上界只能刷记录，下界才宣告天花板；而当每个宣称都自带 Lean 证书，公司连新闻稿都省了。Aaronson 的那句「他们干脆直接往 GitHub 传论文」，描述的是一种新的发布范式：可机检的证明让「我说我做到了」变成「你可以自己验」。值得跟踪的是，这套范式会不会溢出到模型能力宣称上——比如每一份 benchmark 成绩都附可复现的评测脚本与数据快照。

**最便宜的加速来自「不要重复付费」。** DFly2 没换模型、没改输出、没加显存，只是让草稿模型复用目标模型已经算过的稀疏位置，就换来了最高 4.2 倍。这类优化的共性是把「两个组件各自维护一份状态」改成「共享一份已被支付过的状态」。同样的思路在缓存、检索、多智能体协作里都成立：先问一句「这份计算是不是已经有人付过钱了」。

**公开直播的科研流水线，可能是今年最可复用的组织发明。** 30 个席位、思考型与构建型分工、红队专职推翻、墓地归档失败路线、每条引理一个 PR 与超时。这套结构的价值不在 P vs NP 本身（它离解决还很远），而在于它证明：凡是能形式化验收的工作，都可以被拆成可并行、可审计、可回滚的流水线。下一个落点可能是芯片验证、合规审计、乃至教材编写的正确性检查。
