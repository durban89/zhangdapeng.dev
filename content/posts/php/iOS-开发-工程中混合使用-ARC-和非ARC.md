---
title: "iOS 开发，工程中混合使用 ARC 和非ARC"
date: "2025-06-17 11:59:43"
slug: "ios-kai-fa-gong-cheng-zhong-hun-he-shi-yong-arc-he-fei-arc"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS-开发，工程中混合使用-ARC-和非ARC/"
  - "/2025/06/17/iOS-开发，工程中混合使用-ARC-和非ARC.html"
  - "/iOS-开发，工程中混合使用-ARC-和非ARC/"
  - "/iOS-开发，工程中混合使用-ARC-和非ARC.html"
  - "/2025/06/17/iOS-开发-工程中混合使用-ARC-和非ARC/"
  - "/2025/06/17/iOS-开发-工程中混合使用-ARC-和非ARC.html"
  - "/2025/06/17/ios-kai-fa-gong-cheng-zhong-hun-he-shi-yong-arc-he-fei-arc/"
  - "/2025/06/17/ios-kai-fa-gong-cheng-zhong-hun-he-shi-yong-arc-he-fei-arc.html"
  - "/ios-kai-fa-gong-cheng-zhong-hun-he-shi-yong-arc-he-fei-arc.html"
---
问题是这样的：

在项目开发过程中我们通常会用到第三方提供的源代码，麻烦的是有些开源项目用的是 ARC，有的用的是非 ARC。  
我在使用 SVProgressHUD 做等待视图时遇到问题，最终发现该项目使用的是 ARC 模式，而我的工程使用的是非 ARC 模式。

解决方法是这样的：

Xcode 项目中我们可以使用 ARC 和非 ARC 的混合模式。  
如果你的项目使用的非 ARC 模式，则为 ARC 模式的代码文件加入 `-fobjc-arc` 标签。  
如果你的项目使用的是 ARC 模式，则为非 ARC 模式的代码文件加入 `-fno-objc-arc` 标签。  
添加标签的方法：  
1，打开：你的target -> Build Phases -> Compile Sources.  
2，双击对应的 \*.m 文件  
3，在弹出窗口中输入上面提到的标签 -fobjc-arc / -fno-objc-arc  
4，点击 done 保存

参考：http://blog.csdn.net/fangzhangsc2006/article/details/8049765#reply
