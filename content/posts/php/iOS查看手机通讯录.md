---
title: "iOS查看手机通讯录"
date: "2025-06-23 15:49:31"
slug: "ios-cha-kan-shou-ji-tong-xun-lu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS查看手机通讯录/"
  - "/2025/06/23/iOS查看手机通讯录.html"
  - "/iOS查看手机通讯录/"
  - "/iOS查看手机通讯录.html"
  - "/2025/06/23/ios-cha-kan-shou-ji-tong-xun-lu/"
  - "/2025/06/23/ios-cha-kan-shou-ji-tong-xun-lu.html"
  - "/ios-cha-kan-shou-ji-tong-xun-lu.html"
---
查看iphone的手机通讯录的话，需要用到一个库AddressBook。

可以使用里面的方法调用我们自己的通许录

```objectivec
-(void) getPhoneContacts{
    ABAddressBookRef addressBook = nil;
    if([[UIDevice currentDevice].systemVersion doubleValue] >= 6.0)
    {
        addressBook = ABAddressBookCreateWithOptions(NULL, NULL);
        
        dispatch_semaphore_t sema = dispatch_semaphore_create(0);
        ABAddressBookRequestAccessWithCompletion(addressBook, ^(bool granted, CFErrorRef error) {
            dispatch_semaphore_signal(sema);
        });
        dispatch_semaphore_wait(sema, DISPATCH_TIME_FOREVER);
    }
    else
    {
        addressBook = ABAddressBookCreate();
    }
    
    NSArray *temPeoples = (__bridge NSArray *) ABAddressBookCopyArrayOfAllPeople(addressBook);
    for(id temPerson in temPeoples)
    {
        NSMutableDictionary *dic = [[NSMutableDictionary alloc] initWithCapacity:2];
        NSMutableArray *phoneArray = [[NSMutableArray alloc] initWithCapacity:3];
        
        NSString *tmpFirstName = (__bridge NSString *) ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonFirstNameProperty);
        NSString *tmpLastName = (__bridge NSString *) ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonLastNameProperty);
        
        [dic setValue:[NSString stringWithFormat:@"%@ %@", tmpFirstName, tmpLastName] forKey:@"name"];
        ABMultiValueRef phone = ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonPhoneProperty);
        
        for(int k = 0; k < ABMultiValueGetCount(phone); k++)
        {
            NSString *personPhone = (__bridge NSString *) ABMultiValueCopyValueAtIndex(phone, k);
            [phoneArray addObject:personPhone];
        }
        
        [dic setValue:phoneArray forKey:@"phone"];
        [resultArray addObject:dic];
    }
}
```

ABAddressBookCreate

和

ABAddressBookCreateWithOptions，ABAddressBookRequestAccessWithCompletion

是不同版本所使用的方法

ABAddressBookCreate适用于6.0以上的，另外的则使用雨6.0以后的，

之后调用ABAddressBookCopyArrayOfAllPeople，获取通讯录的内容。

代码如下：

PhoneContactsViewController.m

```objectivec
//
//  PhoneContactsViewController.m
//  PhoneContacts
//
//  Created by david on 13-9-25.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "PhoneContactsViewController.h"
#import <AddressBook/AddressBook.h>

@interface PhoneContactsViewController ()

@end

@implementation PhoneContactsViewController

@synthesize resultArray;
@synthesize tableView;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Dispose of any resources that can be recreated.
    self.navigationItem.title = @"查看手机通讯录";
    resultArray = [[NSMutableArray alloc] initWithCapacity:100];
    [self getPhoneContacts];
    
    //left的button
    UIButton *btnBack = [UIButton buttonWithType:UIButtonTypeCustom];
    [btnBack setFrame:CGRectMake(0, 0, 25, 26)];
    [btnBack setTitle:@"返回" forState:UIControlStateNormal];
    [btnBack addTarget:self action:@selector(pressBtnBack) forControlEvents:UIControlEventTouchUpInside];
    UIBarButtonItem *leftBtn = [[UIBarButtonItem alloc] initWithCustomView:btnBack];
    self.navigationItem.leftBarButtonItem = leftBtn;
    
    
    //表表格处理
    tableView = [[UITableView alloc] initWithFrame:CGRectMake(0.0, 0.0, self.view.frame.size.width, self.view.frame.size.height - 44.0) style:UITableViewStylePlain];
    [tableView setDelegate:self];
    [tableView setDataSource:self];
    [tableView setShowsHorizontalScrollIndicator:NO];
    [tableView setShowsVerticalScrollIndicator:NO];
    [self.view addSubview:tableView];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    
}

-(void) pressBtnBack{
    [self.navigationController popViewControllerAnimated:YES];
}

-(void) getPhoneContacts{
    ABAddressBookRef addressBook = nil;
    if([[UIDevice currentDevice].systemVersion doubleValue] >= 6.0)
    {
        addressBook = ABAddressBookCreateWithOptions(NULL, NULL);
        
        dispatch_semaphore_t sema = dispatch_semaphore_create(0);
        ABAddressBookRequestAccessWithCompletion(addressBook, ^(bool granted, CFErrorRef error) {
            dispatch_semaphore_signal(sema);
        });
        dispatch_semaphore_wait(sema, DISPATCH_TIME_FOREVER);
    }
    else
    {
        addressBook = ABAddressBookCreate();
    }
    
    NSArray *temPeoples = (__bridge NSArray *) ABAddressBookCopyArrayOfAllPeople(addressBook);
    for(id temPerson in temPeoples)
    {
        NSMutableDictionary *dic = [[NSMutableDictionary alloc] initWithCapacity:2];
        NSMutableArray *phoneArray = [[NSMutableArray alloc] initWithCapacity:3];
        
        NSString *tmpFirstName = (__bridge NSString *) ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonFirstNameProperty);
        NSString *tmpLastName = (__bridge NSString *) ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonLastNameProperty);
        
        [dic setValue:[NSString stringWithFormat:@"%@ %@", tmpFirstName, tmpLastName] forKey:@"name"];
        ABMultiValueRef phone = ABRecordCopyValue((__bridge ABRecordRef)(temPerson), kABPersonPhoneProperty);
        
        for(int k = 0; k < ABMultiValueGetCount(phone); k++)
        {
            NSString *personPhone = (__bridge NSString *) ABMultiValueCopyValueAtIndex(phone, k);
            [phoneArray addObject:personPhone];
        }
        
        [dic setValue:phoneArray forKey:@"phone"];
        [resultArray addObject:dic];
    }
}

-(NSInteger) tableView:(UITableView *)tableView indentationLevelForRowAtIndexPath:(NSIndexPath *)indexPath
{
    return 1;
}

-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [resultArray count];
}

-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *cellIdentifier = @"cell";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:cellIdentifier];
    if(cell == nil)
    {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleValue1 reuseIdentifier:cellIdentifier];
        [cell setSelectionStyle:UITableViewCellSelectionStyleGray];
    }

    
    NSDictionary *dic = [resultArray objectAtIndex:indexPath.row];
    NSString *strName = [dic valueForKey:@"name"];
    
    strName = [strName stringByReplacingOccurrencesOfString:@"(null)" withString:@""];

    cell.textLabel.text = strName;
    cell.detailTextLabel.text = @"邀请";
    return cell;
}

-(void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [self performSelector:@selector(deleteSelectedCell) withObject:nil afterDelay:0.1];
    NSDictionary *dic = [resultArray objectAtIndex:indexPath.row];
    NSArray *numArray = [dic valueForKey:@"phone"];
    UIActionSheet *sheet = [[UIActionSheet alloc] init];
    [sheet setTitle:@"请选择号码"];
    for(NSString *number in numArray)
    {
        [sheet addButtonWithTitle:number];
    }
    
    [sheet addButtonWithTitle:@"取消"];
    [sheet setDelegate:self];
    [sheet setCancelButtonIndex:[numArray count]];
    
    [sheet setActionSheetStyle:UIActionSheetStyleBlackTranslucent];
    [sheet showInView:self.view];
}

-(void) deleteSelectedCell
{
    [tableView deselectRowAtIndexPath:[tableView indexPathForSelectedRow] animated:YES];
}

-(void) actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex
{
    NSString *string = [actionSheet buttonTitleAtIndex:buttonIndex];
    if([string isEqualToString:@"取消"])
    {
        return;
    }
    
    [self showMSMViewByNumber:string];
}

-(void) showMSMViewByNumber:(NSString *)string
{
    if([MFMessageComposeViewController canSendText]){
        [self displaySMSComposeSheet:string];
    }else{
        NSLog(@"Device not configured to send SMS.");
    }
}

-(void) displaySMSComposeSheet:(NSString *)string
{
    MFMessageComposeViewController *picker = [[MFMessageComposeViewController alloc] init];
    picker.messageComposeDelegate = self;
    picker.body = @"老婆我爱你";
    picker.recipients = [NSArray arrayWithObjects:string, nil];
    [self presentModalViewController:picker animated:YES];
}

-(void) messageComposeViewController:(MFMessageComposeViewController *)controller didFinishWithResult:(MessageComposeResult)result
{
    switch (result) {
        case MessageComposeResultSent:
            NSLog(@"信息发送成功!");
            break;
        case MessageComposeResultFailed:
            NSLog(@"信息发送失败!");
            break;
            
        default:
            break;
    }
    [self dismissModalViewControllerAnimated:YES];
}

@end
```

PhoneContactsViewController.h

```objectivec
//
//  PhoneContactsViewController.h
//  PhoneContacts
//
//  Created by david on 13-9-25.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MessageUI/MessageUI.h>

@interface PhoneContactsViewController : UIViewController<UITableViewDataSource, UITableViewDelegate, UIActionSheetDelegate, MFMessageComposeViewControllerDelegate>

@property (strong, nonatomic) NSMutableArray *resultArray;
@property (strong, nonatomic) UITableView *tableView;

@end
```

别忘记引入文件：MessageUI和AddressBook

