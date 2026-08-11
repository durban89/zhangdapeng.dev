---
title: "UIDatePickerView的完美使用 日期选取器"
date: "2025-06-20 11:33:34"
slug: "uidatepickerview-de-wan-mei-shi-yong-ri-qi-xuan-qu-qi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/UIDatePickerView的完美使用-日期选取器/"
  - "/2025/06/20/UIDatePickerView的完美使用-日期选取器.html"
  - "/UIDatePickerView的完美使用-日期选取器/"
  - "/UIDatePickerView的完美使用-日期选取器.html"
  - "/2025/06/20/uidatepickerview-de-wan-mei-shi-yong-ri-qi-xuan-qu-qi/"
  - "/2025/06/20/uidatepickerview-de-wan-mei-shi-yong-ri-qi-xuan-qu-qi.html"
  - "/uidatepickerview-de-wan-mei-shi-yong-ri-qi-xuan-qu-qi.html"
---
在ios的开发中，日期选择器是个用的还是蛮多的一个部分，填写用户的出生日期，填写自己的计划，填写自己的约会安排，都是会有用到日期选择的地方的。

我认为这里面的关键点是设置日期的格式（datePickerMode），还有选择日期后去如何处理(这里我没有做)，

浏览一下代码吧

UIDatePickerDemoViewController.m

```objectivec
//
//  UIDatePickerDemoViewController.m
//  UIDatePickerDemo
//
//  Created by david on 13-8-16.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "UIDatePickerDemoViewController.h"

@interface UIDatePickerDemoViewController ()

@end

@implementation UIDatePickerDemoViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    
    self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    self.navigationItem.rightBarButtonItem = BARBUTTON(@"操作", @selector(action:));
    
    UISegmentedControl *seg= [[UISegmentedControl alloc] initWithItems:[@"Time Date DC Count" componentsSeparatedByString:@" "]];
    seg.segmentedControlStyle = UISegmentedControlStyleBar;
    seg.selectedSegmentIndex = 0;
    self.navigationItem.titleView = seg;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - method of UIActionSheet
-(void) actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex{
    UIDatePicker *datePicker = (UIDatePicker *)[actionSheet viewWithTag:101];
    NSDateFormatter *formattor = [[NSDateFormatter alloc] init];
    
    switch ([(UISegmentedControl *) self.navigationItem.titleView selectedSegmentIndex]) {
        case 0:
            formattor.dateFormat = @"h:mm a";
            break;
        case 1:
            formattor.dateFormat = @"dd MMMM yy";
            break;
        case 2:
            formattor.dateFormat = @"MM/dd/YY h:mm a";
            break;
        case 3:
            formattor.dateFormat = @"HH:mm";
            break;
        default:
            break;
    }
    NSString *timestamp = [formattor stringFromDate:datePicker.date];
    [(UILabel *)[self.view viewWithTag:103] setText:timestamp];
    
}

#pragma mark - method of self
-(void) action:(id)sender{
    NSString *title = UIDeviceOrientationIsLandscape([UIDevice currentDevice].orientation) ? @"\n\n\n\n\n\n\n\n\n" : @"\n\n\n\n\n\n\n\n\n\n\n\n";
    UIActionSheet *actionsheet = [[UIActionSheet alloc] initWithTitle:title
                                                             delegate:self
                                                    cancelButtonTitle:nil
                                               destructiveButtonTitle:nil
                                                    otherButtonTitles:@"请选择日期", nil];
    [actionsheet showInView:self.view];

    UIDatePicker *datepicker = [[UIDatePicker alloc] init];
    datepicker.tag = 101;
    datepicker.datePickerMode = [(UISegmentedControl *)self.navigationItem.titleView selectedSegmentIndex];

    [actionsheet addSubview:datepicker];
}
@end
```

UIDatePickerDemoViewController.h

```objectivec
//
//  UIDatePickerDemoViewController.h
//  UIDatePickerDemo
//
//  Created by david on 13-8-16.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

#define COOKBOOK_PURPLE_COLOR [UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]
#define BARBUTTON(TITLE, SELECTOR) [[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]

@interface UIDatePickerDemoViewController : UIViewController<UIActionSheetDelegate>

@end
```
