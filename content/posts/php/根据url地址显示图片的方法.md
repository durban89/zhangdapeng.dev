---
title: "根据url地址显示图片的方法"
date: "2025-06-17 11:59:57"
slug: "gen-ju-url-di-zhi-xian-shi-tu-pian-de-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/根据url地址显示图片的方法/"
  - "/2025/06/17/根据url地址显示图片的方法.html"
  - "/根据url地址显示图片的方法/"
  - "/根据url地址显示图片的方法.html"
  - "/2025/06/17/gen-ju-url-di-zhi-xian-shi-tu-pian-de-fang-fa/"
  - "/2025/06/17/gen-ju-url-di-zhi-xian-shi-tu-pian-de-fang-fa.html"
  - "/gen-ju-url-di-zhi-xian-shi-tu-pian-de-fang-fa.html"
---
虽然说这样的效率不好，但是既然有这样的方式就有这种方式存在的道理

我记录一下其实现方法：

```objectivec
cell.imageViewPic.image = [[UIImage alloc] initWithData:[NSData dataWithContentsOfURL:[NSURL URLWithString:[NSString stringWithFormat:@"personpanel-%@-zfx.jpg",[dic valueForKey:@"person_id"]] relativeToURL:[NSURL URLWithString:@"http://xxxx.xxxx.xxxxx/xxxx/"]]]];
```

cell.imageViewPic是一个实例化的UIImageview
