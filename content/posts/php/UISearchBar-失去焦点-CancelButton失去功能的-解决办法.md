---
title: "UISearchBar 失去焦点 CancelButton失去功能的 解决办法"
date: "2025-06-17 12:01:05"
slug: "uisearchbar-shi-qu-jiao-dian-cancelbutton-shi-qu-gong-neng-de-jie-jue-ban-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/UISearchBar-失去焦点-CancelButton失去功能的-解决办法/"
  - "/2025/06/17/UISearchBar-失去焦点-CancelButton失去功能的-解决办法.html"
  - "/UISearchBar-失去焦点-CancelButton失去功能的-解决办法/"
  - "/UISearchBar-失去焦点-CancelButton失去功能的-解决办法.html"
  - "/2025/06/17/uisearchbar-shi-qu-jiao-dian-cancelbutton-shi-qu-gong-neng-de-jie-jue-ban-fa/"
  - "/2025/06/17/uisearchbar-shi-qu-jiao-dian-cancelbutton-shi-qu-gong-neng-de-jie-jue-ban-fa.html"
  - "/uisearchbar-shi-qu-jiao-dian-cancelbutton-shi-qu-gong-neng-de-jie-jue-ban-fa.html"
---
首先要知道你是如何处理使得UISearchBar失去焦点的，那么我的办法一会你可以看一下，同时还有一个问题解决，就是如何是的CancelButton不失去操作的功能：

代码如下

```objectivec
-(void) scrollViewWillBeginDecelerating:(UIScrollView *)scrollView
{
    [self.personSearch resignFirstResponder];
    
    self.personSearch.showsCancelButton=YES;
    for(id control in [self.personSearch subviews])
    {
        if ([control isKindOfClass:[UIButton class]])
        {
            UIButton * btn =(UIButton *)control;
            [btn setTitle:@"取消" forState:UIControlStateNormal ];
            btn.enabled=YES;
        }
    }
}
```
