---
title: "Objective-C KVC的简单概述和示例"
date: "2025-06-26 11:16:08"
slug: "objective-c-kvc-de-jian-dan-gai-shu-he-shi-li"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/26/Objective-C-KVC的简单概述和示例/"
  - "/2025/06/26/Objective-C-KVC的简单概述和示例.html"
  - "/Objective-C-KVC的简单概述和示例/"
  - "/Objective-C-KVC的简单概述和示例.html"
  - "/2025/06/26/objective-c-kvc-de-jian-dan-gai-shu-he-shi-li/"
  - "/2025/06/26/objective-c-kvc-de-jian-dan-gai-shu-he-shi-li.html"
  - "/objective-c-kvc-de-jian-dan-gai-shu-he-shi-li.html"
---
KVC的简单概述和示例

1 、概述

KVC是KeyValue Coding的简称，它是一种可以直接通过字符串的名字(key)来访问类属性的机制。而不是通过调用Setter、Getter方法访问。

当使用KVO、Core Data、CocoaBindings、AppleScript(Mac支持)时，KVC是关键技术。

2、如何使用KVC

关键方法定义在：NSKeyValueCodingprotocol

KVC支持类对象和内建基本数据类型。

***获取值***

valueForKey:，传入NSString属性的名字。

valueForKeyPath:，传入NSString属性的路径，xx.xx形式。

valueForUndefinedKey它的默认实现是抛出异常，可以重写这个函数做错误处理。

***修改值***

setValue:forKey:

setValue:forKeyPath:

setValue:forUndefinedKey:

setNilValueForKey: 当对非类对象属性设置nil时，调用，默认抛出异常。

***一对多关系成员的情况***

mutableArrayValueForKey：有序一对多关系成员  NSArray

mutableSetValueForKey：无序一对多关系成员  NSSet

---

示例操作：

创建Person和AppleDevice类



```objectivec Person.h
//
//  Person.h
//  KVCDemoa
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Person : NSObject{

@private
    NSString *_name;
    NSArray *_apples;
}

@end
```



```objectivec Person.m
//
//  Person.m
//  KVCDemoa
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@implementation Person

@end
```



```objectivec AppleDevice.h
//
//  AppleDevice.h
//  KVCDemoa
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface AppleDevice : NSObject{

@private
    NSString *_name;
    NSArray *_price;
}

@end
```



```objectivec AppleDevice.m
//
//  AppleDevice.m
//  KVCDemoa
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "AppleDevice.h"

@implementation AppleDevice

@end
```

实现操作过程代码：

```objectivec main.m
//
//  
//  KVCDemoa
//
//  Created by Durban on 13-12-19.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "AppleDevice.h"
#import "Person.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        Person *person = [[Person alloc] init];
        [person setValue:@"Durban"
                  forKey:@"_name"];
        
        AppleDevice *mac = [[AppleDevice alloc] init];
        [mac setValue:@"mac"
               forKey:@"_name"];
        [mac setValue:@10000
               forKey:@"_price"];
        
        AppleDevice *iphone = [[AppleDevice alloc] init];
        [iphone setValue:@"iphone"
               forKey:@"_name"];
        [iphone setValue:@10000
               forKey:@"_price"];
        
        AppleDevice *ipad = [[AppleDevice alloc] init];
        [ipad setValue:@"ipad"
               forKey:@"_name"];
        [ipad setValue:@3800
               forKey:@"_price"];
        
        NSArray *apples = @[mac,ipad,iphone];
        
        [person setValue:apples forKey:@"_apples"];
        
        NSNumber *num = [person valueForKeyPath:@"_apples.@sum._price"];
        NSLog(@"num = %@",num);
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

得到的结果是：

```bash
2013-12-19 08:39:49.754 KVCDemoa[27764:303] num = 23800
2013-12-19 08:39:49.783 KVCDemoa[27764:303] Hello, World!
Program ended with exit code: 0
```

