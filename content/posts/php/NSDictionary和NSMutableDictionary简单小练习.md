---
title: "NSDictionary和NSMutableDictionary简单小练习"
date: "2025-06-24 15:29:49"
slug: "nsdictionary-he-nsmutabledictionary-jian-dan-xiao-lian-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/24/NSDictionary和NSMutableDictionary简单小练习/"
  - "/2025/06/24/NSDictionary和NSMutableDictionary简单小练习.html"
  - "/NSDictionary和NSMutableDictionary简单小练习/"
  - "/NSDictionary和NSMutableDictionary简单小练习.html"
  - "/2025/06/24/nsdictionary-he-nsmutabledictionary-jian-dan-xiao-lian-xi/"
  - "/2025/06/24/nsdictionary-he-nsmutabledictionary-jian-dan-xiao-lian-xi.html"
  - "/nsdictionary-he-nsmutabledictionary-jian-dan-xiao-lian-xi.html"
---
NSDictionary和NSMutableDictionary简单小练习

```objectivec
int main(int argc, const char * argv[])
{
    @autoreleasepool {
        
        //nsdictionary
        NSDictionary *dict1 = [NSDictionary dictionaryWithObject:@"OneValue" forKey:@"One"];
        NSDictionary *dict2 = [NSDictionary dictionaryWithObjectsAndKeys:@"OneValue",@"One",
                               @"TwoValue",@"Two",
                               @"ThreeValue",@"Three",
                               @"FourValue",@"Four",
                               @"FiveValue",@"Five", nil];
        NSLog(@"dict1 = %@", dict1);
        NSLog(@"dict2 = %@", dict2);
        
        NSDictionary *dict3 = [NSDictionary dictionaryWithDictionary:dict2];
        NSLog(@"dict3 = %@",dict3);
        
        //获取字典的数量
        NSInteger count = [dict2 count];
        NSLog(@"dict2 count = %ld",(long)count);
        
        //获取字典的value
        NSString *string = [dict3 objectForKey:@"One"];
        NSLog(@"One String = %@",string);
        
        //获取字典的所有的keys和values
        NSArray *allKeys = [dict3 allKeys];
        NSArray *allValues = [dict3 allValues];
        NSLog(@"dict3 allkeys = %@",allKeys);
        NSLog(@"dict3 allvalues = %@",allValues);
        
        //nsmutablensctionary
        NSMutableDictionary *mutableDict = [[NSMutableDictionary alloc] initWithObjectsAndKeys:@"v1",@"k1",
                                            @"v2",@"k2",
                                            @"v3",@"k3",
                                            @"v4",@"k4",
                                            @"v5",@"k5",
                                            @"v6",@"k6",nil];
        NSLog(@"mutableDict = %@",mutableDict);
        
        //添加
        NSDictionary *dict4 = [NSDictionary dictionaryWithObjectsAndKeys:@"v7",@"k7", nil];
        [mutableDict addEntriesFromDictionary:dict4];
        NSLog(@"mutabledict = %@",mutableDict);
        
        //添加
        [mutableDict setObject:@"v8" forKey:@"k8"];
        NSLog(@"mutableDict = %@",mutableDict);
        
        //创建
        NSMutableDictionary *mutableDict2 = [NSMutableDictionary dictionary];
        [mutableDict2 setDictionary:mutableDict];
        NSLog(@"mutabledict2 = %@",mutableDict2);
        
        //删除
        [mutableDict2 removeObjectForKey:@"k3"];
        NSLog(@"mutabledict2 = %@",mutableDict2);
        
        //遍历字典 一般的方法
        for (int index = 0; index < [mutableDict count]; index++) {
            NSString *string = [mutableDict objectForKey:[[mutableDict allKeys] objectAtIndex:index]];
            NSLog(@"String = %@",string);
        }
        
        NSLog(@"_______________________________________________快速枚举");
        
        //快速枚举
        for(id key in mutableDict){
            NSString *string = [mutableDict objectForKey:key];
            NSLog(@"string = %@",string);
        }
        
        NSLog(@"_______________________________________________枚举类型");
        //使用枚举类型
        NSEnumerator *enumerator = [mutableDict keyEnumerator];
        id key;
        while (key) {
            id obejct = [mutableDict objectForKey:key];
            id key = [enumerator nextObject];
            NSLog(@"string = %@",string);
        }
        
        
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

