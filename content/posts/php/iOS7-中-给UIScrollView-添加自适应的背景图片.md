---
title: "iOS7 中 给UIScrollView 添加自适应的背景图片"
date: "2025-06-26 11:15:38"
slug: "ios7-zhong-gei-uiscrollview-tian-jia-zi-shi-ying-de-bei-jing-tu-pian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-中-给UIScrollView-添加自适应的背景图片/"
  - "/2025/06/26/iOS7-中-给UIScrollView-添加自适应的背景图片.html"
  - "/iOS7-中-给UIScrollView-添加自适应的背景图片/"
  - "/iOS7-中-给UIScrollView-添加自适应的背景图片.html"
  - "/2025/06/26/ios7-zhong-gei-uiscrollview-tian-jia-zi-shi-ying-de-bei-jing-tu-pian/"
  - "/2025/06/26/ios7-zhong-gei-uiscrollview-tian-jia-zi-shi-ying-de-bei-jing-tu-pian.html"
  - "/ios7-zhong-gei-uiscrollview-tian-jia-zi-shi-ying-de-bei-jing-tu-pian.html"
---
要做一个长的能滚动的页面，在IOS7中这个能滚动的话，可以使用UIScrollView，然后使用背景图片来解决我们大部分的ui问题，可以节省我们写ui的时间。

下面来看看代码

```objectivec
UIScrollView *scrollView=[[UIScrollView alloc] initWithFrame:CGRectMake(0, 0,320, 1000)];
scrollView.backgroundColor = [UIColor colorWithPatternImage:[UIImageimageNamed:@"detail.png"]];
[scrollView setContentSize:CGSizeMake(320, 960)];
[self.view addSubview:scrollView];
```

实现很简单，下面你就可以自己去添加一些其他的view到上面去了，嘿嘿

