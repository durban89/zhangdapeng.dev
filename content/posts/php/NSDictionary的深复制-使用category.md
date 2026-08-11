---
title: "NSDictionary的深复制（使用category）"
date: "2025-06-16 14:38:10"
slug: "nsdictionary-de-shen-fu-zhi-shi-yong-category"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/NSDictionary的深复制（使用category）/"
  - "/2025/06/16/NSDictionary的深复制（使用category）.html"
  - "/NSDictionary的深复制（使用category）/"
  - "/NSDictionary的深复制（使用category）.html"
  - "/2025/06/16/NSDictionary的深复制-使用category/"
  - "/2025/06/16/NSDictionary的深复制-使用category.html"
  - "/2025/06/16/nsdictionary-de-shen-fu-zhi-shi-yong-category/"
  - "/2025/06/16/nsdictionary-de-shen-fu-zhi-shi-yong-category.html"
  - "/nsdictionary-de-shen-fu-zhi-shi-yong-category.html"
---
目标：把NSDictionary对象转换成NSMutableDictionary对象，对象内容是字符串数组，需要实现完全复制（深复制）。
如果调用NSDictionary的mutableCopy方法，可以得到一个NSMutableDictionary对象，但这只是浅复制，如果我们修改NSDictionary中数组内的值(当然，数组必须是NSMutableArray），会发现，NSMutableDictionary对象内数组的值也跟着更改了。我们需要增加一个mutableDeepCopy方法来实现深复制，在该方法中，循环复制每一个元素。
要实现这一功能，有两种方法，一是继承，二是使用category。category与继承的区别在于，使用category并不是新建一个类，而是在原类的基础上增加一些方法（使用的时候还是用原类名），这样，我们就不需要修改已经在其他源文件中写好的类名，只需要导入h头文件，再把复制方法修改成我们新增的方法即可。

一、新建Objective-C category文件，我这Category填MutableDeepCopy,Category on填NSDictionary,所以生成的文件是NSDictionary+MutableDeepCopy.h和NSDictionary+MutableDeepCopy.m,生成的文件名很容易理解。

二、两文件源代码：

NSDictionary+MutableDeepCopy.h

```objectivec
#import <Foundation/Foundation.h>  
@interface NSDictionary (MutableDeepCopy)  
-(NSMutableDictionary *)mutableDeepCopy;  
//增加mutableDeepCopy方法  
@end
```

NSDictionary+MutableDeepCopy.m

```objectivec
#import "NSDictionary+MutableDeepCopy.h"  
@implementation NSDictionary (MutableDeepCopy)  
-(NSMutableDictionary *)mutableDeepCopy  
{  
    NSMutableDictionary *dict=[[NSMutableDictionary alloc] initWithCapacity:[self count]];  
    //新建一个NSMutableDictionary对象，大小为原NSDictionary对象的大小  
    NSArray *keys=[self allKeys];  
    for(id key in keys)  
    {//循环读取复制每一个元素  
        id value=[self objectForKey:key];  
        id copyValue;  
        if ([value respondsToSelector:@selector(mutableDeepCopy)]) {  
            //如果key对应的元素可以响应mutableDeepCopy方法(还是NSDictionary)，调用mutableDeepCopy方法复制  
            copyValue=[value mutableDeepCopy];  
        }else if([value respondsToSelector:@selector(mutableCopy)])  
        {  
            copyValue=[value mutableCopy];  
        }  
        if(copyValue==nil)  
            copyValue=[value copy];  
        [dict setObject:copyValue forKey:key];  
   
    }  
    return dict;  
}  
@end
```

这是一篇转自别人的文章，方法当然学习一下，关键的一点是，我们如何去添加方法到已经存在的类中，比如上面的例子，我们如何添加深度复制的方法到NSDictionary中。

通过上面的例子我学习了。大家也学习了

测试代码：

```objectivec
#import <Foundation/Foundation.h>  
#import "NSDictionary+MutableDeepCopy.h"  
//导入头文件  
int main (int argc, const char * argv[])  
{  
   
    @autoreleasepool {  
        NSMutableArray *arr1=[[NSMutableArray alloc] initWithObjects:@"aa",@"bb",@"cc", nil];  
        NSDictionary *dict1=[[NSDictionary alloc] initWithObjectsAndKeys:arr1,@"arr1", nil];  
        NSLog(@"%@",dict1);  
        NSMutableDictionary *dict2=[dict1 mutableCopy];  
        //浅复制  
        NSMutableDictionary *dict3=[dict1 mutableDeepCopy];  
        //深复制  
        [arr1 addObject:@"dd"];  
        NSLog(@"%@",dict2);  
        NSLog(@"%@",dict3);  
   
    }  
    return 0;  
}
```
