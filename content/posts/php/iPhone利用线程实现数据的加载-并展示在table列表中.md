---
title: "iPhone利用线程实现数据的加载，并展示在table列表中"
date: "2025-06-17 14:43:30"
slug: "iphone-li-yong-xian-cheng-shi-xian-shu-ju-de-jia-zai-bing-zhan-shi-zai-table-lie-biao-zhong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iPhone利用线程实现数据的加载，并展示在table列表中/"
  - "/2025/06/17/iPhone利用线程实现数据的加载，并展示在table列表中.html"
  - "/iPhone利用线程实现数据的加载，并展示在table列表中/"
  - "/iPhone利用线程实现数据的加载，并展示在table列表中.html"
  - "/2025/06/17/iPhone利用线程实现数据的加载-并展示在table列表中/"
  - "/2025/06/17/iPhone利用线程实现数据的加载-并展示在table列表中.html"
  - "/2025/06/17/iphone-li-yong-xian-cheng-shi-xian-shu-ju-de-jia-zai-bing-zhan-shi-zai-table-lie-biao-z/"
  - "/2025/06/17/iphone-li-yong-xian-cheng-shi-xian-shu-ju-de-jia-zai-bing-zhan-shi-zai-table-lie-bi.html"
  - "/iphone-li-yong-xian-cheng-shi-xian-shu-ju-de-jia-zai-bing-zhan-shi-zai-table-lie-biao-zhong.html"
---
实现的过程是修改两个table 的controller类，修改方法如下：

```objectivec
#import <UIKit/UIKit.h>
@interface WelcomePavilionViewController : UIViewController
<UITableViewDelegate,UITableViewDataSource>
{
	NSMutableArray  *array;
	IBOutlet UITableView *tableView;
}
@property (nonatomic,retain) NSMutableArray  *array;
@property (nonatomic,retain) UITableView *tableView;
@end
```

实现方法是：

```objectivec
#import “WelcomePavilionViewController.h”
#import “XmlWelcome.h”
@implementation WelcomePavilionViewController
@synthesize array,tableView;
- (void)viewDidLoad {
	[super viewDidLoad];
}
- (void)viewWillAppear:(BOOL)animated {
	if ([self.array count]==0) {
		[NSThread detachNewThreadSelector:@selector(myTaskMethod) toTarget:self withObject:nil];
	}
}
-(void)myTaskMethod
{
	NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
	XmlWelcome *parser=[[XmlWelcome alloc]
	initWithContentsOfURL:[NSURL URLWithString:@"http://mp.myvsp.cn/welcomedemos/getpavilionxml.json?area=a&width=80&height=80&digest_length=20" ]];
	//设置代理
	[parser setDelegate:parser];
	[parser parse];
	self.array=parser.ones;
	[self.tableView reloadData];
	[parser  release];
	[pool release];

}
- (void)didReceiveMemoryWarning {
	// Releases the view if it doesn’t have a superview.
	[super didReceiveMemoryWarning];
	// Release any cached data, images, etc that aren’t in use.
}

- (void)viewDidUnload {
	self.array=nil;
	self.tableView=nil;
}
- (void)dealloc {
	[self.tableView release];
	[self.array release];
	[super dealloc];
}

- (NSInteger)tableView:(UITableView *)tableView
	numberOfRowsInSection:(NSInteger)section {
	return [array count];
}
- (UITableViewCell *)tableView:(UITableView *)tableView
cellForRowAtIndexPath:(NSIndexPath *)indexPath {
	UITableViewCell* cell = [tableView dequeueReusableCellWithIdentifier:@"tag"];
	if (cell==nil) {
		cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle
		reuseIdentifier:@”tag”] autorelease];
	}
	//表格设计
	NSDictionary* one = [array objectAtIndex:indexPath.row];
	cell.textLabel.text = [one objectForKey:@"title"];
	cell.detailTextLabel.text = [one objectForKey:@"content"];
	id path = [one objectForKey:@"image"];
	NSURL *url = [NSURL URLWithString:path];
	NSData *data = [NSData dataWithContentsOfURL:url];
	UIImage *image = [[UIImage alloc] initWithData:data cache:NO];
	cell.image=image;
	[image release];
	return cell;
}
- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section
{
	return @”Hobby Information:”;
}
@end
```


这里总结一下，关键的总结点是这里

```objectivec
- (void)viewWillAppear:(BOOL)animated {
	if ([self.array count]==0) {
		[NSThread detachNewThreadSelector:@selector(myTaskMethod) toTarget:self withObject:nil];
	}
}
```

然后再在自己的调用方法里面调用**`[self.tableView reloadData];`这个方法**
