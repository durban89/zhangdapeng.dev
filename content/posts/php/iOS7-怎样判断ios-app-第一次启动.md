---
title: "iOS7 怎样判断ios app 第一次启动"
date: "2025-06-26 11:15:56"
slug: "ios7-zen-yang-pan-duan-ios-app-di-yi-ci-qi-dong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-怎样判断ios-app-第一次启动/"
  - "/2025/06/26/iOS7-怎样判断ios-app-第一次启动.html"
  - "/iOS7-怎样判断ios-app-第一次启动/"
  - "/iOS7-怎样判断ios-app-第一次启动.html"
  - "/2025/06/26/ios7-zen-yang-pan-duan-ios-app-di-yi-ci-qi-dong/"
  - "/2025/06/26/ios7-zen-yang-pan-duan-ios-app-di-yi-ci-qi-dong.html"
  - "/ios7-zen-yang-pan-duan-ios-app-di-yi-ci-qi-dong.html"
---
关于第一次启动iOS APP的宣传画面的制作中的判断，判断第一次启动，判断是否是第一次启动。关于这个我查找了相关资料，进行了google资料搜索。

---

一个有用的例子是发送一个分析实例。这可能是一个很好的方法来确定有多少人下载实用应用程序。有人会说：“但是，嘿，苹果AppStore已经告诉我，应用程序的下载量了”。

流行的解决方案是在大多数地方是用[NSUserDefaults standardUserDefaults的一个关键，如果它不存在，这意味着这是应用程序启动，否则，它不是第一次。

你可以搜索的关键，如果它未设置运行 first-time-code，并设置它，但在app的其余部分你将无法知道它是不是第一次运行（除非你使用一个全局变量）

因此，我建议我的解决方案：

在appdelegate.m中找到 “`application:didFinishLaunchingWithOptions:`”方法, 添加以下代码:

```objectivec
if (![[NSUserDefaults standardUserDefaults] boolForKey:@"everLaunched"]) 
{  
    [[NSUserDefaults standardUserDefaults] setBool:YES forKey:@"everLaunched"];  
    [[NSUserDefaults standardUserDefaults] setBool:YES forKey:@"firstLaunch"];  
}  
else
{  
    [[NSUserDefaults standardUserDefaults] setBool:NO forKey:@"firstLaunch"];  
}
```

总的解决办法是 2 个key: @”everLaunched”判断用户以前是否登录,

@”firstLaunch” 用来开发者在程序的其他部分判断.

在第一次启动的时候 key @”everLaunched” 不会被赋址的, 并且设置为YES. @”firstLaunch”被设置为 YES.

在程序的其他部分用以下代码判断:

```objectivec
if ([[NSUserDefaults standardUserDefaults] boolForKey:@"firstLaunch"]) 
{  
    // 这里判断是否第一次  
    UIAlertView *alert=[[UIAlertView alloc] initWithTitle:@"第一次"   
                                                  message:@"进入App"  
                                                 delegate:self   
                                        cancelButtonTitle:@"我知道了"   
                                        otherButtonTitles:nil];  
    [alert show];  
    [alert release];  
      
}
```

---

参考文章：

<http://blog.csdn.net/kylinbl/article/details/8638988>

