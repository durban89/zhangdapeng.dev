---
title: "UITabbar 相关属性设置"
date: "2025-06-25 09:57:47"
slug: "uitabbar-xiang-guan-shu-xing-she-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/UITabbar-相关属性设置/"
  - "/2025/06/25/UITabbar-相关属性设置.html"
  - "/UITabbar-相关属性设置/"
  - "/UITabbar-相关属性设置.html"
  - "/2025/06/25/uitabbar-xiang-guan-shu-xing-she-zhi/"
  - "/2025/06/25/uitabbar-xiang-guan-shu-xing-she-zhi.html"
  - "/uitabbar-xiang-guan-shu-xing-she-zhi.html"
---
背景颜色的设置

```objectivec
NSString *tabbarBackgroundImage = [[NSBundle mainBundle] pathForResource:@"bg_tabbar@2x" ofType:@"png"];
    [[UITabBar appearance] setBackgroundImage:[UIImage imageWithContentsOfFile:tabbarBackgroundImage]];
tabbar选择后的背景设置（这里由于图片的大小，做了一下图片的大小调整）

UIImage *image = [UIImage imageWithContentsOfFile:tabbarBackgroundImage];
CGSize size = CGSizeMake(20.0, 0.5);
UIImage *resizeImage = [self reSizeImage:image toSize:size];
[[UITabBar appearance] setSelectionIndicatorImage:resizeImage];
```

tabbar字体的颜色设置

```objectivec
[[UITabBarItem appearance] setTitleTextAttributes:[NSDictionary dictionaryWithObjectsAndKeys:[UIColor grayColor],UITextAttributeTextColor, nil] forState:UIControlStateNormal];
```

加一个图片重新调整的函数

```objectivec
- (UIImage *)reSizeImage:(UIImage *)image toSize:(CGSize)reSize
{
    UIGraphicsBeginImageContext(CGSizeMake(reSize.width, reSize.height));
    [image drawInRect:CGRectMake(0, 0, reSize.width, reSize.height)];
    UIImage *reSizeImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    
    return reSizeImage;
    
}
```

