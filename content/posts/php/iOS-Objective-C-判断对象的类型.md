---
title: "iOS Objective-C 判断对象的类型"
date: "2025-06-10 15:29:18"
slug: "ios-objective-c-pan-duan-dui-xiang-de-lei-xing"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-Objective-C-判断对象的类型/"
  - "/2025/06/10/iOS-Objective-C-判断对象的类型.html"
  - "/iOS-Objective-C-判断对象的类型/"
  - "/iOS-Objective-C-判断对象的类型.html"
  - "/2025/06/10/ios-objective-c-pan-duan-dui-xiang-de-lei-xing/"
  - "/2025/06/10/ios-objective-c-pan-duan-dui-xiang-de-lei-xing.html"
  - "/ios-objective-c-pan-duan-dui-xiang-de-lei-xing.html"
---
所有继承 NSObject 的的对象可以调用isKindOfClass 方法

```objectivec
(BOOL)isKindOfClass:(Class)aClass
```

例如:

```objectivec
BOOL test = [obj isKindOfClass:[SomeClass class]];
```

