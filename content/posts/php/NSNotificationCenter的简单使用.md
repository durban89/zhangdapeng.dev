---
title: "NSNotificationCenter的简单使用"
date: "2025-06-18 11:28:09"
slug: "nsnotificationcenter-de-jian-dan-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/18/NSNotificationCenter的简单使用/"
  - "/2025/06/18/NSNotificationCenter的简单使用.html"
  - "/NSNotificationCenter的简单使用/"
  - "/NSNotificationCenter的简单使用.html"
  - "/2025/06/18/nsnotificationcenter-de-jian-dan-shi-yong/"
  - "/2025/06/18/nsnotificationcenter-de-jian-dan-shi-yong.html"
  - "/nsnotificationcenter-de-jian-dan-shi-yong.html"
---
关于NSNotificationCenter，跟我前面那篇文章是一样的，一直想使用这个，基于种种原因，一直没去涉及，最近因为新浪微博的登录，so，用到了，就简单记录一下吧。

第一步：简单的写个方法

```objectivec
- (void)addObservers
{
    [[NSNotificationCenter defaultCenter] addObserver:self
    selector:@selector(deviceOrientationDidChange:)
    name:@"UIDeviceOrientationDidChangeNotification" 
    object:nil];
}

- (void)removeObservers{
    [[NSNotificationCenter defaultCenter] removeObserver:self
    name:@"UIDeviceOrientationDidChangeNotification" 
    object:nil];
}
```

是这样的，添加一个通知，然后去调用方法

这个方法是做什么的呢

```objectivec
- (void)deviceOrientationDidChange:(id)object
{
	
}
```

你想做什么都可以，因为只是一个例子，你可以抽象的超长发挥的。我没用上，知道这么用就好了先。
