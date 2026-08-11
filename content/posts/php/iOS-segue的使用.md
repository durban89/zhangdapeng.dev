---
title: "iOS segue的使用"
date: "2025-06-13 10:13:48"
slug: "ios-segue-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-segue的使用/"
  - "/2025/06/13/iOS-segue的使用.html"
  - "/iOS-segue的使用/"
  - "/iOS-segue的使用.html"
  - "/2025/06/13/ios-segue-de-shi-yong/"
  - "/2025/06/13/ios-segue-de-shi-yong.html"
  - "/ios-segue-de-shi-yong.html"
---
在storyboard中，segue有几种不同的类型，在iphone和ipad的开发中，segue的类型是不同的。

在iphone中，segue有：push，modal，和custom三种不同的类型，这些类型的区别在与新页面出现的方式。

而在ipad中，有push，modal，popover，replace和custom五种不同的类型。

根据这几个特点，同时自己有观看了，斯坦福大学的公开课，里面也是有关于此方面的应用。废话少说，将自己的实例放上来吧。

里面的内容大部分跟课程里面的内容差不多



```objectivec PsychologistViewController.m
//
//  PsychologistViewController.m
//  Psychologist
//
//  Created by david on 13-5-26.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "PsychologistViewController.h"
#import "happinessViewController.h"

@interface PsychologistViewController ()

@property (nonatomic) int diagnosis;

@end

@implementation PsychologistViewController

@synthesize diagnosis = _diagnosis;

-(void) setAndShowDiagnosis:(int)diagnosis
{
    self.diagnosis = diagnosis;
    [self performSegueWithIdentifier:@"showDiagnosis" sender:self];
}

-(void) prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if([segue.identifier isEqualToString:@"showDiagnosis"])
    {
        [segue.destinationViewController setHappiness:self.diagnosis];
    }
    else if([segue.identifier isEqualToString:@"movie"])
    {
        [segue.destinationViewController setHappiness:50];
    }
    else if([segue.identifier isEqualToString:@"teleplay"])
    {
        [segue.destinationViewController setHappiness:20];
    }
    else if([segue.identifier isEqualToString:@"cartoon"])
    {
        [segue.destinationViewController setHappiness:100];
    }
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation
{
    return YES;
}

- (IBAction)flaying:(id)sender
{
    [self setAndShowDiagnosis:86];
}

- (IBAction)bite:(id)sender
{
    [self setAndShowDiagnosis:70];
}

- (IBAction)play:(id)sender
{
    [self setAndShowDiagnosis:20];
}
@end
```



```objectivec PsychologistViewController.h
//
//  PsychologistViewController.h
//  Psychologist
//
//  Created by david on 13-5-26.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface PsychologistViewController : UIViewController
- (IBAction)flaying:(id)sender;
- (IBAction)bite:(id)sender;
- (IBAction)play:(id)sender;

@end
```



```objectivec faceView.h
//
//  faceView.h
//  happiness
//
//  Created by david on 13-5-23.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>


@class faceView;

@protocol FaceViewDataSource
-(float) smileForFaceView:(faceView *) sender;
@end


@interface faceView : UIView

@property (nonatomic) CGFloat scale;
-(void) pinch:(UIPinchGestureRecognizer *)gesture;

@property (nonatomic, weak) IBOutlet id<FaceViewDataSource> dataSource;

@end
```



```objectivec faceView.m
//
//  faceView.m
//  happiness
//
//  Created by david on 13-5-23.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "faceView.h"

#define DEFAULT_SCALE 0.90
#define EYE_H 0.35
#define EYE_V 0.35
#define EYE_RADIUS  0.10
#define MOUTH_H 0.45
#define MOUTH_V 0.40
#define MOUTH_SMILE 0.25


@implementation faceView

@synthesize scale = _scale;

-(CGFloat) scale
{
    if(!_scale)
    {
        return DEFAULT_SCALE;
    }else{
        return _scale;
    }
}


-(void) setScale:(CGFloat)scale
{
    if(scale != _scale)
    {
        _scale = scale;
        [self setNeedsDisplay];
    }
}

-(void) pinch:(UIPinchGestureRecognizer *)gesture
{
    if((gesture.state == UIGestureRecognizerStateChanged) || (gesture.state == UIGestureRecognizerStateEnded))
    {
        self.scale = gesture.scale;
        gesture.scale = 1;
    }
}


-(void) setup
{
    self.contentMode = UIViewContentModeRedraw;
}

-(void) awakeFromNib
{
    [self setup];
}

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
        [self setup];
    }
    return self;
}

-(void) drawCircleAtPoint:(CGPoint)p withRadius:(CGFloat)radius inContext:(CGContextRef)context
{
    UIGraphicsPushContext(context);
    CGContextBeginPath(context);
    CGContextAddArc(context, p.x, p.y, radius, 0 , 2*M_PI, YES);
    CGContextStrokePath(context);
    UIGraphicsPopContext();
}

// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    
    //face
    CGContextRef context = UIGraphicsGetCurrentContext();
    
    CGPoint midPoint;
    midPoint.x = self.bounds.origin.x + self.bounds.size.width / 2;
    midPoint.y = self.bounds.origin.y + self.bounds.size.height / 2;
    
    
    CGFloat size = self.bounds.size.width / 2;
    if(self.bounds.size.height < self.bounds.size.width) size = self.bounds.size.height / 2;
    
    size *= self.scale;
    
    CGContextSetLineWidth(context, 5.0);
    [[UIColor blueColor] setStroke];
    
    [self drawCircleAtPoint:midPoint withRadius:size inContext: context];
    
    //eye
    CGPoint eyePoint;
    eyePoint.x = midPoint.x - size * EYE_H;
    eyePoint.y = midPoint.y - size * EYE_V;
    [self drawCircleAtPoint:eyePoint withRadius:size * EYE_RADIUS inContext:context];
    eyePoint.x +=  size * EYE_H  * 2;
    [self drawCircleAtPoint:eyePoint withRadius:size * EYE_RADIUS inContext:context];
    
    
    //mouth
    CGPoint mouthStartPoint;
    mouthStartPoint.x = midPoint.x - size * MOUTH_H;
    mouthStartPoint.y = midPoint.y + size * MOUTH_V;
    CGPoint mouthEndPoint = mouthStartPoint;
    mouthEndPoint.x += MOUTH_H * size * 2;
    
    CGPoint mouthCP1 = mouthStartPoint;
    mouthCP1.x += MOUTH_H * size * 2 / 3;
    
    CGPoint mouthCP2 = mouthEndPoint;
    mouthCP2.x -= MOUTH_V * size * 2 / 3;
    
    float smile = [self.dataSource smileForFaceView:self];
    if(smile < -1) smile = -1;
    if(smile > 1) smile = 1;
    
    CGFloat smileOffset = MOUTH_SMILE * size * smile;
    mouthCP1.y += smileOffset;
    mouthCP2.y += smileOffset;
    
    CGContextBeginPath(context);
    CGContextMoveToPoint(context, mouthStartPoint.x, mouthStartPoint.y);
    CGContextAddCurveToPoint(context, mouthCP1.x, mouthCP1.y, mouthCP2.x, mouthCP2.y, mouthEndPoint.x, mouthEndPoint.y);
    CGContextStrokePath(context);
    // Drawing code
}


@end
```



```objectivec happinessViewController.m
//
//  happinessViewController.m
//  happiness
//
//  Created by david on 13-5-23.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "happinessViewController.h"
#import "faceView.h"

@interface happinessViewController ()<FaceViewDataSource>
@property (weak, nonatomic) IBOutlet faceView *faceView;
@end

@implementation happinessViewController


@synthesize happiness = _happiness;
@synthesize faceView = _faceView;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

-(void) setHappiness:(int)happiness
{
    _happiness = happiness;
    [self.faceView setNeedsDisplay];
}

-(void) setFaceView:(faceView *)faceView
{
    _faceView = faceView;
    [self.faceView addGestureRecognizer:[[UIPinchGestureRecognizer alloc] initWithTarget:self.faceView action:@selector(pinch:)]];
    [self.faceView addGestureRecognizer:[[UIPanGestureRecognizer alloc] initWithTarget:self action:@selector(handleHappinessGesture:)]];
    self.faceView.dataSource = self;
}

-(void) handleHappinessGesture:(UIPanGestureRecognizer *)gesture
{
    if(gesture.state == UIGestureRecognizerStateChanged || gesture.state == UIGestureRecognizerStateEnded)
    {
        CGPoint translation = [gesture translationInView:self.faceView];
        self.happiness -= translation.y / 2;
        [gesture setTranslation:CGPointZero inView:self.faceView];
    }
}

-(float) smileForFaceView:(faceView *)sender
{
    return  (self.happiness - 50.0) / 50.0;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation
{
    return YES;
}

@end
```



```objectivec happinessViewController.h
//
//  happinessViewController.h
//  happiness
//
//  Created by david on 13-5-23.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface happinessViewController : UIViewController

@property (nonatomic) int happiness; //0 代表不开心  100 代表开心

@end
```

应用截图相册地址：http://my.poco.cn/album/album\_show\_photo\_list.htx&user\_id=173673909&set\_hash=3946768073
