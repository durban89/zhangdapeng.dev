---
title: "iOS 状态栏的尺寸"
date: "2025-06-11 11:06:58"
slug: "ios-zhuang-tai-lan-de-chi-cun"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-状态栏的尺寸/"
  - "/2025/06/11/iOS-状态栏的尺寸.html"
  - "/iOS-状态栏的尺寸/"
  - "/iOS-状态栏的尺寸.html"
  - "/2025/06/11/ios-zhuang-tai-lan-de-chi-cun/"
  - "/2025/06/11/ios-zhuang-tai-lan-de-chi-cun.html"
  - "/ios-zhuang-tai-lan-de-chi-cun.html"
---
状态栏尺寸的获取方式：

```objectivec
CGRect statusFrame;
statusFrame = [[UIApplication sharedApplication] statusBarFrame];
CGFloat statusHeight = statusFrame.size.height;
CGFloat statusWidth = statusFrame.size.width;
```
