---
title: "分段控件UISegmentedControl"
date: "2025-06-17 17:20:52"
slug: "fen-duan-kong-jian-uisegmentedcontrol"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/分段控件UISegmentedControl/"
  - "/2025/06/17/分段控件UISegmentedControl.html"
  - "/分段控件UISegmentedControl/"
  - "/分段控件UISegmentedControl.html"
  - "/2025/06/17/fen-duan-kong-jian-uisegmentedcontrol/"
  - "/2025/06/17/fen-duan-kong-jian-uisegmentedcontrol.html"
  - "/fen-duan-kong-jian-uisegmentedcontrol.html"
---
最近刚刚接触到这个东西，感觉好神奇一样，就试着用了一下，哈哈，果然还不错：

代码如下，很简单的例子，不寒有任何的杂质

```objectivec
NSArray *item = [[NSArray alloc] initWithObjects:@"男",@"女", nil];

UISegmentedControl *sexSegment = [[UISegmentedControl alloc] initWithItems:item];
sexSegment.segmentedControlStyle = UISegmentedControlStyleBar;
[sexSegment setSegmentedControlStyle:UISegmentedControlStylePlain];
[sexSegment setFrame:CGRectMake(segmentX, segmentY, segmentWidth, segmentHeight)];
[sexSegment addTarget:self
               action:@selector(selectSex:)
     forControlEvents:UIControlEventValueChanged];

[_contentView addSubview:sexSegment];
```
