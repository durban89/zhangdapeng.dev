---
title: "iOS错误之-could not load inserted library"
date: "2025-06-12 09:34:19"
slug: "ios-cuo-wu-zhi-could-not-load-inserted-library"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS错误之-could-not-load-inserted-library/"
  - "/2025/06/12/iOS错误之-could-not-load-inserted-library.html"
  - "/iOS错误之-could-not-load-inserted-library/"
  - "/iOS错误之-could-not-load-inserted-library.html"
  - "/2025/06/12/ios-cuo-wu-zhi-could-not-load-inserted-library/"
  - "/2025/06/12/ios-cuo-wu-zhi-could-not-load-inserted-library.html"
  - "/ios-cuo-wu-zhi-could-not-load-inserted-library.html"
---
最近写一个程序时,不知道怎么弄的,不能build到真机了,到模拟器没有什么问题,出现的错误是 : 研究可很长时间,也没有弄明白,在网上也着了很多资料,说是enable 了 guardmalloc

```shell
could not load inserted library: /usr/lib/libgmalloc.dylib
```

在xcode里面找了很久也没有着到怎么关闭, 最后无意中 发现了关闭他的方法,问题也解决了.  
方法:  
菜单-->Product--->EditScheme, 左边框 有一个列表,点击 run xxx.app , 你会发现在右边 Diagnostics里 有一些checkbox, 第三行 便是 关闭 Guard Malloc,  
保险起见,clean 下工程,重新build 下 就ok了.
