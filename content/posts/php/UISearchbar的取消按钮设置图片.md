---
title: "UISearchbar的取消按钮设置图片"
date: "2025-06-13 10:13:20"
slug: "uisearchbar-de-qu-xiao-an-niu-she-zhi-tu-pian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/UISearchbar的取消按钮设置图片/"
  - "/2025/06/13/UISearchbar的取消按钮设置图片.html"
  - "/UISearchbar的取消按钮设置图片/"
  - "/UISearchbar的取消按钮设置图片.html"
  - "/2025/06/13/uisearchbar-de-qu-xiao-an-niu-she-zhi-tu-pian/"
  - "/2025/06/13/uisearchbar-de-qu-xiao-an-niu-she-zhi-tu-pian.html"
  - "/uisearchbar-de-qu-xiao-an-niu-she-zhi-tu-pian.html"
---
网上找了好多关于给UISearchBar的取消按钮设置图片的文章，结果就是给力一段代码，让人迷迷糊糊，不知道该放在哪里，我经过测试是这样的

一般你会搜到这样的代码段：

```objectivec
for (UIView *searchbuttons in searchBar.subviews)
{
	if ([searchbuttons isKindOfClass:[UIButton class]])
	{
	    UIButton *cancelButton = (UIButton*)searchbuttons;
	    cancelButton.enabled = YES;
	    [cancelButton setBackgroundImage:[UIImage imageNamed:@"yourImageName"] forState:UIControlStateNormal];
	    break;
	}
}
```

我这里修改了上述代码，并放在了具体的方法中：

```objectivec
//--------------------------------
//开始搜搜
//--------------------------------
-(BOOL) searchBarShouldBeginEditing:(UISearchBar *)searchBar{
    [self.searchBar setShowsCancelButton:YES];
    for (UIView *searchbuttons in self.searchBar.subviews)
    {
        if ([searchbuttons isKindOfClass:[UIButton class]])
        {
            UIButton *cancelButton = (UIButton*)searchbuttons;
            cancelButton.enabled = YES;
            NSString *path = [[NSBundle mainBundle] pathForResource:@"GUI_cancel_search" ofType:@"png"];
            [cancelButton setBackgroundImage:[UIImage imageWithContentsOfFile:path] forState:UIControlStateNormal];
            break;
        }
    }
    
    return YES;
}
```

因为我这里要执行的操作是，在进行搜索的时候将取消按钮显示出来，这样的话我就只有在这里进行操作了，经过测试绝对是可以执行的。另外这里有一个点就是，我没有使用UIImage的imageNamed方法，因为会有点小问题，你可以去看我的一篇文章[UIImage中imageNamed的使用注意](https://www.gowhich.com/blog/142)
