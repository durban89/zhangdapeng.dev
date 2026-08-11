---
title: "iOS NSDateFormatter格式详细列表"
date: "2025-06-11 11:09:48"
slug: "ios-nsdateformatter-ge-shi-xiang-xi-lie-biao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-NSDateFormatter格式详细列表/"
  - "/2025/06/11/iOS-NSDateFormatter格式详细列表.html"
  - "/iOS-NSDateFormatter格式详细列表/"
  - "/iOS-NSDateFormatter格式详细列表.html"
  - "/2025/06/11/ios-nsdateformatter-ge-shi-xiang-xi-lie-biao/"
  - "/2025/06/11/ios-nsdateformatter-ge-shi-xiang-xi-lie-biao.html"
  - "/ios-nsdateformatter-ge-shi-xiang-xi-lie-biao.html"
---
iOS开发中NSDateFormatter是一个很常用的类，用于格式化NSDate对象，支持本地化的信息。与时间相关的功能还可能会用到NSDateComponents类和NSCalendar类等。本文主要列出NSDateFormatter常见用法。

NSDate对象包含两个部分，日期（Date）和时间（Time）。格式化的时间字符串主要也是针对日期和时间的。[以下代码中开启了ARC，所以没有release。]

### [基础用法](#1)

```objectivec
NSDate* now = [NSDate date];
NSDateFormatter* fmt = [[NSDateFormatter alloc] init];
fmt.dateStyle = kCFDateFormatterShortStyle;
fmt.timeStyle = kCFDateFormatterShortStyle;
fmt.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
NSString* dateString = [fmt stringFromDate:now];
NSLog(@"%@", dateString);
```

打印输出：10/29/12, 2:27 PM  
这使用的系统提供的格式化字符串，通过 fmt.dateStyle 和 fmt.timeStyle 进行的设置。实例中使用的参数是 kCFDateFormatterShortStyle，此外还有：

```objectivec
typedef CF_ENUM(CFIndex, CFDateFormatterStyle) {    // date and time format styles
    kCFDateFormatterNoStyle = 0,       // 无输出
    kCFDateFormatterShortStyle = 1,    // 10/29/12, 2:27 PM
    kCFDateFormatterMediumStyle = 2,   // Oct 29, 2012, 2:36:59 PM
    kCFDateFormatterLongStyle = 3,     // October 29, 2012, 2:38:46 PM GMT+08:00
    kCFDateFormatterFullStyle = 4      // Monday, October 29, 2012, 2:39:56 PM China Standard Time
};
```

### [自定义区域语言](#2)

如上实例中，我们使用的是区域语言是 en\_US，指的是美国英语。如果我们换成简体中文，则代码是：

```objectivec
fmt.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"zh_CN"];
```

则对应的输出为：

```objectivec
typedef CF_ENUM(CFIndex, CFDateFormatterStyle) {    // date and time format styles
    kCFDateFormatterNoStyle = 0,       // 无输出
    kCFDateFormatterShortStyle = 1,    // 12-10-29 下午2:52
    kCFDateFormatterMediumStyle = 2,   // 2012-10-29 下午2:51:43
    kCFDateFormatterLongStyle = 3,     // 2012年10月29日 GMT+0800下午2时51分08秒
    kCFDateFormatterFullStyle = 4      // 2012年10月29日星期一 中国标准时间下午2时46分49秒
};
```

世界通用的区域语言代码，详见 International Components for Unicode (ICU), <http://userguide.icu-project.org/formatparse/datetime>

### [自定义日期时间格式](#3)

NSDateFormatter提供了自定义日期时间的方法，主要是通过设置属性 dateFormat，常见的设置如下：

```objectivec
NSDate* now = [NSDate date];
NSDateFormatter* fmt = [[NSDateFormatter alloc] init];
fmt.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"zh_CN"];
fmt.dateFormat = @"yyyy-MM-dd'T'HH:mm:ss";
NSString* dateString = [fmt stringFromDate:now];
NSLog(@"%@", dateString);
```

打印输出：2012-10-29T16:08:40  
除了上面列出的，还可以指定很多格式，详见http://userguide.icu-project.org/formatparse/datetime。  
结合设置Locale，还可以打印出本地化的字符串信息。

```objectivec
NSDate* now = [NSDate date];
NSDateFormatter* fmt = [[NSDateFormatter alloc] init];
fmt.locale = [[NSLocale alloc] initWithLocaleIdentifier:@"zh_CN"];
fmt.dateFormat = @"yyyy-MM-dd a HH:mm:ss EEEE";
NSString* dateString = [fmt stringFromDate:now];
NSLog(@"\n%@", dateString);
```

### [自定义月份星期等字符](#4)

NSDateFormatter中同样提供了相应的方式，去修改这些字符。一般情况下，使用相应区域语言下面的默认字符就OK了。但是你的确有这个需求，那么也是可以办到的。相应的方法非常多，如下：  
Managing AM and PM Symbols  
– AMSymbol  
– setAMSymbol:  
– PMSymbol  
– setPMSymbol:  
  
Managing Weekday Symbols  
– weekdaySymbols  
– setWeekdaySymbols:  
– shortWeekdaySymbols  
– setShortWeekdaySymbols:  
– veryShortWeekdaySymbols  
– setVeryShortWeekdaySymbols:  
– standaloneWeekdaySymbols  
– setStandaloneWeekdaySymbols:  
– shortStandaloneWeekdaySymbols  
– setShortStandaloneWeekdaySymbols:  
– veryShortStandaloneWeekdaySymbols  
– setVeryShortStandaloneWeekdaySymbols:  
  
Managing Month Symbols  
– monthSymbols  
– setMonthSymbols:  
– shortMonthSymbols  
– setShortMonthSymbols:  
– veryShortMonthSymbols  
– setVeryShortMonthSymbols:  
– standaloneMonthSymbols  
– setStandaloneMonthSymbols:  
– shortStandaloneMonthSymbols  
– setShortStandaloneMonthSymbols:  
– veryShortStandaloneMonthSymbols  
– setVeryShortStandaloneMonthSymbols:  
  
Managing Quarter Symbols  
– quarterSymbols  
– setQuarterSymbols:  
– shortQuarterSymbols  
– setShortQuarterSymbols:  
– standaloneQuarterSymbols  
– setStandaloneQuarterSymbols:  
– shortStandaloneQuarterSymbols  
– setShortStandaloneQuarterSymbols:  
  
Managing Era Symbols  
– eraSymbols  
– setEraSymbols:  
– longEraSymbols  
– setLongEraSymbols:
