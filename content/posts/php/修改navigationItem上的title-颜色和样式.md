---
title: "修改navigationItem上的title 颜色和样式"
date: "2025-06-26 14:55:30"
slug: "xiu-gai-navigationitem-shang-de-title-yan-se-he-yang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/修改navigationItem上的title-颜色和样式/"
  - "/2025/06/26/修改navigationItem上的title-颜色和样式.html"
  - "/修改navigationItem上的title-颜色和样式/"
  - "/修改navigationItem上的title-颜色和样式.html"
  - "/2025/06/26/xiu-gai-navigationitem-shang-de-title-yan-se-he-yang-shi/"
  - "/2025/06/26/xiu-gai-navigationitem-shang-de-title-yan-se-he-yang-shi.html"
  - "/xiu-gai-navigationitem-shang-de-title-yan-se-he-yang-shi.html"
---
今天正好做到这里，以为之前的设计是通过view的跳转，然后直接传递title过来，然后在viewDidLoad里面直接赋值，但是有遇到了一个比较傻眼的情况，接口只给我id，木有title，于是我就只有获取完title在赋值啦，于是找到了一个策略，就是在获取完数据后，直接使用下面的代码就好了，既可以修改样式还可以修改标题

```objectivec
UILabel *label = [[UILabel alloc] initWithFrame:CGRectZero];
label.backgroundColor = [UIColor clearColor];
label.font = [UIFont boldSystemFontOfSize:18.0];
label.textAlignment = NSTextAlignmentCenter;
label.textColor = [UIColor whiteColor];
self.navigationItem.titleView = label;
label.text = _personName;
[label sizeToFit];
```

---

文章参考：

http://blog.csdn.net/tongzhitao/article/details/9852633

