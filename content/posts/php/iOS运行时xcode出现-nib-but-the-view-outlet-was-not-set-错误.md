---
title: "iOS运行时xcode出现\"nib but the view outlet was not set.\"错误"
date: "2025-06-10 10:21:31"
slug: "ios-yun-xing-shi-xcode-chu-xian-nib-but-the-view-outlet-was-not-set-cuo-wu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS运行时xcode出现\"nib-but-the-view-outlet-was-not-set.\"错误/"
  - "/2025/06/10/iOS运行时xcode出现\"nib-but-the-view-outlet-was-not-set.\"错误.html"
  - "/iOS运行时xcode出现\"nib-but-the-view-outlet-was-not-set.\"错误/"
  - "/iOS运行时xcode出现\"nib-but-the-view-outlet-was-not-set.\"错误.html"
  - "/2025/06/10/iOS运行时xcode出现-nib-but-the-view-outlet-was-not-set-错误/"
  - "/2025/06/10/iOS运行时xcode出现-nib-but-the-view-outlet-was-not-set-错误.html"
  - "/2025/06/10/ios-yun-xing-shi-xcode-chu-xian-nib-but-the-view-outlet-was-not-set-cuo-wu/"
  - "/2025/06/10/ios-yun-xing-shi-xcode-chu-xian-nib-but-the-view-outlet-was-not-set-cuo-wu.html"
  - "/ios-yun-xing-shi-xcode-chu-xian-nib-but-the-view-outlet-was-not-set-cuo-wu.html"
---
出现的问题如标题：

问题原因是：

xib 中, 没有对File's Owner 的Outlets view 进行绑定, 导致在父视图中插入子视图时出错, 在IB中拖拽Files' Owner到view, 添加绑定后, 运行成功!  
总结一下创建视图和绑定的步骤:

- 创建控制器. File->New File->Iphone OS->Cocoa Touch Class->UIViewController subclass;

- 创建xib. File->New File->Iphone OS->User Interface->View XIB

- 绑定controller和view. 用Interface Builder打开xxx.xib, 点击Files' Owner, 在Identity Inspector里面的Class Identity, 选择Step 1创建的控制器类, 接着拖拽File's Owner到View中, 选择Outlets->view.先选中file's owner(这个很重要)

资源来自：[http://blog.csdn.net/thebesttome/article/details/7799893](http://blog.csdn.net/thebesttome/article/details/7799893)
