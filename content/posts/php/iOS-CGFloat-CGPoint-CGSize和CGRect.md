---
title: "iOS CGFloat CGPoint CGSize和CGRect"
date: "2025-06-06 10:35:44"
slug: "ios-cgfloat-cgpoint-cgsize-he-cgrect"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS-CGFloat-CGPoint-CGSize和CGRect/"
  - "/2025/06/06/iOS-CGFloat-CGPoint-CGSize和CGRect.html"
  - "/iOS-CGFloat-CGPoint-CGSize和CGRect/"
  - "/iOS-CGFloat-CGPoint-CGSize和CGRect.html"
  - "/2025/06/06/ios-cgfloat-cgpoint-cgsize-he-cgrect/"
  - "/2025/06/06/ios-cgfloat-cgpoint-cgsize-he-cgrect.html"
  - "/ios-cgfloat-cgpoint-cgsize-he-cgrect.html"
---
CGGeometry类定义几何元素的结构和操作几何元素的函数。

### [1、数据类型：](#1)

CGFloat: 浮点值的基本类型

CGPoint: 表示一个二维坐标系中的点

CGSize: 表示一个矩形的宽度和高度

CGRect: 表示一个矩形的位置和大小

```shell
typedef float CGFloat;// 32-bit
typedef double CGFloat;// 64-bit
struct CGPoint {
    CGFloat x;
    CGFloat y;
};
typedef struct CGPoint CGPoint;
struct CGSize {
    CGFloat width;
    CGFloat height;
};
typedef struct CGSize CGSize;
struct CGRect {
    CGPoint origin;
    CGSize size;
};
typedef struct CGRect CGRect;
```

注意：CGRect数据结构的高度和宽度可以是负数。例如，一个矩形的原点是[0.0，0.0]和大小是[10.0,10.0]。这个矩形完全等同原点是[10.0，10.0]和大小是[-10.0，-10.0]的矩形。

### [2、使用值来创建几何元素的方法](#2)

```c CGPointMake、CGRectMake、CGSizeMake
CGPoint CGPointMake (
                     CGFloat x,
                     CGFloat y
                     );

CGSize CGSizeMake (
                   CGFloat width,
                   CGFloat height
                   );

CGRect CGRectMake (
                   CGFloat x,
                   CGFloat y,
                   CGFloat width,
                   CGFloat height
                   );

CGFloat ten=10.0f;
CGPoint point = CGPointMake(0.0f, 0.0f);
CGSize size = CGSizeMake(10.0f, 10.0f);
CGRect rect = CGRectMake(point.x, point.y, size.width, size.height);
NSLog(@"ten: %f", ten);
NSLog(@"point: %@", NSStringFromCGPoint(point));
NSLog(@"size: %@", NSStringFromCGSize(size));
NSLog(@"rect: %@", NSStringFromCGRect(rect));
```
