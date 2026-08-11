---
title: "CFRunLoop 初次相识"
date: "2025-06-19 13:55:06"
slug: "cfrunloop-chu-ci-xiang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/CFRunLoop-初次相识/"
  - "/2025/06/19/CFRunLoop-初次相识.html"
  - "/CFRunLoop-初次相识/"
  - "/CFRunLoop-初次相识.html"
  - "/2025/06/19/cfrunloop-chu-ci-xiang-shi/"
  - "/2025/06/19/cfrunloop-chu-ci-xiang-shi.html"
  - "/cfrunloop-chu-ci-xiang-shi.html"
---
CFRunLoop的初次相识,不了解他，也不认识她。

我参考的文章中，有一处是这么说的

> Run loops是线程的基础架构部分。一个run loop就是一个事件处理循环，用来不停的调配工作以及处理输入事件。使用run loop的目的是使你的线程在有工作的时候工作，没有的时候休眠。
>
> Run loop的管理并不完全是自动的。你仍必须设计你的线程代码以在适当的时候启动run loop并正确响应输入事件。Cocoa和CoreFundation都提供了run loop对象方便配置和管理线程的run loop。你创建的程序不需要显示的创建run loop；每个线程，包括程序的主线程（main thread）都有与之相应的run loop对象。但是，自己创建的次线程是需要手动运行run loop的。在carbon和cocoa程序中，程序启动时，主线程会自行创建并运行run loop。
>
> 接下来的部分将会详细介绍run loop以及如何为你的程序管理run loop。关于run loop对象可以参阅sdk文档。
>
> 解析Run Loop
>
> run loop，顾名思义，就是一个循环，你的线程在这里开始，并运行事件处理程序来响应输入事件。你的代码要有实现循环部分的控制语句，换言之就是要有while或for语句。在run loop中，使用run loop对象来运行事件处理代码：响应接收到的事件，启动已经安装的处理程序。
>
> Run loop处理的输入事件有两种不同的来源：输入源（input source）和定时源（timer source）。输入源传递异步消息，通常来自于其他线程或者程序。定时源则传递同步消息，在特定时间或者一定的时间间隔发生。两种源的处理都使用程序的某一特定处理路径。

在苹果官方是这样解释的。

> A CFRunLoop object monitors sources of input to a task and dispatches control when they become ready for processing. Examples of input sources might include user input devices, network connections, periodic or time-delayed events, and asynchronous callbacks.

无奈，找到了一个例子：

```objectivec
//    used by thread2 to force thread exit
- (void)forceExit:(ThreadObj*)obj {
    obj.nExitFlag = 1;
    NSLog(@"The current forceExit id = %@", self);
}


// for thread1
- (void)func1 {
    nExitFlag = 0;
    NSLog(@"The current func1 id = %@", self);
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    //A runloop with no sources returns immediately from runMode:beforeDate:
    //That will wake up the loop and chew CPU. Add a dummy source to prevent
    //it.
    
    NSRunLoop *runLoop = [NSRunLoop currentRunLoop];    
    NSMachPort *dummyPort = [[NSMachPort alloc] init];    
    [runLoop addPort:dummyPort forMode:NSDefaultRunLoopMode];
    [dummyPort release];
    [pool release];
    
    while (!nExitFlag){
        NSAutoreleasePool *loopPool = [[NSAutoreleasePool alloc] init];        
        [runLoop runMode:NSDefaultRunLoopMode beforeDate:[NSDate distantFuture]];
        [loopPool drain];
    } 
}


// for thread2
- (void)func2:(NSArray *)args {
    nExitFlag = 0;
    
    NSLog(@"The current func2 id = %@", self);
    NSThread* thread1 = [args objectAtIndex:1];
    id id1 = [args objectAtIndex:0];
    
    //    force thread1 to exit
    [self performSelector:@selector(forceExit:) onThread:thread1 withObject:id1 waitUntilDone:YES];
}
```

里面就是这样调用了一下，输出的结果是：

```bash
2013-07-30 10:06:04.714 MyRunLoop[55395:1803] The current func1 id = <ThreadObj: 0x7132590>
2013-07-30 10:06:04.716 MyRunLoop[55395:2003] The current func2 id = <ThreadObj: 0x7132600>
2013-07-30 10:06:04.720 MyRunLoop[55395:1803] The current forceExit id = <ThreadObj: 0x7132600>
2013-07-30 10:06:05.135 MyRunLoop[55395:c07] Application windows are expected to have a root view controller at the end of application launch
```

是这样子的，你如果自己运行的话，估计会跟我有些区别的。

具体干嘛用，有时间继续 研究，对了还有一个知识点就是：NSMachPort

这个看起来也有大用处，好像跟传递文件有关系

> NSMachPort is a subclass of NSPort that can be used as an endpoint for distributed object connections (or raw messaging). NSMachPort is an object wrapper for a Mach port, the fundamental communication port in OS X. NSMachPort allows for local (on the same machine) communication only. A companion class, NSSocketPort, allows for both local and remote distributed object communication, but may be more expensive than NSMachPort for the local case.

好像越来越强大啦，呵呵

参考的文章地址：

[参考链接1](http://developer.apple.com/library/ios/#DOCUMENTATION/CoreFoundation/Reference/CFRunLoopRef/Reference/reference.html) [参考链接2](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSMachPort_Class/Reference/Reference.html) [参考链接3](http://www.cnblogs.com/scorpiozj/archive/2011/05/26/2058167.html)
