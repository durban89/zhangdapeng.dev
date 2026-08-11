---
title: "UIButton 文字显示位置设置 字体的大小设置 字体的颜色设置 注意事项"
date: "2025-06-13 14:46:09"
slug: "uibutton-wen-zi-xian-shi-wei-zhi-she-zhi-zi-ti-de-da-xiao-she-zhi-zi-ti-de-yan-se-she-zhi-zhu-yi-shi-xiang"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/13/UIButton-文字显示位置设置-字体的大小设置-字体的颜色设置-注意事项/"
  - "/2025/06/13/UIButton-文字显示位置设置-字体的大小设置-字体的颜色设置-注意事项.html"
  - "/UIButton-文字显示位置设置-字体的大小设置-字体的颜色设置-注意事项/"
  - "/UIButton-文字显示位置设置-字体的大小设置-字体的颜色设置-注意事项.html"
  - "/2025/06/13/uibutton-wen-zi-xian-shi-wei-zhi-she-zhi-zi-ti-de-da-xiao-she-zhi-zi-ti-de-yan-se-she-z/"
  - "/2025/06/13/uibutton-wen-zi-xian-shi-wei-zhi-she-zhi-zi-ti-de-da-xiao-she-zhi-zi-ti-de-yan-se-s.html"
  - "/uibutton-wen-zi-xian-shi-wei-zhi-she-zhi-zi-ti-de-da-xiao-she-zhi-zi-ti-de-yan-se-she-zhi-zhu-.html"
---
```objectivec
btn.frame = CGRectMake(x, y, width, height);
[btn setTitle: @"search" forState: UIControlStateNormal];
//设置按钮上的自体的大小
//[btn setFont: [UIFont systemFontSize: 14.0]];    //这种可以用来设置字体的大小，但是可能会在将来的SDK版本中去除改方法
//应该使用
btn.titleLabel.font = [UIFont systemFontOfSize: 14.0];
[btn seBackgroundColor: [UIColor blueColor]];
//最后将按钮加入到指定视图superView
[superView addSubview: btn];
```

---

```objectivec
tvnamelabel=[[UIButton alloc]initWithFrame:CGRectMake(5,5,200,40)];
```

这样初始化的button，文字默认颜色是白色的，所有如果背景也是白色的话，是看不到文字的，

```objectivec
btn.contentHorizontalAlignment=UIControlContentHorizontalAlignmentLeft ;//设置文字位置，现设为居左，默认的是居中
[btn setTitle:@“title”forState:UIControlStateNormal];// 添加文字
```

有些时候我们想让UIButton的title居左对齐，我们设置

```objectivec
btn.textLabel.textAlignment = UITextAlignmentLeft
```

是没有作用的，我们需要设置

```objectivec
btn.contentHorizontalAlignment = UIControlContentHorizonAlignmentLeft;
```

但是问题又出来，此时文字会紧贴到做边框，我们可以设置

```objectivec
btn.contentEdgeInsets = UIEdgeInsetsMake(0,10, 0, 0);
```

使文字距离做边框保持10个像素的距离。

---

设置UIButton上字体的颜色设置UIButton上字体的颜色，不是用：

```objectivec
[btn.titleLabel setTextColor:[UIColorblackColor]];
btn.titleLabel.textColor=[UIColor redColor];
```

而是用：

```objectivec
[btn setTitleColor:[UIColor blackColor]forState:UIControlStateNormal];
```

资源参考：http://blog.csdn.net/chengyingzhilian/article/details/8363855
