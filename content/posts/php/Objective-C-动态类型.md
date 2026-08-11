---
title: "Objective-C 动态类型"
date: "2025-06-13 14:03:15"
slug: "objective-c-dong-tai-lei-xing"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/13/Objective-C-动态类型/"
  - "/2025/06/13/Objective-C-动态类型.html"
  - "/Objective-C-动态类型/"
  - "/Objective-C-动态类型.html"
  - "/2025/06/13/objective-c-dong-tai-lei-xing/"
  - "/2025/06/13/objective-c-dong-tai-lei-xing.html"
  - "/objective-c-dong-tai-lei-xing.html"
---
### [判断对象类型1](#1)

`-(BOOL) isKindOfClass: classObj` 判断是否是这个类或者这个类的子类的实例

`-(BOOL) isMemberOfClass: classObj` 判断是否是这个类的实例

使用方法：

```objectivec
//YES   
if ([teacher isKindOfClass:[Teacher class]]) {  
	NSLog(@"teacher 是 Teacher类或Teacher的子类");  
}  
//YES   
if ([teacher isKindOfClass:[Person class]]) {  
	NSLog(@"teacher 是 Person类或Person的子类");  
}  
//YES   
if ([teacher isKindOfClass:[NSObject class]]) {  
	NSLog(@"teacher 是 NSObject类或NSObject的子类");  
}  

//YES   
if ([teacher isMemberOfClass:[Teacher class]]) {  
	NSLog(@"teacher Teacher类的成员");  
}  
//NO   
if ([teacher isMemberOfClass:[Person class]]) {  
	NSLog(@"teacher Person类的成员");  
}  
//NO   
if ([teacher isMemberOfClass:[NSObject class]]) {  
	NSLog(@"teacher NSObject类的成员");  
}
```

### [判断对象类型2](#2)

`-(BOOL) respondsToSelector: selector` 判断实例是否有这样方法

`+(BOOL) instancesRespondToSelector:` 判断类是否有这个方法。此方法是类方法，不能用在类的对象

使用方法

```objectivec
// YES   
if ( [teacher respondsToSelector: @selector( setName: )] == YES ) {  
	NSLog(@"teacher responds to setSize: method" );  
}  
// NO   
if ( [teacher respondsToSelector: @selector( abcde )] == YES ) {  
	NSLog(@"teacher responds to nonExistant method" );  
}  
// YES   
if ( [Teacher respondsToSelector: @selector( alloc )] == YES ) {  
	NSLog(@"teacher class responds to alloc method\n" );  
}  
// NO   
if ( [Person instancesRespondToSelector: @selector(teach)] == YES ) {  
	NSLog(@"Person instance responds to teach method" );  
}  
// YES   
if ( [Teacher instancesRespondToSelector: @selector(teach)] == YES ) {  
	NSLog(@"Teacher instance responds to teach method");  
}  
// YES   
if ( [Teacher instancesRespondToSelector: @selector(setName:)] == YES ) {  
	NSLog(@"Teacher instance responds to setName: method" );  
}
```

### [Objective-C的id类型](#3)

C++ 使用的是强类型：对象必须符合其类型，否则不能通过编译。在 Objective-C 中，id类型类似于(void*) ,可以指向任何类的实例。而不需要强制转换。  
实例如下：

```objectivec
Person *person = [[Person alloc] init];  
Teacher *teacher = [[Teacher alloc] init];  
  
id p = person;  
id t = teacher;
```
