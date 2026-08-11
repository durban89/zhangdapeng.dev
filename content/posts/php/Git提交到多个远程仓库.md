---
title: "Git提交到多个远程仓库"
date: "2025-06-30 15:57:23"
slug: "git-ti-jiao-dao-duo-ge-yuan-cheng-cang-ku"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/06/30/Git提交到多个远程仓库/"
  - "/2025/06/30/Git提交到多个远程仓库.html"
  - "/Git提交到多个远程仓库/"
  - "/Git提交到多个远程仓库.html"
  - "/2025/06/30/git-ti-jiao-dao-duo-ge-yuan-cheng-cang-ku/"
  - "/2025/06/30/git-ti-jiao-dao-duo-ge-yuan-cheng-cang-ku.html"
  - "/git-ti-jiao-dao-duo-ge-yuan-cheng-cang-ku.html"
---
第一步:添加远程仓库

```bash
git remote add origin 第一个仓库地址 //origin只是个别名哦
git remote add osc 第二个仓库地址 //osc也是个别名哦
```

第二步：

创建分支

```bash
git checkout -b master
git checkout -b osc
```

第三步：

提交代码：

分别切换分支提交

```bash
git chekcout master
git push origin master
//=========================
git checkout osc
git push osc master
```


