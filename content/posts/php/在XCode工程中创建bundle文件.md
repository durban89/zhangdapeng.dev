---
title: "在XCode工程中创建bundle文件"
date: "2025-06-20 11:33:19"
slug: "zai-xcode-gong-cheng-zhong-chuang-jian-bundle-wen-jian"
categories: ["技术"]
tags: ["Xcode"]
aliases:
  - "/2025/06/20/在XCode工程中创建bundle文件/"
  - "/2025/06/20/在XCode工程中创建bundle文件.html"
  - "/在XCode工程中创建bundle文件/"
  - "/在XCode工程中创建bundle文件.html"
  - "/2025/06/20/zai-xcode-gong-cheng-zhong-chuang-jian-bundle-wen-jian/"
  - "/2025/06/20/zai-xcode-gong-cheng-zhong-chuang-jian-bundle-wen-jian.html"
  - "/zai-xcode-gong-cheng-zhong-chuang-jian-bundle-wen-jian.html"
---
关于文件资源的管理，我觉得一个不错的方法，那就是使用bundle。下面是引用一位大牛的，感觉操作和说的都不错。

> 在ios开发中为了方便管理资源文件，可以使用bundle的方式来进行管理，类似于ArcGIS Runtime for iOS中的ArcGIS.bundle .
>
> 切记目前iOS中只允许使用bundle管理资源文件和国际化信息，不支持代码的打包。
>
> 在xcode3.2.5 中只能够创建setting bundle，会默认创建一些配置文件，在xcode中无法直接删除，这也许不是我们需要的。
>
> 那么如何使用最简单的方法创建一个bundle呢?
>
> 1 创建一个文件夹
>
> 2 将该文件夹重命名为a.bundle
>
> 3 将a.bundle拖入到xcode中即可
>
> bundle的本质就是一个文件夹。当然在iOS中还可以干很多事情，详细资料请参考：
>
> [链接](https://developer.apple.com/library/ios/#documentation/CoreFoundation/Conceptual/CFBundles/AboutBundles/AboutBundles.html#//apple_ref/doc/uid/10000123i-CH100-SW7)

在项目中大家自己的可以借鉴一下，方便自己的项目的文件管理
