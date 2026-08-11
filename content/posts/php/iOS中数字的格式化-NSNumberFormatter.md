---
title: "iOS中数字的格式化 NSNumberFormatter"
date: "2025-06-17 16:46:10"
slug: "ios-zhong-shu-zi-de-ge-shi-hua-nsnumberformatter"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS中数字的格式化-NSNumberFormatter/"
  - "/2025/06/17/iOS中数字的格式化-NSNumberFormatter.html"
  - "/iOS中数字的格式化-NSNumberFormatter/"
  - "/iOS中数字的格式化-NSNumberFormatter.html"
  - "/2025/06/17/ios-zhong-shu-zi-de-ge-shi-hua-nsnumberformatter/"
  - "/2025/06/17/ios-zhong-shu-zi-de-ge-shi-hua-nsnumberformatter.html"
  - "/ios-zhong-shu-zi-de-ge-shi-hua-nsnumberformatter.html"
---
最近搞数据展示，需要将数字展示为用千分号分割的字符串，让我好找呀，结果还是被我找到了。

在iOS中我们可以通过NSDateFormatter来设置输出NSDate的格式。相比NSDateFormatter的大名鼎鼎，NSNumberFormatter好像知道的人就不多了。其实通过NSNumberFormatter，同样可以设置NSNumber输出的格式。例如如下代码：

```objectivec
NSNumberFormatter *formatter = [[NSNumberFormatter alloc] init];
formatter.numberStyle = NSNumberFormatterDecimalStyle;
NSString *string = [formatter stringFromNumber:[NSNumber numberWithInt:123456789]];
NSLog(@"Formatted number string:%@",string);
```

输出结果为：`[1223:403] Formatted number string:123,456,789`

其中NSNumberFormatter类有个属性numberStyle，它是一个枚举型，设置不同的值可以输出不同的数字格式。该枚举包括：  
**enum {**  
**NSNumberFormatterNoStyle = kCFNumberFormatterNoStyle,**  
**NSNumberFormatterDecimalStyle = kCFNumberFormatterDecimalStyle,**  
**NSNumberFormatterCurrencyStyle = kCFNumberFormatterCurrencyStyle,**  
**NSNumberFormatterPercentStyle = kCFNumberFormatterPercentStyle,**  
**NSNumberFormatterScientificStyle = kCFNumberFormatterScientificStyle,**  
**NSNumberFormatterSpellOutStyle = kCFNumberFormatterSpellOutStyle**  
**};**  
typedef NSUInteger NSNumberFormatterStyle;

各个枚举对应输出数字格式的效果如下：

```bash
[1243:403] Formatted number string:123456789
[1243:403] Formatted number string:123,456,789
[1243:403] Formatted number string:￥123,456,789.00
[1243:403] Formatted number string:-539,222,988%
[1243:403] Formatted number string:1.23456789E8
[1243:403] Formatted number string:一亿二千三百四十五万六千七百八十九
```

其中第三项和最后一项的输出会根据系统设置的语言区域的不同而不同。
