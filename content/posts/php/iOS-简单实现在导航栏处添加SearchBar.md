---
title: "iOS 简单实现在导航栏处添加SearchBar"
date: "2025-06-25 09:58:04"
slug: "ios-jian-dan-shi-xian-zai-dao-hang-lan-chu-tian-jia-searchbar"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS-简单实现在导航栏处添加SearchBar/"
  - "/2025/06/25/iOS-简单实现在导航栏处添加SearchBar.html"
  - "/iOS-简单实现在导航栏处添加SearchBar/"
  - "/iOS-简单实现在导航栏处添加SearchBar.html"
  - "/2025/06/25/ios-jian-dan-shi-xian-zai-dao-hang-lan-chu-tian-jia-searchbar/"
  - "/2025/06/25/ios-jian-dan-shi-xian-zai-dao-hang-lan-chu-tian-jia-searchbar.html"
  - "/ios-jian-dan-shi-xian-zai-dao-hang-lan-chu-tian-jia-searchbar.html"
---
导航栏出添加搜索框，应该是大多数app应用中需要使用的，这里简单展示一下添加的方法

```objectivec
CGRect mainViewBounds = self.navigationController.view.bounds;
customSearchBar = [[UISearchBar alloc] initWithFrame:CGRectMake(CGRectGetMinX(mainViewBounds),
                                                            CGRectGetMinY(mainViewBounds) + 44.0,
                                                            self.navigationController.view.bounds.size.width,
                                                            40)];
customSearchBar.delegate = self;
customSearchBar.showsCancelButton = YES;
[self.navigationController.view addSubview: customSearchBar];
CGRect viewBounds = self.navigationController.view.bounds;
[self.view setFrame:CGRectMake(CGRectGetMinX(viewBounds),
                               CGRectGetMinY(viewBounds) + 40,
                               CGRectGetWidth(viewBounds),
                               CGRectGetHeight(viewBounds) - 128)];
```

