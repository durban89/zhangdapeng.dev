---
title: "修改Sublime Text 3 的侧边栏字体大小,字体类型"
date: "2025-07-01 11:36:02"
slug: "xiu-gai-sublime-text-3-de-ce-bian-lan-zi-ti-da-xiao-zi-ti-lei-xing"
categories: ["技术"]
tags: ["Sublime"]
aliases:
  - "/2025/07/01/修改Sublime-Text-3-的侧边栏字体大小,字体类型/"
  - "/2025/07/01/修改Sublime-Text-3-的侧边栏字体大小,字体类型.html"
  - "/修改Sublime-Text-3-的侧边栏字体大小,字体类型/"
  - "/修改Sublime-Text-3-的侧边栏字体大小,字体类型.html"
  - "/2025/07/01/修改Sublime-Text-3-的侧边栏字体大小-字体类型/"
  - "/2025/07/01/修改Sublime-Text-3-的侧边栏字体大小-字体类型.html"
  - "/2025/07/01/xiu-gai-sublime-text-3-de-ce-bian-lan-zi-ti-da-xiao-zi-ti-lei-xing/"
  - "/2025/07/01/xiu-gai-sublime-text-3-de-ce-bian-lan-zi-ti-da-xiao-zi-ti-lei-xing.html"
  - "/xiu-gai-sublime-text-3-de-ce-bian-lan-zi-ti-da-xiao-zi-ti-lei-xing.html"
---
**一.修改字体大小**

安装PackageResourceViewer

使用PackageResourceViewer打开Theme文件进行编辑

快捷键 `⌘(command)+⇧(shift)+P` 打开 Command Palette 输入 `PackageResourceViewer: Open Resource` 回车，

打开包列表 选择 `Theme - Default`，

再选择 Default.sublimt-theme [这里有可能是你自己目前安装正在使用的一个主题,如果不能用的话,可以自己更换一个试试]

搜索` sidebar_label`，在 `"class": "sidebar_label"` 后边加一行：`"font.size": 18`，将字体大小设置为18，保存.

**二.修改字体类型**

进行第一步操作后,在`sidebar_label`后面加入一行:`"font.face":"Courier New"`,这里的字体可以是你自己系统里面自带的.


