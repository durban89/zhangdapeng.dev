---
title: "iOS7 - 如何在Objective C中创建一个空白的透明PNG"
date: "2025-06-26 14:55:13"
slug: "ios7-ru-he-zai-objective-c-zhong-chuang-jian-yi-ge-kong-bai-de-tou-ming-png"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-如何在Objective-C中创建一个空白的透明PNG/"
  - "/2025/06/26/iOS7-如何在Objective-C中创建一个空白的透明PNG.html"
  - "/iOS7-如何在Objective-C中创建一个空白的透明PNG/"
  - "/iOS7-如何在Objective-C中创建一个空白的透明PNG.html"
  - "/2025/06/26/ios7-ru-he-zai-objective-c-zhong-chuang-jian-yi-ge-kong-bai-de-tou-ming-png/"
  - "/2025/06/26/ios7-ru-he-zai-objective-c-zhong-chuang-jian-yi-ge-kong-bai-de-tou-ming-png.html"
  - "/ios7-ru-he-zai-objective-c-zhong-chuang-jian-yi-ge-kong-bai-de-tou-ming-png.html"
---
google后的结果很神奇，这里就是一小段的代码

```objectivec
UIGraphicsBeginImageContextWithOptions(CGSizeMake(36, 36), NO, 0.0); 
UIImage *blank = UIGraphicsGetImageFromCurrentImageContext(); 
UIGraphicsEndImageContext();
```

---

参考文章

http://www.16kan.com/question/detail/109385.html

