---
title: "iOS CGRectMake方法"
date: "2025-06-11 10:47:23"
slug: "ios-cgrectmake-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-CGRectMake方法/"
  - "/2025/06/11/iOS-CGRectMake方法.html"
  - "/iOS-CGRectMake方法/"
  - "/iOS-CGRectMake方法.html"
  - "/2025/06/11/ios-cgrectmake-fang-fa/"
  - "/2025/06/11/ios-cgrectmake-fang-fa.html"
  - "/ios-cgrectmake-fang-fa.html"
---
代码：

```objectivec
CG_INLINE CGRect  
CGRectMake(CGFloat x, CGFloat y, CGFloat width, CGFloat height)  
{  
  CGRect rect;  
  rect.origin.x = x; rect.origin.y = y;  
  rect.size.width = width; rect.size.height = height;  
  return rect;  
}
```

这个方法就是make一个rect，定好origin（起点，左上角），宽与高，就可以画出一个位置与大小确定的rect（矩形）这个函数被声明为内联函 数，一是因为它比较小，二是因为在画界面时我们要求一定的效率。这个函数还是藏在刚刚那个头文件里面：CGGeometry.h
