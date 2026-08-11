---
title: "关于scrollView下拉自动刷洗的 操作方法（待续）"
date: "2025-06-16 14:38:22"
slug: "guan-yu-scrollview-xia-la-zi-dong-shua-xi-de-cao-zuo-fang-fa-dai-xu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/关于scrollView下拉自动刷洗的-操作方法（待续）/"
  - "/2025/06/16/关于scrollView下拉自动刷洗的-操作方法（待续）.html"
  - "/关于scrollView下拉自动刷洗的-操作方法（待续）/"
  - "/关于scrollView下拉自动刷洗的-操作方法（待续）.html"
  - "/2025/06/16/关于scrollView下拉自动刷洗的-操作方法-待续/"
  - "/2025/06/16/关于scrollView下拉自动刷洗的-操作方法-待续.html"
  - "/2025/06/16/guan-yu-scrollview-xia-la-zi-dong-shua-xi-de-cao-zuo-fang-fa-dai-xu/"
  - "/2025/06/16/guan-yu-scrollview-xia-la-zi-dong-shua-xi-de-cao-zuo-fang-fa-dai-xu.html"
  - "/guan-yu-scrollview-xia-la-zi-dong-shua-xi-de-cao-zuo-fang-fa-dai-xu.html"
---
关于scrollView下拉自动刷洗的 操作方法，这个我最近由于做应用需要用到，找了几个版本的示例，自己根据原理试着自己做了一个，还是有点问题，先贴到这里，有时间再看看

testRefreshViewViewController.h

```objectivec
//
//  testRefreshViewViewController.h
//  testRefreshView
//
//  Created by david on 13-6-11.
//  Copyright (c) 2013年 walkerfree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "RefreshView.h"

@interface testRefreshViewViewController : UIViewController<RefreshViewDelegate, UIScrollViewDelegate>
{
    UIScrollView *scrollView;
    RefreshView *refreshView;
}
@property (strong, nonatomic) IBOutlet UIScrollView *scrollView;

@end
```

testRefreshViewViewController.m

```objectivec
//
//  testRefreshViewViewController.m
//  testRefreshView
//
//  Created by david on 13-6-11.
//  Copyright (c) 2013年 walkerfree. All rights reserved.
//

#import "testRefreshViewViewController.h"

@interface testRefreshViewViewController ()

@end

@implementation testRefreshViewViewController

@synthesize scrollView = _scrollView;

#pragma RefreshView
-(void) startLoading
{
    [refreshView startLoading];
    //模拟3秒钟后停止
    [self performSelector:@selector(stopLoading) withObject:nil afterDelay:3];
}

-(void) stopLoading
{
    [refreshView stopLoading];
}

-(void) refresh
{
    [self startLoading];
}

//刚拖动的时候
- (void)scrollViewWillBeginDragging:(UIScrollView *)scrollView_
{
    [refreshView scrollViewWillBeginDragging:scrollView_];
}

//拖动过程中
-(void) scrollViewDidScroll:(UIScrollView *)scrollView_
{
    [refreshView scrollViewDidScroll:scrollView_];
}

//拖动结束后
- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView_ willDecelerate:(BOOL)decelerate
{
    NSLog(@"here");
    [refreshView scrollViewDidEndDragging:scrollView_ willDecelerate:decelerate];
}

#pragma mark - RefreshViewDelegate
- (void)refreshViewDidCallBack {
    [self refresh];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
	NSArray *nils = [[NSBundle mainBundle] loadNibNamed:@"RefreshView" owner:self options:nil];
    refreshView = [nils objectAtIndex:0];
    _scrollView.contentSize = CGSizeMake(320, 460);
    _scrollView.contentInset = UIEdgeInsetsMake(REFRESH_HEADER_HEIGHT, 0, 0, 0);
//    _scrollView.backgroundColor = [UIColor blueColor];
    
    [refreshView setupWithOwner:_scrollView delegate:self];
    [self refresh];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

//-(void) start

@end
```

里面有个文件是：

RefreshView.h

这个文件来自于cocoachina，地址：~http://www.cocoachina.com/bbs/read.php?tid=90232&fpage=3~

需要的可以自己去下载一下
