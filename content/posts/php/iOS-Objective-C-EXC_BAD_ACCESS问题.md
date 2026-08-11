---
title: "iOS Objective-C EXC_BAD_ACCESS问题"
date: "2025-06-11 11:27:15"
slug: "ios-objective-c-exc-bad-access-wen-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-Objective-C-EXC-BAD-ACCESS问题/"
  - "/2025/06/11/iOS-Objective-C-EXC-BAD-ACCESS问题.html"
  - "/iOS-Objective-C-EXC-BAD-ACCESS问题/"
  - "/iOS-Objective-C-EXC-BAD-ACCESS问题.html"
  - "/2025/06/11/ios-objective-c-exc-bad-access-wen-ti/"
  - "/2025/06/11/ios-objective-c-exc-bad-access-wen-ti.html"
  - "/ios-objective-c-exc-bad-access-wen-ti.html"
---
写程序遇到 Bug 并不可怕，大部分的问题，通过简单的 Log 或者 代码分析并不难找到原因所在。但是在 Objective-C 编程中遇到 EXC\_BAD\_ACCESS 问题的时候，通过简单常规的手段很难发现问题。  
写程序遇到 Bug 并不可怕，大部分的问题，通过简单的 Log 或者 代码分析并不难找到原因所在。但是在 Objective-C 编程中遇到 EXC\_BAD\_ACCESS 问题的时候，通过简单常规的手段很难发现问题。这篇文章，给大家介绍一个常用的查找 EXC\_BAD\_ACCESS 问题根源的方法。  
首先说一下 EXC\_BAD\_ACCESS 这个错误，可以这么说，90%的错误来源在于对一个已经释放的对象进行release操作。  
Objective-C 这段代码有三个致命问题：1、内存泄露；2、错误释放；3、造成 EXC\_BAD\_ACCESS 错误。

1， NSString\* s = [[NSString alloc]initWithString:@”This is a test string”]; 创建了一个 NSString Object，随后的 s = [s substringFromIndex:[s rangeOfString:@"a"].location]; 执行后，导致创建的对象引用消失，直接造成内存泄露。

2，错误释放。[s release]; 这个问题，原因之一是一个逻辑错误，以为 s 还是我们最初创建的那个 NSString 对象。第二是因为从 substringFromIndex:(NSUInteger i) 这个方法返回的 NSString 对象，并不需要

我们来释放，它其实是一个被 substringFromIndex 方法标记为 autorelease 的对象。如果我们强行的释放了它，那么会造成 EXC\_BAD\_ACCESS 问题。

3， EXC\_BAD\_ACCESS。由于 s 指向的 NSString 对象被标记为 autorelease, 则在 NSAutoreleasePool 中已有记录。但是由于我们在前面错误的释放了该对象，则当 [pool drain] 的时候，NSAutoreleasePool

又一次的对它记录的 s 对象调用了 release 方法，但这个时候 s 已经被释放不复存在，则直接导致了 EXC\_BAD\_ACCESS问题。

查看更多的Console信息

工作区->Excuteables->双击其分组下的文件->Arguments设置运行参数

1: 为工程运行时加入 NSZombieEnabled 环境变量，则在 EXC\_BAD\_ACCESS 发生时，XCode 的 Console 会打印出问题描述。

2：加入 MallocStackLogging 来启用malloc记录

做如下设置：

Project -> Edit active executable ->Argument

添加如下四个参数

> NSDebugEnabled
>
> NSZombieEnabled
>
> MallocStackLogging
>
> MallocStackLoggingNoCompact

来源：http://blog.csdn.net/sjzsp/article/details/6386987
