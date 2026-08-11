---
title: "iOS 操作post提交数据"
date: "2025-06-16 14:38:06"
slug: "ios-cao-zuo-post-ti-jiao-shu-ju"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/16/iOS-操作post提交数据/"
  - "/2025/06/16/iOS-操作post提交数据.html"
  - "/iOS-操作post提交数据/"
  - "/iOS-操作post提交数据.html"
  - "/2025/06/16/ios-cao-zuo-post-ti-jiao-shu-ju/"
  - "/2025/06/16/ios-cao-zuo-post-ti-jiao-shu-ju.html"
  - "/ios-cao-zuo-post-ti-jiao-shu-ju.html"
---
在做app应用的时候，需要将数据提交到服务器去存储，那么方法可以参考如下，哈，自己搜索整理的

```objectivec
//参数1名字=参数1数据&参数2名字＝参数2数据&参数3名字＝参数3数据&...
NSString *postString = [NSString stringWithFormat:@"app_key=XXXXXXXXXXXXXXXXXX"];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&device_token=%@",deviceId]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&teleplay_title=%@",title]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&job_type=%@",type]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&deadline=%@",time]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&age=%@",age]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&sex=%@",sex]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&people_num=%@",num]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&contact_person=%@",person]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&contact=%@",phone]];
postString = [postString stringByAppendingString:[NSString stringWithFormat:@"&description=%@",description]];

NSLog(@"postString:%@",postString);

//将NSSrring格式的参数转换格式为NSData，POST提交必须用NSData数据。
NSData *postData = [postString dataUsingEncoding:NSUTF8StringEncoding allowLossyConversion:YES];
//计算POST提交数据的长度
NSString *postLength = [NSString stringWithFormat:@"%d",[postData length]];
NSLog(@"postLength=%@",postLength);
//定义NSMutableURLRequest
NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
//设置提交目的url
[request setURL:[NSURL URLWithString:[NSString stringWithFormat:@"http://www.baidu.com"]]];
//设置提交方式为 POST
[request setHTTPMethod:@"POST"];
//设置http-header:Content-Type
//这里设置为 application/x-www-form-urlencoded ，如果设置为其它的，比如text/html;charset=utf-8，或者 text/html 等，都会出错。不知道什么原因。
[request setValue:@"application/x-www-form-urlencoded" forHTTPHeaderField:@"Content-Type"];
//设置http-header:Content-Length
[request setValue:postLength forHTTPHeaderField:@"Content-Length"];
//设置需要post提交的内容
[request setHTTPBody:postData];

//定义
NSHTTPURLResponse* urlResponse = nil;
NSError *error = [[NSError alloc] init];

//设置网络状态显示
[UIApplication sharedApplication].networkActivityIndicatorVisible = YES;

//同步提交:POST提交并等待返回值（同步），返回值是NSData类型。
NSData *responseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&urlResponse error:&error];

//将NSData类型的返回值转换成NSString类型
//    NSString *result = [[NSString alloc] initWithData:responseData encoding:NSUTF8StringEncoding];

//将NSData装换为字典类型
NSError *jsonError = [[NSError alloc] init];
NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:responseData
                                                                 options:NSJSONReadingMutableContainers
                                                                   error:&jsonError];
NSString *status = [personDictionary objectForKey:@"status"];

if ([@"ok" compare:status] == NSOrderedSame) {
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
    return YES;
}
return NO;
```
