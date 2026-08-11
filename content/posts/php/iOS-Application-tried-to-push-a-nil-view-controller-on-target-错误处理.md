---
title: "'iOS Application tried to push a nil view controller on target'错误处理"
date: "2025-06-19 09:58:37"
slug: "ios-application-tried-to-push-a-nil-view-controller-on-target-cuo-wu-chu-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/'iOS-Application-tried-to-push-a-nil-view-controller-on-target'错误处理/"
  - "/2025/06/19/'iOS-Application-tried-to-push-a-nil-view-controller-on-target'错误处理.html"
  - "/'iOS-Application-tried-to-push-a-nil-view-controller-on-target'错误处理/"
  - "/'iOS-Application-tried-to-push-a-nil-view-controller-on-target'错误处理.html"
  - "/2025/06/19/iOS-Application-tried-to-push-a-nil-view-controller-on-target-错误处理/"
  - "/2025/06/19/iOS-Application-tried-to-push-a-nil-view-controller-on-target-错误处理.html"
  - "/2025/06/19/ios-application-tried-to-push-a-nil-view-controller-on-target-cuo-wu-chu-li/"
  - "/2025/06/19/ios-application-tried-to-push-a-nil-view-controller-on-target-cuo-wu-chu-li.html"
  - "/ios-application-tried-to-push-a-nil-view-controller-on-target-cuo-wu-chu-li.html"
---
关于“ios Application tried to push a nil view controller on target”这个错误，原因其实很简单，问题都是找到了才觉得简单，处理的时候不知道有多烦恼。呵呵，本来就应该是这样吧。

没有错误的作法：

```objectivec
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    
    rootViewController = [[WalkerUITestViewController alloc] initWithNibName:@"WalkerUITestViewController" bundle:nil];
    navigationController = [[UINavigationController alloc] initWithRootViewController:rootViewController];
    
    
    self.window.rootViewController = navigationController;
    
    
    
    self.window.backgroundColor = [UIColor whiteColor];
    [self.window makeKeyAndVisible];
    return YES;
}
```

有错误的作法

```objectivec
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    
    navigationController = [[UINavigationController alloc] 
    initWithRootViewController:rootViewController];
    
    
    self.window.rootViewController = navigationController;
    
    
    
    self.window.backgroundColor = [UIColor whiteColor];
    [self.window makeKeyAndVisible];
    return YES;
}
```

当然在这两个例子里面，属性的声明是一样的

```objectivec
@synthesize navigationController;
@synthesize rootViewController;
```

其实就是在使用之前，自己有木有初始化的问题。ok。
