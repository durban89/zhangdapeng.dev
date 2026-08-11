---
title: "去掉UITableViewCell边框样式"
date: "2025-06-12 17:19:10"
slug: "qu-diao-uitableviewcell-bian-kuang-yang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/去掉UITableViewCell边框样式/"
  - "/2025/06/12/去掉UITableViewCell边框样式.html"
  - "/去掉UITableViewCell边框样式/"
  - "/去掉UITableViewCell边框样式.html"
  - "/2025/06/12/qu-diao-uitableviewcell-bian-kuang-yang-shi/"
  - "/2025/06/12/qu-diao-uitableviewcell-bian-kuang-yang-shi.html"
  - "/qu-diao-uitableviewcell-bian-kuang-yang-shi.html"
---
### [方法 1:](#1)

如果，UITableView的类型为UITableViewStyleGrounped，发现使用`_tableView.backgroundColor = [UIColor clearColor]`后，tableView的背景色仍然是默认的色，上网查了下：  
`_tableView.backgroundView = nil;`可以搞定。  
测试下发现确实可以，但是不知道以前的版本不确定有没有backgroundView的，所以最好加个判断吧：

```objectivec
if (mainTableView.backgroundView)
{
    mainTableView.backgroundView =nil;
}
```

如果类型为UITableViewStylePlain，[UIColor clearColor]仍然有效，怪哉！  
正常情况下grouped样式（UITableViewStyleGrouped）UITableViewCell都是有边框的，如果要去掉边框可以用：

```objectivec
UIView *tempView = [[[UIView alloc] init] autorelease];
[cell setBackgroundView:tempView];
[cell setBackgroundColor:[UIColor clearColor]];
```

其实很简单，把backgroundView设置为一个空的View，然后就干净了。看了下UITableViewCell的文档，backgroundView在plain-style的TableView里面是nil，在grouped-style的TableView里面并不是空的，所以这里设置空就ok了，这是目前为止我见到的最完美的解决方案。

### [方法 2:](#2)

```objectivec
[tableView setSeparatorColor:[UIColor clearColor]];
```

### [方法 3:](#3)

```objectivec
cell.backgroundView = [[[UIView alloc] initWithFrame:CGRectZero] autorelease];
```
