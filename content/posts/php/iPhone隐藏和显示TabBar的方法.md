---
title: "iPhone隐藏和显示TabBar的方法"
date: "2025-06-13 15:32:40"
slug: "iphone-yin-cang-he-xian-shi-tabbar-de-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iPhone隐藏和显示TabBar的方法/"
  - "/2025/06/13/iPhone隐藏和显示TabBar的方法.html"
  - "/iPhone隐藏和显示TabBar的方法/"
  - "/iPhone隐藏和显示TabBar的方法.html"
  - "/2025/06/13/iphone-yin-cang-he-xian-shi-tabbar-de-fang-fa/"
  - "/2025/06/13/iphone-yin-cang-he-xian-shi-tabbar-de-fang-fa.html"
  - "/iphone-yin-cang-he-xian-shi-tabbar-de-fang-fa.html"
---
关于显示和隐藏TabBar的方法，自己开始不是很懂，查找了很多的资料，在http://blog.csdn.net/riveram/article/details/7345577

这里面，有这样的描述，里面是给了两个方法：

隐藏tabbar的方法：

```objectivec
- (void)hideTabBar {
    if (self.tabBarController.tabBar.hidden == YES) {
        return;
    }
    UIView *contentView;
    if ( [[self.tabBarController.view.subviews objectAtIndex:0] isKindOfClass:[UITabBar class]] )
        contentView = [self.tabBarController.view.subviews objectAtIndex:1];
    else
        contentView = [self.tabBarController.view.subviews objectAtIndex:0];
    contentView.frame = CGRectMake(contentView.bounds.origin.x,  contentView.bounds.origin.y,  contentView.bounds.size.width, contentView.bounds.size.height + self.tabBarController.tabBar.frame.size.height);        
    self.tabBarController.tabBar.hidden = YES;
    
}
```

显示tabbar的方法：

```objectivec
- (void)showTabBar

{
    if (self.tabBarController.tabBar.hidden == NO)
    {
        return;
    }
    UIView *contentView;
    if ([[self.tabBarController.view.subviews objectAtIndex:0] isKindOfClass:[UITabBar class]])
        
        contentView = [self.tabBarController.view.subviews objectAtIndex:1];

    else
        
        contentView = [self.tabBarController.view.subviews objectAtIndex:0];      
    contentView.frame = CGRectMake(contentView.bounds.origin.x, contentView.bounds.origin.y,  contentView.bounds.size.width, contentView.bounds.size.height - self.tabBarController.tabBar.frame.size.height);
    self.tabBarController.tabBar.hidden = NO;
    
}
```

然后直接调用就好了。

另外在cocoachina的网站上，也看到了一个方法，不过只是说是隐藏的方法。

代码如下：

隐藏Tabbar

```objectivec
- (void)makeTabBarHidden:(BOOL)hide
{
    if ( [self.tabBarController.view.subviews count] < 2 )
    {
        return;
    }
    UIView *contentView;
    
    if ( [[self.tabBarController.view.subviews objectAtIndex:0] isKindOfClass:[UITabBar class]] )
    {
        contentView = [self.tabBarController.view.subviews objectAtIndex:1];
    }
    else
    {
        contentView = [self.tabBarController.view.subviews objectAtIndex:0];
    }
    //    [UIView beginAnimations:@"TabbarHide" context:nil];
    if ( hide )
    {
        contentView.frame = self.tabBarController.view.bounds;        
    }
    else
    {
        contentView.frame = CGRectMake(self.tabBarController.view.bounds.origin.x,
                                       self.tabBarController.view.bounds.origin.y,
                                       self.tabBarController.view.bounds.size.width,
                                       self.tabBarController.view.bounds.size.height - self.tabBarController.tabBar.frame.size.height);
    }
    
    self.tabBarController.tabBar.hidden = hide;
    //    [UIView commitAnimations];    
}
```

但是，有经过资料的查找，有个比较简单的方法

我在A视图的代码可参考如下：

```objectivec
-(void) viewWillAppear:(BOOL)animated
{
    
    
    //添加右侧的item
    self.rightButton = [UIButton buttonWithType:UIButtonTypeCustom];
    _rightButton.titleLabel.font = [UIFont fontWithName:@"Avenir-Book" size:14.0];
    _rightButton.contentHorizontalAlignment = UIControlContentHorizontalAlignmentLeft;
    _rightButton.contentEdgeInsets = UIEdgeInsetsMake(0.0, 2.0, 0.0, 0.0);
    [_rightButton setFrame:CGRectMake(0.0, 0.0, 60.0, 30.0)];
    NSString *arrowPath = [[NSBundle mainBundle] pathForResource:@"littleArrow" ofType:@"png"];

    [_rightButton setBackgroundImage:[UIImage imageWithContentsOfFile:arrowPath] forState:UIControlStateNormal];
    [_rightButton addTarget:self
                   action:@selector(personRoleSelect:)
         forControlEvents:UIControlEventTouchUpInside];
    
    if([_role isEqualToString:@""] || (_role == nil))
    {
        [_rightButton setTitle:@"全部" forState:UIControlStateNormal];
    }
    else
    {
        [_rightButton setTitle:[NSString stringWithFormat:@"%@",_role] forState:UIControlStateNormal];
    }
    
    
    
    [_rightButton setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
    
    UIBarButtonItem *rightItemBar = [[UIBarButtonItem alloc] initWithCustomView:_rightButton];
    self.navigationItem.rightBarButtonItem = rightItemBar;
    
    self.hidesBottomBarWhenPushed = YES;
    
    UIBarButtonItem *returnItem = [[UIBarButtonItem alloc] init];
    returnItem.title = @"返回";
    self.navigationItem.backBarButtonItem = returnItem;
}

-(void) viewWillDisappear:(BOOL)animated
{
    self.hidesBottomBarWhenPushed = NO;
    [_dropDown hideDropDown:_rightButton];
}
```

主要是这句：

`self.hidesBottomBarWhenPushed = YES;`

和

`self.hidesBottomBarWhenPushed = NO;`
