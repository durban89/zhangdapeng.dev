---
title: "Objective-C 协议和代理设计模式的基本测试练习"
date: "2025-06-24 16:17:52"
slug: "objective-c-xie-yi-he-dai-li-she-ji-mo-shi-de-ji-ben-ce-shi-lian-xi"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/24/Objective-C-协议和代理设计模式的基本测试练习/"
  - "/2025/06/24/Objective-C-协议和代理设计模式的基本测试练习.html"
  - "/Objective-C-协议和代理设计模式的基本测试练习/"
  - "/Objective-C-协议和代理设计模式的基本测试练习.html"
  - "/2025/06/24/objective-c-xie-yi-he-dai-li-she-ji-mo-shi-de-ji-ben-ce-shi-lian-xi/"
  - "/2025/06/24/objective-c-xie-yi-he-dai-li-she-ji-mo-shi-de-ji-ben-ce-shi-lian-xi.html"
  - "/objective-c-xie-yi-he-dai-li-she-ji-mo-shi-de-ji-ben-ce-shi-lian-xi.html"
---
关于Object-C的协议和代理设计模式，gowhich在这里做了简单的小测试

代码文件列表：

main.m

Helloworld.h

Person.h

Person.m

代码如下：

main.m

```objectivec
//
//  main.m
//  ProtocolTest
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Person.h"
int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        // insert code here...
        NSLog(@"Hello, World!");
        
        Person *durban = [[Person alloc] init];
        
        [durban requestGet];
        [durban requestPost];
        [durban requestPut];
        
    }
    return 0;
}
```

Helloworld.h

```objectivec
//
//  HelloWorld.h
//  ProtocolTest
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@protocol HelloWorld <NSObject>

@required
-(void) requestPost;
-(void) requestPut;
@optional
-(void) requestGet;

@end
```

Person.h

```objectivec
//
//  Person.h
//  ProtocolTest
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "HelloWorld.h"

@interface Person : NSObject<HelloWorld>

-(void) getMethod;

@end
```

Person.m

```objectivec
//
//  Person.m
//  ProtocolTest
//
//  Created by david on 13-11-1.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Person.h"

@implementation Person


-(void) getMethod
{
    NSLog(@"获取数据的方法");
}

-(void) requestPost
{
    NSLog(@"必须实现的方法:这是一个Post方法");
}

-(void) requestPut
{
    NSLog(@"必须实现的方法:这是一个Put方法");
}

-(void) requestGet
{
    NSLog(@"选择实现的方法:这是一个Get方法");
}

@end
```

gowhich得到的结果是:

```bash
2013-11-01 11:35:51.465 ProtocolTest[1989:303] Hello, World!
2013-11-01 11:35:51.467 ProtocolTest[1989:303] 选择实现的方法:这是一个Get方法
2013-11-01 11:35:51.467 ProtocolTest[1989:303] 必须实现的方法:这是一个Post方法
2013-11-01 11:35:51.468 ProtocolTest[1989:303] 必须实现的方法:这是一个Put方法
```

