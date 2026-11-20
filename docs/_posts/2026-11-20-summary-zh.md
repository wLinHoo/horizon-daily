---
layout: default
title: "Horizon 中文日报 · 2026-11-20"
date: 2026-11-20
lang: zh
generated_by: horizon-pages
---

> 从 3 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [PostgreSQL 19 发布，新增 WAIT FOR LSN 支持备库读己之写](#item-tech-news-1) ⭐️ 9.0/10
2. [ChatPRD 因 token 欺诈与转售滥用逐步停掉免费试用](#item-tech-news-2) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [PostgreSQL 19 发布，新增 WAIT FOR LSN 支持备库读己之写](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 9.0/10

PostgreSQL 19 已发布，为把读请求发往备库的应用新增 \`WAIT FOR LSN\` 命令：会话可以等待备库将 WAL 回放到指定 LSN 后再执行查询，从而读到刚在主库写入的数据。该命令支持可选的 \`TIMEOUT\` 参数；如果备库未在指定时间内追上，就会返回错误。此次发布比通常的 9 月节奏晚约两个月，据 Simon Willison 报道，主要原因是 PostgreSQL 团队需要处理大量由 AI 报告的漏洞问题。

rss · Simon Willison · 11月19日 20:43

**「背景：备库重放延迟与“读己之写”」** 在 PostgreSQL 的流复制架构中，备库需要重放主库写入的预写日志（WAL）才能看到新数据；由于重放存在延迟，刚在主库提交的写入不一定能立刻从备库读到，因此在读写分离场景下，要在应用层自行实现“等待备库追平”的逻辑。MediaWiki 长期采用这一模式：把主库的 binlog 位置保存到会话中，在每次请求读取备库前先等待备库追到该位置，其实现如今调用 MySQL 的 WAIT\_FOR\_EXECUTED\_GTID\_SET\(\)，并以 SOURCE\_POS\_WAIT\(\) 作为回退。

**「影响」** 对采用读写分离的应用，关键改动是把主库返回的 LSN 随请求传递，并在备库读取前执行等待；超时不是强制的，但一旦设置，备库落后超过阈值就会让该查询报错，应用需要显式处理这种延迟失败。

**标签**: `#PostgreSQL`, `#databases`, `#open source`, `#release`, `#replication consistency`

---

<a id="item-tech-news-2"></a>
### [ChatPRD 因 token 欺诈与转售滥用逐步停掉免费试用](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 6.0/10

Simon Willison 在博客中引述 ChatPRD 创始人 Claire Vo 的说法：这个面向产品经理、用于把想法转成规格说明的 AI 平台，正遭遇大量免费试用滥用和 token 欺诈。滥用者反复使用免费试用和促销码，接入 ChatPRD 的 AI agent；他们有的只是为了免费用 AI，有的则转售 token，甚至把 agent 用作商业生产工具——其中一例被描述为替一个国际 Roblox 和 Fortnite 地图工作室持续生成地图。Claire 还提到，agent 中常见“骑自行车的鹈鹕”SVG 提示，Simon 推测这与识别底层模型家族有关。她因此正在全面停掉免费试用。

rss · Simon Willison · 11月20日 02:49

**「试用额度与 token 成本」** ChatPRD 是 Claire Vo 面向产品经理运营的 AI 平台，主打把想法转成需求文档，并提供免费试用。免费试用让用户可以调用 ChatPRD 的 agent；一旦试用资格可被批量获取，滥用者就能把平台的模型调用变成免费 AI 用量，或转售访问权、让 agent 持续执行商业任务。Claire 提到的转售促销码、用中继封装服务，以及安装自定义 MCP 让 agent 24 小时运行，都是这种模式的具体表现。

**「影响」** 对 ChatPRD 的潜在用户来说，最直接的变化是免费试用将不再可用；对运营同类 AI agent 产品的团队，这起案例表明，按 token 计费的试用额度可能被反复注册、促销码和转售链条消耗，试用设计需要把滥用检测和额度限制纳入成本模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=ZDpP7JXPlhc">How I fight token fraud as an AI founder - YouTube</a></li>

</ul>
</details>

**标签**: `#AI token fraud`, `#free-trial abuse`, `#LLM agents`, `#AI product economics`, `#ChatPRD`

---
