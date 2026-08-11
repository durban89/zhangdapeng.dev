---
title: "iOS 5中定制Tabbar很简单，如何让选中的Tab显示不同图片"
date: "2025-06-25 09:57:45"
slug: "ios-5-zhong-ding-zhi-tabbar-hen-jian-dan-ru-he-rang-xuan-zhong-de-tab-xian-shi-bu-tong-tu-pian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS-5中定制Tabbar很简单，如何让选中的Tab显示不同图片/"
  - "/2025/06/25/iOS-5中定制Tabbar很简单，如何让选中的Tab显示不同图片.html"
  - "/iOS-5中定制Tabbar很简单，如何让选中的Tab显示不同图片/"
  - "/iOS-5中定制Tabbar很简单，如何让选中的Tab显示不同图片.html"
  - "/2025/06/25/iOS-5中定制Tabbar很简单-如何让选中的Tab显示不同图片/"
  - "/2025/06/25/iOS-5中定制Tabbar很简单-如何让选中的Tab显示不同图片.html"
  - "/2025/06/25/ios-5-zhong-ding-zhi-tabbar-hen-jian-dan-ru-he-rang-xuan-zhong-de-tab-xian-shi-bu-tong-/"
  - "/2025/06/25/ios-5-zhong-ding-zhi-tabbar-hen-jian-dan-ru-he-rang-xuan-zhong-de-tab-xian-shi-bu-t.html"
  - "/ios-5-zhong-ding-zhi-tabbar-hen-jian-dan-ru-he-rang-xuan-zhong-de-tab-xian-shi-bu-tong-tu-pian.html"
---
第一步：获取tabbar

```objectivec
UITabBar *tabBar = self.tabBarController.tabBar;
```

第二步：获取tababr的所有选项

```objectivec
UITabBarItem *item = [tabBar.items objectAtIndex:0];
```

第三步：设置图片，选择要设置的tabbaritem

```objectivec
NSString *homePath = [[NSBundle mainBundle] pathForResource:@"btn_home_highlight@2x" ofType:@"png"];
if(item.tag == 1)
{
    item.selectedImage = [UIImage imageWithContentsOfFile:homePath];
}
```

这个就搞定了
