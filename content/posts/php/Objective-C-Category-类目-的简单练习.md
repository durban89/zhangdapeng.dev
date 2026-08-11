---
title: "Objective-C Category(类目)的简单练习"
date: "2025-06-24 16:17:27"
slug: "objective-c-category-lei-mu-di-jian-dan-lian-xi"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/24/Objective-C-Category(类目)的简单练习/"
  - "/2025/06/24/Objective-C-Category(类目)的简单练习.html"
  - "/Objective-C-Category(类目)的简单练习/"
  - "/Objective-C-Category(类目)的简单练习.html"
  - "/2025/06/24/Objective-C-Category-类目-的简单练习/"
  - "/2025/06/24/Objective-C-Category-类目-的简单练习.html"
  - "/2025/06/24/objective-c-category-lei-mu-di-jian-dan-lian-xi/"
  - "/2025/06/24/objective-c-category-lei-mu-di-jian-dan-lian-xi.html"
  - "/objective-c-category-lei-mu-di-jian-dan-lian-xi.html"
---
### [Objective-C category类目的操作练习](#1)

main.m

```objectivec
#import <Foundation/Foundation.h>
#import "Person.h"
#import "Person+Revert.h"
#import "NSArray+Convert.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        Person *durban = [Person PersonWithName:@"Durban" withAge:25];
        NSLog(@"Durban's name = %@, Durban's age = %d",durban.name, durban.age);
        [durban eat];
        [durban sleep];
        [durban play];
        [durban test];
        
        NSMutableArray *array = [NSArray arrayWithNumber:12345678];
        
        for (id string in array) {
            NSLog(@"string = %@",string);
        }
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

文件的简单列表如下：

1. Person.h
2. Person.m
3. Person+Revert.h
4. Person+Revert.m
5. NSArray+Convert.h
6. NSArray+Convert.m

Person.h

```objectivec
//
//  Person.h
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

#pragma mark - NSObject
@interface Person : NSObject{

@private
    NSString *_name;
    int      _age;
}

@property (nonatomic,copy) NSString *name;
@property (nonatomic) int age;

-(void) test;

-(void) typing;

@end

#pragma mark - Creation

@interface Person (Creation)

+(id) PersonWithName:(NSString *)aName;

+(id) PersonWithName:(NSString *)aName withAge:(int)age;

-(id) initWithName:(NSString *)aName;

-(id) initWithName:(NSString *)aName withAge:(int)age;

@end

#pragma mark - Life

@interface Person (Life)

-(void) eat;

-(void) sleep;

-(void) play;

@end
```

Person.m

```objectivec
//
//  Person.m
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@implementation Person

@synthesize name = _name;
@synthesize age = _age;

-(void) test
{
    NSLog(@"这是一个Person类的Test方法");
}

-(void) typing
{
    NSLog(@"这是一个Person类的Typing方法");
}

@end


#pragma mark - Creation

@implementation Person (Creation)

-(id) initWithName:(NSString *)aName
{
    self = [super init];
    if(self)
    {
        self.name = aName;
    }
    return self;
}

-(id) initWithName:(NSString *)aName withAge:(int)age
{
    self = [super init];
    if(self)
    {
        self.name = aName;
        self.age = age;
    }
    return self;
}

+(id) PersonWithName:(NSString *)aName
{
    Person *person = [[Person alloc] init];
    person.name = aName;
    
    return person;
}

+(id) PersonWithName:(NSString *)aName withAge:(int)age
{
    Person *person = [[Person alloc] init];
    person.name = aName;
    person.age = age;
    return person;
}

@end


@implementation Person (Life)

-(void) eat
{
    NSLog(@"Person Lefe --- 我在吃饭嗯");
}

-(void) sleep
{
    NSLog(@"Person Lefe --- 我在睡觉嗯");
}

-(void) play
{
    NSLog(@"Person Lefe --- 我在打游戏嗯");
}

@end
```

Person+Revert.h

```objectivec
//
//  Person+Revert.h
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@interface Person (Revert)

-(void) eat;

@end
```

Person+Revert.m

```objectivec
//
//  Person+Revert.m
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person+Revert.h"

@implementation Person (Revert)

-(void) eat
{
    NSLog(@"Person (Revert) eat -- 我的在Revert吃饭嗯");
}
@end
```

NSArray+Convert.h

```objectivec
//
//  NSArray+Convert.h
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface NSArray (Convert)

+(NSMutableArray *) arrayWithNumber:(int)number;

@end
```

NSArray+Convert.m

```objectivec
//
//  NSArray+Convert.m
//  CategoryTest
//
//  Created by david on 13-10-30.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "NSArray+Convert.h"

@implementation NSArray (Convert)

+(NSMutableArray *) arrayWithNumber:(int)number
{
    NSMutableArray *numberArray = [[NSMutableArray alloc] init];
    while (number) {
        int last = number % 10;         //取出最后一位
        number /= 10;                   //去掉最后一位
        [numberArray addObject:[NSNumber numberWithInt:last]];
    }
    return numberArray;
}
@end
```

