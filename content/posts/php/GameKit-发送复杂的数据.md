---
title: "GameKit 发送复杂的数据"
date: "2025-06-20 14:34:07"
slug: "gamekit-fa-song-fu-za-de-shu-ju"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/GameKit-发送复杂的数据/"
  - "/2025/06/20/GameKit-发送复杂的数据.html"
  - "/GameKit-发送复杂的数据/"
  - "/GameKit-发送复杂的数据.html"
  - "/2025/06/20/gamekit-fa-song-fu-za-de-shu-ju/"
  - "/2025/06/20/gamekit-fa-song-fu-za-de-shu-ju.html"
  - "/gamekit-fa-song-fu-za-de-shu-ju.html"
---
使用GameKit 发送复杂的数据，

通过GameKit以字符串的形式发送颜色信息，这里涉及到一个知识点就是序列化数据和反序列化数据

关于复杂数据的发送有两个方法

```objectivec
-(NSString *) stringFromColor
{
    const CGFloat *c = CGColorGetComponents(self.CGColor);
    CGColorSpaceModel csm = CGColorSpaceGetModel(CGColorGetColorSpace(self.CGColor));
    return (csm == kCGColorSpaceModelRGB) ?
    [NSString stringWithFormat:@"%0.2f %0.2f %0.2f %0.2f", c[0], c[1], c[2], c[3]]
    :
    [NSString stringWithFormat:@"%0.2f %0.2f %0.2f %0.2f", c[0], c[0], c[0], c[1]];

}

+(UIColor *) colorWithString: (NSString *) colorString
{
    const CGFloat c[4];
    sscanf([colorString cStringUsingEncoding:NSUTF8StringEncoding], "%f %f %f %f", &c[0], &c[1], &c[2], &c[3]);
    return [UIColor colorWithRed:c[0] green:c[1] blue:c[2] alpha:c[3]];
}
```

这就是颜色转字符串，字符串转颜色的方法，这里实现支持ios5

这点代码放在了[DrawView](https://github.com/zhangda89/DrawView)文件中

整个发送复杂数据的流程如下

ComplexObjectsViewController.h

```objectivec
//
//  ComplexObjectsViewController.h
//  SendingComplexObjects
//
//  Created by david on 13-9-6.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GameKitHelper.h"
#import "DrawView.h"

#define BARBUTTON(TITLE, SELECTOR) 	[[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]
#define COLOR_ARRAY [NSArray arrayWithObjects:[UIColor whiteColor], [UIColor lightGrayColor], [UIColor darkGrayColor], [UIColor redColor], [UIColor orangeColor], [UIColor yellowColor], [UIColor greenColor], [UIColor blueColor], [UIColor purpleColor],  nil]
#define BASE_TINT	[UIColor darkGrayColor]

#define DATAPATH [NSString stringWithFormat:@"%@/Documents/drawing.archive", NSHomeDirectory()]

@interface ComplexObjectsViewController : UIViewController

-(void) archiveInterface;

@end
```

ComplexObjectsViewController.m

```objectivec
//
//  ComplexObjectsViewController.m
//  SendingComplexObjects
//
//  Created by david on 13-9-6.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "ComplexObjectsViewController.h"

@interface ComplexObjectsViewController ()

@end

@implementation ComplexObjectsViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	
    self.view.backgroundColor = [UIColor blackColor];
    self.navigationController.navigationBar.tintColor = BASE_TINT;
    
    //Retrieve (or create) the drawing surface
    [self unarchiveInterface];
    
    //Set up the color picking segmented controller
    NSMutableArray *items = [NSMutableArray array];
    for(UIColor *color in COLOR_ARRAY)
    {
        [items addObject:[self swatchWithColor:color]];
    }
    
    UISegmentedControl *seg = [[UISegmentedControl alloc] initWithItems:items];
    seg.tag = 102;
    seg.segmentedControlStyle = UISegmentedControlStyleBar;
    seg.center = CGPointMake(160.0f, 416.0f - 15.0f);
    seg.tintColor = BASE_TINT;
    seg.selectedSegmentIndex = 0;
    [seg addTarget:self
            action:@selector(colorChange:)
  forControlEvents:UIControlEventValueChanged];
    [self.view addSubview:seg];
    
    self.navigationItem.leftBarButtonItem = BARBUTTON(@"清除", @selector(doClear));
    
    [GameKitHelper sharedInstance].dataDelegate = self.view;
    [GameKitHelper sharedInstance].sessionID = @"Drawing Together";
    [GameKitHelper assignViewController:self];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(UIImage *) swatchWithColor:(UIColor *)color
{
    float side = 20.0f;
    UIGraphicsBeginImageContext(CGSizeMake(side, side));
    CGContextRef context = UIGraphicsGetCurrentContext();
    [color setFill];
    CGContextFillRect(context, CGRectMake(0.0f, 0.0f, side, side));
    UIImage *img = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return img;
}

//Transmit a clear request to the draw view
-(void) doClear
{
    [(DrawView *)[self.view viewWithTag:101] clear];
}

//Transmit a color change request to the draw view
-(void) colorChange:(UISegmentedControl *)seg
{
    UIColor *color = [COLOR_ARRAY objectAtIndex:seg.selectedSegmentIndex];
    DrawView *dv = (DrawView *)[self.view viewWithTag:101];
    dv.currentColor = color;
}

//Save the interface to file
-(void) archiveInterface
{
    DrawView *dv = (DrawView *)[self.view viewWithTag:101];
    [NSKeyedArchiver archiveRootObject:dv
                                toFile:DATAPATH];
    
}

-(void) unarchiveInterface
{
    DrawView *dv = [NSKeyedUnarchiver unarchiveObjectWithFile:DATAPATH];
    if(!dv)
    {
        dv = [[DrawView alloc] initWithFrame:CGRectMake(0.0f, 0.0f, 320.0f, 416.0f - 30.0f)];
        dv.userInteractionEnabled = YES;
        dv.tag = 101;
        [self.view  addSubview:dv];
    }
}

@end
```

这里的GameKitHelper.h和GameKitHelper.m文件可以到这里下载[GameKitHelper](https://github.com/zhangda89/GameKitHelper)

