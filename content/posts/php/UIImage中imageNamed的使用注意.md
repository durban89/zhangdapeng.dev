---
title: "UIImage中imageNamed的使用注意"
date: "2025-06-13 10:13:15"
slug: "uiimage-zhong-imagenamed-de-shi-yong-zhu-yi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/UIImage中imageNamed的使用注意/"
  - "/2025/06/13/UIImage中imageNamed的使用注意.html"
  - "/UIImage中imageNamed的使用注意/"
  - "/UIImage中imageNamed的使用注意.html"
  - "/2025/06/13/uiimage-zhong-imagenamed-de-shi-yong-zhu-yi/"
  - "/2025/06/13/uiimage-zhong-imagenamed-de-shi-yong-zhu-yi.html"
  - "/uiimage-zhong-imagenamed-de-shi-yong-zhu-yi.html"
---
最近查找了关于这个imageNamed的使用方法说明：有几篇文章是这样说的

第一篇文章：http://hi.baidu.com/dongliqian/item/f9a60bdee1dad84fdcf9be6e

在这篇文章里面提到，`[UIImage imageNamed: @""]` 多次操作之后，应用经常发生内存警告从而导致自动退出的问题，由此看来[UIImage imageNamed:]只适合与UI界面中小的贴图的读取，而一些比较大的资源文件应该尽量避免使用这个接口。

第二篇文章里面是这样说的：http://www.cocoachina.com/bbs/simple/?t27420.html

里面提到“这种方法在application bundle的顶层文件夹寻找由供应的名字的图象 。 如果找到图片，装载到iPhone系统缓存图象。那意味图片是(理论上)放在内存里作为cache的。”

综合以上我觉得，使用这个方法还是需要注意的，建议使用下面这总方法:

```objectivec
NSString *path = [[NSBundle mainBundle] pathForResource:@"search" ofType:@"png"];
UIImage *image = [UIImage imageWithContentsOfFile:path];
```
