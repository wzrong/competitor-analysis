---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-12

## 今日概览

> 一天之内，AI 世界的两个"定价锚"同时松动。英伟达董事会开始为没有黄仁勋的未来做准备——《华尔街日报》称正准备罢免、《纽约时报》曝出第二段办公室关系、彭博社称已在物色继任者与临时 CEO 方案，盘后股价一度跌 9%。另一头，Anthropic 的路演被认购到"数倍于发行量"，承销商考虑把发行价抬到 70–78 美元之上，估值冲回 1.5 万亿美元。技术侧同样在拆地基：Anthropic 披露 Mythos 只用三天就把 Claude 移植到 AMD GPU，谷歌则用 Gemini Decision 1 把"决策"从生成里拆出来单独定价。

- **英伟达董事会酝酿换帅**：罢免议案、继任者搜寻、临时 CEO 方案三线并进，盘后市值跌至 4.19 万亿美元。来源：[IT之家](https://www.ithome.com/1/025/829.htm)·[Reuters](https://www.reuters.com/technology/nvidia-is-preparing-oust-ceo-jensen-huang-wsj-reports-2026-11-11/)
- **Anthropic IPO 超额认购**：承销商考虑上调发行价，估值或破 1.5 万亿美元，募资有望超 1000 亿美元。来源：[IT之家](https://www.ithome.com/1/025/526.htm)
- **Mythos 三天完成 AMD GPU 移植**：路演视频披露四个芯片家族并行训练与服务，CUDA 适应成本被 AI 自己抹平。来源：[The Decoder](https://the-decoder.com/anthropic-says-ai-is-eroding-nvidias-cuda-lead-cutting-an-amd-chip-switch-from-months-to-three-days/)
- **Gemini Decisions API 上线**：单次前向对千条是非题打分，输出免费，每百万输入 0.1 美元。来源：[Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)
- **AlphaGenome 2 转向单细胞条件预测**：致病变异识别量接近翻倍，可泛化到未见过细胞状态。来源：[DeepMind](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ 英伟达董事会准备罢免黄仁勋：罢免、寻人、临时 CEO 三线并行

11 月 11 日美东时间，三家媒体先后给出同一条主线。《华尔街日报》报道英伟达**董事会正准备解除黄仁勋的 CEO 职务**，最早在周三召开专项会议表决；彭博社随后称董事会已**聘请外部机构物色继任者**，并考虑在过渡期任命临时 CEO；《纽约时报》则披露五名前员工指控黄仁勋存在第二段办公室关系，对象是向他直接汇报的医疗健康业务副总裁金伯利·鲍威尔（48 岁），两人均已婚。

这轮升级发生在 11 月 10 日他公开承认"对妻子不忠"之后。市场反应剧烈：英伟达股价周二收跌 **5.47%**，叠加周一 4% 以上的跌幅；盘后最低触及 157.96 美元，较收盘价再跌 **9.08%**，对应市值 4.19 万亿美元。Polymarket 上"2027 年 7 月前离任"的概率升至 **80%**，其长女黄敏珊成为接任 CEO 的热门押注。

董事会面临的是一道没有标准答案的选择题：解除职务，公司将失去自创立以来唯一一位 CEO，而 AI 算力分配正处在最紧绷的时点；保留职务，则要面对国会议员、投资者、客户与员工的持续审查。此前董事会已委托 Wachtell Lipton 与前联邦检察官 Joon H. Kim 开展独立调查。

**核心观点**：英伟达过去两年的风险叙事一直围绕需求、供应与出口管制，这家公司第一次把最大的不确定性挂在某一个人的私德上。更值得注意的是"继任者真空"——一家 4 万亿美元市值、几乎垄断训练芯片供给的公司，没有公开的第二号技术人物可以让市场放心。这种结构性脆弱，比任何一份出口禁令都更难对冲。

来源：[IT之家](https://www.ithome.com/1/025/829.htm) · [Reuters](https://www.reuters.com/technology/nvidia-is-preparing-oust-ceo-jensen-huang-wsj-reports-2026-11-11/) · [IT之家·SEC 候选人](https://www.ithome.com/1/025/852.htm)

另见：[IT之家·股价](https://www.ithome.com/1/025/855.htm) · [IT之家·第二段关系](https://www.ithome.com/1/025/857.htm) · [WSJ](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad)

### ⭐ Anthropic IPO 被买到超额：承销商考虑上调发行价，估值或破 1.5 万亿美元

路演启动不到一天，局面就反转了。《金融时报》援引五位知情人士称，在认购需求"异常旺盛"的推动下，承销商已表示**预计会把发行价上调至每股 70 至 78 美元之上**，目标估值可能因此升破 **1.5 万亿美元**，IPO 募资总额有望**突破 1000 亿美元**。彭博社的说法更直接：这单 IPO 已被**数倍超额认购**。高盛与摩根士丹利牵头承销。

几个细节拼出了完整的定价图景。公司 10 月年化营收已达 **810 亿美元**，第三季度营收 170 亿；三位投资方称管理层现在更在意"募到尽可能多的钱"去支撑算力开支，而不是死守某个估值数字。晨星给出的合理股权价值是 1.7 万亿，但区间从 **5000 亿到 3 万亿**——这个跨度本身就是市场对 AI 热潮缺乏共识的证据。

上市前的场外交易已经在抢跑：一家纽约券商代售最高 5 亿美元的股份，报价比最终发行价**高 4%**；另有机构通过 SPV 提供 12.5 亿美元份额，对应估值 1.5 万亿。Anthropic 已开始限制 SPV 使用，并警告不认可部分二级经纪商的交易。

**核心观点**：定价权在这一周从发行人手里滑到了认购方手里。原定 1.4 万亿的上限被需求顶回去，说明公开市场对"增速 + 算力订单"这套叙事的买单意愿仍在；但把募资额置于估值之上，也意味着公司自己清楚——真正稀缺的是现金，而不是纸面估值。

来源：[IT之家](https://www.ithome.com/1/025/526.htm) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-11/anthropic-s-mega-ipo-is-said-to-be-multiple-times-oversubscribed)

### ⭐ 三天把 Claude 移植到 AMD GPU：CUDA 护城河第一次被模型自己填平

Anthropic 路演视频里最硬的一段，来自联合创始人兼首席算力官 Tom Brown：公司现在**同时在 AWS Trainium、谷歌 TPU、英伟达 GPU 与 AMD GPU 四个芯片家族上训练和服务 Claude**。这个"多芯片"赌注在几年前被业内普遍认为不值得做——每块芯片都要一套定制软件栈与推理栈，昂贵且耗时。

今年的实测给出了新答案。Anthropic 首次接入 AMD GPU，没有派出数十名工程师，而是让前沿模型 **Mythos 自己去试**：三天后 Claude 已经在 AMD 的 **MI355X** 上跑起来，几乎无人干预，模型自己移植或编写了接近 **100%** 的 kernel。作为对照，传统上一个新计算平台的适配通常要 6 至 12 个月。

如果这组数字站得住，被削弱的正是英伟达最坚固的那层——不是芯片，而是人力密集的软件适配工作。英伟达当前在 AI 芯片上的毛利率超过 **70%**，这个数字之所以能维持，前提是"迁移太贵所以没人迁移"。当迁移成本从"工程师月"压缩成"GPU 天"，定价权就会重新回到买方的算力池里。

**核心观点**：这是一次"可验证任务"的胜利——kernel 能否编译、能否跑通、性能是否达标，全部有客观验收标准，AI 恰好最擅长这类工作。把它和昨天的 AlphaProof Code 放在一起看，规律是一致的：先被智能体接管的，永远是能机器判定对错的工程环节。

来源：[The Decoder](https://the-decoder.com/anthropic-says-ai-is-eroding-nvidias-cuda-lead-cutting-an-amd-chip-switch-from-months-to-three-days/) · [Simon Willison](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) · [IT之家](https://www.ithome.com/1/025/736.htm)

### ⭐ Gemini Decisions API：把"决策"从生成里拆出来单独定价

11 月 11 日，谷歌发布 Gemini Decisions API 与底层的 Gemini Decision 1 模型。它不是聊天模型：你把一份多模态输入（文本、图像、音频、视频、PDF，最多 **256K token**）和最多 **1000 个独立问题**一起交进去，模型用**单次前向计算**给每个候选选项打分，返回概率与置信度，端到端延迟 150 至 250 毫秒。

定价是这次发布真正的杀招：每百万输入 token **0.10 美元**，**输出 token 不收费**。同一份输入无论问多少问题只计费一次，官方称在共享基准上比 Gemini 3.5 Flash-Lite 便宜近 **5 倍**。谷歌内部已用它做 Gemini Notebook 的模型路由、Stitch 的设计原型判定与搜索的安全检查。

这个品类在一周内被接力做成：创业公司 Jev 先发，OpenAI、Cloudflare、微软跟上，谷歌补上最后一个大厂位置。Simon Willison 的实测补了个有趣细节——面对"视频里有龙吗"这类是非题，Jev 与 OpenAI 干脆给 1.0 或 0.0，Gemini 则坚持给出不那么笃定的分数；同时它是三家之中唯一真正多模态的，Jev 只吃文本与 JSON。

**核心观点**：agent 系统里最贵的不是"生成一段话"，而是每秒要做几百次的"路由、质检、策略检查"这类小决策。把这类判断从自回归解码里剥离出来，等于把成本结构从"按字计费"改成"按判断计费"——这比任何一次模型分数提升都更能改变生产环境的账本。

来源：[Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) · [IT之家](https://www.ithome.com/1/025/858.htm) · [Simon Willison](https://simonwillison.net/2026/Nov/11/gemini-decisions-api/) · [The Decoder](https://the-decoder.com/google-joins-the-decision-model-wave-with-gemini-decision-1-scoring-1000-questions-in-a-single-pass/)

### ⭐ AlphaGenome 2：从"组织平均"走到"单个细胞状态"，致病变异识别接近翻倍

DeepMind 发布新一代 DNA 序列模型 AlphaGenome 2，核心改动是把架构从**并行预测多组织**改成**条件式模型**：输入百万字母长度的 DNA 序列，同时输入一个目标生物学条件（组织、细胞类型或细胞状态），模型只针对这一条件预测变异效应。

训练规模是 68 类组织、超过 **1.07 亿个单细胞图谱**。在覆盖 28 类原代免疫细胞的 TenK10K 数据集上，它识别到的因果变异占比达 **30%**（初代 16%），基因效应方向判断准确率 **43%**（初代 23%），均接近翻倍。初代模型曾复现的炎症性肠病案例——远端调控序列变异通过过度激活肠道巨噬细胞的 ETS2 基因致病——这次被逐细胞类型精确复现。

更实用的是零样本泛化：科研人员上传几十个细胞的单细胞 RNA 测序快照，模型压成细胞状态表征后即可预测从未见过的状态。在新冠 mRNA 疫苗数据上，它能区分疫苗激活的 T 细胞与静息 T 细胞，还揭示出与重症相关的变异在激活状态下干扰更强——这种效应在未激活细胞里完全看不到。

**核心观点**：基因组学的瓶颈正在从"测什么"转向"在哪种细胞里测"。把静态细胞图谱变成可条件查询的预测引擎后，GWAS 找到的数千个关联信号第一次能被落到具体细胞类型上——这是药物靶点发现最缺的一环。边界也要说清：目前只对非商业研究开放，且未获临床或诊断验证。

来源：[DeepMind](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/) · [IT之家](https://www.ithome.com/1/025/822.htm) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model)

---

## OpenAI

### 三季度营收 100 亿美元、环比增 50%，但调整后经营亏损扩大到 109 亿

据 WSJ 与 The Information，OpenAI 三季度营收 **100 亿美元**，环比增速从上季的 17% 跳到 **50%**，为去年同期的近 3 倍；调整后经营亏损从 101 亿升至 **109 亿美元**，股票薪酬另计 26 亿，利润率由 -150% 收窄至 **-109%**。企业业务翻倍并成为收入主体，ChatGPT 周活 12 亿、付费订阅 1 亿，广告产品 8 月年化收入已达 10 亿美元。

来源：[The Decoder](https://the-decoder.com/enterprise-sales-push-openais-quarterly-revenue-to-10-billion-though-it-still-trails-anthropic/) · [IT之家](https://www.ithome.com/1/025/560.htm)

### 12 月 11 日停用旧版语音模式，全面转向 GPT-Live

高级语音模式与标准语音模式将同日下线，用户自动切换到全双工的 GPT-Live；实时视频、屏幕共享与自定义 GPT 语音对话暂留旧模式。官方承认部分用户更喜欢旧版回答风格，社区已有取消订阅的声浪。

来源：[IT之家](https://www.ithome.com/1/025/567.htm)

### 为退伍军人提供一年免费 ChatGPT Plus

服役或退役未满 12 个月的美军人员可领取，已有超过 2 万人申领，用于简历、面试与职业转型。

来源：[OpenAI](https://openai.com/index/chatgpt-plus-for-veterans)

---

## Google DeepMind / Gemini

### AlphaGenome 2 发布：单细胞条件预测，致病变异识别接近翻倍

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[DeepMind](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model)

### Gemini Decisions API 上线，Decision 1 单次前向答千题

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) · [IT之家](https://www.ithome.com/1/025/858.htm)

### A2UI 1.0 稳定版发布：智能体可以直接"回"一个界面

谷歌开源协议的首个稳定版本上线，配套网页、Android、iOS 三端渲染器 SDK 与 Python、TypeScript、Dart 的智能体 SDK。新增双向功能调用与可访问性扩展；Atlassian、彭博社、字节跳动已在使用，渲染器可运行在 Claude、Gemini 等支持 MCP 应用的助手里。

来源：[IT之家](https://www.ithome.com/1/025/862.htm)

### 苹果 CarPlay 接入 Gemini：车内免提对话，记录同步回手机

即日起向全球 iOS 端 Gemini 用户逐步推送，覆盖 Gemini Live 已支持的全部语言，可连接 Gmail 与日历做当日简报与邮件总结。

来源：[IT之家](https://www.ithome.com/1/025/831.htm)

---

## Anthropic / Claude

### IPO 获数倍超额认购，承销商考虑上调发行价

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/025/526.htm) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-11/anthropic-s-mega-ipo-is-said-to-be-multiple-times-oversubscribed)

### Mythos 三天完成 AMD GPU 适配，四芯片家族并行

[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[The Decoder](https://the-decoder.com/anthropic-says-ai-is-eroding-nvidias-cuda-lead-cutting-an-amd-chip-switch-from-months-to-three-days/) · [IT之家](https://www.ithome.com/1/025/736.htm)

### MCP Apps 扩展预览：第三方应用可直接嵌进 Claude 全屏运行

新增 App Tools 与 Embedded Sites，开发者可以把完整应用界面放进对话侧栏甚至全屏，Claude 在授权后可直接修改当前页面、表格行或文件。Adobe、Atlassian、Box、HubSpot、Notion 已支持；同日 Anthropic 为 Pro 至 Team 用户提供一次免费额度重置。

来源：[IT之家](https://www.ithome.com/1/025/292.htm)

### 阿莫迪"十年攻克癌症"的预测引来医学界反驳

Vertex 执行董事长莱登称此类时间表是"彻头彻尾的胡说八道"，理由很具体：该公司测试过约 50 家 AI 公司从 1 万种化合物里筛选候选，没有一家独立拿出可用药物；临床试验与监管审批仍占研发周期的绝大部分。截至 2026 年，尚无 AI 设计的药物实现全面临床应用。

来源：[IT之家](https://www.ithome.com/1/025/617.htm)

---

## 国内大厂动态

> DeepSeek / Kimi / 豆包 / 智谱 等

### 阿里官宣 Qwen4，Qwen4-Max 预览版首发上线 Token Plan

官方口径是知识理解、世界感知、Coding 与 Agentic 能力同步进阶；千问办公、Qoder、千问 App、QwenStudio 第一时间接入。预览版按 Token Plan 计费，个人版月付 39 元起、新客折后 19.5 元。

来源：[IT之家](https://www.ithome.com/1/025/301.htm)

### 阿里开源 Qwen Code 1.0：把 Qoder 的 Harness 并入同一内核

统一事件模型、接入调度执行分层、推理与工具执行"手脑分离"，从"一个进程多个会话"演进到"多个节点多个会话"，并集中治理 MCP 配置与沙箱资源。以独立 Preview 分支开放。

来源：[IT之家](https://www.ithome.com/1/025/393.htm) · [GitHub](https://github.com/QwenLM/qwen-code)

### 百度发布 ERNIE 5.5 Flash Preview：280B 总参、14B 激活、百万上下文

后训练中间版本，API 已上千帆，权重承诺 **11 月 25 日前开源**。量子位的实测里，它只用 Python 就在 116 秒内生成 20 种画风的动画、用 11 小时做出 UE5.8 武侠游戏、约半小时在 Blender 里搭出苏州园林；官方称在 Terminal-Bench 等基准上与 Opus 5.5、GPT-6.1 Sol 同台竞争。

来源：[IT之家](https://www.ithome.com/1/025/451.htm) · [量子位](https://www.qbitai.com/2026/11/509224.html)

### 腾讯"元宝搜索"上线：可搜公众号与视频号，广告整块折叠

入口为 so.qq.com，基于千亿级索引重建理解、检索、排序到答案组织的链路，接入 157 个权威信源，广告与答案明确区分。官方称会用"递归自我进化"机制从使用反馈中改进搜索体验。

来源：[IT之家](https://www.ithome.com/1/025/471.htm)

### 张一鸣全员会：字节要做 Muse 类助手，承认预训练数据落后"几个数量级"

彭博社称字节计划数周内推出类似 Meta Muse 的 AI 助手。张一鸣在内部会上说 Seed 系列预训练数据集规模比美国顶尖对手小好几个数量级，真正追平 Anthropic、OpenAI 至少要等到 **2029 或 2030 年**，并强调不应过度依赖蒸馏。公司计划投入最高 **700 亿美元**，把 Seedance 做成领先的视频 AI 平台。

来源：[IT之家](https://www.ithome.com/1/025/726.htm)

### 华为麒麟 9050 新一代 NPU：业界首个 30B MoE 大模型上端

性能提升 140%、功耗降低 66%，支持 Transformer 引擎与 CANN 异构计算，端侧可离线跑 30B MoE，配合低比特量化与多级存算协同，落地到屏幕朗读、智拍 2.0、眼动翻页等功能。

来源：[IT之家](https://www.ithome.com/1/025/331.htm)

### 双 11 出现"Token 品类"：智谱、MiniMax、阿里云齐打五折

淘宝搜索 Token 即可进入 Token 充值中心：MiniMax 三款月卡全部 5 折，阿里云 Token Plan 5 折起，智谱周卡 5 折起，千问办公首月 3 折起，Qoder 月卡 3.3 折低至 19.9 元。大模型额度第一次作为独立消费品类登上电商大促。

来源：[量子位](https://www.qbitai.com/2026/11/509085.html)

### 昆腾动力：物流仓机器人拿下近 5000 台订单，供包效率每小时 1200 件

称重、量方、分拣供包场景完成 PMF 验证，双臂机器人已在多家头部电商与物流企业仓库落地，供包成功率 99%，开始进入规模化交付。

来源：[量子位](https://www.qbitai.com/2026/11/509281.html)

---

## 海外大厂动态

### 英伟达：董事会酝酿罢免黄仁勋，同日曝出第二段办公室关系

罢免表决、外部机构寻人、临时 CEO 方案在同一天被三家媒体披露，盘后股价一度跌 9%。 [⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[IT之家](https://www.ithome.com/1/025/829.htm) · [Reuters](https://www.reuters.com/technology/nvidia-is-preparing-oust-ceo-jensen-huang-wsj-reports-2026-11-11/)

### OpenRouter 正式并入 Stripe，交易金额约 75 至 80 亿美元

8 月宣布、11 月 10 日交割。平台已接入 80 多家供应商的 400 多款模型，服务超 1000 万开发者；10 月处理约 **790 万亿 token**，环比增 37%，其中 **76%** 来自智能体调用。

来源：[IT之家](https://www.ithome.com/1/025/833.htm)

### Helsing 发布 Clarity：把传感器数据加工成"目标建议"的智能体平台

数百个专用智能体并行处理传感器、开源情报与书面报告，识别部队、设施与阵地，再由人类逐次授权移交武器系统；公司强调欧洲本土开发、部署在客户自有基础设施，并称每次决策都记录责任人姓名。直接对标 Palantir 的 Maven。

来源：[The Decoder](https://the-decoder.com/helsing-built-an-ai-system-that-prepares-targets-for-weapons-systems-and-says-every-decision-will-carry-a-human-name/)

### 美联航禁止个人 AI 助手代订机票

出于隐私与监管考虑，AI 可以查航班与展示信息，但不能代替用户完成交易；CEO 柯比的解释很直白："我不想再增加一个中间人。"eBay 与多家银行也在设类似门槛。

来源：[IT之家](https://www.ithome.com/1/025/879.htm) · [WSJ](https://www.wsj.com/tech/ai/united-airlines-is-banning-ai-bots-from-booking-flights-5b514b38)

### 英国 AI 芯片公司 Fractile 融资 7.2 亿美元，估值 70 亿

Lightspeed、Founders Fund 等参投，主打推理芯片。英国本土算力供应链在英伟达之外补上了一个资本节点。

来源：[TechCrunch](https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/)

### Grok Build 泄露：37,571 个应用里 94.7% 可被任何人打开

安全公司 Claroc 发现分享链接默认"任何人可访问"，且子域名会被被动 DNS 收录，形成可检索的"幽灵分享"。受害方包括医院患者检验值、3500 人名单、消防排班表、18 组明文密码，以及 SpaceXSI 自己的销售区域图与广告方案。

来源：[IT之家](https://www.ithome.com/1/025/790.htm) · [Ars Technica](https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi/)

### 英国监管机构：AI 让课程作业评分"接近不可能"，威胁制裁不改考核的大学

学生事务办公室对 127 所院校 300 余名受访者的调查显示，学生大量使用 AI 写作且难以被检测，得分与不使用者相近；监管方要求大幅增加无 AI 考核，并警告可能对不改革考核形式的院校采取制裁。

来源：[The Decoder](https://the-decoder.com/uk-regulator-threatens-universities-with-sanctions-unless-they-adopt-ai-proof-exam-formats/) · [The Guardian](https://www.theguardian.com/education/2026/nov/11/ai-close-to-impossible-assess-university-cour)

### 纽约 RAISE Act 开放登记：72 小时内上报安全事故，罚款最高 300 万美元

年营收超 5 亿美元的前沿实验室须在 **2027 年 1 月 1 日**前完成注册、公开安全框架与透明度报告，违规首次最高罚 100 万美元、再犯 300 万美元。州长同日宣布在宾汉姆顿设立独立评估中心。

来源：[IT之家](https://www.ithome.com/1/025/548.htm)

---

## AI 研究前沿

### Deletion Tuning：删掉不到 0.05% 的权重，就能追平全参数微调

论文在 RLVR、监督微调与 on-policy 蒸馏三种后训练范式上验证了同一结论：只学习一个作用于门控投影的二值掩码、把选定权重清零，就能匹配全量微调的表现。两个实际好处——训练产物比全参 checkpoint 小几百到几千倍，且对旧任务的遗忘显著更少：持续学习场景下基础任务准确率几乎不掉，而全参、LoRA 与随机稀疏微调最多掉 5.4 个点。

来源：[arXiv](https://arxiv.org/abs/2611.10866)

### MMDM：给"单次前向做决策"的模型补一个专门基准

系统一决策模型不生成推理轨迹，直接对查询给定选项输出结构化概率，但现有评测多借用旧基准、存在污染。MMDM 重新构造 5448 道题、16 个任务类别，覆盖单选、多选与软标签决策，强调长上下文、大选项空间与复杂逻辑依赖。它的出现与 Gemini Decision 1 同日，说明新品类开始有自己的量尺。

来源：[arXiv](https://arxiv.org/abs/2611.14309)

### 密集奖励在 GRPO 里可能不划算

在算力对齐的条件下，蒙特卡洛式过程奖励反而弱于标准 GRPO；真正带来稳定小幅提升的是"按预测成功率接近 1/2 挑提示词"这类数据侧操作。对做 RL 后训练的团队，这是一个省 token 的负面结论。

来源：[arXiv](https://arxiv.org/abs/2611.13560)

### RoboScript / World In-Context Learning：把经验写进上下文而不是权重

观察是智能体在上下文里学到的是语义（任务步骤、物体角色）而非外观，因此一个世界里的经验能迁移到另一个。做法是用冻结模型从单条演示出发，在模拟器里排练任务，把反馈写回上下文。配套开源了模块化基础设施 RoboScript。

来源：[arXiv](https://arxiv.org/abs/2611.12885)

### 机器人的"记忆"可能只是一个时钟

论文指出记忆增强的 VLA 策略常把"暂停"误判为"进展"，因为记忆按时间索引，导致过早停止；改成按事件索引后无需重训即可缓解。对调试长程操作任务的人，这条能省不少排查时间。

来源：[arXiv](https://arxiv.org/abs/2611.14488)

### BVSR：给 AI 科学家少喂一点任务信息，反而更有创造力

受"盲变—选择性保留"认知框架启发，提案阶段刻意限制任务信息以扩大探索，再用已验证的同任务提案与结果做筛选。五个提案模型、12 个科学任务上，原创性与非显然性显著提升。

来源：[arXiv](https://arxiv.org/abs/2611.12184)

> 同批次其余值得一读的：WikiTrace 把每条蒸馏经验链接回源轨迹与理由，让智能体先验证再使用，减少"记忆导致的能力退化"（[arXiv](https://arxiv.org/abs/2611.14320)）；DepthGraft 用跨层分层共享 KV 表示降低显存并提升精度（[arXiv](https://arxiv.org/abs/2611.03142)）；还有一项工作用可验证的奖励—上下文冲突揭示 RL 智能体的"合规捷径"，并证明上下文惩罚能在不牺牲任务能力的前提下提升合规率（[arXiv](https://arxiv.org/abs/2611.12865)）。本批次共 31 篇，日期集中在 11 月 10 日至 11 日。

---

## 行业观点与解读

### 美国数据经纪商向中国实验室卖出约 5 亿美元的 RL 训练环境

ChinaTalk 的调查识别出至少 **9 家**美国数据公司——Mercor、Surge AI、AfterQuery、Turing 等在列——向中国 AI 实验室出售强化学习环境。这类模拟世界让模型在编码、金融分析、办公等具体任务上受训，中国实验室特意购买"已经卖给过 Anthropic 或 OpenAI 的同款"，以跳过自研与失败训练的成本；叠加用 GPT、Claude 输出做蒸馏，构成"双管齐下"的追赶路径。

真正值得警惕的是监管盲区：RL 环境既不是模型权重也不是芯片，出口管制基本管不到；订单还通过新加坡、圣何塞的采购办公室与离岸结构流转，分包商常把客户代号写在 LinkedIn 与简历上。作者特别点了双用途风险——编码环境同时提升攻防网络能力，生物环境可能触及基因合成与生物武器相关应用。

来源：[The Decoder](https://the-decoder.com/us-data-brokers-are-selling-half-a-billion-dollars-in-rl-training-environments-to-chinese-ai-labs/)

### Mercor 完成 7.5 亿美元 D 轮，估值 200 亿美元、年化收入 30 亿

Benchmark、General Catalyst 与英伟达参投。公司称有 500 万专家，并给出一个刺眼的自述："我们在推理上的支出已经是员工薪酬的 3 倍，而且它靠让团队更擅长本职工作回本。"

来源：[Latent Space](https://latent.space/p/ainews-mercor-750m-series-d-at-20b-valuation-3b-run-rate/) · [Reuters](https://www.reuters.com/legal/transactional/ai-training-startup-mercor-valued-20-billion-latest-funding-round-2026-11-10/)

### Ramp AI 支出指数：企业支出创新高但增速只有 1.65%，token 单价一个月跌 21%

10 月美国企业 AI 支出环比增 1.65%；头部 1% 公司人均每月花 1.02 万美元，典型公司只有 16.32 美元。Anthropic 采用率 44.8%、OpenAI 40.6%，1% 的公司贡献两家 80% 的收入。处理百万文本 token 的平均价格单月下降 21%——用量涨得比支出快，AI 在持续变便宜。

来源：[The Decoder](https://the-decoder.com/us-corporate-ai-spending-hits-a-new-high-in-october-but-growth-slows-to-1-65-percent/)

### Lenny's：把全家人的记忆搬进 Claude Code + Obsidian

Scott Farrar 的做法是把家庭待办、日程、医疗记录、孩子的学校信息放进本地 Obsidian 库，让 Claude Code 读写同一份 Markdown。比"又一个笔记应用"更有意思的是它的架构：数据留在本地纯文本，AI 只是访问层，换模型不迁移数据。

来源：[Lenny's Newsletter](https://www.lennysnewsletter.com/p/claude-code-obsidian-my-familys-ai)

---

## 值得关注的视频

> YouTube 播客与频道近期值得看的视频。标注 ⭐ 的为重点推荐。

### 花开花落：AI 日报 2026-11-12 晨间版（七条要闻）

七条速览，包含 Qwen4-Max 预览、平头哥赴港上市、日本拟对高性能 AI 设罚则年底前修法、Fractile 融资与 Helsing 平台。适合当监管与芯片线索的索引。 [B站](https://www.bilibili.com/video/BV1ALWX6jEgj)

### 肥鱼速览：11 月 12 日 13 条 AI 圈动态

自动化剪辑，条目最全，额外点了美团 LongCat-2.5 以 MIT 协议开源、智谱拟回购最多 40 亿港元 H 股，可当交叉核对清单。 [B站](https://www.bilibili.com/video/BV1goWQ6bECp)

### 一只 AI 风向标：Gemini 4 Hydrogen 内测、Grok 4.8 推送、Qwen Code 1.0 开源

传闻部分需自行判断：称 Gemini 4 Hydrogen 开启内测、Flash 级模型推理速度 300 至 500 tok/s。同日还列了 MuJoCo 全面免费开源、Runway 开放 Praxis-1 权重等 19 条。 [B站](https://www.bilibili.com/video/BV1NTWX6QEkR)

### 白鸦：Qwen4-Max 预览入口、文心 5.5 Flash 与 Gemini 决策接口实测

把三个新东西放在一起讲，含 Qwen4-Max 使用条件与开源代码的观察，适合快速对照今天国内三家的动作。 [B站](https://www.bilibili.com/video/BV1AgWX6SE2b)

---

## 灵感种子

**CEO 是单点故障。** 一家 4 万亿美元市值、几乎决定全球训练算力分配的公司，风险敞口在一周内从"出口管制"变成"某人的私生活"。这不是英伟达独有的问题，而是所有把关键决策权集中在创始人身上的 AI 公司的结构性问题——董事会真正要找的不是 CEO，而是一套在创始人缺席时仍然能运转的决策机制。值得追问的是：你的组织里，哪些判断只有一个人能做？

**护城河正在由模型自己拆除。** 三天把 Claude 移植到 AMD、写出接近 100% 的 kernel，这个动作的意义不在 Anthropic 省了多少工程师，而在它证明了"迁移成本"这件事可以外包给 AI。CUDA 的壁垒本质是一份巨大的、人力密集的适配工作清单，而 AI 最擅长的正是处理有客观验收标准的工程清单。顺着这个逻辑往下推，所有靠"切换成本高"维持溢价的生意，都该重新评估自己的护城河还剩多少人力厚度。

**决策 token 与生成 token 开始分家。** Gemini Decision 1 按输入计费、输出免费，MMDM 基准同日出现，一周内 Jev、OpenAI、Cloudflare、微软、谷歌排队入场——一个以"每秒几千次小判断"为计价单位的新市场正在形成。这对做 agent 的人是成本结构的重写，对做模型的人是市场份额的重分配：谁能在 150 毫秒内给出校准良好的概率，谁就拿到路由权，而路由权比生成权更接近流量入口。

**出口管制的下一个盲区是"环境"而不是"模型"。** 5 亿美元的 RL 训练环境生意说明，能力差距可以不被芯片、也不被权重承载，而是藏在一个个模拟任务的评分逻辑里。监管的直觉总是盯住有形物，而这些买来的"驾校"既提升编码也提升攻防，既训练办公也训练生物实验——它天然是双用途的。值得提前想清楚的问题是：如果评测环境本身成了战略物资，行业需要怎样的可核查披露机制？
