---
title: "iOS 监测网络链接状态"
date: "2025-06-11 10:44:13"
slug: "ios-jian-ce-wang-luo-lian-jie-zhuang-tai"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-监测网络链接状态/"
  - "/2025/06/11/iOS-监测网络链接状态.html"
  - "/iOS-监测网络链接状态/"
  - "/iOS-监测网络链接状态.html"
  - "/2025/06/11/ios-jian-ce-wang-luo-lian-jie-zhuang-tai/"
  - "/2025/06/11/ios-jian-ce-wang-luo-lian-jie-zhuang-tai.html"
  - "/ios-jian-ce-wang-luo-lian-jie-zhuang-tai.html"
---
使用之前请从Apple网站下载示例：[点此下载](https://developer.apple.com/library/ios/samplecode/Reachability/Reachability.zip)

然后将Reachability.h 和 Reachability.m 加到自己的项目中，并引用 SystemConfiguration.framework，就可以使用了。

Reachability 中定义了3种网络状态：

```objectivec
// the network state of the device for Reachability 1.5.
typedef enum {
    NotReachable = 0,  //无连接
    ReachableViaCarrierDataNetwork, //使用3G/GPRS网络
    ReachableViaWiFiNetwork  //使用WiFi网络
} NetworkStatus;

// the network state of the device for Reachability 2.0.
typedef enum {
    NotReachable = 0,  //无连接
    ReachableViaWiFi,  //使用3G/GPRS网络
    ReachableViaWWAN  //使用WiFi网络
} NetworkStatus;
```

比如检测某一特定站点的接续状况，可以使用下面的代码：

```objectivec
Reachability *r = [Reachability reachabilityWithHostName:@“www.apple.com”];
switch ([r currentReachabilityStatus]) {
    case NotReachable:
        // 没有网络连接
        break;
    case ReachableViaWWAN:
        // 使用3G网络
        break;
    case ReachableViaWiFi:
        // 使用WiFi网络
        break;
}
```

检测当前网络环境：

```objectivec
// 是否wifi
+ (BOOL) IsEnableWIFI {
    return ([[Reachability reachabilityForLocalWiFi] currentReachabilityStatus] != NotReachable);
}

// 是否3G
+ (BOOL) IsEnable3G {
    return ([[Reachability reachabilityForInternetConnection] currentReachabilityStatus] != NotReachable);
}
```

连接状态实时通知

网络连接状态的实时检查，通知在网络应用中也是十分必要的。接续状态发生变化时，需要及时地通知用户。由于Reachability1.5版与2.0版有一些变化，这里分开来说明使用方法。

Reachability 1.5



```objectivec My.AppDelegate.h
#import "Reachability.h"

@interface MyAppDelegate : NSObject <UIApplicationDelegate> {
    NetworkStatus remoteHostStatus;
}

@property NetworkStatus remoteHostStatus;

@end
```



```objectivec My.AppDelegate.m
#import "MyAppDelegate.h"

@implementation MyAppDelegate

@synthesize remoteHostStatus;

// 更新网络状态
- (void)updateStatus {
    self.remoteHostStatus = [[Reachability sharedReachability] remoteHostStatus];
}

// 通知网络状态
- (void)reachabilityChanged:(NSNotification *)note {
    [self updateStatus];
    if (self.remoteHostStatus == NotReachable) {
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:NSLocalizedString(@"AppName", nil) message:NSLocalizedString(@"NotReachable", nil)
        delegate:nil cancelButtonTitle:@"OK" otherButtonTitles: nil];
        [alert show];
        [alert release];
    }
}

// 程序启动器，启动网络监视
- (void)applicationDidFinishLaunching:(UIApplication *)application {

    // 设置网络检测的站点
    [[Reachability sharedReachability] setHostName:@"www.apple.com"];
    [[Reachability sharedReachability] setNetworkStatusNotificationsEnabled:YES];
    // 设置网络状态变化时的通知函数
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(reachabilityChanged:)
                                                 name:@"kNetworkReachabilityChangedNotification" object:nil];
    [self updateStatus];
}

- (void)dealloc {
    // 删除通知对象
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    [window release];
    [super dealloc];
}
```

Reachability 2.0



```objectivec MyAppDelegate.h
@class Reachability;

@interface MyAppDelegate : NSObject <UIApplicationDelegate> {
    Reachability  *hostReach;
}

@end
```



```objectivec MyAppDelegate.m
- (void)reachabilityChanged:(NSNotification *)note {
    Reachability* curReach = [note object];
    NSParameterAssert([curReach isKindOfClass: [Reachability class]]);
    NetworkStatus status = [curReach currentReachabilityStatus];

    if (status == NotReachable) {
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"AppName"
                                                        message:@"NotReachable"
                                                       delegate:nil
                                              cancelButtonTitle:@"YES" otherButtonTitles:nil];
        [alert show];
        [alert release];
    }
}

- (void)applicationDidFinishLaunching:(UIApplication *)application {
    // ...

    // 监测网络情况
    [[NSNotificationCenter defaultCenter] addObserver:self
                                          selector:@selector(reachabilityChanged:)
                                          name: kReachabilityChangedNotification
                                          object: nil];
    hostReach = [[Reachability reachabilityWithHostName:@"www.google.com"] retain];
    [hostReach startNotifer];
    // ...
}
```

来源：http://www.cnblogs.com/mrhgw/archive/2012/08/01/2617760.html
