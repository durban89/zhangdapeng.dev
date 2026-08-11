---
title: "在iOS上用Quartz绘制圆角矩形"
date: "2025-06-23 15:48:54"
slug: "zai-ios-shang-yong-quartz-hui-zhi-yuan-jiao-ju-xing"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/在iOS上用Quartz绘制圆角矩形/"
  - "/2025/06/23/在iOS上用Quartz绘制圆角矩形.html"
  - "/在iOS上用Quartz绘制圆角矩形/"
  - "/在iOS上用Quartz绘制圆角矩形.html"
  - "/2025/06/23/zai-ios-shang-yong-quartz-hui-zhi-yuan-jiao-ju-xing/"
  - "/2025/06/23/zai-ios-shang-yong-quartz-hui-zhi-yuan-jiao-ju-xing.html"
  - "/zai-ios-shang-yong-quartz-hui-zhi-yuan-jiao-ju-xing.html"
---
Bezels是Mac OS X下，苹果私有的UI控件，用来提示用户某些信息。不过iOS下，就有很多第三方的Bezels风格的提示控件实现了。相信大家也见过很多了。下图左侧是OSX的提示音量变化的Bezels，右侧是iOS上的Bezels风格的进度提示。

在iOS上做Bezels的思路很简单，无非就是在UIView里绘制一个半透明的圆角矩形，然后加入其他的SubView。因为没有现成的绘制圆角矩形的API可用，所以我们来自己绘制一个——反正是为了学习嘛。

新建项目，添加一个UIView的子类，修改drawRect方法，如下：

```objectivec
- (void)drawRect:(CGRect)rect
{
    CGFloat width = rect.size.width;
    CGFloat height = rect.size.height;
    // 简便起见，这里把圆角半径设置为长和宽平均值的1/10
    CGFloat radius = (width + height) * 0.05;

    // 获取CGContext，注意UIKit里用的是一个专门的函数
    CGContextRef context = UIGraphicsGetCurrentContext();
    // 移动到初始点
    CGContextMoveToPoint(context, radius, 0);

    // 绘制第1条线和第1个1/4圆弧
    CGContextAddLineToPoint(context, width - radius, 0);
    CGContextAddArc(context, width - radius, radius, radius, -0.5 * M_PI, 0.0, 0);

    // 绘制第2条线和第2个1/4圆弧
    CGContextAddLineToPoint(context, width, height - radius);
    CGContextAddArc(context, width - radius, height - radius, radius, 0.0, 0.5 * M_PI, 0);

    // 绘制第3条线和第3个1/4圆弧
    CGContextAddLineToPoint(context, radius, height);
    CGContextAddArc(context, radius, height - radius, radius, 0.5 * M_PI, M_PI, 0);

    // 绘制第4条线和第4个1/4圆弧
    CGContextAddLineToPoint(context, 0, radius);
    CGContextAddArc(context, radius, radius, radius, M_PI, 1.5 * M_PI, 0);

    // 闭合路径
    CGContextClosePath(context);
    // 填充半透明黑色
    CGContextSetRGBFillColor(context, 0.0, 0.0, 0.0, 0.5);
    CGContextDrawPath(context, kCGPathFill);
}
```

其实这用到的只是些很基本的Quartz绘图函数而已。不过，我们顺利的绘制出了半透明，黑色的，圆角Bezel风格的View

