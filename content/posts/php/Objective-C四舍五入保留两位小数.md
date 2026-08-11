---
title: "Objective-C四舍五入保留两位小数"
date: "2025-06-16 14:37:43"
slug: "objective-c-si-she-wu-ru-bao-liu-liang-wei-xiao-shu"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/16/Objective-C四舍五入保留两位小数/"
  - "/2025/06/16/Objective-C四舍五入保留两位小数.html"
  - "/Objective-C四舍五入保留两位小数/"
  - "/Objective-C四舍五入保留两位小数.html"
  - "/2025/06/16/objective-c-si-she-wu-ru-bao-liu-liang-wei-xiao-shu/"
  - "/2025/06/16/objective-c-si-she-wu-ru-bao-liu-liang-wei-xiao-shu.html"
  - "/objective-c-si-she-wu-ru-bao-liu-liang-wei-xiao-shu.html"
---
Objective-C也需要这个，我真是用到了才去看，这叫遇到了才学，不主动，呵呵，废话少说，见代码

```objectivec
NSNumber* tempnumber = [NSNumber numberWithDouble:[[NSString stringWithFormat:@"%.2f",  
                                                  (float)(rand()%100001)*0.001f -20] doubleValue]]; 
cell.listProgressScore = [NSString stringWithFormat:@"%0.2f",[[detailDic valueForKey:@"current_index"] doubleValue]];
```
