---
title: "UIPickerView的完美使用 基于视图的选取器"
date: "2025-06-20 11:33:31"
slug: "uipickerview-de-wan-mei-shi-yong-ji-yu-shi-tu-de-xuan-qu-qi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/UIPickerView的完美使用-基于视图的选取器/"
  - "/2025/06/20/UIPickerView的完美使用-基于视图的选取器.html"
  - "/UIPickerView的完美使用-基于视图的选取器/"
  - "/UIPickerView的完美使用-基于视图的选取器.html"
  - "/2025/06/20/uipickerview-de-wan-mei-shi-yong-ji-yu-shi-tu-de-xuan-qu-qi/"
  - "/2025/06/20/uipickerview-de-wan-mei-shi-yong-ji-yu-shi-tu-de-xuan-qu-qi.html"
  - "/uipickerview-de-wan-mei-shi-yong-ji-yu-shi-tu-de-xuan-qu-qi.html"
---
UIPickerView的完美使用 基于视图的选取器

关于这个，其实在许多的项目开发中，还是有很多必要的，因为，你要实现一个图片说明，而不需要文字的话，这个就是个关键点，使用图标来做选择项。

原理其实也是很简单的，只要在`-(UIView *) pickerView:(UIPickerView *)pickerView viewForRow:(NSInteger)row forComponent:(NSInteger)component reusingView:(UIView *)view`

实现对每个Component中的row进行uiview的操作就好了。

```objectivec
-(UIView *) pickerView:(UIPickerView *)pickerView viewForRow:(NSInteger)row forComponent:(NSInteger)component reusingView:(UIView *)view{
    
    UIImageView *imageView;
    imageView = view ? (UIImageView *)view : [[UIImageView alloc] initWithFrame:CGRectMake(0.0f,
                                                                                           0.0f,
                                                                                           60.0f,
                                                                                           60.0f)];
    
    NSArray *names = [NSArray arrayWithObjects:@"club.png", @"diamond.png", @"heart.png", @"spade.png", nil];
    imageView.image = [UIImage imageNamed:[names objectAtIndex:(row % 4)]];
    CFShow((__bridge CFTypeRef)(imageView.image));
    return imageView;
}
```

是不是很简单，其实UIPickerView里面已经自己的设置了这个方法，很是方便。

代码呈现如下：

ViewBasedPickerViewController.m

```objectivec
//
//  ViewBasedPickerViewController.m
//  View based Picker
//
//  Created by david on 13-8-16.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "ViewBasedPickerViewController.h"

@interface ViewBasedPickerViewController ()

@end

@implementation ViewBasedPickerViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    srandom([NSDate timeIntervalSinceReferenceDate]);
    self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    self.navigationItem.rightBarButtonItem = BARBUTTON(@"操作", @selector(action:));
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - method of uipickerview
-(NSInteger) numberOfComponentsInPickerView:(UIPickerView *)pickerView{
    return 3;
}

-(NSInteger) pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{
    return 1000000;
}

-(CGFloat) pickerView:(UIPickerView *)pickerView rowHeightForComponent:(NSInteger)component{
    return 100.0f;
}

-(UIView *) pickerView:(UIPickerView *)pickerView viewForRow:(NSInteger)row forComponent:(NSInteger)component reusingView:(UIView *)view{
    
    UIImageView *imageView;
    imageView = view ? (UIImageView *)view : [[UIImageView alloc] initWithFrame:CGRectMake(0.0f,
                                                                                           0.0f,
                                                                                           60.0f,
                                                                                           60.0f)];
    
    NSArray *names = [NSArray arrayWithObjects:@"club.png", @"diamond.png", @"heart.png", @"spade.png", nil];
    imageView.image = [UIImage imageNamed:[names objectAtIndex:(row % 4)]];
    CFShow((__bridge CFTypeRef)(imageView.image));
    return imageView;
}

#pragma mark - method of uiactionsheet
-(void)actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex{
    UIPickerView *pickerView = (UIPickerView *)[actionSheet viewWithTag:101];
    NSArray *names = [NSArray arrayWithObjects:@"C",@"D",@"H",@"S", nil];
    
    self.title = [NSString stringWithFormat:@"%@•%@•%@",
                  [names objectAtIndex:([pickerView selectedRowInComponent:0] % 4)],
                  [names objectAtIndex:([pickerView selectedRowInComponent:1] % 4)],
                  [names objectAtIndex:([pickerView selectedRowInComponent:2] % 4)]
                  ];
    
    
}

#pragma mark - method of self
-(void) action:(id) sender{
    NSString *title = UIDeviceOrientationIsLandscape([UIDevice currentDevice].orientation) ? @"\n\n\n\n\n\n\n\n\n" : @"\n\n\n\n\n\n\n\n\n\n\n\n";
    UIActionSheet *actionsheet = [[UIActionSheet alloc] initWithTitle:title
                                                             delegate:self
                                                    cancelButtonTitle:nil
                                               destructiveButtonTitle:nil
                                                    otherButtonTitles:@"请选择", nil];
    [actionsheet showInView:self.view];
    
    UIPickerView *pickerView = [[UIPickerView alloc] init];
    pickerView.tag = 101;
    pickerView.delegate = self;
    pickerView.dataSource = self;
    pickerView.showsSelectionIndicator = YES;
    [actionsheet addSubview:pickerView];
    
    // Pick a random item in the middle of the table
    [pickerView selectRow:50000 + (random() % 4) inComponent:0 animated:YES];
    [pickerView selectRow:50000 + (random() % 4) inComponent:1 animated:YES];
    [pickerView selectRow:50000 + (random() % 4) inComponent:2 animated:YES];
    
    CFShow((__bridge CFTypeRef)(NSStringFromCGRect(pickerView.frame)));


}

@end
```

ViewBasedPickerViewController.h

```objectivec
//
//  ViewBasedPickerViewController.h
//  View based Picker
//
//  Created by david on 13-8-16.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>

#define COOKBOOK_PURPLE_COLOR [UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]
#define BARBUTTON(TITLE, SELECTOR) [[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]



@interface ViewBasedPickerViewController : UIViewController<UIPickerViewDelegate, UIPickerViewDataSource, UIActionSheetDelegate>


@end
```

此例子中使用的是storyboard
