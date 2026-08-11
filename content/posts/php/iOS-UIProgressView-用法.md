---
title: "iOS UIProgressView 用法"
date: "2025-06-12 17:44:54"
slug: "ios-uiprogressview-yong-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-UIProgressView-用法/"
  - "/2025/06/12/iOS-UIProgressView-用法.html"
  - "/iOS-UIProgressView-用法/"
  - "/iOS-UIProgressView-用法.html"
  - "/2025/06/12/ios-uiprogressview-yong-fa/"
  - "/2025/06/12/ios-uiprogressview-yong-fa.html"
  - "/ios-uiprogressview-yong-fa.html"
---
iOS实例-UIProgressView的简单实用方法

代码如下：

```objectivec ProgressViewViewController.h
#import <UIKit/UIKit.h>
@interface ProgressViewViewController : UIViewController
{
    UIProgressView *progressview;
    UIProgressView *barprogressview;
    NSTimer *timer;
    IBOutlet UIButton *startButton;
    IBOutlet UIButton *stopButton; 
}

@property (nonatomic,retain) IBOutlet UIProgressView *progressview;
@property (nonatomic,retain) IBOutlet UIProgressView *barprogressview;
-(IBAction) startProgress:(id)sender;
-(IBAction) stopProgress:(id)sender;

@end
```

```objectivec ProgressViewViewController.m
@implementation ProgressViewViewController

@synthesize progressview;
@synthesize barprogressview;

- (void)viewDidLoad
{
    self.progressview=nil;
    self.barprogressview=nil;
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    stopButton.enabled = NO;
    startButton.enabled = YES; 
}

-(void) dealloc
{
    self.progressview=nil;
    self.barprogressview=nil;
    
    [super dealloc];
}

- (void)viewDidUnload
{
    self.progressview=nil;
    self.barprogressview=nil;
    [super viewDidUnload];
    // Release any retained subviews of the main view.
}


/*进度条每次加0.01 */
-(void) timerChanged:(id)sender
{
    self.progressview.progress +=0.01f;
    self.barprogressview.progress +=0.01f;
}

-(IBAction) startProgress:(id)sender
{
    
    timer=[NSTimer scheduledTimerWithTimeInterval:0.03f
                                         target:self 
                                         selector:@selector(timerChanged:) 
                                         userInfo:nil 
                                         repeats:YES];
     //[timer retain];
      startButton.enabled = NO;
    stopButton.enabled = YES;
}
-(IBAction) stopProgress:(id)sender
{
    [timer invalidate];
    //[timer release];
    //timer =nil;
    
    self.progressview.progress=0.0f;
    self.barprogressview.progress=0.0f;
 
     startButton.enabled = YES;
    stopButton.enabled = NO;
}
```

这里提示一点是progress的最大值为1，最小值为0
