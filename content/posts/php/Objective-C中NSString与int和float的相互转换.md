---
title: "Objective-C中NSString与int和float的相互转换.md"
date: "2025-06-12 17:44:47"
slug: "objective-c-zhong-nsstring-yu-int-he-float-de-xiang-hu-zhuan-huan-md"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/12/Objective-C中NSString与int和float的相互转换.md/"
  - "/2025/06/12/Objective-C中NSString与int和float的相互转换.md.html"
  - "/Objective-C中NSString与int和float的相互转换.md/"
  - "/Objective-C中NSString与int和float的相互转换.md.html"
  - "/2025/06/12/Objective-C中NSString与int和float的相互转换/"
  - "/2025/06/12/Objective-C中NSString与int和float的相互转换.html"
  - "/2025/06/12/objective-c-zhong-nsstring-yu-int-he-float-de-xiang-hu-zhuan-huan-md/"
  - "/2025/06/12/objective-c-zhong-nsstring-yu-int-he-float-de-xiang-hu-zhuan-huan-md.html"
  - "/objective-c-zhong-nsstring-yu-int-he-float-de-xiang-hu-zhuan-huan-md.html"
---
```objectivec
NSString *tempA = @"123";
NSString *tempB = @"456";
```

### [字符串拼接](#1)

```objectivec
NSString *newString = [NSString stringWithFormat:@"%@%@",tempA,tempB];
```

### [字符转int](#2)

```objectivec
int intString = [newString intValue];
```

### [int转字符](#3)

```objectivec
NSString *stringInt = [NSString stringWithFormat:@"%d",intString];
```

### [字符转float](#4)

```objectivec
float floatString = [newString floatValue];
```

### [float转字符](#5)

```objectivec
NSString *stringFloat = [NSString stringWithFormat:@"%f",intString];
```
