---
title: "iOS UIScrollView的touchesBegan和touchesEnd"
date: "2025-06-13 13:52:36"
slug: "ios-uiscrollview-de-touchesbegan-he-touchesend"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-UIScrollView的touchesBegan和touchesEnd/"
  - "/2025/06/13/iOS-UIScrollView的touchesBegan和touchesEnd.html"
  - "/iOS-UIScrollView的touchesBegan和touchesEnd/"
  - "/iOS-UIScrollView的touchesBegan和touchesEnd.html"
  - "/2025/06/13/ios-uiscrollview-de-touchesbegan-he-touchesend/"
  - "/2025/06/13/ios-uiscrollview-de-touchesbegan-he-touchesend.html"
  - "/ios-uiscrollview-de-touchesbegan-he-touchesend.html"
---
使用UIScrollView的时候，总是调用不了touchesBegan和touchesEnd，还有另外的两个方法，经过查找是因为UIScrollViewDelegate没有这个方法，不过我们可以自己来定义这个方法，来调用父类的方法：

touchScrollView.h

```objectivec
//
//  touchScrollView.h
//  xunYi7
//
//  Created by david on 13-5-28.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface touchScrollView : UIScrollView

@end
```

touchScrollView.m

```objectivec
//
//  touchScrollView.m
//  xunYi7
//
//  Created by david on 13-5-28.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "touchScrollView.h"

@implementation touchScrollView

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
    }
    return self;
}

-(void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event{
    [super touchesBegan:touches withEvent:event];
    if ( !self.dragging )
    {
        [[self nextResponder] touchesBegan:touches withEvent:event];
    }
}

-(void) touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event{
    [super touchesEnded:touches withEvent:event];
    if ( !self.dragging )
    {
        [[self nextResponder] touchesEnded:touches withEvent:event];
    }
}

-(void) touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event
{
    [super touchesEnded:touches withEvent:event];
    if(!self.dragging)
    {
        [[self nextResponder] touchesCancelled:touches withEvent:event];
    }
}

-(void) touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event
{
    [super touchesMoved:touches withEvent:event];
    if(!self.dragging)
    {
        [[self nextResponder] touchesMoved:touches withEvent:event];
    }
}

/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    // Drawing code
}
*/

@end
```

使用方法可以这样

```objectivec
@property (strong, nonatomic) IBOutlet touchScrollView *scrollView;
```
