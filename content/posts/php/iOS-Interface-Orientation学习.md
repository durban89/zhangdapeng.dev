---
title: "iOS Interface Orientation学习"
date: "2025-06-23 15:27:33"
slug: "ios-interface-orientation-xue-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS-Interface-Orientation学习/"
  - "/2025/06/23/iOS-Interface-Orientation学习.html"
  - "/iOS-Interface-Orientation学习/"
  - "/iOS-Interface-Orientation学习.html"
  - "/2025/06/23/ios-interface-orientation-xue-xi/"
  - "/2025/06/23/ios-interface-orientation-xue-xi.html"
  - "/ios-interface-orientation-xue-xi.html"
---
### [设备方向改变通知](#1)

iOS设备内置有加速计(Accelerometer)可以检测出当前设备的方法,当设备方向改变时,系统会发送UIDeviceOrientationDidChangeNotification通知,UIKit框架会监听此通知并根据当前应用设置来自动更新用户界面方向(Interface Orientation)。

在iOS6版本中,设置应用支持的界面方向的方法和iOS5及之前的版本有差异,下面将分别介绍两个版本下的界面方向设置。


### [iOS6中设置支持的界面方向(Interface Orientations)](#2)

在iOS6中,UIKit框架接收到方向改变的通知时,会使用UIApplication的全局设置和当前topmost view controller的设置来共同判断是否允许旋转至此方向。

1,[Info.plist](http://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247)中的[UISupportedInterfaceOrientations](http://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW10)

设置Info.plist中的[UISupportedInterfaceOrientations](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW10)对应的数组可控制app全局支持的方向，此设置对app的所有view controller都有效。使用当前topmost view controller支持的方向与此设置的与(AND)来确定给定的方向是否支持。与操作的结果不能为0，若为0，则会引发[UIApplicationInvalidInterfaceOrientationException](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/c/data/UIApplicationInvalidInterfaceOrientationException)异常。

2,Topmost view controller支持的方向

1. Topmost view controller是什么?

   **Important**: Here, the topmost view controller refers to the window’s root view controller unless another view controller is currently presented, in which case, the presented view controller becomes the topmost view controller for the duration it is presented. This should not be confused with the topViewController of a navigation controller.

   如Technical Q&A QA1688中所述，topmost view controller有两类:

   a. window的root view controller(当没有其他view controller正在被presented时);

   b. 当前正在被presented显示的其他view controller。

   查找当前topmost view controller的代码为:

   ```objectivec
   +(UIViewController*) topMostController
   {
       UIViewController*topController =[UIApplication sharedApplication].keyWindow.rootViewController;

       while(topController.presentedViewController){
           topController = topController.presentedViewController;
       }

       return topController;
   }
   ```

   注(重要):要使iOS6中的方向旋转相关的方法生效,必须设置window的rootViewController属性,而不能简单的将root view controller的view加入到window中。
2. UIViewController的方向设置(topmost view controller)

   a.[supportedInterfaceOrientations](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/occ/instm/UIViewController/supportedInterfaceOrientations)    设置view controller支持的界面方向(Interface Orientations)

   可以通过重写UIViewController的supportedInterfaceOrientations方法来确定当前view controller支持的Interface Orientation。默认情况下,iPad支持所有四个方向,iPhone支持除[UIInterfaceOrientationPortraitUpsideDown](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40006728-CH3-SW5)以外的三个方向。下面为设置支持portrait方法和 landscape-left方向的代码。

   ```objectivec
   - (NSUInteger)supportedInterfaceOrientations
   {
       return UIInterfaceOrientationMaskPortrait | UIInterfaceOrientationMaskLandscapeLeft;
   }
   ```

   b. [shouldAutorotate](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/occ/instm/UIViewController/shouldAutorotate)    设置是否允许自动旋转

   如果想暂时禁掉自动旋转,但不想修改supportedInterfaceOrientations中的方向mask,可重写shouldAutorotate方法,如果shouldAutorotate返回NO,则不进行旋转。

   c. [preferredInterfaceOrientationForPresentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/occ/instm/UIViewController/preferredInterfaceOrientationForPresentation)    设置View Controller被Presented时的首选显示方向。

   当view controller被presented显示时，可能在一个特定的方向显示最合适,如果其仅仅支持这一个方向，可以在supportedInterfaceOrientations方法中简单的返回此方向。但如果view controller支持多个方向显示,但在某一个方向显示最佳,则可以通过重写preferredInterfaceOrientationForPresentation方法来返回此方向。这样,当view controller被presented时,将会以preferredInterfaceOrientationForPresentation返回的方向显示。<\br>  
    注意:preferredInterfaceOrientationForPresentation返回的方向是supportedInterfaceOrientations中的一个。
 

### [iOS5及之前版本中设置支持的界面方向(Interface Orientations)](#3)

1.Info.plist中的UISupportedInterfaceOrientations

    与iOS6版本不同,iOS5版本中的UISupportedInterfaceOrientations对应的方向数组仅仅作为提示,不参与能否旋转至特定方向的判断

2.shouldAutorotateToInterfaceOrientation:

    默认情况下，此方法只对UIInterfaceOrientationPortrait返回YES，如果view controller需要支持其他方向，则需要重写此方法，对支持的方向返回YES。

当对容器类view controller(container view controller)，比如UINavigationController，UITabBarController调用shouldAutorotateToInterfaceOrientation:方法时，其会对所有的子view controller调用同样的方法，如果子view controller不支持参数中指定的方法，同样返回NO。所以，在iOS5中，如果topmost view controller是个container view controller，则其子view controllers同样会参与旋转方向的判断。

    为了尽量遵循和iOS6一致的策略,应该在同时支持iOS5中的应用中做如下设置

    1,对topmost view controller，仅返回其所支持的界面方向

    2,在子view controller中，支持所有的界面方向，并合理设置自适应的view layout来支持不同的页面分辨率

### [界面方向旋转过程](#4)

当旋转发生时，在旋转的各个阶段对会调用topmost view controller中合适的方法，若topmost view controller是个container view controller，则会继续调用当前可见的子view controller中的对应方法。view contoller可以在这些方法中隐藏或者显示视图，调整视图的位置或者大小，或者将方向变化通知给app的其它部分。因为这些方法在旋转的过程中调用，所有不能做任何耗时操作。应该避免在这些方法中替换整个view 架构。

相关方法的调用顺序为:

1. window调用view controller的willRotateToInterfaceOrientation:duration:方法  
     
    在此方法中,所有调整都还未进行。view的bounds,view controller的interfaceOrientation以及UIApplication的statusBarOrientation都为原来的值；可在此方法中隐藏视图或者做其他view布局的改变。
2. window改变view的bounds。改变view的bounds会引发下面一系列操作(假定未使用autolayout):

   注:viewWillLayoutSubviews，viewDidLayoutSubviews方法在iOS5.0引入。

           a. view及其子views根据自身的autoresizing掩码设置重新调整大小。

           b. 调用view controller的viewWillLayoutSubviews方法。  
            在此方法运行时,view的bounds、view controller的interfaceOrientation以及UIApplication的statusBarOrientation都已经更新为新值。

           c. 调用view的layoutsubviews方法。

           d. 调用view controlelr的viewDidLayoutSubviews方法。
3. 调用view controller的willAnimateRotationToInterfaceOrientation:duration:方法。

   此方法在动画块（animation block）中被调用，所以在此方法中的属性改变也参与到旋转动画中。
4. 旋转动画终止。
5. 调用view controller的didRotateFromInterfaceOrientation: 方法通知旋转动画已终止。

### [隐藏view controller的界面旋转](#5)

若旋转发生时,view controller的内容没有显示在屏幕上(比如present了一个全屏view controller)，则此view controller不会收到上述的旋转消息。当此view controller重新显示时,其view会被调整位置和大小以适应新的界面方法，其过程如上述中的步骤2。

### [横屏竖屏使用不同的ViewController](#6)

如果一个页面在横屏和竖屏数据显示方式差别很大,可以使用两个单独的view controllers，一个使用竖屏显示，另一个使用横屏显示。使用两个view controllers与每次选择都调整整个view架构相比简单而且效率高。

其实现方式如下:

1. 实现两个view controller对象,一个做竖屏显示布局，另一个做横屏显示布局。按照本文前面所述方法设置每个view controller只支持特定的一种界面方向，以防止在设备旋转时，view controller内部自行做旋转操作。
2. 主view controller(通常为竖屏的那个)注册

   接收UIDeviceOrientationDidChangeNotification通知，在通知的处理方法中，根据当前的设备方向presen或dismiss另一个view controller。

   参考代码如下:

   ```objectivec
   @implementation PortraitViewController
   {
       BOOL isShowingLandscapeView;
       LandscapeViewController *landscapeViewController;
   }
   - (id)init
   {
       self = [super init];
       if (self) {
           landscapeViewController = [[LandscapeViewController alloc]init];

           [[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];
           [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(orientationChanged:) name:UIDeviceOrientationDidChangeNotification object:nil];
       }
       return self;
   }

   -(void)orientationChanged:(NSNotification *)notification
   {
       UIDeviceOrientation deviceOrientation = [UIDevice currentDevice].orientation;
       if (UIDeviceOrientationIsLandscape(deviceOrientation) && !isShowingLandscapeView) {
           [self presentModalViewController:landscapeViewController animated:YES];
           isShowingLandscapeView = YES;
       }else if(UIDeviceOrientationIsPortrait(deviceOrientation) && isShowingLandscapeView){
           [self dismissModalViewControllerAnimated:YES];
           isShowingLandscapeView = NO;
       }
   }

   -(NSUInteger)supportedInterfaceOrientations
   {
       return UIInterfaceOrientationMaskPortrait;
   }

   -(BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation
   {
       if (UIInterfaceOrientationIsPortrait(toInterfaceOrientation)) {
           return YES;
       }
       return NO;
   }

   ...
   @end

   @implementation LandscapeViewController

   - (id)init
   {
       self = [super init];
       if (self) {
          self.modalTransitionStyle = UIModalTransitionStyleCrossDissolve;
       }
       return self;
   }

   -(NSUInteger)supportedInterfaceOrientations
   {
       return UIInterfaceOrientationMaskLandscape;
   }

   -(BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation
   {
       if (UIInterfaceOrientationIsLandscape(toInterfaceOrientation)) {
           return YES;
       }
       return NO;
   }

   ...
   @end
   ```

### [Contrainer View controller与设备旋转](#7)

Container View Controller在设备旋转的过程中扮演重要的角色。在iOS5旋转方向判断时,Container View Controller会调用子View controller的shouldAutorotateToInterfaceOrientation:方法，判断是否支持某一方向。在界面旋转的过程中,Container View Controller会调用当前正在显示的子View Controllers的[willRotateToInterfaceOrientation:duration:](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewController_Class/Reference/Reference.html#//apple_ref/occ/instm/UIViewController/willRotateToInterfaceOrientation:duration:)等一系列方法。

对于系统定义的Container View Controller，如UINavigationController,UITabBarViewController，上述过程是自动进行的。对于自定义的Container View Controller，则在添加/删除child view controllers时要做合适的处理,以保证相关消息的正确分发。

1. 向container View Controller增加child view controller

   ```objectivec
   - (void) displayContentController: (UIViewController*) content;
   {
      [self addChildViewController:content];                 // 1
      content.view.frame = [self frameForContentController]; // 2
      [self.view addSubview:self.currentClientView];
      [content didMoveToParentViewController:self];          // 3
   }
   ```

   1.调用container的addChildViewController:方法添加child，调用addChildViewController:会自动调用child的willMoveToParentViewController:方法。  
     
    2.修改child view的frame，并将其加入到container的view架构中。  
     
    3.调用child的 didMoveToParentViewController:方法通知操作已结束。
2. 从container View Controller移除child view controller

   ```objectivec
   - (void) hideContentController: (UIViewController*) content
   {
      [content willMoveToParentViewController:nil];  // 1
      [content.view removeFromSuperview];            // 2
      [content removeFromParentViewController];      // 3
   }
   ```

   1.调用child的willMoveToParentViewController:，传递参数为nil，告知其将被移除。  
     
    2.将child的view从container的view架构中移出。  
     
    3.调用child的removeFromParentViewController的方法,调用此方法会自动调用child的didMoveToParentViewController:方法。
3. 在两个child view controllers之间切换,综合上面两个步骤

   ```objectivec
   - (void) cycleFromViewController: (UIViewController*) oldC
               toViewController: (UIViewController*) newC
   {
       [oldC willMoveToParentViewController:nil];                        // 1
       [self addChildViewController:newC];

       newC.view.frame = [self newViewStartFrame];                       // 2
       CGRect endFrame = [self oldViewEndFrame];

       [self transitionFromViewController: oldC toViewController: newC   // 3
             duration: 0.25 options:0
             animations:^{
                newC.view.frame = oldC.view.frame;                       // 4
                oldC.view.frame = endFrame;
              }
              completion:^(BOOL finished) {
                [oldC removeFromParentViewController];                   // 5
                [newC didMoveToParentViewController:self];
               }];
   }
   ```

   如果不想container自动转发rotation事件给child,则可重写shouldAutomaticallyForwardRotationMethods返回NO,然后在合适的时机手动调用child的willRotateToInterfaceOrientation:duration:等方法。

**附加:枚举常量定义**

获取当前方向的三个方法

```objectivec
UIViewController的interfaceOrientation;
[[UIApplication sharedApplication] statusBarOrientation];
[[UIDevice currentDevice] orientation];
```

UIDeviceOrientation定义

```objectivec
typedef enum {
  UIDeviceOrientationUnknown,
  UIDeviceOrientationPortrait,
  UIDeviceOrientationPortraitUpsideDown,
  UIDeviceOrientationLandscapeLeft,
  UIDeviceOrientationLandscapeRight,
  UIDeviceOrientationFaceUp,
  UIDeviceOrientationFaceDown
} UIDeviceOrientation;
```

UIInterfaceOrientation定义

```objectivec
typedef enum {
  UIInterfaceOrientationPortrait           = UIDeviceOrientationPortrait,
  UIInterfaceOrientationPortraitUpsideDown = UIDeviceOrientationPortraitUpsideDown,
  UIInterfaceOrientationLandscapeLeft      = UIDeviceOrientationLandscapeRight,
  UIInterfaceOrientationLandscapeRight     = UIDeviceOrientationLandscapeLeft
} UIInterfaceOrientation;
```

注意:UIInterfaceOrientationLandscapeLeft定义为UIDeviceOrientationLandscapeRight，UIInterfaceOrientationLandscapeRight定义为UIDeviceOrientationLandscapeLeft，两者是相反的。

UIInterfaceOrientationMask定义

```objectivec
typedef enum {
  UIInterfaceOrientationMaskPortrait = (1 << UIInterfaceOrientationPortrait),
  UIInterfaceOrientationMaskLandscapeLeft = (1 << UIInterfaceOrientationLandscapeLeft),
  UIInterfaceOrientationMaskLandscapeRight = (1 << UIInterfaceOrientationLandscapeRight),
  UIInterfaceOrientationMaskPortraitUpsideDown = (1 << UIInterfaceOrientationPortraitUpsideDown),
  UIInterfaceOrientationMaskLandscape =
  (UIInterfaceOrientationMaskLandscapeLeft | UIInterfaceOrientationMaskLandscapeRight),
  UIInterfaceOrientationMaskAll =
  (UIInterfaceOrientationMaskPortrait | UIInterfaceOrientationMaskLandscapeLeft |
  UIInterfaceOrientationMaskLandscapeRight | UIInterfaceOrientationMaskPortraitUpsideDown),
  UIInterfaceOrientationMaskAllButUpsideDown =
  (UIInterfaceOrientationMaskPortrait | UIInterfaceOrientationMaskLandscapeLeft |
  UIInterfaceOrientationMaskLandscapeRight),
} UIInterfaceOrientationMask;
```

