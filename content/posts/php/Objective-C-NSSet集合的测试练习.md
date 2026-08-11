---
title: "Objective-C NSSet集合的测试练习"
date: "2025-06-24 16:16:59"
slug: "objective-c-nsset-ji-he-de-ce-shi-lian-xi"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/24/Objective-C-NSSet集合的测试练习/"
  - "/2025/06/24/Objective-C-NSSet集合的测试练习.html"
  - "/Objective-C-NSSet集合的测试练习/"
  - "/Objective-C-NSSet集合的测试练习.html"
  - "/2025/06/24/objective-c-nsset-ji-he-de-ce-shi-lian-xi/"
  - "/2025/06/24/objective-c-nsset-ji-he-de-ce-shi-lian-xi.html"
  - "/objective-c-nsset-ji-he-de-ce-shi-lian-xi.html"
---
### [NSSet集合的测试练习](#1)

```objectivec
//NSSet 测试
//集合的创建
NSSet *set1 = [NSSet setWithObjects:@"1",@"2", nil];
NSSet *set2 = [NSSet setWithObjects:@"3",@"4",@"5",@"6", nil];
NSArray *array = [NSArray arrayWithObjects:@"6",@"7",@"8", nil];
NSSet *set3 = [NSSet setWithArray:array];
NSSet *set4 = [NSSet setWithSet:set1];
NSSet *set5 = [NSSet setWithObjects:@"1",@"2", nil];
NSSet *set6 = [NSSet setWithObjects:@"1",@"2",@"6",@"7", nil];


NSLog(@"set1 = %@",set1);
NSLog(@"set2 = %@",set2);
NSLog(@"set3 = %@",set3);
NSLog(@"set4 = %@",set4);

//返回数量
NSInteger count = [set3 count];
NSLog(@"set3 count = %ld",(long)count);

//返回任意对象
NSString *string = [set3 anyObject];
NSLog(@"string = %@",string);

//返回所有对象
NSArray *objects = [set3 allObjects];
NSLog(@"objects = %@",objects);

//是否包含
BOOL isContain = [set3 containsObject:@"6"];
BOOL isContain1 = [set3 containsObject:@"10"];
NSLog(@"isContain = %d, isContain1 = %d",isContain, isContain1);

//集合间是否存在交集
BOOL isIntersect = [set2 intersectsSet:set3];
BOOL isInterset1 = [set1 intersectsSet:set2];
NSLog(@"isItersect = %ld,isItersect1 = %ld",(long)isIntersect,(long)isInterset1);

//集合是否匹配
BOOL isEqual = [set1 isEqualToSet:set2];
BOOL isEqual1 = [set1 isEqualToSet:set5];
NSLog(@"isEqual = %ld,isEqual1 = %ld",(long)isEqual,(long)isEqual1);

//结合是否是字子集
BOOL isSub = [set2 isSubsetOfSet:set3];
bool isSub1 = [set1 isSubsetOfSet:set6];
NSLog(@"isSub = %ld, isSub1 = %ld",(long)isSub, (long)isSub1);

//集合的添加
NSSet *set7 = [set5 setByAddingObject:@"One"];
NSLog(@"set7 = %@",set7);
NSArray *array1 = [NSArray arrayWithObjects:@"two",@"three",@"four", nil];
NSSet *set8 = [set7 setByAddingObjectsFromArray:array1];
NSLog(@"set8 = %@",set8);
NSSet *set9 = [set8 setByAddingObjectsFromSet:set5];
NSLog(@"set9 = %@",set9);

//可变结合的应用

NSMutableSet *mutableSet1 = [NSMutableSet set];
NSMutableSet *mutableSet2 = [NSMutableSet setWithObjects:@"1",@"a", nil];
NSMutableSet *mutableSet3 = [NSMutableSet setWithObjects:@"2",@"a", nil];
NSMutableSet *mutableSet4 = [NSMutableSet setWithObjects:@"2",@"a",@"b", nil];
NSMutableSet *mutableSet5 = [NSMutableSet setWithObjects:@"2",@"a",@"b",@"c",@"d", nil];
NSLog(@"mutableSet1 = %@",mutableSet1);
NSLog(@"mutableSet2 = %@",mutableSet2);
NSLog(@"mutableSet3 = %@",mutableSet3);
//一个集合减去另一个集合的元素，
//        [mutableSet2 minusSet:mutableSet3];
//        NSLog(@"mutableSet2 = %@",mutableSet2);

//两个集合获取交集部分
//        [mutableSet2 intersectSet:mutableSet3];
//        NSLog(@"mutableSet2 = %@",mutableSet2);

//获取两个集合的并集
//        [mutableSet2 unionSet:mutableSet3];
//        NSLog(@"mutableSet2 = %@",mutableSet2);

//一个集合给另一个集合赋值
[mutableSet1 setSet:mutableSet3];
NSLog(@"mutableSet1 = %@",mutableSet1);

//删除集合中的对象
NSLog(@"mutableSet4 = %@",mutableSet4);
[mutableSet4 removeObject:@"b"];
NSLog(@"mutableSet4 = %@",mutableSet4);
[mutableSet4 removeAllObjects];
NSLog(@"mutableSet4 = %@",mutableSet4);

//使用数组的方式进行添加对象
NSLog(@"mutableSet5 = %@",mutableSet5);
NSArray *array2 = [NSArray arrayWithObjects:@"e",@"f", nil];
[mutableSet5 addObjectsFromArray:array2];
NSLog(@"mutableSet5 = %@",mutableSet5);
```

