---
title: "Git拉取远程分支到本地"
date: "2025-07-02 15:39:59"
slug: "git-la-qu-yuan-cheng-fen-zhi-dao-ben-di"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/02/Git拉取远程分支到本地/"
  - "/2025/07/02/Git拉取远程分支到本地.html"
  - "/Git拉取远程分支到本地/"
  - "/Git拉取远程分支到本地.html"
  - "/2025/07/02/git-la-qu-yuan-cheng-fen-zhi-dao-ben-di/"
  - "/2025/07/02/git-la-qu-yuan-cheng-fen-zhi-dao-ben-di.html"
  - "/git-la-qu-yuan-cheng-fen-zhi-dao-ben-di.html"
---
前提是远程仓库已经存在某个分支，本地并没有对应的分支【这是情景描述前提】

对应的标题操作很简单，方法如下：

```bash
git fetch origin remote_branch:local_branch
```


