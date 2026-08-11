---
title: "nil,Nil,NULL 和NSNull的学习"
date: "2025-06-13 15:32:36"
slug: "nilnilnull-he-nsnull-de-xue-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/nil,Nil,NULL-和NSNull的学习/"
  - "/2025/06/13/nil,Nil,NULL-和NSNull的学习.html"
  - "/nil,Nil,NULL-和NSNull的学习/"
  - "/nil,Nil,NULL-和NSNull的学习.html"
  - "/2025/06/13/nil-Nil-NULL-和NSNull的学习/"
  - "/2025/06/13/nil-Nil-NULL-和NSNull的学习.html"
  - "/2025/06/13/nilnilnull-he-nsnull-de-xue-xi/"
  - "/2025/06/13/nilnilnull-he-nsnull-de-xue-xi.html"
  - "/nilnilnull-he-nsnull-de-xue-xi.html"
---
1.object-c最好 用nil [nil 任意方法],不会崩溃  
`nil` 是一个对象值。  
`NULL` 是一个通用指针（泛型指针）。  
  
2. NSNULL，NULL和nil在本质上应该是一样的，NULL和nil其实就是0，但是在Objective-c中，对于像NSArray这样的类型，nil或NULL不能做为加到其中的Object，如果定义了一个NSArray，为其分配了内存，又想设置其中的内容为空，则可以用[NSNULL null返回的对象来初始化NSArray中的内容，  
3.因为在NSArray和NSDictionary中nil中有特殊的含义（表示列表结束），所以不能在集合中放入nil值。如要确实需要存储一个表示“什么都没有”的值，可以使用NSNull类。NSNull只有一个方法：

- `+ (NSNull *) null;`

因为Object-C的集合对象，如NSArray、NSDictionary、NSSet等，都有可能包含NSNull对象，所以，如果一下代码中的item为NSNull，则会引起程序崩溃。  
  
以下代码是常见的错误，release对象没有设置为nil，从而引起程序崩溃。

```objectivec
NSString *item=[NSArray objectAtIndex:i];
if([item isEqualToString:@"TestNumber"])
{
//
}
```

```objectivec
id someObject=[[Object alloc] init];
//...
[someObject release];
//...
if(someObject)
{
//crash here
}
```

nil用来给对象赋值（Object-C的任何对象都属于id类型），NULL则给任何指针赋值，NULL和nil不能互换，nil用于类指针赋值（在Object-C中类是一个对象，是类的meta-class的实例），而NSNull则用于集合操作，虽然它们表示的都是空值，但是使用场合完全不同，所以在编码时严格按照变量类型来赋值，将正确的空值赋给正确的类型，使代码易于阅读和维护，也不易引起错误。

```objectivec
//判断对象不空
if(object) {}

//判断对象为空
if(object == nil) {}

//数组初始化，空值结束
NSArray *pageNames=[[NSArray alloc] initWithObjects:@"DocumentList",@"AdvancedSearch",@"Statistics",nil];

//判断数组元素是否为空
UIViewController *controller=[NSArray objectAtIndex:i];
if((NSNull *)controller == [NSNull null])
{
//
}

//判断字典对象的元素是否为空
NSString *userId=[NSDictionary objectForKey:@"UserId"];
if(userId == [NSNull null])
{
//
}
```

Object-C有个可爱的特性，就是当发消息给nil对象时，系统返回0值而不是引起异常，这和JAVA烦人的NullPointerException以及C/C++的程序直接崩溃的处理完全不一样，明白Object-C的这个特性对于开发正确的IOS程序非常重要，因为nil是对象的合法值，nil对象同样可以接收消息，例如：

```objectivec
person=nil;
[person castBallot];
NSLog("person=%@",person);
```

对象置空，然后发送消息，程序同样接着往下执行而不会崩溃。
