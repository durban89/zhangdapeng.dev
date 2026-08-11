---
title: "iOS7 UIViewController中使用UIRefreshControl  实现 UITableView下拉刷新"
date: "2025-06-26 14:55:28"
slug: "ios7-uiviewcontroller-zhong-shi-yong-uirefreshcontrol-shi-xian-uitableview-xia-la-shua-xin"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-UIViewController中使用UIRefreshControl-实现-UITableView下拉刷新/"
  - "/2025/06/26/iOS7-UIViewController中使用UIRefreshControl-实现-UITableView下拉刷新.html"
  - "/iOS7-UIViewController中使用UIRefreshControl-实现-UITableView下拉刷新/"
  - "/iOS7-UIViewController中使用UIRefreshControl-实现-UITableView下拉刷新.html"
  - "/2025/06/26/ios7-uiviewcontroller-zhong-shi-yong-uirefreshcontrol-shi-xian-uitableview-xia-la-shua-/"
  - "/2025/06/26/ios7-uiviewcontroller-zhong-shi-yong-uirefreshcontrol-shi-xian-uitableview-xia-la-s.html"
  - "/ios7-uiviewcontroller-zhong-shi-yong-uirefreshcontrol-shi-xian-uitableview-xia-la-shua-xin.html"
---
之前做了一个使用UITableViewController中实现刷新的方法，这里实现一个使用UIViewController实现下拉刷新，当果然要使用到UIRefreshControl。

创建啥的我就不记录了，文件列一下

MeCelebrityViewController.m

MeCelebrityViewController.h

MeCelebrityViewController.xib

下面列出主要的实现过程

第一步：组件的添加

```objectivec
@property (nonatomic, strong) UIRefreshControl* refreshControl;
```

viewDidLoad的初始化

```objectivec
//添加刷新
_refreshControl = [[UIRefreshControl alloc] init];
[_refreshControl addTarget:self
                  action:@selector(refreshView:)
        forControlEvents:UIControlEventValueChanged];
[_refreshControl setAttributedTitle:[[NSAttributedString alloc] initWithString:@"松手更新数据"]];
[_dataTableView addSubview:_refreshControl];
```

这里的`_dataTableView`是要自己添加的

```objectivec
CGFloat tableViewX = 0.0;
CGFloat tableViewY = 0.0;
CGFloat tableWidth = self.navigationController.navigationBar.frame.size.width;
CGFloat tableHeight = [[UIScreen mainScreen] bounds].size.height;
_dataTableView = [[UITableView alloc] initWithFrame:CGRectMake(tableViewX,
                                                               tableViewY,
                                                               tableWidth,
                                                               tableHeight)
                                              style:UITableViewStylePlain];

_cellHeight = 70.0;
_dataTableView.delegate = self;
_dataTableView.dataSource = self;
[self.view addSubview:_dataTableView];
```

第二步：实现下拉刷新的动作

```objectivec
-(void) refreshView:(UIRefreshControl *)refresh
{
    refresh.attributedTitle = [[NSAttributedString alloc] initWithString:@"更新数据中..."];
    
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    [formatter setDateFormat:@"MMM d, h:mm a"];
    NSString *lastUpdated = [NSString stringWithFormat:@"上次更新日期 %@",
                             [formatter stringFromDate:[NSDate date]]];
    refresh.attributedTitle = [[NSAttributedString alloc] initWithString:lastUpdated];
    [self initData];
    [_dataTableView reloadData];
    [refresh endRefreshing];
}
```

结果不是很完美，因为有遮挡的现象，不过流程走通了，下面开始自己的制作吧，如果有需要的帮助的话，请看下面的QQ群，加群交流

---

参考文章：

<http://www.yourdeveloper.net/item/program-a-uitableview-with-pulldown-to-refresh/>

http://www.techrepublic.com/blog/software-engineer/ios-6-best-practices-introducing-the-uirefreshcontrol/

