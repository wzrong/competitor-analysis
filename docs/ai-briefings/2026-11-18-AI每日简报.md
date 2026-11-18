---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-18

## 今日概览

> 11 月 17 日的主线只有一个词：每任务成本。OpenAI 用 Fable 5.2 五分之一的成本追上它的分数，微软一口气放出七款模型、全部按单任务报价，商汤用 9B 参数打出 27B 的性能。资本侧同步加速：Anthropic 拿到纳斯达克代码 ANT、给出 70–78 美元发行区间，OpenAI 选在定价前夜发模型；英伟达则在交出翻倍财报的同一天，正式关掉中国 H200 的门。

- **GPT-6.2 Astra 与 Sol 发布**：Agents' Last Exam 比 Fable 5.2 高 5.5 分，单任务成本只有其 5%。来源：[IT之家](https://www.ithome.com/1/028/577.htm) · [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/)
- **微软 Ignite 七款模型连发**：MAI Code 2 单任务 0.309 美元，约为 Claude Opus 5.5 的 5%。来源：[IT之家](https://www.ithome.com/1/028/579.htm)
- **Anthropic 获准上市**：代码 ANT，发行价 70–78 美元，中值募资约 611 亿美元，连同步私募合计约 846 亿。来源：[IT之家](https://www.ithome.com/1/028/599.htm)
- **英伟达 Q3 营收 1158 亿美元**：同比增 103%，同日确认不再向中国销售 H200。来源：[NVIDIA](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) · [TechCrunch](https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/)
- **商汤开源 Loop-9B**：9B 参数、10GB 显存可跑，NL2Repo 与 AIDABench 比肩 Qwen3.8-27B。来源：[IT之家](https://www.ithome.com/1/028/534.htm)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ GPT-6.2 Astra 与 Sol：在 Anthropic 定价前夜，OpenAI 报了"五分之一的价"

11 月 17 日，OpenAI 发布 **GPT-6.2 Astra 与 GPT-6.2 Sol**。Astra 定位旗舰，面向科学、法律、金融等专业工作；Sol 定位日常任务，主打效率。两款模型先向 ChatGPT Work 与 Codex 的 Plus、Pro、Enterprise、Business、Edu 用户开放，**暂未进入普通聊天模式**；Pro 500 可用两款模型的 Ultrafast 模式，Pro 200 首次拿到 Sol 的 Ultrafast 权限。

定价是这次发布的核心。Astra 输入每百万 token **8 美元**、缓存输入 0.40 美元、输出 40 美元，比 GPT-6 Astra 全线降 20%，缓存价降 60%；Sol 维持 GPT-6.1 Sol 的 2 美元 / 10 美元。按 Simon Willison 的对照，6.2 Astra 与 Claude Fable 5.2 恰好同价，而两者都是各自上一代的八折——两条产品线在同一个月做了同一道算术题。

更值得看的是成本口径。OpenAI 称在 Agents' Last Exam 上，Astra 比 GPT-6 Astra 高 5.2 分且成本不到三分之一；比 Claude Fable 5.2 高 5.5 分，成本只有后者 **5%**。Terminal-Bench-Science 同样高出 9 分、成本不到三分之一；Harvey LAB-AA 法律基准上，通过率是 Fable 5.2 的两倍多，成本约六分之一；GDPval-v2 高出 6.2 分且输出 token 少 22%。

第三方口径略有温差。Artificial Analysis 智能指数把 Astra 排**第二**，仅次于 Fable 5.2，但认为它在成本—性能的帕累托前沿上领先；Epoch AI 则给出与 Fable 5.2 **并列**的结果。The Decoder 指出，Agents' Last Exam 上唯一跟得住 Astra 的是 Gemini 4 Carbon。而在 Simon 的 3D 动画基准里，Astra 与 Sol 的成品都没能超过 Fable 5.2 和 Gemini 4 Carbon——分数与观感之间的差距还在。

**核心观点**：这次发布真正改变的是比较单位。当"高 5.5 分"和"便宜 95%"同时出现在一张表里，买家的问题就从"谁最强"变成"为这 5.5 分该付多少倍的钱"，而后者的答案在绝大多数业务里都很明显。OpenAI 选在 Anthropic 定价前一天发布，把这条信息直接送到了 IPO 路演的桌面上——模型发布日历第一次被资本市场编排。

来源：[IT之家·发布细节](https://www.ithome.com/1/028/577.htm) · [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/) · [OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol)

另见：[Simon Willison 实测](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/)

### ⭐ 微软 Ignite 七连发：把"每任务成本"做成一整条产品线

11 月 17 日的 Ignite 2026 上，微软一次放出七款自研模型，每一款都只讲一件事：同样的活，比对手便宜多少。

编程线是 MAI Code 2 与 Code 2 Flash。Code 2 在四项编程基准上达到 GPT-6.1 Sol 约 98% 的表现，价格约 40%；单次任务成本 **0.309 美元**，对比 GPT-6.1 Sol 的 0.761 美元、Claude Opus 5.5 的 6.306 美元，只占后者约 5%。Flash 在 50% 促销价下单任务低至 0.052 美元，DeepSWE 1.1、Terminal-Bench 2.1、SWE Atlas 三项平均通过率 61.0%，高于 GPT-6 Luna 的 55.1% 与 Haiku 5.5 的 53.9%。

语音线是 **MAI Realtime 1**，微软首款语音对语音模型，基础价每分钟 0.01 美元，涉及推理时按输入 1 美元、输出 5 美元每百万 token 另计。Big Bench Audio 准确率 **98.9%**，每小时音频成本约 1.35 美元，对照 GPT-Realtime-2 High 的 96.6% / 4.14 美元与 Grok Voice 2.0 的 97.2% / 4.80 美元。

图像线是 **MAI Image 2.7 与 2.7 Flash**，每千张约 35 美元与 10 美元。2.7 在 Artificial Analysis 图像编辑榜以 1215 分登顶，领先 GPT Image 2.6 Sunburst 4 分，**成本约其五分之一**；两款都支持透明背景，另配一个交互式工作区 Canvas。

另外三款更偏基础设施。**Microsoft-Decision-1.1** 专做路由、分类、优先级这类高频判断，输入每百万 token 0.042 美元、输出免费，决策指数 68 分列第八，在 Copilot 内部替代大模型做请求路由后**速度快 2.2 倍、成本低 4.4 倍**。MAI Cyber 2 Flash 主打网络安全，性能比肩 GPT-6 Astra，单任务成本约 2%。自研芯片 Maia 200 转入规模生产：台积电 3 纳米、216GB HBM3e、FP4 超 10 PFLOPS，已部署在美国、欧洲、澳大利亚，微软称其在 Teams、Copilot 等场景每瓦 token 处理量最高提升 **1.7 倍**。

**核心观点**：七款模型里没有一款在冲击"最强"。微软的策略是把前沿能力拆成七个价位，让每个价位都有一个"够用且比对手便宜五到二十倍"的选项——这是一种典型的平台公司打法：不赌谁赢，赌调用量增长。配套的 AI 透明度计划（与埃森哲、Adobe、KPMG、万事达卡等 40 多家组织合作，按"观察、验证、控制"三步定义智能体可审计性）说明它还想顺便当规则制定者。对买方的直接含义是：模型采购正在从"选一家"变成"按任务分档配货"。

来源：[IT之家·MAI Code 2](https://www.ithome.com/1/028/579.htm) · [IT之家·MAI Realtime 1](https://www.ithome.com/1/028/588.htm) · [IT之家·MAI Image 2.7](https://www.ithome.com/1/028/582.htm)

另见：[IT之家·Decision-1.1](https://www.ithome.com/1/028/593.htm) · [IT之家·MAI Cyber 2 Flash](https://www.ithome.com/1/028/585.htm) · [IT之家·Maia 200](https://www.ithome.com/1/028/597.htm) · [IT之家·透明度计划](https://www.ithome.com/1/028/603.htm)

### ⭐ Anthropic 的上市定价：70–78 美元，7 倍超额认购，与一个被质疑的估值

11 月 17 日，SEC 公示文件显示 Anthropic 的 A 类普通股获准在纳斯达克全球精选市场上市，代码 **ANT**，发行价区间维持每股 70 至 78 美元。公司拟发行 8.25 亿股，其中新股约 8.014 亿股、老股东出售约 2365 万股；按 74 美元中值估算，公开发行规模约 **611 亿美元**。

除公开募股外，还有一笔 260 亿美元的同步私募配售，参与方包括谷歌、英伟达、AMD、微软、博通、美光与台积电。两者合计预计净募资约 846 亿美元，若承销商全额行使 1.2375 亿股的超额配售权，可达约 937 亿美元。这个数字将刷新人类史上最大 IPO 纪录。

招股书里还有几组值得记住的数：IPO 后亚马逊预计持股约 14.7%、谷歌约 13.7%，若亚马逊可转债全部转换，其持股可达 23.8%；因限制性股票单位归属调整，公司一次性计入约 65 亿美元股权激励费用；市场认购需求接近发行股份的 **7 倍**，公司优先向现有投资者配售。另据 Latent Space 引述，S-1 显示 Anthropic 2026 上半年营收 163 亿美元，算力成本占营收比例从 251% 降到 48%。

质疑同样存在。按最高价与全部股本推算，市场给出的估值上限到过 1.4 万亿美元；澳大利亚最大养老金基金的高管公开表示，这一估值水平带有非理性成分。今天将是定价日，最终数字会回答所有争论。

**核心观点**：这份招股书最有信息量的不是募资额，而是"算力成本从 251% 降到 48%"这一行——它说明前沿实验室的商业模型第一次接近可持续，而这正是 1.4 万亿美元估值唯一站得住的支点。同时，OpenAI 选在定价前夜发布更便宜的模型，本质是在提醒承销商：这条护城河的价格正在被快速重估。

来源：[IT之家·上市文件细节](https://www.ithome.com/1/028/599.htm) · [Anthropic·路演启动](https://www.anthropic.com/news/roadshow-launch)

另见：[Latent Space·S-1 数据](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)

### ⭐ 英伟达交卷：营收翻倍的同一天，关掉中国 H200 的门

11 月 17 日，英伟达公布 2027 财年第三季度财报：营收 **1158 亿美元**、同比增 103%，数据中心业务 1076 亿美元、同比增 110%；前三季度归母净利润 1832.97 亿美元、同比增 137.72%。这是黄仁勋 11 月 12 日辞任 CEO 后的第一份财报，指引高于市场预期。

同一天，代 CEO Colette Kress 在电话会上确认：英伟达将**不再向中国销售 H200** 芯片，退出由黄仁勋与特朗普政府撮合、美国抽取 25% 关税的那笔交易。她同时表示，公司会"克制且有选择地"支持新兴云厂商；受此影响，CoreWeave 与 Nebius 盘后涨超 **9%**。

治理层面的震荡没有停。董事会主席哈维·琼斯明确表示，董事会无意让黄仁勋回归，称其因个人行为违反公司准则辞职、董事会一致接受辞呈；新设的国家安全与出口管制监督委员会开始运转。黄仁勋本人则打破沉默，称若董事会允许愿重返岗位，请愿签名已超过 18 万，开发者技术总监致信董事会警告核心人才流失，他的 X 账号已移除 CEO 头衔、只保留"创始人"。外部声音不一：贝索斯建议若不回归应优先内部选拔，美财长贝森特认为应在外部找新 CEO；《华尔街日报》称 SEC 正在调查公司披露是否误导投资者。

**核心观点**：把财报和人事放在一起看，英伟达第一次同时面对三个方向的不确定性——战略（中国收入归零）、治理（创始人离场后的权力结构）、监管（SEC 调查）。但它交出的数字说明，短期订单簿还没有感知到这些风险。真正需要盯的是一个时间差：如果 AI 资本开支持续，治理问题会被增长掩盖；一旦增速放缓，这三件事会同时变成折价理由。

来源：[NVIDIA·财报](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) · [IT之家·财报细节](https://www.ithome.com/1/028/575.htm) · [TechCrunch·H200 退出中国](https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/)

另见：[IT之家·董事会表态](https://www.ithome.com/1/028/580.htm) · [IT之家·黄仁勋回应](https://www.ithome.com/1/028/566.htm) · [WSJ·SEC 调查](https://www.wsj.com/business/sec-is-probing-nvidia-amid-departure-of-ceo-jensen-huang-ee7643f8)

### ⭐ 商汤 Loop-9B：9B 的参数，27B 的水平，10GB 的显存

11 月 17 日晚，商汤发布并开源 SenseNova Loop-9B。模型总参数约 9B，核心是 Loop 结构：把第 4–27 层组成共享权重的循环模块、执行两次，一次前向传播完成 **56 次**解码器层计算，等于用 9B 的参数买到了更深的计算图。双流 mHC 负责两条残差流之间的信息路由，注意力按三层线性、一层全注意力交替，上下文最高 512K。

工程指标比榜单更有说服力：4bit 量化后权重约 **4.9GB**，部署显存需求低到 10GB 以内；4bit 权重加 8bit KV 缓存跑 256K 长上下文，显存约 15GiB。官方在发布首日同步提供 AWQ 4bit 版本，并放出权重与代码。

效果上，它的对标对象是 27B 级模型而非同级：NL2Repo 得 **41.36**，接近 Qwen3.8-27B 的 44.60；AIDABench 得 **65.31**，略高于后者的 65.01。也就是说，它在 Agent、数据分析类任务上追平了**近三倍参数量**的模型，代价是纸面知识密度可能更低。

产业侧的配合几乎同步：寒武纪宣布完成 Day 0 适配，基于 vllm_mlu 把循环层静态展开为 56 个顺序层，复用标准调度与 KV cache，并针对 mHC 的 Sinkhorn 迭代自动生成 Triton 融合算子。这意味着国产芯片在模型发布当天就能跑。

**核心观点**：在算力与显存受限的现实约束下，"重复计算同一组权重"正在成为一条独立的 scaling 路线——Loop-9B 之外，今天的 Loopback Transformer 论文与商汤此前的 Preview 版都指向同一结论：深度可以借用，宽度和参数不能。对做私有化部署的人来说，10GB 显存这个门槛比任何榜单分数都重要，它把"能跑前沿级 Agent"的硬件预算拉回到了消费级显卡。

来源：[IT之家·模型发布](https://www.ithome.com/1/028/534.htm) · [IT之家·寒武纪 Day 0 适配](https://www.ithome.com/1/028/568.htm) · [Hugging Face·模型合集](https://huggingface.co/collections/sensenova/sensenova-loop)

### ⭐ 中国旗舰模型集体收紧网攻能力：一次发布前的数据手术

11 月 17 日，彭博社报道称，阿里、腾讯、月之暗面最新一代模型普遍限制了网络进攻能力。具体做法各不相同：Qwen4-Max 在训练数据中刻意过滤可用于攻击的材料，保留漏洞检测等防御能力，且该版本暂不公开权重，用户无法自行部署无审查版本；腾讯在 Hy4 正式版发布前就把漏洞利用生成数据从训练流程中剔除；月之暗面在 K3.1 Pro 的后训练两个阶段移除攻击相关材料，过滤后模型在内部漏洞利用基准上得 **81.0%**，低于未过滤版本的 90.5%；智谱则在开放 GLM-5.3 权重前做了安全审查。

背景是真实发生的攻击。CrowdStrike 10 月底披露，一个名为 **VAPOR PANDA** 的组织用 DeepSeek 模型配合 ARTEX 框架，在 11 天窗口内针对至少 **14 个国家的 200 余家机构**发起入侵。腾讯首席 AI 科学家姚顺雨 11 月 7 日表示，模型的网络能力以及"很快到来的生物能力"正触及可能造成实际危害的阈值。

制度侧也在收紧。商务部与科技部 10 月 16 日就修订《中国禁止出口限制出口技术目录》公开征求意见，拟将 AI 驱动的恶意代码生成与变异等 23 项技术纳入管制；国家发改委官员表示正在加快推出面向 AI 开发者的安全标准。安全公司 Fangcun AI 创始人李晓健对彭博社的判断是：剔除攻击性材料是在成本与效果之间的平衡，但"目前没有方法能完全消除模型的风险"。

**核心观点**：这是一次典型的"发布前治理"——不靠上线后的过滤层，而是在训练数据与后训练阶段就把能力剪掉，代价是明确的（内部基准掉 9.5 个百分点）。它同时改变了两件事：开源社区拿不到最强的开放权重版本，闭源用户拿到的是一个"能力被设计过"的产品。对做安全评测的人来说，这意味着评估基准本身正在被模型厂商反向优化，外部独立评测的重要性进一步上升。

来源：[IT之家·彭博社报道](https://www.ithome.com/1/028/133.htm)

### ⭐ Simon Willison 的外部沙箱：让编码智能体在一台"可抛弃的电脑"上跑

11 月 17 日，Simon Willison 发布与研究团队 Prime Radiant 合作的"**外部沙箱**"方案。思路是把智能体运行的环境和执行代码的环境彻底分开：智能体在 Mac 上思考、写代码，代码被发送到 WebAssembly、QEMU 或 Apple Container 里执行，机器本身只是宿主，坏掉的永远是那个一次性容器。

方案里有两个细节值得抄：一是**允许列表代理**（allow-list proxy），容器内的网络请求必须经过宿主的代理，只有白名单域名能出去；二是**凭据替换**（credential replacement），智能体看到的 token 是假的，真 token 只在代理出口处注入——这样即使提示词注入成功，攻击者也拿不到可用的密钥。

他的出发点很具体：本地模型越来越可用，但让一个可能被提示注入的模型直接在你机器上跑 `rm -rf`，风险与收益不成比例。沙箱化之后，"试一试本地模型"这件事的成本才真正降到可接受。

**核心观点**：智能体安全正在从"过滤提示词"转向"限制爆炸半径"。这套方案的价值不在于技术新颖，而在于它把企业级的安全实践（网络白名单、秘密管理、不可变基础设施）搬到了个人开发者的桌面上，而且用的是现成的开源组件。可以预期的下一步是标准化：沙箱镜像、权限清单、审计日志如果形成通用格式，智能体应用就能像容器一样被打包和审查。

来源：[Simon Willison](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) · [Latent Space·AI News](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)

### ⭐ 学习率调度遇到两条岔路：变分估计最优曲线，或者干脆不衰减

11 月 17 日同一天出现了两篇方向相反的预训练工程文章。

苏剑林在「科学空间」解析了一篇关于权重归一化训练中学习率调度的论文。论文的做法是先把训练动态简化成**一维微分方程**，再在方程约束下用变分思想最大化某个目标，从而解出最优调度曲线。他在文中强调，这个工作最吸引人的地方不是最终公式，而是提供了一套把"训练直觉"翻译成"调度形状"的**通用框架**——调度不再靠调参试出来，而是从假设里推导出来。

Sebastian Raschka 则在博客里做了一份横向统计：**cosine decay**（Llama 3、OLMo 3、GLM-5、Kimi K3、Phi-4）、**warmup-stable-decay**（DeepSeek V3/V4/V4.1-Flash、Kimi K2、Nemotron 3、MiniMax M2），以及第三条刚冒头的路线——**完全不衰减**，用恒定学习率加最后若干 checkpoint 的权重平均（Kolibri-1、DatologyAI 的模型）。他的判断是：不承诺总训练长度，工程上最省心。

**核心观点**：两篇文章合起来是一个信号——"训练多久"这个超参数正在被重新审视。变分路线想用数学消灭调参，无衰减路线想用平均消灭终点，两者都在回答同一个问题：当模型训练越来越长、越来越贵，任何需要提前承诺训练步数的设计都会变成负担。对做预训练或微调的人来说，无衰减加权重平均是最容易抄的一条，成本几乎为零。

来源：[苏剑林·科学空间](https://spaces.ac.cn/archives/12010) · [Raschka·Pre-Training Without Learning Rate Decay](https://sebastianraschka.com/blog/2026/llm-pretraining-without-learning-rate-decay.html)

---

## OpenAI

### ChatGPT 上线销售场景：Sales 插件与 30 多个合作插件

11 月 17 日，OpenAI 推出 ChatGPT for Sales，核心是一个 Sales 插件：研究潜在客户、准备提案、更新 CRM、推进交易，全部在对话里完成。同时上线 30 多个新建或增强的合作伙伴插件，覆盖面从数据查询到会议记录。这是 OpenAI 第一次按职能部门而不是按行业打包产品，与此前的 Healthcare、Law 形成同一套思路。

来源：[OpenAI](https://openai.com/index/introducing-chatgpt-for-sales)

### Astra for Law：24 个法律领域评测排名第一

同日，OpenAI 发布基于 GPT-6.2 Astra 的 Astra for Law，称其在一项覆盖 **24 个法律领域**的发布评测中位列第一，ChatGPT Enterprise 客户可通过 Trusted Access Program 申请访问。法律是少数"错误成本极高"的场景，OpenAI 选择在这里公布对照评测，显然是想把 Astra 的专业定位立住。

来源：[OpenAI](https://openai.com/index/astra-law-6-2)

### 与北约及盟国网络机构合作：用 AI 找漏洞、先修再披露

OpenAI 宣布与北约及盟国网络安全机构合作，帮助"可信防御方"发现漏洞、测试修复并保护关键系统。合作框架延续了此前的 **Patch the Planet** 思路：先由防御方拿到漏洞信息，修补完成后再进入公开流程。

来源：[OpenAI](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)

### OpenAI for Chile：与智利政府合作推动公共部门 AI

OpenAI 与智利政府达成合作，支持负责任的 AI 采用、建设公共部门技能，并帮助本地创业公司开发应用。拉美正在成为各家争夺**政府客户**的重点区域。

来源：[OpenAI](https://openai.com/index/introducing-openai-for-chile)

---

## Google DeepMind / Gemini

### Tasks in Gemini 在六国免费，接入 Workspace

11 月 17 日，Google 宣布 Gemini 的 Tasks 功能在**六个国家**免费开放，美国用户先拿到新功能，并与 Google Workspace 深度集成——可以直接在 Gmail、日历、Docs 之间替你完成任务。这是把"智能体代办"从付费墙后面推到默认入口的一步。

来源：[Google](https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/)

### AlphaGenome 2：从组织平均走到单个细胞类型

DeepMind 发布 AlphaGenome 2，把基因组变异预测从"组织平均"细化到"细胞类型与细胞状态"。新模型是条件模型：输入一段百万字母的 DNA 序列加一个生物条件（可从参考目录选细胞类型，也可用细胞编码器从用户自己的单细胞实验现场生成），预测变异对基因表达的影响。

训练数据超过 **1 亿个单细胞谱**、覆盖 68 种组织。DeepMind 称新模型识别出的"改变基因表达的变异"数量几乎是上一代的两倍，并且能对没见过的细胞状态做预测。非商业研究可通过 AlphaGenome API 使用，商业研究走 Google Cloud 私有预览。

来源：[DeepMind](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease)

### Gemini 隐私控制更新：可以保留记录，但不用于训练

Google 更新 Gemini 应用设置，允许用户在保留聊天记录的同时选择不把记录用于模型训练，保存期限仍可调整、记录仍可手动查看删除。若用户关闭新的"历史记录"设置，之后产生的对话仍会保存约**两个月**，用于回复、处理反馈与安全目的。

来源：[IT之家](https://www.ithome.com/1/028/581.htm)

---

## Anthropic / Claude

### DeepMind 首席战略官跳槽 Anthropic，人才流向已成趋势

11 月 16–17 日，谷歌 DeepMind 首席战略官 Jasjit Sekhon 确认离职并加入 Anthropic，将负责让 Claude 的知识与判断建立在严格、可靠的事实基础上。Sekhon 是统计学家，研究方向包括因果推断，曾任教于哈佛、伯克利与耶鲁，2018 年起在桥水基金任高级科学家兼 AI 负责人，今年 3 月才加入 DeepMind。

据英国数据公司 Zecki 统计，过去一年离开 DeepMind 的员工中，**25% 加入 Anthropic**，21% 去 Meta，14% 去 OpenAI。此前 Noam Shazeer 转投 OpenAI，AlphaFold 共同发明人 John Jumper 加入 Anthropic。

来源：[IT之家](https://www.ithome.com/1/028/360.htm)

### Claude Platform 支持关联计费

Anthropic 在 Claude Platform 上线**关联计费**（Linked Billing），让团队可以把不同工作区的用量归集到同一账单。对刚起步的企业客户来说，这是采购流程里最常被卡住的一环。

来源：[Claude](https://claude.com/resources/articles/linked-billing-on-claude-platform)

### Claude Code 加入实验性 Code Mode

Claude Code 上线实验性的 Code Mode，让模型用写代码的方式调用工具，而不是逐个发起工具调用。同一天社区还传出，Claude Code 桌面版已能在 iOS 模拟器里跑 iPhone Duo、并折叠展开设备测试布局。

来源：[B站·白鸦 AI 日报](https://www.bilibili.com/video/BV1MasC6qEhJ) · [Latent Space](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)

---

## 国内大厂动态

### 快手可灵 Kling Image 4.0：原生 8K、单图 2000 字

11 月 17 日深夜，快手可灵上线 **Kling Image 4.0**，同时向企业客户与开发者开放 API。模型采用"理解生成统一"架构，三项升级指向专业设计场景：**原生 8K** 输出；单张图内可生成 **2000 字**，内置 70 多种商用字体、支持 7 种语言；一次描述最多生成 10 张风格连贯的系列图，并能规划电商详情页与网页长图。输入上限 1.5 万 token，另内置 110 多种影调预设。

来源：[IT之家](https://www.ithome.com/1/028/563.htm)

### 国行 iPad 与 Mac 上线 Apple 智能，Siri 与写作工具接入千问

11 月 17 日，iPadOS 与 macOS 27.3 开发者预览版 Beta 2 为国行设备新增 **Apple 智能**。搭载 M 系列芯片的 Mac 与 iPad 均支持，A17 Pro、A20 Pro 的 iPad mini 也在范围内。国行版本不含 Siri AI，Siri 与写作工具等接入的是**千问大模型**，集成方式类似其他地区设备接入 ChatGPT。该服务已完成备案，适用场景覆盖手机、平板、笔记本。

来源：[IT之家](https://www.ithome.com/1/028/039.htm)

### 李彦宏在 APEC 警告 AI 泡沫：上层应用落地不及预期

11 月 17 日，李彦宏在深圳 APEC 工商领导人峰会上表示，当前 AI 行业上层应用落地成效不及预期，**存在泡沫风险**；同时他对长期趋势保持乐观，认为百度 AI 业务收入占比会持续提升。同场他还称，无人驾驶出租车的安全记录大约是人类司机的 **10 倍**。

来源：[IT之家](https://www.ithome.com/1/028/225.htm)

### 字节 TRAE 账号今日起自动升级为豆包飞书账号

字节跳动宣布，自 2026 年 11 月 18 日起，TRAE 账号将自动升级为豆包飞书账号。这属于账号体系统一，但也意味着编程工具与办公套件的用户身份正在合并。

来源：[IT之家](https://www.ithome.com/1/023/552.htm)

### 传闻：DeepSeek 算力吃紧，考虑开启付费服务

据部分中文 AI 日报转述媒体报道，DeepSeek 因算力压力正在考虑开启付费服务。此前 11 月 16 日已有用户在免费端看到"不再支持超过 7 天不活跃的长对话"等限额提示，但官方始终没有公告，付费方案也未见任何官方文件。列入本条仅为跟踪算力这条线，不作事实结论。

来源：[B站·白光 AI 日报](https://www.bilibili.com/video/BV1qhs666EM7)

---

## 海外大厂动态

### Isomorphic Labs 完成 50 亿美元 C 轮

11 月 17 日，Demis Hassabis 领导的药物 AI 公司 Isomorphic Labs 宣布完成 **50 亿美元 C 轮**融资，Greenoaks 与 Sequoia Capital 共同领投，a16z 等新投资者加入，Alphabet 继续投入，Thrive、MGX、GV、CapitalG、淡马锡、英国主权 AI 基金等老股东跟投。资金将用于推进基础模拟模型、扩大药物候选项目、建设 AI 驱动的生物工程基础设施。

在 Anthropic 定价、英伟达财报的同一天，这笔融资说明资本对"AI for Science"的定价远没有冷却。

来源：[IT之家](https://www.ithome.com/1/028/533.htm)

### Perplexity 年化收入破 10 亿美元，2026 年内涨 4 倍

Perplexity CEO Aravind Srinivas 在公开活动中表示，公司年化营收已突破 **10 亿美元**。年初这个数字还不到 2.5 亿，8 月超过 7.5 亿。按同类智能体公司的倍数估算，其估值区间约 **300 亿至 500 亿美元**——前提是单位经济模型站得住。近期产品线包括 Computer（本地运行）、Automations、Teammates、Monitor API，以及拥有上万块 GPU 的 Frontier Research 实验室。

来源：[Latent Space·AI News](https://latent.space/p/ainews-perplexity-hits-a-1b-revenue-run-rate-up-4x-in-2026/)

### AMD 82 亿美元完成收购 World Labs，李飞飞出任执行副总裁兼首席科学家

11 月 16 日，AMD 宣布完成对 World Labs 的收购：全股票交易，向原股东定向发行 1497.8 万股，估值约 82 亿美元，从 9 月 28 日签约到 11 月 13 日交割只用了 46 天，是 AMD 史上第二大并购。李飞飞出任执行副总裁兼首席科学家，直接向苏姿丰汇报；Justin Johnson 与 Ben Mildenhall 留任，团队在 AMD 内部作为独立前沿研究组织继续做基础模型。

World Labs 的核心资产是空间智能模型 **Atlas**：以相机位姿为条件预测下一个视角，在约 50 万次人类盲测中排名第一，可生成超过 **60 秒、1440p** 的连贯视角视频，并已有机器人"仿真训练、零样本真机部署"的案例。

来源：[量子位](https://www.qbitai.com/2026/11/510695.html)

### Genesis AI 完成 5 亿美元 A 轮，估值 35 亿美元

法国通用机器人公司 Genesis AI 完成 **5 亿美元 A 轮**融资，估值 35 亿美元，是欧洲机器人行业规模最大的融资之一。投资方包括施密特、Khosla Ventures、英伟达与法国政府支持的 Bpifrance。公司由前 Mistral AI 研究人员联合创立，将用资金提高通用机器人 Eno 的产量、扩大数据采集与训练规模。

来源：[IT之家](https://www.ithome.com/1/028/605.htm)

### Suno 上线 Visuals：把歌变成最长 15 秒的可续接短片

Suno 推出 Visuals 功能，用户可把曲库中的歌曲生成最长 15 秒的视频片段，再拼接、编辑、重新提示成完整 MV，底层使用基于 MiniMax 的模型。视觉积分与歌曲积分分开计费。

来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-11-17/ai-music-generator-suno-to-let-users-create-music-videos)

### Cloudflare 自称"neolab"：两款系统一模型之后，还要做 LLM

在 AI Engineer Code Summit 上，Cloudflare AI 平台产品负责人 Michelle Chen 介绍了 **Clef 与 Clairic** 两款"系统一"模型：Clef 是受 TypeSafe 的 Jev 启发的决策模型，Clairic 是新型"抽取"模型。她在会后采访中透露，Cloudflare 不会止步于此，正在实验推理模型与其他 LLM，但路线是**后训练而非从零预训练**——"我们团队大多数人只做后训练"。

来源：[Latent Space](https://latent.space/p/cloudflare/)

### 苹果改 Mac 权限机制，目标直指 AI 智能体

macOS 27.3 Beta 2 起，苹果把"完全磁盘访问"与"设备控制与数据访问"拆分为"系统与应用保护覆盖"和"辅助功能"两项，鼓励用户只开放单个应用或文件夹，并可设为"**每次询问**"；应用跨应用控制时菜单栏会出现透明度指示器。古尔曼评论称，这是苹果**提前两年**为自家 AI 智能体铺路：先让用户习惯"AI 要权限时必须谨慎"。

来源：[IT之家](https://www.ithome.com/1/028/116.htm)

---

## AI 研究前沿

### 米哈游开源 Gamer：把一万小时键鼠轨迹当预训练语料

米哈游《崩坏》系列 AI 团队公布通用视觉语言动作模型 Gamer，可自主游玩 2D 与 3D 游戏：不读游戏内部数据、不依赖专用 API，以每秒 5 帧采集画面为输入，输出相当于 30Hz 的键鼠指令。团队用超过 1 万小时跨游戏操作轨迹做持续预训练，配合稀疏思维指令微调与时序感知强化学习；自研 Streaming-vLLM 把 H200 上的端到端延迟从 1306 毫秒降到 **65.12 毫秒**。Gamer-RL 在 40 项未见过的迷你游戏上平均成功率 49.7%。

这篇论文在 Hugging Face 日榜拿到 118 个赞，是今日第二热的论文，仅次于一篇关于智能体机器人的综述。

来源：[IT之家](https://www.ithome.com/1/028/503.htm) · [Hugging Face](https://huggingface.co/papers/2611.18397)

### K2-Horizon：从 0.9B 到 375B-A23B 的六个全开源模型

来自 Institute of Foundation Models 的 **K2-Horizon** 一次放出六款完全开放的语言模型，跨度从 **0.9B 稠密模型到 375B 总参、23B 激活的 MoE**，覆盖数学、科学、软件工程、深度研究与办公自动化。今日榜单 55 赞。

来源：[Hugging Face](https://huggingface.co/papers/2611.21003)

### ScaleVLA：把视觉语言动作模型推到 5520 亿参数

研究团队把 VLA 模型规模推到 **552B**，论点是前沿视觉语言模型（如 GPT-6 Astra）在机器人控制上的表现说明"广谱预训练的知识对物理动作同样有价值"，而现有 VLA 策略的规模都远小于此。今日榜单 37 赞。

来源：[Hugging Face](https://huggingface.co/papers/2611.21607)

### SWE-CoWork：当编码智能体被当成"数字员工"来考核

Tokenwave.AI 构建了一套接近真实企业交付的软件工程任务基准：从需求澄清、实现、验证到交接。结论不乐观——现有编码智能体**即使局部测试通过，也很少能完整走完全流程**。今日榜单 32 赞。

来源：[Hugging Face](https://huggingface.co/papers/2611.20218)

### 今日论文速览

以下几篇今日在 Hugging Face 榜单靠前，涵盖机器人、编码智能体与推理优化三个方向。

智能体机器人综述提出以"具身 System 2"为核心的新范式与统一评测框架，124 赞为今日榜首（[2611.18359](https://huggingface.co/papers/2611.18359)）；VibePrevisBench 用 Blender 4D 场景生成来考核编码智能体（[2611.15789](https://huggingface.co/papers/2611.15789)，88 赞）。

推理侧，MMFlash 让视觉语言模型的投机解码快 **3.58 倍**且无损（[2611.18482](https://huggingface.co/papers/2611.18482)）；Loopback Transformer 给残差循环结构一个统一视角（[2611.07226](https://huggingface.co/papers/2611.07226)）。安全侧，SPILLWAY 把"目标准入"与"内容消毒"拆成两道闸，用于防御工具型智能体的提示注入（[2611.07222](https://huggingface.co/papers/2611.07222)）。

---

## 行业观点与解读

### 苏剑林：最优学习率调度可以被"推"出来

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[科学空间](https://spaces.ac.cn/archives/12010)

### Raschka：2026 年出现第三条路——不衰减

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Ahead of AI](https://sebastianraschka.com/blog/2026/llm-pretraining-without-learning-rate-decay.html)

### Simon Willison：沙箱化之后，才敢试本地模型

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Simon Willison](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/)

---

## 值得关注的视频

### 白鸦 AI 日报 11-18：微软七款模型与国内图像模型

章节完整：微软 MAI 系列怎么把价格打下来、可灵 Image 4.0 的 8K 与长文字、Gemini 任务六国免费、AI Studio 构建安卓应用、Claude Code 的 Code Mode、Devin Bots、英伟达财报。顶部快讯还补了 ChatGPT for Sales、Astra for Law、Anthropic 的股东结构。**信息密度在当天最高**。推荐观看。

来源：[B站](https://www.bilibili.com/video/BV1MasC6qEhJ)

### 两个人在吃饭 第 41 期：GPT-6.2 便宜两成

本期把 GPT-6.2 的定价、105 万上下文与同一天的攻防评估放在一起讲，附了官方发布页、OpenAI 官方帖、OpenCode 的 GLM 5.3 promote 帖与 Cursor 安全事件调查结论的原始链接。适合用来快速核对数字。

来源：[B站](https://www.bilibili.com/video/BV1QTsy6kECp)

### 肥鱼速览 11-18：13 条动态一次过

13 条包括英伟达财报、黄仁勋表态、GPT-6.2、Anthropic 定价、微软七款模型、Isomorphic 50 亿美元、SC26 的 Rubin HPC、Suno Visuals、Replit Missions，以及"**编程智能体六成花费打水漂**"的评测。每条都能追到原始来源。

来源：[B站](https://www.bilibili.com/video/BV1Rcsy62EqT)

### 白光 AI 日报 第 48 期：DeepSeek 的算力账本

把国内的算力与付费两条线串起来：华为具身世界模型、DeepSeek 算力吃紧与付费传闻、AI 办公三家竞争。附了阿里 Qwen 官方关于 Qwen4-Max 的**推文链接**，是本条国内传闻唯一的可追溯出处。

来源：[B站](https://www.bilibili.com/video/BV1qhs666EM7)

### Latent Space：Cloudflare 为什么自称 neolab

Michelle Chen 讲 Cloudflare 从基础设施公司变成"模型公司"的逻辑：先做两款便宜的系统一模型，再往后训练方向扩到 LLM 与推理模型。对关心"**模型公司**"这个身份边界如何移动的人，这期提供了一个很好的样本。

来源：[Latent Space](https://latent.space/p/cloudflare/)

---

## 灵感种子

**成本曲线已经跑在能力曲线前面。** 同一天，OpenAI 用 5% 的成本追平 Fable 5.2，微软用 5% 的成本做出 Opus 5.5 的九成水平，商汤用 9B 参数追平 27B。三家做的是同一件事：把"够用"的门槛往下压一个数量级。对做产品的人，这意味着模型选型的默认答案会从"选最强"变成"选刚好够用、便宜十倍的那个"；而中间会长出一层新的基础设施——按任务类型动态路由、带成本预算控制的模型网关。这类东西现在还是各家自己写的胶水代码，没人做成标准件。

**发布日历第一次被资本市场编排。** OpenAI 选在 Anthropic 定价前一天发模型，Anthropic 则抢在感恩节前完成定价，英伟达把财报和人事变动放进同一周。模型发布的时间点过去由技术节奏决定，现在由路演节奏决定。读简报的人可能需要养成一个新习惯：先看财报日历，再读模型发布——发布顺序本身就是一种竞争手段。

**"重复用同一组权重"正在成为受限算力下的 scaling 路线。** 商汤的 Loop-9B 把 32 层循环成 56 层计算，10GB 显存就能跑；今天的 Loopback Transformer 论文在给残差循环找统一框架；Gamer 用 Streaming-vLLM 把延迟压到 65 毫秒，靠的也是推理侧的工程而不是更大的模型。这条线的共同点是：不追求更多参数，追求单位参数被计算更多次。在 HBM 供应紧张的年份，它可能比堆参数更现实。

**安全正在从"对齐论文"变成两个可以收费的工程环节。** 上游是发布前的数据手术——三家中国厂商同一周砍掉网攻能力，月之暗面为此付出 9.5 个百分点的内部基准。下游是发布后的可观测性——微软拉着 40 多家组织定义"观察、验证、控制"，Simon Willison 的沙箱则把爆炸半径压到一台容器。中间缺的那块很明确：一个能同时说清"这个模型被剪掉了什么"和"它在你的环境里能碰到什么"的评测产品。现在做评测的公司大多只做后半句。
