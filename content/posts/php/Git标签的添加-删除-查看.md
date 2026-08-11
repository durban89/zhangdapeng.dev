---
title: "Git标签的添加、删除、查看"
date: "2025-06-30 15:57:36"
slug: "git-biao-qian-de-tian-jia-shan-chu-cha-kan"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/06/30/Git标签的添加、删除、查看/"
  - "/2025/06/30/Git标签的添加、删除、查看.html"
  - "/Git标签的添加、删除、查看/"
  - "/Git标签的添加、删除、查看.html"
  - "/2025/06/30/Git标签的添加-删除-查看/"
  - "/2025/06/30/Git标签的添加-删除-查看.html"
  - "/2025/06/30/git-biao-qian-de-tian-jia-shan-chu-cha-kan/"
  - "/2025/06/30/git-biao-qian-de-tian-jia-shan-chu-cha-kan.html"
  - "/git-biao-qian-de-tian-jia-shan-chu-cha-kan.html"
---
最近突然想试试git的tag标签，感觉git的标签很实用，比如说你要在某个分之上发布一个app的版本包，ok，你就可以直接将此分支搞过来就好了，下次你想使用或者查看上一个版本的包，可以指定上一个tag就可以直接获取到上一个版本的代码了。

其实理解一下tag的添加、查看、删除这些基本的操作很简单的。

问题是，如果我想要获得某个版本的代码即某个标签的代码，来做修改，改如何处理呢？

这里我在网上搜索了一些资料。简单的介绍了一下git的分支管理策略，这个对项目的管理，测试，分发，以及后面的代码bug修改都有很大的帮助。

一篇是[git的分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html "git的分支管理策略")，一篇是[git标签的操作指南](http://zengrong.net/post/1746.htm "git标签的操作指南")，简要的介绍了一个标签的创建和使用，更简单的git标签的使用也可以参考这篇文章：[GIT-打标签](http://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E6%89%93%E6%A0%87%E7%AD%BE "git-打标签")，同时还有另外一篇文章，解决了我的疑问的文章，就是[如何获取git打好的tag所对应的代码](http://www.oschina.net/question/1030451_105857 "如何获取git打好的tag所对应的代码")，了解了这几篇文章，我觉得对git的合理利用应该能够可以得到充分的理解了。

 
