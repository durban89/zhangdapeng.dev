---
title: "UIWebView与js(JavaScript) 的交互 示例"
date: "2025-06-20 11:33:13"
slug: "uiwebview-yu-jsjavascript-de-jiao-hu-shi-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/UIWebView与js(JavaScript)-的交互-示例/"
  - "/2025/06/20/UIWebView与js(JavaScript)-的交互-示例.html"
  - "/UIWebView与js(JavaScript)-的交互-示例/"
  - "/UIWebView与js(JavaScript)-的交互-示例.html"
  - "/2025/06/20/UIWebView与js-JavaScript-的交互-示例/"
  - "/2025/06/20/UIWebView与js-JavaScript-的交互-示例.html"
  - "/2025/06/20/uiwebview-yu-jsjavascript-de-jiao-hu-shi-li/"
  - "/2025/06/20/uiwebview-yu-jsjavascript-de-jiao-hu-shi-li.html"
  - "/uiwebview-yu-jsjavascript-de-jiao-hu-shi-li.html"
---
关于这个的使用是源于我参看的一个图表表格的使用

操作步骤是这样的

第一步，自己写个页面，用来实现页面的某些效果的，比如这里的温度曲线图，是调用的highchart的js插件。外加一些css效果。

第二步，在自己的app中将要使用的页面加载进来，这里调用的是index.html

第三步，使用webview进行呈现，还要灵活的使用webview的一个方法【stringByEvaluatingJavaScriptFromString】

这里只演示一下如何使用，具体的页面部分，可以自己写，我放在自己的[github](https://github.com/zhangda89/TemperatureCurve)上。

TemperatureCurveViewController.h

```objectivec
//
//  TemperatureCurveViewController.h
//  Real-time temperature curve
//
//  Created by david on 13-8-15.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface TemperatureCurveViewController : UIViewController<UIWebViewDelegate, UITextFieldDelegate>

@property(retain, nonatomic) UIWebView *webViewForSelectDate;
@property(retain, nonatomic) NSTimer *timer;

@end
```

TemperatureCurveViewController.m

```objectivec
//
//  TemperatureCurveViewController.m
//  Real-time temperature curve
//
//  Created by david on 13-8-15.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "TemperatureCurveViewController.h"

@interface TemperatureCurveViewController ()

@end

@implementation TemperatureCurveViewController

@synthesize webViewForSelectDate;
@synthesize timer;

- (void)viewDidLoad
{
    [super viewDidLoad];
    
//    UIInterfaceOrientation orientation = [UIDevice currentDevice].orientation;
//    if(UIDeviceOrientationIsPortrait(orientation) || orientation == UIDeviceOrientationUnknown){
//        if([[UIDevice currentDevice] respondsToSelector:@selector(setOrientation:)]){
//            [[UIDevice currentDevice] performSelector:@selector(setOrientation:)
//                                           withObject:(id)UIDeviceOrientationLandscapeRight];
//        }
//    
//    }

    CGRect webFrame = self.view.frame;
    webFrame.origin.x = 0;
    webFrame.origin.y = 0;
    
    webViewForSelectDate = [[UIWebView alloc] initWithFrame:webFrame];
    webViewForSelectDate.delegate = self;
    webViewForSelectDate.scalesPageToFit = YES;
    webViewForSelectDate.opaque = NO;
    webViewForSelectDate.backgroundColor = [UIColor clearColor];
    webViewForSelectDate.autoresizingMask = (UIViewAutoresizingFlexibleHeight | UIViewAutoresizingFlexibleWidth);
    [self.view addSubview:webViewForSelectDate];
    
    NSString *htmlPath = [[[NSBundle mainBundle] resourcePath] stringByAppendingPathComponent:@"curve.bundle/index.html"];
    
    NSURL *url = [NSURL fileURLWithPath:htmlPath];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    
    [webViewForSelectDate loadRequest:request];
    
    
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(BOOL) shouldAutorotate{
    return YES;
}

-(NSUInteger)supportedInterfaceOrientations{
    return UIInterfaceOrientationMaskAll;
}

-(void) updateData{
    NSDate *nowDate = [[NSDate alloc] init];
    NSTimeInterval nowTimeInterval = [nowDate timeIntervalSince1970] * 1000;
    
    int temperature = [self getRandomNumber:20 to:50];
    
    NSMutableString *jsStr = [[NSMutableString alloc] initWithCapacity:0];
    [jsStr appendFormat:@"updateData(%f,%d)",nowTimeInterval, temperature];
    
    [webViewForSelectDate stringByEvaluatingJavaScriptFromString:jsStr];
}

-(int) getRandomNumber:(int)from to:(int)to{
    return (int)(from + (arc4random() % (to - from + 1)));
}

#pragma mark - delegate o webview
-(BOOL) webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType{
    return YES;
}

-(void) webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error{

}

-(void) webViewDidFinishLoad:(UIWebView *)webView{
    timer = [NSTimer scheduledTimerWithTimeInterval:1
                                             target:self
                                           selector:@selector(updateData)
                                           userInfo:nil
                                            repeats:YES];
}

@end
```

其主要的一点就是使用`stringByEvaluatingJavaScriptFromString`这个方法，他可以灵活的将js嵌入页面中，进行操作，而且一定是要在webview加载完后进行调用。
