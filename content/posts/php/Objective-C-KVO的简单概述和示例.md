---
title: "Objective-C KVO的简单概述和示例"
date: "2025-06-26 11:45:00"
slug: "objective-c-kvo-de-jian-dan-gai-shu-he-shi-li"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/26/Objective-C-KVO的简单概述和示例/"
  - "/2025/06/26/Objective-C-KVO的简单概述和示例.html"
  - "/Objective-C-KVO的简单概述和示例/"
  - "/Objective-C-KVO的简单概述和示例.html"
  - "/2025/06/26/objective-c-kvo-de-jian-dan-gai-shu-he-shi-li/"
  - "/2025/06/26/objective-c-kvo-de-jian-dan-gai-shu-he-shi-li.html"
  - "/objective-c-kvo-de-jian-dan-gai-shu-he-shi-li.html"
---
KVO（Key Value Observing）是Cocoa的一个重要机制，他提供了观察某一属性变化的方法，极大的简化了代码。这种观察－被观察模型适用于这样的情况，比方说根据A（数 据类）的某个属性值变化，B（view类）中的某个属性做出相应变化。对于推崇MVC的cocoa而言，kvo应用的地方非常广泛。（这样的机制听起来类 似Notification，但是notification是需要一个发送notification的对象，一般是 notificationCenter，来通知观察者。而kvo是直接通知到观察对象。）

when use KVO，it usually follows below：

1 注册：

```Objective-C
- (void)addObserver:(NSObject *)anObserver forKeyPath:(NSString *)keyPath options:(NSKeyValueObservingOptions)options context:(void*)context
```

keyPath就是要观察的属性值，options给你观察键值变化的选择，而context方便传输你需要的数据（注意这是一个void型）

2 实现变化方法：

```Objective-C
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object
change:(NSDictionary *)change context:(void*)context
```

change里存储了一些变化的数据，比如变化前的数据，变化后的数据；如果注册时context不为空，这里context就能接收到。

是不是很简单？kvo的逻辑非常清晰，实现步骤简单。

说了这么多，大家都要跃跃欲试了吧。可是，在此之前，我们还需要了解KVC机制。看看这篇文章的使用-[Object-C KVC的简单概述和示例]( https://www.gowhich.com/blog/509 )

---

演示一个实例看看：

创建两个类Child和Nurse

Child.h

```Objective-C
//
//  Child.h
//  KVODemo
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Child : NSObject

@property (nonatomic,assign) NSInteger happyVal;

@end
```

Child.m

```Objective-C
//
//  Child.m
//  KVODemo
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Child.h"

@implementation Child

-(id) init
{
    self = [super init];
    if(self != nil)
    {
        _happyVal = 100;
        [NSTimer scheduledTimerWithTimeInterval:1
                                         target:self
                                       selector:@selector(timerAction:)
                                       userInfo:nil
                                        repeats:YES];
    }
    
    return self;
}

-(void) timerAction:(NSTimer *)timer
{
    self.happyVal--;//必须使用点语法
    //第二种语法
//    _happyVal--;
//    [self setValue:[NSNumber numberWithInteger:_happyVal] forKey:@"happyVal"];
}

@end
```

Nurse.h

```Objective-C
//
//  Nurse.h
//  KVODemo
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@class Child;
@interface Nurse : NSObject

@property (nonatomic, retain) Child *child;
-(id) initWithChild:(Child *)child;

@end
```

Nurse.m

```Objective-C
//
//  Nurse.m
//  KVODemo
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Nurse.h"
#import "Child.h"

@implementation Nurse
@synthesize child = _child;

-(id) initWithChild:(Child *)child
{
    self = [super init];
    if(self != nil)
    {
        _child = child;
        [_child addObserver:self
                 forKeyPath:@"happyVal"
                    options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld
                    context:@"xx"];
    }
    
    return self;
}

-(void) observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    NSLog(@"change = %@",change);
}

@end
```

---

测试实现过程如下：

```Objective-C
//
//  main.m
//  KVODemo
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Child.h"
#import "Nurse.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        Child *child = [[Child alloc] init];
        Nurse *nurse = [[Nurse alloc] initWithChild:child];
        [[NSRunLoop currentRunLoop] run];
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

得到的结果是：

```bash
2013-12-19 10:58:58.364 KVODemo[36662:303] change = {
    kind = 1;
    new = 99;
    old = 100;
}
2013-12-19 10:58:59.359 KVODemo[36662:303] change = {
    kind = 1;
    new = 98;
    old = 99;
}
2013-12-19 10:59:00.359 KVODemo[36662:303] change = {
    kind = 1;
    new = 97;
    old = 98;
}
2013-12-19 10:59:01.358 KVODemo[36662:303] change = {
    kind = 1;
    new = 96;
    old = 97;
}
Program ended with exit code: 9
```

如果得到如上的结果，说明使用是正确的

---

参考文章：

http://blog.csdn.net/weiwangchao_/article/details/7454968

