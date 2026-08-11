---
title: "UINavigationController pop的三个方法"
date: "2025-06-12 09:56:37"
slug: "uinavigationcontroller-pop-de-san-ge-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/UINavigationController-pop的三个方法/"
  - "/2025/06/12/UINavigationController-pop的三个方法.html"
  - "/UINavigationController-pop的三个方法/"
  - "/UINavigationController-pop的三个方法.html"
  - "/2025/06/12/uinavigationcontroller-pop-de-san-ge-fang-fa/"
  - "/2025/06/12/uinavigationcontroller-pop-de-san-ge-fang-fa.html"
  - "/uinavigationcontroller-pop-de-san-ge-fang-fa.html"
---
当我们在视图里面调用pushViewController的时候，有时间不想要这种默认的返回方式，或者也会用，但是有时候会遇到奇怪的问题，比如我就遇到了push之后没有返回按钮，或者说返回按钮消失了，不见了，因为我在rootViewController里面将navigationBar隐藏掉了，因为我想要我自己定义的navigationBar，之后在切换的视图里面就要自己定义这个但会按钮，然后给予他一个响应事件，来调用下面的类似代码，但是往往不知道返回到哪里

```objectivec
[self.navigationController popToRootViewControllerAnimated:<#(BOOL)#>]
[self.navigationController popToViewController:<#(UIViewController *)#> animated:<#(BOOL)#>]
[self.navigationController popViewControllerAnimated:<#(BOOL)#>]
```

在我的代码中，我是希望返回到到rootViewController这个视图中，那就只有调用`[self.navigationController popToRootViewControllerAnimated:<#(BOOL)#>]`

这个方法最适合了。结果达到了我想要的效果
