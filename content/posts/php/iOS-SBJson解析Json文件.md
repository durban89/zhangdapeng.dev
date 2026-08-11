---
title: "iOS SBJson解析Json文件"
date: "2025-06-10 15:30:39"
slug: "ios-sbjson-jie-xi-json-wen-jian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-SBJson解析Json文件/"
  - "/2025/06/10/iOS-SBJson解析Json文件.html"
  - "/iOS-SBJson解析Json文件/"
  - "/iOS-SBJson解析Json文件.html"
  - "/2025/06/10/ios-sbjson-jie-xi-json-wen-jian/"
  - "/2025/06/10/ios-sbjson-jie-xi-json-wen-jian.html"
  - "/ios-sbjson-jie-xi-json-wen-jian.html"
---
最近在搞到，如何解析json文件，使用ios自带的函数很容易解析出来，但是对于中文的问题，一直困扰着我，于是查看了各种相关资料，最后我的解决方法如下：

1，让我找到了一个兼容ARC机制的类库，SBJson，现在地址：https://github.com/stig/json-framework/downloads，最近的一个版本支持ARC

2，将其下载过来后，引入到项目中，#import "SBJson.h"

3，使用方法是

```objectivec
-(void) test{
    NSLog(@"test 开始运行");
    NSString *testString = [[NSString alloc]initWithString:@"{\"customer\":[{\"name\":\"roamer\",\"ycount\":\"232.4\",\"sumcount\":\"322.3\"},{\"name\":\"王三\",\"ycount\":\"221.2\",\"sumcount\":\"1123.2\"},{\"name\":\"李四\",\"ycount\":\"1221.2\",\"sumcount\":\"12123.2\"}]}"];
    
    SBJsonParser *parser = [[SBJsonParser alloc] init];
    NSLog(@"%@",testString);
    NSError *error = nil;
    
    NSMutableDictionary *root = [[NSMutableDictionary alloc] initWithDictionary:[parser objectWithString:testString error:&error]];
    //注意转换代码
    SBJsonWriter *jsonWriter = [[SBJsonWriter alloc] init];
    NSString *jsonString = [jsonWriter stringWithObject:root];
    NSLog(@"%@",jsonString);
    //注意转换代码
    NSMutableArray * customers = [root objectForKey:@"customer"];
    NSLog(@"%@",customers);
    for(NSMutableDictionary * member  in customers){
        NSLog(@"%@",[[member objectForKey:@"name"] description]);
    }
}
```

上面只是一个，自己写的json格式的字符串，自己可以使用来自远程获取的数据，做一下测试
