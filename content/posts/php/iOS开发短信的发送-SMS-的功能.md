---
title: "iOS开发短信的发送（SMS）的功能"
date: "2025-06-20 10:36:15"
slug: "ios-kai-fa-duan-xin-de-fa-song-sms-de-gong-neng"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/iOS开发短信的发送（SMS）的功能/"
  - "/2025/06/20/iOS开发短信的发送（SMS）的功能.html"
  - "/iOS开发短信的发送（SMS）的功能/"
  - "/iOS开发短信的发送（SMS）的功能.html"
  - "/2025/06/20/iOS开发短信的发送-SMS-的功能/"
  - "/2025/06/20/iOS开发短信的发送-SMS-的功能.html"
  - "/2025/06/20/ios-kai-fa-duan-xin-de-fa-song-sms-de-gong-neng/"
  - "/2025/06/20/ios-kai-fa-duan-xin-de-fa-song-sms-de-gong-neng.html"
  - "/ios-kai-fa-duan-xin-de-fa-song-sms-de-gong-neng.html"
---
在ios的开发中，如果自己想调用一个发送短信的方式，其实可以很简答的调用的

短信的发送（SMS）的发送，是使用了一个MessageUI库，然后使用里面的MFMessageComposeViewControllerDelegate协议

我将自己的演示代码贴到下面：

SMSViewController.h

```objectivec
//
//  SMSViewController.h
//  SMS
//
//  Created by david on 13-8-2.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MessageUI/MessageUI.h>


@interface SMSViewController : UIViewController<MFMessageComposeViewControllerDelegate,UINavigationBarDelegate>
- (IBAction)showSMSPicker:(id)sender;

@end
```

SMSViewController.m

```objectivec
//
//  SMSViewController.m
//  SMS
//
//  Created by david on 13-8-2.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "SMSViewController.h"

@interface SMSViewController ()

@end

@implementation SMSViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)showSMSPicker:(id)sender {
    
    if([MFMessageComposeViewController canSendText]){
        [self displaySMSComposeSheet];
    }else{
        NSLog(@"Device not configured to send SMS.");
    }
}

-(void) displaySMSComposeSheet{
    MFMessageComposeViewController *picker = [[MFMessageComposeViewController alloc] init];
    picker.messageComposeDelegate = self;
    
    picker.body = @"你好，今天很想与你共进午餐";
    [self presentViewController:picker
                       animated:YES
                     completion:NULL];
}

-(void) messageComposeViewController:(MFMessageComposeViewController *)controller didFinishWithResult:(MessageComposeResult)result{
    
    // Notifies users about errors associated with the interface
    switch (result)
    {
        case MessageComposeResultCancelled:
            NSLog(@"Result: SMS sending canceled");
            break;
        case MessageComposeResultSent:
            NSLog(@"Result: SMS sent");
            break;
        case MessageComposeResultFailed:
            NSLog(@"Result: SMS sending failed");
            break;
        default:
            NSLog(@"Result: SMS not sent");
            break;
    }
    
    [self dismissViewControllerAnimated:YES completion:NULL];
}

-(BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation{
    return (toInterfaceOrientation == UIInterfaceOrientationMaskPortrait);
}
@end
```

ok，直接运行一下就可以了。模拟器似乎是不能使用的，要在真机上才可以测试的
