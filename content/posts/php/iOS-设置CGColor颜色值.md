---
title: "iOS 设置CGColor颜色值"
date: "2025-06-12 09:35:00"
slug: "ios-she-zhi-cgcolor-yan-se-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-设置CGColor颜色值/"
  - "/2025/06/12/iOS-设置CGColor颜色值.html"
  - "/iOS-设置CGColor颜色值/"
  - "/iOS-设置CGColor颜色值.html"
  - "/2025/06/12/ios-she-zhi-cgcolor-yan-se-zhi/"
  - "/2025/06/12/ios-she-zhi-cgcolor-yan-se-zhi.html"
  - "/ios-she-zhi-cgcolor-yan-se-zhi.html"
---
通过Core Library的文档，我们知道创建颜色有这么几个方法：  
- CGColorCreate  
- CGColorCreateCopy  
- CGColorCreateGenericGray  
- CGColorCreateGenericRGB  
- CGColorCreateGenericCMYK  
- CGColorCreateCopyWithAlpha  
- CGColorCreateWithPattern  

再来看一下CGColorCreate：  

```objectivec
CGColorRef CGColorCreate (  
  CGColorSpaceRef colorspace,  
  const CGFloat components[]  
);
```

我们通过CGColorCreate就可以创建颜色。既然我们要用RGB表示颜色，那么colorspace这个参数我们就可以使用CGColorSpaceCreateDeviceRGB()，而我们主要来探讨components这个参数。  
这个参数是一个数组，带有4个数值：  

float color[]={红色分量, 绿色分量, 蓝色分量, alpha分量};

这4个数值都是0-1区间，0表示黑（不发光），数字越大这种颜色的光线越强，alpha分量表示透明度。比如{1.0, 0, 0,1.0}就是纯红色而且完全不透明。

最终的使用方法，如下代码：

```objectivec
[UIColor colorWithRed:55.0/255.0 green:137.0/255.0 blue:195.0/255.0 alpha:1.0];
```

里面的值（55.0,137.0,195.0）可以自己选择,我是通过使用photoshop自己选择的，你也可以试试
