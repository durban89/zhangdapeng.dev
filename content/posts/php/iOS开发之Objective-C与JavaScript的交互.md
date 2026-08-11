---
title: "iOS开发之Objective-C与JavaScript的交互"
date: "2025-06-20 11:33:16"
slug: "ios-kai-fa-zhi-objective-c-yu-javascript-de-jiao-hu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS开发之Objective-C与JavaScript的交互/"
  - "/2025/06/20/iOS开发之Objective-C与JavaScript的交互.html"
  - "/iOS开发之Objective-C与JavaScript的交互/"
  - "/iOS开发之Objective-C与JavaScript的交互.html"
  - "/2025/06/20/ios-kai-fa-zhi-objective-c-yu-javascript-de-jiao-hu/"
  - "/2025/06/20/ios-kai-fa-zhi-objective-c-yu-javascript-de-jiao-hu.html"
  - "/ios-kai-fa-zhi-objective-c-yu-javascript-de-jiao-hu.html"
---
UIWebView是iOS最常用的SDK之一，它有一个stringByEvaluatingJavaScriptFromString方法可以将javascript嵌入页面中，通过这个方法我们可以在iOS中与UIWebView中的网页元素交互。  
  
*stringByEvaluatingJavaScriptFromString*  
  
使用stringByEvaluatingJavaScriptFromString方法，需要等UIWebView中的页面加载完成之后去调用。我们在界面上拖放一个UIWebView控件。在Load中将google mobile加载到这个控件中，代码如下：

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    webView.backgroundColor = [UIColor clearColor];
    webView.scalesPageToFit =YES;
    webView.delegate =self;
    NSURL *url =[[NSURL alloc] initWithString:@"http://www.google.com.hk/m?gl=CN&hl=zh_CN&source=ihp"];
    
    NSURLRequest *request =  [[NSURLRequest alloc] initWithURL:url];
    [webView loadRequest:request]; 
}
```

我们在webViewDidFinishLoad方法中就可以通过javascript操作界面元素了。  
下面实现一个关于如何进行google关键字搜索的操作  
示例1:获取当前页面的url

```objectivec
- (void)webViewDidFinishLoad:(UIWebView *)webView {  
    NSString *currentURL = [webView stringByEvaluatingJavaScriptFromString:@"document.location.href"];
}
```

示例2:获取页面title

```objectivec
- (void)webViewDidFinishLoad:(UIWebView *)webView {
    NSString *title = [webview stringByEvaluatingJavaScriptFromString:@"document.title"]; 
}
```

示例3:修改界面元素的值

```objectivec
- (void)webViewDidFinishLoad:(UIWebView *)webView {
    NSString 
*js_result = [self.webView 
stringByEvaluatingJavaScriptFromString:@"document.getElementsByName('q')[0].value='GoWhich';"];
}
```

示例4:表单提交

```objectivec
- (void)webViewDidFinishLoad:(UIWebView *)webView {
    NSString *js_result2 = [webView stringByEvaluatingJavaScriptFromString:@"document.forms[0].submit(); "];
}
```

示例3跟示例4，就实现了在google搜索关键字："Gowich"的功能。  
  
示例5：完整的表单提交  
上面的功能我们可以封装到一个js函数中，将这个函数插入到页面上执行，代码如下：

```objectivec
-(void)webViewDidFinishLoad:(UIWebView *)webView{
    [self.webView stringByEvaluatingJavaScriptFromString:@"var script = document.createElement('script');"
     "script.type = 'text/javascript';"
     "script.text = \"function searchFunction() { "
     "var field = document.getElementsByName('q')[0];"
     "field.value='GoWhich';"
     "document.forms[0].submit();"
     "}\";"
     "document.getElementsByTagName('head')[0].appendChild(script);"];
    
    [self.webView stringByEvaluatingJavaScriptFromString:@"searchFunction();"];
}
```

第一步、首先通过js创建一个script的标签，type为'text/javascript'。  
  
第二步、然后在这个标签中插入一段字符串，这段字符串就是一个函数：searchFunction，这个函数实现google自动搜索关键字的功能。  
  
第三步、然后使用stringByEvaluatingJavaScriptFromString执行searchFunction函数。  
  
stringByEvaluatingJavaScriptFromString的用法，它的功能非常的强大，用起来非常简单，通过它我们可以很方便的操作uiwebview中的页面元素。  
详细代码如下：

GoogleSearchViewController.m

```objectivec
//
//  GoogleSearchViewController.m
//  JavascriptAndIOS
//
//  Created by david on 13-8-15.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "GoogleSearchViewController.h"

@interface GoogleSearchViewController ()

@end

@implementation GoogleSearchViewController

@synthesize webView;

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    CGRect webFrame = self.view.frame;
    webFrame.origin.x = 0;
    webFrame.origin.y = 0;
    
    webView = [[UIWebView alloc] initWithFrame:webFrame];
    self.webView.backgroundColor = [UIColor clearColor];
    self.webView.scalesPageToFit =YES;
    self.webView.delegate =self;
    NSURL *url =[[NSURL alloc] initWithString:@"http://www.google.com.hk/m?gl=CN&hl=zh_CN&source=ihp"];
    
    NSURLRequest *request =  [[NSURLRequest alloc] initWithURL:url];
    [self.webView loadRequest:request];
    [self.view addSubview:self.webView];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(void)webViewDidFinishLoad:(UIWebView *)webView{
    [self.webView stringByEvaluatingJavaScriptFromString:@"var script = document.createElement('script');"
     "script.type = 'text/javascript';"
     "script.text = \"function searchFunction() { "
     "var field = document.getElementsByName('q')[0];"
     "field.value='GoWhich';"
     "document.forms[0].submit();"
     "}\";"
     "document.getElementsByTagName('head')[0].appendChild(script);"];
    
    [self.webView stringByEvaluatingJavaScriptFromString:@"searchFunction();"];
}

@end
```

GoogleSearchViewController.h

```objectivec
//
//  GoogleSearchViewController.h
//  JavascriptAndIOS
//
//  Created by david on 13-8-15.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface GoogleSearchViewController : UIViewController<UIWebViewDelegate>

@property (retain, nonatomic) UIWebView *webView;

@end
```
