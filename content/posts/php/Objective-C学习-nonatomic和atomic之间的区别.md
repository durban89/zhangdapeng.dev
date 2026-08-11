---
title: "Objective-C学习 nonatomic和atomic之间的区别"
date: "2025-06-17 16:46:07"
slug: "objective-c-xue-xi-nonatomic-he-atomic-zhi-jian-de-qu-bie"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/17/Objective-C学习-nonatomic和atomic之间的区别/"
  - "/2025/06/17/Objective-C学习-nonatomic和atomic之间的区别.html"
  - "/Objective-C学习-nonatomic和atomic之间的区别/"
  - "/Objective-C学习-nonatomic和atomic之间的区别.html"
  - "/2025/06/17/objective-c-xue-xi-nonatomic-he-atomic-zhi-jian-de-qu-bie/"
  - "/2025/06/17/objective-c-xue-xi-nonatomic-he-atomic-zhi-jian-de-qu-bie.html"
  - "/objective-c-xue-xi-nonatomic-he-atomic-zhi-jian-de-qu-bie.html"
---
一直想搞明白nonatomic和atomic的区别，由于时间的问题一直没有去合理的看一下，最近搜索资料无意间被自己发现了，简答的记录一下

> atomic的意思就是setter/getter这两个函数的一个原语操作。如果有多个线程同时调用setter的话，不会出现某一个线程执行setter全部语句之前，另一个线程开始执行setter情况，相当于函数头尾加了锁一样。 nonatomic不保证setter/getter的原语行，所以你可能会取到不完整的东西。 比如setter函数里面改变两个成员变量，如果你用nonatomic的话，getter可能会取到只更改了其中一个变量时候的状态。 atomic是线程安全的,nonatomic是线程不安全的。如果只是单线程操作的话用nonatomic最好,因为后者效率高一些。

上面是引用自参考资料的

我的理解就是，为了追求获取变量值的安全性的话就使用atomic,如果追求效率而不是安全性的话就是使用nonatomic

参考：http://blog.csdn.net/wenwei19861106/article/details/8959483
