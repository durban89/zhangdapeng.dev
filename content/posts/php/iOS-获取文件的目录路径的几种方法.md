---
title: "iOS 获取文件的目录路径的几种方法"
date: "2025-06-16 14:38:14"
slug: "ios-huo-qu-wen-jian-de-mu-lu-lu-jing-de-ji-zhong-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/iOS-获取文件的目录路径的几种方法/"
  - "/2025/06/16/iOS-获取文件的目录路径的几种方法.html"
  - "/iOS-获取文件的目录路径的几种方法/"
  - "/iOS-获取文件的目录路径的几种方法.html"
  - "/2025/06/16/ios-huo-qu-wen-jian-de-mu-lu-lu-jing-de-ji-zhong-fang-fa/"
  - "/2025/06/16/ios-huo-qu-wen-jian-de-mu-lu-lu-jing-de-ji-zhong-fang-fa.html"
  - "/ios-huo-qu-wen-jian-de-mu-lu-lu-jing-de-ji-zhong-fang-fa.html"
---
iphone沙箱模型的有四个文件夹，分别是什么，永久数据存储一般放在什么位置，得到模拟器的路径的简单方式是什么.  
documents，tmp，app，Library。  
(NSHomeDirectory())手动保存的文件在documents文件里  
Nsuserdefaults保存的文件在tmp文件夹里  
- Documents 目录：您应该将所有的应用程序数据文件写入到这个目录下。这个目录用于存储用户数据或其它应该定期备份的信息。  
- AppName.app 目录：这是应用程序的程序包目录，包含应用程序的本身。由于应用程序必须经过签名，所以您在运行时不能对这个目录中的内容进行修改，否则可能会使应用程序无法启动。  
- Library 目录：这个目录下有两个子目录：Caches 和 Preferences  
Preferences 目录：包含应用程序的偏好设置文件。您不应该直接创建偏好设置文件，而是应该使用NSUserDefaults类来取得和设置应用程序的偏好.  
Caches 目录：用于存放应用程序专用的支持文件，保存应用程序再次启动过程中需要的信息。  
- tmp 目录：这个目录用于存放临时文件，保存应用程序再次启动过程中不需要的信息。  

获取这些目录路径的方法：  

- 获取家目录路径的函数：  
`NSString *homeDir = NSHomeDirectory();` 

- 获取Documents目录路径的方法：  
`NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);`  
`NSString *docDir = [paths objectAtIndex:0];`  

- 获取Caches目录路径的方法：  
`NSArray *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);`  
`NSString *cachesDir = [paths objectAtIndex:0];`  

- 获取tmp目录路径的方法：  
`NSString *tmpDir = NSTemporaryDirectory();`

- 获取应用程序程序包中资源文件路径的方法：  
例如获取程序包中一个图片资源（apple.png）路径的方法：

```objectivec
NSString *imagePath = [[NSBundle mainBundle] pathForResource:@”apple” ofType:@”png”];
UIImage *appleImage = [[UIImage alloc] initWithContentsOfFile:imagePath];
```

代码中的mainBundle类方法用于返回一个代表应用程序包的对象。  
iphone沙盒(sandbox)中的几个目录获取方式：  
  
- 获取沙盒主目录路径   
`NSString *homeDir = NSHomeDirectory();` 

- 获取Documents目录路径   
`NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);`  
`NSString *docDir = [paths objectAtIndex:0];` 

- 获取Caches目录路径   
`NSArray *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);`  
`NSString *cachesDir = [paths objectAtIndex:0];`

- 获取tmp目录路径   
`NSString *tmpDir = NSTemporaryDirectory();` 
  
- 获取当前程序包中一个图片资源（apple.png）路径   
`NSString *imagePath = [[NSBundle mainBundle] pathForResource:@"apple" ofType:@"png"];`
`UIImage *appleImage = [[UIImage alloc] initWithContentsOfFile:imagePath];` 
  
例子：

```objectivec
NSFileManager* fm=[NSFileManager defaultManager];
if(![fm fileExistsAtPath:[self dataFilePath]]){
    //下面是对该文件进行制定路径的保存
    [fm createDirectoryAtPath:[self dataFilePath] withIntermediateDirectories:YES attributes:nil error:nil];

    //取得一个目录下得所有文件名
    NSArray *files = [fm subpathsAtPath: [self dataFilePath] ];

    //读取某个文件
    NSData *data = [fm contentsAtPath:[self dataFilePath]];

    //或者
    NSData *data = [NSData dataWithContentOfPath:[self dataFilePath]];
}
```
