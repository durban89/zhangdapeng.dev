---
title: "iOS UIButton 做圆角效果"
date: "2025-06-12 09:34:57"
slug: "ios-uibutton-zuo-yuan-jiao-xiao-guo"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-UIButton-做圆角效果/"
  - "/2025/06/12/iOS-UIButton-做圆角效果.html"
  - "/iOS-UIButton-做圆角效果/"
  - "/iOS-UIButton-做圆角效果.html"
  - "/2025/06/12/ios-uibutton-zuo-yuan-jiao-xiao-guo/"
  - "/2025/06/12/ios-uibutton-zuo-yuan-jiao-xiao-guo.html"
  - "/ios-uibutton-zuo-yuan-jiao-xiao-guo.html"
---
首先引入文件：**#import <QuartzCore/QuartzCore.h>**

再次执行类似下面的代码：

```objectivec
UIButton *moreButton = [UIButton buttonWithType:UIButtonTypeCustom];
moreButton.frame = CGRectMake(1.0f, 1.0f, cell.contentView.frame.size.width-2, cell.contentView.frame.size.height-2);
[moreButton.layer setMasksToBounds:YES];
[moreButton.layer setCornerRadius:10.0]; //设置矩形四个圆角半径
[moreButton.layer setBorderWidth:1.0]; //边框宽度
moreButton.backgroundColor = [UIColor clearColor];
```
