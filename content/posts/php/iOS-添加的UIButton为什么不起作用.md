---
title: "iOS 添加的UIButton为什么不起作用"
date: "2025-06-19 09:58:30"
slug: "ios-tian-jia-de-uibutton-wei-shen-me-bu-qi-zuo-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS-添加的UIButton为什么不起作用/"
  - "/2025/06/19/iOS-添加的UIButton为什么不起作用.html"
  - "/iOS-添加的UIButton为什么不起作用/"
  - "/iOS-添加的UIButton为什么不起作用.html"
  - "/2025/06/19/ios-tian-jia-de-uibutton-wei-shen-me-bu-qi-zuo-yong/"
  - "/2025/06/19/ios-tian-jia-de-uibutton-wei-shen-me-bu-qi-zuo-yong.html"
  - "/ios-tian-jia-de-uibutton-wei-shen-me-bu-qi-zuo-yong.html"
---
先看两个例子：

第一个例子，代码如下：

```objectivec
-(void) setPersonInfo:(CGFloat)x y:(CGFloat)y heihgt:(CGFloat)height{
    CGFloat width = self.view.frame.size.width - 2 * x;
    UILabel *labelInfoArea = [[UILabel alloc]initWithFrame:CGRectMake(x, y+10.0, width, height)];
    labelInfoArea.backgroundColor = [UIColor clearColor];
    [_contentScroll addSubview:labelInfoArea];
    
    //基本信息的标题
    UILabel *labelInfoCaption = [[UILabel alloc] initWithFrame:CGRectMake(0.0, 0.0, labelInfoArea.frame.size.width * 0.5, 30.0)];
    labelInfoCaption.textColor = [UIColor blackColor];
    labelInfoCaption.text = @"基本信息";
    labelInfoCaption.font = [UIFont systemFontOfSize:16.0];
    labelInfoCaption.backgroundColor = [UIColor clearColor];
    [labelInfoArea addSubview:labelInfoCaption];
    
    //complete button
    if([[NSString stringWithFormat:@"%@",[_personInfo valueForKey:@"is_completed"]] isEqualToString:@"0"]){
        UIButton *completeBtn = [UIButton buttonWithType:UIButtonTypeCustom];
        completeBtn.layer.borderColor = [[UIColor colorWithRed:161.0/255.0 green:159.0/255.0 blue:160.0/255.0 alpha:1.0] CGColor];
        completeBtn.layer.borderWidth = 1.0;
        completeBtn.layer.cornerRadius = 5.0;
        completeBtn.layer.backgroundColor = [[UIColor colorWithRed:161.0/255.0 green:159.0/255.0 blue:160.0/255.0 alpha:1.0] CGColor];
        [completeBtn setTitle:@"我来完善" forState:UIControlStateNormal];
        completeBtn.titleLabel.font = [UIFont systemFontOfSize:12.0];
        [completeBtn addTarget:self
                        action:@selector(redirectCompleteDetail)
              forControlEvents:UIControlEventTouchUpInside];
        [completeBtn setFrame:CGRectMake(self.view.frame.size.width - 80.0, y + 15.0, 60.0, 20.0)];
        [_contentScroll addSubview:completeBtn];
    }
    
    //基本信息表格
    UILabel *labelInfoTable = [[UILabel alloc] initWithFrame:CGRectMake(labelInfoCaption.frame.origin.x, labelInfoCaption.frame.origin.x + labelInfoCaption.frame.size.height, labelInfoArea.frame.size.width, height - 30.0)];
    labelInfoTable.backgroundColor = [UIColor lightGrayColor];
    labelInfoTable.layer.borderColor = [[UIColor lightGrayColor] CGColor];
    labelInfoTable.layer.borderWidth = 1.0;
    labelInfoTable.layer.cornerRadius = 10.0;
    [labelInfoArea addSubview:labelInfoTable];
    
    CGFloat tableCellHeight = labelInfoTable.frame.size.height / 2;
    CGFloat tableCellWidth = labelInfoTable.frame.size.width / 4;
    
    //添加基本信息-年龄
    UILabel *labelAge = [[UILabel alloc] initWithFrame:CGRectMake(0.0, 0.0, tableCellWidth, tableCellHeight)];
    labelAge.backgroundColor = [UIColor whiteColor];
    labelAge.text = @"年龄";
    labelAge.font = [UIFont systemFontOfSize:14];
    labelAge.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelAge];
    
    //添加基本信息-身高
    UILabel *labelHeight = [[UILabel alloc] initWithFrame:CGRectMake(labelAge.frame.origin.x + labelAge.frame.size.width, 0.0, labelAge.frame.size.width, labelAge.frame.size.height)];
    labelHeight.backgroundColor = [UIColor whiteColor];
    labelHeight.text = @"身高";
    labelHeight.font = [UIFont systemFontOfSize:14];
    labelHeight.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelHeight];
    
    //添加基本信息-体重
    UILabel *labelWeight = [[UILabel alloc] initWithFrame:CGRectMake(labelHeight.frame.origin.x + labelHeight.frame.size.width, 0.0, labelHeight.frame.size.width, labelHeight.frame.size.height)];
    labelWeight.backgroundColor = [UIColor whiteColor];
    labelWeight.text = @"体重";
    labelWeight.font = [UIFont systemFontOfSize:14];
    labelWeight.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelWeight];
    
    //添加基本信息-性别
    UILabel *labelBMI = [[UILabel alloc] initWithFrame:CGRectMake(labelWeight.frame.origin.x + labelWeight.frame.size.width, 0.0, labelHeight.frame.size.width, labelHeight.frame.size.height)];
    labelBMI.backgroundColor = [UIColor whiteColor];
    labelBMI.text = @"性别";
    labelBMI.font = [UIFont systemFontOfSize:14];
    labelBMI.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelBMI];
    
    
    //+++++++++++++++++++
    //添加基本信息-年龄值
    UILabel *labelAgeValue = [[UILabel alloc] initWithFrame:CGRectMake(0.0, labelInfoTable.frame.size.height / 2, labelInfoTable.frame.size.width / 4, labelInfoTable.frame.size.height / 2)];
    labelAgeValue.backgroundColor = [UIColor whiteColor];
    labelAgeValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"age"]] isEqualToString:@"0"])
    {
        labelAgeValue.text = @"无";
    }
    else
    {
        labelAgeValue.text = [NSString stringWithFormat:@"%@岁",[self.personInfo valueForKey:@"age"]];
    }
    
    labelAgeValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelAgeValue];
    
    //添加基本信息-身高值
    UILabel *labelHeightValue = [[UILabel alloc] initWithFrame:CGRectMake(labelAgeValue.frame.origin.x + labelAgeValue.frame.size.width, labelAgeValue.frame.origin.y, labelAgeValue.frame.size.width, labelAgeValue.frame.size.height)];
    labelHeightValue.backgroundColor = [UIColor whiteColor];
    labelHeightValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"height"]] isEqualToString:@"0"])
    {
        labelHeightValue.text = @"无";
    }
    else
    {
        labelHeightValue.text = [NSString stringWithFormat:@"%@CM",[self.personInfo valueForKey:@"height"]];
    }
    
    labelHeightValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelHeightValue];
    
    //添加基本信息-体重值
    UILabel *labelWeightValue = [[UILabel alloc] initWithFrame:CGRectMake(labelHeightValue.frame.origin.x + labelHeightValue.frame.size.width, labelHeightValue.frame.origin.y, labelHeightValue.frame.size.width, labelHeightValue.frame.size.height)];
    labelWeightValue.backgroundColor = [UIColor whiteColor];
    labelWeightValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"weight"]] isEqualToString:@"0"])
    {
        labelWeightValue.text = @"无";
    }
    else
    {
        labelWeightValue.text = [NSString stringWithFormat:@"%@KG",[self.personInfo valueForKey:@"weight"]];
    }
    
    
    labelWeightValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelWeightValue];
    
    //添加基本信息-性别
    UILabel *labelBMIValue = [[UILabel alloc] initWithFrame:CGRectMake(labelWeightValue.frame.origin.x + labelWeightValue.frame.size.width, labelWeightValue.frame.origin.y, labelWeightValue.frame.size.width, labelWeightValue.frame.size.height)];
    labelBMIValue.backgroundColor = [UIColor whiteColor];
    labelBMIValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"sex"]] isEqualToString:@"0"])
    {
        labelBMIValue.text = @"无";
    }
    else
    {
        labelBMIValue.text = [NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"sex"]];
    }
//    
//    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"bmi"]] isEqualToString:@"0"])
//    {
//        labelBMIValue.text = @"无";
//    }
//    else
//    {
//        labelBMIValue.text = [NSString stringWithFormat:@"%@KG",[self.personInfo valueForKey:@"bmi"]];
//    }
    
    labelBMIValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelBMIValue];
    //++++++++++++++++
    
    //横轴分割线-第一根
    UILabel *vfirstLine = [[UILabel alloc] initWithFrame:CGRectMake(0.0,  tableCellHeight + labelAge.frame.origin.y, labelInfoTable.frame.size.width, 1.0)];
    vfirstLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:vfirstLine];
    
    //竖轴分割线-第一根
    UILabel *firstLine = [[UILabel alloc] initWithFrame:CGRectMake(labelAge.frame.origin.x + labelAge.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    firstLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:firstLine];
    
    //竖轴分割线-第二根
    UILabel *secondLine = [[UILabel alloc] initWithFrame:CGRectMake(labelHeight.frame.origin.x + labelHeight.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    secondLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:secondLine];
    
    //竖轴分割线-第三根
    UILabel *thridLine = [[UILabel alloc] initWithFrame:CGRectMake(labelWeight.frame.origin.x + labelWeight.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    thridLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:thridLine];
}
```

第二个例子，代码如下：

```objectivec
-(void) setPersonInfo:(CGFloat)x y:(CGFloat)y heihgt:(CGFloat)height{
    CGFloat width = self.view.frame.size.width - 2 * x;
    UILabel *labelInfoArea = [[UILabel alloc]initWithFrame:CGRectMake(x, y+10.0, width, height)];
    labelInfoArea.backgroundColor = [UIColor clearColor];
    [_contentScroll addSubview:labelInfoArea];
    
    //基本信息的标题
    UILabel *labelInfoCaption = [[UILabel alloc] initWithFrame:CGRectMake(0.0, 0.0, labelInfoArea.frame.size.width * 0.5, 30.0)];
    labelInfoCaption.textColor = [UIColor blackColor];
    labelInfoCaption.text = @"基本信息";
    labelInfoCaption.font = [UIFont systemFontOfSize:16.0];
    labelInfoCaption.backgroundColor = [UIColor clearColor];
    [labelInfoArea addSubview:labelInfoCaption];

    //基本信息表格
    UILabel *labelInfoTable = [[UILabel alloc] initWithFrame:CGRectMake(labelInfoCaption.frame.origin.x, labelInfoCaption.frame.origin.x + labelInfoCaption.frame.size.height, labelInfoArea.frame.size.width, height - 30.0)];
    labelInfoTable.backgroundColor = [UIColor lightGrayColor];
    labelInfoTable.layer.borderColor = [[UIColor lightGrayColor] CGColor];
    labelInfoTable.layer.borderWidth = 1.0;
    labelInfoTable.layer.cornerRadius = 10.0;
    [labelInfoArea addSubview:labelInfoTable];
    
    CGFloat tableCellHeight = labelInfoTable.frame.size.height / 2;
    CGFloat tableCellWidth = labelInfoTable.frame.size.width / 4;
    
    //添加基本信息-年龄
    UILabel *labelAge = [[UILabel alloc] initWithFrame:CGRectMake(0.0, 0.0, tableCellWidth, tableCellHeight)];
    labelAge.backgroundColor = [UIColor whiteColor];
    labelAge.text = @"年龄";
    labelAge.font = [UIFont systemFontOfSize:14];
    labelAge.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelAge];
    
    //添加基本信息-身高
    UILabel *labelHeight = [[UILabel alloc] initWithFrame:CGRectMake(labelAge.frame.origin.x + labelAge.frame.size.width, 0.0, labelAge.frame.size.width, labelAge.frame.size.height)];
    labelHeight.backgroundColor = [UIColor whiteColor];
    labelHeight.text = @"身高";
    labelHeight.font = [UIFont systemFontOfSize:14];
    labelHeight.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelHeight];
    
    //添加基本信息-体重
    UILabel *labelWeight = [[UILabel alloc] initWithFrame:CGRectMake(labelHeight.frame.origin.x + labelHeight.frame.size.width, 0.0, labelHeight.frame.size.width, labelHeight.frame.size.height)];
    labelWeight.backgroundColor = [UIColor whiteColor];
    labelWeight.text = @"体重";
    labelWeight.font = [UIFont systemFontOfSize:14];
    labelWeight.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelWeight];
    
    //添加基本信息-性别
    UILabel *labelBMI = [[UILabel alloc] initWithFrame:CGRectMake(labelWeight.frame.origin.x + labelWeight.frame.size.width, 0.0, labelHeight.frame.size.width, labelHeight.frame.size.height)];
    labelBMI.backgroundColor = [UIColor whiteColor];
    labelBMI.text = @"性别";
    labelBMI.font = [UIFont systemFontOfSize:14];
    labelBMI.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelBMI];
    
    
    //+++++++++++++++++++
    //添加基本信息-年龄值
    UILabel *labelAgeValue = [[UILabel alloc] initWithFrame:CGRectMake(0.0, labelInfoTable.frame.size.height / 2, labelInfoTable.frame.size.width / 4, labelInfoTable.frame.size.height / 2)];
    labelAgeValue.backgroundColor = [UIColor whiteColor];
    labelAgeValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"age"]] isEqualToString:@"0"])
    {
        labelAgeValue.text = @"无";
    }
    else
    {
        labelAgeValue.text = [NSString stringWithFormat:@"%@岁",[self.personInfo valueForKey:@"age"]];
    }
    
    labelAgeValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelAgeValue];
    
    //添加基本信息-身高值
    UILabel *labelHeightValue = [[UILabel alloc] initWithFrame:CGRectMake(labelAgeValue.frame.origin.x + labelAgeValue.frame.size.width, labelAgeValue.frame.origin.y, labelAgeValue.frame.size.width, labelAgeValue.frame.size.height)];
    labelHeightValue.backgroundColor = [UIColor whiteColor];
    labelHeightValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"height"]] isEqualToString:@"0"])
    {
        labelHeightValue.text = @"无";
    }
    else
    {
        labelHeightValue.text = [NSString stringWithFormat:@"%@CM",[self.personInfo valueForKey:@"height"]];
    }
    
    labelHeightValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelHeightValue];
    
    //添加基本信息-体重值
    UILabel *labelWeightValue = [[UILabel alloc] initWithFrame:CGRectMake(labelHeightValue.frame.origin.x + labelHeightValue.frame.size.width, labelHeightValue.frame.origin.y, labelHeightValue.frame.size.width, labelHeightValue.frame.size.height)];
    labelWeightValue.backgroundColor = [UIColor whiteColor];
    labelWeightValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"weight"]] isEqualToString:@"0"])
    {
        labelWeightValue.text = @"无";
    }
    else
    {
        labelWeightValue.text = [NSString stringWithFormat:@"%@KG",[self.personInfo valueForKey:@"weight"]];
    }
    
    
    labelWeightValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelWeightValue];
    
    //添加基本信息-性别
    UILabel *labelBMIValue = [[UILabel alloc] initWithFrame:CGRectMake(labelWeightValue.frame.origin.x + labelWeightValue.frame.size.width, labelWeightValue.frame.origin.y, labelWeightValue.frame.size.width, labelWeightValue.frame.size.height)];
    labelBMIValue.backgroundColor = [UIColor whiteColor];
    labelBMIValue.font = [UIFont systemFontOfSize:14];
    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"sex"]] isEqualToString:@"0"])
    {
        labelBMIValue.text = @"无";
    }
    else
    {
        labelBMIValue.text = [NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"sex"]];
    }
//    
//    if([[NSString stringWithFormat:@"%@",[self.personInfo valueForKey:@"bmi"]] isEqualToString:@"0"])
//    {
//        labelBMIValue.text = @"无";
//    }
//    else
//    {
//        labelBMIValue.text = [NSString stringWithFormat:@"%@KG",[self.personInfo valueForKey:@"bmi"]];
//    }
    
    labelBMIValue.textAlignment = NSTextAlignmentCenter;
    [labelInfoTable addSubview:labelBMIValue];
    //++++++++++++++++
    
    //横轴分割线-第一根
    UILabel *vfirstLine = [[UILabel alloc] initWithFrame:CGRectMake(0.0,  tableCellHeight + labelAge.frame.origin.y, labelInfoTable.frame.size.width, 1.0)];
    vfirstLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:vfirstLine];
    
    //竖轴分割线-第一根
    UILabel *firstLine = [[UILabel alloc] initWithFrame:CGRectMake(labelAge.frame.origin.x + labelAge.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    firstLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:firstLine];
    
    //竖轴分割线-第二根
    UILabel *secondLine = [[UILabel alloc] initWithFrame:CGRectMake(labelHeight.frame.origin.x + labelHeight.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    secondLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:secondLine];
    
    //竖轴分割线-第三根
    UILabel *thridLine = [[UILabel alloc] initWithFrame:CGRectMake(labelWeight.frame.origin.x + labelWeight.frame.size.width, 0.0, 1.0, labelInfoTable.frame.size.height)];
    thridLine.backgroundColor = [UIColor lightGrayColor];
    [labelInfoTable addSubview:thridLine];
}


//完善信息的按钮
-(void) setupComplateButton:(CGFloat) y{
    //基本信息的完善按钮
    if([[NSString stringWithFormat:@"%@",[_personInfo valueForKey:@"is_completed"]] isEqualToString:@"0"]){
        UIButton *completeBtn = [UIButton buttonWithType:UIButtonTypeCustom];
        completeBtn.layer.borderColor = [[UIColor colorWithRed:161.0/255.0 green:159.0/255.0 blue:160.0/255.0 alpha:1.0] CGColor];
        completeBtn.layer.borderWidth = 1.0;
        completeBtn.layer.cornerRadius = 5.0;
        completeBtn.layer.backgroundColor = [[UIColor colorWithRed:161.0/255.0 green:159.0/255.0 blue:160.0/255.0 alpha:1.0] CGColor];
        [completeBtn setTitle:@"我来完善" forState:UIControlStateNormal];
        completeBtn.titleLabel.font = [UIFont systemFontOfSize:12.0];
        [completeBtn addTarget:self
                        action:@selector(redirectCompleteDetail)
              forControlEvents:UIControlEventTouchUpInside];
        [completeBtn setFrame:CGRectMake(self.view.frame.size.width - 80.0, y + 15.0, 60.0, 20.0)];
        [_contentScroll addSubview:completeBtn];
    }
}
```

第一个例子，我将按钮直接放在了里面。导致我后面做操作的时候，似乎将重新添加了一个层，将我的UIbutton按钮覆盖掉了。导致不起作用。第二个例子是我在这个项目的解决方案，直接分开，我将UIButton直接作为最后的层添加到view上，这样就不会覆盖掉，结果达到了我想要的效果。
