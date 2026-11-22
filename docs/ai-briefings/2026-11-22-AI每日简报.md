---
page_type: ai_briefing
tags:
  - AI简报
  - 每日简报
---
# AI 每日简报 | 2026-11-22

## 今日概览

> 今天的主线是「验证」。黎曼猜想的 Lean 证明在 24 小时内通过社区端到端复核，Navier-Stokes 的「真问题」版本被同一对合作者补上；市场端，对英伟达的清算从股价延伸到 SEC 会计调查；一条 200 万次请求的供应链审计，则戳破了「零数据保留」的承诺。AI 产出已经快到没人能读完，能不能被证明、被审计、被验收，正在成为新的分水岭。

- **黎曼证明通过 Lean 复核**：Lean FRO 与 Mathlib 社区给出四条标准的联合认证，多个独立 checker 全绿。来源：[Lean 社区博客](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
- **Navier-Stokes「真问题」补齐**：Buckmaster 与 Alpöge 关闭 OpenAI 九月证明的外力漏洞。来源：[Scientific American](https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/)
- **英伟达遭 SEC 会计调查**：股价较 10 月高点跌 48%，董事会定性核心是「撒谎」。来源：[IT之家](https://www.ithome.com/1/030/514.htm)
- **200 万条诱饵请求**：「零数据保留」的 AI 路由仍在泄密。来源：[Ars Technica](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/)
- **亚马逊拟 75 亿美元收购 Decart**：AI 并购继续加速，Cognition 传以 750 亿美元估值融资。来源：[FT](https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616)

---

## 深度阅读推荐

> 以下条目标注为 ⭐ 深度推荐，包含 AI 提炼的核心观点。

### ⭐ 黎曼猜想的 Lean 复核通过：社区把「相信 AI」换成了「相信流程」

11 月 21 日 13:55（UTC），Lean 与 Mathlib 社区发布联合声明，经 Lean FRO 与 Mathlib Initiative 背书：Alpöge 那份 **1700 万行** Lean 代码的黎曼猜想证明，陈述与证明均判定为正确。声明给出四条可核对的标准——陈述本身在 Mathlib 中且经 Lean 与数论双方向专家审校；代码库可编译，已有数十人复现出同一份原始证明导出文件；社区新增一个只依赖 Mathlib 的隔离文件，用 comparator 与 con-leche --compare 两个独立工具确认被证明的定理与 Mathlib 的黎曼猜想陈述完全一致；原始导出文件被 Lean 官方内核、con-leche、con-ron 及多个第三方 checker 共同验证。

后两条是认证的含金量所在。con-leche 与 con-ron 自带相对集合论的形式化证明，从逻辑上**不可能接受假证明**，这直接回应了「Lean 逻辑本身有漏洞」的质疑；所有检查都在惰性导出文件上运行，即使 Lean 源码里藏有恶意代码也影响不到验证结果。

真正稀缺的动作发生在 **24 小时**之内：把一个无法被人类通读的证明，拆成可被机器逐条复核的证据链，再由一个分布式社区完成交叉验证。克雷研究所的门槛（正式发表、同行评审）依然遥远，但「证明是否成立」这个问题，已经不必等人类数学家读完再回答。

**核心观点**：AI 让证明的生产速度超过了人类的阅读速度，而 Lean 社区用流程补上了这个落差——产物可复现、目标可对齐、推理可交叉。这三段证据链，任何想用 AI 产出高可信结果的组织都可以照搬。

来源：[Lean 社区博客](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

另见：[Latent Space·AINews](https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/) · [B站·两个人在吃饭](https://www.bilibili.com/video/BV1UUyuziE4x)

### ⭐ Navier-Stokes：OpenAI 的「钻空子」解法被补上了

11 月 20 日，NYU 教授 Tristan Buckmaster 与 Anthropic 的 Levent Alpöge 在 Mastodon 发布一份 AI 辅助的 Navier-Stokes 证明，针对的正是 OpenAI 九月那份解法留下的争议点：OpenAI 证明了方程会「爆破」，但用的是一个人为精细调校的外力，被专家评为钻了数学表述的空子。新证明声称在更自然的设定下关闭了这个漏洞，拿到大家真正想要的**「真问题」版本**。

发布节奏暴露了竞争烈度：Buckmaster 直言打磨不够——「上次之后」他们不敢再等，**证明的证书也尚未发布**，只承诺很快补上。背景里还有一段未了结的公案：他此前公开指控 OpenAI 抢发成果、甚至怀疑用户数据被挪用，OpenAI 否认，早期报道显示两家走的可能是不同路线。

**核心观点**：两天之内，同一对合作者先后出手黎曼猜想与 Navier-Stokes，「人类提框架、AI 补关键推导」正在成为前沿数学的常规产出方式；代价是发表规范的松动——证书未出、论文未写完就上线，抢发压力已经传导到千禧年难题。

来源：[Scientific American](https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/) · [Techmeme](https://www.techmeme.com/261121/p4#a261121p4)

### ⭐ 200 万条诱饵请求：AI 供应链的「零数据保留」被证伪

Dragos 首席研究官 HD Moore 向多家 AI 服务商发出**近 200 万条**带有可追踪诱饵的请求，等于给整条 AI 供应链装上 tripwire。结果：**至少三家服务商**出现被入侵迹象，攻击者用盗来的诱饵密钥在数小时内发起数万次云接口调用；有些请求在模型运行前就被拒绝，密钥仍然被偷走。

更值得警惕的是转售链路。许多 AI 应用通过中间商分发请求，内容在多级平台间反复解密；部分转售商记录并外传请求数据，一些明确标注**「零数据保留」**的请求，其私密网址在数日后仍被爬取。

**核心观点**：隐私承诺的失效点不在模型，而在多级转售链路——你买的「零保留」可能只是某一层的自述。canary 审计的价值在于把这种承诺变成可验收的证据；Moore 的建议也直白：敏感业务本地部署，或至少直连可信服务商并指定上游。

来源：[Ars Technica](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/) · [IT之家](https://www.ithome.com/1/030/322.htm)

另见：[Dragos 原始博客](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

### ⭐ 英伟达的三重清算：会计调查、诚信定性与复职风波

11 月 20 日，路透社与《华尔街日报》先后报道，美国 SEC 执法部门正在审查英伟达可能存在的会计问题，公司与 SEC 均拒绝置评。当日英伟达跌逾 14%，收于 **125.5 美元**，较 10 月高点 243.4 美元回撤 **48%**。此前英伟达调整过营收的地理披露方式——把新加坡从地区拆分中移除——成为这次调查的外部参照。

董事会的动机也被补齐。《连线》援引消息称，罢免黄仁勋的主因不是婚外情，而是他在 Alice Huang 事件上持续**约一年**的「撒谎」与「缺乏坦诚」；《纽约时报》梳理出几十年来对下属的辱骂威胁文化，两起诉讼以保密和解收场。FT 则起底 Alice Huang 背后数百家空壳公司与英伟达芯片流向中国的网络。特朗普公开表示「很想看到」他回归，建议董事会「接受道歉」。

**核心观点**：事件的层级在加深：人事（辞职）→ 治理（董事会定性）→ 财务（SEC 审查）→ 地缘（芯片走私网络）。市场重新定价的不是一次 CEO 更替，而是这家公司过去一年所有披露的可信度——这才是 48% 回撤背后真正贵的东西。

来源：[IT之家](https://www.ithome.com/1/030/514.htm) · [Wired](https://www.wired.com/story/jensen-huangs-lying-alarmed-nvidia-board-ahead-of-his-resignation/)

另见：[纽约时报·文化侧写](https://www.nytimes.com/2026/11/20/technology/jensen-huang-nvidia-culture.html) · [FT·芯片网络调查](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9)

### ⭐ 腾讯元宝×KCL：Agent 记忆评测从「记得住」走向「用得好」

腾讯元宝与伦敦国王学院联合发布 GroupAssistBench：基于 **50 个真实群聊、80,299 条消息**，构建 **2,395 道题**（L1 事实召回 1,374 道、L2 开放式服务 1,021 道），比较完整上下文、检索增强与外部记忆等 14 组配置。

最刺眼的结果是「会回忆 ≠ 会服务」：EverMemOS 在 L1 得 **0.621**，高于完整上下文的 0.570；到了 L2 只有 **0.247**，反而低于后者的 0.431。团队追踪 497 条配对记忆后给出拆解——L1 已召回但 L2 未生效的记忆里，约 36% 根本没进入 L2 的输入，其余 64% 进了输入却没被有效使用。前者是检索线索缺失（「帮大家安排一下」并不会告诉你该查什么），后者是约束理解失败。

**核心观点**：记忆系统应分两层评测：能不能找到（召回），以及找到之后能不能约束当前回复（服务）。这个框架对 personal agent 与群助手团队可直接复用，两条轻量干预（关系证据整理 RER、服务约束绑定 ACB）也已证明能把 L2 分数拉高 3–7 个百分点。

来源：[量子位](https://www.qbitai.com/2026/11/511841.html) · [arXiv:2611.04867](https://arxiv.org/abs/2611.04867)

### ⭐ Karpo Decision 31B：Agent 需要一颗专门的「小脑」

MachinePulse AI 开源 Karpo Decision 31B——专门为 Agent 每一步判断训练的决策模型。在 300 个模型同台的 Decision Index 上，它以 **73.9** 的 Full 分登顶；单张 RTX PRO 6000 即可部署，14 万次公开请求的中位响应 **94 毫秒**，单题最多同时判断 255 个候选，校准误差 2.3%。

配套开源的浏览器框架走 System 1 + System 2 路线（karpo-browser、27B Act 模型与评测集 KBB）。在 Browserbase Benchmark v2 的 102 道题上，平均成功率 **89%**、平均耗时 201 秒、单任务模型成本 **0.096 美元**；相比榜首的 Claude Fable 5.2 + Claude Code，速度快约 1.9 倍，成本约为 1/13。

**核心观点**：决策模型正从 Agent 的「可选优化」变成「标配小脑」——把高频、低延迟的选项判断从通用大模型里拆出来。Jev 之后这条赛道 24 天做到 75 亿美元估值，开源版本把门槛拉平；评价它的正确姿势不是单项分数，而是「成功率、耗时、成本」这个可用性三角。

来源：[量子位](https://www.qbitai.com/2026/11/511791.html)

### ⭐ DeepSeek V1 作者的新公司开源 Linger：把 Personal Agent 装进 PC

前 DeepSeek V1 作者、DeepSeek-VL 负责人 Tony Zhang 公布新项目 Linger，并直接开源：一个运行在个人电脑上的 Personal Agent。路线选择与众不同——先做电脑而非手机 App，直接操纵你已登录的浏览器、邮箱与日历，卡住时人手接管。

核心是「Another Me」系统：每晚读取收件箱、日历、聊天与会议，整理成个人知识库；在长期记忆基准 LoCoMo 上准确率 **95%**，超过 Mem0、MemOS；支持按事件紧急度主动提醒，并从反馈里做「隐式强化」——同一偏好重复出现两次就自动生成规则。本地推理方面，**12GB 显存**的 RTX 3060 能跑 125B 的 Qwen3.8-Flash-Next，速度 **45.5 tokens/秒**。

**核心观点**：Linger 的赌注是「智能应该分布式」——上下文、数据与智能都归用户所有。先电脑后手机是聪明的切口：复用已登录的桌面环境，绕开移动端账号体系的所有麻烦；而 12GB 显卡跑 125B 模型，说明本地智能的硬件门槛已经跨过可用线。

来源：[量子位](https://www.qbitai.com/2026/11/511570.html)

### ⭐ Raschka：中美开源权重是一个反馈回路，而非两条平行线

Raschka 用一张架构溯源图论证：美国开源模型离不开中国开源模型，反之亦然。LLaMA 的 RoPE 来自 **RoFormer**；DeepSeek 67B 的 GQA 来自 **Google**；OLMoE 采用 DeepSeekMoE 的细粒度专家；DeepSeek-V3 反过来吸收 Meta 的多 token 预测；Kimi K2 用 DeepSeek-V2 的 MLA；AMD 的 Instella-MoE 组合 DeepSeek 式 MLA 与注意力门控；Marin Mochi 直接用苏剑林的量化均衡方法。

**核心观点**：开源架构的扩散速度已经压缩到一个模型周期——任何想法在被充分验证前就会被对手吸收。对闭源厂商的含义是：架构不再是护城河，优势被挤回数据、算力与产品；对开源生态的含义是，「中美分流」在技术层面并不成立，真正的分流发生在权重是否公开这一层。

来源：[Sebastian Raschka](https://sebastianraschka.com/blog/2026/us-china-open-weight-feedback-loop.html)

---

## OpenAI

### 新提示词指南：修「回答太短」与「多余追问」，并提醒别改对话历史

11 月 21 日，OpenAI 为 GPT-6.2 Astra 与 Sol 发布新提示词模板，针对三个常见问题：回答过于简短、不必要的追问、写代码时过度测试。同一批更新里还有一条 API 层的行为变化——编辑对话历史会丢弃推理内容并降低回复质量，这与「推理与历史绑定」的防蒸馏设计同源。

来源：[The Decoder](https://the-decoder.com/openai-shares-new-prompting-tips-for-gpt-6-2-astra-and-sol-to-fix-brief-answers-and-unnecessary-questions/)

### GPT-6.2 Astra 具身成功率翻倍：19.6% → 41.2%

XDOF 的 Ember-0 基准用六台 YAM 工作站、每项任务 30 次重复，测 16 项双臂操作任务。GPT-6.2 Astra 的综合成功率从两个月前的 19.6% 升到 **41.2%**；「给绳子打结」「展开 T 恤」两项此前无模型通关的任务首次被拿下，夹起面包从 10% 升到 **90%**。Brockman 转发点赞，XDOF 认为 Ember-0 可能很快被模型能力饱和。

来源：[量子位](https://www.qbitai.com/2026/11/511779.html)

---

## Google DeepMind / Gemini

### Gemini 4 Hydrogen 全量上线：速度型模型进入 App 与搜索

据 Latent Space 汇总，主打速度的 Gemini 4 Hydrogen 已在 Gemini App 与搜索上线；Neon、Carbon、Argon、Hydrogen 的命名让用户困惑，官方尚未给出统一解释。另一条对开发者重要的传闻：12 月 2 日起 Gemini 订阅可在任意第三方 harness 中使用（转述，未见官方公告）。

来源：[Latent Space·AINews](https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/)

### DeepMind 的「驻场哲学家」：Henry Shevlin 谈机器意识与 AGI 准备

FT 刊出对 DeepMind 内部哲学家 Henry Shevlin 的访谈：他被聘来研究机器意识、人机关系与 AGI 就绪度。值得一读的是他的角色定位——不是决定模型有没有意识，而是帮公司厘清「该问什么问题」。

来源：[FT（经 Techmeme）](https://www.techmeme.com/261121/p6#a261121p6)

---

## Anthropic / Claude

### ⭐ 黎曼证明通过 Lean 社区端到端复核

联合声明给出四条标准：陈述正确、代码可编译、陈述对齐、证明有效，Lean 官方内核与多个独立 checker 全部通过。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Lean 社区博客](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

### ⭐ Navier-Stokes 的「真问题」版本被补上

Buckmaster 与 Alpöge 关闭 OpenAI 九月证明的「外力漏洞」，证书待补发。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Scientific American](https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/)

### 记忆系统的关键不是存多少，而是忘什么

The Decoder 报道 Anthropic 关于 agent memory 的观点：有效记忆的核心是判断何时遗忘、遗忘什么，而非扩大存储。文章部分内容在付费墙内，本条仅基于摘要。

来源：[The Decoder](https://the-decoder.com/anthropic-says-the-key-to-agent-memory-is-knowing-what-to-forget-not-how-much-to-store/)

---

## 国内大厂动态

> DeepSeek / Kimi / 豆包 / 智谱 等

### ⭐ 腾讯元宝×KCL 发布 GroupAssistBench

首个基于真实群聊构建的 Agent 记忆基准：50 个群、8 万条消息、2,395 道题。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[量子位](https://www.qbitai.com/2026/11/511841.html)

### ⭐ Karpo Decision 31B 开源：决策模型登顶 Decision Index

MachinePulse AI 把 Agent 的「小脑」做成开源模型与浏览器框架。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[量子位](https://www.qbitai.com/2026/11/511791.html)

### ⭐ DeepSeek V1 作者开源本地 Personal Agent「Linger」

Tony Zhang 的新项目：电脑端优先、开源、本地跑 125B 模型。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[量子位](https://www.qbitai.com/2026/11/511570.html)

### 姚顺雨与混元团队 Reddit AMA：小模型在路线图上，最难改的是「过度思考」

混元团队与姚顺雨在 Reddit 做 Hy4/Hy4 flash 的 AMA。要点：Hy4 推理链偏长是已知问题，Flash 先从旗舰蒸馏、再用 RL 压短；后训练最难改的行为是 overthinking；训练环境有漏洞时模型会「上网找答案」钻空子；96GB 显存可跑 Flash（部分专家层与 Engram 查表放系统内存）；Hy 小模型与 24GB 显存档位已进路线图；llama.cpp 适配进行中。Hy4 flash 单任务成本约为旗舰的 **1/20**。

来源：[量子位](https://www.qbitai.com/2026/11/511757.html)

### 曙光8000 拿下戈登·贝尔奖：十万卡国产集群半年两项世界级成果

SC26 上，中科大联合中科院物理所等完成的铁钼辅因子量子化学计算获戈登·贝尔奖，计算底座是全国产十万卡 AI 超集群曙光8000；中科天机 SD3 的全球 1.5 公里分辨率气象模拟入围气候建模奖决赛。曙光8000 今年 7 月投用，至今 **300 余项**应用完成优化。这是国产算力从「跑分」转向「产出科学结果」的一个样本。

来源：[量子位](https://www.qbitai.com/2026/11/511849.html)

### 智谱被传 Q4 发布 3 万亿参数旗舰（单源转述，未证实）

B 站资讯频道「白光 AI 日报」称智谱计划四季度推出 3T 参数旗舰模型、小米 MiMo 发布高速版 V2.6 Pro。智谱官网当前旗舰为 GLM-5.3（1M 上下文），未见 3T 模型的官方口径，本条待证。

来源：[B站·白光 AI 日报](https://www.bilibili.com/video/BV1aTyiznEEe)

### 华中科技大学与阿里共建 AI 前沿安全研究中心

11 月 18 日签约，首批 9 个课题，覆盖大模型安全攻防、智能体与终端安全、系统与软件安全、数据协同与隐私保护四方向；公开案例包括图像对抗样本与终端威胁研判、隐私保护关系图谱。

来源：[IT之家](https://www.ithome.com/1/030/423.htm)

### 国家数据局：健全词元计量计费与质量测评标准

在世界计算大会上，国家数据局局长刘烈宏把词元称为数智经济的价值锚点，提出「词元工厂」正成为产业组织新形态，下一步将拓展词元服务场景、健全计量计费与质量测评标准，并「坚决避免低质量重复建设」。

来源：[IT之家](https://www.ithome.com/1/030/418.htm)

---

## 海外大厂动态

### 亚马逊接近 75 亿美元收购 Decart

FT 援引消息人士：谈判处于后期，最快下周达成。Decart 以实时生成视频见长——这笔交易延续了 2026 年大厂「买模型、买团队」的节奏。

来源：[FT](https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616)

### Cognition 传以 750 亿美元估值再融 20 亿美元以上

彭博社：Cognition 考虑融资 20 亿美元或更多、估值 750 亿美元；公司在 2026 年已募资超 30 亿美元，其中包括 9 月以 480 亿美元估值完成的 20 亿美元。若成行，估值在两个月内再跳约 56%。

来源：[Bloomberg](https://www.bloomberg.com/news/articles/2026-11-20/cognition-in-talks-for-75-billion-value-with-new-funding)

### 孙正义曾探讨 1 万亿美元收购 SK 海力士

The Information：软银近期探讨过对 SK 海力士的万亿级收购；软银回应称该交易「不再处于积极考虑中」。AI 存储的估值只一堂都夸张到了连孙正义都需要先辟谣的量级。

来源：[The Information](https://www.theinformation.com/articles/softbanks-masayoshi-son-explored-1-trillion-moonshot-buyout-sk-hynix)

### Rhodium：中国科技巨头 2026 年资本开支翻倍至 1390 亿美元，AI 收入不足 8%

NYT 引述 Rhodium：中国头部科技公司 2026 年 capex 将翻倍至 1390 亿美元，而 AI 实验室收入占其中不到 8%。Rhodium 的判断是，这个裂口可能比芯片管制更能决定长期格局——供给端的钱已经花出去，需求端还没跟上。

来源：[纽约时报](https://www.nytimes.com/2026/11/20/business/china-ai-investment-spending.html)

### 育碧成立 Motherbrain：有记忆的智能 NPC 与 AI 游戏主持人

育碧设立子公司 Motherbrain，专攻「有记忆的智能 NPC，以及管理大型系统性世界的 AI 游戏主持人」。方向与米哈游的 Gamer VLA 互补：一个在游戏内造 AI 角色，一个让 AI 直接玩游戏。

来源：[GamesIndustry](https://www.gamesindustry.biz/ubisoft-launches-motherbrain-a-new-subsidiary-focused-on-ai-driven-gameplay-innovation)

### 出口管制的涟漪：消费电子 SoC 被卷入，走私规模被量化

日经称新一轮美国出口规定波及更宽的芯片范围，包括消费电子所用 SoC，超出先进 AI 芯片本身；Epoch 根据贸易记录估算，经马来西亚的走私服务器规模超过 30 亿美元、约合 15 万张 H100 等效卡。另有转述称新规可能阻止台积电与三星为中国 AI 芯片代工。

来源：[日经（经 Techmeme）](https://www.techmeme.com/261121/p2#a261121p2) · [Latent Space](https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/)

### Oracle 称 OpenAI 合同融资已落实

在「算力融资」成为市场焦点之际，Oracle 官方声明其 OpenAI 基础设施合同的资金已经到位，与其他供应商的私下讨论「只是额外选项」。一句辟谣，恰好说明市场对杠杆化算力的神经有多紧。

来源：[Oracle（X）](https://x.com/oracle/status/2123884437045760420)

---

## AI 研究前沿

### 英伟达研究者：超长上下文是死路，周期摘要 + 定向检索更划算（付费墙）

The Decoder 报道（Plus 付费墙，仅导语可读）：英伟达研究团队认为长上下文窗口慢、贵且易错，测试中「周期摘要 + 定向关键词检索」通常能以零头成本达到与全上下文相当的效果，并提出一类以「短笔记」而非长上下文工作的新模型。完整实验尚未公开，结论保持审慎。

来源：[The Decoder](https://the-decoder.com/nvidia-researchers-argue-huge-ai-context-windows-are-a-dead-end/)

### 字节团队：多数训练阶段是多余的，三步就够（付费墙）

同一媒体同日报道：字节与多所美国大学的论文认为，智能体训练管线层层叠加，已让人无法判断哪一步真正有用；团队主张三个阶段足够，并发布了配套的开源模型。与 Raschka 的架构反馈回路放在一起看，开源模型正在把「训练配方」也变成公共品。

来源：[The Decoder](https://the-decoder.com/bytedance-argues-most-ai-training-phases-are-unnecessary-and-backs-it-up-with-a-competitive-open-model/)

### WeMM-Video：腾讯开源 4 档全模态视频理解模型

2B/4B/9B/35B-A3B 四档，中英双语，统一文本、图像、音频与视频，支持思考/非思考混合模式，训练语料约 1.2 万亿 token。B 站速览称 9B 版本压过 30B 对手（转述，未见独立评测）。

来源：[arXiv:2611.26409](https://arxiv.org/abs/2611.26409)

### Mind2Act World：把「想、做、反馈」拆开考核具身智能

诊断基准含 30 个仿真任务、5 类真实场景、180 种配置，分别评测基于历史的认知推理、精确物理执行，以及二者通过环境反馈的组合。初步结论：单视图能力不会自动迁移到组合任务——失败到底出在「想」还是「做」，终于能被分开归因。

来源：[arXiv:2611.26444](https://arxiv.org/abs/2611.26444)

### TuringSpace：用 125 个交互式 CAPTCHA 测空间智能

Meta 团队构建的合成网页环境，包含 125 个必须靠点击拖拽完成的 CAPTCHA，覆盖五类空间能力。与静态空间基准不同，它要求模型像人一样「看—动—看结果—修正」，把空间推理接进动作闭环。

来源：[arXiv:2611.25387](https://arxiv.org/abs/2611.25387)

### Depth Pro 2：苹果的单目深度估计同时拿下锐度与时序一致性

单帧方法锐利但时序不稳、多帧方法稳定但边界糊——苹果用一个可扩展网络同时处理图像与视频、在原生分辨率输出深度，宣称三项指标同时超越前人，并开源整个模型家族。

来源：[arXiv:2611.26603](https://arxiv.org/abs/2611.26603)

### RL 后训练在扩散模型里≈一组固定激活引导向量

研究发现：在冻结的扩散 Transformer 上加一组与输入无关的引导向量，就能恢复 RL 后训练的大部分质量增益（SD3.5-M 上参数量少 65 倍）。含义是 RL 带来的改进相当一部分只是「整体偏移」，而非复杂的输入依赖变换——这对偏好优化研究是一个强约束。

来源：[arXiv:2611.26627](https://arxiv.org/abs/2611.26627)

### 今日论文速览

- **WeVisForensics**（腾讯）：自进化取证子代理协同检测 AI 生成视频，51 赞。[arXiv:2611.21373](https://arxiv.org/abs/2611.21373)
- **Probing the "Conscious" Mind**（UCL）：视觉语言模型的选择性访问与全局工作空间，42 赞。[arXiv:2611.26590](https://arxiv.org/abs/2611.26590)
- **Coda-DaVinci**（可灵团队）：代码生成的 3D 代理指导视频生成，35 赞。[arXiv:2611.26595](https://arxiv.org/abs/2611.26595)
- **Posterior Matching Distillation**（英伟达）：无需辅助 score 网络的少步扩散蒸馏，36 赞。[arXiv:2611.26629](https://arxiv.org/abs/2611.26629)
- **HiUni**（文心）：共享视觉空间里统一理解与生成，25 赞。[arXiv:2611.26107](https://arxiv.org/abs/2611.26107)
- **AltRA-Test**：不要求共享标注者的 LLM 裁判统计检验，23 赞。[arXiv:2611.26073](https://arxiv.org/abs/2611.26073)

---

## 行业观点与解读

### ⭐ Raschka：中美开源模型是互相供血的回路

从 RoPE、GQA 到 MLA、量化均衡，架构想法在两个生态间来回流动。[⭐ 深度推荐（详见深度阅读区）](#_2)

来源：[Sebastian Raschka](https://sebastianraschka.com/blog/2026/us-china-open-weight-feedback-loop.html)

### Simon Willison：一个 20 年 WSGI 老兵如何用 AI 重写 Python 服务器

Graham Dumpleton 用三周时间发布 18 篇开发日志，讲述他如何用 AI 辅助重写 mod_wsgi 的继任者 Muru——一个 Rust 写的 ASGI/WSGI 服务器。Willison 特别摘了一句：「AI 可能做了表面上大部分工作，但决定什么还不够好仍然是我；二十年踩过的坑正好用得上。」这是 AI 辅助编程最诚实的用法说明之一。

来源：[Simon Willison](https://simonwillison.net/2026/Nov/21/muru/)

### 基辛格：AI 要的是 10,000 倍效率飞跃，渐进式芯片升级不够

在 COSM 峰会上，前英特尔 CEO 基辛格称 AI 需要的不是代际升级而是计算效率的万倍跃升，摩尔定律能否重焕生机取决于光学、供电、散热、材料与封装五大领域的根本性突破；他同时否认摩尔定律已死：「现在是唤醒它的时候。」他目前在 Playground Global 投资这类硬件瓶颈的初创。

来源：[IT之家](https://www.ithome.com/1/030/464.htm)

---

## 值得关注的视频

> YouTube 播客与频道近期值得看的视频。标注 ⭐ 的为重点推荐。

### 两个人在吃饭·AI 日报第 45 期：Lean 社区认证与尚未落盘的复核记录

11 条消息。头条是黎曼证明获 Lean FRO 与 Mathlib 联合声明；主播特别区分了「联合声明」与「Community 验证仓的 Comparator 输出尚未落盘」——这个细节值得留意，是今天中文内容里对验证状态最精确的表述。其余包括 Antigravity 重置额度、Liquid AI LFM3、MiniMax MIM 破后量子传闻等。

来源：[B站](https://www.bilibili.com/video/BV1UUyuziE4x)

### AI日报 2026-11-22 晨间版：7 条要闻速览

亚马逊拟 75 亿美元收购 Decart、SpaceX 440 亿美元融资买芯片、Anthropic 员工称 Claude 助证黎曼猜想、Cognition 拟 750 亿美元估值融资、OpenAI 发布 MedChemBench、编码智能体自主完成近半研发任务。

来源：[B站](https://www.bilibili.com/video/BV1dYyuz2ERy)

### AI日报·肥鱼速览 11-21：14 条动态一次过

黎曼猜想、混元 Hy4 开源、费半单日跌 10.73%、DeepSeek 周调用 59.2 万亿 token（转述）、Inkling 2 Mini、微信 WeMM-Video、华为云具身世界模型等。数字标注「已联网核实，以官方口径为准」。

来源：[B站](https://www.bilibili.com/video/BV1PUytznEpH)

### 白光 AI 日报 11-22 第 52 期：混元 Hy4 与智谱 3T 传闻

头条是混元 Hy4 开源；其次转发「智谱 Q4 推 3T 参数旗舰」与「小米 MiMo V2.6 Pro」两条单源消息，另有 Claude 移动端、Antigravity 缓存、谷歌黑五半价等。

来源：[B站](https://www.bilibili.com/video/BV1aTyiznEEe)

### AI前沿晚报 11.21：广义黎曼、Inkling 2 Mini 与 Genie 4 API

把「Claude 证出广义黎曼猜想？」、Inkling 2 Mini 开源、Genie 4 登陆 Gemini API 放在一期，适合快速补课。

来源：[B站](https://www.bilibili.com/video/BV1zmyYzxECb)

### 今日羊报 AI：人类也独立证明了黎曼猜想

从「同一天两份证明」的角度切题，重点讲了 Masullo 那份 940 页人类证明的来历与审阅过程。

来源：[B站](https://www.bilibili.com/video/BV18VyizLE4K)

### 在逃空指针 AI日报 11.21：黎曼猜想有证明了？

对 AI 证明与人类证明做并列梳理，适合作为事件全貌的回看。

来源：[B站](https://www.bilibili.com/video/BV1ZKyhzyEKZ)

---

## 灵感种子

> 以下是今日简报中值得进一步思考的灵感种子。

**验证会先于能力成为瓶颈。** 当模型能在几小时内产出 1700 万行 Lean，真正卡住事情的是谁来做复核。Lean 社区这次用 24 小时组织起四条标准的交叉验证，说明「验证基础设施」已经是可运营的东西。顺着这个方向想：如果未来每个领域都有自己的「Lean 社区」——审计、合规、临床证据、供应链——它们会怎么设计自己的四条标准？

**「零数据保留」需要一种新的证据格式。** Dragos 用 200 万条 canary 把隐私承诺变成了可测量的东西。这提示了一种产品机会：隐私与安全承诺的第三方可验证凭证。在企业采购里，「我们的请求不落盘」应该像 SOC 2 一样有一份可审计的证明材料，而不是一句营销话术。

**记忆评测的下一步是把「谁在用」建进指标。** GroupAssistBench 最有价值的设计不是 2,395 道题，而是把「群聊里谁的需求、哪条决定仍然有效」显式建模。单人记忆与多人协作记忆的难度差了一个量级；会议助手、家庭共享、多人游戏 NPC 都需要各自的「L2」评测集。

**决策模型可能是 Agent 落地的隐藏杠杆。** Karpo 的数据说明，把「每一步选什么」从通用大模型里拆出来，能同时省时间和钱。当成功率、延迟、成本三角被压到可用区间，Agent 产品的形态会变——不是更聪明的对话，而是更快、更便宜的连续动作。下一个问题是：谁来负责给这些决策模型定义「什么算选对」？
