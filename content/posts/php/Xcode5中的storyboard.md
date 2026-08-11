---
title: "Xcode5中的storyboard"
date: "2025-06-20 14:34:02"
slug: "xcode5-zhong-de-storyboard"
categories: ["技术"]
tags: ["Xcode"]
aliases:
  - "/2025/06/20/Xcode5中的storyboard/"
  - "/2025/06/20/Xcode5中的storyboard.html"
  - "/Xcode5中的storyboard/"
  - "/Xcode5中的storyboard.html"
  - "/2025/06/20/xcode5-zhong-de-storyboard/"
  - "/2025/06/20/xcode5-zhong-de-storyboard.html"
  - "/xcode5-zhong-de-storyboard.html"
---
Xcode5 试用版发布了， 对于iOS开发者而言，仁者见仁，智者见智。 于我来说， 我更关心的是 storyboard 框架是否突破了原有的禁锢。

说来还有一段故事。我一向是推崇storyboard 框架的， 对于iOS 初学者，若想后浪推前浪，一定要善用storyboard 技术，因为它可以让你在UI实现上事半而功倍。 当Xcode4.2 所推出的storyboard 框架也有其先天的不足。 具体表现在，整个UI视图都容纳到一个storyboard 文件中， 当多人修改这个文件时，会造成凌乱， 无法merge。 从而，storyboard技术从一开始，就被贴上了一个“缺陷”的标签。 那就是，不适用团队协同开发。 可谓一丑遮百俊。

也正是这个诟病， storyboard 框架推行起来，困难重重。 尤其是习惯了通过编码写UI的程序员，更是抵触。

那么，这次Xcode5的发布， 是否对storyboard 框架有所改进呢？ 经过测试，果然没人失望，这正是我所期待的。

我们可以做个小实验，以便快速了解storyboard 框架的改进。

1.  通过Xcode 4.2 或4.5 或4.6 创建一个工程， 在storybaord 文件上，添加一个UIScrollview ，并在UIScrollview 内添加一些常用控件，比如： UILabel、 UIButton 等。  保存。

storyboard 文件，从本质上说，是一个 xib  文件， 更具体地说，是一个XML文件。

选中这个storyboard Open As > Source Code

2. 通过Xcode5 打开以上工程， 再打开这个storyboard文件

从提示文字可以看出， 当用Xcode5打开这个文件时，这个文件会自动升级， 而且是不可逆的。 这就是意味着， 这个文件结构将发生变化。  选中 “upgrade”， 继续.

这时， 再通过Open As > Source Code， 查看这个storyboard 文件结构。 你会惊喜地发现，xcode5 下的storyboard 文件结构比Xcode4 下，规整了很多， 更为重要的是， 这个XML的代码量大大缩减。  Xcode5下的storyboard 代码值规整，完全可以让你轻松地直接编写xml。

至此，可以说，Xcode4下的storyboard框架之良莠参半，在Xcode5下已达到可圈可点。 它解决了 xib 文件的merge 问题， 从而使得团队协同使用storyboard 框架成为可能。

