---
title: "Finishing up a navigation transition in an unexpected state"
date: "2025-06-12 17:18:35"
slug: "finishing-up-a-navigation-transition-in-an-unexpected-state"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/Finishing-up-a-navigation-transition-in-an-unexpected-state/"
  - "/2025/06/12/Finishing-up-a-navigation-transition-in-an-unexpected-state.html"
  - "/Finishing-up-a-navigation-transition-in-an-unexpected-state/"
  - "/Finishing-up-a-navigation-transition-in-an-unexpected-state.html"
  - "/2025/06/12/finishing-up-a-navigation-transition-in-an-unexpected-state/"
  - "/2025/06/12/finishing-up-a-navigation-transition-in-an-unexpected-state.html"
  - "/finishing-up-a-navigation-transition-in-an-unexpected-state.html"
---
我在做我的iOS应用中，遇到了这样的情况：错误代码如下：

```shell
2013-05-13 21:46:47.985 xunYi4[31694:c07] nested pop animation can result in corrupted navigation bar
2013-05-13 21:46:48.336 xunYi4[31694:c07] Finishing up a navigation transition in an unexpected state. Navigation Bar subview tree might get corrupted.
2013-05-13 21:46:48.337 xunYi4[31694:c07] Unbalanced calls to begin/end appearance transitions for <personViewController: 0x75a01b0>.
```

使得我的运行的结果是，在调用pushViewConroller的时候出现了两次push，导致程序不能达到自己想要的效果，于是查找资料，最终我的解决方案是：如下：

```objectivec
personViewController *person = [[personViewController alloc] initWithNibName:@"personViewController" bundle:nil];
[self.navigationController popToRootViewControllerAnimated:NO];
person.navigationItem.title = button.titleLabel.text;
[self.navigationController pushViewController:person animated:YES];
```

达到了我要的效果，但是问题是这个报错的信息还是存在，请求高手给予指点
