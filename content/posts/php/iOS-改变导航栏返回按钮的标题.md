---
title: "iOS 改变导航栏返回按钮的标题"
date: "2025-06-12 17:18:22"
slug: "ios-gai-bian-dao-hang-lan-fan-hui-an-niu-de-biao-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-改变导航栏返回按钮的标题/"
  - "/2025/06/12/iOS-改变导航栏返回按钮的标题.html"
  - "/iOS-改变导航栏返回按钮的标题/"
  - "/iOS-改变导航栏返回按钮的标题.html"
  - "/2025/06/12/ios-gai-bian-dao-hang-lan-fan-hui-an-niu-de-biao-ti/"
  - "/2025/06/12/ios-gai-bian-dao-hang-lan-fan-hui-an-niu-de-biao-ti.html"
  - "/ios-gai-bian-dao-hang-lan-fan-hui-an-niu-de-biao-ti.html"
---
新写的App中需要使用UINavigationController对各个页面进行导航，但由于第一级页面的title较长，在进入第二级页面后返回按钮leftButtonItem的title就会变得很长，对NavigationBar空间占用很大，而且不美观，于是使用代码对leftButtonItem的title文本进行修改，无论是设置`self.navigationItem.leftBarButtonItem.title = @"返回";`还是`self.navigationItem.backBarButtonItem.title = @"返回";`都没有效果，title文本始终不会发生变化。到网上乱搜一通后，得到了以下解决方法，相对来说比较简单，特记录如下：

在第一级页面的viewDidLoad方法中加入以下代码：

```objectivec
UIBarButtonItem *backButtonItem = [[UIBarButtonItem alloc] init];
backButtonItem.title = @"返回";
self.navigationItem.backBarButtonItem = backButtonItem;
```

也就是用一个新的按钮在进行导航前将原来的返回按钮替换掉就可以了。  
可以如下设置 但是这样的缺点是那个按键会变成方形 可以添加图片来进行修改。

```objectivec
UIBarButtonItem *backButton = [[UIBarButtonItem alloc] initWithTitle:@"Back"
                                                                   style:UIBarButtonItemStyleBordered
                                                                  target:self
                                                                  action:@selector(backToPrevious)];
    
self.navigationItem.leftBarButtonItem = backButton;

- (void)backToPrevious
{
    [self.navigationController popViewControllerAnimated:YES];
}
```

添加图片的相关代码如下

```objectivec
UIButton *leftButton = [[UIButtonalloc] initWithFrame:CGRectMake(0, 0, 60, 40)];
[leftButton setTitle:@"返回"forState:UIControlStateNormal];
[leftButton setImage:[UIImageimageNamed:@"UINavigationBar.png"] forState:UIControlStateNormal];
[leftButton setImage:[UIImageimageNamed:@"UINavigationBar.png"] forState:UIControlStateHighlighted];
[leftButton addTarget:selfaction:@selector(leftAction:) forControlEvents:UIControlEventTouchUpInside];
UIBarButtonItem *leftItem = [[UIBarButtonItemalloc] initWithCustomView:leftButton];
[leftButton release];
self.navigationItem.leftBarButtonItem = leftItem;
```
