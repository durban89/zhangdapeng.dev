---
title: "iOS 为UINavigationBar设置背景图片"
date: "2025-06-25 09:58:07"
slug: "ios-wei-uinavigationbar-she-zhi-bei-jing-tu-pian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS-为UINavigationBar设置背景图片/"
  - "/2025/06/25/iOS-为UINavigationBar设置背景图片.html"
  - "/iOS-为UINavigationBar设置背景图片/"
  - "/iOS-为UINavigationBar设置背景图片.html"
  - "/2025/06/25/ios-wei-uinavigationbar-she-zhi-bei-jing-tu-pian/"
  - "/2025/06/25/ios-wei-uinavigationbar-she-zhi-bei-jing-tu-pian.html"
  - "/ios-wei-uinavigationbar-she-zhi-bei-jing-tu-pian.html"
---
ios开发中，对于如何设置UINavigationBar的背景图片的设置，我搜索到了如下的一些代码

***第一种方法：针对局部NavigationBar进行背景更改的方法：***

```objectivec
float version = [[[UIDevice currentDevice] systemVersion] floatValue];
UIImage *backgroundImage = [UIImage imageNamed:@"myBackgroundImage.png"];
if (version >= 5.0) {
    [self.navigationController.navigationBar setBackgroundImage:backgroundImage forBarMetrics:UIBarMetricsDefault];
}
else
{
    [self.navigationController.navigationBar insertSubview:[[[UIImageView alloc] initWithImage:backgroundImage] autorelease] atIndex:1];
}
```

***第二种方法：全局更改NavigationBar背景的方法:***

```objectivec
- (UIImage *)barBackground
{
    return [UIImage imageNamed:@"topNavigationBar.png"];
}
- (void)didMoveToSuperview
{
    //iOS5 only
    if ([self respondsToSelector:@selector(setBackgroundImage:forBarMetrics:)])
    {
        [self setBackgroundImage:[self barBackground] forBarMetrics:UIBarMetricsDefault];
    }
}
//this doesn't work on iOS5 but is needed for iOS4 and earlier
- (void)drawRect:(CGRect)rect
{
    //draw image
    [[self barBackground] drawInRect:rect];
}
@end
```

在iPhone开发中, 有时候我们想给导航条添加背景图片, 实现多样化的导航条效果, 用其他方法往往无法达到理想的效果, 经过网上搜索及多次实验, 确定如下最佳实现方案:

***第三种方法：为UINavigatonBar增加如下Category:***

```objectivec
@implementation UINavigationBar (CustomImage)
- (void)drawRect:(CGRect)rect {
UIImage *image = [UIImage imageNamed: @"NavigationBar.png"];
[image drawInRect:CGRectMake(0, 0, self.frame.size.width, self.frame.size.height)];
}
@end
```

例如, 在我的项目中, 添加如下代码:

```objectivec
/* input: The image and a tag to later identify the view */
@implementation UINavigationBar (CustomImage)
- (void)drawRect:(CGRect)rect {
UIImage *image = [UIImage imageNamed: @"title_bg.png"];
[image drawInRect:CGRectMake(0, 0, self.frame.size.width, self.frame.size.height)];
}
@end
@implementation FriendsPageViewController
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
self.navigationBar.tintColor = [UIColor purpleColor];
[self initWithRootViewController:[[RegPageViewController alloc] init]];
    [super viewDidLoad];
}
```

