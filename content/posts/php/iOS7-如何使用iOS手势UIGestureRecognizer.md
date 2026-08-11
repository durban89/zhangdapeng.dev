---
title: "iOS7 如何使用iOS手势UIGestureRecognizer"
date: "2025-06-25 11:35:12"
slug: "ios7-ru-he-shi-yong-ios-shou-shi-uigesturerecognizer"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS7-如何使用iOS手势UIGestureRecognizer/"
  - "/2025/06/25/iOS7-如何使用iOS手势UIGestureRecognizer.html"
  - "/iOS7-如何使用iOS手势UIGestureRecognizer/"
  - "/iOS7-如何使用iOS手势UIGestureRecognizer.html"
  - "/2025/06/25/ios7-ru-he-shi-yong-ios-shou-shi-uigesturerecognizer/"
  - "/2025/06/25/ios7-ru-he-shi-yong-ios-shou-shi-uigesturerecognizer.html"
  - "/ios7-ru-he-shi-yong-ios-shou-shi-uigesturerecognizer.html"
---
今天终于有时间接触了UIGestureRecognizer，果然很好玩，下面关于他的一些使用，以下内容完全来自于网上，尚未做过测试。

UIKit中包含了UIGestureRecognizer类，用于检测发生在设备中的手势。UIGestureRecognizer是一个抽象类，定义了所有手势的基本行为，它有下面一些子类用于处理具体的手势：

* 拍击UITapGestureRecognizer (任意次数的拍击)
* 向里或向外捏UIPinchGestureRecognizer (用于缩放)
* 摇动或者拖拽UIPanGestureRecognizer
* 滑动UISwipeGestureRecognizer (以任意方向)
* 旋转UIRotationGestureRecognizer (手指朝相反方向移动)
* 长按UILongPressGestureRecognizer

对于不同类型的手势识别器，具有不同的配置属性。比如UITapGestureRecognizer，可以配置拍击次数。界面接收到手势之后，可以发送一 个消息，用于处理响应手势动作后的任务。当然，不同的手势识别器，发送的消息方法也会有所不同。下面列举几个具体示例代码：

一个手指，拍击两次手势

```objectivec
// 创建一个手势识别器
UITapGestureRecognizer *oneFingerTwoTaps =
[[[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(oneFingerTwoTaps)] autorelease];
// Set required taps and number of touches
[oneFingerTwoTaps setNumberOfTapsRequired:2];
[oneFingerTwoTaps setNumberOfTouchesRequired:1];
// Add the gesture to the view
[[self view] addGestureRecognizer:oneFingerTwoTaps];
消息方法oneFingerTwoTaps
- (void)oneFingerTwoTaps
{
    NSLog(@"Action: One finger, two taps");
}
```

两个手指，拍击两次手势

```objectivec
UITapGestureRecognizer *twoFingersTwoTaps =
[[[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(twoFingersTwoTaps)] autorelease];
[twoFingersTwoTaps setNumberOfTapsRequired:2];
[twoFingersTwoTaps setNumberOfTouchesRequired:2];
[[self view] addGestureRecognizer:twoFingersTwoTaps];
消息方法twoFingersTwoTaps
- (void)twoFingersTwoTaps {
    NSLog(@"Action: Two fingers, two taps");
}
```

一个手指向上、向下滑动手势

```objectivec
// 向上滑动
UISwipeGestureRecognizer *oneFingerSwipeUp =
[[[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(oneFingerSwipeUp:)] autorelease];
[oneFingerSwipeUp setDirection:UISwipeGestureRecognizerDirectionUp];
[[self view] addGestureRecognizer:oneFingerSwipeUp];
- (void)oneFingerSwipeUp:(UISwipeGestureRecognizer *)recognizer
{
    CGPoint point = [recognizer locationInView:[self view]];
    NSLog(@"Swipe up - start location: %f,%f", point.x, point.y);
}
// 向下滑动
UISwipeGestureRecognizer *oneFingerSwipeDown =
[[[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(oneFingerSwipeDown:)] autorelease];
[oneFingerSwipeDown setDirection:UISwipeGestureRecognizerDirectionDown];
[[self view] addGestureRecognizer:oneFingerSwipeDown];
- (void)oneFingerSwipeDown:(UISwipeGestureRecognizer *)recognizer
{
    CGPoint point = [recognizer locationInView:[self view]];
    NSLog(@"Swipe down - start location: %f,%f", point.x, point.y);
}
```

旋转手势

```objectivec
UIRotationGestureRecognizer *twoFingersRotate =
[[[UIRotationGestureRecognizer alloc] initWithTarget:self action:@selector(twoFingersRotate:)] autorelease];
[[self view] addGestureRecognizer:twoFingersRotate];
- (void)twoFingersRotate:(UIRotationGestureRecognizer *)recognizer
{
    // Convert the radian value to show the degree of rotation
    NSLog(@"Rotation in degrees since last change: %f", [recognizer rotation] * (180 / M_PI));
}
```

向里或向外捏的手势

```objectivec
UIPinchGestureRecognizer *twoFingerPinch =
[[[UIPinchGestureRecognizer alloc] initWithTarget:self action:@selector(twoFingerPinch:)] autorelease];
[[self view] addGestureRecognizer:twoFingerPinch];
- (void)twoFingerPinch:(UIPinchGestureRecognizer *)recognizer
{
    NSLog(@"Pinch scale: %f", recognizer.scale);
}
```

```objectivec
UITapGestureRecognizer *twoFingersTwoTaps =
[[[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(twoFingersTwoTaps)] autorelease];
[twoFingersTwoTaps setNumberOfTapsRequired:2];
[twoFingersTwoTaps setNumberOfTouchesRequired:2];
[[self view] addGestureRecognizer:twoFingersTwoTaps];
// 消息方法twoFingersTwoTaps
- (void)twoFingersTwoTaps {
    NSLog(@"Action: Two fingers, two taps");
}
```

参考文章：

* <http://www.cnblogs.com/y041039/archive/2012/07/11/2586629.html>
* <http://www.cocoachina.com/newbie/basic/2012/0604/4322.html>

