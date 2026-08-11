---
title: "Git 之 用socks5加速git clone"
date: "2025-07-03 16:50:08"
slug: "git-zhi-yong-socks5-jia-su-git-clone"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/03/Git-之-用socks5加速git-clone/"
  - "/2025/07/03/Git-之-用socks5加速git-clone.html"
  - "/Git-之-用socks5加速git-clone/"
  - "/Git-之-用socks5加速git-clone.html"
  - "/2025/07/03/git-zhi-yong-socks5-jia-su-git-clone/"
  - "/2025/07/03/git-zhi-yong-socks5-jia-su-git-clone.html"
  - "/git-zhi-yong-socks5-jia-su-git-clone.html"
---
需要使用github，但是国内访问很慢，往往会发生connection refused的事情发生，那就自己去弄个vpn吧。前提不要做扰乱国家安稳的事情

下面记录下git的配置方法

```bash
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```
