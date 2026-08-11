---
title: "iOS UIAlertView屏幕闪烁问题"
date: "2025-06-17 14:43:40"
slug: "ios-uialertview-ping-mu-shan-shuo-wen-ti"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/17/iOS-UIAlertView屏幕闪烁问题/"
  - "/2025/06/17/iOS-UIAlertView屏幕闪烁问题.html"
  - "/iOS-UIAlertView屏幕闪烁问题/"
  - "/iOS-UIAlertView屏幕闪烁问题.html"
  - "/2025/06/17/ios-uialertview-ping-mu-shan-shuo-wen-ti/"
  - "/2025/06/17/ios-uialertview-ping-mu-shan-shuo-wen-ti.html"
  - "/ios-uialertview-ping-mu-shan-shuo-wen-ti.html"
---
关于这个问题，我查找过了很多资料

最终的解决办法是：将UIAlertView在主线程上展现出来

实现过程如下：

```objectivec
+(void) showNetworkMessage
{
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"网络连接异常"
                                                    message:@"暂无法访问寻艺"
                                                   delegate:self
                                          cancelButtonTitle:@"确定"
                                          otherButtonTitles:nil];
    [alert performSelectorOnMainThread:@selector(show) withObject:nil waitUntilDone:YES];
}
```

然后在后面直接调用就可以了
