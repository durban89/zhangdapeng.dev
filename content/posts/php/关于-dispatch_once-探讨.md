---
title: "关于 dispatch_once 探讨"
date: "2025-06-19 10:48:34"
slug: "guan-yu-dispatch-once-tan-tao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/关于-dispatch-once-探讨/"
  - "/2025/06/19/关于-dispatch-once-探讨.html"
  - "/关于-dispatch-once-探讨/"
  - "/关于-dispatch-once-探讨.html"
  - "/2025/06/19/guan-yu-dispatch-once-tan-tao/"
  - "/2025/06/19/guan-yu-dispatch-once-tan-tao.html"
  - "/guan-yu-dispatch-once-tan-tao.html"
---
`dispatch_once` 在ios中是用来创建单例的，具体为什么要创建单例，咱先不讨论，咱先看看，这个要怎么使用。

利用dispatch_once创建单例

在开发中我们会用到NSNotificationCenter、NSFileManager等，获取他们的实例通过`[NSNotificationCenter defaultCenter]`和`[NSFileManager defaultManager]`来获取，其实这就是单例。

我们先看下函数`void dispatch_once( dispatch_once_t *predicate, dispatch_block_t block);`其中第一个参数predicate，该参数是检查后面第二个参数所代表的代码块是否被调用的谓词，第二个参数则是在整个应用程序中只会被调用一次的代码块。dispach_once函数中的代码块只会被执行一次，而且还是线程安全的。

接下来我们来实现自己的单例，这里有一个TestManager类，为这个类实现单例

```objectivec
+(TestManager *)sharedInstance
{
    static TestManager *sharedManager;
    
    static dispatch_once_t once;
    dispatch_once(&once, ^{
        sharedManager = [[TestManager alloc] init];
    });
    
    return sharedManager;
}
```

到目前为止，我们就实现了一个单例，一切就搞定了，是不是很简单！

使用就按照如下方式获取唯一实例即可：

```objectivec
TestManager *testManager = [TestManager sharedInstance];
```

讨论dispatch_once函数实现单例的方法就这样结束啦，呵呵
