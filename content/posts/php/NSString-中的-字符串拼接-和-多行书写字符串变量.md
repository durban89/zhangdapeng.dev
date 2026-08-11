---
title: "NSString 中的 字符串拼接 和 多行书写字符串变量"
date: "2025-06-27 10:25:46"
slug: "nsstring-zhong-de-zi-fu-chuan-pin-jie-he-duo-xing-shu-xie-zi-fu-chuan-bian-liang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/NSString-中的-字符串拼接-和-多行书写字符串变量/"
  - "/2025/06/27/NSString-中的-字符串拼接-和-多行书写字符串变量.html"
  - "/NSString-中的-字符串拼接-和-多行书写字符串变量/"
  - "/NSString-中的-字符串拼接-和-多行书写字符串变量.html"
  - "/2025/06/27/nsstring-zhong-de-zi-fu-chuan-pin-jie-he-duo-xing-shu-xie-zi-fu-chuan-bian-liang/"
  - "/2025/06/27/nsstring-zhong-de-zi-fu-chuan-pin-jie-he-duo-xing-shu-xie-zi-fu-chuan-bian-liang.html"
  - "/nsstring-zhong-de-zi-fu-chuan-pin-jie-he-duo-xing-shu-xie-zi-fu-chuan-bian-liang.html"
---
#### [字符串拼接](#1)

```objectivec
NSString *str1 = @"我是durban";
NSString *str2 = @"我是wenwen";
NSString *result;
//方法1
result = [str1 stringByAppendingString:str2];
NSLog(result, nil);
//方法2
result = [NSString stringWithFormat:@"%@%@", str1, str2];
NSLog(result, nil);
//方法3
result = [@"" stringByAppendingFormat:@"%@%@", str1, str2];
NSLog(result, nil);
//方法4
NSMutableString *ms = [[NSMutableString alloc] init];
[ms appendString:str1];
[ms appendString:str2];
NSLog(ms, nil);
[ms release];
    
//结果都是：我是durban我是wenwen
```

一般推荐使用方法1，如果需要大量字符串连接推荐使用方法4，需要更少的内存开销。

#### [多行书写字符串变量](#2)

```objectivec
NSString *str1 = @"SELECT [CustomerID], [CustomerName] "

"FROM [Customer] "

"WHERE [CustomerName] LIKE '%durban%'";



NSString *str2 = @"SELECT [CustomerID], [CustomerName] \

FROM [Customer] \

WHERE [CustomerName] LIKE '%durban%'";



NSLog(str1, nil);

NSLog(str2, nil);



//结果都是：SELECT [CustomerID], [CustomerName] FROM [Customer] WHERE [CustomerName] LIKE '%durban%'
```

注意字符串中每行结尾处的空格。这种字符串声明方式虽然看上去是多行，实际上字符串中并没有换行符，也就是说整个字符串实际上是一行。如果需要在字符串中换行，可以在字符串中加入换行符"\n"。这种声明方式一般用在需要在代码中多行显示字符串以便提高可读性，例如：SQL语句往往需要多行显示来提高可读性、较长的文本的段落之间需要分行显示以便更容易找到分段位置。

