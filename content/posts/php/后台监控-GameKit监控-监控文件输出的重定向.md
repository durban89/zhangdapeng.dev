---
title: "后台监控 GameKit监控 监控文件输出的重定向"
date: "2025-06-20 14:33:59"
slug: "hou-tai-jian-kong-gamekit-jian-kong-jian-kong-wen-jian-shu-chu-de-zhong-ding-xiang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/后台监控-GameKit监控-监控文件输出的重定向/"
  - "/2025/06/20/后台监控-GameKit监控-监控文件输出的重定向.html"
  - "/后台监控-GameKit监控-监控文件输出的重定向/"
  - "/后台监控-GameKit监控-监控文件输出的重定向.html"
  - "/2025/06/20/hou-tai-jian-kong-gamekit-jian-kong-jian-kong-wen-jian-shu-chu-de-zhong-ding-xiang/"
  - "/2025/06/20/hou-tai-jian-kong-gamekit-jian-kong-jian-kong-wen-jian-shu-chu-de-zhong-ding-xiang.html"
  - "/hou-tai-jian-kong-gamekit-jian-kong-jian-kong-wen-jian-shu-chu-de-zhong-ding-xiang.html"
---
在了解GameKit这一块的时候，有个是关于监控的，就是监控错误的输出，然后显示，在项目中我们可以巧妙的使用这个技巧来完成错误日志的输出然后提交的给我们，然后我们进行错误日志的分析，来改善我们的项目

这里是选自cookbook的示例

MonitorGameKitViewController.h

```objectivec
//
//  MonitorGameKitViewController.h
//  MonitorGameKit
//
//  Created by david on 13-9-4.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GameKitHelper.h"

#define COOKBOOK_PURPLE_COLOR	[UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]
#define BARBUTTON(TITLE, SELECTOR) 	[[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]
#define STDERR_OUT [NSHomeDirectory() stringByAppendingPathComponent:@"tmp/stderr.txt"]


@interface MonitorGameKitViewController : UIViewController
@property (strong, nonatomic) IBOutlet UITextView *textView;

@end
```

MonitorGameKitViewController.m

```objectivec
//
//  MonitorGameKitViewController.m
//  MonitorGameKit
//
//  Created by david on 13-9-4.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "MonitorGameKitViewController.h"

@interface MonitorGameKitViewController ()

@end

@implementation MonitorGameKitViewController

@synthesize textView;

-(void) listenForStderr: (NSTimer *) timer
{
    NSString *contents = [NSString stringWithContentsOfFile:STDERR_OUT
                                                   encoding:NSUTF8StringEncoding
                                                      error:NULL];
    contents = [contents stringByReplacingOccurrencesOfString:@"\n"
                                                   withString:@"\n\n"];
    if([contents isEqualToString:textView.text])
    {
        return ;
    }
    [textView setText:contents];
    textView.contentOffset = CGPointMake(0.0f, MAX(textView.contentSize.height - textView.frame.size.height, 0.0f));
    
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    [GameKitHelper sharedInstance].sessionID = @"Peeking at GameKit";
    [GameKitHelper assignViewController:self];
    
    freopen([STDERR_OUT fileSystemRepresentation], "w", stderr);
    [NSTimer scheduledTimerWithTimeInterval:1.0f
                                     target:self
                                   selector:@selector(listenForStderr:)
                                   userInfo:nil
                                    repeats:YES];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
```

关于GameKitHelper的文件，可以到这里下载[GameKitHelper](https://github.com/zhangda89/iphone-3.0-cookbook-/blob/master/C12-GameKit/02-Monitoring%20GameKit/main.m)，如果想支持IOS5的话可以到这里[GameKitHelper](https://github.com/zhangda89/GameKitHelper)

这里重要的一点是利用了错误日志重定向到文件。

