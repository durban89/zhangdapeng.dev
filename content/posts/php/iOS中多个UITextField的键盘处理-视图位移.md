---
title: "iOS中多个UITextField的键盘处理-视图位移"
date: "2025-06-26 14:55:07"
slug: "ios-zhong-duo-ge-uitextfield-de-jian-pan-chu-li-shi-tu-wei-yi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS中多个UITextField的键盘处理-视图位移/"
  - "/2025/06/26/iOS中多个UITextField的键盘处理-视图位移.html"
  - "/iOS中多个UITextField的键盘处理-视图位移/"
  - "/iOS中多个UITextField的键盘处理-视图位移.html"
  - "/2025/06/26/ios-zhong-duo-ge-uitextfield-de-jian-pan-chu-li-shi-tu-wei-yi/"
  - "/2025/06/26/ios-zhong-duo-ge-uitextfield-de-jian-pan-chu-li-shi-tu-wei-yi.html"
  - "/ios-zhong-duo-ge-uitextfield-de-jian-pan-chu-li-shi-tu-wei-yi.html"
---
当有多个UITextField的时候，一个比较好的处理方式就是实现视图移位，实现的方法也很简单。

首先是加入UITextField的代理UITextFieldDelegate。

其次，在代理的`-(void) textFieldDidBeginEditing:(UITextField *)textField`方法中实现

```objectivec
CGFloat keyboardHeight = 216.0;
if ((textField.frame.origin.y + keyboardHeight + textField.frame.size.height) >= ([[UIScreen mainScreen] bounds].size.height - 100.0))
{
    //此时，编辑框被键盘盖住，则对视图做对应的位移
    CGRect frame =  CGRectMake(0.0, 0.0, 320, [[UIScreen mainScreen] bounds].size.height + 120.0);
    frame.origin.y -= textField.frame.origin.y + keyboardHeight + textField.frame.size.height - [[UIScreen mainScreen] bounds].size.height + 120.0;//偏移量=编辑框原点Y值+键盘高度+编辑框高度-屏幕高度
    _scrollView.frame=frame;
}
```

这里面的具体位置可以自己调整，算法也是不唯一的

当到达最后一个UITextField的时候，要隐藏键盘，这里如何做呢，如下所示：

在代理

`- (BOOL)textFieldShouldReturn:(UITextField *)textField`

方法中

最后一个失去焦点的时候

```objectivec
[_bloodTextField resignFirstResponder];
CGRect frame =  _scrollView.frame;
frame.size.height = [[UIScreen mainScreen] bounds].size.height;
frame.origin.y = 0.0;
_scrollView.frame=frame;
return YES;
```

判断的话我使用这样子实现的

```objectivec
if ([_bloodTextField isFirstResponder])
```

是不是很简单

