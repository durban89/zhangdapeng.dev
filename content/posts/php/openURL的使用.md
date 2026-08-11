---
title: "openURL的使用"
date: "2025-06-17 16:45:54"
slug: "openurl-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/openURL的使用/"
  - "/2025/06/17/openURL的使用.html"
  - "/openURL的使用/"
  - "/openURL的使用.html"
  - "/2025/06/17/openurl-de-shi-yong/"
  - "/2025/06/17/openurl-de-shi-yong.html"
  - "/openurl-de-shi-yong.html"
---
查资料的时候无意间发现了一个很好玩的：

代码段：[[UIApplication sharedApplication] openURL:url];  
  
其中系统的url有：

1.Map  `http://maps.google.com/maps?q=Shanghai`

2.Email  `mailto://myname@google.com`  

3.Tel  `tel://10086`

4.Msg  `sms://10086`

```objectivec
- (IBAction)openMaps {
//打开地图 
NSString*addressText = @"beijing";
//@"1Infinite Loop, Cupertino, CA 95014"; 
addressText =[addressText stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding]; 

NSString  *urlText = [NSString stringWithFormat:@"http://maps.google.com/maps?q=%@",addressText]; 
NSLog(@"urlText=============== %@", urlText);
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:urlText]];
}

- (IBAction)openEmail {
//打开mail // Fire off an email to apple support
[[UIApplication sharedApplication]openURL:[NSURL   URLWithString:@"mailto://devprograms@apple.com"]];
} 

- (IBAction)openPhone {

//拨打电话
// Call Google 411
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"tel://10086"]];
} 

- (IBAction)openSms {
//打开短信
// Text toGoogle SMS
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"sms://10086"]];
}

-(IBAction)openBrowser {
//打开浏览器
// Lanuch any iPhone developers fav site
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://blog.csdn.net/duxinfeng2010"]];
}
```

参考资料：http://blog.csdn.net/duxinfeng2010/article/details/8176317
