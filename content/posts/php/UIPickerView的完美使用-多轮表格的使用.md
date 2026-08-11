---
title: "UIPickerView的完美使用  多轮表格的使用"
date: "2025-06-20 11:33:10"
slug: "uipickerview-de-wan-mei-shi-yong-duo-lun-biao-ge-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/UIPickerView的完美使用-多轮表格的使用/"
  - "/2025/06/20/UIPickerView的完美使用-多轮表格的使用.html"
  - "/UIPickerView的完美使用-多轮表格的使用/"
  - "/UIPickerView的完美使用-多轮表格的使用.html"
  - "/2025/06/20/uipickerview-de-wan-mei-shi-yong-duo-lun-biao-ge-de-shi-yong/"
  - "/2025/06/20/uipickerview-de-wan-mei-shi-yong-duo-lun-biao-ge-de-shi-yong.html"
  - "/uipickerview-de-wan-mei-shi-yong-duo-lun-biao-ge-de-shi-yong.html"
---
之前自己也使用过，但是感觉很是别扭，还要调试什么尺寸的这个问题，今天看了cookbook的方法，明白了，该如何使用，来个例子好了。

UIPickerViewDemoViewController.h

```objectivec
//
//  UIPickerViewDemoViewController.h
//  UIPickerViewDemo
//
//  Created by david on 13-8-14.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

#define COOKBOOK_PURPLE_COLOR [UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]
#define BARBUTTON(TITLE, SELECTOR) [[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]

@interface UIPickerViewDemoViewController : UIViewController<UIPickerViewDataSource,UIPickerViewDelegate,UIActionSheetDelegate>

@end
```

UIPickerViewDemoViewController.m

```objectivec
//
//  UIPickerViewDemoViewController.m
//  UIPickerViewDemo
//
//  Created by david on 13-8-14.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "UIPickerViewDemoViewController.h"

@interface UIPickerViewDemoViewController ()

@end

@implementation UIPickerViewDemoViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    
    self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    self.navigationItem.rightBarButtonItem = BARBUTTON(@"操作", @selector(action:));
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation{
    return YES;
}

#pragma mark - UIPickerView Method
-(NSInteger) numberOfComponentsInPickerView:(UIPickerView *)pickerView{
    return 3;
}

-(NSInteger) pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{
    return 20;
}

-(NSString *) pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component{
    return [NSString stringWithFormat:@"%@-%d", (component == 1 ? @"R" : @"L"), row];
}

-(void) actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex{
    UIPickerView *pickerView = (UIPickerView *)[actionSheet viewWithTag:101];
    self.title = [NSString stringWithFormat:@"L%d-R%d-L%d",[pickerView selectedRowInComponent:0], [pickerView selectedRowInComponent:1], [pickerView selectedRowInComponent:2]];
    
}

-(void) action:(id)sender{
    NSString *title = UIDeviceOrientationIsLandscape([UIDevice currentDevice].orientation) ? @"\n\n\n\n\n\n\n\n\n" : @"\n\n\n\n\n\n\n\n\n\n\n\n";
    UIActionSheet *actionsheet = [[UIActionSheet alloc] initWithTitle:title
                                                             delegate:self
                                                    cancelButtonTitle:nil
                                               destructiveButtonTitle:nil
                                                    otherButtonTitles:@"选择此项", nil];
    [actionsheet showInView:self.view];
    
    UIPickerView *pickerView = [[UIPickerView alloc] init];
    pickerView.tag = 101;
    pickerView.delegate = self;
    pickerView.dataSource = self;
    pickerView.showsSelectionIndicator = YES;
    
    [actionsheet addSubview:pickerView];
    
    CFShow((__bridge CFTypeRef)(NSStringFromCGRect(pickerView.frame)));
}
@end
```

在自己的项目中，没有任何强制要求的前提下，完全是可以做出很华丽的应用的，要掌握正确的使用方式。

这里面其实重点是要使用代理方法UIPickerViewDataSource,UIPickerViewDelegate,UIActionSheetDelegate这个三个在这里是不能少的。
