---
title: "iOS 状态栏操作（收集）"
date: "2025-06-16 14:37:50"
slug: "ios-zhuang-tai-lan-cao-zuo-shou-ji"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/iOS-状态栏操作（收集）/"
  - "/2025/06/16/iOS-状态栏操作（收集）.html"
  - "/iOS-状态栏操作（收集）/"
  - "/iOS-状态栏操作（收集）.html"
  - "/2025/06/16/iOS-状态栏操作-收集/"
  - "/2025/06/16/iOS-状态栏操作-收集.html"
  - "/2025/06/16/ios-zhuang-tai-lan-cao-zuo-shou-ji/"
  - "/2025/06/16/ios-zhuang-tai-lan-cao-zuo-shou-ji.html"
  - "/ios-zhuang-tai-lan-cao-zuo-shou-ji.html"
---
让状态栏显示网络等待标志

```objectivec
[UIApplication sharedApplication].networkActivityIndicatorVisible = YES; //显示  
[UIApplication sharedApplication].networkActivityIndicatorVisible = NO; //隐藏
```

状态栏是可以通过UIApplication类提供的一些方法来修改的，比如完全去掉状态栏或者修改风格，不过这些改变只是在你的程序内部，当你退出你的程序又会复原。

```objectivec
UIApplication *myApp = [UIapplication sharedApplication];
```

1.隐藏状态栏

```objectivec
[myApp setStatusBarHidden:YES animated:YES];
```

记得隐藏状态栏后的你的“桌面”就增加320×20的大小，所以最好是在任何window或者view创建之前隐藏它。  
2.状态栏风格

```objectivec
[myApp setStatusBarStyle: UIStatusbarStyleBlackOpaque];  
typedef enum {  
        UIStatusBarStyleDefault,  
        UIStatusBarStyleBlackTranslucent,  
        UIStatusBarStyleBlackOpaque  
    } UIStatusBarStyle;
```

3.状态栏方向

```objectivec
[myApp setStatusBarOrientation:UIInterfaceOrientationLandscapeLeft animated:NO];  
typedef enum {  
     UIInterfaceOrientationPortrait           = UIDeviceOrientationPortrait,  
     //竖屏，垂直向上  
     UIInterfaceOrientationPortraitUpsideDown = UIDeviceOrientationPortraitUpsideDown,  
     //竖屏，垂直方向上下颠倒  
     UIInterfaceOrientationLandscapeLeft      = UIDeviceOrientationLandscapeRight,  
     //设备逆时针旋转到横屏模式  
     UIInterfaceOrientationLandscapeRight     = UIDeviceOrientationLandscapeLeft  
     //设备顺时针旋转到横屏模式  
   } UIInterfaceOrientation;
```

有时候，需要在状态栏上显示一些自定义信息，比如新浪微博的官方iOS客户端：告知用户信息处于发送队列、发送成功或者发送失败。  
  
通过在状态栏显示自定义信息，可以给用户友好又不影响软件使用的提示。  
为此，我们显得定义一个自定义状态栏类，包含一个显示信息的Label：

```objectivec
@interface CustomStatusBar : UIWindow  
{  
    UILabel *_messageLabel;  
}  
  
- (void)showStatusMessage:(NSString *)message;  
- (void)hide;  
  
@end
```

接着，设置大小和系统状态栏一致，背景为黑色：

```objectivec
self.frame = [UIApplication sharedApplication].statusBarFrame;  
self.backgroundColor = [UIColor blackColor];
```

到这里，为了让自定义的状态栏可以让用户看到，还需要设置它的windowLevel。  
在iOS中，windowLevel属性决定了UIWindow的显示层次。默认的windowLevel为UIWindowLevelNormal，即0.0。  
系统定义了三个层次如下，具体可参考官方文档：

```objectivec
const UIWindowLevel UIWindowLevelNormal;  
const UIWindowLevel UIWindowLevelAlert;  
const UIWindowLevel UIWindowLevelStatusBar;  
typedef CGFloat UIWindowLevel;
```

为了能够覆盖系统默认的状态栏，我们把自定义的状态栏的windowLevel调高点：

```objectivec
self.windowLevel = UIWindowLevelStatusBar + 1.0f;
```

最后，为显示信息和隐藏添加一点无伤大雅的动画：

```objectivec
- (void)showStatusMessage:(NSString *)message  
{  
    self.hidden = NO;  
    self.alpha = 1.0f;  
    _messageLabel.text = @"";  
      
    CGSize totalSize = self.frame.size;  
    self.frame = (CGRect){ self.frame.origin, 0, totalSize.height };  
      
    [UIView animateWithDuration:0.5f animations:^{  
        self.frame = (CGRect){ self.frame.origin, totalSize };  
    } completion:^(BOOL finished){  
        _messageLabel.text = message;  
    }];  
}  
  
- (void)hide  
{  
    self.alpha = 1.0f;  
      
    [UIView animateWithDuration:0.5f animations:^{  
        self.alpha = 0.0f;  
    } completion:^(BOOL finished){  
        _messageLabel.text = @"";  
        self.hidden = YES;  
    }];;  
}
```
