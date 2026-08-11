---
title: "iOS文件系统的管理"
date: "2025-06-17 16:46:14"
slug: "ios-wen-jian-xi-tong-de-guan-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS文件系统的管理/"
  - "/2025/06/17/iOS文件系统的管理.html"
  - "/iOS文件系统的管理/"
  - "/iOS文件系统的管理.html"
  - "/2025/06/17/ios-wen-jian-xi-tong-de-guan-li/"
  - "/2025/06/17/ios-wen-jian-xi-tong-de-guan-li.html"
  - "/ios-wen-jian-xi-tong-de-guan-li.html"
---
用于执行一般的文件系统操作 (reading and writing is done via NSData, et. al.).

主要功能包括：

**从一个文件中读取数据；**

**向一个文件中写入数据；**

**删除文件；**

**复制文件；**

**移动文件；**

**比较两个文件的内容；**

**测试文件的存在性；**

**读取/更改文件的属性... ...**

Just alloc/init an instance and start performing operations. Thread safe.

### [常见的NSFileManager处理文件的方法如下：](#0-1)

**NSFileManager \*fileManager = [[NSFileManager alloc]init]; //最好不要用defaultManager。**  
**NSData \*myData = [fileManager contentsAtPath:path]; // 从一个文件中读取数据**  
**[fileManager createFileAtPath:path contents:myData attributes:dict];//向一个文件中写入数据，属性字典允许你制定要创建**  
**[fileManager removeItemAtPath:path error:err];**  
**[fileManager moveItemAtPath:path toPath:path2 error:err];**  
**[fileManager copyItemAtPath:path toPath:path2 error:err];**  
**[fileManager contentsEqualAtPath:path andPath:path2];**  
**[fileManager fileExistsAtPath:path]; ... ...**

### [常见的NSFileManager处理目录的方法如下：](#0-2)

**[fileManager currentDirectoryPath];**  
**[fileManager changeCurrentDirectoryPath:path];**  
**[fileManager copyItemAtPath:path toPath:path2 error:err];**  
**[fileManager createDirectoryAtPath:path withIntermediateDirectories:YES attributes:nil error:err];**  
**[fileManager fileExistsAtPath:path isDirectory:YES];**  
**[fileManager enumeratorAtPath:path]; //获取目录的内容列表。一次可以枚举指定目录中的每个文件。 ... ...**  
**Has a delegate with lots of “should” methods (to do an operation or proceed after an error).**  
**And plenty more. Check out the documentation.**

### 1、[文件的创建](#1)

```objectivec
-(IBAction) CreateFile{

    //对于错误信息

    NSError *error;

    // 创建文件管理器

    NSFileManager *fileMgr = [NSFileManager defaultManager];

    //指向文件目录

    NSString *documentsDirectory= [NSHomeDirectory() stringByAppendingPathComponent:@"Documents"];


    //创建一个目录

    [[NSFileManager defaultManager]   createDirectoryAtPath: [NSString stringWithFormat:@"%@/myFolder", NSHomeDirectory()] attributes:nil];

    // File we want to create in the documents directory我们想要创建的文件将会出现在文件目录中

    // Result is: /Documents/file1.txt结果为：/Documents/file1.txt

    NSString *filePath= [documentsDirectory

    stringByAppendingPathComponent:@"file2.txt"];

    //需要写入的字符串

    NSString *str= @"iPhoneDeveloper Tips\nhttp://iPhoneDevelopTips,com";

    //写入文件

    [str writeToFile:filePath atomically:YES encoding:NSUTF8StringEncoding error:&error];

    //显示文件目录的内容

    NSLog(@"Documentsdirectory: %@",[fileMgr contentsOfDirectoryAtPath:documentsDirectory error:&error]);
}
```

### 2、[对文件重命名](#2)

对一个文件重命名,想要重命名一个文件，我们需要把文件移到一个新的路径下。下面的代码创建了我们所期望的目标文件的路径，然后请求移动文件以及在移动之后显示文件目录。

```objectivec
//通过移动该文件对文件重命名
NSString *filePath2= [documentsDirectory
stringByAppendingPathComponent:@"file2.txt"];
//判断是否移动
if ([fileMgr moveItemAtPath:filePath toPath:filePath2 error:&error] != YES)
NSLog(@"Unable to move file: %@", [error localizedDescription]);
//显示文件目录的内容
NSLog(@"Documentsdirectory: %@",
[fileMgr contentsOfDirectoryAtPath:documentsDirectoryerror:&error]);
```

### 3、[删除一个文件](#3)

为了使这个技巧完整，让我们再一起看下如何删除一个文件：

```objectivec
//在filePath2中判断是否删除这个文件
if ([fileMgr removeItemAtPath:filePath2 error:&error] != YES)
NSLog(@"Unable to delete file: %@", [error localizedDescription]);
//显示文件目录的内容
NSLog(@"Documentsdirectory: %@",
[fileMgr contentsOfDirectoryAtPath:documentsDirectoryerror:&error]);
```

一旦文件被删除了，正如你所预料的那样，文件目录就会被自动清空：  
这些示例能教你的，仅仅只是文件处理上的一些皮毛。想要获得更全面、详细的讲解，你就需要掌握NSFileManager文件的知识。

### 4、[删除目录下所有文件](#4)

```objectivec
//获取文件路径
- (NSString *)attchmentFolder{

    NSString *document = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];

    NSString *path = [document stringByAppendingPathComponent:@"Attchments"];


    NSFileManager *manager = [NSFileManager defaultManager];


    if(![manager contentsOfDirectoryAtPath:path error:nil]){

        [manager createDirectoryAtPath:path withIntermediateDirectories:NO attributes:nil error:nil];

    }
    return path;

}
```

--清除附件

```objectivec
BOOL result = [[NSFileManager defaultManager] removeItemAtPath:[[MOPAppDelegate instance] attchmentFolder] error:nil];
```

### 5、[判断文件是否存在](#5)

```objectivec
NSString *filePath = [self dataFilePath];
if ([[NSFileManager defaultManager]fileExistsAtPath:filePath]) 
｛
  //do some thing
｝

-(NSString *)dataFilePath
{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentDirectory = [paths objectAtIndex:0];
    return [documentDirectory stringByAppendingPathComponent:@"data.plist"];
}
```

常用路径工具函数

```objectivec
NSString * NSUserName（）； 返回当前用户的登录名 
NSString * NSFullUserName（）； 返回当前用户的完整用户名 
NSString * NSHomeDirectory（）； 返回当前用户主目录的路径 
NSString * NSHomeDirectoryForUser（）； 返回用户user的主目录 
NSString * NSTemporaryDirectory（）； 返回可用于创建临时文件的路径目录
```

常用路径工具方法

```objectivec
-（NSString *） pathWithComponents：components    根据components（NSArray对象）中元素构造有效路径 
-（NSArray *）pathComponents                                          析构路径，获取路径的各个部分 
-（NSString *）lastPathComponent                                       提取路径的最后一个组成部分 
-（NSString *）pathExtension                                           路径扩展名 
-（NSString *）stringByAppendingPathComponent：path                    将path添加到现有路径末尾 
-（NSString *）stringByAppendingPathExtension：ext           将拓展名添加的路径最后一个组成部分 
-（NSString *）stringByDeletingPathComponent                           删除路径的最后一个部分 
-（NSString *）stringByDeletingPathExtension                           删除路径的最后一个部分 的扩展名 
-（NSString *）stringByExpandingTildeInPath          将路径中的代字符扩展成用户主目录（~）或指定用户主目录（~user） 
-（NSString *）stringByResolvingSymlinksInPath                         尝试解析路径中的符号链接 
-（NSString *）stringByStandardizingPath            通过尝试解析~、..、.、和符号链接来标准化路径
```

使用路径NSPathUtilities.h

```objectivec
tempdir = NSTemporaryDirectory(); 临时文件的目录名 
path = [fm currentDirectoryPath];
[path lastPathComponent]; 从路径中提取最后一个文件名 
fullpath = [path stringByAppendingPathComponent:fname];将文件名附加到路劲的末尾 
extenson = [fullpath pathExtension]; 路径名的文件扩展名 
homedir = NSHomeDirectory();用户的主目录 
component = [homedir pathComponents];  路径的每个部分
```

NSProcessInfo类：允许你设置或检索正在运行的应用程序的各种类型信息

```objectivec
（NSProcessInfo *）processInfo                                  返回当前进程的信息
-（NSArray*）arguments                                           以NSString对象数字的形式返回当前进程的参数
-（NSDictionary *）environment                                   返回变量/值对词典。描述当前的环境变量
-（int）processIdentity                                          返回进程标识
-（NSString *）processName                                       返回进程名称
-（NSString *）globallyUniqueString   每次调用该方法都会返回不同的单值字符串，可以用这个字符串生成单值临时文件名   
-（NSString *）hostname                                          返回主机系统的名称 
-（unsigned int）operatingSystem                                 返回表示操作系统的数字 
-（NSString *）operatingSystemName                                     返回操作系统名称 
-（NSString *）operatingSystemVersionString                                     返回操作系统当前版本
-（void）setProcessName：（NSString *）name                                将当前进程名称设置为name
```

NSFileHandle类允许更有效地使用文件。

可以实现如下功能：

1、打开一个文件，执行读、写或更新（读写）操作；

2、在文件中查找指定位置；

3、从文件中读取特定数目的字节，或将特定数目的字节写入文件中

另外，NSFileHandle类提供的方法也可以用于各种设备或套接字。一般而言，我们处理文件时都要经历以下三个步骤：

1、打开文件，获取一个NSFileHandle对象（以便在后面的I/O操作中引用该文件）。

2、对打开文件执行I/O操作。

3、关闭文件。

```objectivec
NSFileHandle *fileHandle = [[NSFileHandle alloc]init]; 
fileHandle = [NSFileHandle fileHandleForReadingAtPath:path]; //打开一个文件准备读取
fileHandle = [NSFileHandle fileHandleForWritingAtPath:path]; 
fileHandle = [NSFileHandle fileHandleForUpdatingAtPath:path]; 
fileData = [fileHandle availableData]; // 从设备或者通道返回可用的数据 
fileData = [fileHandle readDataToEndOfFile]; 
[fileHandle writeData:fileData]; //将NSData数据写入文件 
[fileHandle closeFile]; //关闭文件 ... ...
```

注：NSFileHandle类没有提供创建文件的功能，所以必须使用NSFileManager来创建文件

参考：http://blog.csdn.net/zhuzhihai1988/article/details/7904333
