---
title: "Mac下如何禁用Adobe无用自启动项"
date: "2025-07-14 14:50:49"
slug: "mac-xia-ru-he-jin-yong-adobe-wu-yong-zi-qi-dong-xiang"
categories: ["技术"]
tags: ["MacOS"]
aliases:
  - "/2025/07/14/Mac下如何禁用Adobe无用自启动项/"
  - "/2025/07/14/Mac下如何禁用Adobe无用自启动项.html"
  - "/Mac下如何禁用Adobe无用自启动项/"
  - "/Mac下如何禁用Adobe无用自启动项.html"
  - "/2025/07/14/mac-xia-ru-he-jin-yong-adobe-wu-yong-zi-qi-dong-xiang/"
  - "/2025/07/14/mac-xia-ru-he-jin-yong-adobe-wu-yong-zi-qi-dong-xiang.html"
  - "/mac-xia-ru-he-jin-yong-adobe-wu-yong-zi-qi-dong-xiang.html"
---
之前安装了一次mac版本的PS软件，之后不想用了，就直接把PS删掉了

然后就发现系统里面多了Adobe，看起来挺烦的，我又不需要，就一个一个的删除掉了

再然后每次启动后就提示我是否要修复的提示，经过查找资料也找到了解决办法

首先我们要记得以下几个路径

```bash
~/Library/LaunchAgents

/Library/LaunchAgents

/Library/LaunchDaemons

/System/Library/LaunchAgents

/System/Library/LaunchDaemons
```

然后每个都打开，检查里面是都带有adobe的，直接删掉就好了

其次、偏好设置里面也要检查下

在“扩展”中关闭Core Sync和Core Sync Helper。

最后删除CCLibrary、CCXProcess以及CoreSync文件夹

前往/Applications/Utilities/Adobe Creative Cloud，删除CCLibrary、CCXProcess以及CoreSync文件夹。

```bash
cd /Applications/Utilities/Adobe\ Creative\ Cloud
```
