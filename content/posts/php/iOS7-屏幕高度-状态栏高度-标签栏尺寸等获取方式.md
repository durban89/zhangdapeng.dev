---
title: "iOS7 屏幕高度，状态栏高度，标签栏尺寸等获取方式"
date: "2025-06-25 11:35:04"
slug: "ios7-ping-mu-gao-du-zhuang-tai-lan-gao-du-biao-qian-lan-chi-cun-deng-huo-qu-fang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS7-屏幕高度，状态栏高度，标签栏尺寸等获取方式/"
  - "/2025/06/25/iOS7-屏幕高度，状态栏高度，标签栏尺寸等获取方式.html"
  - "/iOS7-屏幕高度，状态栏高度，标签栏尺寸等获取方式/"
  - "/iOS7-屏幕高度，状态栏高度，标签栏尺寸等获取方式.html"
  - "/2025/06/25/iOS7-屏幕高度-状态栏高度-标签栏尺寸等获取方式/"
  - "/2025/06/25/iOS7-屏幕高度-状态栏高度-标签栏尺寸等获取方式.html"
  - "/2025/06/25/ios7-ping-mu-gao-du-zhuang-tai-lan-gao-du-biao-qian-lan-chi-cun-deng-huo-qu-fang-shi/"
  - "/2025/06/25/ios7-ping-mu-gao-du-zhuang-tai-lan-gao-du-biao-qian-lan-chi-cun-deng-huo-qu-fang-sh.html"
  - "/ios7-ping-mu-gao-du-zhuang-tai-lan-gao-du-biao-qian-lan-chi-cun-deng-huo-qu-fang-shi.html"
---
关于新的获取屏幕高度，状态栏尺寸，标签栏尺寸的获取方法，找了多个资料和文章，其方法总结如下

### [App尺寸，去掉状态栏](#1)

```objectivec
CGRect r = [ UIScreen mainScreen ].applicationFrame;
NSLog(@"r.height = %f,r.width = %f,r.x = %f,r.y = %f",r.size.height,r.size.width,r.origin.x,r.origin.y);
```

gowhich得到的结果如下：

```bash
2013-11-28 12:09:22.188 寻艺[49308:70b] r.height = 548.000000,r.width = 320.000000,r.x = 0.000000,r.y = 20.000000
```

### [屏幕尺寸](#2)

```objectivec
CGRect rx = [UIScreen mainScreen].bounds;
NSLog(@"rx.height = %f,rx.width = %f,rx.x = %f,rx.y = %f",rx.size.height,rx.size.width,rx.origin.x,rx.origin.y);
```

得到的结果如下：

```bash
2013-11-28 12:09:22.189 寻艺[49308:70b] rx.height = 568.000000,rx.width = 320.000000,rx.x = 0.000000,rx.y = 0.000000
```

### [状态栏尺寸](#3)

```objectivec
CGRect rect  = [[UIApplication sharedApplication] statusBarFrame];
NSLog(@"rect.height = %f,rect.width = %f,rect.x = %f,rect.y = %f",rect.size.height,rect.size.width,rect.origin.x,rect.origin.y);
```

得到的结果如下：

```bash
2013-11-28 12:14:18.972 寻艺[49617:70b] rect.height = 20.000000,rect.width = 320.000000,rect.x = 0.000000,rect.y = 0.000000
```

### [iPhone中获取屏幕分辨率的方法](#4)

```objectivec
CGRect rect = [[UIScreen mainScreen] bounds];

CGSize size = rect.size;

CGFloat width = size.width;

CGFloat height = size.height;
```

另外，设计UI的时候，注意用户最小的触控面积。有2种说法

`44*44` 好像是来自sdk

`64*64` 来自standford讲义

参考文章:

http://blog.csdn.net/linzhiji/article/details/6764738

