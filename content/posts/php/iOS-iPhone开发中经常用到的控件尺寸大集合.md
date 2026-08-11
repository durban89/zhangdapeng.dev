---
title: "iOS iPhone开发中经常用到的控件尺寸大集合"
date: "2025-06-12 14:39:27"
slug: "ios-iphone-kai-fa-zhong-jing-chang-yong-dao-de-kong-jian-chi-cun-da-ji-he"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-iPhone开发中经常用到的控件尺寸大集合/"
  - "/2025/06/12/iOS-iPhone开发中经常用到的控件尺寸大集合.html"
  - "/iOS-iPhone开发中经常用到的控件尺寸大集合/"
  - "/iOS-iPhone开发中经常用到的控件尺寸大集合.html"
  - "/2025/06/12/ios-iphone-kai-fa-zhong-jing-chang-yong-dao-de-kong-jian-chi-cun-da-ji-he/"
  - "/2025/06/12/ios-iphone-kai-fa-zhong-jing-chang-yong-dao-de-kong-jian-chi-cun-da-ji-he.html"
  - "/ios-iphone-kai-fa-zhong-jing-chang-yong-dao-de-kong-jian-chi-cun-da-ji-he.html"
---
网站上搜集了一些，关于iphone的尺寸方面的资料：简单的贴到下面，喜欢的朋友可以自己查看一下：

|  |  |
| --- | --- |
| Element | Size (in points) |
| Window (including status bar) | 320 x 480 pts |
| Status Bar  ([How to hide the status bar](http://www.idev101.com/code/User_Interface/UIStatusBar.html)) | 20 pts |
| View inside window  (visible status bar) | 320 x 460 |
| Navigation Bar | 44 pts |
| Nav Bar Image/Toolbar Image | up to 20 x 20 pts (transparent PNG) |
| Tab Bar | 49 pts |
| Tab Bar Icon | up to 30 x 30 pts (transparent PNGs) |
| Text Field | 31 pts |
| Height of a view inside a navigation bar | 416 pts |
| Height of a view inside a tab bar | 411 pts |
| Height of a view inside a navbar *and* a tab bar | 367 pts |
| Portrait Keyboard height | 216 pts |
| Landscape Keyboard height | 140 pts |

**Points vs. Pixels**  
The iPhone 4 introduced a high resolution display with twice the pixels of previous iPhones. However you don't have to modify your code to support high-res displays; the coordinate system goes by points rather than pixels, and the dimensions in points of the screen and all UI elements remain the same.  
iOS 4 supports high resolution displays (like the iPhone 4 display) via the scale property on UIScreen, UIView, UIImage, and CALayer classes. If the object is displaying high-res content, its scale property is set to 2.0. Otherwise it defaults to 1.0.  
All you need to do to support high-res displays is to provide @2x versions of the images in your project. See the [checklist for updating to iOS4](http://www.idev101.com/code/Distribution/updating_ios4.html#l2) or Apple documentation for [Supporting High Resolution Screens](http://developer.apple.com/library/ios/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/SupportingHiResScreens/SupportingHiResScreens.html) for more info.  
**Adjusting Sizes**  
Click here to see how to adjust [View Frames and Bounds](http://www.idev101.com/code/User_Interface/view_frames_bounds.html).  
**Additional References**

* Apple Documentation: [Points vs. Pixels](http://developer.apple.com/library/ios/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/GraphicsDrawingOverview/GraphicsDrawingOverview.html#/apple_ref/doc/uid/TP40010156-CH14-SW7)
* Apple Documentation: [UIBarButtonItem Class Reference](http://developer.apple.com/iphone/library/documentation/UIKit/Reference/UIBarButtonItem_Class/Reference/Reference.html#/apple_ref/doc/uid/TP40007519-CH3-SW3) says "Typically, the size of a toolbar and navigation bar image is 20 x 20 points."
* Apple Documentation: [UITabBarItem Class Reference](http://developer.apple.com/iphone/library/documentation/UIKit/Reference/UITabBarItem_Class/Reference/Reference.html#/apple_ref/occ/instm/UITabBarItem/initWithTitle:image:tag:) says "The size of an tab bar image is typically 30 x 30 points."

