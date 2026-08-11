---
title: "iOS7 下操作 UIToolbar UINavigationController UINavigationBar UIBarButtonItem"
date: "2025-06-25 11:34:51"
slug: "ios7-xia-cao-zuo-uitoolbar-uinavigationcontroller-uinavigationbar-uibarbuttonitem"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS7-下操作-UIToolbar-UINavigationController-UINavigationBar-UIBarButtonItem/"
  - "/2025/06/25/iOS7-下操作-UIToolbar-UINavigationController-UINavigationBar-UIBarButtonItem.html"
  - "/iOS7-下操作-UIToolbar-UINavigationController-UINavigationBar-UIBarButtonItem/"
  - "/iOS7-下操作-UIToolbar-UINavigationController-UINavigationBar-UIBarButtonItem.html"
  - "/2025/06/25/ios7-xia-cao-zuo-uitoolbar-uinavigationcontroller-uinavigationbar-uibarbuttonitem/"
  - "/2025/06/25/ios7-xia-cao-zuo-uitoolbar-uinavigationcontroller-uinavigationbar-uibarbuttonitem.html"
  - "/ios7-xia-cao-zuo-uitoolbar-uinavigationcontroller-uinavigationbar-uibarbuttonitem.html"
---
关于UIToolbar，UINavigationController，UINavigationBar，UIBarButtonItem在ios7的使用的简单的介绍，经过搜索资料做了如下的一些汇集

----------------------------UIBarButtonItem----------------------------

1:  UIBarButtonItem 隐藏的方式

```objectivec
[self.btnPunctuation setWidth:0];
```

2:  UIBarButtonItem 获取所在父视图中的frame 相当于将 UIBarButtonItem 转换成 UIView

```objectivec
UIBarButtonItem *barButtonItem = (UIBarButtonItem *)sender;
UIView *targetView = (UIView *)[barButtonItem performSelector:@selector(view)];
```

3:设置自定义字体和 系统的self.title 保持风格完全一致.

```objectivec
UIButton *titleButton = [UIButton buttonWithType:UIButtonTypeCustom];
[titleButton setBackgroundColor:[UIColor clearColor]];
[titleButton setFrame:(CGRect){0,0,100,44}];
[titleButton setContentEdgeInsets:UIEdgeInsetsMake(-2, 0, 0, 0)];
[titleButton setTitle:@"社会活动" forState:UIControlStateNormal];
[titleButton.titleLabel setFont:[UIFont boldSystemFontOfSize:20]];
[titleButton.titleLabel setShadowOffset:(CGSize){0,-1}];
[self.navigationItem setTitleView:titleButton];
```

----------------------------UIBarButtonItem----------------------------

----------------------------UINavigationBar----------------------------

1:  修改导航控制器背景图片的方式(IOS5以上)

```objectivec
[[UINavigationBar appearance] setBackgroundImage:image forBarMetrics:UIBarMetricsDefault];
```

注: 通过appearance可以设置全局的控件初始化外观.不过在初始化成功以后,有单独样式需求亦可用同样的方法修改.

UINavigationBar的标准高度是44,在iOS7之前可以通过44+X的方式实现背景+阴影的效果.从iOS7以后就不行了.

iOS7对UINavigationBar的标准进行重新的定义,其高度可以延伸到状态栏.所以44+20的高度等于64.

而刚刚说的44+X方式不再适用于iOS7,iOS7的新规范是64+1.背景图和阴影将单独来设定,代码如下:

```objectivec
//iOS7 新背景图片设置方法 高度 必需是 64
[self.navigationController.navigationBar setBackgroundImage:[UIImage imageNamed:@"toolbar_background_iOS7Test"] forBarPosition:UIBarPositionTopAttached barMetrics:UIBarMetricsDefault];
//iOS7 阴影需单独设定 UIColor clearColor 是去掉字段 1像素阴影
[self.navigationController.navigationBar setShadowImage:[UIImage Help_imageWithColor:[UIColor clearColor]]];
```

2:为UINavigationBar设置半透明的背景效果:

```objectivec
[self.navigationController.navigationBar setTranslucent:YES];
```

注:在iOS7中 默认生成 UINavigationBar的translucent属性为YES. 自动添加遮罩模糊效果.

3:修改UINavigationBar的背景颜色(iOS7以上)

```objectivec
[[UINavigationBar appearance] setBarTintColor:[UIColor redColor]];
```

----------------------------UINavigationBar----------------------------

----------------------------UINavigationController----------------------------

1: 修改UINavigationController的高度

```objectivec
[self.navigationController.navigationBar setFrame:CGRectMake(0,20, 320, 60)];
```

2:激活 UINavigationControllerDelegate的方式

```objectivec
self.navigationController.delegate =self;
```

3:为  UINavigationController 设置 默认的  navigationBar

这里只提供一下思路:

继承:UINavigationController以后重写 如下两个方法:

```objectivec
- (id)initWithRootViewController:(UIViewController *)rootViewController
{
    self = [super initWithRootViewController:rootViewController];
    [self Base_backAction_initNavigationBar:rootViewController];
    return self;
}
-(void)pushViewController:(UIViewController *)viewController animated:(BOOL)animated
{
    [super pushViewController:viewController animated:animated];
    [self Base_backAction_initNavigationBar:viewController];
}
```

----------------------------UINavigationController----------------------------

果然使用起来还是有些变化的

