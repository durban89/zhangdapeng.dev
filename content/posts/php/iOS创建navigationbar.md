---
title: "iOS创建navigationbar"
date: "2025-06-06 11:44:14"
slug: "ios-chuang-jian-navigationbar"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS创建navigationbar/"
  - "/2025/06/06/iOS创建navigationbar.html"
  - "/iOS创建navigationbar/"
  - "/iOS创建navigationbar.html"
  - "/2025/06/06/ios-chuang-jian-navigationbar/"
  - "/2025/06/06/ios-chuang-jian-navigationbar.html"
  - "/ios-chuang-jian-navigationbar.html"
---
使用代码创建自己的navigationbar：

环境:

```shell
xcode:Version 4.6.1 (4H512)

simulater:iPhone6.1
```

直接上代码：

```c MasterViewController.h

//
//  MasterViewController.h
//  vlinkagePerson
//
//  Created by david on 13-4-14.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface MasterViewController : UIViewController

//导航栏
@property (strong, nonatomic) UINavigationBar *navbar;
//导航栏集合
@property (strong, nonatomic) UINavigationItem *navItem;
//左边按钮
@property (strong, nonatomic) UIBarButtonItem *searchButton;
//右边按钮
@property (strong, nonatomic) UIBarButtonItem *attentionButton;

//自定义方法
//搜索操作
-(void) searchEvent;
-(void) attentionList;

@end
```

```c MasterViewController.m

//
//  MasterViewController.m
//  vlinkagePerson
//
//  Created by david on 13-4-14.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "MasterViewController.h"

@interface MasterViewController ()

@end

@implementation MasterViewController

@synthesize navbar,navItem,searchButton,attentionButton;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    
    //创建一个导航栏
    self.navbar = [[UINavigationBar alloc] initWithFrame:CGRectMake(0, 0, 320, 44)];
    
    //创建一个导航栏集合
    self.navItem = [[UINavigationItem alloc] initWithTitle:@"艺人列表"];
    
    //在这个集合Item中添加标题，按钮
    //style:设置按钮的风格，一共有三种选择
    //action：@selector:设置按钮的点击事件
    //创建一个左边按钮
    self.searchButton = [[UIBarButtonItem alloc] initWithTitle:@"搜索" style:UIBarButtonItemStylePlain target:self action:@selector(searchEvent)];
    
    //创建一个右边按钮
    self.attentionButton = [[UIBarButtonItem alloc] initWithTitle:@"我的关注" style:UIBarButtonItemStylePlain target:self action:@selector(attentionList)];

    //把导航栏集合添加到导航栏中，设置动画关闭
    [self.navbar pushNavigationItem:self.navItem animated:YES];
    
    //把左右两个按钮添加到导航栏集合中去
    [self.navItem setLeftBarButtonItem:self.searchButton];
    [self.navItem setRightBarButtonItem:self.attentionButton];
    
    //将标题栏中的内容全部添加到主视图当中
    [self.view addSubview:self.navbar];
    
}

-(void) searchEvent{
    
}

-(void) attentionList{
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
 
```
