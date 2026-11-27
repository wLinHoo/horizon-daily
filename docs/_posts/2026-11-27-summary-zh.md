---
layout: default
title: "Horizon 中文日报 · 2026-11-27"
date: 2026-11-27
lang: zh
generated_by: horizon-pages
---

> 从 67 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [荷兰大臣反对美国 MATCH 法案限制 ASML 对华销售](#item-tech-news-1) ⭐️ 8.0/10
2. [Google 推动 AI 代理使用 Workspace MCP，Gmail 服务器不能发信](#item-tech-news-2) ⭐️ 7.0/10
3. [Nemotron 3.5 Parse 技术指南：开放数据、微调与推理加速](#item-tech-news-3) ⭐️ 7.0/10
4. [英伟达据报暂停向东南亚四国发运服务器](#item-tech-news-4) ⭐️ 7.0/10
5. [谷歌 Play 将全球公开商家开发者电话和地址](#item-tech-news-5) ⭐️ 7.0/10
6. [中国推 BCI 标准，Neuralink 启动 ALS 晚期试验](#item-tech-news-6) ⭐️ 7.0/10
7. [sqlite3\_rsync：无需本地完整副本的 SQLite 远程快照](#item-tech-news-7) ⭐️ 6.0/10
8. [AMD Ryzen 与 Radeon 的 llama.cpp 基准测试面板发布](#item-tech-news-8) ⭐️ 6.0/10
9. [阿伦森：AI 完成高难数学证明的影响才刚开始](#item-tech-news-9) ⭐️ 6.0/10
10. [Kimi 推出科研支持计划：入选团队可获免费 API 额度](#item-tech-news-10) ⭐️ 5.0/10
11. [DeepSeek 灰度测试对话额度显示：单轮 Token 与估算费用](#item-tech-news-11) ⭐️ 5.0/10

**财经新闻**
1. [英伟达据报暂停对东南亚销售，美国收紧对华限制](#item-finance-news-1) ⭐️ 7.0/10
2. [奥驰亚据报探讨现金收购英国帝国品牌，或涉及拆分](#item-finance-news-2) ⭐️ 6.0/10
3. [CNBC：英伟达 GPU 买家被告知须排除中国租用方](#item-finance-news-3) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [荷兰大臣反对美国 MATCH 法案限制 ASML 对华销售](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 8.0/10

11 月 26 日，荷兰外贸与发展合作大臣 Sjoerd Sjoerdsma 在议会表示，荷兰不会接受美国进一步限制 ASML 对华销售，并反对 MATCH Act 的域外管辖，称荷兰“不会任人摆布”。荷兰正与欧盟委员会协调，并联合德国、法国游说，争取把该法案从美国年度国防政策法案中剔除。MATCH Act 由两党共同提出，要求荷兰、日本等盟友对华实施更严格的半导体设备出口管制，否则美方将单方面限制；中国约占 ASML 今年销售额的 20%，国会预计 12 月中旬表决，外界认为通过可能性很大。

telegram · zaihuapd · 11月26日 14:56

**「背景」** MATCH Act 是美国两党提出的法案，要求荷兰、日本等盟友对华实施更严格的半导体设备出口管制，否则美方将单方面限制这些盟友的设备销售；荷兰争议的核心是该法案的域外管辖效力。据 IOP Plus 报道，荷兰政府此前已在 11 月 18 日正式拒绝该法案。路透社还报道，荷兰议员在 11 月 24 日敦促政府抵制该法案，随后大臣在议会重申拒绝，并说明正与欧盟委员会及德国、法国协调，争取把法案从美国年度国防政策法案中剔除。

**「影响」** 若 MATCH Act 按现文本通过，ASML 等盟友国家的半导体设备商可能被迫收紧对华销售，否则将面临美国单方面限制；荷兰在表决前联合德国、法国推动剔除该条款，结果将直接影响 ASML 约 20% 的中国市场销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ioplus.nl/en/posts/dutch-reject-us-match-act-over-asml-export-controls">Dutch reject US MATCH act over ASML export controls</a></li>
<li><a href="https://www.reuters.com/world/china/dutch-lawmakers-urge-government-resist-us-match-bill-targeting-asml-2026-11-24/">Dutch lawmakers urge government to resist US MATCH bill ...</a></li>

</ul>
</details>

**标签**: `#ASML`, `#semiconductor export controls`, `#Netherlands`, `#US-China tech policy`, `#chip equipment`

---

<a id="item-tech-news-2"></a>
### [Google 推动 AI 代理使用 Workspace MCP，Gmail 服务器不能发信](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 7.0/10

据 TechStackUps 报道，Google 计划让 AI 代理通过其 MCP 服务器访问 Workspace 服务，但其中 Gmail 服务器不能发送邮件。该报道描述的是 Google 对代理接入方式的安排，并未证明完整的发信能力已经普遍可用。对于构建邮件自动化代理的开发者，这一限制意味着无法通过该 Gmail MCP 服务器完成发送环节；报道没有说明限制是临时措施、权限设计还是最终产品范围。

hackernews · ritzaco · 11月26日 09:44 · [社区讨论](https://news.ycombinator.com/item?id=50653477)

**「背景」** MCP 服务器把外部服务的具体操作暴露为 AI 代理可调用的工具；Google 的 Workspace MCP 接入说明要求先建立 Google Cloud 项目、创建面向 AI 代理的 OAuth 2.0 客户端，并配置 AI 应用连接这些服务器。也就是说，代理能执行哪些 Gmail 动作取决于服务器公开的工具集，而不是由 MCP 协议自动赋予。

**「影响」** 若该 Gmail MCP 服务器按报道所述不能发送邮件，依赖代理完成邮件发送的自动化流程会在发送环节中断，开发者需要保留独立的发信集成或采用其他受支持路径；报道未给出替代方案或时间表。

**「社区讨论」** 评论者围绕限制原因展开争论：perdy 指出 MCP 的 elicitation 原语可在工具调用前暂停并请求用户确认，因此将发送邮件设为合作方专属更像商业决定而非单纯安全措施；Schnitz 和 sp1nningaway 则分别提出用浏览器操作或 SMTP/IMAP 绕过，认为这会让集成更繁琐或更难被检测。上述均为评论者观点，不代表已证实的产品细节。

<details><summary>参考链接</summary>
<ul>
<li>Configure the Google Workspace MCP servers</li>

</ul>
</details>

**标签**: `#MCP`, `#Google Workspace`, `#AI agents`, `#Gmail API`, `#developer tooling`

---

<a id="item-tech-news-3"></a>
### [Nemotron 3.5 Parse 技术指南：开放数据、微调与推理加速](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) ⭐️ 7.0/10

Hugging Face 博客发布了 Nemotron 3.5 Parse 的构建指南，内容围绕开放数据、模型微调与推理优化展开。现有材料只提供文章标题和摘要，未给出数据集许可、模型参数规模、推理吞吐提升幅度或兼容性条件等具体数字。因此，这篇文章应被视为技术实践说明，而非新的模型版本发布，也不是经过独立验证的性能声明。

rss · Hugging Face Blog · 11月26日 05:05

**「背景」** Nemotron 3.5 Parse 是 NVIDIA 的紧凑型文档图像解析模型，用于把页面图像转换为带语义版面类别、边界框和阅读顺序的机器可读文本，供检索增强生成（RAG）等下游流程使用。此次 Hugging Face 博文讨论的是在该模型基础上公开三套合成数据集、微调配方和一个 DFlash2 speculator，属于配套数据与推理优化材料，而不是另发一个新的基础模型。

**「对使用者的具体影响」** 对使用该解析器的开发者而言，可直接照搬其方案：先用自有文档做 SFT 教会模型特定版式能力，再用 RLVR 提升输出一致性，同时借助文中所述的架构改动与 DFlash2 降低推理开销。需要注意的是，该模型（约 6.31 亿参数）输出的是包含语义版面类别、边界框和阅读顺序的结构化结果，下游处理流程须按此结构解析，而不能再按纯文本处理。

<details><summary>参考链接</summary>
<ul>
<li>Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster ...</li>
<li>nemotron-3.5-parse Model by NVIDIA</li>
<li>Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning,... - daily.dev</li>
<li><a href="https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin">Building on Nemotron 3 . 5 Parse : Open Data, Fine-Tuning, and Faster...</a></li>
<li><a href="https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-3_5-parse">nvidia / nemotron - 3 . 5 - parse</a></li>
<li><a href="https://theresanaiforthat.com/model/nemotron-3-5-parse/">Nemotron 3 . 5 Parse | AI Model | There&#x27;s An AI For That</a></li>

</ul>
</details>

**标签**: `#Nemotron`, `#fine-tuning`, `#open data`, `#inference optimization`, `#Hugging Face`

---

<a id="item-tech-news-4"></a>
### [英伟达据报暂停向东南亚四国发运服务器](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/) ⭐️ 7.0/10

据 TechCrunch 报道，英伟达已要求其制造合作伙伴暂停向马来西亚、新加坡、泰国和印度尼西亚发运服务器。报道称，这一暂停与美国收紧限制、阻止 AI 芯片流入中国的举措有关。报道没有说明暂停将持续多久、涉及哪些产品型号或出货规模，英伟达也未公开确认这一消息，因此目前仍属未经证实的报道。

rss · TechCrunch AI · 11月26日 20:03

**「背景」** 背景在于，Nvidia 的芯片由制造合作伙伴组装成服务器后出货；路透社和 PCMag 均转述《金融时报》的报道称，Nvidia 要求暂停向马来西亚、新加坡、泰国和印度尼西亚发运这类含其芯片的服务器。此举发生在美国收紧对华 AI 芯片出口限制之际，但现有报道没有披露暂停期限、涉及的芯片型号或受影响出货规模。

**「影响」** 对马来西亚、新加坡、泰国和印度尼西亚的 AI 服务器采购方而言，最直接的后果是已排期的交付可能延后；有报道称戴尔和超微等制造伙伴也受到此次暂停波及。相关企业应尽快向供应商确认订单状态和新的交付时间表，并据此调整算力上线计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/asia-pacific/nvidia-halts-chip-shipments-southeast-asia-ft-reports-2026-11-26/">Nvidia halts server shipments to four Southeast Asian ...</a></li>
<li><a href="https://www.pcmag.com/news/nvidia-halts-gpu-exports-to-malaysia-singapore-thailand-and-indonesia">Nvidia Halts GPU Exports to Malaysia, Singapore, Thailand ...</a></li>
<li><a href="https://www.thenationalnews.com/future/technology/2026/11/26/nvidia-halts-chip-shipments-to-south-east-asia-amid-us-crackdown/">Nvidia halts chip shipments to South-East Asia amid US ...</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/nvidia-halts-chip-shipments-southeast-asia-ft-reports-2026-11-26/">Nvidia halts server shipments to four Southeast Asian ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#export controls`, `#supply chain`, `#Southeast Asia`

---

<a id="item-tech-news-5"></a>
### [谷歌 Play 将全球公开商家开发者电话和地址](https://www.theverge.com/tech/1043228/android-play-store-google-developer-address-eu) ⭐️ 7.0/10

谷歌 Play 计划自 2027 年 3 月 1 日起，在全球范围向用户展示自我声明为“商家”的开发者的联系方式，包括个人账户持有者的电话号码和地址。所有活跃开发者账户须在 2027 年 2 月 1 日前申报商家或非商家身份，逾期可能无法更新应用，并从全球 Play 下架。该政策旨在满足欧盟《数字服务法》，但谷歌表示联系方式将向全球公开；欧盟相关规定并未要求向欧盟以外用户展示这些信息。独立开发者因此担忧隐私，谷歌不接受邮政信箱作为付款地址，而苹果仅在欧洲相关国家展示地址并允许使用邮政信箱。

rss · The Verge Tech · 11月26日 17:06

**「背景」** 欧盟《数字服务法》要求平台核验并公开商家身份信息，谷歌据此在 Play 商店引入“商家”申报机制。开发者须在 2027 年 2 月 1 日前自行申报是否属于英国和欧盟法律下的商家；谷歌给出的宽泛定义侧重于开发者是否通过应用获得收入，尤其是经常性或高额收入。

**「对开发者的实际影响」** 自行声明为“商家”的开发者若使用个人账户，其电话号码和住址将在全球范围的 Play 商店页面对所有用户可见，而谷歌不接受邮政信箱作为付款地址，这意味着没有独立营业地址的独立开发者可能被迫公开住址。开发者须在 2027 年 2 月 1 日前完成申报，逾期可能无法更新应用并被全球下架；作为对照，苹果仅对欧盟区 App Store 展示商家联系方式并允许使用邮政信箱（见 tool-2-1、tool-2-2），因此习惯苹果做法的开发者容易低估此次全球可见的范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/">Manage European Union Digital Services Act trader requirements ...</a></li>
<li><a href="https://www.macrumors.com/2024/10/17/developers-eu-app-store-trader-requirements/">Developers Now Required to Share Phone Number and Address on...</a></li>

</ul>
</details>

**标签**: `#Google Play`, `#Android`, `#Digital Services Act`, `#developer policy`, `#privacy`

---

<a id="item-tech-news-6"></a>
### [中国推 BCI 标准，Neuralink 启动 ALS 晚期试验](https://www.scmp.com/business/china-business/article/3375858/china-pushes-brain-computer-interface-breakthroughs-neuralink-advances-towards-market) ⭐️ 7.0/10

中国多家企业正竞相宣布脑机接口（BCI）突破，北京同时推动标准制定并扩大实际应用，试图在这一战略产业中超越美国。Neuralink 周三表示，将启动一项晚期临床试验，评估其植入式 BCI 设备对患有肌萎缩侧索硬化症（ALS）的成年人的安全性和有效性。报道未披露该试验的规模、时间表或中国标准的具体内容。

rss · SCMP Technology · 11月26日 07:00

**「背景」** 脑机接口通过读取神经信号并将其转化为控制指令，使 ALS 等疾病导致瘫痪的患者能够操作外部设备。据 Gizmodo 报道，Neuralink 此前已获得美国 FDA 批准，对 ALS 导致瘫痪的患者开展研究；当前的晚期试验是在这一监管与临床基础上的后续推进。

**「影响」** 对 ALS 成年患者而言，这项晚期试验将评估植入式 BCI 的安全性和有效性，是该设备走向商业化前的关键临床验证；对中国 BCI 企业而言，标准制定把行业规范纳入商业化路径，竞争不只取决于单点技术突破，还取决于能否满足后续规范并落地实际应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/neuralink-obtains-fda-approval-for-als-brain-implant-trial-2000845737">Neuralink Obtains FDA Approval for ALS Brain Implant Trial</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#Neuralink`, `#China tech policy`, `#neurotechnology`, `#medical devices`

---

<a id="item-tech-news-7"></a>
### [sqlite3\_rsync：无需本地完整副本的 SQLite 远程快照](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 6.0/10

Simon Willison 在 2026 年 11 月 26 日的文章中强调，SQLite 的 sqlite3\_rsync 可通过 SSH 把数据库快照复制到另一台机器，无需先在本地生成完整副本。这避免了 backup API 或 VACUUM INTO 在磁盘占用超过一半、无法容纳等大副本时无法完成快照的问题。该工具并非新发布：它作为实验性功能随 SQLite 3.47.0 于 2024 年 10 月加入，并在 2025 年 5 月的 3.50.0 中得到增强。SQLite 文档称，其页面哈希协商只传输有差异的页面；即使两端差异极大，哈希交换带来的额外带宽最多也仅为数据库大小的几个百分点。

rss · Simon Willison · 11月26日 06:08

**「背景」** 常规快照依赖 backup API 或 VACUUM INTO，两者都需要在本地写出与源库同等大小的副本，因此当实例已用空间超过一半时就没有足够空间完成快照。sqlite3\_rsync 把这一过程改为基于页面哈希的增量协商，既可用于首次远程复制，也可用于同步已有副本。

**「影响」** 对已用磁盘超过一半的小型实例，开发者可以把快照直接复制到另一台可通过 SSH 访问的机器，而不必先腾出与数据库等大的本地空间；使用前提是具备可用的 SSH 连接和该工具。

**标签**: `#SQLite`, `#sqlite3\_rsync`, `#database backup`, `#remote replication`, `#developer tools`

---

<a id="item-tech-news-8"></a>
### [AMD Ryzen 与 Radeon 的 llama.cpp 基准测试面板发布](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) ⭐️ 6.0/10

Hugging Face 博客于 2026 年 11 月 26 日发布公告，推出面向 AMD Ryzen 处理器与 Radeon 显卡的 llama.cpp 基准测试面板（benchmark dashboard），用于集中展示在这些 AMD 硬件上运行 llama.cpp 的性能测试结果。该面板的服务对象是关注本地大模型推理的 AMD 平台用户，使其不必只依赖零散的个人测试来判断硬件表现。现有材料仅包含公告标题与简介，未说明面板收录的模型、量化格式、llama.cpp 版本、测试方法或数据更新频率，也未给出任何具体性能数字，因此这些能力目前仍属待核实的公告内容。

rss · Hugging Face Blog · 11月26日 11:37

**「背景」** llama.cpp 是 ggml-org 维护的 C/C++ 大语言模型推理项目，代码库提供 1.5 位至 8 位的整数量化，并通过 HIP 支持 AMD GPU。此次 Hugging Face 发布的基准面板面向 AMD Ryzen 与 Radeon 硬件，汇总 llama.cpp 的测试结果，便于在本地推理场景中对比不同 AMD 配置。

**「实际影响」** 对打算用 Ryzen 或 Radeon 搭建本地推理环境的用户，这类汇总面板可作为选型与横向比较的参考入口；但在依赖其中数据前，需要先确认测试所用的 llama.cpp 版本、量化格式和驱动版本是否与自己的环境一致，否则跨配置的分数不能直接对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml - org / llama . cpp : LLM inference in C/C++ · GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AMD`, `#benchmarking`, `#local LLM`, `#hardware`

---

<a id="item-tech-news-9"></a>
### [阿伦森：AI 完成高难数学证明的影响才刚开始](https://www.cnbeta.com.tw/articles/tech/1588158.htm) ⭐️ 6.0/10

据 The Decoder 报道，前 OpenAI 研究员、美国得克萨斯大学奥斯汀分校教授斯科特·阿伦森（Scott Aaronson）在文章中称，相比证明黎曼猜想本身，AI 能够独立完成这类高难度数学证明才更值得关注，其影响可能从重塑全球经济延伸到威胁人类生存，但他也指出不同研究者对此看法不一。他分析了 OpenAI 近期在矩阵乘法和傅里叶变换上的成果：前者为一种现有快速算法给出了匹配的计算复杂度下界，后者不仅找到更快的计算方法，还证明其速度难以进一步大幅提升。阿伦森称，这类下界证明揭示的是算法优化的理论极限；他个人首次觉得证明 P≠NP 已为时不远，并称据多个可靠来源几乎确定 AI 实验室已有一项或多项未公开的密码学重磅成果，但不知具体细节。这些判断属于其评论和转述，文章未给出 P≠NP 证明或相关密码学成果的具体内容。

telegram · AI\_News\_CN · 11月27日 04:36

**「背景」** 计算复杂度下界证明并不用于刷新某个算法的速度纪录，而是试图揭示在特定计算模型下算法优化能够达到的理论极限。阿伦森今年 10 月曾撰文称，AI 实验室正在测试其模型能否破解密码系统，这为他此次关于未公开密码学成果的说法提供了直接背景。

**「对算法优化的实际约束」** 对算法研究者和依赖矩阵乘法的开发者而言，下界证明的实际约束是划定特定计算模型下的优化上限；OpenAI 11 月 24 日论文声称矩阵乘法指数恰为 9/4 并给出匹配的上下界，若该结论成立，在这些模型内继续追求更低渐进复杂度的空间将基本关闭，相关工作需转向常数因子、硬件实现或模型外条件。采用前应核对证明适用的计算模型和同行评审状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>

</ul>
</details>

**标签**: `#AI research`, `#mathematics`, `#computational complexity`, `#OpenAI`, `#cryptography`

---

<a id="item-tech-news-10"></a>
### [Kimi 推出科研支持计划：入选团队可获免费 API 额度](https://rss.bz/zh/post/kimi-free-api-credits-scientific-research?source=telegram) ⭐️ 5.0/10

Moonshot AI 旗下的 Kimi 宣布一项科研支持计划，向入选的全球研究团队提供免费的 API 额度、最新模型访问权限，以及长期合作机会。该消息由 Telegram 频道 AI 情报局转述，未披露额度规模、具体模型版本、申请条件、遴选标准或生效日期。目前可确认的只是计划被宣布，尚无法核实实际发放规模或使用限制。

telegram · AI\_News\_CN · 11月27日 04:00

**「背景」** Kimi 的“Kimi for Science”项目页面显示，该项目面向处于不同阶段的科研探索，并列出包括 K3.1 Pro、K2.6 在内的多款模型。此次面向全球研究团队提供免费 API 额度，属于该科研支持方向，让入选团队可以直接调用其最新模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/news/kimi-for-science-program">Kimi for Science｜让更多 科 学想法成为可能</a></li>

</ul>
</details>

**标签**: `#Kimi`, `#Moonshot AI`, `#API access`, `#research program`, `#AI models`

---

<a id="item-tech-news-11"></a>
### [DeepSeek 灰度测试对话额度显示：单轮 Token 与估算费用](https://www.cnbeta.com.tw/articles/tech/1588148.htm) ⭐️ 5.0/10

DeepSeek 正在网页端和移动端 App 灰度测试“显示本轮消耗额度”功能。用户完成一轮对话后，界面会弹出详情卡片，列出本轮消耗的 Token，并细分为“输入（缓存未命中）”和“输出”，按与 API 持平的价格估算金额，同时提示当前上下文占用百分比。用户截图显示，单轮估算费用可低至 0.000536 元，但卡片仍标注“免费”。该功能目前来自用户反馈的灰度测试，DeepSeek 尚未公布正式上线范围和计费规则。

telegram · AI\_News\_CN · 11月27日 04:15

**「背景」** 大模型 API 通常按 Token 计费，并把输入与输出分开计价，其中命中缓存的输入单价更低；DeepSeek 的网页端和 App 对话本身免费，但底层算力消耗与 API 调用同源。此次灰度测试的卡片正是把一轮对话的 Token 拆成“输入（缓存未命中）”和“输出”，再按持平 API 的价格折算成参考金额，并给出上下文占用比例，让免费用户在免费使用中看到与计费口径一致的消耗情况。

**「实际影响」** 处于灰度范围的用户可直接看到每轮对话的 Token 构成和上下文占用，便于判断长对话的成本；但卡片金额只是按 API 价格估算，且截图显示“免费”，不应将其理解为实际扣费。

**标签**: `#DeepSeek`, `#token usage`, `#AI cost transparency`, `#product update`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达据报暂停对东南亚销售，美国收紧对华限制](https://news.google.com/rss/articles/CBMiggFBVV95cUxNSHM3RHJjQzd5X25CS3B2YkpjVm9fa092SkJjUmlWLS1xRi1EaFZNam9wTi1lbUpmTXdPeVRaYXdjM2hnT2dLenQyQXVtOHZzcDJ5SkZSeGdlS0ZCZHMtMUNfclhqT3VJVUNmNy1yUmtNMnlnRkhvd1ZWV2FKdVQ1QmtB?oc=5) ⭐️ 7.0/10

据《纽约时报》报道，英伟达已暂停向东南亚销售，背景是美国进一步收紧对华出口限制；《华尔街日报》亦报道，该公司要求合作伙伴暂停向东南亚发货。报道未说明涉及的具体产品、暂停范围和持续时间，英伟达与相关政府机构也未作确认。

google\_news · The New York Times · 11月27日 02:45

**「背景」** 背景是，东南亚已成为英伟达的重要市场，当地一些被称为“neoclouds”的数据中心运营商专门对外出租算力。据《金融时报》报道，其中四个东南亚国家已成为中国 AI 开发者获取受华盛顿限制的英伟达最先进芯片的热门目的地，而美国在英伟达此举前一周刚出台新的出口限制。

**「影响」** 马来西亚、新加坡、泰国和印度尼西亚的数据中心运营商，以及英伟达的代工合作厂商，将直接受到冲击：据 TrendForce 和 U.S. News 报道，上周生效的美国新规要求向上述国家出口先进芯片必须申请许可证，因此相关 AI 服务器交付已被要求暂停。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/26/business/nvidia-southeast-asia-sales.html">Nvidia Halts Sales to Southeast Asia as U . S . Tightens China ...</a></li>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/11/26/nvidia-reportedly-halts-ai-chip-shipments-to-southeast-asia-as-us-tightens-china-curbs/">Nvidia Halts Server Shipments To 4 Southeast Asian Countries Amid...</a></li>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/26/news-nvidia-reportedly-suspends-ai-server-shipments-to-four-southeast-asian-countries-as-u-s-targets-chinese-ai-access/">[News] NVIDIA Reportedly Suspends AI Server Shipments to Four ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-11-26/nvidia-halts-server-shipments-to-four-southeast-asian-countries-ft-reports">Nvidia Halts Server Shipments to Four Southeast Asian ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#U.S. export controls`, `#China restrictions`, `#semiconductors`, `#Southeast Asia`

---

<a id="item-finance-news-2"></a>
### [奥驰亚据报探讨现金收购英国帝国品牌，或涉及拆分](https://www.investing.com/news/stock-market-news/marlboro-maker-altria-explores-takeover-of-uks-imperial-brands-5052558) ⭐️ 6.0/10

路透社报道称，万宝路母公司奥驰亚（Altria）正在探讨以现金收购英国上市的帝国品牌（Imperial Brands），并可能对后者进行拆分。该报道未提及交易金额、融资安排或已确认的正式报价，交易仍处探索阶段。

rss · Investing.com Stock Market News · 11月27日 04:06

**「背景」** 奥驰亚（万宝路品牌母公司）与帝国品牌都是大型烟草企业，两家在新型烟草产品线上落后于菲利普莫里斯国际和英美烟草等对手，此前向传统烟草以外扩张的尝试结果好坏参半。帝国品牌在伦敦上市，若交易达成，将是又一家从伦敦市场退市的英国大型上市公司。

**「潜在影响」** 若交易推进，Imperial Brands 股东可能获得现金对价，伦敦上市公司行列也将再少一家大型烟草企业；但该收购目前仍处探索阶段，尚未提出正式报价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nypost.com/2026/11/26/business/marlboro-maker-altria-exploring-imperial-brands-takeover-in-big-tobacco-mega-deal/">Marlboro maker Altria exploring Imperial Brands takeover in Big...</a></li>
<li><a href="https://www.ft.com/content/696e99b0-f6d1-4a1a-95b0-f68de88520d9?syn-25a6b1a6=1">Altria explores takeover bid for Imperial Brands</a></li>
<li><a href="https://www.ft.com/content/696e99b0-f6d1-4a1a-95b0-f68de88520d9?syn-25a6b1a6=1">Altria explores takeover bid for Imperial Brands</a></li>

</ul>
</details>

**标签**: `#Altria`, `#Imperial Brands`, `#M&amp;A`, `#tobacco`, `#UK`

---

<a id="item-finance-news-3"></a>
### [CNBC：英伟达 GPU 买家被告知须排除中国租用方](https://news.google.com/rss/articles/CBMib0FVX3lxTE1ydHdQWUpYRU16SjgyRXBibzZ6UFN4RThEMUV3VkRJV0NCNmk1Nm1wTFlvTnpsLS1VVHdmczlIQjZRN0RKZnlBdm5oSmFUY0lCaWV5dTY2bDBiRHcyV0lfMjk3ZS1TQW1oM3F0TTJFRdIBdEFVX3lxTE1hb0dnX1V6U3RzcVduQUhNcHBONFFMMVVaaThOcEc5dy1EOVMwUXBVM1lSMWljNm12aTJXT0FvMWdkaUdyTEZyZGY0dHJ0R3kxQllKQ2RaMl9MYmxIY2pHcTh6TWVDRkhCSkVqUVUtbVFOam81?oc=5) ⭐️ 6.0/10

CNBC 援引未具名消息人士报道，英伟达（Nvidia）GPU 的买家被告知，采购时必须排除中国租用方。报道未说明该要求的适用范围、执行方式或财务影响。

google\_news · CNBC · 11月26日 15:34

**「背景」** 所谓“neocloud”是指对外出租 AI 算力的云服务商；据 CNBC 基于两名知情人士的报道，芯片销售方把“不向中国公司出租算力”作为向其供应英伟达芯片的条件。

<details><summary>参考链接</summary>
<ul>
<li>Nvidia chip buyers told to rule out Chinese renters to purchase GPUs</li>
<li>Nvidia chip buyers told to rule out Chinese renters to purchase GPUs ...</li>

</ul>
</details>

**标签**: `#Nvidia`, `#GPUs`, `#export controls`, `#AI chips`, `#China`

---
