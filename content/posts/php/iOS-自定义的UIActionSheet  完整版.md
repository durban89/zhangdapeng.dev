---
title: "iOS 自定义的UIActionSheet  完整版"
date: "2025-06-13 11:34:52"
slug: "ios-zi-ding-yi-de-uiactionsheet-wan-zheng-ban"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-自定义的UIActionSheet-完整版/"
  - "/2025/06/13/iOS-自定义的UIActionSheet-完整版.html"
  - "/iOS-自定义的UIActionSheet-完整版/"
  - "/iOS-自定义的UIActionSheet-完整版.html"
  - "/2025/06/13/ios-zi-ding-yi-de-uiactionsheet-wan-zheng-ban/"
  - "/2025/06/13/ios-zi-ding-yi-de-uiactionsheet-wan-zheng-ban.html"
  - "/ios-zi-ding-yi-de-uiactionsheet-wan-zheng-ban.html"
---
自定义的UIActionSheet ，网上找了好久，都没有完整的解决办法，于是自己 经过查找资料，然后根据自己的项目需要做了一些改动，得到了一个完整版的，自定义的UIActionSheet,代码如下：

```objectivec
-(void) setUpDatePicker
{
    //点击显示时间
    self.actionSheet = [[UIActionSheet alloc] initWithTitle:nil
                                                   delegate:self
                                          cancelButtonTitle:nil
                                     destructiveButtonTitle:nil
                                          otherButtonTitles:nil];
    
    UISegmentedControl *cancelButton = [[UISegmentedControl alloc] initWithItems:[NSArray arrayWithObject:@"取消"]];
    UISegmentedControl *confirmButton =[[UISegmentedControl alloc] initWithItems:[NSArray arrayWithObject:@"确定"]];
    [self.actionSheet setActionSheetStyle:UIActionSheetStyleBlackTranslucent];
    // Add the picker
    self.datePicker = [[UIDatePicker alloc] init];
    self.datePicker.datePickerMode = UIDatePickerModeDate;
    [self.datePicker addTarget:self
                        action:@selector(dateChanged:)
              forControlEvents:UIControlEventValueChanged];
    [self.actionSheet addSubview:self.datePicker];
    [self.actionSheet showInView:self.view];
    [self.actionSheet setBounds:CGRectMake(0,0,320, 500)];
    
    CGRect pickerRect;
    pickerRect = self.datePicker.bounds;
    pickerRect.origin.y = -50;
    self.datePicker.bounds = pickerRect;
    cancelButton.momentary = YES;
    cancelButton.frame = CGRectMake(10.0f, 7.0f, 65.0f, 32.0f);
    cancelButton.segmentedControlStyle = UISegmentedControlStyleBar;
    [cancelButton addTarget:self action:@selector(DatePickerDoneClick:) forControlEvents:UIControlEventValueChanged];
    [self.actionSheet addSubview:cancelButton];

    cancelButton.tag = 1;
    confirmButton.momentary = YES;
    confirmButton.frame = CGRectMake(245.0f, 7.0f, 65.0f, 32.0f);
    confirmButton.segmentedControlStyle = UISegmentedControlStyleBar;
    [confirmButton addTarget:self action:@selector(DatePickerDoneClick:) forControlEvents:UIControlEventValueChanged];
    [self.actionSheet addSubview:confirmButton];

    confirmButton.tag = 2;
    [self.actionSheet showInView:self.view];
    [self.actionSheet setBounds:CGRectMake(0,0, 320, 500)];
    
}

-(void) DatePickerDoneClick:(id) sender
{
    UIButton *button = (UIButton *)sender;
    if(button.tag == 1)
    {
        [self.actionSheet dismissWithClickedButtonIndex:0 animated:YES];
    }
    
    if(button.tag == 2)
    {
        [self.actionSheet dismissWithClickedButtonIndex:0 animated:YES];
    }
}

-(void) dateChanged:(id)sender
{
    NSDate *dateValue = [NSDate date];
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd"];
    dateValue = ((UIDatePicker *)sender).date;
    
    self.teleplayDate.text = [dateFormatter stringFromDate:dateValue];//[NSString stringWithFormat:@"%@",dateValue];
}
```

这里简单的解释一下：

- -(void) setUpDatePicker方法用于调用UIDatePicker

- -(void) DatePickerDoneClick:(id) sender方法用于实现隐藏UIdatePicker

- -(void) dateChanged:(id)sender方法实现获取日期结果值的方法。

如果没有实现效果，别忘记加上协议，这个是比较容易忘记的
