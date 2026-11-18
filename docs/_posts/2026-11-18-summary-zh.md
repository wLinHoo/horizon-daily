---
layout: default
title: "Horizon 中文日报 · 2026-11-18"
date: 2026-11-18
lang: zh
---

> 从 5 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [GPT‑6.2 Astra 和 Sol 上线 API，Astra 降价](#item-tech-news-1) ⭐️ 8.0/10
2. [Datasette Lite 改用 Service Worker 在浏览器中运行](#item-tech-news-2) ⭐️ 8.0/10
3. [Prime Radiant 发布三款编码代理外部沙箱](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GPT‑6.2 Astra 和 Sol 上线 API，Astra 降价](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/) ⭐️ 8.0/10

OpenAI 已在 API 中推出 \`gpt-6.2-astra\` 和 \`gpt-6.2-sol\`，命令行工具 LLM 0.38 已支持这两款模型。Astra 的输入和输出价格较 GPT‑6 Astra 均下降 20%，分别为每百万 token 8 美元和 40 美元，缓存输入价格下降 60% 至 0.40 美元；Sol 的输入和输出价格维持在每百万 token 2 美元和 10 美元。能力方面，Simon Willison 的单项 Three.js 动画测试中，两款模型在 Ultra 推理档位下都不如 Claude Fable 5.2 和 Gemini 4 Carbon 擅长呈现城市变形成机甲的过程。

rss · Simon Willison · 11月17日 22:38

**「缓存输入如何计费」** 提示词缓存让后续请求可以按较低费率复用命中的输入内容，例如长任务中反复使用的上下文；未命中的输入仍按常规费率计费。上一代 GPT‑6 Astra 的缓存输入价格为每百万 token 1 美元。

**「长任务的成本变化」** 如果迁移前后的 token 用量和缓存命中率相同，反复复用大量上下文的长任务会比很少命中缓存的任务获得更高比例的 API 费用降幅。

**标签**: `#OpenAI API`, `#GPT-6.2`, `#LLM pricing`, `#prompt caching`, `#LLM CLI`

---

<a id="item-tech-news-2"></a>
### [Datasette Lite 改用 Service Worker 在浏览器中运行](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison 发布了重写版 Datasette Lite，借助 Service Worker 和基于 WebAssembly 的 Pyodide，在浏览器中直接运行原本部署在服务器上的 Datasette Python 应用。用户可以通过链接加载 SQLite 数据库、JSON、CSV 或 SQL 脚本，指定 PyPI 上的 Datasette 发行版或 GitHub 上的提交、标签或分支，并从 100 多个 SQLite 版本中选择。链接还可指定从 PyPI 或 wheel 文件地址安装插件，包括 JavaScript 可视化插件；远程数据文件的托管方需通过 CORS 允许跨域读取。作者称新版体验已接近服务端应用，但并未证实所有功能都能在浏览器中运行。

rss · Simon Willison · 11月17日 16:48

**「旧版的限制」** 2022 年推出的初版在 Web Worker 中运行 Pyodide 来模拟请求，再通过 innerHTML 将返回的 HTML 插入页面。这样插入的脚本标签不会执行，导致依赖 JavaScript 的功能无法正常工作。

**「无需部署即可验证修复」** 开发者可以用两条链接在相同数据上对比故障版本和修复版本，无需为演示另起服务器。Willison 已用这种方式展示一个分页问题：同一查询在 Datasette 1.0a42 中翻到第二页时结果为空，在 1.0a43 中则已修复。

**标签**: `#Datasette`, `#service workers`, `#Pyodide`, `#WebAssembly`, `#SQLite`

---

<a id="item-tech-news-3"></a>
### [Prime Radiant 发布三款编码代理外部沙箱](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison 与 Prime Radiant 发布了三款外部沙箱服务器：编码代理留在沙箱之外，由代理发起的代码执行则交给独立沙箱，旨在减少误操作或提示注入对宿主机造成的损害。三款实现均运行 Alpine Linux，分别采用 WebAssembly 中的 v86、Apple Containers 和内置 QEMU 的微软 Quicksand，并提供相同的本机 API，可配置供 Pi、Claude Code 和 Codex 调用。发布说明未比较三种实现的隔离强度或取舍。

rss · Simon Willison · 11月17日 22:52

**「为什么要隔离代码执行」** 如果编码代理直接在宿主机上执行命令，模型的误操作或提示注入诱导的命令就可能以代理进程的权限访问文件或发起网络请求。外部沙箱把代码执行与代理进程分开，为被执行的代码单独设定权限边界，但不会自动限制代理通过其他工具执行的操作。

**「联网与凭据控制」** 开发者可以启用可选的 HTTP/HTTPS 代理，通过允许列表限制沙箱代码可访问的主机，并借助凭据替换机制发起经过身份验证的 API 请求，无需把密钥交给代理。

**标签**: `#coding agents`, `#sandboxing`, `#prompt injection`, `#local models`

---
