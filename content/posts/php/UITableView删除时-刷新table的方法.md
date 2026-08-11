---
title: "UITableView删除时，刷新table的方法"
date: "2025-06-13 15:33:08"
slug: "uitableview-shan-chu-shi-shua-xin-table-de-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/UITableView删除时，刷新table的方法/"
  - "/2025/06/13/UITableView删除时，刷新table的方法.html"
  - "/UITableView删除时，刷新table的方法/"
  - "/UITableView删除时，刷新table的方法.html"
  - "/2025/06/13/UITableView删除时-刷新table的方法/"
  - "/2025/06/13/UITableView删除时-刷新table的方法.html"
  - "/2025/06/13/uitableview-shan-chu-shi-shua-xin-table-de-fang-fa/"
  - "/2025/06/13/uitableview-shan-chu-shi-shua-xin-table-de-fang-fa.html"
  - "/uitableview-shan-chu-shi-shua-xin-table-de-fang-fa.html"
---
不知道什么原因，自己在做删除操作的时候，会有个错误，总是删除了，又以空的形式出现，我火了。

查找了很多资料，自己拼出一个还算能够使用的方法

```objectivec
-(void) refreshData
{
    NSMutableDictionary *tmpMutableDictionary = [NSMutableDictionary dictionaryWithCapacity:20];
    NSArray *allKeys = [self.dataDic allKeys];
    NSMutableArray *allMutableKeys = [allKeys mutableCopy];
    NSComparator cmptr = ^(id obj1, id obj2){
        if ([obj1 integerValue] > [obj2 integerValue]) {
            return (NSComparisonResult)NSOrderedDescending;
        }
        
        if ([obj1 integerValue] < [obj2 integerValue]) {
            return (NSComparisonResult)NSOrderedAscending;
        }
        return (NSComparisonResult)NSOrderedSame;
    };
    NSArray *resultKeys = [allMutableKeys sortedArrayUsingComparator:cmptr];
    
    int k = 0;
    for (id item in resultKeys) {
        NSDictionary *dic = [self.dataDic valueForKey:[NSString stringWithFormat:@"%@",item]];
        [tmpMutableDictionary setValue:dic forKey:[NSString stringWithFormat: @"%d", k]];
        k++;
    }

    self.dataDic = [tmpMutableDictionary mutableCopy];
}
```
