---
title: "iOS 修改导航栏的返回按钮的内容"
date: "2025-06-13 14:09:32"
slug: "ios-xiu-gai-dao-hang-lan-de-fan-hui-an-niu-de-nei-rong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-修改导航栏的返回按钮的内容/"
  - "/2025/06/13/iOS-修改导航栏的返回按钮的内容.html"
  - "/iOS-修改导航栏的返回按钮的内容/"
  - "/iOS-修改导航栏的返回按钮的内容.html"
  - "/2025/06/13/ios-xiu-gai-dao-hang-lan-de-fan-hui-an-niu-de-nei-rong/"
  - "/2025/06/13/ios-xiu-gai-dao-hang-lan-de-fan-hui-an-niu-de-nei-rong.html"
  - "/ios-xiu-gai-dao-hang-lan-de-fan-hui-an-niu-de-nei-rong.html"
---
如何修改导航栏的返回按钮内容，开始我也费了好久的时间最后打算自定义一个算了，结果方法还是被我找到了。

导航的返回按钮的加载原理是这样的：

1、如果B视图有一个自定义的左侧按钮（leftBarButtonItem），则会显示这个自定义按钮；  
2、如果B没有自定义按钮，但是A视图的`backBarButtonItem`属性有自定义项，则显示这个自定义项；  
3、如果前2条都没有，则默认显示一个后退按钮，后退按钮的标题是A视图的标题。  
按照这个解释，我把`UIBarButtonItem *backItem`……这段代码放在A视图的`pushViewController`语句之前。

实现过程是这样的

A视图的代码：

```objectivec
-(void) tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    NSUInteger row = [indexPath row];
    
    UIBarButtonItem *returnButtonItem = [[UIBarButtonItem alloc] init];
    returnButtonItem.title = @"返回";
    self.navigationItem.backBarButtonItem = returnButtonItem;
    
    if(row == 2)
    {
        personViewController *person = [[personViewController alloc] initWithNibName:@"personViewController" bundle:nil];
        [self.navigationController pushViewController:person animated:YES];
    }
    
    if(row == 3)
    {
        teleplayViewController *teleplay = [[teleplayViewController alloc] initWithNibName:@"teleplayViewController" bundle:nil];
        [self.navigationController pushViewController:teleplay animated:YES];
    }
}
```

注意这段代码：

```objectivec
UIBarButtonItem *returnButtonItem = [[UIBarButtonItem alloc] init];
returnButtonItem.title = @"返回";
self.navigationItem.backBarButtonItem = returnButtonItem;
```

B视图我是什么也没有做的。结果就达到你想要的效果了。

查资料的时候有一种新的方法，没有试过，先帖在这里了：

```objectivec
self.navigationController.navigationBar.topItem.title=self.message;
self.navigationController.navigationBar.tintColor=[UIColorblackColor];
UIBarButtonItem*backButton = [[UIBarButtonItemalloc] initWithTitle:@" fan hui "style:UIBarButtonItemStyleBorderedtarget:selfaction:@selector(PopViewController)];
self.navigationItem.leftBarButtonItem= backButton;
```

这个应该是贴在B视图里面（就是你要跳转到的视图）

补充

对于这段代码：

```objectivec
UIBarButtonItem *returnButtonItem = [[UIBarButtonItem alloc] init];
returnButtonItem.title = @"返回";
self.navigationItem.backBarButtonItem = returnButtonItem;
```

很好解释的，事实上也不用一定要放在我说的那里，也是可以放在 viewWillAppear里面的

```objectivec
-(void) viewWillAppear:(BOOL)animated
{
    UIBarButtonItem *returnButtonItem = [[UIBarButtonItem alloc] init];
    returnButtonItem.title = @"返回";
    self.navigationItem.backBarButtonItem = returnButtonItem;
}
```
