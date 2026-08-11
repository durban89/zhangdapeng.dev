---
title: "NSCoding解释  initWithCoder:  encodeWithCoder:"
date: "2025-06-19 10:48:44"
slug: "nscoding-jie-shi-initwithcoder-encodewithcoder"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/NSCoding解释-initWithCoder:-encodeWithCoder:/"
  - "/2025/06/19/NSCoding解释-initWithCoder:-encodeWithCoder:.html"
  - "/NSCoding解释-initWithCoder:-encodeWithCoder:/"
  - "/NSCoding解释-initWithCoder:-encodeWithCoder:.html"
  - "/2025/06/19/NSCoding解释-initWithCoder-encodeWithCoder/"
  - "/2025/06/19/NSCoding解释-initWithCoder-encodeWithCoder.html"
  - "/2025/06/19/nscoding-jie-shi-initwithcoder-encodewithcoder/"
  - "/2025/06/19/nscoding-jie-shi-initwithcoder-encodewithcoder.html"
  - "/nscoding-jie-shi-initwithcoder-encodewithcoder.html"
---
1、为了将应用数据存储到硬盘中，iOS提供基本的文件API、Property List序列化、SQLite、CoreData以及NSCoding。对于轻量级的数据要求，NSCoding因其简单而成为一种比较合适的方式。 NSCoding是一个你需要在数据类上要实现的协议以支持数据类和数据流间的编码和解码。数据流可以持久化到硬盘。

2、是类对象本身数据的写入到本地文件。

我们需要实现两个方法: encodeWithCoder和initWithEncoder。encodeWithCoder就是编码，initWithCoder就是解码。 encodeWithCoder方法传入的是一个NSCoder对象，实现的时候我们就可以调用encodeObject、encodeFloat、 encodeInt等各种方法并通过指定键值进行编码。

APLProduct.m的代码如下

```objectivec
#import "APLProduct.h"

NSString *ProductTypeDevice = @"Device";
NSString *ProductTypeDesktop = @"Desktop";
NSString *ProductTypePortable = @"Portable";


@implementation APLProduct

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name year:(NSNumber *)year price:(NSNumber *)price
{
    APLProduct *newProduct = [[self alloc] init];
    newProduct.type = type;
    newProduct.name = name;
    newProduct.yearIntroduced = year;
    newProduct.introPrice = price;
    
    return newProduct;
}

+ (NSArray *)deviceTypeNames
{
    static NSArray *deviceTypeNames = nil;
    static dispatch_once_t once;

    dispatch_once(&once, ^{
        deviceTypeNames = @[ProductTypeDevice, ProductTypePortable, ProductTypeDesktop];
    });

    return deviceTypeNames;
}

+ (NSString *)displayNameForType:(NSString *)type
{
    static NSMutableDictionary *deviceTypeDisplayNamesDictionary = nil;
    static dispatch_once_t once;

    dispatch_once(&once, ^{
        deviceTypeDisplayNamesDictionary = [[NSMutableDictionary alloc] init];
        for (NSString *deviceType in [self deviceTypeNames])
        {
            NSString *displayName = NSLocalizedString(deviceType, @"dynamic");
            deviceTypeDisplayNamesDictionary[deviceType] = displayName;
        }
    });

    return deviceTypeDisplayNamesDictionary[type];
}


#pragma mark - Archiving

static NSString *NameKey = @"NameKey";
static NSString *TypeKey = @"TypeKey";
static NSString *YearKey = @"YearKey";
static NSString *PriceKey = @"PriceKey";

- (id)initWithCoder:(NSCoder *)aDecoder
{
    self = [super init];
    if (self) {
        _name = [aDecoder decodeObjectForKey:NameKey];
        _type = [aDecoder decodeObjectForKey:TypeKey];
        _yearIntroduced = [aDecoder decodeObjectForKey:YearKey];
        _introPrice = [aDecoder decodeObjectForKey:PriceKey];
    }
    return self;
}

- (void)encodeWithCoder:(NSCoder *)aCoder
{
    [aCoder encodeObject:self.name forKey:NameKey];
    [aCoder encodeObject:self.type forKey:TypeKey];
    [aCoder encodeObject:self.yearIntroduced forKey:YearKey];
    [aCoder encodeObject:self.introPrice forKey:PriceKey];
}

@end
```

APLProduct.h的代码如下

```objectivec
extern NSString *ProductTypeDevice;
extern NSString *ProductTypeDesktop;
extern NSString *ProductTypePortable;


@interface APLProduct : NSObject <NSCoding>

@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *type;
@property (nonatomic, copy) NSNumber *yearIntroduced;
@property (nonatomic) NSNumber *introPrice;

+ (instancetype)productWithType:(NSString *)type name:(NSString *)name year:(NSNumber *)year price:(NSNumber *)price;

+ (NSArray *)deviceTypeNames;
+ (NSString *)displayNameForType:(NSString *)type;

@end
```
