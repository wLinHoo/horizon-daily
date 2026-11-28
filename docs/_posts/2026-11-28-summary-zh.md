---
layout: default
title: "Horizon 中文日报 · 2026-11-28"
date: 2026-11-28
lang: zh
generated_by: horizon-pages
---

> 从 59 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [Google DeepCrossAttention 称最高提速 3 倍且质量相当](#item-tech-news-1) ⭐️ 7.0/10
2. [腾讯在《自然》发表 AI 药物设计论文，靶向肥胖、糖尿病与癌症](#item-tech-news-2) ⭐️ 7.0/10
3. [OpenAI 反诉苹果窃取商业机密并阻挠硬件供应](#item-tech-news-3) ⭐️ 7.0/10
4. [《我的世界》基岩版资源包漏洞已在 26.65 修复](#item-tech-news-4) ⭐️ 7.0/10
5. [Convex 技能被指上传用户应用构想](#item-tech-news-5) ⭐️ 6.0/10
6. [datasette-charts 0.4a0 改进插件钩子并上线文档站](#item-tech-news-6) ⭐️ 5.0/10
7. [OpenAI 演示语音对话周边商店](#item-tech-news-7) ⭐️ 5.0/10

**财经新闻**
1. [欧洲央行官员据报释放进一步加息信号](#item-finance-news-1) ⭐️ 7.0/10
2. [彭博：英伟达 Blackwell 芯片出现在与中国一处与 Alice Huang 有关联的地点](#item-finance-news-2) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google DeepCrossAttention 称最高提速 3 倍且质量相当](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 在一篇博客中介绍了 DeepCrossAttention，一种针对 transformer 残差连接的改进方法，声称在模型质量相当的情况下运行速度最高可提升 3 倍。现有材料没有提供可供独立复核的详细基准，也未说明具体模型、硬件或任务范围，因此这一加速幅度应视为研究团队的声明，而非已经复现的结果。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** Google Research 在 2026 年 11 月 23 日的博客中介绍的 DeepCrossAttention，源自其 ICML 2025 论文。它针对 Transformer 中“直接把前几层输出相加”的传统残差连接：论文认为这种做法可能稀释关键信息，因此改用依赖输入的逐层交叉注意力来生成 Query、Key 和 Value。

**「影响」** 对考虑采用该方法的团队而言，当前最具体的动作是先在自己的模型和硬件上复测速度与质量，而不是直接把 3 倍加速计入容量规划；缺乏详细基准意味着兼容性和实际收益仍不确定。

**「社区讨论」** Hacker News 的讨论更多集中在结果呈现而非技术验证：一位评论者认为这些结果不应画成折线图，因为各方法之间没有时间关系；另一位则追问该加速能否与现有推理优化叠加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/abs/2502.06785">[2502.06785] DeepCrossAttention : Supercharging Transformer ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#AI research`, `#model optimization`, `#Google Research`, `#residual connections`

---

<a id="item-tech-news-2"></a>
### [腾讯在《自然》发表 AI 药物设计论文，靶向肥胖、糖尿病与癌症](https://www.scmp.com/tech/tech-trends/article/3376082/chinas-tencent-makes-ai-drug-discovery-breakthrough-nature-paper) ⭐️ 7.0/10

腾讯宣布已在《自然》（Nature）发表论文，介绍其利用人工智能设计肥胖、糖尿病和癌症新型疗法的研究。该论文于 2025 年 6 月投稿，本周三正式刊出，研究团队来自腾讯。目前公开的报道摘录被截断，未披露具体分子结果、基准测试或实验验证数据，因此“突破”的程度尚无法独立评估。

rss · SCMP Technology · 11月27日 12:30

**「背景」** AI 药物发现通常先由模型生成或筛选候选分子，再通过实验验证；此次腾讯的论文涉及一个名为 ORIDTP 的平台，目标是设计能同时作用于两个疾病靶点的高活性治疗性多肽。论文于 2025 年 6 月投稿，2026 年 11 月才在《Nature》刊出，说明其经过了同行评审流程。

**「可核查性」** 论文正式刊出后，外部研究者可以查阅腾讯的方法细节并据此评估或复现其流程；在完整结果与验证数据公开前，将该方法用于实际药物开发仍缺乏依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://insightsintegration.com/tencents-ai-drug-breakthrough-designing-dual-target-peptides-for-obesity-diabetes-and-cancer/">Tencent’s AI Drug Breakthrough: Designing Dual-Target ...</a></li>

</ul>
</details>

**标签**: `#AI drug discovery`, `#Tencent`, `#Nature`, `#machine learning`, `#biotech`

---

<a id="item-tech-news-3"></a>
### [OpenAI 反诉苹果窃取商业机密并阻挠硬件供应](https://www.cnbeta.com.tw/articles/tech/1588264.htm) ⭐️ 7.0/10

OpenAI 于周五向加州法院提起诉讼，反诉苹果窃取商业机密、胁迫供应商阻断其硬件计划，并指控苹果“不择手段地进行不正当竞争”。这是对苹果今夏指控 OpenAI 及包括首席硬件官 Tang Tan 在内的前员工泄露机密的回应；OpenAI 还称，一名重返苹果的前员工向苹果泄露了其产品计划和供应商细节，而苹果被指鼓励员工将公司文件存放在个人设备和云存储中。苹果尚未立即回应置评请求，上述指控尚未经法院认定，报道也未提供苹果方面的说法。

telegram · AI\_News\_CN · 11月27日 21:36

**「背景」** 这起反诉源于 2026 年 7 月 10 日苹果在加州联邦法院对 OpenAI 及其硬件子公司 io Products、两名前苹果员工 Tang Tan 和 Chang Liu 提起的商业秘密诉讼；Tang Tan 现任 OpenAI 首席硬件官。OpenAI 当时否认窃密，并在 8 月将苹果的诉讼称为阻止其招募苹果员工的手段。

**「影响」** 对同时服务两家公司的供应商而言，这起诉讼把苹果施压的风险公开化；在法院厘清前，供应商可能面临更严格的保密与排产取舍，OpenAI 新设备计划的供应链安排也会更不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jul/10/apple-sues-openai-trade-secrets">Apple sues OpenAI , alleging artificial intelligence company stole trade ...</a></li>
<li><a href="https://www.business-standard.com/technology/tech-news/apple-openai-trade-secret-dispute-internal-chats-timeline-explained-126080500870_1.html">Apple - OpenAI trade secret fight: Claims, chats... - Business Standard</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Apple`, `#trade secrets`, `#legal dispute`, `#hardware supply chain`

---

<a id="item-tech-news-4"></a>
### [《我的世界》基岩版资源包漏洞已在 26.65 修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

《我的世界》基岩版被曝存在资源包安全漏洞：含 content.zipe 的资源包可修改 Ore UI 界面文件并运行隐藏脚本。附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开该问题，称已确认影响 26.52 至 26.63 版本，更早版本也可能受影响，覆盖 PC、手机和主机，Java 版不受影响。玩家加入服务器或 Realm 并开启资源包自动下载时，可能在未手动安装的情况下收到问题文件；已列举的利用方式包括删除全部存档、获取玩家 IP，以及在 Windows 特定条件下无提示打开任意 URI 或启动资源包内批处理文件下载恶意软件。Mojang 已在 26.65 版修复；AxmBro 发布的 Windows 只读检测工具可查找 content.zipe，但无法判定资源包是否恶意。

telegram · zaihuapd · 11月27日 18:04

**「背景」** 《我的世界》基岩版的 Ore UI 是游戏界面框架，资源包则可由服务器或 Realm 在玩家加入时自动下发。此次问题把两者连接起来：资源包内的 content.zipe 可改写 Ore UI 文件，使恶意资源包不再只是替换材质外观。

**「影响与应对」** 服务器和 Realm 管理员应确认玩家客户端升级到 26.65，或在无法升级时关闭资源包自动下载，以降低玩家加入时自动接收问题资源包的风险。只读检测工具只能定位 content.zipe，不能替代版本升级，也不能判断资源包是否具有恶意意图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://minecraft.pl/en/news/minecraft-bedrock-mojang-patches-resource-pack-security-hole">Minecraft Bedrock: Mojang patches resource pack security</a></li>
<li><a href="https://nqbrief.com/en/games/minecraft-bedrock-26-65-resource-pack-fix/">Minecraft Bedrock 26.65 released to fix resource-pack exploit</a></li>

</ul>
</details>

**标签**: `#Minecraft Bedrock`, `#安全漏洞`, `#资源包`, `#远程代码执行`, `#Mojang`

---

<a id="item-tech-news-5"></a>
### [Convex 技能被指上传用户应用构想](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 6.0/10

一份提交到 convex-backend-skill 仓库的 GitHub issue（\#64）指控 Convex 的后端技能在未告知用户的情况下，把用户的应用构想发送到远程服务器。Convex CEO Jamie 在评论中说明，该插件中的提示上传用于支撑 Convex 的“quickstart”功能，并称 quickstart 是近期关停的端到端 vibe-coding 产品 Convex Chef 的继任者。现有材料确认了 quickstart 涉及提示上传，但未独立验证“未告知”的指控，也未说明上传内容的保留范围或用户退出方式。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 的 \`convex-backend-skill\` 插件把 quickstart 作为一项代理技能，用于快速搭建并运行后端项目。2026 年 10 月 26 日，一名代理技能目录维护者提交了 issue \#64，称 \`quickstart\`、\`add\` 和 \`labs-quickstart\` 会把用户的应用想法发送到 \`convex.site\` 主机并执行远程脚本，其中 \`labs-quickstart\` 还把下载与运行拆成两次 Bash 调用以避开安全检查。

**「影响」** 对使用该技能的开发者而言，若提示中包含未公开的应用构想，应假定这些内容会随 quickstart 上传到远程服务器；处理敏感项目时，应先确认披露和数据处理条款，或避免把机密构想写进提示。

**「社区讨论」** Convex CEO Jamie 在评论中说明上传用于 quickstart，并称 quickstart 是已关停的 Convex Chef 的继任者；其他评论者则围绕信任与风险发表看法，有人认为“点子很廉价”，也有人认为提示注入比模型自主发起恶意工具调用更常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/convex/convex-backend-skill/issues">Issues · convex/convex-backend-skill · GitHub</a></li>
<li><a href="https://dev.to/frankchu/3-telemetry-calls-before-your-app-exists-convex-skills-69f">3 telemetry calls before your app exists — Convex skills</a></li>

</ul>
</details>

**标签**: `#AI developer tools`, `#privacy`, `#security`, `#Convex`, `#agent tooling`

---

<a id="item-tech-news-6"></a>
### [datasette-charts 0.4a0 改进插件钩子并上线文档站](https://simonwillison.net/2026/Nov/27/datasette-charts/) ⭐️ 5.0/10

datasette-charts 发布 0.4a0 版本，重点针对其用于让其他插件定义新图表类型的插件钩子做了重新设计。作者 Simon Willison 表示，此前该钩子尚未被实际使用，他让 Claude Opus 5.5 构建了一个实验性插件来试用该钩子，发现多处设计摩擦点，此版本针对这些问题做了调整，目标是让构建额外图表插件更顺手。同时新增了插件网站 charts.datasette.io，包含面向插件作者的教程，以及展示全部核心图表与标注的 gallery，每个条目都链接到 Datasette Lite 上的可交互演示。这是一个 alpha 版本，属增量改进，主要影响 Datasette 生态中的插件开发者。

rss · Simon Willison · 11月27日 23:57

**「背景」** Datasette 通过插件钩子让第三方扩展其功能；datasette-charts 也提供了一套钩子，允许其他插件定义新的图表类型，但作者此前尚未实际用它构建过图表插件。0.4a0 对钩子设计的调整，来自一次用 Claude Opus 5.5 编写的实验性插件对这套钩子的试用。

**「影响」** 对于已经在写或计划写图表插件的开发者，0.4a0 改变了插件钩子接口，意味着针对旧钩子设计的第三方图表插件需要按新设计调整；由于是 0.4a0 预发布版，升级前应先在测试环境验证现有插件与图表的兼容性，教程和 gallery 中的演示可作为对照参考。

**标签**: `#datasette`, `#open-source`, `#developer-tools`, `#data-visualization`, `#plugin-architecture`

---

<a id="item-tech-news-7"></a>
### [OpenAI 演示语音对话周边商店](https://x.com/OpenAIDevs/status/2126372238853112227) ⭐️ 5.0/10

OpenAI Developers 在 X 上发布了一段短视频，演示一个可以用语音对话的周边商品商店。演示称，GPT-Live-1.1 会读出加急费用和预计送达时间，Decisions API 用于给退回马克杯的损坏程度打分，WebMCP 则让任何 agent 都能调用商店的购物车工具。帖子没有提供这些接口的版本细节、可用范围或独立测试结果，因此目前只能视为官方宣传演示，而非已经发布的产品能力。

twitter · OpenAI Developers · 11月27日 17:47

**「背景」** GPT-Live 是 OpenAI 的全双工语音模型，可同时听与说，不再像对讲机那样轮流发言；据 64bit.co.uk 报道，ChatGPT 高级语音模式默认使用 GPT-Live-1 mini，付费用户可调用完整模型。WebMCP 是 Chrome 开发者文档中与 MCP 并列的浏览器侧方案，让网站把页面内的操作以工具形式暴露给 AI 代理，由代理直接调用而不必模拟点击。推文中出现的 GPT-Live-1.1 与“Decisions API”未在上述资料里出现，其具体能力和开放范围目前无法从现有信息确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aixploria.com/en/ai-radar/openai-gpt-live-voice-stops-interrupting-you/">OpenAI &#x27;s GPT - Live Wants ChatGPT to Stop Interrupting You - AIxploria</a></li>
<li><a href="https://64bit.co.uk/openai-gpt-live-1-voice-models/">OpenAI Launches GPT - Live - 1 Voice Models That Listen and Speak...</a></li>
<li><a href="https://developer.chrome.com/docs/ai/webmcp/compare-mcp">When to use WebMCP and MCP | AI in Chrome | Chrome for Developers</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#agents`, `#developer tools`, `#WebMCP`, `#API`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [欧洲央行官员据报释放进一步加息信号](https://www.investing.com/news/stock-market-news/ecb-officials-signal-further-rate-hikes-as-inflation-remains-elevated-5054086) ⭐️ 7.0/10

据 Investing.com 报道，在欧洲通胀仍处高位之际，欧洲央行官员释放了将进一步加息的信号。该报道未提及具体官员姓名、加息幅度或通胀数据。

rss · Investing.com Stock Market News · 11月28日 01:40

**「背景」** 据雅虎财经报道，欧元区通胀率目前为 4%，是欧洲央行 2%中期目标的两倍（tool-1-1）。欧洲央行已在 2026 年 9 月 10 日的会议上将三项关键利率上调 25 个基点，并表示通胀将在较长时期内明显高于目标（tool-1-2）。

**「影响」** 若加息落地，浮动利率房贷借款人将直接面临更高的还款成本，房地产和公用事业等对利率敏感的行业也被市场评论视为最易承压的板块；这类板块在欧洲股市中的表现可能受到拖累（上述为市场参与者观点，非欧洲央行评估）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/economy/policy/articles/ecb-officials-signal-further-rate-021011560.html?fr=sycsrp_catchall">ECB officials signal further rate hikes as inflation remains ...</a></li>
<li><a href="https://www.ecb.europa.eu/press/economic-bulletin/html/eb202606.en.html">Economic Bulletin Issue 6, 2026 - European Central Bank</a></li>
<li><a href="https://www.linkedin.com/posts/turki-alahmadi-msc-5a748884_ecb-interestrates-inflation-activity-7440706255117029376-kQcQ">ECB Rate Hikes Loom: Impact on European Markets | LinkedIn</a></li>

</ul>
</details>

**标签**: `#ECB`, `#monetary policy`, `#interest rates`, `#inflation`, `#eurozone`

---

<a id="item-finance-news-2"></a>
### [彭博：英伟达 Blackwell 芯片出现在与中国一处与 Alice Huang 有关联的地点](https://news.google.com/rss/articles/CBMitgFBVV95cUxOajRDYnpkT2kwWEdlR2REeG93cnBZdkdsYmo3dTFmaVp3enZYN3Jid0RYVWZwNXJvcE00OG5FNjdwd0MzQXpFV1gzeUxkdnhxTVNoaGVNRmpnRllMTGY4emNtNW9VYnc4RWZVX0I2WExQNy1Ha21aV0FNWWVUb0FacnFLM01rUWRudjBCdGJpbGxCVUx3dl9KMEtZb0pyYURCTG1iWW5xUmNpaDlnc0lsMVpldmV6QQ?oc=5) ⭐️ 6.0/10

彭博社报道称，英伟达 Blackwell 芯片出现在中国一处与 Alice Huang 有关联的地点；报道未披露芯片数量、涉及各方或来源等细节，具体情况尚不清楚。

google\_news · Bloomberg.com · 11月27日 11:45

**「背景」** Blackwell 是英伟达的先进 AI 芯片，美国规定其出口到中国需许可证，目前仅性能较低的 H200 可在附加条件下对华销售。彭博查阅的文件显示，相关芯片出现在与 Megaspeed 有关联的 Alice Huang 相关的上海数据中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/">Export-banned Nvidia chips are behind China&#x27;s most powerful ...</a></li>
<li><a href="https://nypost.com/2026/11/27/us-news/banned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report/">Banned Nvidia chips uncovered at Chinese data center linked ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Blackwell chips`, `#China`, `#export controls`, `#AI supply chain`

---
