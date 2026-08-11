---
title: "iOS开发之表格排序（UITableView排序）"
date: "2025-06-20 11:07:31"
slug: "ios-kai-fa-zhi-biao-ge-pai-xu-uitableview-pai-xu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS开发之表格排序（UITableView排序）/"
  - "/2025/06/20/iOS开发之表格排序（UITableView排序）.html"
  - "/iOS开发之表格排序（UITableView排序）/"
  - "/iOS开发之表格排序（UITableView排序）.html"
  - "/2025/06/20/iOS开发之表格排序-UITableView排序/"
  - "/2025/06/20/iOS开发之表格排序-UITableView排序.html"
  - "/2025/06/20/ios-kai-fa-zhi-biao-ge-pai-xu-uitableview-pai-xu/"
  - "/2025/06/20/ios-kai-fa-zhi-biao-ge-pai-xu-uitableview-pai-xu.html"
  - "/ios-kai-fa-zhi-biao-ge-pai-xu-uitableview-pai-xu.html"
---
关于表格的排序是使用了NSComparisonResult这个方法，很简单的，只要自己定义几个方法，就可以了

代码：

```objectivec
@interface NSString (sortingExtension)

@end

@implementation NSString (sortingExtension)
- (NSComparisonResult) reverseCompare: (NSString *) aString
{
	return -1 * [self caseInsensitiveCompare:aString];
}

- (NSComparisonResult) lengthCompare: (NSString *) aString
{
	if (self.length == aString.length) return NSOrderedSame;
	if (self.length > aString.length) return NSOrderedDescending;
	return NSOrderedAscending;
}
@end
```

自己写个方法，然后封装到里面就好了,关于NSString (sortingExtension)这个名字，没研究出啥道道来，只是觉得奇怪

我迫于喜欢IOS5的storyboard，于是此篇也是用了storyboard

SortTableViewController.h

```objectivec
//
//  SortTableViewController.h
//  SortTable
//
//  Created by david on 13-8-7.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

#define COOKBOOK_PURPLE_COLOR	[UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]
#define BARBUTTON(TITLE, SELECTOR) 	[[[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR] autorelease]
#define SYSBARBUTTON(ITEM, SELECTOR) [[[UIBarButtonItem alloc] initWithBarButtonSystemItem:ITEM target:self action:SELECTOR] autorelease]
#define CRAYON_NAME(CRAYON)	[[CRAYON componentsSeparatedByString:@"#"] objectAtIndex:0]
#define CRAYON_COLOR(CRAYON) [self getColor:[[CRAYON componentsSeparatedByString:@"#"] lastObject]]


@interface NSString (sortingExtensionFF)

@end

@implementation NSString (sortingExtensionFF)
- (NSComparisonResult) reverseCompare: (NSString *) aString
{
	return -1 * [self caseInsensitiveCompare:aString];
}

- (NSComparisonResult) lengthCompare: (NSString *) aString
{
	if (self.length == aString.length) return NSOrderedSame;
	if (self.length > aString.length) return NSOrderedDescending;
	return NSOrderedAscending;
}
@end


@interface SortTableViewController : UIViewController<UITableViewDataSource, UITableViewDelegate>
@property (strong, nonatomic) IBOutlet UITableView *tableView;

@property (retain) NSArray *items;

@end
```

SortTableViewController.m

```objectivec
//
//  SortTableViewController.m
//  SortTable
//
//  Created by david on 13-8-7.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "SortTableViewController.h"

@interface SortTableViewController ()

@end

@implementation SortTableViewController

@synthesize items;
@synthesize tableView;

- (void)viewDidLoad
{
    [super viewDidLoad];
    self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    
    self.tableView.delegate = self;
    self.tableView.dataSource = self;
    
    NSError *error;
    NSString *pathname = [[NSBundle mainBundle]  pathForResource:@"content" ofType:@"text"];

	self.items = [[NSString stringWithContentsOfFile:pathname
                                            encoding:NSUTF8StringEncoding
                                               error:&error] componentsSeparatedByString:@"\n"];
    
	UISegmentedControl *seg = [[UISegmentedControl alloc] initWithItems:[@"Ascending Descending Length" componentsSeparatedByString:@" "]];
	seg.segmentedControlStyle = UISegmentedControlStyleBar;
	seg.selectedSegmentIndex = 0;
	[seg addTarget:self action:@selector(updateSort:) forControlEvents:UIControlEventValueChanged];
	self.navigationItem.titleView = seg;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - UITableViewCell Method
- (NSInteger)numberOfSectionsInTableView:(UITableView *)aTableView
{
	return 1;
}

- (NSInteger)tableView:(UITableView *)aTableView numberOfRowsInSection:(NSInteger)section
{
	return items.count;
}

- (UITableViewCell *)tableView:(UITableView *)tView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
	UITableViewCellStyle style =  UITableViewCellStyleDefault;
	UITableViewCell *cell = [tView dequeueReusableCellWithIdentifier:@"BaseCell"];
	if (!cell) cell = [[UITableViewCell alloc] initWithStyle:style reuseIdentifier:@"BaseCell"];
	NSString *crayon = [items objectAtIndex:indexPath.row];
	cell.textLabel.text = CRAYON_NAME(crayon);
	if (![CRAYON_NAME(crayon) hasPrefix:@"White"])
		cell.textLabel.textColor = CRAYON_COLOR(crayon);
	else
		cell.textLabel.textColor = [UIColor blackColor];
	return cell;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
	NSString *crayon = [self.items objectAtIndex:indexPath.row];
	self.navigationController.navigationBar.tintColor = CRAYON_COLOR(crayon);
}

- (void) updateSort: (UISegmentedControl *) seg
{
	if (seg.selectedSegmentIndex == 0)
		self.items = [self.items sortedArrayUsingSelector:@selector(caseInsensitiveCompare:)];
	else if (seg.selectedSegmentIndex == 1)
		self.items = [self.items sortedArrayUsingSelector:@selector(reverseCompare:)];
	else if (seg.selectedSegmentIndex == 2)
		self.items = [self.items sortedArrayUsingSelector:@selector(lengthCompare:)];
    
	[self.tableView reloadData];
}



- (UIColor *) getColor: (NSString *) hexColor
{
	unsigned int red, green, blue;
	NSRange range;
	range.length = 2;
    
	range.location = 0;
	[[NSScanner scannerWithString:[hexColor substringWithRange:range]] scanHexInt:&red];
	range.location = 2;
	[[NSScanner scannerWithString:[hexColor substringWithRange:range]] scanHexInt:&green];
	range.location = 4;
	[[NSScanner scannerWithString:[hexColor substringWithRange:range]] scanHexInt:&blue];
    
	return [UIColor colorWithRed:(float)(red/255.0f) green:(float)(green/255.0f) blue:(float)(blue/255.0f) alpha:1.0f];
}

@end
```

以上代码绝对支持ARC,时代是新的，代码的创新，跟着创新走吧，别烦恼更新太快，为了项目的最新，为了能够展示更好的项目，更新并不是什么坏事。
