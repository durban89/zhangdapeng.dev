---
title: "loaded the \"BlueView\" nib but the view outlet was not set 错误的解决办法"
date: "2025-06-12 09:56:48"
slug: "loaded-the-blueview-nib-but-the-view-outlet-was-not-set-cuo-wu-de-jie-jue-ban-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/loaded-the-\"BlueView\"-nib-but-the-view-outlet-was-not-set-错误的解决办法/"
  - "/2025/06/12/loaded-the-\"BlueView\"-nib-but-the-view-outlet-was-not-set-错误的解决办法.html"
  - "/loaded-the-\"BlueView\"-nib-but-the-view-outlet-was-not-set-错误的解决办法/"
  - "/loaded-the-\"BlueView\"-nib-but-the-view-outlet-was-not-set-错误的解决办法.html"
  - "/2025/06/12/loaded-the-BlueView-nib-but-the-view-outlet-was-not-set-错误的解决办法/"
  - "/2025/06/12/loaded-the-BlueView-nib-but-the-view-outlet-was-not-set-错误的解决办法.html"
  - "/2025/06/12/loaded-the-blueview-nib-but-the-view-outlet-was-not-set-cuo-wu-de-jie-jue-ban-fa/"
  - "/2025/06/12/loaded-the-blueview-nib-but-the-view-outlet-was-not-set-cuo-wu-de-jie-jue-ban-fa.html"
  - "/loaded-the-blueview-nib-but-the-view-outlet-was-not-set-cuo-wu-de-jie-jue-ban-fa.html"
---
解决办法：

- 创建控制器. File->New File->Iphone OS->Cocoa Touch Class->UIViewController subclass;

- 创建xib. File->New File->Iphone OS->User Interface->View XIB

- 绑定controller和view. 用Interface Builder打开xxx.xib, 点击Files' Owner, 在Identity Inspector里面的Class Identity, 选择Step 1创建的控制器类, 接着拖拽File's Owner到View中, 选择Outlets->view.先选中file's owner(这个很重要)

来源:http://blog.csdn.net/thebesttome/article/details/7799893
