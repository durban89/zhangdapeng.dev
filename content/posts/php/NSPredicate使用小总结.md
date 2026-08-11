---
title: "NSPredicate使用小总结"
date: "2025-06-20 11:07:44"
slug: "nspredicate-shi-yong-xiao-zong-jie"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/NSPredicate使用小总结/"
  - "/2025/06/20/NSPredicate使用小总结.html"
  - "/NSPredicate使用小总结/"
  - "/NSPredicate使用小总结.html"
  - "/2025/06/20/nspredicate-shi-yong-xiao-zong-jie/"
  - "/2025/06/20/nspredicate-shi-yong-xiao-zong-jie.html"
  - "/nspredicate-shi-yong-xiao-zong-jie.html"
---
一般来说这种情况还是蛮多的，比如你从文件中读入了一个array1，然后想把程序中的一个array2中符合array1中内容的元素过滤出来。  
  
正 常傻瓜一点就是两个for循环，一个一个进行比较，这样效率不高，而且代码也不好看。  
  
其实一个循环或者无需循环就可以搞定了，那就需要用到NSPredicate这个类  
  
1）例子一，循环过滤  
  
我想过滤arrayContents的话只要循环 arrayFilter就好了

```objectivec
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSArray *arrayFilter = [NSArray arrayWithObjects:@"pict", @"blackrain", @"ip", nil];
        
       
 NSArray *arrayContents = [NSArray arrayWithObjects:@"I am a picture.", 
@"I am a guy", @"I am gagaga", @"ipad", @"iphone", nil];
        
        int i = 0;
        int count = (int)[arrayFilter count];
        
        for(i = 0; i < count; i ++)
        {
            
            NSString *arrayItem = (NSString *)[arrayFilter objectAtIndex:i];
            
            NSPredicate *filterPredicate = [NSPredicate predicateWithFormat:@"SELF CONTAINS %@", arrayItem];
            NSLog(@"Filtered array with filter %@, %@", arrayItem, [arrayContents filteredArrayUsingPredicate:filterPredicate]);
        }
        
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:35:06.642 test[90135:303] Filtered array with filter pict, (
    "I am a picture."
)
2013-08-12 23:35:06.644 test[90135:303] Filtered array with filter blackrain, (
)
2013-08-12 23:35:06.645 test[90135:303] Filtered array with filter ip, (
    ipad,
    iphone
)
```

当然以上代码中arrayContent最好用mutable 的，这样就可以直接filter了，NSArray是不可修改的。  
  
2）例子二，无需循环

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSArray *arrayFilter = [NSArray arrayWithObjects:@"abc1", @"abc3", nil];
        
        NSArray *arrayContent = [NSArray arrayWithObjects:@"a1", @"abc1", @"abc4", @"abc2", nil];
        
        NSPredicate *thePredicate = [NSPredicate predicateWithFormat:@"NOT (SELF in %@)", arrayFilter];

        arrayContent = [arrayContent filteredArrayUsingPredicate:thePredicate];
        NSLog(@"arrayContent = %@",arrayContent);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:34:36.653 test[90122:303] arrayContent = (
    a1,
    abc4,
    abc2
)
```

这样arrayContent过滤出来的就是不包含 arrayFilter中的所有item了。  
  
  
3）生成文件路径下文件集合列表

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSFileManager *fileManager = [NSFileManager defaultManager];
        
        NSString *defaultPath = [[NSBundle mainBundle] resourcePath];
        
        NSError *error;
        
        NSArray *directoryContents = [fileManager contentsOfDirectoryAtPath:defaultPath error:&error];
        NSLog(@"directoryContents = %@",directoryContents);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:33:11.844 test[90093:303] directoryContents = (
    test
)
```

4）match的用法

1. 简单比较

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSFileManager *fileManager = [NSFileManager defaultManager];
        
        NSString *defaultPath = [[NSBundle mainBundle] resourcePath];
        
        NSError *error;
        
        NSArray *directoryContents = [fileManager contentsOfDirectoryAtPath:defaultPath error:&error];
        NSLog(@"directoryContents = %@",directoryContents);
        NSString *match = @"imagexyz-999.png";
        NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF == %@", match];
        NSArray *results = [directoryContents filteredArrayUsingPredicate:predicate];
        NSLog(@"results = %@",results);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:41:50.130 test[90258:303] directoryContents = (
    test
)
2013-08-12 23:41:50.132 test[90258:303] results = (
)
```

2. match里like的用法（类似Sql中的用法）

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSFileManager *fileManager = [NSFileManager defaultManager];
        
        NSString *defaultPath = [[NSBundle mainBundle] resourcePath];
        
        NSError *error;
        
        NSArray *directoryContents = [fileManager contentsOfDirectoryAtPath:defaultPath error:&error];
        NSLog(@"directoryContents = %@",directoryContents);
        NSString *match = @"imagexyz*.png";
        NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF like %@", match];
        NSArray *results = [directoryContents filteredArrayUsingPredicate:predicate];
        NSLog(@"results = %@",results);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:45:15.239 test[90312:303] directoryContents = (
    test
)
2013-08-12 23:45:15.245 test[90312:303] results = (
)
```

3. 大小写比较  
  
［c］表示忽略大小写，［d］表示忽略重音，可以在一起使用，如下：

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSFileManager *fileManager = [NSFileManager defaultManager];
        
        NSString *defaultPath = [[NSBundle mainBundle] resourcePath];
        
        NSError *error;
        
        NSArray *directoryContents = [fileManager contentsOfDirectoryAtPath:defaultPath error:&error];
        NSLog(@"directoryContents = %@",directoryContents);
        NSString *match = @"imagexyz*.png";
        NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF like [cd] %@", match];
        NSArray *results = [directoryContents filteredArrayUsingPredicate:predicate];
        NSLog(@"results = %@",results);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:46:29.758 test[90336:303] directoryContents = (
    test
)
2013-08-12 23:46:29.764 test[90336:303] results = (
)
```

4.使用正则

```objectivec
//
//  main.m
//  test
//
//  Created by david on 13-8-12.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSFileManager *fileManager = [NSFileManager defaultManager];
        
        NSString *defaultPath = [[NSBundle mainBundle] resourcePath];
        
        NSError *error;
        
        NSArray *directoryContents = [fileManager contentsOfDirectoryAtPath:defaultPath error:&error];
        NSLog(@"directoryContents = %@",directoryContents);
        NSString *match = @"imagexyz-\\d{3}\\.png";
        NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF matches %@", match];
        NSArray *results = [directoryContents filteredArrayUsingPredicate:predicate];
        NSLog(@"results = %@",results);
    }
    return 0;
}
```

输出结果是：

```bash
2013-08-12 23:47:30.005 test[90358:303] directoryContents = (
    test
)
2013-08-12 23:47:30.015 test[90358:303] results = (
)
```

