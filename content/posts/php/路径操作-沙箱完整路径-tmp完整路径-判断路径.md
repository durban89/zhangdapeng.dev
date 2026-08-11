---
title: "路径操作 沙箱完整路径 tmp完整路径 判断路径"
date: "2025-06-16 14:37:58"
slug: "lu-jing-cao-zuo-sha-xiang-wan-zheng-lu-jing-tmp-wan-zheng-lu-jing-pan-duan-lu-jing"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/路径操作-沙箱完整路径-tmp完整路径-判断路径/"
  - "/2025/06/16/路径操作-沙箱完整路径-tmp完整路径-判断路径.html"
  - "/路径操作-沙箱完整路径-tmp完整路径-判断路径/"
  - "/路径操作-沙箱完整路径-tmp完整路径-判断路径.html"
  - "/2025/06/16/lu-jing-cao-zuo-sha-xiang-wan-zheng-lu-jing-tmp-wan-zheng-lu-jing-pan-duan-lu-jing/"
  - "/2025/06/16/lu-jing-cao-zuo-sha-xiang-wan-zheng-lu-jing-tmp-wan-zheng-lu-jing-pan-duan-lu-jing.html"
  - "/lu-jing-cao-zuo-sha-xiang-wan-zheng-lu-jing-tmp-wan-zheng-lu-jing-pan-duan-lu-jing.html"
---
### [获取沙箱目录的完整路径](#1)

```objectivec
//获取沙箱目录的完整路径
//uuid.plist
NSArray *myPaths = NSSearchPathForDirectoriesInDomains(NSDocumentationDirectory, NSUserDomainMask, YES);
NSString *myDocPath = [myPaths objectAtIndex:0];

NSLog(@"myDocPath = %@",myDocPath);

NSString *filename = [myDocPath stringByAppendingPathComponent:@"uuid.plist"];
NSLog(@"filename = %@",filename);
```

### [获取tmp目录](#2)

```objectivec
//获取tmp目录
NSString *tmpPath = NSTemporaryDirectory();
NSString *tmpfilename = [tmpPath stringByAppendingPathComponent:@"uuid.plist"];
NSLog(@"tmpfilename = %@",tmpfilename);
```

### [判断路径是否存在](#3)

```objectivec
//判断路径是否存在
if([[NSFileManager defaultManager] fileExistsAtPath:filename])
{
    NSLog(@"文件存在");
}
else
{
    NSLog(@"文件不存在");
}
```
