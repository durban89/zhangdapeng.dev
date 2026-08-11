---
title: "iOS uitableview uitableviewcell简单举例"
date: "2025-06-06 18:04:09"
slug: "ios-uitableview-uitableviewcell-jian-dan-ju-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS-uitableview-uitableviewcell简单举例/"
  - "/2025/06/06/iOS-uitableview-uitableviewcell简单举例.html"
  - "/iOS-uitableview-uitableviewcell简单举例/"
  - "/iOS-uitableview-uitableviewcell简单举例.html"
  - "/2025/06/06/ios-uitableview-uitableviewcell-jian-dan-ju-li/"
  - "/2025/06/06/ios-uitableview-uitableviewcell-jian-dan-ju-li.html"
  - "/ios-uitableview-uitableviewcell-jian-dan-ju-li.html"
---
我学过网页制作，多多少少的能理解一下table这个元素，关于ios的uitableview应该也有这些类似的东西，觉得在uitableview中，都能够找与table对应的部分，看下面代码：

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

@synthesize navbar,navItem,searchButton,attentionButton,personTable,keys,objects,content;

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
    self.keys = [NSArray arrayWithObjects:@"mainTitleKey",@"secondaryTitleKey",@"imageKey",nil];
    self.objects = [NSArray arrayWithObjects:@"How",@"Are",@"You",nil];
    
    //表格添加内容
    self.content = [[NSDictionary alloc] initWithObjects:objects forKeys:keys];
    
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
    
    
    
    //添加UITableView
    self.personTable = [[UITableView alloc] initWithFrame:CGRectMake(0, 44, 320, 460)
                                                      style:UITableViewStyleGrouped];
    [self.personTable setDataSource:self];
    [self.personTable setDelegate:self];
    
    //将标题栏中的内容全部添加到主视图当中
    [self.view addSubview:self.navbar];
    //将表格添加到主视图中
    [self.view addSubview:self.personTable];
    
}

-(void) searchEvent{
    
}

-(void) attentionList{
    
}
//Section总数
- (NSArray *)sectionIndexTitlesForTableView:(UITableView *)tableView{
    return self.objects;
}

//每个section显示的标题
//设置caption
- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section{
    return @"大家好";
}


//指定有多少个分区(Section)，默认为1
//需要多少个table
-(NSInteger) numberOfSectionsInTableView:(UITableView *)tableView{
    return 4;
}

//指定每个分区中有多少行，默认为1
//table的行数
-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
    return 2;
}

//绘制Cell
//为每个表格赋值
-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath{
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyIdentifier"];
    
    if (cell == nil) {
        
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"MyIdentifier"];
        
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
        
    }
    
    cell.textLabel.text = [self.content objectForKey:@"mainTitleKey"];
    
    cell.detailTextLabel.text = [self.content objectForKey:@"secondaryTitleKey"];
    
    NSString *path = [[NSBundle mainBundle] pathForResource:[self.content objectForKey:@"imageKey"] ofType:@"png"];
    
    UIImage *theImage = [UIImage imageWithContentsOfFile:path];
    
    cell.imageView.image = theImage;
    
    
    return cell;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
 
```
