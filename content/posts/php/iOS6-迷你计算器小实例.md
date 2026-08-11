---
title: "iOS6 迷你计算器小实例"
date: "2025-06-23 15:27:29"
slug: "ios6-mi-ni-ji-suan-qi-xiao-shi-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS6-迷你计算器小实例/"
  - "/2025/06/23/iOS6-迷你计算器小实例.html"
  - "/iOS6-迷你计算器小实例/"
  - "/iOS6-迷你计算器小实例.html"
  - "/2025/06/23/ios6-mi-ni-ji-suan-qi-xiao-shi-li/"
  - "/2025/06/23/ios6-mi-ni-ji-suan-qi-xiao-shi-li.html"
  - "/ios6-mi-ni-ji-suan-qi-xiao-shi-li.html"
---
我们来做一下小的实例，迷你计算器，很简单的，虽然这里初次不是很完善，后面会渐渐完善的。

新建Single View Application项目CaculateUI,类前缀CaculateUI。

CaculateUIAppDelegate两个文件均为自动生成未修改。

新建一个Objective-C Class，名为CalculatorBrain，这个就是MVC模式中的Model,所有的数据处理都在这里，CalculatorViewController取到数据后，作简单的转换以符合Model的要求，再传给Model，由Model处理完返回处理结果给Controller,再由Controller更新View.

CalculatorBrain.h

```objectivec
//
//  CalculatorBrain.h
//  CaculateUI
//
//  Created by david on 13-9-10.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface CalculatorBrain : NSObject

//存储执行结果
@property (nonatomic) double result;
//存储操作符
@property (copy, nonatomic) NSString *tempOperateString;


-(void) operate:(double) number:(NSString *) operateString;
-(double) caculate:(double) number;

@end
```

CalculatorBrain.m

```objectivec
//
//  CalculatorBrain.m
//  CaculateUI
//
//  Created by david on 13-9-10.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "CalculatorBrain.h"

@implementation CalculatorBrain

@synthesize result;
@synthesize tempOperateString;

-(void) operate:(double)number :(NSString *)operateString
{
    self.result = number;
    self.tempOperateString = operateString;
}

-(double) caculate:(double)number
{
    //根据操作符执行相关操作
    if([self.tempOperateString isEqualToString:@"+"])
    {
        self.result += number;
    }
    else if([self.tempOperateString isEqualToString:@"-"])
    {
        self.result -= number;
    }
    else if([self.tempOperateString isEqualToString:@"*"])
    {
        self.result *= number;
    }
    else if([self.tempOperateString isEqualToString:@"/"])
    {
        if(number == 0)
        {
            self.result = 0;
        }
        else
        {
            self.result /= number;
        }
    }
    
    return self.result;
}

@end
```

由于我这里没有使用xib这种东西，所以下面就感觉比较复杂，不过您如果有更好的方法，请提示我一下，谢谢

CaculateUIViewController.h

```objectivec
//
//  CaculateUIViewController.h
//  CaculateUI
//
//  Created by david on 13-8-29.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
@class CalculatorBrain;
@class FUIButton;

@interface CaculateUIViewController : UIViewController

@property (strong, nonatomic) FUIButton *One;
@property (strong, nonatomic) FUIButton *Two;
@property (strong, nonatomic) FUIButton *Three;
@property (strong, nonatomic) FUIButton *Four;
@property (strong, nonatomic) FUIButton *Five;
@property (strong, nonatomic) FUIButton *Six;
@property (strong, nonatomic) FUIButton *Seven;
@property (strong, nonatomic) FUIButton *Eight;
@property (strong, nonatomic) FUIButton *Nine;
@property (strong, nonatomic) FUIButton *Ten;
@property (strong, nonatomic) FUIButton *Zero;

//小数点
@property (strong, nonatomic) FUIButton *Decimal;
//等号
@property (strong, nonatomic) FUIButton *Equal;
//加号
@property (strong, nonatomic) FUIButton *Plus;
//减号
@property (strong, nonatomic) FUIButton *Minus;
//乘号
@property (strong, nonatomic) FUIButton *Multiply;
//除号
@property (strong, nonatomic) FUIButton *Division;

@property (strong, nonatomic) UILabel *display;
@property (nonatomic) BOOL isEntering;
@property (strong, nonatomic) CalculatorBrain *brain;


//数字键按下操作
-(void) digitalPressed:(id)sender;
//操作符按下操作
-(void) operatePressed:(id)sender;
//等于号按下操作
-(void) enterPressed:(id)sender;




@end
```

CaculateUIViewController.m

```objectivec
//
//  CaculateUIViewController.m
//  CaculateUI
//
//  Created by david on 13-8-29.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "CaculateUIViewController.h"
#import "CalculatorBrain.h"
#import "FUIButton.h"
#import "UIColor+FlatUI.h"
#import "UIFont+FlatUI.h"
#import "UINavigationBar+FlatUI.h"

@interface CaculateUIViewController ()

@end

@implementation CaculateUIViewController

@synthesize One;
@synthesize Two;
@synthesize Three;
@synthesize Four;
@synthesize Five;
@synthesize Six;
@synthesize Seven;
@synthesize Eight;
@synthesize Nine;
@synthesize Ten;
@synthesize Zero;
@synthesize Decimal;
@synthesize Equal;
@synthesize Plus;
@synthesize Minus;
@synthesize Multiply;
@synthesize Division;


@synthesize display;
@synthesize brain;
@synthesize isEntering;

- (void)viewDidLoad
{
//    CGFloat btnWidth = 70.0;
    CGFloat btnXInterval = 5.0;
    CGFloat btnWidth = (self.view.frame.size.width - 2 * 5.0 - 3 * btnXInterval) / 4;
    
    
    self.title = @"迷你计算器";
    
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    display = [[UILabel alloc] initWithFrame:CGRectMake(5.0,
                                                        5.0,
                                                        310.0,
                                                        90.0)];
    display.backgroundColor = [UIColor blackColor];
    display.text = @"";
    display.textAlignment = NSTextAlignmentRight;
    display.font = [UIFont systemFontOfSize:40.0];
    display.textColor = [UIColor whiteColor];
    [self.view addSubview:display];
    
    if(!self.brain)
    {
        self.brain = [[CalculatorBrain alloc] init];
    }

    
    //第一个按钮
    One = [FUIButton buttonWithType:UIButtonTypeCustom];
    [One setFrame:CGRectMake(5.0,
                             100.0,
                             btnWidth,
                             30.0)];
    [One setTitle:@"1" forState:UIControlStateNormal];
    [One addTarget:self
            action:@selector(digitalPressed:)
  forControlEvents:UIControlEventTouchUpInside];
    [self decorationButton:One];
    [self.view addSubview:One];
    
    //第二个按钮
    Two = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Two setFrame:CGRectMake(btnWidth + 5.0 + btnXInterval,
                             100.0,
                             btnWidth,
                             30.0)];
    [Two setTitle:@"2" forState:UIControlStateNormal];
    [Two addTarget:self
            action:@selector(digitalPressed:)
  forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Two];
    
    //第三个按钮
    Three = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Three setFrame:CGRectMake(2 * btnWidth + 5.0 + 2 * btnXInterval,
                             100.0,
                             btnWidth,
                             30.0)];
    [Three setTitle:@"3" forState:UIControlStateNormal];
    [Three addTarget:self
            action:@selector(digitalPressed:)
  forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Three];
    
    
    //加号按钮
    Plus = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Plus setFrame:CGRectMake(3 * btnWidth + 5.0 + 3 * btnXInterval,
                               100.0,
                               btnWidth,
                               30.0)];
    [Plus setTitle:@"+" forState:UIControlStateNormal];
    [Plus addTarget:self
              action:@selector(operatePressed:)
    forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Plus];

    
    
    //第四个按钮
    Four = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Four setFrame:CGRectMake(5.0,
                               135.0,
                               btnWidth,
                               30.0)];
    [Four setTitle:@"4" forState:UIControlStateNormal];
    [Four addTarget:self
              action:@selector(digitalPressed:)
    forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Four];
    
    //第五个按钮
    Five = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Five setFrame:CGRectMake(btnWidth + 5.0 + btnXInterval,
                               135.0,
                               btnWidth,
                               30.0)];
    [Five setTitle:@"5" forState:UIControlStateNormal];
    [Five addTarget:self
             action:@selector(digitalPressed:)
   forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Five];
    
    //第六个按钮
    Six = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Six setFrame:CGRectMake(2 * btnWidth + 5.0 + 2 * btnXInterval,
                               135.0,
                               btnWidth,
                               30.0)];
    [Six setTitle:@"6" forState:UIControlStateNormal];
    [Six addTarget:self
             action:@selector(digitalPressed:)
   forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Six];
    
    //减号按钮
    Minus = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Minus setFrame:CGRectMake(3 * btnWidth + 5.0 + 3 * btnXInterval,
                             135.0,
                             btnWidth,
                             30.0)];
    [Minus setTitle:@"-" forState:UIControlStateNormal];
    [Minus addTarget:self
                 action:@selector(operatePressed:)
       forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Minus];
    
    
    //第七个按钮
    Seven = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Seven setFrame:CGRectMake(5.0,
                               170.0,
                               btnWidth,
                               30.0)];
    [Seven setTitle:@"7" forState:UIControlStateNormal];
    [Seven addTarget:self
            action:@selector(digitalPressed:)
  forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Seven];
    
    //第八个按钮
    Eight = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Eight setFrame:CGRectMake(btnWidth + 5.0 + btnXInterval,
                               170.0,
                               btnWidth,
                               30.0)];
    [Eight setTitle:@"8" forState:UIControlStateNormal];
    [Eight addTarget:self
              action:@selector(digitalPressed:)
    forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Eight];
    
    //第九个按钮
    Nine = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Nine setFrame:CGRectMake(2 * btnWidth + 5.0 + 2 * btnXInterval,
                               170.0,
                               btnWidth,
                               30.0)];
    [Nine setTitle:@"9" forState:UIControlStateNormal];
    [Nine addTarget:self
              action:@selector(digitalPressed:)
    forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Nine];
    
    //乘号按钮
    Multiply = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Multiply setFrame:CGRectMake(3 * btnWidth + 5.0 + 3 * btnXInterval,
                               170.0,
                               btnWidth,
                               30.0)];
    [Multiply setTitle:@"*" forState:UIControlStateNormal];
    [Multiply addTarget:self
                 action:@selector(operatePressed:)
       forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Multiply];
    
    //小数点按钮
    Decimal = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Decimal setFrame:CGRectMake(5.0,
                             205.0,
                             btnWidth,
                             30.0)];
    [Decimal setTitle:@"." forState:UIControlStateNormal];
    [Decimal addTarget:self
            action:@selector(digitalPressed:)
  forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Decimal];
    
    
    //第十个按钮
    Ten = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Ten setFrame:CGRectMake(btnWidth + 5.0 + btnXInterval,
                               205.0,
                               btnWidth,
                               30.0)];
    [Ten setTitle:@"0" forState:UIControlStateNormal];
    [Ten addTarget:self
             action:@selector(digitalPressed:)
   forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Ten];
    
    //等号按钮
    Equal = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Equal setFrame:CGRectMake(2 * btnWidth + 5.0 + 2 * btnXInterval,
                             205.0,
                             btnWidth,
                             30.0)];
    [Equal setTitle:@"=" forState:UIControlStateNormal];
    [Equal addTarget:self
              action:@selector(enterPressed:)
    forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Equal];
    
    //除号按钮
    Division = [FUIButton buttonWithType:UIButtonTypeCustom];
    [Division setFrame:CGRectMake(3 * btnWidth + 5.0 + 3 * btnXInterval,
                                  205.0,
                                  btnWidth,
                                  30.0)];
    [Division setTitle:@"/" forState:UIControlStateNormal];
    [Division addTarget:self
                 action:@selector(operatePressed:)
       forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:Division];
    
    [self decorationButton:One];
    [self decorationButton:Two];
    [self decorationButton:Three];
    [self decorationButton:Four];
    [self decorationButton:Five];
    [self decorationButton:Six];
    [self decorationButton:Seven];
    [self decorationButton:Eight];
    [self decorationButton:Nine];
    [self decorationButton:Ten];
    [self decorationButton:Zero];
    [self decorationButton:Equal];
    [self decorationButton:Decimal];
    [self decorationButton:Plus];
    [self decorationButton:Minus];
    [self decorationButton:Multiply];
    [self decorationButton:Division];
}

-(void) viewDidAppear:(BOOL)animated
{
    [self.navigationController.navigationBar configureFlatNavigationBarWithColor:[UIColor midnightBlueColor]];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(void) decorationButton:(FUIButton *)btn{
    btn.buttonColor = [UIColor turquoiseColor];
    btn.shadowColor = [UIColor greenSeaColor];
    btn.shadowHeight = 3.0f;
    btn.cornerRadius = 6.0f;
    btn.titleLabel.font = [UIFont boldFlatFontOfSize:16];
    [btn setTitleColor:[UIColor cloudsColor] forState:UIControlStateNormal];
    [btn setTitleColor:[UIColor cloudsColor] forState:UIControlStateHighlighted];
}

//-(CalculatorBrain *) brain
//{
//    if(!self.brain)
//    {
//        self.brain = [[CalculatorBrain alloc] init];
//    }
//    return  self.brain;
//}

//数字键按下操作
-(void) digitalPressed:(id)sender
{
    if(self.isEntering == YES)
    {
        //如果之前输入的数字少于12位
        if([self.display.text length] < 12)
        {
            //把按到的数字转换成字符串加到原来显示的字符串的末尾，并更新显示
            self.display.text = [self.display.text stringByAppendingString:[sender currentTitle]];
        }
        else//如果就输入的数字大于等于12位，不操作，直接返回
        {
            return;
        }
    }
    else//如果之前不是输入状态，即现在输入的是数字的第一位（最高位）
    {
        //显示输入的数字
        self.display.text = [sender currentTitle];
        //把输入的状态改为YES
        self.isEntering = YES;
    }
}

//操作符按下操作
-(void) operatePressed:(id)sender
{
    //输入状态改为NO
    self.isEntering = NO;
    //取到显示的数字。转换为double
    double num = [self.display.text doubleValue];
    //把数字和操作符发送给CalculatorBrain的operate接收器
    [self.brain operate:num :[sender currentTitle]];
}

//等于号按下操作
-(void) enterPressed:(id)sender
{
    //把输入状态改为NO
    self.isEntering = NO;
    //取到显示的数字，转换为double
    double num = [self.display.text doubleValue];
    //把数字发送给CalculateBrain的calcute接收器，并接受返回的结果
    double result = [self.brain caculate:num];
    //把结果显示在屏幕上
    self.display.text = [NSString stringWithFormat:@"%g",result];
}

-(BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation
{
    return (toInterfaceOrientation != UIDeviceOrientationPortraitUpsideDown);
}

//-(BOOL) shouldAutorotate
//{
//    return YES;
//}
//
//-(NSUInteger) supportedInterfaceOrientations
//{
//    return UIInterfaceOrientationMaskLandscape;
//}


@end
```

里面使用到了FlatUI，可以自行google搜索然后下载。

