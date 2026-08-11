---
title: "点击UITextField 跳出UIDatePicker以选取日期(生日,NSDate)"
date: "2025-06-26 14:55:02"
slug: "dian-ji-uitextfield-tiao-chu-uidatepicker-yi-xuan-qu-ri-qi-sheng-ri-nsdate"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/点击UITextField-跳出UIDatePicker以选取日期(生日,NSDate)/"
  - "/2025/06/26/点击UITextField-跳出UIDatePicker以选取日期(生日,NSDate).html"
  - "/点击UITextField-跳出UIDatePicker以选取日期(生日,NSDate)/"
  - "/点击UITextField-跳出UIDatePicker以选取日期(生日,NSDate).html"
  - "/2025/06/26/点击UITextField-跳出UIDatePicker以选取日期-生日-NSDate/"
  - "/2025/06/26/点击UITextField-跳出UIDatePicker以选取日期-生日-NSDate.html"
  - "/2025/06/26/dian-ji-uitextfield-tiao-chu-uidatepicker-yi-xuan-qu-ri-qi-sheng-ri-nsdate/"
  - "/2025/06/26/dian-ji-uitextfield-tiao-chu-uidatepicker-yi-xuan-qu-ri-qi-sheng-ri-nsdate.html"
  - "/dian-ji-uitextfield-tiao-chu-uidatepicker-yi-xuan-qu-ri-qi-sheng-ri-nsdate.html"
---
首先添加一个UITextField。

```objectivec
_brithdayTextField = [[UITextField alloc] initWithFrame:CGRectMake(birthdayLabelX + birthdayLabelWidth + 10.0,
                                                                      birthdayLabelY,
                                                                      textFieldWidth,
                                                                      textFieldHeight)];
_brithdayTextField.text = [NSString stringWithFormat:@"%@",[_userinfo valueForKey:@"birthday"]];
_brithdayTextField.textAlignment = NSTextAlignmentLeft;
_brithdayTextField.backgroundColor = textFieldDebugColor;
_brithdayTextField.delegate = self;
_brithdayTextField.tag = 10008;
_brithdayTextField.returnKeyType = UIReturnKeyNext;
[_scrollView addSubview:_brithdayTextField];
```

其次，实现UITextFieldDelegate的代理方法，在`-(void) textFieldDidBeginEditing:(UITextField *)textField`方法中实现

```objectivec
if ([_brithdayTextField isFirstResponder])
{
    // 建立 UIDatePicker
    _datePicker = [[UIDatePicker alloc]init];
    _datelocale = [[NSLocale alloc] initWithLocaleIdentifier:@"zh_CN"];
    _datePicker.locale = _datelocale;
    _datePicker.timeZone = [NSTimeZone timeZoneWithName:@"GMT"];
    _datePicker.datePickerMode = UIDatePickerModeDate;
    _brithdayTextField.inputView = _datePicker;
    
    // 建立 UIToolbar
    UIToolbar *toolBar = [[UIToolbar alloc]initWithFrame:CGRectMake(0, 0, 320, 44)];
    UIBarButtonItem *right = [[UIBarButtonItem alloc]initWithBarButtonSystemItem:UIBarButtonSystemItemDone
                                                                          target:self
                                                                          action:@selector(cancelPicker)];
    UIBarButtonItem *space = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemFixedSpace
                                                                           target:nil
                                                                           action:nil];
    toolBar.items = [NSArray arrayWithObjects:space,right,nil];
    _brithdayTextField.inputAccessoryView = toolBar;
}
```

最后在完成选取的时候，进行下面的操作

```objectivec
-(void) cancelPicker {
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    [formatter setDateFormat:@"yyyy-MM-dd"];
    _brithdayTextField.text = [NSString stringWithFormat:@"%@",[formatter stringFromDate:_datePicker.date]];
    CGRect frame =  _scrollView.frame;
    frame.size.height = [[UIScreen mainScreen] bounds].size.height;
    frame.origin.y = 0.0;
    _scrollView.frame=frame;
    [_brithdayTextField resignFirstResponder];
}
```

---

参考文章

http://blog.hsin.tw/2013/ios-dev-tap-uitextfield-popup-uidatepicker-to-pick-date/

