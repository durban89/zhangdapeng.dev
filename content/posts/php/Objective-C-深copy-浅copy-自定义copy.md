---
title: "Objective-C 深copy 浅copy 自定义copy"
date: "2025-06-25 10:26:11"
slug: "objective-c-shen-copy-qian-copy-zi-ding-yi-copy"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/25/Objective-C-深copy-浅copy-自定义copy/"
  - "/2025/06/25/Objective-C-深copy-浅copy-自定义copy.html"
  - "/Objective-C-深copy-浅copy-自定义copy/"
  - "/Objective-C-深copy-浅copy-自定义copy.html"
  - "/2025/06/25/objective-c-shen-copy-qian-copy-zi-ding-yi-copy/"
  - "/2025/06/25/objective-c-shen-copy-qian-copy-zi-ding-yi-copy.html"
  - "/objective-c-shen-copy-qian-copy-zi-ding-yi-copy.html"
---
深copy指的是对象内的属性的copy，但是深copy的前提是，这个变量是可变的

浅copy值的是只copy对象

自定义copy调用的是NSCopying协议进行的copy

gowhich举了一个例子

第一个例子，看一下copy与retain的区别，来显示一下copy的作用

```objectivec
//retain操作
NSMutableArray *array = [[NSMutableArray alloc] initWithObjects:@"one",@"two",@"three", nil];
NSMutableArray *array1 = [array retain];
[array1 removeLastObject];

NSLog(@"array = %@",array);
NSLog(@"array retaincount = %ld",[array retainCount]);
NSLog(@"array1 = %@",array1);

//copy操作
NSMutableArray *copyArray = [[NSMutableArray alloc] initWithObjects:@"one",@"two",@"three", nil];
NSMutableArray *copyArray1 = [copyArray mutableCopy];
[copyArray1 removeLastObject];

NSLog(@"copyArray = %@",copyArray);
NSLog(@"copyArray1 %@",copyArray1);
```

得到的结果是：

```bash
2013-11-19 10:13:01.166 CopyDemo[73423:303] array = (
    one,
    two
)
2013-11-19 10:13:01.168 CopyDemo[73423:303] array retaincount = 2
2013-11-19 10:13:01.168 CopyDemo[73423:303] array1 = (
    one,
    two
)
2013-11-19 10:13:01.169 CopyDemo[73423:303] copyArray = (
    one,
    two,
    three
)
2013-11-19 10:13:01.169 CopyDemo[73423:303] copyArray1 (
    one,
    two
)
```

copy的结果是，copy后得到的对象的操作不影响源对象

第二个例子：copy的一般应用

```objectivec
//copy操作
NSArray *array3 = [NSArray arrayWithObjects:@"one",@"two",nil];
NSArray *array31 = [array3 copy];
NSMutableArray *array32 = [array3 mutableCopy];
[array32 addObject:@"three"];

NSLog(@"array3 = %@",array3);
NSLog(@"array31 = %@",array31);
NSLog(@"array32 = %@",array32);
```

得到的结果是：

```bash
2013-11-19 10:15:01.853 CopyDemo[73470:303] array3 = (
    one,
    two
)
2013-11-19 10:15:01.855 CopyDemo[73470:303] array31 = (
    one,
    two
)
2013-11-19 10:15:01.856 CopyDemo[73470:303] array32 = (
    one,
    two,
    three
)
```

第三个例子：一个简单的浅copy

```objectivec
//浅copy
NSMutableArray *array = [NSMutableArray array];
for(int i =0;i < 3;i++){
    NSObject *obj = [[NSObject alloc] init];
    [array addObject:obj];
    [obj release];
}

for (NSObject *obj in array) {
    NSLog(@"指针地址：%p, 应用计数：%ld",obj, obj.retainCount);
}

NSArray *array2 = [array copy];
for (NSObject *obj in array2) {
    NSLog(@"指针地址：%p, 应用计数：%ld",obj, obj.retainCount);
}
```

得到的结果是：

```bash
2013-11-19 10:16:07.092 CopyDemo[73505:303] 指针地址：0x100202590, 应用计数：1
2013-11-19 10:16:07.094 CopyDemo[73505:303] 指针地址：0x100202e70, 应用计数：1
2013-11-19 10:16:07.094 CopyDemo[73505:303] 指针地址：0x100202ec0, 应用计数：1
2013-11-19 10:16:07.095 CopyDemo[73505:303] 指针地址：0x100202590, 应用计数：2
2013-11-19 10:16:07.095 CopyDemo[73505:303] 指针地址：0x100202e70, 应用计数：2
2013-11-19 10:16:07.095 CopyDemo[73505:303] 指针地址：0x100202ec0, 应用计数：2
```

可以看出，里面的属性并没有改变，只是计数增加了。

第四个例子：看一下自定义的copy

先定义一个类，在类里面实现NSCopying协议的-(id)copyWithZone:(NSZone \*)zone;

Person.m

```objectivec
//
//  Person.m
//  CopyDemo
//
//  Created by Durban on 13-11-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@implementation Person

-(id)copyWithZone:(NSZone *)zone
{
    //浅copy - 第一种方法
//    Person *person = [[[self class] allocWithZone:zone] init];
//    person.name = _name;
//    person.age = _age;
//    return person;
    
    //浅copy - 第二种方法
//    Person *person = [[[self class] allocWithZone:zone] init];
//    person.name = [_name copy];
//    person.age = [_age copy];
//    return person;
    
    //深copy
    Person *person = [[[self class] allocWithZone:zone] init];
    person.name = [_name mutableCopy];
    person.age = [_age copy];//因为age是一个不可变变量
    return person;
}

@end
```

Person.h

```objectivec
//
//  Person.h
//  CopyDemo
//
//  Created by Durban on 13-11-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Person : NSObject<NSCopying>

@property (nonatomic,copy) NSString *name;
@property (nonatomic,retain) NSNumber *age;

@end
```

在main.m中调用

```objectivec
//深copy
Person *person = [[Person alloc] init];
person.name  = @"Durban";
person.age = @12;

Person *person2 = [person copy];

NSLog(@"person 的地址:%p",person);
NSLog(@"person2 的地址:%p",person2);

NSLog(@"person.name 的地址:%p",person.name);
NSLog(@"person2.name 的地址:%p",person2.name);

NSLog(@"person.age 的地址:%p",person.age);
NSLog(@"person2.age 的地址:%p",person2.age);
```

得到的结果是：

```bash
2013-11-19 10:21:34.246 CopyDemo[73625:303] person 的地址:0x100202e60
2013-11-19 10:21:34.248 CopyDemo[73625:303] person2 的地址:0x100200380
2013-11-19 10:21:34.249 CopyDemo[73625:303] person.name 的地址:0x100002350
2013-11-19 10:21:34.249 CopyDemo[73625:303] person2.name 的地址:0x100204650
2013-11-19 10:21:34.250 CopyDemo[73625:303] person.age 的地址:0xc27
2013-11-19 10:21:34.250 CopyDemo[73625:303] person2.age 的地址:0xc27
```

如果我们把`-(id)copyWithZone:(NSZone *)zone;`里面的代码改成

这个样子的

```objectivec
Person *person = [[[self class] allocWithZone:zone] init];
person.name = _name;
person.age = _age;
return person;
```

或者是这个样子的试试

```objectivec
Person *person = [[[self class] allocWithZone:zone] init];
person.name = [_name copy];
person.age = [_age copy];
return person;
```

得到的结果如下：

```bash
2013-11-19 10:24:25.746 CopyDemo[73692:303] person 的地址:0x100202e60
2013-11-19 10:24:25.748 CopyDemo[73692:303] person2 的地址:0x100200380
2013-11-19 10:24:25.748 CopyDemo[73692:303] person.name 的地址:0x100002350
2013-11-19 10:24:25.749 CopyDemo[73692:303] person2.name 的地址:0x100002350
2013-11-19 10:24:25.749 CopyDemo[73692:303] person.age 的地址:0xc27
2013-11-19 10:24:25.749 CopyDemo[73692:303] person2.age 的地址:0xc27
```

