---
title: "iOS UIScreen（屏幕）UIWindow（画框)UIView(画布)didFinishLaunchingWithOptions的概念"
date: "2025-06-06 10:33:47"
slug: "ios-uiscreen-ping-mu-uiwindow-hua-kuang-uiview-hua-bu-didfinishlaunchingwithoptions-de-gai-nian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS-UIScreen（屏幕）UIWindow（画框)UIView(画布)didFinishLaunchingWithOptions的概念/"
  - "/2025/06/06/iOS-UIScreen（屏幕）UIWindow（画框)UIView(画布)didFinishLaunchingWithOptions的概念.html"
  - "/iOS-UIScreen（屏幕）UIWindow（画框)UIView(画布)didFinishLaunchingWithOptions的概念/"
  - "/iOS-UIScreen（屏幕）UIWindow（画框)UIView(画布)didFinishLaunchingWithOptions的概念.html"
  - "/2025/06/06/iOS-UIScreen（屏幕）UIWindow（画框-UIView-画布-didFinishLaunchingWithOptions的概念/"
  - "/2025/06/06/iOS-UIScreen（屏幕）UIWindow（画框-UIView-画布-didFinishLaunchingWithOptions的概念.html"
  - "/2025/06/06/ios-uiscreen-ping-mu-uiwindow-hua-kuang-uiview-hua-bu-didfinishlaunchingwithoptions-de-/"
  - "/2025/06/06/ios-uiscreen-ping-mu-uiwindow-hua-kuang-uiview-hua-bu-didfinishlaunchingwithoptions.html"
  - "/ios-uiscreen-ping-mu-uiwindow-hua-kuang-uiview-hua-bu-didfinishlaunchingwithoptions-de-gai-nia.html"
---
didFinishLaunchingWithOptions 方法：顾名思义。在app开始运行时会调用里面的方法。

```c
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    //返回的是带有状态栏的矩形
    self.window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];
    
    CGRect bound = [[UIScreen mainScreen]bounds];  //返回的是不带有状态栏的Rect
    NSLog(@"boundwith:%f    boundheight:%f",bound.size.width,bound.size.height);
    NSLog(@"boundx:%f    boundy:%f",bound.origin.x,bound.origin.y);
    //2012-08-03 23:21:45.716 DinkMixer[599:c07] boundwith:320.000000    boundheight:480.000000
    //2012-08-03 23:21:45.719 DinkMixer[599:c07] boundx:0.000000    boundy:0.000000
    
    CGRect appBound = [[UIScreen mainScreen]applicationFrame];  //返回的是带有状态栏的Rect
    NSLog(@"appBoundwith:%f    boundheight:%f",appBound.size.width,appBound.size.height);
    NSLog(@"appBoundx:%f    boundy:%f",appBound.origin.x,appBound.origin.y);
    //2012-08-03 23:21:45.720 DinkMixer[599:c07] appBoundwith:320.000000    boundheight:460.000000
    //2012-08-03 23:21:45.720 DinkMixer[599:c07] appBoundx:0.000000    boundy:20.000000
    
    //很明显状态栏占用了空间20像素
    
    MasterViewController *masterViewController = [[[MasterViewController alloc] initWithNibName:@"MasterViewController" bundle:nil] autorelease];//根据nib文件的名称来创建一个视图控制器
    
    self.navigationController = [[[UINavigationController alloc] initWithRootViewController:masterViewController] autorelease];//创建一个导航控制器，并指定该导航控制器的根视图控制器为上面建立的masterViewController
    
    self.window.rootViewController = self.navigationController;//窗体（window）有一个根视图控制器——这个视图控制器负责配置当窗体显示时最先显示的视图。要让你的视图控制器的内容显示在窗体中，需要去设置窗体的根视图控制器为你的视图控制器。
    
    [self.window makeKeyAndVisible];//这行代码会让包含了视图控制器视图的Window窗口显示在屏幕上。
    return YES;
}
```
