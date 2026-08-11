---
title: "iOS开发 视图翻转效果的实现  transition"
date: "2025-06-20 10:36:25"
slug: "ios-kai-fa-shi-tu-fan-zhuan-xiao-guo-de-shi-xian-transition"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS开发-视图翻转效果的实现-transition/"
  - "/2025/06/20/iOS开发-视图翻转效果的实现-transition.html"
  - "/iOS开发-视图翻转效果的实现-transition/"
  - "/iOS开发-视图翻转效果的实现-transition.html"
  - "/2025/06/20/ios-kai-fa-shi-tu-fan-zhuan-xiao-guo-de-shi-xian-transition/"
  - "/2025/06/20/ios-kai-fa-shi-tu-fan-zhuan-xiao-guo-de-shi-xian-transition.html"
  - "/ios-kai-fa-shi-tu-fan-zhuan-xiao-guo-de-shi-xian-transition.html"
---
关于视图的翻转效果，最近我稍微的做了一下研究

主要的是使用了一个函数

`+ (void)transitionFromView:(UIView *)fromView toView:(UIView *)toView duration:(NSTimeInterval)duration options:(UIViewAnimationOptions)options completion:(void (^)(BOOL finished))completion NS_AVAILABLE_IOS(4_0);`

还是演示一下吧，我这里是使用的storyboard

FlipViewViewController.h

```objectivec
//
//  FlipViewViewController.h
//  FlipView
//
//  Created by david on 13-8-4.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface FlipViewViewController : UIViewController

@property (strong, nonatomic) UIView *frontView;
@property (strong, nonatomic) UIView *backView;
@property (nonatomic) BOOL goingToFrontView;

@property (strong, nonatomic) IBOutlet UIBarButtonItem *FlipButton;
- (IBAction)FlipButtonAction:(id)sender;

@end
```

FlipViewViewController.m

```objectivec
//
//  FlipViewViewController.m
//  FlipView
//
//  Created by david on 13-8-4.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "FlipViewViewController.h"

@interface FlipViewViewController ()

@end


@implementation FlipViewViewController

@synthesize frontView;
@synthesize backView;
@synthesize FlipButton;
@synthesize goingToFrontView;

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    self.frontView = [[UIView alloc] initWithFrame:self.view.frame];
    self.backView = [[UIView alloc] initWithFrame:self.view.frame];
}

-(void) viewWillAppear:(BOOL)animated{
    self.FlipButton.title = @"前视图";
    self.goingToFrontView = YES;
    
    [self initFrontViewBackgroundColor];
    [self initBackViewBackGroundColor];
    
    [self.view addSubview:self.frontView];
    [self.view addSubview:self.backView];
    
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)FlipButtonAction:(id)sender {
    self.goingToFrontView = !self.goingToFrontView;
    
    UIView *fromView = self.goingToFrontView ? self.backView : self.frontView;
    UIView *toView = self.goingToFrontView ? self.frontView : self.backView;
    
    
    UIViewAnimationOptions transitionDirection = self.goingToFrontView ? UIViewAnimationOptionTransitionFlipFromRight : UIViewAnimationOptionTransitionFlipFromLeft;
    
    [UIView transitionFromView:fromView
                        toView:toView
                      duration:1.0
                       options:transitionDirection
                    completion:^(BOOL finished) {
                        
                        [self showButtonTitle];
                        
                    }];
}

-(void) initFrontViewBackgroundColor{
    self.frontView.backgroundColor = [UIColor redColor];
}

-(void) initBackViewBackGroundColor{
    self.backView.backgroundColor = [UIColor blueColor];
}

-(void) showButtonTitle{
    if(self.goingToFrontView){
        self.FlipButton.title = @"前视图";
    }else{
        self.FlipButton.title = @"后视图";
    }
}

@end
```
