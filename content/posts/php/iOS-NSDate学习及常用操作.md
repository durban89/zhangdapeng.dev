---
title: "iOS NSDate学习及常用操作"
date: "2025-06-13 13:40:03"
slug: "ios-nsdate-xue-xi-ji-chang-yong-cao-zuo"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-NSDate学习及常用操作/"
  - "/2025/06/13/iOS-NSDate学习及常用操作.html"
  - "/iOS-NSDate学习及常用操作/"
  - "/iOS-NSDate学习及常用操作.html"
  - "/2025/06/13/ios-nsdate-xue-xi-ji-chang-yong-cao-zuo/"
  - "/2025/06/13/ios-nsdate-xue-xi-ji-chang-yong-cao-zuo.html"
  - "/ios-nsdate-xue-xi-ji-chang-yong-cao-zuo.html"
---
### [创建或初始化可用以下方法](#1)

#### [用于创建NSDate实例的类方法有](#1-1)

- `+ (id)date;  `
返回当前时间  

- `+ (id)dateWithTimeIntervalSinceNow:(NSTimeInterval)secs;`
返回以当前时间为基准，然后过了secs秒的时间,这里的值可以为负值  

- `+ (id)dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval)secs;  `
返回以2001/01/01 GMT为基准，然后过了secs秒的时间，这里的值可以为负值  

- `+ (id)dateWithTimeIntervalSince1970:(NSTimeInterval)secs;  `
返回以1970/01/01 GMT为基准，然后过了secs秒的时间，这里的值可以为负值  

- `+ (id)distantFuture;  `
返回很多年以后的未来的某一天。（比如你需要一个比现在(Now)晚(大)很长时间的时间值，则可以调用该方法。测试返回了4000/12/31 16:00:00）  

- `+ (id)distantPast;  `
返回很多年以前的某一天。（比如你需要一个比现在(Now)早(小)大很长时间的时间值，则可以调用该方法。测试返回了公元前0001/12/31 17:00:00）

#### [用于创建NSDate实例的实例方法有](#1-1-1)

- `- (id)addTimeInterval:(NSTimeInterval)secs;  `
返回以目前的实例中保存的时间为基准，然后过了secs秒的时间，这里的值可以为负值

#### [用于初始化NSDate实例的实例方法有](#1-2)

- `- (id)init;  `
初始化为当前时间。类似date方法  
初始化为以2001/01/01 GMT为基准，然后过了secs秒的时间。类似dateWithTimeIntervalSinceReferenceDate:方法  

- `- (id)initWithTimeInterval:(NSTimeInterval)secs sinceDate:(NSDate *)refDate; ` 
初始化为以refDate为基准，然后过了secs秒的时间，这里的值可以为负值  

- `- (id)initWithTimeIntervalSinceNow:(NSTimeInterval)secs;  `
初始化为以当前时间为基准，然后过了secs秒的时间，这里的值可以为负值

### [日期之间比较可用以下方法](#2)

- `- (BOOL)isEqualToDate:(NSDate *)otherDate; ` 
与otherDate比较，相同返回YES  

- `- (NSDate *)earlierDate:(NSDate *)anotherDate; ` 
与anotherDate比较，返回较早的那个日期  

- `- (NSDate *)laterDate:(NSDate *)anotherDate; ` 
与anotherDate比较，返回较晚的那个日期 

- `- (NSComparisonResult)compare:(NSDate *)other;`
该方法用于排序时调用:
- 当实例保存的日期值与anotherDate相同时返回NSOrderedSame  
- 当实例保存的日期值晚于anotherDate时返回NSOrderedDescending  
- 当实例保存的日期值早于anotherDate时返回NSOrderedAscending

### [取回时间间隔可用以下方法](#3)

- `- (NSTimeInterval)timeIntervalSinceDate:(NSDate \*)refDate;  `
以refDate为基准时间，返回实例保存的时间与refDate的时间间隔  

- `- (NSTimeInterval)timeIntervalSinceNow; ` 
以当前时间(Now)为基准时间，返回实例保存的时间与当前时间(Now)的时间间隔 

- `- (NSTimeInterval)timeIntervalSince1970;  `
以1970/01/01 GMT为基准时间，返回实例保存的时间与1970/01/01 GMT的时间间隔  

- `- (NSTimeInterval)timeIntervalSinceReferenceDate; ` 
以2001/01/01 GMT为基准时间，返回实例保存的时间与2001/01/01 GMT的时间间隔  

- `+ (NSTimeInterval)timeIntervalSinceReferenceDate; ` 
以2001/01/01 GMT为基准时间，返回当前时间(Now)与2001/01/01 GMT的时间间隔


### [将时间表示成字符串](#4)

- `- (NSString *)description;  `
以YYYY-MM-DD HH:MM:SS ±HHMM的格式表示时间。（其中 "±HHMM" 表示与GMT的存在多少小时多少分钟的时区差异。比如，若时区设置在北京，则 "±HHMM" 显示为 "+0800"）
