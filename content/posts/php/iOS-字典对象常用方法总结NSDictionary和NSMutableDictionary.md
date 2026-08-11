---
title: "iOS 字典对象 常用方法总结 NSDictionary 和 NSMutableDictionary"
date: "2025-06-10 15:30:47"
slug: "ios-zi-dian-dui-xiang-chang-yong-fang-fa-zong-jie-nsdictionary-he-nsmutabledictionary"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-字典对象-常用方法总结-NSDictionary-和-NSMutableDictionary/"
  - "/2025/06/10/iOS-字典对象-常用方法总结-NSDictionary-和-NSMutableDictionary.html"
  - "/iOS-字典对象-常用方法总结-NSDictionary-和-NSMutableDictionary/"
  - "/iOS-字典对象-常用方法总结-NSDictionary-和-NSMutableDictionary.html"
  - "/2025/06/10/iOS-字典对象常用方法总结NSDictionary和NSMutableDictionary/"
  - "/2025/06/10/iOS-字典对象常用方法总结NSDictionary和NSMutableDictionary.html"
  - "/2025/06/10/ios-zi-dian-dui-xiang-chang-yong-fang-fa-zong-jie-nsdictionary-he-nsmutabledictionary/"
  - "/2025/06/10/ios-zi-dian-dui-xiang-chang-yong-fang-fa-zong-jie-nsdictionary-he-nsmutabledictiona.html"
  - "/ios-zi-dian-dui-xiang-chang-yong-fang-fa-zong-jie-nsdictionary-he-nsmutabledictionary.html"
---
### [NSDictionary的常用方法有](#1)

- +(id)dictionaryWithObjectsAndKeys:obj1,key1,obj2,key2,......nil
顺序添加对象和键值来创建一个字典，注意结尾是nil

- -(id)initWithObjectsAndKeys::obj1,key1,obj2,key2,......nil
初始化一个新分配的字典，顺序添加对象和值，结尾是nil

- -(unsigned int)count
返回字典中的记录数

- -(NSEnumerator*)keyNSEnumerator
返回字典中的所有键到一个 NSEnumerator 对象

- -(NSArray*)keysSortedByValueUsingSelector:(SEL)selector
将字典中所有键按照selector 指定的方法进行排序，并将结果返回

- -(NSEnumerator*)objectEnumerator
返回字典中所有的值到一个 NSEnumetator 类型对象

- -(id)objectForKey:key
返回指定key 值的对象

### [NSMutableDictionary的常用方法有：](#2)

- +(id)dictionaryWithCapacity:size
创建一个size大小的可变字典

- -(id)initWithCapacity:size
初始化一个size 大小的可变字典

- -(void)removeAllObjects
删除字典中所有元素

- -(void)removeObjectForKey:key
删除字典中key位置的元素

- -(void)setObject:obj forKey:key
添加 (key , obj)到字典中去；若key已经存在，则替换值为 obj
