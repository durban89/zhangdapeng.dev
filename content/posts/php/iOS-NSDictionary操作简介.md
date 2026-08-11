---
title: "iOS NSDictionary操作简介"
date: "2025-06-06 18:01:44"
slug: "ios-nsdictionary-cao-zuo-jian-jie"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS-NSDictionary操作简介/"
  - "/2025/06/06/iOS-NSDictionary操作简介.html"
  - "/iOS-NSDictionary操作简介/"
  - "/iOS-NSDictionary操作简介.html"
  - "/2025/06/06/ios-nsdictionary-cao-zuo-jian-jie/"
  - "/2025/06/06/ios-nsdictionary-cao-zuo-jian-jie.html"
  - "/ios-nsdictionary-cao-zuo-jian-jie.html"
---
iOS NSDictionary 操作代码如下：

```c
- (void)loopThrough
   {
        NSArray * keys=[NSArray arrayWithObjects:@"key1“，@"key2",@"key3",nill];
        NSArray *objects=[NSArray arrayWithOjbects:@"how",@"are",@"you",nill];
 
        NSDictionary *dic=[NSDictionary dictionaryWithObjects:objects,forKeys:keys];

        //loop 1
        for(id key in dic)
        {
            NSLog(@"key:%@,value:%@"，key,[dic objectForKey:key]);
        }

        //loop 2
        NSEnumerator *enumerator;
        id key;
        enumerator=[dic keyEnumerator];
        while((key=[enumerator nextObject]))
          {
            NSLog(@"key:%@,value:%@",key,objectForKey:key]);
          }
   }

-(void)testNsMutableDictionary
   {
      NSMutableDictionary *dic=[NSMutableDictionary dictionaryWithCapacity:30];
      //dictionaryWithObjectsAndKeys:[NSMuble numberWithInt:1] @"math1",[NSMuble numberWithInt:2] @"math2"];

      [dic setObject:@"one" forKey:@"dog"];
      [dic setObject:@"two" forKey:@"cat"];
      [dic setValue:[NSString stringWithFormat:@"three"] forKey:@"pig"];


      [dic removeObjectForkey:@"cat"];
      [dic removeAllObjects];

      NSMutableArray arraylist=[[NSMutableArray alloc] init];
      [arrarlist addObject:dic];
      [dic release];
   }
 ```
