---
title: "在popViewControllerAnimated后调用函数"
date: "2025-06-12 11:49:38"
slug: "zai-popviewcontrolleranimated-hou-diao-yong-han-shu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/在popViewControllerAnimated后调用函数/"
  - "/2025/06/12/在popViewControllerAnimated后调用函数.html"
  - "/在popViewControllerAnimated后调用函数/"
  - "/在popViewControllerAnimated后调用函数.html"
  - "/2025/06/12/zai-popviewcontrolleranimated-hou-diao-yong-han-shu/"
  - "/2025/06/12/zai-popviewcontrolleranimated-hou-diao-yong-han-shu.html"
  - "/zai-popviewcontrolleranimated-hou-diao-yong-han-shu.html"
---
当你在A视图调用pushViewController:animated:，并且从B视图返回A视图的时候需要做一些操作，比如刷新数据，或者做个浏览记录的操作的时候，可以调用这个函数viewWillAppear，就可以解决问题了。

在我的实例中，我在A视图做了这个操作：

```objectivec
self.navigationController.navigationBarHidden = YES;
```

但是在B视图我要做相反的操作

```objectivec
self.navigationController.navigationBarHidden = NO;
```

但是在返回来的时候，问题出现了，A视图达不到我想要的效果了，似乎也继承了B视图的navigationBar不隐藏的操作，但是我需要隐藏，那么结果做这个操作就好 了：

```objectivec
-(void) viewWillAppear:(BOOL)animated{
    self.navigationController.navigationBarHidden = YES;
}
```
