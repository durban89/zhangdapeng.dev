---
title: "UITableView下拉刷新功能，完成"
date: "2025-06-17 11:59:46"
slug: "uitableview-xia-la-shua-xin-gong-neng-wan-cheng"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/UITableView下拉刷新功能，完成/"
  - "/2025/06/17/UITableView下拉刷新功能，完成.html"
  - "/UITableView下拉刷新功能，完成/"
  - "/UITableView下拉刷新功能，完成.html"
  - "/2025/06/17/UITableView下拉刷新功能-完成/"
  - "/2025/06/17/UITableView下拉刷新功能-完成.html"
  - "/2025/06/17/uitableview-xia-la-shua-xin-gong-neng-wan-cheng/"
  - "/2025/06/17/uitableview-xia-la-shua-xin-gong-neng-wan-cheng.html"
  - "/uitableview-xia-la-shua-xin-gong-neng-wan-cheng.html"
---
看了几个实例，最终解决了这个问题，之间为什么老是有问题没有解决呢，原因我觉得是跟ARC有关，因为我的应用是使用ARC的然后将下载回来的代码进行了调整，将release的代码段去掉了。结果有了一些问题，也不是很了解具体是哪里。目前问题解决了，里面使用了关于ARC机制和非ARC机制共存的办法,详细的内容可以参考我的这篇文章[iOS 开发，工程中混合使用 ARC 和非ARC](http://gowhich.com/blog/191)。

代码段贴一下好了：

EGOTableViewPullRefresh的下载地址：<http://vdisk.weibo.com/s/FtH88>

indexViewController.h

```objectivec
//
//  indexViewController.h
//  index
//
//  Created by david on 13-6-8.
//  Copyright (c) 2013年 walkerfree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "EGORefreshTableHeaderView.h"

@interface indexViewController : UIViewController<UITableViewDataSource, UITableViewDelegate, UISearchBarDelegate, EGORefreshTableHeaderDelegate>
{
    EGORefreshTableHeaderView *_refreshHeaderView;
    BOOL _reloading;
}
@property (strong, nonatomic) IBOutlet UISearchBar *personSearch;
@property (strong, nonatomic) IBOutlet UITableView *dataTable;
@property (strong, nonatomic) NSMutableDictionary *dataDic;

-(void) initPersonIndexListData;
@end
```

indexViewController.m

```objectivec
//
//  indexViewController.m
//  index
//
//  Created by david on 13-6-8.
//  Copyright (c) 2013年 walkerfree. All rights reserved.
//

#import "indexViewController.h"
#import "personIndexTrendViewController.h"
#import "listCell.h"

@interface indexViewController ()

@end

@implementation indexViewController

@synthesize personSearch = _personSearch;
@synthesize dataTable = _dataTable;
@synthesize dataDic = _dataDic;

- (void)viewDidLoad
{
    [super viewDidLoad];
    [self initPersonIndexListData];
    self.dataTable.delegate = self;
    self.dataTable.dataSource = self;
    
    if (_refreshHeaderView == nil) {
        //初始化下拉刷新控件
        _refreshHeaderView = [[EGORefreshTableHeaderView alloc] init];
        _refreshHeaderView.delegate = self;
        //将下拉刷新控件作为子控件添加到UITableView中
        [self.dataTable addSubview:_refreshHeaderView];
    }
    
    
    [_refreshHeaderView refreshLastUpdatedDate];
    
}

-(void) startLoadingTableViewData
{
    [self initPersonIndexListData];
    _reloading = YES;
}

-(void) endLoadingTableViewData
{
    _reloading = NO;
    [_refreshHeaderView egoRefreshScrollViewDataSourceDidFinishedLoading:self.dataTable];
//    NSLog(@"done");
}

#pragma mark -
#pragma mark UIScrollViewDelegate Methods
-(void) scrollViewDidScroll:(UIScrollView *)scrollView
{
    [_refreshHeaderView egoRefreshScrollViewDidScroll:scrollView];
}

-(void) scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate
{
    [_refreshHeaderView egoRefreshScrollViewDidEndDragging:scrollView];
}

-(void)scrollViewDidEndScrollingAnimation:(UIScrollView *)scrollView
{
    [_refreshHeaderView egoRefreshScrollViewDidEndDragging:scrollView];
}

#pragma mark -
#pragma mark EGORefreshTableHeaderDelegate Methods
-(void) egoRefreshTableHeaderDidTriggerRefresh:(EGORefreshTableHeaderView *)view
{
    [self startLoadingTableViewData];
    [self performSelector:@selector(endLoadingTableViewData) withObject:nil afterDelay:3.0];
}

-(BOOL) egoRefreshTableHeaderDataSourceIsLoading:(EGORefreshTableHeaderView *)view
{
    return _reloading;
}

-(NSDate *)egoRefreshTableHeaderDataSourceLastUpdated:(EGORefreshTableHeaderView *)view
{
    return [NSDate date];
}



-(void) viewWillDisappear:(BOOL)animated
{
    UIBarButtonItem *returnBarItem = [[UIBarButtonItem alloc] init];
    returnBarItem.title = @"返回";
    self.navigationItem.backBarButtonItem = returnBarItem;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma UITableView
-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [self.dataDic count];
}

-(NSInteger) numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}

-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *listCellIdentifier = @"listCell";
    
    UINib *nib = [UINib nibWithNibName:@"listCell" bundle:nil];
    [self.dataTable registerNib:nib forCellReuseIdentifier:listCellIdentifier];
    
    listCell *cell = [tableView dequeueReusableCellWithIdentifier:listCellIdentifier];
    if(cell == nil){
        cell = [[listCell alloc]initWithStyle:UITableViewCellStyleDefault
                              reuseIdentifier:listCellIdentifier];
        
    }
    
    NSDictionary *dic = [self.dataDic objectForKey:[NSString stringWithFormat:@"%d",[indexPath row]]];
    
    cell.personRank.text = [NSString stringWithFormat:@"%d",[indexPath row] + 1];
    cell.personName.text = [dic valueForKey:@"zh_name"];
    cell.personIndex.text = [NSString stringWithFormat:@"艺人新媒体指数 %0.2f",[[dic valueForKey:@"score"] floatValue]];
    cell.personIndex.font = [UIFont systemFontOfSize:14.0];
    cell.personIndex.textColor = [UIColor lightGrayColor];
    
    if([[NSString stringWithFormat:@"%u",[indexPath row]] isEqualToString:@"0"])
    {
        cell.personRank.backgroundColor = [UIColor greenColor];
    }
    else
    {
        cell.personRank.backgroundColor = [UIColor lightGrayColor];
    }
    
    if([[NSString stringWithFormat:@"%u",[indexPath row]] isEqualToString:@"1"])
    {
        cell.personRank.backgroundColor = [UIColor greenColor];
    }
    
    if([[NSString stringWithFormat:@"%u",[indexPath row]] isEqualToString:@"2"])
    {
        cell.personRank.backgroundColor = [UIColor greenColor];
    }
    
    
    
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    
    return cell;
}

-(void) tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    NSDictionary *dic = [self.dataDic valueForKey:[NSString stringWithFormat:@"%u",[indexPath row]]];
    personIndexTrendViewController *trend = [[personIndexTrendViewController alloc] initWithNibName:@"personIndexTrendViewController"
                                                                            bundle:nil];
    trend.personInfo = [dic mutableCopy];
    [self.navigationController pushViewController:trend animated:YES];
    
}

#pragma UISearchBar


#pragma 自定义函数
-(void)initPersonIndexListData
{
    NSLog(@"加载数据");
    [UIApplication sharedApplication].networkActivityIndicatorVisible = YES;
    NSDate *date = [NSDate date];
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd"];
    
    NSString *dateString = [dateFormatter stringFromDate: [NSDate dateWithTimeInterval:-(2 * 24 * 60 * 60) sinceDate:date]];
    
    NSString *urlString = @"http://XXXXXXXXX.XXX.XXX.XXX?";
    
    NSURL *url = [[NSURL alloc] initWithString:urlString];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestUseProtocolCachePolicy
                                              timeoutInterval:60];
    
    NSURLResponse *response = [[NSURLResponse alloc] init];
    NSError *receiveDataError = [[NSError alloc] init];
    
    NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request
                                                                         returningResponse:&response
                                                                                     error:&receiveDataError];
    
    if(receivedData == nil)
    {
        NSLog(@"获取数据失败");
    }
    else
    {    
        NSError *jsonError = [[NSError alloc] init];
        NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                         options:NSJSONReadingMutableContainers
                                                                           error:&jsonError];
        NSMutableDictionary *personInfo = [personDictionary objectForKey:@"data"];
        
        NSMutableDictionary *personList = [personInfo objectForKey:@"list"];
        
        self.dataDic = [NSMutableDictionary dictionaryWithCapacity:20];
        
        if([personList isKindOfClass:[NSMutableArray class]])
        {
            int i = 0;
            for (NSDictionary *dic in personList) {
                [self.dataDic setObject:dic forKey:[NSString stringWithFormat:@"%d",i]];
                i++;
            }
        }
        
        
        
        if([personList isKindOfClass:[NSMutableDictionary class]])
        {
            NSLog(@"NSMutableDictionary 类");
        }
        
        if([self.dataDic count] > 0)
        {
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
        }
    }
}
@end
```
