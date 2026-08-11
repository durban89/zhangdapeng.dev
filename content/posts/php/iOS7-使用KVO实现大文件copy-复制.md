---
title: "iOS7 使用KVO实现大文件copy（复制）"
date: "2025-06-26 11:45:09"
slug: "ios7-shi-yong-kvo-shi-xian-da-wen-jian-copy-fu-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-使用KVO实现大文件copy（复制）/"
  - "/2025/06/26/iOS7-使用KVO实现大文件copy（复制）.html"
  - "/iOS7-使用KVO实现大文件copy（复制）/"
  - "/iOS7-使用KVO实现大文件copy（复制）.html"
  - "/2025/06/26/iOS7-使用KVO实现大文件copy-复制/"
  - "/2025/06/26/iOS7-使用KVO实现大文件copy-复制.html"
  - "/2025/06/26/ios7-shi-yong-kvo-shi-xian-da-wen-jian-copy-fu-zhi/"
  - "/2025/06/26/ios7-shi-yong-kvo-shi-xian-da-wen-jian-copy-fu-zhi.html"
  - "/ios7-shi-yong-kvo-shi-xian-da-wen-jian-copy-fu-zhi.html"
---
之前的一篇文章里面有说关于大文件的copy，这里介绍一下使用kvo的方式，进行文件copy（复制），其实就是检测文件copy的进度。

代码如下:建立两个类FileHandle和Computer

Computer.m

```objectivec
//
//  Computer.m
//  FileCopyKVODemo
//
//  Created by Durban on 13-12-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "Computer.h"
#import "FileHandle.h"

@implementation Computer

@synthesize filehandle = _filehandle;

-(id) init
{
    self = [super init];
    if(self != nil)
    {
        NSString *homePath = NSHomeDirectory();
        NSString *srcPath = [homePath stringByAppendingPathComponent:@"android系统框架的介绍.avi"];
        NSString *targetPath = [homePath stringByAppendingPathComponent:@"android系统框架的介绍1.avi"];
        
        _filehandle = [[FileHandle alloc] initWithSrcPath:srcPath withTargetPath:targetPath];
        [_filehandle addObserver:self
                      forKeyPath:@"readSize"
                         options:NSKeyValueObservingOptionNew
                         context:nil];
    }
    return self;
}

-(void) copyAction
{
    [_filehandle runCopy];
}


-(void) observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    if([keyPath isEqualToString:@"readSize"])
    {
        if([object isKindOfClass:[FileHandle class]])
        {
            NSNumber *readSieNum = [change objectForKey:@"new"];
            float readSize = [readSieNum floatValue];
            
            FileHandle *file = (FileHandle *)object;
            float fileSize = file.fileSize;
            
            float ret = readSize / fileSize * 100;
            NSLog(@"%0.1f%%",ret);
        }
    }
}
@end
```

Computer.h

```objectivec
//
//  Computer.h
//  FileCopyKVODemo
//
//  Created by Durban on 13-12-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@class FileHandle;
@interface Computer : NSObject

@property (nonatomic , strong) FileHandle *filehandle;
-(void) copyAction;

@end
```

FileHandle.m

```objectivec
//
//  FileHandle.m
//  FileCopyKVODemo
//
//  Created by Durban on 13-12-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "FileHandle.h"

@implementation FileHandle
@synthesize srcPath = _srcPath;
@synthesize targetPath = _targetPath;

-(id) initWithSrcPath:(NSString *)srcPath withTargetPath:(NSString *)targetPath;
{
    self = [super init];
    if(self != nil)
    {
        _srcPath = [srcPath copy];
        _targetPath = [targetPath copy];
    }
    return self;
    
}

-(void) runCopy
{
    //读取大文件，并写入大文件中
    NSFileManager *fileManager = [NSFileManager defaultManager];
    
//    NSString *homePath = NSHomeDirectory();
//    NSString *srcPath = [homePath stringByAppendingPathComponent:@"android学习路线图介绍.avi"];
//    NSString *targetPath = [homePath stringByAppendingPathComponent:@"android学习路线图介绍1.avi"];
    
    BOOL success = [fileManager createFileAtPath:_targetPath
                                        contents:nil
                                      attributes:nil];
    if(success)
    {
        NSLog(@"成功创建文件 ：%@",_targetPath);
    }
    
    NSFileHandle *infile = [NSFileHandle fileHandleForWritingAtPath:_targetPath];
    NSFileHandle *outfile = [NSFileHandle fileHandleForReadingAtPath:_srcPath];
    
    //获取文件的尺寸
    NSDictionary *fileAttr = [fileManager attributesOfItemAtPath:_srcPath
                                                           error:nil];
    NSNumber *fileSizeNum = [fileAttr objectForKey:NSFileSize];
    
    BOOL isEnd = NO;
    self.fileSize = [fileSizeNum longLongValue];
    
    while (!isEnd) {
        NSData *data = nil;
        NSInteger subleng = self.fileSize - _readSize;
        if(subleng < 500)
        {
            isEnd = YES;
            data = [outfile readDataToEndOfFile];
        }
        else
        {
            data = [outfile readDataOfLength:500];
            self.readSize += 500;
            [outfile seekToFileOffset:_readSize];
        }
        [infile writeData:data];
    }
    [infile closeFile];
    [outfile closeFile];
}

@end
```

FileHandle.h

```objectivec
//
//  FileHandle.h
//  FileCopyKVODemo
//
//  Created by Durban on 13-12-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface FileHandle : NSObject


@property (nonatomic, strong) NSString *srcPath;
@property (nonatomic, strong) NSString *targetPath;

@property (nonatomic ,assign) float fileSize;
@property (nonatomic, assign) float readSize;

-(id) initWithSrcPath:(NSString *)srcPath withTargetPath:(NSString *)targetPath;
-(void) runCopy;

@end
```

示例调用的代码-实现过程是这样子的：

```objectivec
//
//  main.m
//  FileCopyKVODemo
//
//  Created by Durban on 13-12-20.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Computer.h"

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        Computer *computer = [[Computer alloc] init];
        [computer copyAction];
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

gowhich得到的结果是，文件进行了完整的copy，并且能进行正常使用，没有出现文件损坏。看看结果吧。

```bash
2013-12-20 10:13:43.356 FileCopyKVODemo[8446:303] 成功创建文件 ：/Users/davidzhang/android系统框架的介绍1.avi
2013-12-20 10:13:43.789 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.883 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.884 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.884 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.885 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.885 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.886 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.886 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:43.887 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.139 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.140 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.141 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.141 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.142 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.142 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.143 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.143 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.144 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.145 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:44.145 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.041 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.041 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.042 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.043 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.043 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.054 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.055 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.056 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.056 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.057 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.057 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.058 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.058 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.633 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.634 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.635 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.635 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.636 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.636 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.637 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.637 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.638 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.639 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.639 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.640 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.640 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.640 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.641 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.641 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.642 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.642 FileCopyKVODemo[8446:303] 0.0%
2013-12-20 10:13:46.643 FileCopyKVODemo[8446:303] 0.0%
。。。。。。
```

这里自己可以进行调整的，比如百分比的小数位可以调整大点，都是可以的。

