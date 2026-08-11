---
title: "Mac 之 git mergetool的安装使用"
date: "2025-07-03 11:58:29"
slug: "mac-zhi-git-mergetool-de-an-zhuang-shi-yong"
categories: ["技术"]
tags: ["MacOS", "Git"]
aliases:
  - "/2025/07/03/Mac-之-git-mergetool的安装使用/"
  - "/2025/07/03/Mac-之-git-mergetool的安装使用.html"
  - "/Mac-之-git-mergetool的安装使用/"
  - "/Mac-之-git-mergetool的安装使用.html"
  - "/2025/07/03/mac-zhi-git-mergetool-de-an-zhuang-shi-yong/"
  - "/2025/07/03/mac-zhi-git-mergetool-de-an-zhuang-shi-yong.html"
  - "/mac-zhi-git-mergetool-de-an-zhuang-shi-yong.html"
---
git mergetool 工具安装

```bash
brew install meld 或 brew install homebrew/gui/meld
git config --global merge.tool meld
git mergetool
```

