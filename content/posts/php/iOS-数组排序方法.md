---
title: "iOS 数组排序方法"
date: "2025-06-13 15:33:04"
slug: "ios-shu-zu-pai-xu-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-数组排序方法/"
  - "/2025/06/13/iOS-数组排序方法.html"
  - "/iOS-数组排序方法/"
  - "/iOS-数组排序方法.html"
  - "/2025/06/13/ios-shu-zu-pai-xu-fang-fa/"
  - "/2025/06/13/ios-shu-zu-pai-xu-fang-fa.html"
  - "/ios-shu-zu-pai-xu-fang-fa.html"
---
第一种，利用数组的sortedArrayUsingComparator调用 NSComparator ，obj1和obj2指的数组中的对象

```objectivec
NSComparator cmptr = ^(id obj1, id obj2){
 if ([obj1 integerValue] > [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedDescending;
    }
 
    if ([obj1 integerValue] < [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedAscending;
    }
    return (NSComparisonResult)NSOrderedSame;
};

NSArray *sortArray = [[NSArray alloc] initWithObjects:@"1",@"3",@"4",@"7",@"8",@"2",@"6",@"5",@"13",@"15",@"12",@"20",@"28",@"",nil];
//排序前
NSMutableString *outputBefore = [[NSMutableString alloc] init];
for(NSString *str in sortArray){
	[outputBefore appendFormat:@""];
}
NSLog(@"排序前:%@",outputBefore);
//排序后
NSArray *array = [sortArray sortedArrayUsingComparator:cmptr];
NSMutableString *outputAfter = [[NSMutableString alloc] init];
for(NSString *str in array){
	[outputAfter appendFormat:@"];
}
NSLog(@"排序后:%@",outputAfter);
```

第二种 排序方法 利用sortedArrayUsingFunction 调用 对应方法customSort，这个方法中的obj1和obj2分别是指数组中的对象。

```objectivec
NSInteger customSort(id obj1, id obj2,void* context){
if ([obj1 integerValue] > [obj2 integerValue]) {
    return (NSComparisonResult)NSOrderedDescending;
}

if ([obj1 integerValue] < [obj2 integerValue]) {
    return (NSComparisonResult)NSOrderedAscending;
}
return (NSComparisonResult)NSOrderedSame;
}

NSArray *sortArray = [[NSArray alloc] initWithObjects:@"1",@"3",@"4",@"7",@"8",@"2",@"6",@"5",@"13",@"15",@"12",@"20",@"28",@"",nil];
//排序前
NSMutableString *outputBefore = [[NSMutableString alloc] init];
	for(NSString *str in sortArray){
	[outputBefore appendFormat:@""];
}
NSLog(@"排序前:%@",outputBefore);

NSArray *array = [sortArray sortedArrayUsingFunction:customSort context:nil];

NSMutableString *outputAfter = [[NSMutableString alloc] init];
for(NSString *str in array){
	[outputAfter appendFormat:@""];
}
NSLog(@"排序后:%@",outputAfter);
```

第三种 利用sortUsingDescriptors调用NSSortDescriptor

```objectivec
NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"price" 
															   ascending:NO];//其中，price为数组中的对象的属性，这个针对数组中存放对象比较更简洁方便
NSArray *sortDescriptors = [[NSArray alloc] initWithObjects:&sortDescriptor count:1];
[_totalInfoArray sortUsingDescriptors:sortDescriptors];
[_airListView refreshTable:_totalInfoArray];
```


字符串的比较模式：

```objectivec
NSComparator cmptr = ^(id obj1, id obj2){
    if([[NSString stringWithFormat:@"%@",obj1] compare:[NSString stringWithFormat:@"%@",obj2] options:NSNumericSearch] > 0)
    {
        return (NSComparisonResult)NSOrderedDescending;
    }
    
    if([[NSString stringWithFormat:@"%@",obj1] compare:[NSString stringWithFormat:@"%@",obj2] options:NSNumericSearch] < 0)
    {
        return (NSComparisonResult)NSOrderedAscending;
    }

    return (NSComparisonResult)NSOrderedSame;
};
```

数字比较模式：

```objectivec
NSInteger customSort(id obj1, id obj2,void* context){
    if ([obj1 integerValue] > [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedDescending;
    }
     
    if ([obj1 integerValue] < [obj2 integerValue]) {
        return (NSComparisonResult)NSOrderedAscending;
    }
    return (NSComparisonResult)NSOrderedSame;
}
```
