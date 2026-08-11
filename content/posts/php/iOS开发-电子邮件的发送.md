---
title: "iOS开发 电子邮件的发送"
date: "2025-06-20 10:36:11"
slug: "ios-kai-fa-dian-zi-you-jian-de-fa-song"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS开发-电子邮件的发送/"
  - "/2025/06/20/iOS开发-电子邮件的发送.html"
  - "/iOS开发-电子邮件的发送/"
  - "/iOS开发-电子邮件的发送.html"
  - "/2025/06/20/ios-kai-fa-dian-zi-you-jian-de-fa-song/"
  - "/2025/06/20/ios-kai-fa-dian-zi-you-jian-de-fa-song.html"
  - "/ios-kai-fa-dian-zi-you-jian-de-fa-song.html"
---
在ios开发中，电子邮件的发送，看起来是很简单的

只要使用这个MFMailComposeViewControllerDelegate代理就好了

同时还有调用#import <MessageUI/MessageUI.h>这个库

演示一下吧

MailViewController.h

```objectivec
//
//  MailViewController.h
//  Mail
//
//  Created by david on 13-8-2.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MessageUI/MessageUI.h>

@interface MailViewController : UIViewController<MFMailComposeViewControllerDelegate, UINavigationBarDelegate>
- (IBAction)showMailPicker:(id)sender;

@end
```

MailViewController.m

```objectivec
//
//  MailViewController.m
//  Mail
//
//  Created by david on 13-8-2.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "MailViewController.h"

@interface MailViewController ()

@end

@implementation MailViewController

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



- (IBAction)showMailPicker:(id)sender {
    if([MFMailComposeViewController canSendMail]){
        [self displayMailComposerSheet];
    }else{
        NSLog(@"Device not configured to send SMS.");
    }
    
}

- (void)displayMailComposerSheet
{
    MFMailComposeViewController *picker = [[MFMailComposeViewController alloc] init];
    picker.mailComposeDelegate = self;
    
    [picker setSubject:@"Hello from California!"];
    
    // Set up recipients
    NSArray *toRecipients = [NSArray arrayWithObject:@"xx@xx"];
    NSArray *ccRecipients = [NSArray arrayWithObjects:@"xx@xx", @"xx@xx", nil];
    NSArray *bccRecipients = [NSArray arrayWithObject:@"xx@xx"];
    
    [picker setToRecipients:toRecipients];
    [picker setCcRecipients:ccRecipients];
    [picker setBccRecipients:bccRecipients];
    
    // Attach an image to the email
    NSString *path = [[NSBundle mainBundle] pathForResource:@"rainy" ofType:@"jpg"];
    NSData *myData = [NSData dataWithContentsOfFile:path];
    [picker addAttachmentData:myData mimeType:@"image/jpeg" fileName:@"rainy"];
    
    // Fill out the email body text
    NSString *emailBody = @"It is raining in sunny California!";
    [picker setMessageBody:emailBody isHTML:NO];
    
    [self presentViewController:picker animated:YES completion:NULL];
}

#pragma mark - delegate Methods

- (void)mailComposeController:(MFMailComposeViewController*)controller
          didFinishWithResult:(MFMailComposeResult)result error:(NSError*)error{
    // Notifies users about errors associated with the interface
    switch (result)
    {
        case MFMailComposeResultCancelled:
            NSLog(@"Result: Mail sending canceled") ;
            break;
        case MFMailComposeResultSaved:
            NSLog(@"Result: Mail saved") ;
            break;
        case MFMailComposeResultSent:
            NSLog(@"Result: Mail sent") ;
            break;
        case MFMailComposeResultFailed:
            NSLog(@"Result: Mail sending failed") ;
            break;
        default:
            NSLog(@"Result: Mail not sent") ;
            break;
    }
    
    [self dismissViewControllerAnimated:YES completion:NULL];
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}
@end
```

运行一下就可以了。如果提示“Device not configured to send SMS.”

那么请在设置中打开邮件那个选项吧
