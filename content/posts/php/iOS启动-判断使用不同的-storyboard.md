---
title: "iOS启动 判断使用不同的 storyboard"
date: "2025-06-19 09:58:40"
slug: "ios-qi-dong-pan-duan-shi-yong-bu-tong-de-storyboard"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS启动-判断使用不同的-storyboard/"
  - "/2025/06/19/iOS启动-判断使用不同的-storyboard.html"
  - "/iOS启动-判断使用不同的-storyboard/"
  - "/iOS启动-判断使用不同的-storyboard.html"
  - "/2025/06/19/ios-qi-dong-pan-duan-shi-yong-bu-tong-de-storyboard/"
  - "/2025/06/19/ios-qi-dong-pan-duan-shi-yong-bu-tong-de-storyboard.html"
  - "/ios-qi-dong-pan-duan-shi-yong-bu-tong-de-storyboard.html"
---
关于这个问题，也是一直困扰我很久的问题了，一直记恨于心啊，终于今天让我知道了，如何解决这个问题啦，哈哈，大笑江湖呀。

```objectivec
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
     UIViewController *rootVC;
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];
    if(![[NSUserDefaults standardUserDefaults] boolForKey:@"logged_in"]) {
           rootVC=[self.storyboard instantiateViewControllerWithIdentifier: @"vc1"];
    } else {
           rootVC=[self.storyboard instantiateViewControllerWithIdentifier: @"vc2"];
     }
    window.rootViewConroller=rootVC;
    [self.window makeKeyAndVisible];
    return YES;
}
```

这里面的“vc1”和“vc2”，其实就是storyboard的表示符，自己在创建storyboard的时候一般都会看到的，如果自己还不知道的话，多创建几个自己就知道了。
