---
title: "Git 操作 pull 强制重写本地文件"
date: "2025-06-30 14:31:21"
slug: "git-cao-zuo-pull-qiang-zhi-zhong-xie-ben-di-wen-jian"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/06/30/Git-操作-pull-强制重写本地文件/"
  - "/2025/06/30/Git-操作-pull-强制重写本地文件.html"
  - "/Git-操作-pull-强制重写本地文件/"
  - "/Git-操作-pull-强制重写本地文件.html"
  - "/2025/06/30/git-cao-zuo-pull-qiang-zhi-zhong-xie-ben-di-wen-jian/"
  - "/2025/06/30/git-cao-zuo-pull-qiang-zhi-zhong-xie-ben-di-wen-jian.html"
  - "/git-cao-zuo-pull-qiang-zhi-zhong-xie-ben-di-wen-jian.html"
---
最近很烦恼一个问题，在不同设备上进行操作的时候，会出现两台设备都存在一个修改文件，问题是如果一台机器上代码提交了，想在另外一台机器上进行pull来更新代码，会提示你先要commit本地的修改代码，问题是如果这样的话会出现冲突，但是我又想重写，不管现在的代码更改的如何，于是想要重写本地的文件。对于不是很懂git的我，找到了一个解决的方案：

```bash
git fetch origin master
git reset --hard FETCH_HEAD
git clean -df
```

经过这样的操作，结果很令我满意。提示，如果不是很想覆盖本地的代码的话，可以思考另外一个办法。不要强制使用此方案


