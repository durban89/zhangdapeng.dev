---
title: "iOS7 UITextView 退出键盘的方式"
date: "2025-06-26 11:45:03"
slug: "ios7-uitextview-tui-chu-jian-pan-de-fang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-UITextView-退出键盘的方式/"
  - "/2025/06/26/iOS7-UITextView-退出键盘的方式.html"
  - "/iOS7-UITextView-退出键盘的方式/"
  - "/iOS7-UITextView-退出键盘的方式.html"
  - "/2025/06/26/ios7-uitextview-tui-chu-jian-pan-de-fang-shi/"
  - "/2025/06/26/ios7-uitextview-tui-chu-jian-pan-de-fang-shi.html"
  - "/ios7-uitextview-tui-chu-jian-pan-de-fang-shi.html"
---
关于UITextView 退出键盘的方式，google后找到了几个比较好的方法。

第一种方法：程序是有导航条的，可以在导航条上面加多一个Done的按钮，用来退出键盘，当然要先实UITextViewDelegate。代码如下：

```objectivec
- (void)textViewDidBeginEditing:(UITextView *)textView {
   UIBarButtonItem *done =    [[[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemDone target:self action:@selector(leaveEditMode)] autorelease];
   self.navigationItem.rightBarButtonItem = done;    
}

- (void)textViewDidEndEditing:(UITextView *)textView {
    self.navigationItem.rightBarButtonItem = nil;
}

- (void)leaveEditMode {
    [self.textView resignFirstResponder];
}
```

第二种方法：如果UITextview里不用回车键，可以把回车键当做退出键盘的响应键。代码如下：

```objectivec
#pragma mark - UITextView Delegate Methods
-(BOOL)textView:(UITextView *)textView shouldChangeTextInRange:(NSRange)range replacementText:(NSString *)text
{
    if ([text isEqualToString:@"\n"]) {
        [textView resignFirstResponder];
        return NO;
    }
    return YES;
}
```

第三种方法：在弹出的键盘上面加一个view来放置退出键盘的Done按钮。代码如下：

```objectivec
CGFloat profileX = x + hInterval;
CGFloat profileY = y + areaLabel.frame.size.height + areaLabel.frame.origin.y + 10.0;
CGFloat profileWidth = width - 2 * hInterval;
CGFloat profileHeight = 200.0;
UITextView *profile = [[UITextView alloc] initWithFrame:CGRectMake(profileX,
                                                                   profileY,
                                                                   profileWidth,
                                                                   profileHeight)];

profile.text = @"请输入简介信息";
[profile.layer setBorderColor:[[UIColor lightGrayColor] CGColor]];
[profile.layer setBorderWidth:1.0];
[profile.layer setCornerRadius:1.0];
profile.editable = YES;
profile.delegate = self;
[_scrollView addSubview:profile];


UIToolbar * topView = [[UIToolbar alloc]initWithFrame:CGRectMake(0.0, 0.0, 320.0, 30.0)];
[topView setBarStyle:UIBarStyleDefault];

UIBarButtonItem * btnSpace = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemFlexibleSpace
                                                                           target:self
                                                                           action:nil];

UIBarButtonItem * completeButton = [[UIBarButtonItem alloc] initWithTitle:@"完成"
                                                                    style:UIBarButtonItemStyleDone
                                                                   target:self
                                                                   action:@selector(dismissKeyBoard)];

NSArray * buttonsArray = [NSArray arrayWithObjects:btnSpace,completeButton,nil];

[topView setItems:buttonsArray];
[profile setInputAccessoryView:topView];
```

隐藏键盘的方法：

```objectivec
-(void)dismissKeyBoard
{
    [[UIApplication sharedApplication] sendAction:@selector(resignFirstResponder)
                                               to:nil
                                             from:nil
                                         forEvent:nil];
}
```

可以试试吧。

---

参考文章：

http://blog.csdn.net/kylinbl/article/details/6694897

