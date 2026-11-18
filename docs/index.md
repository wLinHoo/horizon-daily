---
layout: default
title: Horizon 中文日报
---

[订阅中文日报]({{ '/feed-zh.xml' | relative_url }})

## 日报归档

<ul>
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% for post in zh_posts %}
    <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
  {% else %}
    <li>暂无日报</li>
  {% endfor %}
</ul>
