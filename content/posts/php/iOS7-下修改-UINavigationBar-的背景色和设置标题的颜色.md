---
title: "iOS7 下修改 UINavigationBar 的背景色和设置标题的颜色"
date: "2025-06-25 11:34:55"
slug: "ios7-xia-xiu-gai-uinavigationbar-de-bei-jing-se-he-she-zhi-biao-ti-de-yan-se"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS7-下修改-UINavigationBar-的背景色和设置标题的颜色/"
  - "/2025/06/25/iOS7-下修改-UINavigationBar-的背景色和设置标题的颜色.html"
  - "/iOS7-下修改-UINavigationBar-的背景色和设置标题的颜色/"
  - "/iOS7-下修改-UINavigationBar-的背景色和设置标题的颜色.html"
  - "/2025/06/25/ios7-xia-xiu-gai-uinavigationbar-de-bei-jing-se-he-she-zhi-biao-ti-de-yan-se/"
  - "/2025/06/25/ios7-xia-xiu-gai-uinavigationbar-de-bei-jing-se-he-she-zhi-biao-ti-de-yan-se.html"
  - "/ios7-xia-xiu-gai-uinavigationbar-de-bei-jing-se-he-she-zhi-biao-ti-de-yan-se.html"
---
关于修改 UINavigationBar 的背景色和设置标题的颜色，至于以前是如何设置的我到现在已经忘的差不多了，因为总是在不同的平台和语言之间进行切换，偶尔某个会耽搁时间比较久，反正之前的iOS7之前是不是这样设置的，到时候后来的结果出现了问题。

下面简单的介绍下再iOS7下是如何进行设置的

```objectivec
//导航条背景色
NSString *navBackgroundBarImage = [[NSBundle mainBundle] pathForResource:@"bg_head"
																  ofType:@"png"];
[self.navigationController.navigationBar setBackgroundImage:[UIImage imageWithContentsOfFile:navBackgroundBarImage] forBarMetrics:UIBarMetricsDefault];

//字体大小、颜色
NSDictionary *attributes = [NSDictionary dictionaryWithObjectsAndKeys:
							[UIColor whiteColor],
							NSForegroundColorAttributeName, nil];
[self.navigationController.navigationBar setTitleTextAttributes:attributes];
```

将这几行代码添加到`-(void) viewDidLoad;`方法中，顺便将图片改为自己想要的图片，就会有结果了。自己试试看看

