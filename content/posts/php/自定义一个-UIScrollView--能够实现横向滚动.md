---
title: "自定义一个 UIScrollView ，能够实现横向滚动"
date: "2025-06-20 09:52:02"
slug: "zi-ding-yi-yi-ge-uiscrollview-neng-gou-shi-xian-heng-xiang-gun-dong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/自定义一个-UIScrollView-，能够实现横向滚动/"
  - "/2025/06/20/自定义一个-UIScrollView-，能够实现横向滚动.html"
  - "/自定义一个-UIScrollView-，能够实现横向滚动/"
  - "/自定义一个-UIScrollView-，能够实现横向滚动.html"
  - "/2025/06/20/自定义一个-UIScrollView-能够实现横向滚动/"
  - "/2025/06/20/自定义一个-UIScrollView-能够实现横向滚动.html"
  - "/2025/06/20/zi-ding-yi-yi-ge-uiscrollview-neng-gou-shi-xian-heng-xiang-gun-dong/"
  - "/2025/06/20/zi-ding-yi-yi-ge-uiscrollview-neng-gou-shi-xian-heng-xiang-gun-dong.html"
  - "/zi-ding-yi-yi-ge-uiscrollview-neng-gou-shi-xian-heng-xiang-gun-dong.html"
---
关于自定义UIScrollview的方式，其实很简单，但是如何做到横向滚动，我自己是第一次使用，

先来定义一个类吧:customScrollView.h

```objectivec
#import <UIKit/UIKit.h>

@interface customScrollView : UIScrollView <UIScrollViewDelegate>

@end
```

下面看customScrollView.m的定义

```objectivec
@property (nonatomic, strong) NSMutableArray *visibleLabels;
@property (nonatomic, strong) UIView *labelContainerView;
```

定义两个属性，第一个是label数组，第二个是一个UIView

然后实现一下初始化的代码操作

```objectivec
- (id)initWithCoder:(NSCoder *)aDecoder
{
    if ((self = [super initWithCoder:aDecoder]))
    {
        self.contentSize = CGSizeMake(5000, self.frame.size.height);
        
        _visibleLabels = [[NSMutableArray alloc] init];
        
        _labelContainerView = [[UIView alloc] init];
        self.labelContainerView.frame = CGRectMake(0, 0, self.contentSize.width, self.contentSize.height/2);
        [self addSubview:self.labelContainerView];

        [self.labelContainerView setUserInteractionEnabled:NO];
        
        // hide horizontal scroll indicator so our recentering trick is not revealed
        [self setShowsHorizontalScrollIndicator:NO];
    }
    return self;
}
```

都是一些基本的初始化的操作

下面看一下这个方法，这个方法，是在UIScrollView在滚动的时候进行调用的

```objectivec
- (void)layoutSubviews
{
    [super layoutSubviews];
    
    [self recenterIfNecessary];
 
    // tile content in visible bounds
    CGRect visibleBounds = [self convertRect:[self bounds] toView:self.labelContainerView];
    CGFloat minimumVisibleX = CGRectGetMinX(visibleBounds);
    CGFloat maximumVisibleX = CGRectGetMaxX(visibleBounds);
    
    [self tileLabelsFromMinX:minimumVisibleX toMaxX:maximumVisibleX];
}
```

里面有一个方法，我写下下面

```objectivec
- (void)recenterIfNecessary
{
    CGPoint currentOffset = [self contentOffset];
    CGFloat contentWidth = [self contentSize].width;
    CGFloat centerOffsetX = (contentWidth - [self bounds].size.width) / 2.0;
    CGFloat distanceFromCenter = fabs(currentOffset.x - centerOffsetX);
    
    if (distanceFromCenter > (contentWidth / 4.0))
    {
        self.contentOffset = CGPointMake(centerOffsetX, currentOffset.y);
        
        // move content by the same amount so it appears to stay still
        for (UILabel *label in self.visibleLabels) {
            CGPoint center = [self.labelContainerView convertPoint:label.center toView:self];
            center.x += (centerOffsetX - currentOffset.x);
            label.center = [self convertPoint:center toView:self.labelContainerView];
        }
    }
}
```

这个方法是用来控制label的位置的。

当UIScrollview在滚动的时候，我们需要做一些操作

```objectivec
- (UILabel *)insertLabel
{
    UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 500, 80)];
    [label setNumberOfLines:3];
    [label setText:@"1024 Block Street\nShaffer, CA\n95014"];
    [self.labelContainerView addSubview:label];

    return label;
}


- (CGFloat)placeNewLabelOnRight:(CGFloat)rightEdge
{
    UILabel *label = [self insertLabel];
    [self.visibleLabels addObject:label]; // add rightmost label at the end of the array
    
    CGRect frame = [label frame];
    frame.origin.x = rightEdge;
    frame.origin.y = [self.labelContainerView bounds].size.height - frame.size.height;
    [label setFrame:frame];
        
    return CGRectGetMaxX(frame);
}

- (CGFloat)placeNewLabelOnLeft:(CGFloat)leftEdge
{
    UILabel *label = [self insertLabel];
    [self.visibleLabels insertObject:label atIndex:0]; // add leftmost label at the beginning of the array
    
    CGRect frame = [label frame];
    frame.origin.x = leftEdge - frame.size.width;
    frame.origin.y = [self.labelContainerView bounds].size.height - frame.size.height;
    [label setFrame:frame];
    
    return CGRectGetMinX(frame);
}

- (void)tileLabelsFromMinX:(CGFloat)minimumVisibleX toMaxX:(CGFloat)maximumVisibleX
{
    // the upcoming tiling logic depends on there already being at least one label in the visibleLabels array, so
    // to kick off the tiling we need to make sure there's at least one label
    if ([self.visibleLabels count] == 0)
    {
        [self placeNewLabelOnRight:minimumVisibleX];
    }
    
    // add labels that are missing on right side
    UILabel *lastLabel = [self.visibleLabels lastObject];
    CGFloat rightEdge = CGRectGetMaxX([lastLabel frame]);
    while (rightEdge < maximumVisibleX)
    {
        rightEdge = [self placeNewLabelOnRight:rightEdge];
    }
    
    // add labels that are missing on left side
    UILabel *firstLabel = self.visibleLabels[0];
    CGFloat leftEdge = CGRectGetMinX([firstLabel frame]);
    while (leftEdge > minimumVisibleX)
    {
        leftEdge = [self placeNewLabelOnLeft:leftEdge];
    }
    
    // remove labels that have fallen off right edge
    lastLabel = [self.visibleLabels lastObject];
    while ([lastLabel frame].origin.x > maximumVisibleX)
    {
        [lastLabel removeFromSuperview];
        [self.visibleLabels removeLastObject];
        lastLabel = [self.visibleLabels lastObject];
    }
    
    // remove labels that have fallen off left edge
    firstLabel = self.visibleLabels[0];
    while (CGRectGetMaxX([firstLabel frame]) < minimumVisibleX)
    {
        [firstLabel removeFromSuperview];
        [self.visibleLabels removeObjectAtIndex:0];
        firstLabel = self.visibleLabels[0];
    }
}
```

一个是插入label的方法

一个是从左侧到右侧滑动的操作

一个是从右侧到左侧滑动的操作

还有一个方法是用来控制label的

好了。一些基本的操作就在这里面了，打击可以自己复制一份自己看看

我来个完整版的,当然我这个调用的时候，是在自己的xib文件中调用的。

```objectivec
#import "customScrollView.h"

@interface InfiniteScrollView ()

@property (nonatomic, strong) NSMutableArray *visibleLabels;
@property (nonatomic, strong) UIView *labelContainerView;

@end


@implementation InfiniteScrollView

- (id)initWithCoder:(NSCoder *)aDecoder
{
    if ((self = [super initWithCoder:aDecoder]))
    {
        self.contentSize = CGSizeMake(5000, self.frame.size.height);
        
        _visibleLabels = [[NSMutableArray alloc] init];
        
        _labelContainerView = [[UIView alloc] init];
        self.labelContainerView.frame = CGRectMake(0, 0, self.contentSize.width, self.contentSize.height/2);
        [self addSubview:self.labelContainerView];

        [self.labelContainerView setUserInteractionEnabled:NO];
        
        // hide horizontal scroll indicator so our recentering trick is not revealed
        [self setShowsHorizontalScrollIndicator:NO];
    }
    return self;
}


#pragma mark - Layout

// recenter content periodically to achieve impression of infinite scrolling
- (void)recenterIfNecessary
{
    CGPoint currentOffset = [self contentOffset];
    CGFloat contentWidth = [self contentSize].width;
    CGFloat centerOffsetX = (contentWidth - [self bounds].size.width) / 2.0;
    CGFloat distanceFromCenter = fabs(currentOffset.x - centerOffsetX);
    
    if (distanceFromCenter > (contentWidth / 4.0))
    {
        self.contentOffset = CGPointMake(centerOffsetX, currentOffset.y);
        
        // move content by the same amount so it appears to stay still
        for (UILabel *label in self.visibleLabels) {
            CGPoint center = [self.labelContainerView convertPoint:label.center toView:self];
            center.x += (centerOffsetX - currentOffset.x);
            label.center = [self convertPoint:center toView:self.labelContainerView];
        }
    }
}

- (void)layoutSubviews
{
    [super layoutSubviews];
    
    [self recenterIfNecessary];
 
    // tile content in visible bounds
    CGRect visibleBounds = [self convertRect:[self bounds] toView:self.labelContainerView];
    CGFloat minimumVisibleX = CGRectGetMinX(visibleBounds);
    CGFloat maximumVisibleX = CGRectGetMaxX(visibleBounds);
    
    [self tileLabelsFromMinX:minimumVisibleX toMaxX:maximumVisibleX];
}


#pragma mark - Label Tiling

- (UILabel *)insertLabel
{
    UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 500, 80)];
    [label setNumberOfLines:3];
    [label setText:@"1024 Block Street\nShaffer, CA\n95014"];
    [self.labelContainerView addSubview:label];

    return label;
}


- (CGFloat)placeNewLabelOnRight:(CGFloat)rightEdge
{
    UILabel *label = [self insertLabel];
    [self.visibleLabels addObject:label]; // add rightmost label at the end of the array
    
    CGRect frame = [label frame];
    frame.origin.x = rightEdge;
    frame.origin.y = [self.labelContainerView bounds].size.height - frame.size.height;
    [label setFrame:frame];
        
    return CGRectGetMaxX(frame);
}

- (CGFloat)placeNewLabelOnLeft:(CGFloat)leftEdge
{
    UILabel *label = [self insertLabel];
    [self.visibleLabels insertObject:label atIndex:0]; // add leftmost label at the beginning of the array
    
    CGRect frame = [label frame];
    frame.origin.x = leftEdge - frame.size.width;
    frame.origin.y = [self.labelContainerView bounds].size.height - frame.size.height;
    [label setFrame:frame];
    
    return CGRectGetMinX(frame);
}

- (void)tileLabelsFromMinX:(CGFloat)minimumVisibleX toMaxX:(CGFloat)maximumVisibleX
{
    // the upcoming tiling logic depends on there already being at least one label in the visibleLabels array, so
    // to kick off the tiling we need to make sure there's at least one label
    if ([self.visibleLabels count] == 0)
    {
        [self placeNewLabelOnRight:minimumVisibleX];
    }
    
    // add labels that are missing on right side
    UILabel *lastLabel = [self.visibleLabels lastObject];
    CGFloat rightEdge = CGRectGetMaxX([lastLabel frame]);
    while (rightEdge < maximumVisibleX)
    {
        rightEdge = [self placeNewLabelOnRight:rightEdge];
    }
    
    // add labels that are missing on left side
    UILabel *firstLabel = self.visibleLabels[0];
    CGFloat leftEdge = CGRectGetMinX([firstLabel frame]);
    while (leftEdge > minimumVisibleX)
    {
        leftEdge = [self placeNewLabelOnLeft:leftEdge];
    }
    
    // remove labels that have fallen off right edge
    lastLabel = [self.visibleLabels lastObject];
    while ([lastLabel frame].origin.x > maximumVisibleX)
    {
        [lastLabel removeFromSuperview];
        [self.visibleLabels removeLastObject];
        lastLabel = [self.visibleLabels lastObject];
    }
    
    // remove labels that have fallen off left edge
    firstLabel = self.visibleLabels[0];
    while (CGRectGetMaxX([firstLabel frame]) < minimumVisibleX)
    {
        [firstLabel removeFromSuperview];
        [self.visibleLabels removeObjectAtIndex:0];
        firstLabel = self.visibleLabels[0];
    }
}

@end
```
