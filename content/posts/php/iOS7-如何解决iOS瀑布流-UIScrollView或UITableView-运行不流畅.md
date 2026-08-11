---
title: "iOS7 如何解决iOS瀑布流(UIScrollView或UITableView)运行不流畅"
date: "2025-06-26 14:55:24"
slug: "ios7-ru-he-jie-jue-ios-pu-bu-liu-uiscrollview-huo-uitableview-yun-xing-bu-liu-chang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-如何解决iOS瀑布流(UIScrollView或UITableView)运行不流畅/"
  - "/2025/06/26/iOS7-如何解决iOS瀑布流(UIScrollView或UITableView)运行不流畅.html"
  - "/iOS7-如何解决iOS瀑布流(UIScrollView或UITableView)运行不流畅/"
  - "/iOS7-如何解决iOS瀑布流(UIScrollView或UITableView)运行不流畅.html"
  - "/2025/06/26/iOS7-如何解决iOS瀑布流-UIScrollView或UITableView-运行不流畅/"
  - "/2025/06/26/iOS7-如何解决iOS瀑布流-UIScrollView或UITableView-运行不流畅.html"
  - "/2025/06/26/ios7-ru-he-jie-jue-ios-pu-bu-liu-uiscrollview-huo-uitableview-yun-xing-bu-liu-chang/"
  - "/2025/06/26/ios7-ru-he-jie-jue-ios-pu-bu-liu-uiscrollview-huo-uitableview-yun-xing-bu-liu-chang.html"
  - "/ios7-ru-he-jie-jue-ios-pu-bu-liu-uiscrollview-huo-uitableview-yun-xing-bu-liu-chang.html"
---
如果UITableView滑动太快，可能同时就发出了比如10个图片请求。这些请求虽然都在后台运行，但是它们可能在同一个时间点返回UI线程。这个时候如果加载图片到UIImageView太频繁，就会造成UI卡得严重。（虽然在new iPad和iPhone4s上看不出来）

在找到这个问题的同时，也发现performSelectorAfterDelay这个方法，会堆积到UI线程空闲的时候执行。而dispatch\_after或者dispatch\_async都会直接插入UI线程当场执行。所以这个问题其实可以用performSelectorAfterDelay来解决，测试也是非常流畅，感觉不出一点点的卡。但会出现新的问题，那就是在滑动过程中，不会加载任何图片。知道scrollView停止的时候，图片才会出来。当然这不是理想的解决方法了。这个方法也没有解决异步过程集中到达UI线程的问题。然后采用了NSOperationQueue来解决这个问题。

问题本身和UITableView加载不流畅是一样的。

#### [解决办法](#1)

主要要做到一下几个方面：

1. 除了UI部分，所有的加载操作都在后台完成。  
   这一点可以通过dispatch或者performSelectorInBackground或者NSOperationQueue来实现。见：  
   在iOS开发中利用GCD进行多线程编程  
   iOS开发中使用NSOperationQueue进行多线程操作
2. 避免后台加载完成多个资源之后集中到达占用UI线程的处理时间太长。  
   这一点可以通过NSOperationQueue来实现，将资源到UI的展现过程放在队列中逐个执行，且在每个操作完成之后进行强制等待，可以用usleep(int microSeconds)来解决。
3. 重用cell。  
   创建cell一般是很慢的，一定要重用，甚至为了performance，可以在view创建之初就创建足够多的cell在重用队列中。

---

参考文章

http://blog.unieagle.net/2012/08/31/如何解决ios瀑布流uiscrollview或uitableview运行不流畅/

