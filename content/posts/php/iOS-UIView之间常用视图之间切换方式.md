---
title: "iOS UIView之间常用视图之间切换方式"
date: "2025-06-12 09:34:49"
slug: "ios-uiview-zhi-jian-chang-yong-shi-tu-zhi-jian-qie-huan-fang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-UIView之间常用视图之间切换方式/"
  - "/2025/06/12/iOS-UIView之间常用视图之间切换方式.html"
  - "/iOS-UIView之间常用视图之间切换方式/"
  - "/iOS-UIView之间常用视图之间切换方式.html"
  - "/2025/06/12/ios-uiview-zhi-jian-chang-yong-shi-tu-zhi-jian-qie-huan-fang-shi/"
  - "/2025/06/12/ios-uiview-zhi-jian-chang-yong-shi-tu-zhi-jian-qie-huan-fang-shi.html"
  - "/ios-uiview-zhi-jian-chang-yong-shi-tu-zhi-jian-qie-huan-fang-shi.html"
---
在iOS开发中，经常遇到两个View之间互相切换，列举下各种方式，但是下面每种方式都要自己灵活运用，不一定就是进入下一个、后一个必须用“一”里面的方式。

### [进入下/后一个View](#1)

A:insertSubView系列：（注意，如果你新增视图不够大，则遮不住上一层视图，即前后2个视图都存在，当然你可以做透明来查看所有，与二A对应）

- addSubview: （常用增加视图在本View上面）  
- bringSubviewToFront；将新视图放在其他同级视图的top位置  
- insertSubview:atIndex: 将新视图放在第index层，index是从底层向上数的下标位置  
- insertSubview:aboveSubview:将新视图放在第二个参数view的上面  
- insertSubview:belowSubview:将新视图放在第二个参数view的下面  
- exchangeSubviewAtIndex:withSubviewAtIndex:改变新视图从第一个位置到第二个位置

B:presentViewController系列：（常用视图切换,与二B对应）

- presentViewController:animated:completion: 弹出，出现一个新视图 可以带动画效果，完成后可以做相应的执行函数经常为nil  
- presentModalViewController:animated: 弹出，出现一个新视图 可以带动画效果

C:UINavigationController系列：（常用导航栏视图切换，与二C对应）

- pushViewController:animated: 推进一个新视图到栈里，出现新视图，可以带动画效果  
例 pushViewController:animated:

### [返回上/前一个View](#2)

A:insertSubView系列：（注意，如果你新增视图不够大，则遮不住上一层视图，即前后2个视图都存在，当然你可以做透明来查看所有，与一A对应）

- sendSubviewToBack: 将新视图放在其他同级视图的behind位置  
- removeFromSuperview：将新视图从父视图上移除

B:presentViewController系列：（与一B对应）

- dismissViewControllerAnimated:completion:退出一个新视图 可以带动画效果，完成后可以做相应的执行函数经常为nil  
- dismissModalViewControllerAnimated: 退出一个新视图 可以带动画效果

C:UINavigationController系列：（常用导航栏视图切换，与一C对应）

- popViewControllerAnimated: 从一个栈中退出视图，返回上一层，可以带动画效果  
- popToRootViewControllerAnimated:从一个栈中退出视图，返回到navigation的RootView，可以带动画效果  
- popToViewController:animated:从一个栈中退出视图，返回到navigation中指定的view，可以带动画效果  
基本上上面已经介绍完全部常用视图切换方式：

### [UITabBarController：（需要先将几种视图在tabBar种设置好）](#3)

- setViewControllers:animated:设置要出现的视图

- selectedViewController 设置要出现的视图

- selectedIndex 设置要出现的视图下标

来源:http://blog.csdn.net/u010335966/article/details/8858172
