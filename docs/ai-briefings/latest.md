---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-24

## 今日概览

> 今天两条主线并行。模型侧，智谱把旗舰换成「循环 Transformer」，750B 参数打出对标 2T-3T 的官方口径，并称之为「广义编程」的起点；OpenAI 则把 GPT-6.2 Sol 全量推进 ChatGPT，图像理解从 47.4% 跳到 71.7%。资本侧更热闹：英伟达董事会全票请回黄仁勋，市值一天回补超 1 万亿美元；亚马逊花约 75 亿美元买 Decart 的跨芯片优化技术，马斯克则在内部承认「出租算力比自研 Grok 更赚钱」。中间还夹着一个安静的信号：DeepMind 用智能体团队加 Lean 优化量子算法，arcsin 子程序提速 290 倍。

- **智谱发布 GLM-5.4**：750B 循环 Transformer，28 层跑两遍，权重后续开放。来源：[z.ai](https://z.ai/blog/glm-5.4)
- **英伟达全票请回黄仁勋**：NVDA 收涨 31%，市值重回 4 万亿美元，12 月 3 日将赴参议院作证。来源：[IT之家](https://www.ithome.com/1/031/217.htm)
- **DeepMind 让智能体团队优化量子算法**：聚变模拟成本降 11.8 倍，结果全部过 Lean 验证。来源：[DeepMind](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
- **Anthropic 推出 Claude Ship**：Claude 可自动审查、修复并按团队策略批准 PR。来源：[ZDNET](https://www.zdnet.com/innovation/claude-ship-code-how-to-try/)
- **GPT-6.2 Astra 独立证明 2006 年定理**：1800 行 Lean 证明，94 分钟、21.58 美元。来源：[The Decoder](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ 智谱 GLM-5.4：750B 用「循环层」换深度，官方口径对标 2T-3T

11 月 23 日，智谱发布 GLM-5.4，这是国内首个把旗舰押在 Loop Transformer 上的大模型：**7500 亿参数**，但第 27 到 54 层会被跑两遍，用权重共享的二次迭代换取「不增加参数的深度」。为控制开销，每次前向、每个 token 都有独立的 AdGates 门控决定回写幅度，两遍共享 KV 缓存，稀疏注意力的选点在第一遍算好后直接被第二遍复用。

它不是从零训练的。团队把 2 月发布的 GLM-5 底座改造成循环模型——Z.ai 明确说，同算力下从零训练的循环模型反而更差。在一个与 750B 同架构的 30B 对照模型上，循环版在 AIME25 从 19.2 涨到 30.4、GPQA-Diamond 从 47.6 涨到 56.3，且回答平均短了 12% 左右，部分推理被挪进了循环层的额外计算里。

需要打折扣的是：**750B 本体的基准分数一个都没公布**，外推只能靠 30B 实验；也没有 Artificial Analysis 之类的独立评测。可用性是现成的——已上线 Coding Plan、ZCode 与 Z.ai Chat，IT之家实测模型列表带 1M 上下文与视觉标签，持有 V2/V3/团队版的用户额度同步上调至 1.5 倍。官方表示权重会在安全测试后开放，并预告了一个更大的模型。

**核心观点**：循环层把「训练算力」换成了「推理时深度」，参数量不再是能力上限的唯一刻度——同一代权重可以随 loop 次数伸缩，等于在推理端加了一个成本旋钮。但「对标 2T-3T」目前是架构承诺而非实测结论，等权重开出来才能验证。

来源：[z.ai](https://z.ai/blog/glm-5.4) · [The Decoder](https://the-decoder.com/z-ai-follows-openai-into-loop-transformer-territory-with-its-new-750b-flagship-model/)

另见：[IT之家](https://www.ithome.com/1/030/809.htm) · [Simon Willison](https://simonwillison.net/2026/Nov/23/glm-54/)

### ⭐ 黄仁勋 11 天后「被复职」：董事会全票、白宫介入、国会反对

11 月 23 日，英伟达董事会一致投票，即日起恢复黄仁勋总裁、CEO 及董事职务，认定其不存在国家安全风险；科莱特·克雷斯结束临时 CEO 职责回任 CFO，独立调查委员会继续推进，公司另设首席合规官。距离其辞职仅 **11 天**。市场反应剧烈：盘前涨约 30%，开盘一度 32%，收盘涨 31%，市值增加超 **1 万亿美元**，重回 4 万亿美元上方。

幕后版本来自多家媒体：Semafor 称特朗普亲自接入董事会会议推动复职，NYT 称由 JD Vance 主导协调、向董事会保证「无国安风险」；彭博则说董事会没有咨询公司高管，高管最后时刻才被告知。政治反弹同步到来——两党议员批评这一决定并要求国会收紧对华芯片出口立法，参议院银行委员会主席 Tim Scott 宣布黄仁勋将于 **12 月 3 日**公开作证。同一天，商务部把 Megaspeed 列入实体清单。

**核心观点**：一家 4 万亿美元公司的 CEO 去留，由白宫、董事会与国会在一周内往返博弈决定——公司治理让位于产业政策。而「无国家安全风险」的认定与同日新增的实体清单并置，说明出口管制的执行正从「按清单」走向「按个案逐人判断」。

来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director) · [IT之家](https://www.ithome.com/1/031/207.htm)

另见：[Reuters](https://www.reuters.com/business/lawmakers-criticize-nvidia-decision-reinstate-huang-ceo-2026-11-23/) · [Semafor](https://www.semafor.com/article/11/23/2026/jensen-huang-reinstated-as-nvidia-ceo) · [CNBC（Megaspeed）](https://www.cnbc.com/2026/11/23/nvidia-megaspeed-chipmaker-us.html)

### ⭐ DeepMind：Gemini 4 智能体「开会」优化量子算法，结果全部过 Lean

11 月 23 日，DeepMind 与 Google Quantum AI 发布联合研究：把多个独立的 Gemini 4 智能体团队放进同一个共享笔记本，各自提出量子电路改进，所有想法先经 Lean 形式化证明才能入库，每四小时开一次「虚拟会议」交换、辩论、比较方案，直到算力成本曲线收敛。

结果落在四个真实科学场景：惯性约束聚变的成本降了 **11.8 倍**，纠错量子比特从 5650 压到 4338；药物代谢与光化学模拟降 8 倍；细胞色素 P450 相关模拟提速 2.5 倍，内存从 481 个量子比特降到 333；基础组件上，Grover 算法特定实现提速 2.57 倍，反正弦（arcsin）子程序最高提速 **290 倍**。团队已开源 Lean 量子算法库、问题定义与验证通过的解。

**核心观点**：这是「多智能体搜索 + 形式化验证」第一次闭环到可发表的科学成果——智能体负责发散，Lean 负责拒绝错误答案，人类只定义问题与监督方向。可复用的不是量子算法本身，而是这条流水线：任何「正确性可机器判定」的领域都能照此组装。

来源：[DeepMind](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) · [IT之家](https://www.ithome.com/1/031/232.htm)

### ⭐ Claude Ship：让 Claude 审查、修复、并批准 PR

11 月 23 日，Anthropic 推出 Claude Ship 测试版，把代码合并前的人工链条交给一组 agent：Code Review 正式开放，PR Steward 与 Claude Approvals 处于 beta。前者处理 CI 失败、合并冲突与评审反馈，每次推送都在评论里写明改了什么、怎么撤销；后者读取仓库里的自然语言策略文件，结合 Code Review 结论与企业自建分类器的信号，判断哪些 PR 可以自动批准，拿不准时转人工。

设计上有几处克制：PR Steward 不能批准或合并；审批建议先在「仅观察模式」跑；可按仓库启用并设置月度支出上限；开发者随时可以用 @claude 叫停。Anthropic 说得很直白——自己的 Claude Code 团队已经让 Claude 写了大部分代码，目标是「代码写多快就发多快」；但 ZDNET 也提醒，并非所有开发者愿意交出手里最后一道关。

**核心观点**：审批权是软件工程里最后一层人类控制，当它被写成自然语言 policy 文件，「谁写 policy、policy 是否完备」就取代「谁点了批准」成为新的审计对象。这套机制的可信度不取决于模型多强，而取决于策略文件与操作日志能否被外部复核。

来源：[ZDNET](https://www.zdnet.com/innovation/claude-ship-code-how-to-try/) · [IT之家](https://www.ithome.com/1/031/257.htm)

另见：[The Decoder](https://the-decoder.com/anthropic-launches-claude-ship-to-review-fix-and-approve-pull-requests/)

### ⭐ GPT-6.2 Astra 独立证明 2006 年定理：1800 行 Lean，94 分钟，21.58 美元

Vals AI 披露：OpenAI 的 GPT-6.2 Astra 在全程零人工帮助的情况下，给出了 **Smoktunowicz 间隙定理**（2006 年）的机器可验证 Lean 证明——据其称是已知首个。定理内容大致是：一串系统在乘性增长中，要么增长很慢，要么增长很快，没有中间地带。由于原证明的关键基础在 Mathlib 中缺失，Astra 换了条路：用「capacity」（每一步计算至少新增元素个数的度量）重建论证。

任务来自 Autoform-Hard——Vals 从 Meta FAIR 的 AutoformBench 中挑出的 56 道题，Meta 研究中十个模型都没在预算内解出。Astra 在第 47 分钟、花了 8 美元时尝试退出，被系统拒绝（未解出的提交在花满 20 美元前不受理）；沉默 9 分钟寻找新策略后，在第 94 分钟交出 1800 行证明。它目前以 49 题领跑该榜，GPT-6.2 Sol 与 Claude Fable 5.2 各 48 题紧随。

**核心观点**：瓶颈已经不只是模型能力，还有库的完备性——Mathlib 缺基础，模型就绕道自建路线，说明「形式化数学的基础设施债」正被模型主动消化。这类任务的成本（94 分钟、21.58 美元）也是信号：可验证推理正变得便宜到可以日常化。

来源：[The Decoder](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/) · [Vals AI](https://vals.ai/)

### ⭐ 马斯克内部承认：出租算力比自研 Grok 更赚钱

NYT 报道：马斯克近日向员工承认，SpaceX 在 AI 模型研发上落后于 Anthropic、OpenAI，与其把全部算力用于自研产品，不如出租给竞争对手。AI 业务部门已更名 SpaceXSI，贡献 SpaceX 超过一半的营收；自 5 月起向 Anthropic、谷歌出租数据中心，每月进账数十亿美元。他一度把工作群改名为「Sell compute because we can't compete」。

合同细节很具体：Anthropic 在 5 月至 10 月签署并多次修订算力协议，总额最高 **1205 亿美元**，期限至 2029 年，全部交付后月付约 31 亿美元，算力预计 2026 年 12 月交付完毕；谷歌的协议约 11 万块英伟达 GPU，2026 年 10 月至 2029 年 6 月每月支付 9.2 亿美元。他要求工程师每周汇报 GPU 用途，浪费者可能被解雇。

**核心观点**：算力正在从成本项变成可交易资产——同一批 GPU，出租给前沿实验室的收益高于自己训练一个落后模型。这会重写「自研」的战略算术：当租金收益率持续高于自研的边际期望，模型竞赛会自动把中立算力供应商推向「卖铲子」的位置。

来源：[IT之家（转 NYT）](https://www.ithome.com/1/031/246.htm) · [The Decoder](https://the-decoder.com/anthropics-appetite-for-compute-is-pushing-xai-toward-a-rent-over-build-strategy/)

### ⭐ MemOnce：南大记忆架构，把长上下文的 KV 缓存压缩 1313 倍

南京大学（B 站 AI 前沿晚报称与中科大合作）提出 MemOnce：不再逐层逐 token 缓存完整的 KV，而只把最后一层的少量隐状态压缩成「记忆表示」存起来，需要时再动态解码回各层注意力用的 KV；每个新输入的稀疏检索索引只算一次，跨层复用。改造成 Qwen3.5-4B 后，记忆状态缓存缩小 **1,313 倍**，prefill 开销同步下降，复杂度回到线性。

**核心观点**：「压缩历史 + 按需解码」正在成为长记忆的主流路线——记忆不再是被动缓存，而是可学习的稀疏结构。它与端侧路线互相加强：B 站转述称压缩后仅约 25MB，千亿参数端侧模型的可行性和这类架构直接相关。

来源：[arXiv:2611.27973](https://arxiv.org/abs/2611.27973)

另见：[B站·AI前沿晚报 11.23](https://www.bilibili.com/video/BV16JyXzLEY7)

### ⭐ Import AI 482：AscendGYM——让 AI agent 去优化华为昇腾内核

Jack Clark 本期头条是深圳循环经济研究院发布的 AscendGYM：一个面向昇腾 NPU 的内核优化基准，核心问题是「给一个正确的内核实现，agent 能否在预算内、不破坏正确性的前提下继续提速」，配套 AscendForge 提供编译、正确性校验、性能测量与反馈的统一接口。测试中 Opus 5 最好，其次 GPT-5.6，再次 GLM-5.3；Claude Code 给出最高绝对分，GPT 在 Codex 里表现更好。

同一期还收了两个值得记住的结论：LLNL 的 SciResearch-Eval 让 agent 在「模拟器故意有缺陷」的材料科学任务上报告 95% 置信区间，默认设置下只有 GPT-6 Astra 与 Claude Fable 5.2 可靠，Claude 5.5 要开到最高推理档才行，开源模型全部失败；李飞飞团队的 Yejin Choi 与 Carlos Guestrin 创立 Noeri，融资 1.1 亿美元，主张「复数智能」——前沿不该只由几个巨型模型定义。

**核心观点**：出口管制的另一面是软件自举——如果 agent 能持续榨出昇腾内核的性能，芯片硬件差距会被「编译器 + agent」部分抵消，这与 CUDA 护城河是同一场战争的两端。而「报告诚实的不确定性」被列为前沿能力，意味着评测正在从答对题转向像科学家一样工作。

来源：[Import AI 482](https://jack-clark.net/2026/11/23/import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-labs-ai-science-benchmark/)

---

## OpenAI

### GPT-6.2 Sol 全量进入 ChatGPT 聊天标签页

OpenAI 把聊天版 GPT-6.2 推向全球 Plus、Pro、Business、Enterprise 用户。官方内部测试：图像理解从 **47.4% 提升到 71.7%**，困难指令跟随从 62.5% 到 78.1%，专家级任务内部基准 65-71 分（GPT-6 为 52-66），内部 BrowseComp 最高档领先约 10 个百分点。系统卡显示困难对话中安全策略遵循率从 77-80% 提到 **91-94%**，青少年安全（情感依赖、进食障碍、危险行为）进步最大。Work 与 Codex 模型不变，企业管理员可控制开关。

来源：[The Decoder](https://the-decoder.com/openai-updates-chatgpt-to-handle-complex-everyday-questions-web-searches-and-images-more-reliably/) · [B站·AI 日报第 47 期](https://www.bilibili.com/video/BV1GWydzgEmW)

### OpenAI 与思科开源 Shirudo：给运行中的 Linux 打「临时补丁」

传统漏洞响应要经历修复、测试、灰度、全量，动辄数天；Shirudo 用 eBPF 在不停机的情况下观测内核与网络活动，对可疑行为施加精准控制。防护层（shield）由 Codex 生成，加载前须经加密签名验证，TPM 记录加载与移除；受控测试中成功拦截针对运行中 Elasticsearch 的 Java4Shell 攻击且未重启服务。项目以 BSD 2-Clause 开源。

来源：[OpenAI](https://openai.com/index/introducing-shirudo) · [IT之家](https://www.ithome.com/1/031/245.htm)

### ⭐ GPT-6.2 Astra 证出 Smoktunowicz 间隙定理

1800 行 Lean 证明、94 分钟、21.58 美元，零人工帮助。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Decoder](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/)

---

## Google DeepMind / Gemini

### ⭐ 智能体团队 + Lean 优化量子算法

聚变模拟成本降 11.8 倍、arcsin 提速 290 倍，全部结果形式化验证。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[DeepMind](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)

### Google 搜索的「个人智能」接入 Wallet 与 Drive

11 月 23 日起，用户可在 AI Mode 中选择授权，把 Google Wallet 接入 Personal Intelligence，Drive 与 Gemini app 将在未来几周跟进；连同此前的 Gmail、日历、相册，搜索回答可以基于消费记录、个人文档和聊天内容。官方给出的用法是梳理消费、优化信用卡积分、基于文件生成个人计划，强调所有连接均可随时在设置中关闭。

来源：[Google Blog](https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/)

### Gemini 4 Helium 的传闻

B 站 AI 日报第 31 期称谷歌网页代码中出现 TIER_HELIUM 字样，推测 Gemini 4 Helium 即将发布；同时转述「谷歌订阅 12 月 2 日向第三方开放」。两条均无官方口径，仅作线索。

来源：[B站·AI 日报第 31 期](https://www.bilibili.com/video/BV1P8yQzSEoR)

---

## Anthropic / Claude

### ⭐ Claude Ship 测试版：审查、修复、批准一条龙

PR Steward 与 Claude Approvals 进入 beta，审批依据是仓库里的自然语言策略文件。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[ZDNET](https://www.zdnet.com/innovation/claude-ship-code-how-to-try/)

### 零数据保留 + 企业前沿保障（EFS）进入公测

11 月 23 日，Anthropic 宣布 Enterprise Frontier Safeguards 进入 beta：在**不保留任何数据**的前提下，仍能检测对前沿模型的复杂滥用，Anthropic 与云厂商都不留存企业数据。九月公布以来已有 100 多家客户参与开发，包括财富 100 强的四分之一；Bridgewater、Salesforce、Stripe 在私测名单中，引用里反复出现的一句是「数据留在我自己的账户与密钥下，检测交给 Anthropic」。

来源：[Claude](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards)

### 达里奥 IPO 当日套现约 2.8 亿美元

SEC Form 4 显示，阿莫代伊在 Anthropic 上市当天以发行价 **83 美元**卖出 3,378,378 股 A 类普通股，金额约 2.804 亿美元；11 月 19 日另有 345,011 股被扣留用于 RSU 所得税。其信托持有 35,932,660 股。截至 11 月 23 日收盘，股价 87.64 美元，市值约 1.15 万亿美元。文件未标注本次交易依据 10b5-1 计划。

来源：[IT之家](https://www.ithome.com/1/031/253.htm)

---

## 国内大厂动态

> DeepSeek / Kimi / 豆包 / 智谱 等

### ⭐ 智谱 GLM-5.4：750B 循环 Transformer

28 层跑两遍对标 2T-3T，已上线 Coding Plan，权重后续开放。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[z.ai](https://z.ai/blog/glm-5.4)

### 蚂蚁百灵医疗健康大模型全面开源

蚂蚁阿福生态大会上，百灵医疗健康模型家族整体亮相并开源两款核心模型：多模态的 **LingSante-3.1-air-VL**，124B 总参数、5.5B 激活，可在笔记本本地部署，医疗影像报告、皮肤疾病识别等细分任务自称全球第一；深度推理的 **LingSante-3.1-flash**，560B 参数、支持 1M Token 上下文，面向长病历与多轮检索。另有实时视频问诊的 Live、预测六年发病风险的 Pulse 与医疗安全防护 MedGuard。阿福现有 1.5 亿用户，日问诊近 2000 万次，四分之一是老年人。

来源：[IT之家](https://www.ithome.com/1/030/784.htm) · [量子位](https://www.qbitai.com/2026/11/512017.html)

### 豆包工作上线 21 个专业工作台

字节豆包工作把能力切成 21 个「岗位」：金融投研、创意设计、医生、教师等，每个工作台预配技能与数据源。上线三个月 DAU 突破 **800 万**，企业客户 ARR 突破 **20 亿元**，业内人士称其为字节优先级最高的产品。量子位用四个工作台做了实测（80 分）：研报数字可逐项核对、补了来源但未完全遵守「未披露就写未披露」的指令，设计工作台能一次出五张不同方向的电商主图。结论是「有用的工作底稿，但成品要人拍板」。

来源：[量子位](https://www.qbitai.com/2026/11/511933.html)

### Edge0-145B：1450 亿参数端侧模型，宣称笔记本 80+ token/s

无界方舟发布 Edge0-145B，自称「全球首个千亿参数端侧原生基础模型」：最低 12GB 显存 + 20GB 内存的 PC 或 48GB 统一内存的 Mac 可跑，断网 Vibe Coding，官方演示 80+ token/s；对比云端私有化部署 180-300 万元的服务器，成本约 1.5 万元笔记本。量子位实测 3D 建模、游戏、视频三项任务，认为接近 GPT-6 Astra 水平。

一个值得注意的细节：Hugging Face 上 Edge0/Edge0-145B-NVFP4 的权重卡把 base_model 标为 Qwen3.8-Flash-Next（94k 下载、799 赞、11 月 11 日创建），与「端侧原生基础模型」的表述存在张力，官方模型卡说明出来前这个口径宜存疑。

来源：[量子位](https://www.qbitai.com/2026/11/512195.html) · [Hugging Face](https://huggingface.co/Edge0/Edge0-145B-NVFP4)

### 腾讯微信 AI 开源 4B 端侧多模态模型 WePocketModel1.0

tencent/WePocketModel1.0-4B 以 Apache-2.0 许可开源，image-text-to-text 管线，标签含 on-device、多模态 embedding、结构化决策，架构标注 qwen3_5。B 站转述其特点为「单权重并行做生成、检索与决策」。该仓 11 月 17 日创建，下载量仍很低，属于早期放出。

来源：[Hugging Face](https://huggingface.co/tencent/WePocketModel1.0-4B) · [B站·AI前沿晚报 11.23](https://www.bilibili.com/video/BV16JyXzLEY7)

### 阿里云 AgentLoop 记忆库、经验库与优化任务 12 月 7 日起收费

三项 agent 资产功能按 AI Credits 实际消耗计费：记忆库从对话中抽取跨会话长期记忆，经验库从执行轨迹提炼可复用经验，优化任务对 Prompt、Skill 等资产自动调优。官方建议用户先评估用量再做预算。

来源：[IT之家](https://www.ithome.com/1/030/926.htm)

### 知乎 15 亿元经基金间接入股 DeepSeek（转述，待核实）

B 站白光 AI 日报引述英为财情与搜狐：知乎以 15 亿元认购一只 AI 基金份额，经该基金间接持有 DeepSeek 低个位数百分比股权。该说法目前只有二手转述，未见知乎或 DeepSeek 官方公告。

来源：[B站·白光 AI 日报第 54 期](https://www.bilibili.com/video/BV1fryQz3E3G)

### DeepSeek 周调用量被报 65 万亿 Token 居首（转述，待核实）

多个 B 站 AI 日报称 DeepSeek 周调用 Token 量约 65 万亿、居全球第一，并称其对免费用户做了限额。数据口径与统计方不明，仅作观察线索。

来源：[B站·肥鱼速览 11-24](https://www.bilibili.com/video/BV1KeydzYEFW) · [B站·白光 AI 日报第 54 期](https://www.bilibili.com/video/BV1fryQz3E3G)

### 公安部公布 10 起 AI 造谣典型案例

「净网-2026」专项行动半年查处 190 余人，此次公布的案例全部由 AI 工具生成：张家界玻璃桥「坍塌」、广州夜市「水浸」、假冒警察形象、编造稀土走私案值 46 亿、伪造艺人发帖、高考调包、毒大米生产线、诺如病毒再袭等。处置从行政处罚到刑事强制措施不等。

来源：[IT之家](https://www.ithome.com/1/031/261.htm)

---

## 海外大厂动态

### ⭐ 英伟达董事会全票恢复黄仁勋职务

市值一日增加超 1 万亿美元，总统介入、议员反对、12 月 3 日参议院作证。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)

### 亚马逊约 75 亿美元收购 Decart 的 AI 优化技术

亚马逊宣布收购 Decart 的 Optimisation Stack 与团队，彭博称金额约 **75 亿美元**（官方未披露）。DOS 是跨芯片的推理优化引擎，能在英伟达、谷歌、亚马逊芯片间切换；Decart 自 2025 年起即为 Trainium 做优化。关键人物与核心资产一起并入，是一次典型的「技术 acqui-hire」。

来源：[IT之家](https://www.ithome.com/1/031/262.htm) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-23/amazon-is-said-to-pay-7-5-billion-for-ai-startup-decart-s-tech)

### 马斯克承认 AI 研发落后，出租算力比自研更赚钱

SpaceXSI 贡献 SpaceX 超一半营收，Anthropic 合同最高 1205 亿美元。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家（转 NYT）](https://www.ithome.com/1/031/246.htm)

### Sierra 传以 300 亿美元估值融资超 17.5 亿美元

彭博称 Bret Taylor 的客服 AI 公司 Sierra 正敲定 Lightspeed 与 Greenoaks 领投的融资，估值 300 亿美元，较 5 月的 158 亿美元近乎翻倍。企业客服 agent 仍是融资最热的赛道之一。

来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-11-23/bret-taylor-s-sierra-finalizing-more-than-1-75-billion-round)

### Marlowe 2.77 亿美元种子轮，押注非英伟达芯片优化

Accel 领投，估值 11.5 亿美元。Marlowe 做多云基础设施与性能工具，专门为「非英伟达 AI 芯片」调度与优化负载，方向上与亚马逊买 Decart 完全同构。

来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-11-23/marlowe-raises-277-million-to-bolster-alternatives-to-nvidia-chips)

### CrowdStrike 以 439 亿美元全股票收购 Zscaler

每股 Zscaler 换 1.135 股 CrowdStrike，隐含每股约 260.41 美元、溢价约 34%。合并后年经常性收入预计超 100 亿美元，交易预计 2027 年下半年完成。安全厂商的合并正在与「agent 安全」这一新品类同步加速。

来源：[IT之家](https://www.ithome.com/1/031/188.htm)

---

## AI 研究前沿

> 重要论文、技术突破

### ⭐ MemOnce：把长上下文的 KV 缓存压 1313 倍

只缓存末层少量隐状态、按需解码回 KV，稀疏索引跨层复用。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[arXiv:2611.27973](https://arxiv.org/abs/2611.27973)

### NoPeWorld：给视频世界模型装一个「防穿模」小头

港理工团队先做了 NoPeBench：给交互式视频世界模型设置物理障碍，结果**没有开源模型能可靠阻止物体穿模**。有意思的是，作者发现扩散 Transformer 的隐状态里其实已经编码了「这个动作会穿模」的信息——于是训练一个不到 200 万参数的轻量头来检测并阻止，无需重训底座。B 站转述称穿模率从 74% 降到 16%。

来源：[arXiv:2611.27963](https://arxiv.org/abs/2611.27963)

### Clover-35B-A3B：扩散语言模型的「agent 版」

DiffuSpace 的 MoE 扩散语言模型，35B 总参数、3B 激活，支持 thinking 模式；把 Gated Delta Networks 的循环记忆与块内双向注意力结合，历史记忆与当前块 token 共享 softmax。报告称在七个 agent 指标上领先，SWE-bench Verified **73.6**、Terminal-Bench 2.1 **51.7**。扩散式生成在代码 agent 任务上的可行性值得继续跟踪。

来源：[arXiv:2611.24636](https://arxiv.org/abs/2611.24636)

### 今日论文速览

- **ReSpaceBench**：3,244 个问题、590 个场景、9 类任务，专门测「重访同一空间时能否认出同一个地方并更新记忆」，填补具身智能的空间记忆评测空白。[arXiv:2611.21485](https://arxiv.org/abs/2611.21485)
- **Intent Contracts**：规划模型手里完全不给工具，只能提交「目标 + 用户原话引用 + 范围」的合同，由小模型校验后亲自写工具调用；让规划器的每一次影响都留在可审计的日志里。[arXiv:2611.24025](https://arxiv.org/abs/2611.24025)
- **AgentRoboCritic**：在 12 个操作基准上对前沿 agent 做动作级批评——策略同时声明局部意图，批评者按意图判断结果与失败模式，比 episode 级成功率细得多。[arXiv:2611.26613](https://arxiv.org/abs/2611.26613)
- **NextUnit-Bench**：把「通用性」从模型挪到建模者身上——agent 两小时内为未见过的设备交付可执行预测器，24 个数据集 58 折，前沿 agent 得分超 AutoML 两倍以上。[arXiv:2611.25252](https://arxiv.org/abs/2611.25252)
- **漏洞时间线审计**：3,758 个有利用证据的漏洞中 98% 有披露日期，仅有 **15.7%** 能追溯到补丁证据，供应商侧所需日期几乎全部缺失。[arXiv:2611.22479](https://arxiv.org/abs/2611.22479)

---

## 行业观点与解读

> KOL 重要推文、深度分析文章

### ⭐ Import AI 482：AscendGYM 与中国算力自举

用 agent 优化昇腾内核、SciResearch-Eval 的「诚实不确定性」、Noeri 的复数智能。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Import AI](https://jack-clark.net/2026/11/23/import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-labs-ai-science-benchmark/)

### 苏剑林：Muon 背后的优化理论（系列第一篇）

「科学空间」开新系列，从《Understanding Gradient Orthogonalization via Non-Euclidean Trust-Region Optimization》出发，把 SignSGD、Muon 等统一进 LMO（线性最小化预言机）框架：先选范数，再在单位球内找与梯度内积最大的方向反向更新。重点讲全量、随机与动量三种情形下的收敛分析，并补充自己的推导。

来源：[科学空间](https://spaces.ac.cn/archives/12014)

### Simon Willison 实测 GLM-5.4：一周内第二次见到循环 Transformer

他走 Coding Plan 订阅拿到 API Key（与常规 API 共享 OpenAI 兼容的 Responses API），写了 llm-glm 插件，并照例用「鹈鹕骑自行车」横评四代 GLM：5.3 与 5.4 的生成风格已回归主流模型观感，而 5.1/5.2 有鲜明自家风格。他还点出，11 月 20 日 Thinking Machines 的 Inkling 2 Mini 同样是 looped transformer——循环架构正在从论文走进产品线。

来源：[Simon Willison](https://simonwillison.net/2026/Nov/23/glm-54/)

### AWS CEO Matt Garman：AI 安全不能靠「紧急刹车」

他在自家新闻页撰文称，把 AI 安全寄托于一个紧急停机开关是误解，真正有效的是让几十年安全系统工程的方法论——纵深防御、可观测性、最小权限——迁移到 AI 系统上。这与同期 Claude Ship 的「观察模式先行、policy 化审批」是同一思路的产品化。

来源：[About Amazon](https://www.aboutamazon.com/news/aws/aws-ceo-ai-safety-engineering)

---

## 值得关注的视频

> YouTube 播客与频道近期值得看的视频。标注 ⭐ 的为重点推荐。YouTube 侧本期无 24 小时内新片（No Priors、Lex Fridman 最近更新均为 11 月 19 日），以下为 B 站中文频道。

### ⭐ AI前沿晚报 11.23：10 条热点，每条附一手信源

信息密度最高的一期：黄仁勋复职、GLM-5.4、MemOnce、微信 WePocketModel、NoPeWorld、HF 智能体评测指南、Sierra 融资、Alexandr Wang 警告、五大银行修改 AI 代理条款、Taylor & Francis 撤稿（作者藏白字提示词诱导 AI 审稿）。时间轴精确到分，适合当当日全景索引。

来源：[B站](https://www.bilibili.com/video/BV16JyXzLEY7)

### AI日报·肥鱼速览 11 月 24 日：14 条动态一次过

英伟达、GLM-5.4、GPT-6.2 进聊天页、Claude 插件合并、蚂蚁百灵开源、微信 WePM、中国电信 285B 星辰、MemOnce、a16z 一万一千次 agent 购物实测、知乎入股 DeepSeek、DeepSeek 周调用、Shirudo、Antigravity 开 Carbon 等，标注「数字已联网核实」。

来源：[B站](https://www.bilibili.com/video/BV1KeydzYEFW)

### AI 日报第 47 期：GPT-6.2 杀进 ChatGPT

12 条消息，每条标注官方出处（help.openai.com、nvidianews、openai.com、deepmind.google 等），并区分「官方帖」与「博主原帖、官方未确认」。想核对某条消息的一手链接，这期最省事。

来源：[B站](https://www.bilibili.com/video/BV1GWydzgEmW)

### 鲸鱼娘：11 月 24 日 AI 圈 5 件事

智谱 GLM-5.4、谷歌搜索接入钱包、Anthropic 零数据保留、蚂蚁百灵开源、阿里云 AgentLoop 收费，每件事附原始出处链接，4 分钟竖屏速览。

来源：[B站](https://www.bilibili.com/video/BV1E2y9z2E3f)

### 白光 AI 日报 11-24 第 54 期：DeepSeek 调用量与知乎入股

头条分析知乎 15 亿元经基金间接入股 DeepSeek 的路径与含义——「间接持股不等于话语权，更像财务投资」，并给出「份额稀缺推高下一轮定价」的推断。注意其数据引用均为二手转述。

来源：[B站](https://www.bilibili.com/video/BV1fryQz3E3G)

### AI 日报第 31 期：TIER_HELIUM 与 20 条速览

单条 60 秒的密集速览：Gemini 4 Helium 传闻、Arena 前三、Inkling-2-Mini-heretic、GPT-Aeon 目击、字节 Axion 1.0、DeepSeek harness 大更、Tesla Reality View、苹果四档端侧模型、中国电信 Xing4.1、MiniMax pi-H3、蚂蚁 Ling-3.2-air 等。传闻与事实混杂，适合找线索，引用前需回查官方。

来源：[B站](https://www.bilibili.com/video/BV1P8yQzSEoR)

---

## 灵感种子

> 以下是今日简报中值得进一步思考的灵感种子。

**「循环层」正在把缩放定律拆成两条轴。** GLM-5.4 让 28 层跑两遍、GPT-6 Astra 同用循环架构、Inkling 2 Mini 把中间层跑三遍——一周内三家押注同一路线。参数不动、深度翻倍，等于把「每 token 算力」从推理配置变成模型设计的一部分；训练侧省下的参数，转到推理侧按调用付费。接下来值得追的是：loop 次数会不会像温度、思考预算一样，变成服务商按价格和档位分层的旋钮，以及这对「同等算力下谁更聪明」的评测口径意味着什么。

**审批权被写成 policy 文件之后。** Claude Ship 把 CODEOWNERS 升级成了自然语言策略库：CI、评审、分类器信号汇总成「可否自动批准」的判断。人类不再是每次合并的最后闸门，审计对象就从「谁点了批准」变成「policy 完备吗、日志可复核吗」。这可能是企业 AI 落地里第一个真正意义上的「治理即代码」场景——值得思考的是，它会不会反过来成为合规认证的新载体：能不能自动批准 PR，变成一张可被审计的证书。

**形式化验证正在成为智能体的裁判席。** 本周三件事同构：DeepMind 量子电路过 Lean 才入库，Astra 在 Mathlib 缺基础时绕道自建证明，Navier-Stokes 论文先有 Lean 后有正文。「搜索 + 机器验证」正在成为科学发现的标准流水线，而瓶颈已从模型能力转向可验证知识库的完备程度——Mathlib 的缺口直接决定了模型的绕道路线。顺着想：补齐形式化数学库这件事，本身就可能被 agent 接管，形成「模型修库、库再喂模型」的飞轮。

**算力竞争从「造芯片」转向「榨芯片」。** 同一天的四个信号：SpaceX 出租 GPU 比自研模型赚钱、亚马逊 75 亿美元买 Decart 的跨芯片优化、Marlowe 靠非英伟达优化拿到 2.77 亿美元种子轮、AscendGYM 让 agent 优化昇腾内核。它们指向同一个判断：在制程与生态差距被拉平之前，中间层——调度、编译、内核优化——会先被重新定价。对创业者的启示是，护城河可能不在硬件也不在模型，而在「同一块芯片上多榨出多少有效算力」这件事的工程积累。
