---
title: "iOS UILabel(label控件)的详细使用及特殊效果"
date: "2025-06-11 10:52:15"
slug: "ios-uilabellabel-kong-jian-de-xiang-xi-shi-yong-ji-te-shu-xiao-guo"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-UILabel(label控件)的详细使用及特殊效果/"
  - "/2025/06/11/iOS-UILabel(label控件)的详细使用及特殊效果.html"
  - "/iOS-UILabel(label控件)的详细使用及特殊效果/"
  - "/iOS-UILabel(label控件)的详细使用及特殊效果.html"
  - "/2025/06/11/iOS-UILabel-label控件-的详细使用及特殊效果/"
  - "/2025/06/11/iOS-UILabel-label控件-的详细使用及特殊效果.html"
  - "/2025/06/11/ios-uilabellabel-kong-jian-de-xiang-xi-shi-yong-ji-te-shu-xiao-guo/"
  - "/2025/06/11/ios-uilabellabel-kong-jian-de-xiang-xi-shi-yong-ji-te-shu-xiao-guo.html"
  - "/ios-uilabellabel-kong-jian-de-xiang-xi-shi-yong-ji-te-shu-xiao-guo.html"
---
详细使用：

```objectivec
UILabel *label = [[UILabelalloc] initWithFrame:CGRectMake(0, 0, 75, 40)];   //声明UIlbel并指定其位置和长宽
label.backgroundColor = [UIColorclearColor];   //设置label的背景色，这里设置为透明色。
label.font = [UIFont fontWithName:@"Helvetica-Bold" size:13];   //设置label的字体和字体大小。 
label.transform = CGAffineTransformMakeRotation(0.1);     //设置label的旋转角度
label.text = @“helloworld”;   //设置label所显示的文本
label.textColor = [UIColorwhiteColor];    //设置文本的颜色
label.shadowColor = [UIColorcolorWithWhite:0.1falpha:0.8f];    //设置文本的阴影色彩和透明度。
label.shadowOffset = CGSizeMake(2.0f, 2.0f);     //设置阴影的倾斜角度。
label.textAlignment = UITextAlignmentCenter;     //设置文本在label中显示的位置，这里为居中。
//换行技巧：如下换行可实现多行显示，但要求label有足够的宽度。
label.lineBreakMode = UILineBreakModeWordWrap;     //指定换行模式
label.numberOfLines = 2;    // 指定label的行数
//lable的旋转
label.transform = CGAffineTransformMakeRotation(0.2);     //设置label的旋转角度
[self.view addSubview:label];    //将label载入
```

label的美化和特效：

这里使用FXLabel来实现特殊效果，如上图的“每日”二字就是用FXLabel来实现的，但要加入FXLbal.h和FXLabel.m两个文件，具体代码如下。

```objectivec
FXLabel *label = [[FXLabelalloc] initWithFrame:CGRectMake(0, 0, 100, 30)];
label.backgroundColor = [UIColorclearColor];
label.font = [UIFontfontWithName:@"Helvetica-Bold"size:15];
label.text = [secondTitle objectAtIndex:i];
label.textColor = [UIColorgrayColor];
label.shadowColor = [UIColorcolorWithWhite:1.0falpha:0.8f];
label.shadowOffset = CGSizeMake(1.0f, 2.0f);
label.shadowBlur = 1.0f;
label.innerShadowColor = [UIColorcolorWithWhite:0.0falpha:0.8f]; 
label.innerShadowOffset = CGSizeMake(1.0f, 2.0f);  
label.textAlignment = UITextAlignmentLeft;
[view addSubview:label];
```

其用法和UILabel相差不大，很好理解，代码大家可以直接调用，具体属性自己修改。

FXLabel下面地址：https://github.com/nicklockwood/FXLabel

来源：http://wuchaorang.2008.blog.163.com/blog/static/48891852201232014339972/
