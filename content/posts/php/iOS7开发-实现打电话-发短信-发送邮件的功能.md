---
title: "iOS7开发 实现打电话 发短信 发送邮件的功能"
date: "2025-06-26 10:32:37"
slug: "ios7-kai-fa-shi-xian-da-dian-hua-fa-duan-xin-fa-song-you-jian-de-gong-neng"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7开发-实现打电话-发短信-发送邮件的功能/"
  - "/2025/06/26/iOS7开发-实现打电话-发短信-发送邮件的功能.html"
  - "/iOS7开发-实现打电话-发短信-发送邮件的功能/"
  - "/iOS7开发-实现打电话-发短信-发送邮件的功能.html"
  - "/2025/06/26/ios7-kai-fa-shi-xian-da-dian-hua-fa-duan-xin-fa-song-you-jian-de-gong-neng/"
  - "/2025/06/26/ios7-kai-fa-shi-xian-da-dian-hua-fa-duan-xin-fa-song-you-jian-de-gong-neng.html"
  - "/ios7-kai-fa-shi-xian-da-dian-hua-fa-duan-xin-fa-song-you-jian-de-gong-neng.html"
---
最近搞ios开发遇到一个很小的问题，就是在你的应用里面给你一个号码，如何用这个号码进行拨打电话，想了半天，还是google给力。找到了一篇帖子，so，总结如下

1、调用 自带mail

```objectivec
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"mailto://xx@xx"]];
```

2、调用 电话phone

```objectivec
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"tel://8008808888"]];
```

3、调用 SMS

```objectivec
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"sms://800888"]];
```

4、调用自带 浏览器 safari

```objectivec
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://www.hzlzh.com"]];
```

#### [发送短信](#1)

调用phone可以传递号码，调用SMS 只能设定号码，不能初始化SMS内容。

若需要传递内容可以做如下操作：

加入：MessageUI.framework

`#import <MessageUI/MFMessageComposeViewController.h>`

实现代理：MFMessageComposeViewControllerDelegate

调用sendSMS函数

```objectivec
//内容，收件人列表
- (void)sendSMS:(NSString *)bodyOfMessage recipientList:(NSArray *)recipients
{
    
    MFMessageComposeViewController *controller = [[[MFMessageComposeViewController alloc] init] autorelease];
    
    if([MFMessageComposeViewController canSendText])
        
    {
        
        controller.body = bodyOfMessage;
        
        controller.recipients = recipients;
        
        controller.messageComposeDelegate = self;
        
        [self presentModalViewController:controller animated:YES];
        
    }
    
}
// 处理发送完的响应结果
- (void)messageComposeViewController:(MFMessageComposeViewController *)controller didFinishWithResult:(MessageComposeResult)result
{
    [self dismissModalViewControllerAnimated:YES];
    
    if (result == MessageComposeResultCancelled)
    {
        NSLog(@"Message cancelled")
    }
    else if(result == MessageComposeResultSent)
    {
        NSLog(@"Message sent")
    }
    else
    {
        NSLog(@"Message failed")
    }
                
}
```

#### [发送邮件](#2)

导入`#import <MessageUI/MFMailComposeViewController.h>`

实现代理：MFMailComposeViewControllerDelegate

```objectivec
//发送邮件
-(void)sendMail:(NSString *)subject content:(NSString *)content{
    
    MFMailComposeViewController *controller = [[[MFMailComposeViewController alloc] init] autorelease];
    
    if([MFMailComposeViewController canSendMail])
        
    {
        
        [controller setSubject:subject];
        
        [controller setMessageBody:content isHTML:NO];
        
        controller.mailComposeDelegate = self;
        
        [self presentModalViewController:controller animated:YES];
        
    }
}
//邮件完成处理
-(void)mailComposeController:(MFMailComposeViewController *)controller didFinishWithResult:(MFMailComposeResult)result error:(NSError *)error{
    
    [self dismissModalViewControllerAnimated:YES];
    
    if (result == MessageComposeResultCancelled)
    {
        NSLog(@"Message cancelled");
    }
    else if(result == MessageComposeResultSent)
    {
        NSLog(@"Message sent");
    }
    else
    {
        NSLog(@"Message failed");
    }
}
```

默认发送短信的界面为英文的，解决办法为：

在.xib 中的Localization添加一組chinese就ok了

