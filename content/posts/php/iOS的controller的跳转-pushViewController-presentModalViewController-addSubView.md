---
title: "iOS的controller的跳转 pushViewController/presentModalViewController/addSubView"
date: "2025-06-09 11:27:58"
slug: "ios-de-controller-de-tiao-zhuan-pushviewcontrollerpresentmodalviewcontrolleraddsubview"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/09/iOS的controller的跳转-pushViewController/presentModalViewController/addSubView/"
  - "/2025/06/09/iOS的controller的跳转-pushViewController/presentModalViewController/addSubView.html"
  - "/iOS的controller的跳转-pushViewController/presentModalViewController/addSubView/"
  - "/iOS的controller的跳转-pushViewController/presentModalViewController/addSubView.html"
  - "/2025/06/09/iOS的controller的跳转-pushViewController-presentModalViewController-addSubView/"
  - "/2025/06/09/iOS的controller的跳转-pushViewController-presentModalViewController-addSubView.html"
  - "/2025/06/09/ios-de-controller-de-tiao-zhuan-pushviewcontrollerpresentmodalviewcontrolleraddsubview/"
  - "/2025/06/09/ios-de-controller-de-tiao-zhuan-pushviewcontrollerpresentmodalviewcontrolleraddsubv.html"
  - "/ios-de-controller-de-tiao-zhuan-pushviewcontrollerpresentmodalviewcontrolleraddsubview.html"
---
1. 用UINavigationController的时候用pushViewController:animated（在调用的函数里面添加如下类似代码）
```c
teleplayViewController *teleplay = [[teleplayViewController alloc] init];
[self.navigationController pushViewController:teleplay animated:YES];
```

2. 其他时候用presentModalViewController:animated（在调用的函数里面添加如下类似代码）
```c
[self presentModalViewController:controller animated:YES];
```
同时不要忘记在另一个视图中调用函数dismissViewControllerAnimated（代码类似如下）

```c
[self dismissViewControllerAnimated:YES completion:NULL];
```

3. 切换视图一般用不到addSubview

UINavigationController是导航控制器，如果pushViewController的话，会跳转到下一个ViewController，点返回会回到现在这个ViewController；

如果是addSubview的话，其实还是对当前的ViewController操作，只是在当前视图上面又“盖”住了一层视图，其实原来的画面在下面呢，看不到而已。（当然，也可以用insertSubView atIndex那个方法设置放置的层次)
