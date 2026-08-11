---
title: "NSDateFormatter setDateFormat 自定义日期/时间格式"
date: "2025-06-13 11:34:56"
slug: "nsdateformatter-setdateformat-zi-ding-yi-ri-qi-shi-jian-ge-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/NSDateFormatter-setDateFormat-自定义日期/时间格式/"
  - "/2025/06/13/NSDateFormatter-setDateFormat-自定义日期/时间格式.html"
  - "/NSDateFormatter-setDateFormat-自定义日期/时间格式/"
  - "/NSDateFormatter-setDateFormat-自定义日期/时间格式.html"
  - "/2025/06/13/NSDateFormatter-setDateFormat-自定义日期-时间格式/"
  - "/2025/06/13/NSDateFormatter-setDateFormat-自定义日期-时间格式.html"
  - "/2025/06/13/nsdateformatter-setdateformat-zi-ding-yi-ri-qi-shi-jian-ge-shi/"
  - "/2025/06/13/nsdateformatter-setdateformat-zi-ding-yi-ri-qi-shi-jian-ge-shi.html"
  - "/nsdateformatter-setdateformat-zi-ding-yi-ri-qi-shi-jian-ge-shi.html"
---
NSDateFormatter自定义日期/时间格式 ,简单的举一个例子，看下面的代码就可以了

```objectivec
NSDate *dateValue = [NSDate date];
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateFormat:@"yyyy-MM-dd"];
dateValue = ((UIDatePicker *)sender).date;

self.teleplayDate.text = [dateFormatter stringFromDate:dateValue];//[NSString stringWithFormat:@"%@",dateValue];
self.wantToSaveTeleplayDate = self.teleplayDate.text;
```

下面附上几个格式：

```bash
yyyy:MM:dd G 'at' HH:mm:ss zzz      1996.07.10 AD at 15:08:56 PDT  
EEE, MMM d, "yy                     Wed,july 10, '99  
h:mm a                           12:08 PM  
hh 'o"clock' a,zzzz                   12 o'clock PM, Pacific Daylight Time  
K:mm a, z                         0:00 PM, PST  
yyyyy,MMMM.dd GGG hh:mm aaa        01996.july.10 AD 12:08 PM  
```
  
下面是得到当前的年，月，日，时，分，秒。  

```objectivec
NSCalendar *cal = [NSCalendar currentCalendar];  
unsigned int unitFlags = NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit | NSHourCalendarUnit | NSMinuteCalendarUnit | NSSecondCalendarUnit;  
NSDateComponents *dd = [cal components:unitFlags fromDate:date];  
int y = [dd year];  
int m = [dd month];  
int d = [dd day];  
int h = [dd hour];  
int m = [dd minute];  
int s = [dd second];
```

当然不止这些的，有兴趣的可以去参考一下：http://unicode.org/reports/tr35/tr35-6.html#Date\_Format\_Patterns
