---
title: "XCode实用插件"
date: "2025-06-23 15:48:58"
slug: "xcode-shi-yong-cha-jian"
categories: ["技术"]
tags: ["Xcode"]
aliases:
  - "/2025/06/23/XCode实用插件/"
  - "/2025/06/23/XCode实用插件.html"
  - "/XCode实用插件/"
  - "/XCode实用插件.html"
  - "/2025/06/23/xcode-shi-yong-cha-jian/"
  - "/2025/06/23/xcode-shi-yong-cha-jian.html"
  - "/xcode-shi-yong-cha-jian.html"
---
IOS开发会遇到很多的问题，但是如果有一些好的插件的话，应该可以解决很多的问题的，尤其是在项目中，有了一些简便的插件，能够解决很大的问题。

### [全能搜索家CodePilot 2.0](#1)

你要找的是文件？是文件夹？是代码？Never Mind，CMD+SHIFT+X调出CodePilot，输入任何你想到搜的东西吧！想搜 appFinishLaunchingWithOptions？忘记咋拼了？没关系强大的代码搜索能力，appflaun一样也可以找到！超级强大的正则 匹配，匹配任何你所想！

项目地址：<http://codepilot.cc>

### [Vim控必备的XVim](#2)

XVim是一个针对Xcode的Vim插件，能让开发者在不放弃任何xcode功能的前提下体验vim的功能。

项目地址：<https://github.com/JugglerShu/XVim>

### [YouCompleteMe（vim的插件）](#3)

如果你比较喜欢用vim来写代码的话，这里有一个非常棒的vim插件——YouCompleteMe——当你在编写OC代码时，可以提升体验。 YouCompleteMe可以在Vim中添加代码自动补全功能，并且不需要你来按某个键来查看代码补全建议——针对OC、OC++、C++以及C该插件 可以自动补全建议。

项目地址：<https://github.com/Valloric/YouCompleteMe>

### [XCode颜色显示插件ColorSense](#4)

代码里的那些冷冰冰的颜色数值，到底时什么颜色？如果你经常遇到这个问题，每每不得不运行下模拟器去看看，那么这个插件绝对不容错过。更彪悍的是你甚至可以点击显示的颜色面板，直接通过系统的ColorPicker来自动生成对应颜色代码，再也不用做各种颜色代码转换了！

项目地址： <https://github.com/omz/ColorSense-for-Xcode>

### [大段文本利器HOStringSense](#5)

经常输入大段文本的时候，如果文本里面有各种换行和特殊字符，经常会让人很头疼，有了HOStringSense，再也不不用为这个问题犯愁了，顺便附送字数统计功能。

项目地址：<https://github.com/holtwick/HOStringSense-for-Xcode>

### [规范注释生成器VVDocumenter](#6)

很多时候，为了快速开发，很多的技术文档都是能省则省，这个时候注释就变得异常重要，再配合Doxygen这种注释自动生成文档的，就完美了。但 是每次都要手动输入规范化的注释，着实也麻烦，但有了VVDocumenter，规范化的注释，主需要输入三个斜线“///”，就OK啦！ （VVDocumenter在Mac OSX 10.8.5和Xcode 4.6.3上进行开发，应该能支持所有Xcode 4版本，如果想支持Xcode 5，可以对plist文件稍作修改。

项目地址：<https://github.com/onevcat/VVDocumenter-Xcode>

### [CocoaPods for Xcode](#7)

非常方便的Xcode pods插件。可以很方便的在Xcode通过pods安装各种objective-c第三方库，省去以前还要手动去跑pods命令行的麻烦；此外，还支持 通过cocoaDocs来安装库文档。唯一的遗憾是，它目前只支持Xcode5，4版本还用不了。

项目地址：<https://github.com/kattrali/cocoapods-xcode-plugin>

### [Xcode语法高亮插件](#8)

以前用eclipse开发，自带的有语法高亮的效果。做ios开发也许久了，但是没发现一款语法高亮的插件，因为xcode自己的效果是仅在变量 或类名下面加了个虚线，平时看起代码来十分不舒服，最近果断为xcode写了一款语法高亮的插件，不过功能非常有限，没有eclipse的那么好用，也没 对对象的作用域区分，勉强能使用吧。和有需要的分享一下吧。

下载附件，解压后放在：你的用户/Library/Application Support/Developer/Shared/Xcode/Plug-ins目录下，有的童鞋还没有Plug-ins这个目录吧，那就手动建一个， 然后把解压后的highlight-Plugin.xcplugin放进去，重启xcode即可。然后就能看到高亮的菜单了。

项目地址： <http://www.cocoachina.com/bbs/read.php?tid=150107>

### [KSImageNamed-Xcode](#9)

为项目中使用的UIImage的imageNamed提供文件名自动补全功能。使用[UIImage imageNamed:@"xxx"]时，该插件会扫描整个workspace中的图片文件。

项目地址： <https://github.com/ksuther/KSImageNamed-Xcode>

### [xcode-extend-plug-in](#10)

帮助你快速格式化代码、生成注释、复制一行等。

项目地址： <https://code.google.com/p/xcode-extend-plug-in/>

### [XcodeColors](#11)

改变调试控制台颜色

项目地址： <https://github.com/robbiehanson/XcodeColors>

### [SCXcodeMiniMap](#12)

一个Xcode插件，可以在当前的窗口内创建一个代码迷你地图，并在屏幕上高亮提示。

项目地址： <https://github.com/stefanceriu/SCXcodeMiniMap>

### [Lin本地化字符串](#13)

之前我们提到过一个开源的Mac基础工具SCStringsUtility，可以让你在一个清爽的界面编辑不同的语言，简单地输入/输出 NSLocalizedString数据。Lin是一款功能相近的Xcode插件，提供了一个非常不错的操作界面，并且为不同的语言提供了不同的区域。

项目地址：<https://github.com/questbeat/Lin>

### [插件管理Alcatraz](#14)

Alcatraz是一个开源的Xcode 4包管理器，可以让你更便捷地发现、安装以及管理插件、模板和配色方案。只需要简单地点击或者勾选，不需要手工复制和粘贴。

项目地址： <https://github.com/mneorr/Alcatraz>
