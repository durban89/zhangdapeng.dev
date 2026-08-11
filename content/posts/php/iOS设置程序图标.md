---
title: "iOS设置程序图标"
date: "2025-06-11 11:09:43"
slug: "ios-she-zhi-cheng-xu-tu-biao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS设置程序图标/"
  - "/2025/06/11/iOS设置程序图标.html"
  - "/iOS设置程序图标/"
  - "/iOS设置程序图标.html"
  - "/2025/06/11/ios-she-zhi-cheng-xu-tu-biao/"
  - "/2025/06/11/ios-she-zhi-cheng-xu-tu-biao.html"
  - "/ios-she-zhi-cheng-xu-tu-biao.html"
---
iOS中心有图标的相关说明,地址为：https://developer.apple.com/library/ios/#documentation/UserExperience/Conceptual/ MobileHIG/IconsImages/IconsImages.html#//apple\_ref/doc/uid/TP40006556-CH14-SW16

这里解释一下，方便自己查看：

### [iOS图标尺寸一览](#1)

iPhone专用程序:

|图标名称| 大小| 圆角| 用途| 必需  
|--|--|--|--|--
|Icon.png| 57 X 57| 10px| 用于程序商店和在iPhone/iPod Touch中显示| 必需 
|Icon\@2x.png|114 X 114| 20px| Icon.png的高清模式    |
|Icon-Small.png| 29 X 29| 20px| 用于设置和Spotlight搜索 |
|Icon-Small\@2x.png|58 X 58| 8px| Icon-Small.png的高清模式|

ipad专用程序:

|图标名称| 大小| 圆角| 用途| 必需
|--|--|--|--|--
|Icon-72.png| 72 X 72| 20px| 用于在iPad桌面中显示| 必需  
|Icon-50.png| 50 X 50| ?| 用于iPad中的Spotlight搜索    
|Icon-29.png| 29 X 29| 10px| 设置页面

通用程序:

|图标名称| 大小| 圆角| 用途| 必需  
|--|--|--|--|--
|Icon-72.png| 72 X 72| 20px| 用于在iPad桌面中显示| 必需  
|Icon.png| 57 X 57| 10px| 用于程序商店和在iPhone/iPod Touch中显示| 必需  
|Icon-50.png| 50 X 50| 10px| 用于iPad中的Spotlight搜索|    
|Icon-29.png| 29 X 29| 20px| 用于设置和Spotlight搜索|

### [取消图标上的高光](#2)

系统会默认会在图标上自动加上半透明的高光半圆，如果我们不想要这个效果或者图标本身已经包含了这个高光效果，我们可以在项目配置里把系统的高光功能取消掉：  
**xcode3.2x建的项目：**  
在info plist里加一个配置项，key为“Icon already includes gloss and bevel effects”， 类型为bool，然后打上钩就，这样系统就不会自动加高光；  
**xcode4建的项目：**  
在项目target的summary标签页下找到App Icons项，在“Prerendered”打上钩  
再找到“Icon files (iOS 5)”项目（如果有的话），展开，把里面的“Icon already includes gloss effects”也设置成“YES”：这样程序中的高光效果就取消了。

### [itunes connect上的图标](#3)

我们在itunes connect网站上创建应用时也要求上传图标，上传后 itunes connect也会给图标加上高光效果。这不用担心，如果我们的程序已经取消了高光效果，在程序上传后，网站上图标的高光效果也会自动取消掉的。
