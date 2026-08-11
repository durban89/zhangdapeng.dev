---
title: "iOS 6的Rotation"
date: "2025-06-23 15:27:25"
slug: "ios-6-de-rotation"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS-6的Rotation/"
  - "/2025/06/23/iOS-6的Rotation.html"
  - "/iOS-6的Rotation/"
  - "/iOS-6的Rotation.html"
  - "/2025/06/23/ios-6-de-rotation/"
  - "/2025/06/23/ios-6-de-rotation.html"
  - "/ios-6-de-rotation.html"
---
UIViewController的shouldAutorotateToInterfaceOrientation方法被deprecated。在ios6里，是使用supportedInterfaceOrientations and shouldAutorotate 2个方法来代替shouldAutorotateToInterfaceOrientation。注意：为了向后兼容iOS 4 and 5，还是需要在你的app里保留shouldAutorotateToInterfaceOrientation。

ios 4 and 5, 如果没有重写shouldAutorotateToInterfaceOrientation，那么对于iphone来讲，by default是只支持portrait，不能旋转。

 ios 6, 如果没有重写shouldAutorotate and supportedInterfaceOrientations,by default, iphone则是"可以旋转，支持非upside down的方向"，而ipad是"可以选择，支持所有方向"

举个例子;

ios 4 and 5, iphone device, 若要"可以旋转，支持非upside down的方向"，则可以在view controller里

```objectivec
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation 
{
    return (interfaceOrientation != UIDeviceOrientationPortraitUpsideDown);
}
```

ios 6, iphone device, 若要“不能旋转，只支持portait"，则可以在view controller里

```objectivec
- (BOOL)shouldAutorotate
{
    return NO;
}
```

ios 6, ipad device, 若要“可以旋转，只支持landscape"，则可以在view controller里

```objectivec
-(NSUInteger)supportedInterfaceOrientations
{
    return UIInterfaceOrientationMaskLandscape;
}

- (BOOL)shouldAutorotate
{
    return YES;
}
```

在iOS 4 and 5，都是由具体的view controller来决定对应的view的orientation设置。而在iOS 6,则是由top-most  controller来决定view的orientation设置。

举个例子：你的app的rootViewController是navigation controller "nav", 在”nav"里的stack依次是：main view -> sub view > sub sub view，而main view里有一个button会present modal view "modal view".

那么ios 4 and 5，在ipad里，如果你要上述view都仅支持横屏orientation，你需要在上面的main view, sub view, sub sub view, model view里都添加

```objectivec
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation 
{
    return (interfaceOrientation == UIInterfaceOrientationLandscapeLeft || interfaceOrientation==UIInterfaceOrientationLandscapeRight);
}
```

而对于iOS6, 由于是由top-most controller来设置orientation，因此你在main view, sub view, sub sub view里添加下面的代码是没有任何效果的，而应该是在nav controller里添加下列代码。而modal view则不是在nav container里，因此你也需要在modal view里也添加下列代码。

```objectivec
-(NSUInteger)supportedInterfaceOrientations
{
    return UIInterfaceOrientationMaskLandscape;
}

- (BOOL)shouldAutorotate
{
    return YES;
}
```

注意几点：

1，你需要自定义一个UINavigationController的子类for "nav controller"，这样才可以添加上述代码。

2，和navigation controller类似，tab controller里的各个view的orientation设置应该放在tab controller里

ios6的top-most controller决定orientation设置，导致这样一个问题：在 top-most controller里的views无法拥有不相同的orientation设置。例如：for iphone, 在nav controller里，你有main view, sub view and sub sub view，前2个都只能打竖，而sub sub view是用来播放video，可以打横打竖。那么在ios 4 and 5里可以通过在main view and sub view的shouldAutorotateToInterfaceOrientation里设置只能打竖，而在sub sub view的shouldAutorotateToInterfaceOrientation设置打竖打横即可。而在ios 6里则无法实现这种效果，因为在main view, sub view and sub sub view的orientation设置是无效的，只能够在nav controller里设置。那么你可能想着用下列代码在nav controller里控制哪个view打竖，哪个view打横

```objectivec
-(NSUInteger)supportedInterfaceOrientations
{
    if([[self topViewController] isKindOfClass:[SubSubView class]])
        return UIInterfaceOrientationMaskAllButUpsideDown;
    else
        return UIInterfaceOrientationMaskPortrait;
}
```

是的，这样可以使得在main view and sub view里无法打横，而sub sub view横竖都行。但问题来了，如果在sub sub view时打横，然后back to sub view，那么sub view是打横显示的！

目前想到的解决方法只能是把sub sub view脱离nav controller，以modal view方式来显示。这样就可以在modal view里设置打横打竖，而在nav controller里设置只打竖。

1，说了那么多，其实如果你的app的所有view的orientation的设置是统一的，那么你可以简单的在plist file里设置即可，不用添加上面的代码。而如果你添加了上面的代码，就会覆盖plist里orientation的设置。

2，iOS 6, 当view controller present时，不会call willRotateToInterfaceOrientation:duration:, willAnimateRotationToInterfaceOrientation:duration:, and didRotateFromInterfaceOrientation: methods，只有在发生rotate的时候才会call

