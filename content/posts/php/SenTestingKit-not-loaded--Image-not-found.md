---
title: "SenTestingKit not loaded, Image not found"
date: "2025-06-17 17:21:20"
slug: "sentestingkit-not-loaded-image-not-found"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/SenTestingKit-not-loaded,-Image-not-found/"
  - "/2025/06/17/SenTestingKit-not-loaded,-Image-not-found.html"
  - "/SenTestingKit-not-loaded,-Image-not-found/"
  - "/SenTestingKit-not-loaded,-Image-not-found.html"
  - "/2025/06/17/SenTestingKit-not-loaded-Image-not-found/"
  - "/2025/06/17/SenTestingKit-not-loaded-Image-not-found.html"
  - "/2025/06/17/sentestingkit-not-loaded-image-not-found/"
  - "/2025/06/17/sentestingkit-not-loaded-image-not-found.html"
  - "/sentestingkit-not-loaded-image-not-found.html"
---
报错信息：

dyld: Library not loaded: @rpath/SenTestingKit.framework/Versions/A/SenTestingKit

文件我参考“http://www.carrotcoded.com/2012/10/10/sentestingkit-not-loaded-image-not-found/”

里面是这样的描述的

> I am pretty sure that it was working perfectly in the old macbook pro, therefore i set out to google and see that alot of people actually hit this issue but there wasn’t any clear cut answer. To solve this basically, expand your solution -> Frameworks -> Remove the SenTestingKit from your project. This should resolve the issue. Note : Please remove reference not delete it.

大概的意思就是说，去掉这个SenTestingKit.framework框架就好了。

我去掉后确实可以了，也没有影响我的后面的运行

Note : Please remove reference not delete it.

注意这一句，别删掉了，这个可是框架自己本身就有的
