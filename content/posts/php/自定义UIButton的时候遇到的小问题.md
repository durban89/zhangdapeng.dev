---
title: "自定义UIButton的时候遇到的小问题"
date: "2025-06-13 11:35:03"
slug: "zi-ding-yi-uibutton-de-shi-hou-yu-dao-de-xiao-wen-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/自定义UIButton的时候遇到的小问题/"
  - "/2025/06/13/自定义UIButton的时候遇到的小问题.html"
  - "/自定义UIButton的时候遇到的小问题/"
  - "/自定义UIButton的时候遇到的小问题.html"
  - "/2025/06/13/zi-ding-yi-uibutton-de-shi-hou-yu-dao-de-xiao-wen-ti/"
  - "/2025/06/13/zi-ding-yi-uibutton-de-shi-hou-yu-dao-de-xiao-wen-ti.html"
  - "/zi-ding-yi-uibutton-de-shi-hou-yu-dao-de-xiao-wen-ti.html"
---
出现问题的代码如下：

```objectivec
//选择按钮
UIButton *performerButton = [UIButton buttonWithType:UIButtonTypeCustom];
[performerButton setFrame:CGRectMake(tip.frame.size.width+10.0, y+11.0, 35.0, 25.0)];
[performerButton addTarget:self
                    action:@selector(setTeleplayType:)
          forControlEvents:UIControlEventTouchUpInside];
[self.scrollView addSubview:performerButton];
[performerButton setTitle:@"演员" forState:UIControlStateNormal];
[performerButton setTitleColor:[UIColor redColor] forState:UIControlStateNormal];
```

结果是看不到你添加的标题。

问题的关键是如何解决的，呵呵，蠢死我了，其实就是自己设计的button的宽度太小了，没有将字体显示出来.

结果的代码如下修改就好：

```objectivec
//选择按钮
UIButton *performerButton = [UIButton buttonWithType:UIButtonTypeCustom];
[performerButton setFrame:CGRectMake(tip.frame.size.width+10.0, y+11.0, 45.0, 25.0)];
[performerButton addTarget:self
                    action:@selector(setTeleplayType:)
          forControlEvents:UIControlEventTouchUpInside];
[self.scrollView addSubview:performerButton];
[performerButton setTitle:@"演员" forState:UIControlStateNormal];
[performerButton setTitleColor:[UIColor redColor] forState:UIControlStateNormal];
```
