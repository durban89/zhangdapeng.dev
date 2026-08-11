---
title: "UITabbar 中的 item的字体颜色 item点击后的tint颜色 和图片颜色的修改"
date: "2025-06-27 10:07:17"
slug: "uitabbar-zhong-de-item-de-zi-ti-yan-se-item-dian-ji-hou-de-tint-yan-se-he-tu-pian-yan-se-de-xiu-gai"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/UITabbar-中的-item的字体颜色-item点击后的tint颜色-和图片颜色的修改/"
  - "/2025/06/27/UITabbar-中的-item的字体颜色-item点击后的tint颜色-和图片颜色的修改.html"
  - "/UITabbar-中的-item的字体颜色-item点击后的tint颜色-和图片颜色的修改/"
  - "/UITabbar-中的-item的字体颜色-item点击后的tint颜色-和图片颜色的修改.html"
  - "/2025/06/27/uitabbar-zhong-de-item-de-zi-ti-yan-se-item-dian-ji-hou-de-tint-yan-se-he-tu-pian-yan-s/"
  - "/2025/06/27/uitabbar-zhong-de-item-de-zi-ti-yan-se-item-dian-ji-hou-de-tint-yan-se-he-tu-pian-y.html"
  - "/uitabbar-zhong-de-item-de-zi-ti-yan-se-item-dian-ji-hou-de-tint-yan-se-he-tu-pian-yan-se-de-xi.html"
---
这个问题解决了有些时候了，终于知道了办法，先看个代码

```objectivec
[[UITabBar appearance] setTintColor:[UIColor colorWithRed:0.0
                                                    green:176.0/255.0
                                                     blue:226.0/255.0
                                                    alpha:1.0]];

[[UITabBarItem appearance] setTitleTextAttributes:[NSDictionary dictionaryWithObjectsAndKeys:
                                                   [UIColor lightGrayColor], UITextAttributeTextColor, nil]
                                         forState:UIControlStateNormal];
```

UITabbar有个setTintColor这个方法，可以理解为，高亮的时候，或者点击后的颜色设置。

UITabBarItem有个setTitleTextAttributes的方法，是用来设置字体的颜色。

我这里是在viewDidLoad添加的。

代码如下：

```objectivec
//设置tabbar的背景图片
UITabBar *tabBar = self.tabBarController.tabBar;
[tabBar setTintColor:[UIColor colorWithRed:0.0
                                     green:176.0/255.0
                                      blue:226.0/255.0
                                     alpha:1.0]];
tabBar.selectedImageTintColor = [UIColor clearColor];
UITabBarItem *item = [tabBar.items objectAtIndex:0];
NSString *homePath = [[NSBundle mainBundle] pathForResource:@"btn_home_highlight" ofType:@"png"];
if(item.tag == 1)
{
    [item setTitleTextAttributes:[NSDictionary dictionaryWithObjectsAndKeys:
                                  [UIColor lightGrayColor], UITextAttributeTextColor, nil]
                        forState:UIControlStateNormal];
    item.selectedImage = [UIImage imageWithContentsOfFile:homePath];
}
```

