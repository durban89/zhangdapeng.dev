---
title: "Objective-C 中 NSFileHandle 和 NSFileManager联合使用"
date: "2025-06-25 10:09:37"
slug: "objective-c-zhong-nsfilehandle-he-nsfilemanager-lian-he-shi-yong"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/25/Objective-C-中-NSFileHandle-和-NSFileManager联合使用/"
  - "/2025/06/25/Objective-C-中-NSFileHandle-和-NSFileManager联合使用.html"
  - "/Objective-C-中-NSFileHandle-和-NSFileManager联合使用/"
  - "/Objective-C-中-NSFileHandle-和-NSFileManager联合使用.html"
  - "/2025/06/25/objective-c-zhong-nsfilehandle-he-nsfilemanager-lian-he-shi-yong/"
  - "/2025/06/25/objective-c-zhong-nsfilehandle-he-nsfilemanager-lian-he-shi-yong.html"
  - "/objective-c-zhong-nsfilehandle-he-nsfilemanager-lian-he-shi-yong.html"
---
NSFileHandle获取出路文件的手柄

NSFileManager处理文件的（创建、删除等）

第一个实例：追加数据

```objectivec
NSString *homePath = NSHomeDirectory();
NSString *filePath = [homePath stringByAppendingPathComponent:@"phone/nsfile_test_data.txt"];
NSLog(@"file path = %@",filePath);
NSFileHandle *fileHandle = [NSFileHandle fileHandleForUpdatingAtPath:filePath];
[fileHandle seekToEndOfFile];
NSString *str = @"要追加的数据";
NSData *data = [str dataUsingEncoding:NSUTF8StringEncoding];
[fileHandle writeData:data];
[fileHandle closeFile];
```

第二个实例：追加数据到指定的位置

```objectivec
NSString *homePath = NSHomeDirectory();
NSString *filePath = [homePath stringByAppendingPathComponent:@"phone/nsfile_test_data.txt"];
NSLog(@"file path = %@",filePath);
NSFileHandle *fileHandle = [NSFileHandle fileHandleForUpdatingAtPath:filePath];

[fileHandle seekToFileOffset:5];
NSString *str = @"要追加的数据";
NSData *data = [str dataUsingEncoding:NSUTF8StringEncoding];
[fileHandle writeData:data];
[fileHandle closeFile];
```

第三个实例：定位读取数据

```objectivec
NSString *homePath = NSHomeDirectory();
NSString *filepath = [homePath stringByAppendingPathComponent:@"phone/nsfile_test_data.txt"];
NSFileHandle *fileHandle = [NSFileHandle fileHandleForReadingAtPath:filepath];
NSUInteger length = [[fileHandle availableData] length];
[fileHandle seekToFileOffset:length / 2];
NSData *data = [fileHandle readDataToEndOfFile];
NSString *str = [[NSString alloc] initWithData:data
                                      encoding:NSUTF8StringEncoding];
NSLog(@"str = %@",str);
```

第四个实例：复制文件

```objectivec
NSString *homepath = NSHomeDirectory();
NSString *sourcepath  = [homepath stringByAppendingPathComponent:@"phone/nsfile_test_data.txt"];
NSString *targetpath = [homepath stringByAppendingPathComponent:@"phone/nsfile_test_data_bak.txt"];

NSFileManager *manager = [NSFileManager defaultManager];
BOOL success = [manager createFileAtPath:targetpath
                                contents:nil
                              attributes:nil];
if(success)
{
    NSLog(@"创建目标文件成功");
}
NSFileHandle *outfile = [NSFileHandle fileHandleForReadingAtPath:sourcepath];
NSFileHandle *infile = [NSFileHandle fileHandleForWritingAtPath:targetpath];

NSData *outdata = [outfile readDataToEndOfFile];

[infile writeData:outdata];

[infile closeFile];
[outfile closeFile];
```

