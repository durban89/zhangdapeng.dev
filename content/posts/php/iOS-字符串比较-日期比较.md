---
title: "iOS 字符串比较 日期比较"
date: "2025-06-19 10:29:06"
slug: "ios-zi-fu-chuan-bi-jiao-ri-qi-bi-jiao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS-字符串比较-日期比较/"
  - "/2025/06/19/iOS-字符串比较-日期比较.html"
  - "/iOS-字符串比较-日期比较/"
  - "/iOS-字符串比较-日期比较.html"
  - "/2025/06/19/ios-zi-fu-chuan-bi-jiao-ri-qi-bi-jiao/"
  - "/2025/06/19/ios-zi-fu-chuan-bi-jiao-ri-qi-bi-jiao.html"
  - "/ios-zi-fu-chuan-bi-jiao-ri-qi-bi-jiao.html"
---
字符串比较

```objectivec
//字符串比较
NSString *string = @"hello nihao";
NSString *otherString = @"hello niyeyao";
if([string compare:otherString] == NSOrderedAscending){
    NSLog(@"我比你大");
}else{
    NSLog(@"我是小三");
}
```

日期比较

```objectivec
//日期比较
NSDate *nowDate = [NSDate date];
NSDate *yesterdayDate = [[NSDate alloc] initWithTimeIntervalSinceNow:-24 * 60 * 60];
if([nowDate compare:yesterdayDate] == NSOrderedAscending){
    NSLog(@"我是今天");
}else{
    NSLog(@"我是我昨天");
}
```

当然这里也可以，将指定的字符串转换为时间进行比较，字符串的时间格式要跟自己设定的时间格式相对应

```objectivec
//日期比较
NSString *nowDateString = @"2013/7/13";
NSString *yesterdayDateString = @"2013/7/12";
NSDateFormatter *dateFromatter = [[NSDateFormatter alloc] init];
[dateFromatter setDateFormat:@"yy/MM/dd"];
NSDate *nowDate = [dateFromatter dateFromString:nowDateString];
NSDate *yesterdayDate = [dateFromatter dateFromString:yesterdayDateString];

if([nowDate compare:yesterdayDate] == NSOrderedAscending){
    NSLog(@"我是今天");
}else{
    NSLog(@"我是我昨天");
}
```

结果他的表现就是

```objectivec
2013-07-20 18:18:03.165 寻艺[90532:c07] 我比你大
2013-07-20 18:18:03.168 寻艺[90532:c07] 我是我昨天
```

这里需要注意的就是

NSOrderedAscending

我们在Xcode定位的话

会找到这样的代码

```objectivec
typedef NS_ENUM(NSInteger, NSComparisonResult) {NSOrderedAscending = -1L, NSOrderedSame, NSOrderedDescending};
```

结果 跟 -1 0 1应该是一样的。
