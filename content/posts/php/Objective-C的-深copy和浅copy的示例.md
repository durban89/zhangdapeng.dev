---
title: "Objective-C的 深copy和浅copy的示例"
date: "2025-06-25 10:26:25"
slug: "objective-c-de-shen-copy-he-qian-copy-de-shi-li"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/25/Objective-C的-深copy和浅copy的示例/"
  - "/2025/06/25/Objective-C的-深copy和浅copy的示例.html"
  - "/Objective-C的-深copy和浅copy的示例/"
  - "/Objective-C的-深copy和浅copy的示例.html"
  - "/2025/06/25/objective-c-de-shen-copy-he-qian-copy-de-shi-li/"
  - "/2025/06/25/objective-c-de-shen-copy-he-qian-copy-de-shi-li.html"
  - "/objective-c-de-shen-copy-he-qian-copy-de-shi-li.html"
---
深copy和浅copy的示例

下面进行看代码

第一个示例：浅copy

先声明两个类

Car和Engine类


```objectivec Car.h
//
//  Car.h
//  CarDemo
//
//  Created by Durban on 13-11-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Engine.h"

@interface Car : NSObject<NSCopying>

//
@property (nonatomic, retain) Engine *engine;
@property (nonatomic,retain) NSNumber *weight;
@property (nonatomic, copy) NSString *name;

@end
```

```objectivec Car.m
//
//  Car.m
//  CarDemo
//
//  Created by Durban on 13-11-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Car.h"

@implementation Car

@synthesize engine = _engine;
@synthesize name = _name;
@synthesize weight = _weight;

-(id) copyWithZone:(NSZone *)zone
{
    //浅copy
    Car *car = [[[self class] allocWithZone:zone] init];
    car.name = _name;
    car.engine = _engine;
    car.weight = _weight;
    return car;
}

-(void) dealloc
{
    
    NSLog(@"car dealloc");
    [_name release];
    [_weight release];
    [_engine release];
    
    [super dealloc];
}

@end
```


```objectivec Engine.h
//
//  Engine.h
//  CarDemo
//
//  Created by Durban on 13-11-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Engine : NSObject<NSCopying>

@end
```


```objectivec Engine.m
//
//  Engine.m
//  CarDemo
//
//  Created by Durban on 13-11-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Engine.h"

@implementation Engine

-(id)copyWithZone:(NSZone *)zone
{
    Engine *engine = [[[self class] allocWithZone:zone] init];
    return engine;
}

@end
```

运行得到的结果是：

```objectivec main.m
//
//  
//  CarDemo
//
//  Created by Durban on 13-11-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Engine.h"
#import "Car.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        Car *car = [[Car alloc] init];
        Engine *engine = [[Engine alloc] init];
        car.name = @"奥迪";
        car.weight = @1389;
        car.engine = engine;
        
        Car *car2 = [car copy];
        
        NSLog(@"car = %p",car);
        NSLog(@"car2 = %p",car2);
        
        
        [car release];
        [car2 release];
        [engine release];
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

第二个示例：深copy

有两种方法：

第一种方法：

修改属性，将

```objectivec
@property (nonatomic, retain) Engine *engine;
@property (nonatomic,retain) NSNumber *weight;
@property (nonatomic, copy) NSString *name;
```

修改为：

```objectivec
@property (nonatomic, copy) Engine *engine;
@property (nonatomic,copy) NSNumber *weight;
@property (nonatomic, copy) NSString *name;
```

第二种方法：

修改copy的操作，将：

```objectivec
-(id) copyWithZone:(NSZone *)zone
{
    //浅copy
    Car *car = [[[self class] allocWithZone:zone] init];
    car.name = _name;
    car.engine = _engine;
    car.weight = _weight;
    return car;
}
```

改为：

```objectivec
-(id) copyWithZone:(NSZone *)zone
{
    //深copy - 1
    Car *car = [[[self class] allocWithZone:zone] init];
    Engine *engine = [_engine copy];
    NSString *name = [_name copy];
    NSNumber *weight = [_weight copy];
    
    car.name = name;
    car.engine = engine;
    car.weight = weight;
    
    [engine release];
    [name release];
    [weight release];
    return car;
}
```

结果都是一样的，嘿嘿

```bash
2013-11-20 11:21:34.432 CarDemo[93002:303] car = 0x100200b40
2013-11-20 11:21:34.434 CarDemo[93002:303] car2 = 0x1002045c0
2013-11-20 11:21:34.434 CarDemo[93002:303] car dealloc
2013-11-20 11:21:34.435 CarDemo[93002:303] car dealloc
```

