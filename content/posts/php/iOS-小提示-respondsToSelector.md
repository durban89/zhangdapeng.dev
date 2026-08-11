---
title: "iOS 小提示 respondsToSelector"
date: "2025-06-11 10:44:01"
slug: "ios-xiao-ti-shi-respondstoselector"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-小提示-respondsToSelector/"
  - "/2025/06/11/iOS-小提示-respondsToSelector.html"
  - "/iOS-小提示-respondsToSelector/"
  - "/iOS-小提示-respondsToSelector.html"
  - "/2025/06/11/ios-xiao-ti-shi-respondstoselector/"
  - "/2025/06/11/ios-xiao-ti-shi-respondstoselector.html"
  - "/ios-xiao-ti-shi-respondstoselector.html"
---
respondsToSelector的大概方法如下：

```objectivec
if ([NSArray respondsToSelector:@selector(arrayWithObjects:)]){
}
```

就是NSArray是否会执行arrayWithObjects:方法，一般在执行代理函数之前先这样respondsToSelector检测一下。
