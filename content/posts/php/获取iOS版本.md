---
title: "获取iOS版本"
date: "2025-06-23 15:49:28"
slug: "huo-qu-ios-ban-ben"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/获取iOS版本/"
  - "/2025/06/23/获取iOS版本.html"
  - "/获取iOS版本/"
  - "/获取iOS版本.html"
  - "/2025/06/23/huo-qu-ios-ban-ben/"
  - "/2025/06/23/huo-qu-ios-ban-ben.html"
  - "/huo-qu-ios-ban-ben.html"
---
如果你想开发一个同时支持IOS2和IOS3的应用，那你就需要获取当前的IOS版本了。因为IOS2中的部分方法在IOS3中已被移除。  
  
例如，在旋转开始之后，最后的旋转动画发生之前将会自动调用willAnimateRotationToInterfaceOrientation:duration:方法，而该方法是IOS3中新增的方法，在以前的SDK版本中，可以使用willAnimateSecondHalfOfRotationFromInterfaceOrientation:duration:方法，但是，IOS3以前的版本中使用的两段式动画比willAnimateRotationToInterfaceOrientation:duration:方法要慢得多，所以应避免这些方法，除非确实需要在应用程序中支持旧的IOS版本。  
  
用宏指令判断版本号：

```objectivec
#ifdef __IPHONE_6_0  
// code  
#else  
// code  
#endif
```

示例：

```objectivec
#ifdef __IPHONE_6_0  
- (void)willAnimateRotationToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation duration:(NSTimeInterval)duration {  
#else  
- (void)willAnimateSecondHalfOfRotationFromInterfaceOrientation: (UIInterfaceOrientation)fromInterfaceOrientation duration:(NSTimeInterval)duration {  
#endif  
}
```

你还可以通过以下方法获取IOS的版本：

```objectivec
[UIDevice currentDevice].systemVersion
```

这将会返回IOS的当前版本。  
  
在方法体中判断：

```objectivec
if([[UIDevice currentDevice].systemVersion doubleValue] >= 6.0){
    //你的逻辑
}
```

