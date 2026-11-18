---
layout: default
title: "Horizon 中文日报 · 2026-11-18"
date: 2026-11-18
lang: zh
generated_by: horizon-pages
---

> 从 5 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Datasette Lite 借 Service Worker 与 Pyodide 运行完整应用](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 发布 GPT-6.2 Astra 与 Sol，API 价格下调](#item-tech-news-2) ⭐️ 8.0/10
3. [编码智能体的外部沙箱模式与三个实现](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Datasette Lite 借 Service Worker 与 Pyodide 运行完整应用](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison 发布了 Datasette Lite 的完整重写版，改用 Service Worker 和 Pyodide，让完整的 Datasette Python 应用直接在浏览器中运行；他称其现在与真正的服务端版本“几乎无法区分”。用户可通过 lite.datasette.io 的 URL 参数从 PyPI 选择已发布的 Datasette 版本，或指定 GitHub 仓库的提交、标签、分支，还可在 100 多个 SQLite 版本中选择，并从 PyPI 或 wheel 文件 URL 安装插件，且可重复传参安装多个插件。它也能通过 URL 加载 SQLite 数据库、JSON、CSV 或 SQL 脚本；远程数据库等资源 URL 需要提供开放的 CORS 头。

rss · Simon Willison · 11月17日 16:48

**「背景：从 innerHTML 注入到 Service Worker 拦截」** Datasette Lite 并非新项目：Simon Willison 于 2022 年发布首版，最初更像一个玩笑——把服务端 Python 应用搬进浏览器。但旧实现属于“取巧”：它在 Pyodide Web Worker 中运行 Datasette，模拟请求栈，再把生成的 HTML 通过 innerHTML 注入顶层页面；由于 innerHTML 中的 script 标签不会执行，任何依赖 JavaScript 的功能都会失效。此次重写改用 Service Worker 拦截请求，才使浏览器内的 Datasette 接近真实服务端应用的行为。

**「影响」** 对 Datasette 开发者和用户而言，bug 复现和进行中功能的演示现在可以封装成可分享链接，无需启动 Web 服务器。Willison 已在 issue 中用分别指向 1.0a42 和 1.0a43 的 Datasette Lite 链接对比分页 bug 与修复，说明 URL 中的版本固定参数可直接用于开发协作。

**标签**: `#Datasette`, `#Pyodide`, `#WebAssembly`, `#Service Workers`, `#Python`

---

<a id="item-tech-news-2"></a>
### [OpenAI 发布 GPT-6.2 Astra 与 Sol，API 价格下调](https://openai.com/index/introducing-gpt-6-2-astra-sol) ⭐️ 8.0/10

OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol：前者自称面向最难项目的前沿模型，后者主打日常工作的效率与通用性，二者已可通过 API 以 gpt-6.2-astra 和 gpt-6.2-sol 调用。官方公告称其在专业输出、编程、电脑操作与成本效率上有所提升，但未随公告给出任何基准数据或具体的可用性细节。据 Simon Willison 的博客，Astra 定价为每百万 token 输入 8 美元、输出 40 美元，是上一代 GPT-6 Astra（10/50 美元）的八成，缓存价格由每百万 1 美元降至 0.40 美元；Sol 维持 2/10 美元，与 6.1 Sol 相同，为 GPT-5.6 Sol（4/20 美元）的一半，Willison 的 LLM 0.38 已同步支持这两个模型。早期反馈分化：Willison 用 pelican 绘图和 Codex CLI 的 three.js 动画测试后发现，两模型在“扬克斯变形成机甲”任务上的表现不如 Claude Fable 5.2 与 Gemini 4 Carbon，Astra 在多项基准上也略低于 Fable 5.2，开发者 Theo Browne 则抱怨它在长任务中会停下来追问用户根本无法理解的内部实现细节。

rss · OpenAI News · 11月17日 17:45

**「背景：Astra/Sol 双线命名与前代价格」** Astra 与 Sol 延续了 OpenAI 此前的双线命名：Astra 面向高难度任务，Sol 定位日常高效工作，本次分别接替 GPT-6 Astra 与 GPT-6.1 Sol、GPT-6 Sol。API 中两者以 \`gpt-6.2-astra\` 和 \`gpt-6.2-sol\` 提供。价格沿革也是理解这次发布的关键：GPT-6 Astra 与 Claude Fable 5 均为每百万 token 输入 10 美元、输出 50 美元，GPT-6.2 Astra 降到 8/40 美元；Sol 则维持 2/10 美元，而更早的 GPT-5.6 Sol 为 4/20 美元。

**「对长任务成本与选型的影响」** 对通过 API 或 Codex 跑长时间 agent 任务的团队来说，最直接的变化是价格：Astra 的输入/输出定价为每百万 token 8 美元/40 美元，比上一代 GPT-6 Astra 的 10/50 降了两成，缓存输入价更从每百万 token 1 美元降到 0.40 美元，而 Sol 维持 2/10 美元不变。两个档位的差距并非全面：按第三方汇总数据，Astra 在 17 项基准中赢下 15 项，但 Sol 在 3:1 输入/输出混合口径下每 token 便宜约 4 倍，因此高频、短交互的日常任务仍更适合 Sol。使用上还需注意，Theo Browne 的反馈指出 Astra 在长任务中会因追问用户无法判断的实现细节而进入“blocked”状态，将其用于无人值守的长流程时应预先设定好中断与确认策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/models/compare/gpt-6.2-astra-vs-gpt-6.2-sol">GPT-6.2 Astra vs GPT-6.2 Sol: Benchmarks, Pricing &amp; Which Is ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#LLM release`, `#AI coding`, `#computer use`, `#API efficiency`

---

<a id="item-tech-news-3"></a>
### [编码智能体的外部沙箱模式与三个实现](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison 与 Prime Radiant 发布了面向编码智能体的“外部沙箱”模式，以及三个采用该模式的沙箱服务器实现，目标是降低代理执行代码时因失误或提示注入而破坏本机的风险。三个实现分别是：external-sandbox-v86 用 Node.js 服务器经 v86 在 WebAssembly 中运行 Alpine Linux；external-sandbox-container 用 Python Web 服务器在 Apple Containers 中运行 Alpine Linux；external-sandbox-quicksand 用 Python Web 服务器调用微软的 Quicksand，该库把 QEMU 和 Alpine Linux 打包进 Python 包。它们提供相同的 localhost API，可让 Pi、Claude Code 或 Codex 在需要执行代码时调用沙箱，并附带可选的 HTTP/HTTPS 允许列表代理和凭据替换机制，以限制出站主机并在不向代理暴露密钥的情况下发起认证 API 调用。

rss · Simon Willison · 11月17日 22:52

**「背景」** 外部沙箱模式的关键前提，是把编码 agent 与它实际执行的代码隔离开：agent 只通过 localhost API 向专用沙箱发送要执行的代码，而 agent 自身仍留在沙箱之外。Prime Radiant 是提出这一模式的 AI 研究实验室，也是 Superpowers 的开发方；Superpowers 是一套为编码 agent 提供头脑风暴、规划、测试驱动开发和代码审查等结构化流程的技能框架。

**「影响」** 对需要运行本地模型或不受信任生成代码的开发者，具体做法是把 Pi、Claude Code 或 Codex 的代码执行调用指向该 localhost API，并在允许列表代理中设置允许访问的主机；需要认证的请求可通过凭据替换发出，而不把密钥交给代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://primeradiant.com/superpowers/">Superpowers | Prime Radiant</a></li>
<li><a href="https://primeradiant.com/about/">About | Prime Radiant</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#sandboxing`, `#AI security`, `#prompt injection`, `#developer tooling`

---
