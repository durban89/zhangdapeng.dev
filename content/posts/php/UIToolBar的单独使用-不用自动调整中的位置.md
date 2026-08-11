---
title: "UIToolBar的单独使用-不用自动调整中的位置"
date: "2025-06-17 16:45:39"
slug: "uitoolbar-de-dan-du-shi-yong-bu-yong-zi-dong-tiao-zheng-zhong-de-wei-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/UIToolBar的单独使用-不用自动调整中的位置/"
  - "/2025/06/17/UIToolBar的单独使用-不用自动调整中的位置.html"
  - "/UIToolBar的单独使用-不用自动调整中的位置/"
  - "/UIToolBar的单独使用-不用自动调整中的位置.html"
  - "/2025/06/17/uitoolbar-de-dan-du-shi-yong-bu-yong-zi-dong-tiao-zheng-zhong-de-wei-zhi/"
  - "/2025/06/17/uitoolbar-de-dan-du-shi-yong-bu-yong-zi-dong-tiao-zheng-zhong-de-wei-zhi.html"
  - "/uitoolbar-de-dan-du-shi-yong-bu-yong-zi-dong-tiao-zheng-zhong-de-wei-zhi.html"
---
直接上代码：

```objectivec
//
//  TWFXToolBarViewController.m
//  DemoToolBar
//
//  Created by Lion User on 13-1-19.
//  Copyright (c) 2013年 Lion User. All rights reserved.
//

#import "TWFXToolBarViewController.h"

@interface TWFXToolBarViewController ()

@end

@implementation TWFXToolBarViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil{
self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
	if (self) {
		// Custom initialization

		//创建toolbar
		UIToolbar *toolBar = [[[UIToolbar alloc] initWithFrame:CGRectMake(0.0f, 420.0f, 320.0f, 40.0f) ] autorelease];

		//创建barbuttonitem
		UIBarButtonItem *item1 = [[[UIBarButtonItem alloc] initWithTitle:@"收藏" style:UIBarButtonItemStyleBordered target:self action:@selector(test:)] autorelease];

		//创建barbuttonitem
		UIBarButtonItem *item2 = [[[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemBookmarks target:self action:nil] autorelease];

		//创建一个segmentController
		UISegmentedControl *seg = [[[UISegmentedControl alloc] initWithItems:[NSArray arrayWithObjects:@"牛扒", @"排骨", nil] ] autorelease];

		//设置style
		[seg setSegmentedControlStyle:UISegmentedControlSegmentCenter];


		[seg addTarget:self action:@selector(segmentControllerItem:) forControlEvents:UIControlEventValueChanged];

		//创建一个内容是view的uibarbuttonitem
		UIBarButtonItem *itemSeg = [[[UIBarButtonItem alloc] initWithCustomView:seg] autorelease];

		//创建barbuttonitem,样式是flexible,这个种barbuttonitem用于两个barbuttonitem之间
		//调整两个item之间的距离.flexible表示距离是动态的,fixed表示是固定的
		UIBarButtonItem *flexible = [[[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemFlexibleSpace target:self action:nil] autorelease];

		//把item添加到toolbar里
		[toolBar setItems:[NSArray arrayWithObjects:item1,flexible,itemSeg,flexible,item2, nil] animated:YES];

		//把toolbar添加到view上
		[self.view addSubview:toolBar];

	}
	return self;
}

- (void)viewDidLoad
{
	[super viewDidLoad];
	// Do any additional setup after loading the view from its nib.
}

-(void)test:(id)sender
{
	UIBarButtonItem *item = (UIBarButtonItem *) sender;
	NSString *title = [NSString stringWithFormat:@"%@ 被选中了",item.title];

	UIAlertView *alertView = [[[UIAlertView alloc] initWithTitle:@"Attention" message:title delegate:self cancelButtonTitle:@"ok" otherButtonTitles:nil, nil] autorelease];

	[alertView show];
}


-(void)segmentControllerItem:(id)sender
{
	UISegmentedControl *seg = (UISegmentedControl *) sender;
	NSInteger index = seg.selectedSegmentIndex;
	NSString *message;
	if (index == 0) {
		message = @"你选了牛扒";
	}
	else
	{
		message = @"你选了排骨";
	}

	UIAlertView *alertView = [[[UIAlertView alloc] initWithTitle:@"Attenton" message:message delegate:self cancelButtonTitle:@"OK" otherButtonTitles:nil, nil] autorelease];

	[alertView show];
}

- (void)didReceiveMemoryWarning
{
	[super didReceiveMemoryWarning];
	// Dispose of any resources that can be recreated.
}

- (IBAction)goBack:(UIButton *)sender {
	[self dismissViewControllerAnimated:YES completion:nil];
}
@end
```

自己实践测试过了。效果很不错，在我之前做的和现在比的话，关键一点是“`[toolBar setItems:[NSArray arrayWithObjects:item1,flexible,itemSeg,flexible,item2, nil] animated:YES];`”这里很重要，使得自己不用去通过CGRectMake来设置。

也许你有个问题是我想使用UIButton，好的你跟我的想法是一样的，我贴一帖我的代码好了：

```objectivec
-(void) showEditBar{
    //创建toolbar
    CGRect screenRect = [[UIScreen mainScreen] bounds];
    CGFloat toolbarWidth = 200.0;
    CGFloat toolbarHeight = 45.0;
    CGFloat toolbarMarginBottom = 10.0;
    CGFloat toolbarX = (screenRect.size.width - toolbarWidth) / 2;
    CGFloat toolbarY = (screenRect.size.height - toolbarMarginBottom - toolbarHeight) - 2 * 44.0 - 22.0;
    
    _editToolBar = [[DeleteToolBar alloc] initWithFrame:CGRectMake(toolbarX, toolbarY, toolbarWidth, toolbarHeight)];
    _editToolBar.barStyle = UIBarStyleDefault;
    _editToolBar.translucent = YES;
    
    UIButton *deleteBar = [[UIButton alloc] initWithFrame:CGRectMake(0.0, 0.0, toolbarWidth/2, _editToolBar.frame.size.height)];
    deleteBar.titleLabel.font = [UIFont systemFontOfSize:24.0];
    deleteBar.layer.backgroundColor = [[ColorConfig NavigationColor] CGColor];
    deleteBar.layer.borderWidth = 2.0;
    deleteBar.layer.borderColor = [[ColorConfig NavigationColor] CGColor];
    deleteBar.layer.cornerRadius = 10.0;
    deleteBar.alpha = 1.0;

    [deleteBar setTitle:@"删除" forState:UIControlStateNormal];
    [deleteBar addTarget:self action:@selector(deleteAction:) forControlEvents:UIControlEventTouchUpInside];
    UIBarButtonItem *deleteBarBtn = [[UIBarButtonItem alloc] initWithCustomView:deleteBar];
    
    //创建barbuttonitem,样式是flexible,这个种barbuttonitem用于两个barbuttonitem之间
    //调整两个item之间的距离.flexible表示距离是动态的,fixed表示是固定的
    UIBarButtonItem *flexible = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemFlexibleSpace target:self action:nil];
    
    //把item添加到toolbar里
    [_editToolBar setItems:[NSArray arrayWithObjects:flexible,deleteBarBtn,flexible, nil] animated:YES];
    
    //把toolbar添加到view上
    [self.view addSubview:_editToolBar];

    //设置table的位置
    [self.dataTable setFrame:CGRectMake(0.0, 0.0, self.view.frame.size.width, TABLE_VIEW_HEIGHT - COMPARE_BAR_HEIGHT - 8.0)];
}
```

参考文章：http://www.cnblogs.com/zouzf/archive/2013/01/19/2867574.html
