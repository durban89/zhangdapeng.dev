---
title: "iOS 调试 解决EXC_BAD_ACCESS错误"
date: "2025-06-11 11:27:11"
slug: "ios-tiao-shi-jie-jue-exc-bad-access-cuo-wu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-调试-解决EXC-BAD-ACCESS错误/"
  - "/2025/06/11/iOS-调试-解决EXC-BAD-ACCESS错误.html"
  - "/iOS-调试-解决EXC-BAD-ACCESS错误/"
  - "/iOS-调试-解决EXC-BAD-ACCESS错误.html"
  - "/2025/06/11/ios-tiao-shi-jie-jue-exc-bad-access-cuo-wu/"
  - "/2025/06/11/ios-tiao-shi-jie-jue-exc-bad-access-cuo-wu.html"
  - "/ios-tiao-shi-jie-jue-exc-bad-access-cuo-wu.html"
---
做iOS 程序开发时经常用遇到 EXC\_BAD\_ACCESS 错误导致 Crash，出现这种错误时一般 Xcode 不会给我们太多的信息来定位错误来源，只是在应用 Delegate 上留下像Thread 1: Program received signal:"EXC\_BAD\_ACCESS"，让问题无从找起。

比如你对已释放的对象发送消息时就会出现，EXC\_BAD\_ACCESS，再如release 的对象再 release，release 那些autorelease 的对象等也会报这样的错。默认设置下 Xcode 不会给你定位具体是哪一行代码，不该去使用已释放的对象，或者release 用错了。

比如下面这段代码：

```objectivec
- (void)drawRect:(CGRect)rect
{
    [self setClearsContextBeforeDrawing: YES];
    
    CGContextRef context = UIGraphicsGetCurrentContext();
    
    //画背景线条------------------
    CGColorRef backColorRef = [UIColor blackColor].CGColor;
    CGFloat backLineWidth = 2.f;
    CGFloat backMiterLimit = 0.f;
    
    CGContextSetLineWidth(context, backLineWidth);//主线宽度
    CGContextSetMiterLimit(context, backMiterLimit);//投影角度  
    
    CGContextSetShadowWithColor(context, CGSizeMake(3, 5), 8, backColorRef);//设置双条线 
    
    CGContextSetLineJoin(context, kCGLineJoinRound);
    
    CGContextSetLineCap(context, kCGLineCapRound );
    
    CGContextSetBlendMode(context, kCGBlendModeNormal);
    
    CGContextSetStrokeColorWithColor(context, [UIColor whiteColor].CGColor);
  
    CGFloat x = self.charW;
    CGFloat y = self.chartH;
    
    //绘制纵向的坐标线 和 值
    for (int i=0; i<vDesc.count; i++) {
        
        CGPoint bPoint = CGPointMake(30, y);
        CGPoint ePoint = CGPointMake(x, y);
        
        UILabel *label = [[UILabel alloc]initWithFrame:CGRectMake(0, 0, 30, 30)];
        //纵坐标起始点的y坐标
        //纵坐标起始点的x坐标
        int vX = 15;
        int vY = 30;
        [label setCenter:CGPointMake(bPoint.x-vX, bPoint.y-vY)];
        
        [label setTextAlignment:NSTextAlignmentCenter];
        [label setBackgroundColor:[UIColor clearColor]];
        [label setTextColor:[UIColor whiteColor]];
        [label setText:[vDesc objectAtIndex:i]];
        [self addSubview:label];
        
        CGContextMoveToPoint(context, bPoint.x, bPoint.y-30);
        CGContextAddLineToPoint(context, ePoint.x, ePoint.y-30);
        
        y -= 50;//间隔
        
    }
    
    //绘制横向的坐标线 和 值
    for (int i=0; i<array.count-1; i++) {
        //横向值的y坐标
        CGFloat hY = chartH - 20;
        UILabel *label = [[UILabel alloc]initWithFrame:CGRectMake(i*vInterval+10, hY, 60, 30)];
        label.transform = CGAffineTransformMakeRotation(0.5);
        [label setTextAlignment:NSTextAlignmentCenter];
        [label setBackgroundColor:[UIColor clearColor]];
        [label setTextColor:[UIColor whiteColor]];
        label.numberOfLines = 1;
        label.adjustsFontSizeToFitWidth = YES;
        label.minimumScaleFactor = 1.0f;
        [label setText:[hDesc objectAtIndex:i]];
        
        [self addSubview:label];
    }
    
    
    //画点线条------------------
    CGColorRef pointColorRef = [UIColor colorWithRed:24.0f/255.0f green:116.0f/255.0f blue:205.0f/255.0f alpha:1.0].CGColor;
    CGFloat pointLineWidth = 1.5f;
    CGFloat pointMiterLimit = 5.0f;
    
    CGContextSetLineWidth(context, pointLineWidth);//主线宽度
    CGContextSetMiterLimit(context, pointMiterLimit);//投影角度  
    
    
    CGContextSetShadowWithColor(context, CGSizeMake(3, 5), 8, pointColorRef);//设置双条线 
    
    CGContextSetLineJoin(context, kCGLineJoinRound);
    
    CGContextSetLineCap(context, kCGLineCapRound );
    
    CGContextSetBlendMode(context, kCGBlendModeNormal);
    
    CGContextSetStrokeColorWithColor(context, [UIColor whiteColor].CGColor);

	//绘图
	CGPoint p1 = [[array objectAtIndex:0] CGPointValue];
    //坐标的基础坐标 y值
    int yBase = chartH - 30;
	CGContextMoveToPoint(context, 30, yBase);
	for (int i = 1; i<[array count]; i++)
	{
		p1 = [[array objectAtIndex:i] CGPointValue];
        CGPoint goPoint = CGPointMake(p1.x-20, yBase-p1.y*vInterval/20);
		CGContextAddLineToPoint(context, goPoint.x, goPoint.y);;
        
        //添加触摸点
        UIButton *bt = [UIButton buttonWithType:UIButtonTypeCustom];
        
        [bt setBackgroundColor:[UIColor redColor]];
        
        [bt setFrame:CGRectMake(0, 0, 10, 10)];
        
        [bt setCenter:goPoint];
        
        [bt addTarget:self 
               action:@selector(btAction:) 
     forControlEvents:UIControlEventTouchUpInside];
        
        [self addSubview:bt];
	}
	CGContextStrokePath(context);
    
}
```

上面的代码就会出现EXC\_BAD\_ACCESS 错误：  
错误提示是：

> CoreGraphics`CGColorGetAlpha:  
> 0x31c1d780: vmov.i32d0, #0x0  
> 0x31c1d784: cmp  r0, #0  
> 0x31c1d786: itttt ne  
> 0x31c1d788: ldrne r1, [r0, #28]  
> 0x31c1d78a: addne.wr0, r0, r1, lsl #2  
> 0x31c1d78e: ldrne r0, [r0, #28]<-  
> 0x31c1d790: vmovne d0, r0, r0  
> 0x31c1d794: vmov  r0, s0  
> 0x31c1d798: bx   lr  
> 0x31c1d79a: nop

会定位到红色的那一行，这个实在是让人头痛，不过还是有解决办法的。

NSZombieEnabled环境变量可以帮我们的忙，就是当 设置NSZombieEnabled环境变量后，一个对象销毁时会被转化为\_NSZombie，设置NSZombieEnabled后，当你向一个已经释 放的对象发送消息，这个对象就不会向之前那样Crash或者产生一个难以理解的行为，而是放出一个错误消息，然后以一种可预测的可以产生debug断点的 方式消失， 因此我们就可以找到具体或者大概是哪个对象被错误的释放了。

对 Xcode 设置了NSZombieEnabled 之后，

错误提示是：

> \*\*\* -[Not A Type retain]: message sent to deallocated instance 0x2009b480

应该是内存泄露的问题。

修改代码后，代码如下：

```objectivec
- (void)drawRect:(CGRect)rect
{
    [self setClearsContextBeforeDrawing: YES];
    
    CGContextRef context = UIGraphicsGetCurrentContext();
    
    //画背景线条------------------
//    CGColorRef backColorRef = [UIColor blackColor].CGColor;
    CGColorRef backColorRef = (__bridge CGColorRef)([UIColor blackColor]);
    CGFloat backLineWidth = 2.f;
    CGFloat backMiterLimit = 0.f;
    
    CGContextSetLineWidth(context, backLineWidth);//主线宽度
    CGContextSetMiterLimit(context, backMiterLimit);//投影角度  
    
    CGContextSetShadowWithColor(context, CGSizeMake(3, 5), 8, backColorRef);//设置双条线 
    
    CGContextSetLineJoin(context, kCGLineJoinRound);
    
    CGContextSetLineCap(context, kCGLineCapRound );
    
    CGContextSetBlendMode(context, kCGBlendModeNormal);
    
    CGContextSetStrokeColorWithColor(context, [UIColor whiteColor].CGColor);
  
    CGFloat x = self.charW;
    CGFloat y = self.chartH;
    
    //绘制纵向的坐标线 和 值
    for (int i=0; i<vDesc.count; i++) {
        
        CGPoint bPoint = CGPointMake(30, y);
        CGPoint ePoint = CGPointMake(x, y);
        
        UILabel *label = [[UILabel alloc]initWithFrame:CGRectMake(0, 0, 30, 30)];
        //纵坐标起始点的y坐标
        //纵坐标起始点的x坐标
        int vX = 15;
        int vY = 30;
        [label setCenter:CGPointMake(bPoint.x-vX, bPoint.y-vY)];
        
        [label setTextAlignment:NSTextAlignmentCenter];
        [label setBackgroundColor:[UIColor clearColor]];
        [label setTextColor:[UIColor whiteColor]];
        [label setText:[vDesc objectAtIndex:i]];
        [self addSubview:label];
        
        CGContextMoveToPoint(context, bPoint.x, bPoint.y-30);
        CGContextAddLineToPoint(context, ePoint.x, ePoint.y-30);
        
        y -= 50;//间隔
        
    }
    
    //绘制横向的坐标线 和 值
    for (int i=0; i<array.count-1; i++) {
        //横向值的y坐标
        CGFloat hY = chartH - 20;
        UILabel *label = [[UILabel alloc]initWithFrame:CGRectMake(i*vInterval+10, hY, 60, 30)];
        label.transform = CGAffineTransformMakeRotation(0.5);
        [label setTextAlignment:NSTextAlignmentCenter];
        [label setBackgroundColor:[UIColor clearColor]];
        [label setTextColor:[UIColor whiteColor]];
        label.numberOfLines = 1;
        label.adjustsFontSizeToFitWidth = YES;
        label.minimumScaleFactor = 1.0f;
        [label setText:[hDesc objectAtIndex:i]];
        
        [self addSubview:label];
    }
    
    
    //画点线条------------------
//    CGColorRef pointColorRef = [UIColor colorWithRed:24.0f/255.0f green:116.0f/255.0f blue:205.0f/255.0f alpha:1.0].CGColor;
    CGColorRef pointColorRef = (__bridge CGColorRef)[UIColor colorWithRed:24.0f/255.0f green:116.0f/255.0f blue:205.0f/255.0f alpha:1.0];
    CGFloat pointLineWidth = 1.5f;
    CGFloat pointMiterLimit = 5.0f;
    
    CGContextSetLineWidth(context, pointLineWidth);//主线宽度
    CGContextSetMiterLimit(context, pointMiterLimit);//投影角度  
    
    
    CGContextSetShadowWithColor(context, CGSizeMake(3, 5), 8, pointColorRef);//设置双条线 
    
    CGContextSetLineJoin(context, kCGLineJoinRound);
    
    CGContextSetLineCap(context, kCGLineCapRound );
    
    CGContextSetBlendMode(context, kCGBlendModeNormal);
    
    CGContextSetStrokeColorWithColor(context, [UIColor whiteColor].CGColor);

	//绘图
	CGPoint p1 = [[array objectAtIndex:0] CGPointValue];
    //坐标的基础坐标 y值
    int yBase = chartH - 30;
	CGContextMoveToPoint(context, 30, yBase);
	for (int i = 1; i<[array count]; i++)
	{
		p1 = [[array objectAtIndex:i] CGPointValue];
        CGPoint goPoint = CGPointMake(p1.x-20, yBase-p1.y*vInterval/20);
		CGContextAddLineToPoint(context, goPoint.x, goPoint.y);;
        
        //添加触摸点
        UIButton *bt = [UIButton buttonWithType:UIButtonTypeCustom];
        
        [bt setBackgroundColor:[UIColor redColor]];
        
        [bt setFrame:CGRectMake(0, 0, 10, 10)];
        
        [bt setCenter:goPoint];
        
        [bt addTarget:self 
               action:@selector(btAction:) 
     forControlEvents:UIControlEventTouchUpInside];
        
        [self addSubview:bt];
	}
	CGContextStrokePath(context);
    
}
```

一切正常了。成功了！

如何设置 NSZombieEnabled 呢，在 Xcode3 和 Xcode4 下设置不一样，Xcode4 下设置很简单。

**Xcode3 下 NSZombieEnabled 设置方法如下：**  
- 在XCode左边那个Groups& Files栏中找到Executables，双击其中的一项，或者右键Get Info；  
- 切换到Arguments  
- 这里一共有两个框，在下面那个Variables to be set in theenvironment:点+号添加一项，Name里填NSZombieEnabled，Value填Yes，要保证前面的钩是选中的。  
**Xcode4 下设置 NSZombieEnabled 的方法：**  
你可以点击 Xcode4 菜单 Product -> Edit Scheme-> Arguments, 然后将点击”加号”, 将 NSZombieEnabled 参数加到Environment Variables 窗口中, 后面的数值写上 ”YES”.  
或者在 Xcode4 菜单 Product -> EditScheme -> Diagnostics 设置窗口中直接勾上Enable ZombieObjects 即可，Xcode 可用 cmd＋shift＋< 进到这个窗口。

-----------------------------  
讲Cocoa技术十分专业的网站之一，下面的链接详细讲了讲NSZombieEnable的原理。http://www.cocoadev.com/index.pl?NSZombieEnabled  
苹果官方的Mac OS X Debugging Magic,详细讲述了最为一个高级苹果程序员应该具备的调试技巧 http://developer.apple.com/library/mac/#technotes/tn2004/tn2124.html  
其实还可以在Instruments中开启NSZombie选项，这样就可以在Instruments中直接查看crash时候的callstack了：http://www.markj.net/iphone-memory-debug-nszombie/  
最后提醒NSZombieEnabled只能在调试的时候使用，千万不要忘记在产品发布的时候去掉，因为NSZombieEnabled不会真正去释放dealloc对象的内存，一直开启后果可想而知，自重！

