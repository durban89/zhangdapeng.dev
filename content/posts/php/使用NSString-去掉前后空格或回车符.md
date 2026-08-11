---
title: "使用NSString 去掉前后空格或回车符"
date: "2025-06-19 10:29:24"
slug: "shi-yong-nsstring-qu-diao-qian-hou-kong-ge-huo-hui-che-fu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/使用NSString-去掉前后空格或回车符/"
  - "/2025/06/19/使用NSString-去掉前后空格或回车符.html"
  - "/使用NSString-去掉前后空格或回车符/"
  - "/使用NSString-去掉前后空格或回车符.html"
  - "/2025/06/19/shi-yong-nsstring-qu-diao-qian-hou-kong-ge-huo-hui-che-fu/"
  - "/2025/06/19/shi-yong-nsstring-qu-diao-qian-hou-kong-ge-huo-hui-che-fu.html"
  - "/shi-yong-nsstring-qu-diao-qian-hou-kong-ge-huo-hui-che-fu.html"
---
想要去掉字符串的前后空格和回车符，很简单，如下：

```objectivec
NSString *string = @" spaces in front and at the end ";
NSString *trimmedString = [string stringByTrimmingCharactersInSet:
[NSCharacterSet whitespaceAndNewlineCharacterSet]]; 
NSLog(trimmedString);
```
