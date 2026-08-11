---
title: "Objective-C 自定义对象的归档 NSKeyedArchiver NSKeyedUnarchiver"
date: "2025-06-25 10:26:35"
slug: "objective-c-zi-ding-yi-dui-xiang-de-gui-dang-nskeyedarchiver-nskeyedunarchiver"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/25/Objective-C-自定义对象的归档-NSKeyedArchiver-NSKeyedUnarchiver/"
  - "/2025/06/25/Objective-C-自定义对象的归档-NSKeyedArchiver-NSKeyedUnarchiver.html"
  - "/Objective-C-自定义对象的归档-NSKeyedArchiver-NSKeyedUnarchiver/"
  - "/Objective-C-自定义对象的归档-NSKeyedArchiver-NSKeyedUnarchiver.html"
  - "/2025/06/25/objective-c-zi-ding-yi-dui-xiang-de-gui-dang-nskeyedarchiver-nskeyedunarchiver/"
  - "/2025/06/25/objective-c-zi-ding-yi-dui-xiang-de-gui-dang-nskeyedarchiver-nskeyedunarchiver.html"
  - "/objective-c-zi-ding-yi-dui-xiang-de-gui-dang-nskeyedarchiver-nskeyedunarchiver.html"
---
object-c中自定义对象的归档，实现起来就是使用NSCoding协议，调用其中的两个方法

```objectivec
-(id) initWithCoder:(NSCoder *)aDecoder

-(void) encodeWithCoder:(NSCoder *)aCoder
```

简单的创建一个user类

User.m

```objectivec
//
//  User.m
//  CustomArchiveDemo
//
//  Created by Durban on 13-11-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "User.h"

@implementation User

#define AGE @"age"
#define NICKNAME @"nickname"
#define FIRSTNAME @"firstname"
#define LASTNAME @"lastname"
#define PASSWORD @"password"
#define EMAIL @"email"

@synthesize nickname = _nickname;
@synthesize firstname = _firstname;
@synthesize lastname = _lastname;
@synthesize email = _email;
@synthesize password = _password;

//解归档
-(id) initWithCoder:(NSCoder *)aDecoder
{
    self = [super init];
    if(self != nil){
        _age = [aDecoder decodeObjectForKey:AGE];
        _nickname = [aDecoder decodeObjectForKey:NICKNAME];
        _firstname = [aDecoder decodeObjectForKey:FIRSTNAME];
        _lastname = [aDecoder decodeObjectForKey:LASTNAME];
        _email = [aDecoder decodeObjectForKey:EMAIL];
        _password = [aDecoder decodeObjectForKey:PASSWORD];
        
        self.age = _age;
        self.nickname = _nickname;
        self.firstname = _firstname;
        self.lastname = _lastname;
        self.email = _email;
        self.password = _password;
    }
    return self;
    
}

//归档处理
-(void) encodeWithCoder:(NSCoder *)aCoder
{
    [aCoder encodeObject:_age forKey:AGE];
    [aCoder encodeObject:_nickname forKey:NICKNAME];
    [aCoder encodeObject:_firstname forKey:FIRSTNAME];
    [aCoder encodeObject:_lastname forKey:LASTNAME];
    [aCoder encodeObject:_email forKey:EMAIL];
    [aCoder encodeObject:_password forKey:PASSWORD];
}
@end
```

User.h

```objectivec
//
//  User.h
//  CustomArchiveDemo
//
//  Created by Durban on 13-11-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>


//归档进行 NSCoding
@interface User : NSObject<NSCoding>

@property (nonatomic, copy) NSString *nickname;
@property (nonatomic, copy) NSString *age;
@property (nonatomic, copy) NSString *email;
@property (nonatomic, copy) NSString *password;
@property (nonatomic, copy) NSString *firstname;
@property (nonatomic, copy) NSString *lastname;

@end
```

gowhich给出了简单的实现过程

```objectivec
//
//  main.m
//  CustomArchiveDemo
//
//  Created by Durban on 13-11-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "User.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        User *user = [[User alloc] init];
        user.age = @"19";
        user.nickname = @"Durban";
        user.lastname = @"zhang";
        user.firstname = @"dapeng";
        user.email = @"xx@xx";
        user.password = @"123456";
        
        //归档处理
        NSString *homeDir = NSHomeDirectory();
        NSString *filePath = [homeDir stringByAppendingPathComponent:@"user.info"];
        
        BOOL success = [NSKeyedArchiver archiveRootObject:user
                                                   toFile:filePath];
        if(success)
        {
            NSLog(@"sucess create archiver");
        }
        
        //解归档处理
        NSString *homeDirectory = NSHomeDirectory();
        NSString *dataFilePath = [homeDirectory stringByAppendingPathComponent:@"user.info"];
        User *userInfo = [NSKeyedUnarchiver unarchiveObjectWithFile:dataFilePath];
        NSLog(@"age = %@, email = %@, nickname = %@, lastname = %@, firstname = %@, password = %@",
              userInfo.age,userInfo.email,userInfo.nickname,userInfo.lastname,userInfo.firstname,userInfo.password);
        
        
    }
    return 0;
}
```

得到的结果跟我们添加的结果是一样的

gowhich得到的结果

```bash
2013-11-22 11:30:38.678 CustomArchiveDemo[37027:303] age = 19, email = xx@xx, nickname = Durban, lastname = zhang, firstname = dapeng, password = 123456
```

