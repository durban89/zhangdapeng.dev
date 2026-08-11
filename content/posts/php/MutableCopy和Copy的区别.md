---
title: "mutableCopy和Copy的区别"
date: "2025-06-13 14:08:38"
slug: "mutablecopy-he-copy-de-qu-bie"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/mutableCopy和Copy的区别/"
  - "/2025/06/13/mutableCopy和Copy的区别.html"
  - "/mutableCopy和Copy的区别/"
  - "/mutableCopy和Copy的区别.html"
  - "/2025/06/13/MutableCopy和Copy的区别/"
  - "/2025/06/13/MutableCopy和Copy的区别.html"
  - "/2025/06/13/mutablecopy-he-copy-de-qu-bie/"
  - "/2025/06/13/mutablecopy-he-copy-de-qu-bie.html"
  - "/mutablecopy-he-copy-de-qu-bie.html"
---
这两个方法区别就是一个可以copy后是可变的，一个是不可变的

我举个例子，代码如下：

```objectivec
@property (strong, nonatomic) NSMutableDictionary *dataDic;
@property (strong, nonatomic) NSMutableDictionary *showDataDic;
```

我要copy dataDic到showDataDic里面去

第一种方法：

```objectivec
self.showDataDic = [NSMutableDictionary dictionaryWithCapacity:20];
self.showDataDic = [self.dataDic copy];
```

这样的话self.showDataDic是不可变的

第二种方法：

```objectivec
self.showDataDic = [NSMutableDictionary dictionaryWithCapacity:20];
self.showDataDic = [self.dataDic mutableCopy];
```

这样的话self.showDataDic是可变的
