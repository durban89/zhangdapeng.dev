---
title: "iOS 6 SDK: 在应用内展示App Store"
date: "2025-06-23 15:49:06"
slug: "ios-6-sdk-zai-ying-yong-nei-zhan-shi-app-store"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS-6-SDK:-在应用内展示App-Store/"
  - "/2025/06/23/iOS-6-SDK:-在应用内展示App-Store.html"
  - "/iOS-6-SDK:-在应用内展示App-Store/"
  - "/iOS-6-SDK:-在应用内展示App-Store.html"
  - "/2025/06/23/iOS-6-SDK-在应用内展示App-Store-StoreKit-SKStoreProductViewController/"
  - "/2025/06/23/iOS-6-SDK-在应用内展示App-Store-StoreKit-SKStoreProductViewController.html"
  - "/2025/06/23/ios-6-sdk-zai-ying-yong-nei-zhan-shi-app-store/"
  - "/2025/06/23/ios-6-sdk-zai-ying-yong-nei-zhan-shi-app-store.html"
  - "/ios-6-sdk-zai-ying-yong-nei-zhan-shi-app-store.html"
---
出于什么样的原因你会希望用户从你的iOS app中进入App Store呢？可能你想用户去App Store 为你的应用评分，也可能你希望用户看到你其他的iOS app。iOS 6引入了SKStoreProductViewController类，可以让用户在不离开当前应用的前提下展示App Store中的其他产品。

### [Store Kit](#1)

SKStoreProductViewController类是Store Kit框架的一部分。SKStoreProductViewController使用起来非常简单，在用实例讲解之前，了解一些基本的知识很有必要。

SKStoreProductViewController类是UIViewController的子类, 如果你对view controller比较熟悉的话，那SKStoreProductViewController使用起来也非常简单了。当你希望向用户展示App Store中产品时，你需要：

1.实例化一个SKStoreProductViewController类  
2.设置它的delegate  
3.把sotre product视图控制器显示给消费者

剩下的就交给操作系统来处理了。需要记住一点的是SKStoreProductViewController只能以模态的方式显示。 SKStoreProductViewControllerDelegate协议定义了一个单独的方法— productViewControllerDidFinish:，当消费者离开App Store时会调用这个方法—一般是通过点击左上角画面中的取消按钮。通过给代理发送productViewControllerDidFinish:消 息，操作系统就会把控制权返回到你的程序。下面我来演示一下如何在一个简单的程序中使用SKStoreProductViewController类。

Step 1: Setting Up the Project

我们将要创建的app不是多实用，仅有一个按钮，可以把用户带入App Store，向用户展示我最近发布的一款简单的天气类app。通过实例我们可以了解不同的部分如何很好地契合在一起，还可以了解如何在项目中使用 SKStoreProductViewController类。

从模版列表中选择一个Single View Application模版，在Xcode中创建一个新的项目。

将程序的名称设置为UsingStoreProduct，然后输入一个company identifier，并将device family设置为iPhone，最后勾选上Automatic Reference Counting。剩余的勾选框不要勾选。“告诉”Xcode你希望保存项目的地方，点击创建按钮。

Step 2: Adding the Store Kit Framework

由于SKStoreProductViewController类是Store Kit框架的一部分，所以我们需要将这个Store Kit框架链接到我们的工程中。在工程导航器中选中工程，然后在target列表中选中target。在画面的顶部，选择Build Phase选项，然后打开Link Binary With Libraries。点击‘+’按钮，并在列表中搜索StoreKit并选择StoreKit.framework。这样就可以成功的将Store Kit框架链接到工程中。

为了使用UsingStoreProductViewController类里的Store Kit框架，我们需要输入框架的头文件，打开UsingStoreProductViewController.h，在顶部添加下边这个引入语法：

```objectivec
#import <StoreKit/StoreKit.h>
```

Step 3: Using the SKStoreProductViewController Class

在视图控制器的viewDidLoad方法中，在下面的代码片段中创建一个新的按钮。按钮的类型是UIButtonTypeRoundedRect，然后 我把这个按钮放在视图控制器view的正中间。同时我还给这个按钮制定了一个title，并添加了一个target-action——匹配 UIControlEventTouchUpInside事件。这意味无论何时，用户点击按钮，view controller就会收到“前往寻艺 App Store”的信息。

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    
    
    [super viewDidLoad];
    //初始化一个按钮
    UIButton *button = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    [button setTitle:@"前往寻艺 App Store" forState:UIControlStateNormal];
    [button setFrame:CGRectMake(0.0, 0.0, 200.0, 44.0)];
    [button setCenter:self.view.center];
    [self.view addSubview:button];
    [button addTarget:self
               action:@selector(openAppStore:)
     forControlEvents:UIControlEventTouchUpInside];
    
}
```

在openAppStore: 方法中，我对SKStoreProductViewController进行了初始化，并将自己设置为它的delegate，然后在给这个实例发送一个 loadProductWithParameters:completionBlock:消息。  
loadProductWithParameters:completionBlock:接收两个参数：

（1）一个字典：用一个key指定我们想要显示给用的程序的标示符。

（2）一个completion block。  
当App store请求结束时会调用这个completion block。在完成的block中，我们要核实是否有错误遗漏，并把store product 视图控制器展示给用户。

请记住，即使用户没有离开你的程序，操作系统仍然会在内部进行与App store的连接。由于在请求App Store过程中，会需要稍微长的一段时间，也就是说，最好在请求还没有返回响应时给用户显示一个风火轮。一旦请求完成（成功或者不成功），已经完成的 block将会允许我们解除activity indicator。

```objectivec
-(void) openAppStore:(id)sender
{
    //初始化Product View Controller
    SKStoreProductViewController *storeProductViewController = [[SKStoreProductViewController alloc] init];
    //配置View　Controller
    [storeProductViewController setDelegate:self];
    [storeProductViewController loadProductWithParameters:@{SKStoreProductParameterITunesItemIdentifier:@"685836302"}
                                          completionBlock:^(BOOL result, NSError *error){
                                              if(error)
                                              {
                                                  NSLog(@"Error %@ with User Info %@.", error, [error userInfo]);
                                              }
                                              else
                                              {
                                                  [self presentViewController:storeProductViewController
                                                                     animated:YES
                                                                   completion:nil];
                                              }
                                          }];
    
}
```

注意：你可以在iTunes Connect找到app的唯一识别符，App Store中的每个app都有一个唯一识别符/Apple ID，注意你需要将在参数字典中以字符串的形式传递apple id。

在生成和运行程序之前，我们需要MTViewController类通过实现productViewControllerDidFinish:方法以遵循 SKStoreProductViewControllerDelegate协议。我们可以通过告诉编译器“UsingStoreProductController类符合 SKStoreProductViewController授权协议”来更新view controller的接口文件，看下边：

```objectivec
#import <UIKit/UIKit.h>
#import <StoreKit/StoreKit.h>

@interface UsingStoreProductViewController : UIViewController<SKStoreProductViewControllerDelegate>

@end
```

Step 4: Build and Run

虽然苹果表示SKStoreProductViewController类可以向用户展示其他app，但这是一种理想的在用户不离开当前app的情况下，让用户去App Store评分的方法。

整个的运行逻辑代码：

UsingStoreProductViewController.m

```objectivec
//
//  UsingStoreProductViewController.m
//  UsingStoreProduct
//
//  Created by david on 13-9-23.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "UsingStoreProductViewController.h"

@interface UsingStoreProductViewController ()

@end

@implementation UsingStoreProductViewController

@synthesize indicatorView;

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    
    [super viewDidLoad];
    //初始化一个按钮
    UIButton *button = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    [button setTitle:@"前往寻艺 App Store" forState:UIControlStateNormal];
    [button setFrame:CGRectMake(0.0, 0.0, 200.0, 44.0)];
    [button setCenter:self.view.center];
    [self.view addSubview:button];
    [button addTarget:self
               action:@selector(openAppStore:)
     forControlEvents:UIControlEventTouchUpInside];
    
}


-(void) openAppStore:(id)sender
{
    [self showIndicator];
    //初始化Product View Controller
    SKStoreProductViewController *storeProductViewController = [[SKStoreProductViewController alloc] init];
    //配置View　Controller
    [storeProductViewController setDelegate:self];
    [storeProductViewController loadProductWithParameters:@{SKStoreProductParameterITunesItemIdentifier:@"685836302"}
                                          completionBlock:^(BOOL result, NSError *error){
                                              if(error)
                                              {
                                                  NSLog(@"Error %@ with User Info %@.", error, [error userInfo]);
                                              }
                                              else
                                              {
                                                  [self hideIndicator];
                                                  [self presentViewController:storeProductViewController
                                                                     animated:YES
                                                                   completion:nil];
                                              }
                                          }];
    
}

-(void) productViewControllerDidFinish:(SKStoreProductViewController *)viewController
{
    [self dismissViewControllerAnimated:YES completion:nil];
}

- (void)showIndicator
{
    indicatorView = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleGray];
    indicatorView.autoresizingMask =
    UIViewAutoresizingFlexibleTopMargin | UIViewAutoresizingFlexibleBottomMargin
    | UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin;
    [self.view addSubview:indicatorView];
    [indicatorView sizeToFit];
    [indicatorView startAnimating];
    indicatorView.center = self.view.center;
}

- (void)hideIndicator
{
    [indicatorView stopAnimating];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
```

