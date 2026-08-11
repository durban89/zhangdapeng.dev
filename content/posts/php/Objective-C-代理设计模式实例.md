---
title: "Objective-C 代理设计模式实例"
date: "2025-06-24 16:17:55"
slug: "objective-c-dai-li-she-ji-mo-shi-shi-li"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/24/Objective-C-代理设计模式实例/"
  - "/2025/06/24/Objective-C-代理设计模式实例.html"
  - "/Objective-C-代理设计模式实例/"
  - "/Objective-C-代理设计模式实例.html"
  - "/2025/06/24/objective-c-dai-li-she-ji-mo-shi-shi-li/"
  - "/2025/06/24/objective-c-dai-li-she-ji-mo-shi-shi-li.html"
  - "/objective-c-dai-li-she-ji-mo-shi-shi-li.html"
---
gowhich演示了一个实例，实现功能很简单

> 一个人叫做durban，想要找房子，然后正好有个中介，可以帮助durban找房子。

先做创建一个人的实例的准备：

Person.h

```objectivec
//
//  Person.h
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "FindAparment.h"

@interface Person : NSObject<FindAparment>

@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) id <FindAparment> delegate;
@property HouseRent rent;

-(void)wantToFindApartment;
-(id) initWithName:(NSString *)name withDelegate:(id <FindAparment>)delegate;

@end
```

Person.m

```objectivec
//
//  Person.m
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@implementation Person

@synthesize name = _name;
@synthesize delegate = _delegate;
@synthesize rent = _rent;

-(id) initWithName:(NSString *)name withDelegate:(id <FindAparment>)delegate
{
    self = [super init];
    
    if(self)
    {
        self.name = name;
        self.delegate = delegate;
    }
    
    return self;
}

-(void) wantToFindApartment
{
    [NSTimer scheduledTimerWithTimeInterval:2 target:self
                                   selector:@selector(startFindAparment:)
                                   userInfo:nil
                                    repeats:YES];
}

-(void)startFindAparment:(NSTimer *) timer
{
    
    if([self.delegate respondsToSelector:@selector(FindAparment:)])
    {
        self.rent = [self.delegate FindAparment:self];
    }
    
    if(self.rent == kHighRent)
    {
        NSLog(@"%@ 说: 太贵了，你们再找找吧",self.name);
    }
    else if(self.rent == kMiddleRent)
    {
        NSLog(@"%@ 说: 还是太贵了，你们再找找吧",self.name);
    }
    else
    {
        NSLog(@"%@ 说: 就这个吧，辛苦啦",self.name);
        [timer invalidate];
    }
}

@end
```

接下来做创建中介实例的准备：

Agent.h

```objectivec
//
//  Agent.h
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "FindAparment.h"

@interface Agent : NSObject<FindAparment>

@end
```

Agent.m

```objectivec
//
//  Agent.m
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Agent.h"

@implementation Agent

-(HouseRent) FindAparment:(Person *)person
{
    int count = arc4random() % 3;
    HouseRent rent;
    if(count == 1)
    {
        rent = kHighRent;
        NSLog(@"中介公司说：我们找到了一个价格较高的公寓");
    }
    else if(count == 2)
    {
        rent = kMiddleRent;
        NSLog(@"中介公司说：我们找到了一个价格较合适的公寓");
    }
    else
    {
        rent = kLowerRent;
        NSLog(@"中介公司说：我们找到了一个价格较低的公寓");
    }
    
    return rent;
    
}

@end
```

给中介一个找房子的方法，这里使用了代理模式

```objectivec
//
//  FindAparment.h
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@class Person;
@protocol FindAparment <NSObject>

typedef enum{
    kHighRent = 0,
    kMiddleRent = 1,
    kLowerRent = 2,
}HouseRent;

-(HouseRent) FindAparment:(Person *)person;

@end
```

OK，一切准备就绪，开始找房子喽。

main.m

```objectivec
//
//  main.m
//  Agent
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Person.h"
#import "Agent.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        Agent *agent = [[Agent alloc] init];
        Person *durban = [[Person alloc] initWithName:@"Durban" withDelegate:agent];
        
        [durban wantToFindApartment];

        [[NSRunLoop currentRunLoop] run];
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

结果如下：

```objectivec
2013-11-01 10:53:25.899 Agent[1157:303] 中介公司说：我们找到了一个价格较合适的公寓
2013-11-01 10:53:25.901 Agent[1157:303] Durban 说: 还是太贵了，你们再找找吧
2013-11-01 10:53:27.899 Agent[1157:303] 中介公司说：我们找到了一个价格较高的公寓
2013-11-01 10:53:27.899 Agent[1157:303] Durban 说: 太贵了，你们再找找吧
2013-11-01 10:53:29.898 Agent[1157:303] 中介公司说：我们找到了一个价格较合适的公寓
2013-11-01 10:53:29.899 Agent[1157:303] Durban 说: 还是太贵了，你们再找找吧
2013-11-01 10:53:31.898 Agent[1157:303] 中介公司说：我们找到了一个价格较低的公寓
2013-11-01 10:53:31.899 Agent[1157:303] Durban 说: 就这个吧，辛苦啦
```

