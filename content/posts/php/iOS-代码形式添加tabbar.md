---
title: "iOS 代码形式添加tabbar"
date: "2025-06-12 09:34:25"
slug: "ios-dai-ma-xing-shi-tian-jia-tabbar"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-代码形式添加tabbar/"
  - "/2025/06/12/iOS-代码形式添加tabbar.html"
  - "/iOS-代码形式添加tabbar/"
  - "/iOS-代码形式添加tabbar.html"
  - "/2025/06/12/ios-dai-ma-xing-shi-tian-jia-tabbar/"
  - "/2025/06/12/ios-dai-ma-xing-shi-tian-jia-tabbar.html"
  - "/ios-dai-ma-xing-shi-tian-jia-tabbar.html"
---
可以直接看代码，可以直接复制，自己运行：

VlinkageViewController.h(实现UITabBarDelegate)

```objectivec VlinkageViewController.h
//
//  VlinkageViewController.h
//  xunYi
//
//  Created by david on 13-5-3.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface VlinkageViewController : UIViewController<UITabBarDelegate>

@property (nonatomic, retain) UITabBar *tabBar;

@end
```

VlinkageViewController.m（关键一点是要实现[self.tabBar setDelegate:self]，不然不起作用的）

```objectivec VlinkageViewController.m
//
//  VlinkageViewController.m
//  xunYi
//
//  Created by david on 13-5-3.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <QuartzCore/QuartzCore.h>
#import "VlinkageViewController.h"

@interface VlinkageViewController ()


@end

@implementation VlinkageViewController

@synthesize tabBar;

- (void)viewDidLoad
{
    [super viewDidLoad];
    //判断机体的宽度和高度
    CGRect screenBounds = [[UIScreen mainScreen] bounds];
    CGFloat width = screenBounds.size.width;
    CGFloat height = screenBounds.size.height;
#pragma 添加tabBar
    CGFloat tabBarHeight = 40;
    CGFloat tabBarY = height  - tabBarHeight - searchBar.frame.size.height / 2;
    self.tabBar = [[UITabBar alloc] initWithFrame:
                          CGRectMake(0, tabBarY, width, tabBarHeight)];
    [self.tabBar setDelegate:self];
    
    //设置切换title
    UITabBarItem *tabBarItem1 = [[UITabBarItem alloc] initWithTitle:@"查找" image:nil tag:0];
    UITabBarItem *tabBarItem2 = [[UITabBarItem alloc] initWithTitle:@"我的关注" image:nil tag:1];
    UITabBarItem *tabBarItem3 = [[UITabBarItem alloc] initWithTitle:@"咨询" image:nil tag:2];
    UITabBarItem *tabBarItem4 = [[UITabBarItem alloc] initWithTitle:@"更多" image:nil tag:3];

    NSLog(@"tabBarItem1.tag = %d",tabBarItem1.tag);
    NSLog(@"tabBarItem1.tag = %d",tabBarItem2.tag);
    NSLog(@"tabBarItem1.tag = %d",tabBarItem3.tag);
    NSLog(@"tabBarItem1.tag = %d",tabBarItem4.tag);
    
    //数组形式添加进 tabBar
    NSArray *tabBarItemArray = [[NSArray alloc]
                                initWithObjects:tabBarItem1, tabBarItem2, tabBarItem3, tabBarItem4, nil];
    [self.tabBar setItems:tabBarItemArray];
    [self.view addSubview:self.tabBar];
    
}

-(void) tabBar:(UITabBar *)tabBar didSelectItem:(UITabBarItem *)item
{
    NSLog(@"item.tag= %d", item.tag);
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
@end
```
