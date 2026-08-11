---
title: "iOS 使用AdHoc发布自己的程序"
date: "2025-06-16 14:37:54"
slug: "ios-shi-yong-adhoc-fa-bu-zi-ji-de-cheng-xu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/iOS-使用AdHoc发布自己的程序/"
  - "/2025/06/16/iOS-使用AdHoc发布自己的程序.html"
  - "/iOS-使用AdHoc发布自己的程序/"
  - "/iOS-使用AdHoc发布自己的程序.html"
  - "/2025/06/16/ios-shi-yong-adhoc-fa-bu-zi-ji-de-cheng-xu/"
  - "/2025/06/16/ios-shi-yong-adhoc-fa-bu-zi-ji-de-cheng-xu.html"
  - "/ios-shi-yong-adhoc-fa-bu-zi-ji-de-cheng-xu.html"
---
AdHoc实际主要就是你可以发布版本，通过签名Profile指定这个版本能在哪些设备上运行（不超过100个）。这样你可以把版本直接发给你的测试人员，不需要经过AppStore。起到Beta测试的作用。  
  
### [取得目标机器的UDID（Unique Device Identifier ）](#1) 

启动iTune，连接设备。选取设备，在Summary页面，可以看到Serial Number（序列号）。点击Serial Number（看上去是文字，实际可以点的），Serial Number就变成了UDID了。  

下面的部分翻译自http://www.iphonedevsdk.com/forum/iphone-sdk-development/35818-unofficial-ad-hoc-distribution-guide.html  
  
### [生成包含UDID的Provision file](#2)  

1.到你的iPhone Provision Potral，首先把你需要支持的Devide的UDID都输入进去。  
  
2.然后左边选 Provisioning，然后选Distribution，就到下面页面。按下面选择好。  
  
3.然后下载这个Provision File，双击，自动加入到Xcode中。  
  
### [编译你的工程](#3)

1.生成一个 entitlements plist 文件.  
  
2.我的这个界面和图上不一样，没有这个get-task-allow，而是其他的一些东西。我就什么都没动。  
  
3.在工程中“Get info”，选择Configurations，创建一个adhoc的Config。  
  
4.然后回到Build页面，Configuration选择adhoc，在Code Signing组下面，Code Signing Entitlements设为你刚刚建立的文件。  
  
5.Code Singing Identity用你正常发布的Provision  
  
6.Any iPhone OS Device用你刚刚创建的adhoc的Provision。  
  
7.最后Build你的应用，记着先Clean all Targets一下，然后你就可以在工程的Build目录下找到你的目标App了。  
  
### [如何安装](#4)  

把你的adhoc的Provision File和你刚刚生成的App文件发给你的Tester。  
他需要打开iTunes，在Libary->Applicatione页面，把Provision文件和App文件拖进去。  
连接设备，确认在设备的Apps下面，这个新app已经被选中（Default应该是选中的）

同步设备，App就安装上去了。
