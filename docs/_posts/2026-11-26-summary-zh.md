---
layout: default
title: "Horizon 中文日报 · 2026-11-26"
date: 2026-11-26
lang: zh
generated_by: horizon-pages
---

> 从 77 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [FCC 批准 SpaceX 部署最多百万颗 Starmind 卫星](#item-tech-news-1) ⭐️ 9.0/10
2. [1Password 披露安全事件：客户姓名和邮箱等信息被窃](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic 将 Messages API 从 Python 迁至 Rust，并用 Claude 智能体验证一致性](#item-tech-news-3) ⭐️ 8.0/10
4. [Anthropic GRH Lean 验证出现约 7.6 万行精简版](#item-tech-news-4) ⭐️ 7.0/10
5. [纽约对 AI 聊天玩具实施五年禁令](#item-tech-news-5) ⭐️ 7.0/10
6. [多州总检察长反对 Character.AI 破产拍卖转移用户聊天数据](#item-tech-news-6) ⭐️ 7.0/10
7. [瑞银预测 2028 年国产 AI 芯片占中国市场 88%](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI 小范围测试私密推理](#item-tech-news-8) ⭐️ 7.0/10
9. [科学家为科研 AI 智能体划定使用边界](#item-tech-news-9) ⭐️ 6.0/10
10. [OpenAI 合并 ChatGPT 的 Chat 与 Work 并统一用量计量](#item-tech-news-10) ⭐️ 6.0/10
11. [Nvidia 收紧数据中心担保，neocloud 遭遇建设延期与债务成本上升](#item-tech-news-11) ⭐️ 6.0/10

**财经新闻**
1. [美国法官阻止 FCC 撤销迪士尼旗下 ABC 电视台执照](#item-finance-news-1) ⭐️ 7.0/10
2. [标普警告英伟达董事会可能存在问题，将其评级列入下调观察名单](#item-finance-news-2) ⭐️ 7.0/10
3. [路透：与 Alice Huang 关联的公司在中国登记了 2.7 亿美元 AI 服务器](#item-finance-news-3) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [FCC 批准 SpaceX 部署最多百万颗 Starmind 卫星](https://www.geekwire.com/2026/fcc-clears-spacex-million-satellites-starmind-data-center/) ⭐️ 9.0/10

美国联邦通信委员会（FCC）批准 SpaceX 最多部署 100 万颗搭载 AI 芯片的 Starmind 卫星，用于在轨数据处理，并称这是美国首次批准完整的太空数据中心星座。授权要求 SpaceX 在 2033 年前至少部署一颗卫星，并在 2040 年前达到 100 万颗的部署目标，卫星运行高度为 500 至 1002 公里。FCC 附加了通信备份、定期提交进展和详细轨道碎片减缓方案等条件，并驳回了亚马逊、Viasat 和美国天文学会的反对意见；FCC 还推迟了 SpaceX 关于将 600 公里以上卫星处置到“墓地轨道”的请求。这是监管授权，不代表卫星已实际部署。

telegram · zaihuapd · 11月26日 04:45

**「背景」** Starmind 是 SpaceX 将 AI 计算模块部署到轨道、构建在轨数据中心的计划，核心做法是让卫星在太空直接处理数据。相关报道指出，这一方向仍面临工程可行性、经济性和轨道碎片规则等未解问题。

**「部署仍受后续审批约束」** 对 SpaceX 而言，这项授权并不意味着可以立即在全部轨道高度部署：FCC 要求其在部署任何 600 公里以上的卫星前重新申请，而六个轨道壳层中有四个位于该高度以上，因此 100 万颗的规模仍取决于后续审批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/science/articles/fcc-authorized-spacex-deploy-million-184723696.html">The FCC Authorized SpaceX To Deploy a Million Satellites</a></li>
<li><a href="https://startupfortune.com/fcc-gives-spacex-conditional-approval-for-a-million-data-center-satellites/">FCC gives SpaceX conditional approval for a million data ...</a></li>

</ul>
</details>

**标签**: `#FCC`, `#SpaceX`, `#Starmind`, `#space data centers`, `#satellite constellation`

---

<a id="item-tech-news-2"></a>
### [1Password 披露安全事件：客户姓名和邮箱等信息被窃](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 披露了一起安全事件：攻击者入侵一名员工的企业 GitHub 账户，借此访问源代码并向后台服务推送恶意代码，以下载客户数据。被窃信息包括客户姓名、邮箱地址、账户标识以及账户创建和最近登录时间；公司称客户保险库及其内容未受影响，且未披露受影响用户数量。1Password 于 11 月 19 日开始调查，已停用涉事账户、轮换或撤销可能暴露的内部凭证，并加强邀请和恢复邮件中的验证码；公司表示用户无需更改账户，但应警惕钓鱼。

hackernews · lxhrstn · 11月25日 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**「背景：为什么保险库内容未受影响」** 要理解这次事件的影响边界，需要先了解 1Password 的加密设计：保险库内容以只有用户端能解开的加密形式保存，服务端并不持有可直接解密数据的凭据，登录则依赖 Secure Remote Password 协议，服务器端看到的只是无法用于访问账户的协议参数和本就公开的公钥——1Password 在事件说明中正是以此解释泄露数据为何不含密码或保险库内容（tool-2-1）。也正因如此，攻击者通过员工 GitHub 账户向后台服务推送代码、进而下载数据，造成的后果集中在账户元数据层面，而非用户保存在保险库里的密码与条目。

**「影响」** 被窃的姓名、邮箱、账户标识和登录时间可用于制作更具针对性的钓鱼邮件，而 1Password 表示客户保险库未受影响，因此用户无需更改账户，但仍需对冒充该公司的邮件保持警惕。

**「社区讨论」** 评论中，tptacek 认为员工终端被入侵后向 GitHub 推送代码并被部署，是 SaaS 公司的标准攻击路径，而 1Password 的加密设计缓解了最坏情况；ctidd 则质疑公告未说明是否缺少分支保护、或相关保护是否被绕过。qixxiq 报告收到一封包含其部分信息、来自非官方域名的钓鱼邮件，并认为可能与此次事件有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving... | 1 Password</a></li>

</ul>
</details>

**标签**: `#security incident`, `#1Password`, `#SaaS security`, `#supply chain`, `#phishing`

---

<a id="item-tech-news-3"></a>
### [Anthropic 将 Messages API 从 Python 迁至 Rust，并用 Claude 智能体验证一致性](https://x.com/AnthropicAI/status/2125627317263466739) ⭐️ 8.0/10

Anthropic 在 X 上宣布，其 Messages API 已从 Python 迁移到 Rust。公司表示已在工程博客中说明如何用现有服务来验证新服务：由多组 Claude 智能体追踪并修复新旧两个版本之间的行为差异。该消息只是社交平台上的公告，迁移后的性能指标、上线范围和完成时间均未披露；博客中关于智能体验证方法的技术说法也无法仅凭这条推文独立核实。

twitter · Anthropic · 11月25日 16:26

**「背景」** Messages API 是客户以及 Claude Code、Cowork 等 Anthropic 自有应用访问 Claude 的主要接口。Anthropic 的工程博客称，从 2024 年初到 2026 年秋，其 API 流量增长了约 1,800 倍，这一规模变化构成了此次从 Python 重写为 Rust 的背景。

**「影响」** 这是服务内部实现语言的替换，公告没有提到对客户端接口的变更，而验证工作的目标正是消除新旧版本之间的行为差异；因此调用 Messages API 的开发者目前没有需要跟进的迁移或兼容性动作，实际影响要等工程博客披露差异修复的具体内容后才能判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/migrating-api-to-rust">Migrating our Messages API to Rust \ Anthropic</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#rust`, `#claude`, `#ai-agents`, `#api-infrastructure`

---

<a id="item-tech-news-4"></a>
### [Anthropic GRH Lean 验证出现约 7.6 万行精简版](https://github.com/lsernau/grh-lean) ⭐️ 7.0/10

GitHub 仓库 lsernau/grh-lean 发布了一个更短、更易读的 Lean 形式化版本，针对 Anthropic 的 GRH 验证，据称把约 1700 万行压缩到约 7.6 万行，并加入文档和“已知数学/新数学”划分。该仓库是社区制品，不是同行评审的数学论文，也没有独立确认底层论证。评论者认为更短的代码和文档有助于理解，但指出核心数学论证仍需更清晰的阐释。

hackernews · nb-t · 11月25日 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**「背景」** 这一缩短版针对的是 Anthropic 数学家 Levent Alpöge 于 11 月 20 日发布的原版 Lean 4 证明；据 Stack Futures 报道，原版约 1700 万行，而新仓库将其压缩到约 7.6 万行。新仓库的说明称，它是基于 Mathlib 的 Lean 4 证明，覆盖 Riemann 假设及 Dirichlet L 函数的广义 Riemann 假设，并且只使用 propext、Classical.choice 和 Quot.sound 三条公理。

**「影响」** 对需要审计或学习该形式化的人，文档和“已知数学/新数学”分界让检查重点更明确，可优先审查标为“新数学”的部分；但现有证据只支持这是可读性和工程层面的改进，不能据此认为 GRH 已被独立验证。

**「社区讨论」** 有评论者称赞约 7.6 万行的版本带有清晰分界和文档，应有助于消化，并按约 1700 万行到 7.6 万行算出 99.56% 的缩减；也有人追问这是否回应了陶哲轩一个月前关于“巨大证明缺乏洞见”的批评。另有评论者希望数学家真正理解核心论证，写成可发表或可会议展示的数学论文，而不只是 Lean 代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackfutures.com/blog/anthropic-riemann-lean-proof-17m-to-76k-lines-shorter-grh-nov-2026/">The Riemann Hypothesis Lean Proof Just Shrank From 17 Million ...</a></li>
<li><a href="https://github.com/lsernau/grh-lean/tree/main">GitHub - lsernau/grh-lean: A short Lean 4 proof of the ...</a></li>

</ul>
</details>

**标签**: `#Lean`, `#formal verification`, `#AI-assisted mathematics`, `#Anthropic`, `#proof engineering`

---

<a id="item-tech-news-5"></a>
### [纽约对 AI 聊天玩具实施五年禁令](https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/) ⭐️ 7.0/10

纽约已禁止 AI 聊天玩具五年，依据是 Common Sense Media 的一项新研究。该研究记录了安全失效，包括儿童接触不当内容以及情感受损的风险。现有报道未说明禁令的生效日期、执法方式，也未界定受禁“AI 聊天玩具”的具体范围。

rss · TechCrunch AI · 11月25日 18:11

**「背景」** 这项禁令的法律载体是纽约州法案 S.9408A/A.11144B，州长凯西·霍楚尔已签署该法案，针对的是把 AI 聊天机器人嵌入毛绒玩具、玩偶或机器人并通过联网进行对话的产品。禁令为期五年，将于 2027 年 2 月生效，违规者面临最高每日 1.5 万美元罚款。

**「影响」** 纽约消费者在这五年内将无法购买此类 AI 聊天玩具，家长的节日选购因此受限；销售商则需处理纽约市场的合规问题，但报道未说明具体执法和过渡安排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wshu.org/2026-11-24/new-york-bans-ai-chatbot-toys">New York bans AI chatbot toys - wshu.org</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/york-imposes-five-ban-ai-180458200.html?fr=sycsrp_catchall">New York Imposes Five-Year Ban on AI Chatbot Toys for Kids</a></li>
<li><a href="https://www.baltimoresun.com/2026/11/25/new-york-governor-signs-five-year-ban-on-artificial-intelligence-chatbot-toys/">Chatbot toy law part of New York&#x27;s effort to address children ...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#AI safety`, `#children&\#x27;s technology`, `#consumer AI`, `#New York`

---

<a id="item-tech-news-6"></a>
### [多州总检察长反对 Character.AI 破产拍卖转移用户聊天数据](https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/) ⭐️ 7.0/10

多州总检察长对 Character.AI 拟议中的破产拍卖提出反对，理由是这桩交易将转移超过 2100 万个美国账户的敏感个人聊天数据。这些官员特别指出，其中约 210 万个账户的注册人是未成年人。该拍卖目前仍是拟议交易，而非已经完成的出售；现有来源未说明反对意见的具体法律形式、提交对象或可能的裁决结果。

rss · TechCrunch AI · 11月25日 17:35

**「背景」** Character.AI 于 2026 年 10 月 14 日申请第 11 章破产保护，并宣布出售部分资产；这一程序因此成为处置其用户数据的场合。多州总检察长联盟介入，要求任何买家继续遵守用户已作出的隐私选择（例如退出）。

**「对用户的影响」** 对美国境内逾 2100 万账户使用者而言，直接后果是其私人对话可能作为破产资产的一部分转交给买方，其中包括约 210 万名未成年注册用户的账户。由于聊天数据正是此次反对的争点，交易的最终结构可能取决于这些记录如何处置；但来源未说明用户是否能删除数据或选择退出，也未说明法院或监管机构会如何回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/">Character . AI ’s plan to auction off users’ private chats ... | TechCrunch</a></li>
<li><a href="https://ppc.land/character-ai-faces-40-attorneys-general-over-who-can-buy-its-users-chats/">Character . ai faces 40 attorneys general over who can buy its users...</a></li>
<li><a href="https://anymesgs.com/en/article/characterai-bankruptcy-user-data-ags/">40 Attorneys General Move to Block Character . AI Bankruptcy Sale ...</a></li>

</ul>
</details>

**标签**: `#Character.AI`, `#AI privacy`, `#regulation`, `#user data`, `#bankruptcy`

---

<a id="item-tech-news-7"></a>
### [瑞银预测 2028 年国产 AI 芯片占中国市场 88%](https://www.scmp.com/tech/tech-war/article/3375758/chinese-ai-chips-capture-88-home-market-2028-ubs-says-nvidia-woes-mount) ⭐️ 7.0/10

瑞银预测，到 2028 年中国国产 AI 加速器将占国内市场的 88%；中国每年的 AI 加速器出货量将从 2025 年的 170 万颗增至 2030 年的逾 1000 万颗，接近六倍。该行认为，寒武纪和壁仞科技是其中的领先者。这一判断的背景是北京推进技术自主、美国芯片出口审查升温，以及近期的英伟达风波。上述数字均为瑞银的预测，而非已实现的出货量或独立测试结果。

rss · SCMP Technology · 11月26日 04:00

**「背景」** 中国推动 AI 芯片国产替代的背景，是美国对先进芯片出口的审查持续收紧，使 Nvidia 等美国厂商在华销售高性能 AI 加速器面临更大不确定性，北京因此加大技术自立投入。UBS 的最新数字属于对 2025 至 2030 年出货量和市场份额的预测，而非已经实现的出货或基准测试结果。

**「采购影响」** 若 UBS 的预测兑现，到 2028 年中国境内的 AI 算力采购方将面对以寒武纪、壁仞等国产加速器为主的供应格局，Nvidia 作为默认选项的空间相应收窄；相关企业应把国产芯片的交付节奏和供应连续性纳入采购规划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cambricon_Technologies">Cambricon Technologies - Wikipedia</a></li>
<li><a href="https://www.globaltimes.cn/page/202611/1374549.shtml">Several Chinese chipmakers post upbeat Q3 earnings... - Global Times</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#China`, `#Nvidia`, `#semiconductors`, `#market forecast`

---

<a id="item-tech-news-8"></a>
### [OpenAI 小范围测试私密推理](https://www.cnbeta.com.tw/articles/tech/1588020.htm) ⭐️ 7.0/10

OpenAI 首席执行官萨姆·阿尔特曼 11 月 25 日在 X 上宣布，OpenAI 正面向一小部分客户测试“私密推理”（Private Inference）；据其产品页介绍，该功能结合机密计算与严格、可验证的控制手段，在模型运行期间隔离客户数据，目前处于 Alpha 阶段，定价尚未公布。它是 OpenAI“Private Intelligence”企业方案的两个组件之一，另一组件“零数据保留与私密安全处理”可自动完成安全审查，使 OpenAI 人员无需接触底层内容。作为可比方案，Anthropic 今年 9 月公布的企业前沿防护（EFS）将数据存放在客户自己的云账户中、使用客户自己的密钥，并把监控信号直接发送给客户；该功能计划分批推送、目标是在今年秋天晚些时候全面可用，且 Anthropic 不对此收费。

telegram · AI\_News\_CN · 11月26日 04:25

**「背景」** 机密计算的核心是在数据处理过程中隔离数据与访问权限，使平台运营方也无法直接读取底层内容；OpenAI 称“私密推理”正是把这一机制用于模型运行时，并配合可验证的控制手段。作为同类方向的较早动作，Anthropic 今年 9 月已公布企业前沿防护（EFS），让数据留在客户自己的云账户、使用客户密钥，并把自动监控信号直接发送给客户。

**「影响」** 对需要处理敏感数据的企业客户来说，这项能力目前仅限小范围 Alpha 测试，定价和正式可用时间均未公布，因此还不能作为近期采购、部署或合规承诺的依据；有意采用者需先确认受邀条件以及“可验证控制”的具体范围。

**标签**: `#OpenAI`, `#Private Inference`, `#confidential computing`, `#enterprise AI`, `#data privacy`

---

<a id="item-tech-news-9"></a>
### [科学家为科研 AI 智能体划定使用边界](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) ⭐️ 6.0/10

Hugging Face 博客于 2026 年 11 月 25 日发布了一篇分析文章，讨论科学家在科研工作中为 AI 智能体划定使用边界。文章属于对科研实践的观察与分析，并非新模型、基准测试或产品功能的发布；现有元数据未提供具体的边界规则、受访对象或研究结论。目前可确认的是文章主题和发布渠道，文中具体主张仍需查阅原文核实。

rss · Hugging Face Blog · 11月25日 18:52

**「背景」** Ai2 在 Hugging Face 博客发布的访谈分析，基于对 17 位来自自然科学、应用科学和社会科学的科学家的访谈，梳理他们在让 AI agent 接手更多科研流程前所要求的条件。该分析按五个“科学信任”维度归纳这些边界，关注点包括人类监督、责任归属以及哪些判断需要保留给人类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents">Where scientists draw the line on AI agents - Hugging Face</a></li>
<li><a href="https://creati.ai/ai-news/2026-11-26/where-scientists-draw-the-line-on-ai-agents/">Where scientists draw the line on AI agents</a></li>
<li><a href="https://www.youtube.com/watch?v=upXEigzn2OY">Hugging Face: Where scientists draw the line on AI agents Scientists Draw Boundaries for AI Agents in Research Where 17 Scientists Draw the Line on AI Agents | LLMs Blog Where Scientists Draw the Line on AI Agents | Judy AI Lab Where scientists draw the line on AI agents | OO.NEWS</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI for science`, `#research`, `#Hugging Face`

---

<a id="item-tech-news-10"></a>
### [OpenAI 合并 ChatGPT 的 Chat 与 Work 并统一用量计量](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/) ⭐️ 6.0/10

OpenAI 将把 ChatGPT 中的 Chat 与 Work 两项体验合并，并在 ChatGPT 内引入统一的用量计量（single usage meter），取代此前分开计算的方式。OpenAI 表示，这一变化可能导致重度用户比过去更早触及使用上限。目前披露的信息未说明合并与统一计量的生效时间、具体限额数值，也未说明适用套餐或地区范围。

rss · TechCrunch AI · 11月25日 20:03

**「背景」** OpenAI 此前已宣布，Plus、Pro 和 Business 套餐将改为 ChatGPT 与 Codex 共用的、按 token 计量的额度；用户可在设置中的“用量”页面查看合并后的剩余用量和重置时间。此次将 Chat 与 Work 合并到同一用量表，延续了统一计量的方向，但两者覆盖的产品范围并不相同。

<details><summary>参考链接</summary>
<ul>
<li>Please Keep ChatGPT and Codex Usage Limits Separate in December 2026</li>
<li>Understanding ChatGPT and Codex usage limits | OpenAI Help Center</li>

</ul>
</details>

**标签**: `#ChatGPT`, `#OpenAI`, `#usage limits`, `#product strategy`

---

<a id="item-tech-news-11"></a>
### [Nvidia 收紧数据中心担保，neocloud 遭遇建设延期与债务成本上升](https://techcrunch.com/podcast/ai-data-centers-are-becoming-harder-to-build-and-neoclouds-are-feeling-it/) ⭐️ 6.0/10

TechCrunch 的一档播客节目报道称，Nvidia 已明确表示，在 AI 数据中心接近可以投运之前，不会为其提供兜底或担保；而这一立场出台之际，新兴云服务商（neocloud）正同时面临建设延期和更昂贵的债务融资。节目总结称，对数据中心开发商而言，土地、电力以及已建成的机房比一份商业计划书更重要，Anita Verma-Lallian 正在推销的正是这类已具备落地条件的资产。需要说明的是，该内容来自一段简短的播客摘要，未提供具体项目、涉及金额、延期时长或融资成本数字，因此上述说法属于媒体报道与当事方立场的转述，而非可独立核实的量化结果。

rss · TechCrunch AI · 11月25日 15:41

**「背景」** neocloud 指以 GPU 算力租赁为核心业务、规模小于大型云厂商的云服务商，其 AI 数据中心项目通常依赖外部融资和硬件供应商支持。英伟达的背书会影响这类项目的融资条件；报道显示的新变化是，英伟达要等到设施接近可运行才愿提供支持。

**「融资风险前移」** 对新云（neocloud）运营商而言，英伟达把背书推迟到数据中心“接近可运行”才给出，意味着土地、供电和建设资金必须由自己先行垫付，债务成本上升与工期延误因此直接落在其资产负债表上（tool-2-1）。这也会传导到租用其 GPU 容量的客户：新增算力上线时间取决于厂房完工而非签约意向，采购方需更早锁定供电与交付档期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/podcast/ai-data-centers-are-becoming-harder-to-build-and-neoclouds-are-feeling-it/">AI data centers are becoming harder to build, and neoclouds ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#neoclouds`, `#Nvidia`, `#cloud computing`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国法官阻止 FCC 撤销迪士尼旗下 ABC 电视台执照](https://www.investing.com/news/stock-market-news/us-judge-blocks-fcc-from-revoking-disneys-abc-tv-licenses-5051928) ⭐️ 7.0/10

据报道，一名美国法官阻止了美国联邦通信委员会（FCC）撤销迪士尼旗下 ABC 电视台执照的行动。目前裁决的具体范围、理由及后续步骤尚未披露。

rss · Investing.com Stock Market News · 11月26日 02:45

**「背景」** 此前，美国联邦通信委员会（FCC，负责发放和审查电视台执照的联邦监管机构）要求迪士尼在 30 天内为旗下八家自营 ABC 电视台提交执照续期申请；迪士尼随后提起诉讼，称 FCC 此举是在威胁其广播执照。

**「影响」** 在诉讼继续期间，ABC 旗下电视台可维持现有执照运营，无需面对提前续期审查，迪士尼广播业务近期的监管压力暂时缓解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cbc.ca/news/world/judge-blocks-fcc-revoking-abc-licences-9.7436635">U.S. judge blocks FCC from revoking licences of Disney-owned ...</a></li>
<li><a href="https://www.cnn.com/2026/11/25/media/trump-fcc-carr-disney-abc-stations-judge-blocked">Judge blocks Trump’s FCC from targeting ABC ... | CNN Business</a></li>
<li><a href="https://theheartysoul.com/melania-trump-joke/">Netflix Cut a Melania Joke — and the FCC Went After ABC Over...</a></li>
<li>&#x27;Not a close case:&#x27; Judge blocks review of ABC&#x27;s broadcast licenses - POLITICO</li>

</ul>
</details>

**标签**: `#Disney`, `#FCC`, `#broadcast licenses`, `#media regulation`, `#legal ruling`

---

<a id="item-finance-news-2"></a>
### [标普警告英伟达董事会可能存在问题，将其评级列入下调观察名单](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb1ZBby1iVDJnTmJwX3hDYWJpU2lxTUdLTHdlWHFqRHJUcmtTOWFuQkFRTlUyZTJBcGdNMWR3N3d1YlJIV05kWk1mU21JSDZmSVpZR1BlanpqRzFXSkg3NkxkeElWcHM0Q2Y4eFJKb3Fha29XakxYNFJ4cXExZHo4MFVDOHdDbENrQWs0d0lqQ3Z5cEVDRVBQR1hNNWZxSmhiUll4NFg1amZlU01oWm9fN2hkUFBBNkdKT21v?oc=5) ⭐️ 7.0/10

据路透社报道，标普警告称英伟达董事会可能存在问题，并将这家芯片制造商的信用评级列入下调观察名单；报道未披露具体治理问题或财务数据。

google\_news · Reuters · 11月25日 22:44

**「背景」** 此前英伟达 CEO 一度离任、随后回归，标普全球评级认为这暴露了公司管理层和董事会的薄弱环节，并指出部分董事任期过长可能削弱其独立性。列入负面信用观察名单意味着其“AA”评级可能被下调，但并非已经降级。

**「影响」** 据 CNBC 援引标普全球评级，若英伟达在管理与治理框架上的“缺陷”持续存在，其信用评级可能在 90 天内被下调一档，这将直接抬高该公司债券投资者的风险敞口与后续发债成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/technology/us-finds-no-evidence-china-directed-executive-spy-nvidia-ceo-wsj-reports-2026-11-25/">S&amp;P warns Nvidia&#x27;s board may be compromised, puts ... - Reuters</a></li>
<li><a href="https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3667832">NVIDIA Corp. &#x27;AA&#x27; Ratings Placed On CreditWatch N | S&amp;P ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/26/nvidia-market-governance-risk.html">Nvidia rating could be cut due to &#x27;rising&#x27; M&amp;G risk, says S &amp; P ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#S&amp;P Global Ratings`, `#credit rating downgrade watch`, `#corporate governance`, `#semiconductors`

---

<a id="item-finance-news-3"></a>
### [路透：与 Alice Huang 关联的公司在中国登记了 2.7 亿美元 AI 服务器](https://www.investing.com/news/stock-market-news/exclusivealice-huanglinked-firms-listed-270-million-in-ai-servers-in-china-records-show-5049792) ⭐️ 6.0/10

路透社独家报道称，企业记录显示，与 Alice Huang 有关联的公司在中国登记了价值 2.7 亿美元的人工智能服务器。

rss · Investing.com Stock Market News · 11月26日 03:24

**「背景」** 路透社查阅的公司记录显示，与 Alice Huang 的家族和商业伙伴有关联的企业曾为中国 AI 产业提供融资与设备；与此同时，美国当局正在调查她这家总部位于新加坡的公司。

**「影响」** 据路透报道，这类安排显示，在美国限制先进处理器出口、使硬件采购日益困难的背景下，中国科技企业可通过此类融资方式获得昂贵的 AI 算力设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/finance/alice-huang-linked-firms-listed-270-million-ai-servers-china-records-show-2026-11-25/">Alice Huang-linked firms listed $270 million in AI servers in ...</a></li>
<li><a href="https://electronics.economictimes.indiatimes.com/news/components-hardware/alice-huang-linked-firms-listed-270-million-in-ai-servers-in-china-records-show/136176720">Alice Huang&#x27;s Firms Raise $270 Million for AI Servers Amid ...</a></li>

</ul>
</details>

**标签**: `#AI servers`, `#China`, `#technology supply chain`, `#corporate records`

---
