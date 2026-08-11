---
title: "iOS UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法"
date: "2025-06-13 11:34:40"
slug: "ios-uiview-xia-mian-you-uitextfield-jian-pan-dan-chu-ying-xiang-shu-ru-textfield-de-nei-rong-jie-jue-ban-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法/"
  - "/2025/06/13/iOS-UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法.html"
  - "/iOS-UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法/"
  - "/iOS-UIView下面有UITextField,键盘弹出影响输入TextField的内容，解决办法.html"
  - "/2025/06/13/iOS-UIView下面有UITextField-键盘弹出影响输入TextField的内容-解决办法/"
  - "/2025/06/13/iOS-UIView下面有UITextField-键盘弹出影响输入TextField的内容-解决办法.html"
  - "/2025/06/13/ios-uiview-xia-mian-you-uitextfield-jian-pan-dan-chu-ying-xiang-shu-ru-textfield-de-nei/"
  - "/2025/06/13/ios-uiview-xia-mian-you-uitextfield-jian-pan-dan-chu-ying-xiang-shu-ru-textfield-de.html"
  - "/ios-uiview-xia-mian-you-uitextfield-jian-pan-dan-chu-ying-xiang-shu-ru-textfield-de-nei-rong-j.html"
---
在viewdidload的时候，把每个TextField设好tag。之后就可以根据最下面的UITextField的内容来判断键盘的弹出和关闭了

实例代码：

```objectivec
- (void)textFieldDidBeginEditing:(UITextField *)textField 

{ //当点触textField内部，开始编辑都会调用这个方法。textField将成为first responder  

    if (textField.tag == 2) {

        NSTimeInterval animationDuration = 0.30f;     

        CGRect frame = self.view.frame; 

        frame.origin.y -=216; 

        frame.size.height +=216; 

        self.view.frame = frame; 

        [UIView beginAnimations:@"ResizeView"context:nil]; 

        [UIView setAnimationDuration:animationDuration]; 

        self.view.frame = frame;                 

        [UIView commitAnimations];

    }
} 

 

- (BOOL)textFieldShouldReturn:(UITextField *)textField  

{//当用户按下ruturn，把焦点从textField移开那么键盘就会消失了 

//    textField

    if (textField.tag == 2) {

        NSTimeInterval animationDuration = 0.30f; 

        CGRect frame = self.view.frame;     

        frame.origin.y +=216;       

        frame.size. height -=216;    

        self.view.frame = frame; 

        //self.view移回原位置   

        [UIView beginAnimations:@"ResizeView"context:nil]; 

        [UIView setAnimationDuration:animationDuration]; 

        self.view.frame = frame; 

        [UIView commitAnimations];

    }

    [textField resignFirstResponder];    

    returnYES;
}
```
