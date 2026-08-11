---
title: "iOS7 CGRectInset 该结构体的应用"
date: "2025-06-27 10:07:07"
slug: "ios7-cgrectinset-gai-jie-gou-ti-de-ying-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-CGRectInset-该结构体的应用/"
  - "/2025/06/27/iOS7-CGRectInset-该结构体的应用.html"
  - "/iOS7-CGRectInset-该结构体的应用/"
  - "/iOS7-CGRectInset-该结构体的应用.html"
  - "/2025/06/27/ios7-cgrectinset-gai-jie-gou-ti-de-ying-yong/"
  - "/2025/06/27/ios7-cgrectinset-gai-jie-gou-ti-de-ying-yong.html"
  - "/ios7-cgrectinset-gai-jie-gou-ti-de-ying-yong.html"
---
```objectivec
CGRect CGRectInset (
    CGRect rect,
    CGFloat dx,
    CGFloat dy
);
```

该结构体的应用是以原rect为中心，再参考dx，dy，进行缩放或者放大。

我们做一个示例来看看是不是这样的：

代码如下：

```objectivec
-(void) viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
    
    UIGraphicsBeginImageContext(self.view.bounds.size);
    CGContextRef context = UIGraphicsGetCurrentContext();
    CGRect currentRect = self.view.frame;
    CGContextAddRect(context, currentRect);
    CGContextDrawPath(context, kCGPathFillStroke);
    CGRect original = CGRectMake(100, 100, 200, 200);
    CGContextSetFillColorWithColor(context, [UIColor redColor].CGColor);
    CGContextAddRect(context, original);
    CGContextDrawPath(context, kCGPathFillStroke);
    
    CGRect firstRect = CGRectInset(original, 10, 10);
    CGContextSetFillColorWithColor(context, [UIColor blueColor].CGColor);
    CGContextAddRect(context, firstRect);
    CGContextDrawPath(context, kCGPathFillStroke);
    
    CGRect secondRect = CGRectInset(firstRect, 10, 10);
    CGContextSetFillColorWithColor(context, [UIColor greenColor].CGColor);
    CGContextAddRect(context, secondRect);
    CGContextDrawPath(context, kCGPathFillStroke);
    
    CGRect thirdRect = CGRectInset(secondRect, 10, 10);
    CGContextSetFillColorWithColor(context, [UIColor yellowColor].CGColor);
    CGContextAddRect(context, thirdRect);
    CGContextDrawPath(context, kCGPathFillStroke);
    
    CGRect fourRect = CGRectInset(thirdRect, 10, 10);
    CGContextSetFillColorWithColor(context, [UIColor grayColor].CGColor);
    CGContextAddRect(context, fourRect);
    
    
    UIImage *destImg = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    UIImageView *imgView = [[UIImageView alloc] initWithImage:destImg];
    [self.view addSubview:imgView];
}
```

从这个示例可以看出其使用方法是如何使用的。

