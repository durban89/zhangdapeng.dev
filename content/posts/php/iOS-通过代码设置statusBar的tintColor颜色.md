---
title: "iOS 通过代码设置statusBar的tintColor颜色"
date: "2025-06-13 14:07:37"
slug: "ios-tong-guo-dai-ma-she-zhi-statusbar-de-tintcolor-yan-se"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-通过代码设置statusBar的tintColor颜色/"
  - "/2025/06/13/iOS-通过代码设置statusBar的tintColor颜色.html"
  - "/iOS-通过代码设置statusBar的tintColor颜色/"
  - "/iOS-通过代码设置statusBar的tintColor颜色.html"
  - "/2025/06/13/ios-tong-guo-dai-ma-she-zhi-statusbar-de-tintcolor-yan-se/"
  - "/2025/06/13/ios-tong-guo-dai-ma-she-zhi-statusbar-de-tintcolor-yan-se.html"
  - "/ios-tong-guo-dai-ma-she-zhi-statusbar-de-tintcolor-yan-se.html"
---
在iOS6中，statusbar的颜色是由当前页面的UINavigationBar决定的，也就是当前view中的UINavigationBar决定statusbar的tintColor的。如果我们的UIViewController是UINavigationController的子集，那么就好statusbar的颜色还好设置，如果UINavigationBar被hide掉，或是根本就没有UINavigationController，那么在iOS6上statusbar的颜色就是黑色。  
如何办呢？我们如何才能在iOS6上设置statusbar的颜色？  
刚才说了，statusbar的颜色是由UINavigationBar决定的，那么我们可不可以在当前view中放一个UINavigationBar并设置其颜色，影响其statusbar的颜色。 我们的假设是正确的，这个方法的确可行。

在我们的view中放入一个UINavigationBar,并设置其`frame=CGRectMake(0, -43, 320, 44);`

在这儿y的值一定得是-43（UINavigationBar有一个像素的值）,不然一样达不到效果。

实例代码如下：

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    self.personSearch.delegate = self;
    self.dataTable.delegate = self;
    self.dataTable.dataSource = self;
    
    
    //设置状态栏的颜色为红色
    UINavigationBar *navigationBar = [[UINavigationBar alloc] initWithFrame:CGRectMake(0.0, -43.0, 320, 44)];
    navigationBar.tintColor = [UIColor redColor];
    [self.view addSubview:navigationBar];
}
```
