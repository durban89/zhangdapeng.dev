---
title: "让UISearchBar上英文Cancel变成中文的正确方法(改变搜索按钮文字)"
date: "2025-06-12 09:56:51"
slug: "rang-uisearchbar-shang-ying-wen-cancel-bian-cheng-zhong-wen-de-zheng-que-fang-fa-gai-bian-sou-suo-an-niu-wen-zi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/让UISearchBar上英文Cancel变成中文的正确方法(改变搜索按钮文字)/"
  - "/2025/06/12/让UISearchBar上英文Cancel变成中文的正确方法(改变搜索按钮文字).html"
  - "/让UISearchBar上英文Cancel变成中文的正确方法(改变搜索按钮文字)/"
  - "/让UISearchBar上英文Cancel变成中文的正确方法(改变搜索按钮文字).html"
  - "/2025/06/12/rang-uisearchbar-shang-ying-wen-cancel-bian-cheng-zhong-wen-de-zheng-que-fang-fa-gai-bi/"
  - "/2025/06/12/rang-uisearchbar-shang-ying-wen-cancel-bian-cheng-zhong-wen-de-zheng-que-fang-fa-ga.html"
  - "/rang-uisearchbar-shang-ying-wen-cancel-bian-cheng-zhong-wen-de-zheng-que-fang-fa-gai-bian-sou-.html"
---
UISearchBar 在Xcode默认环境的工程中, 所有文字显示的是英文, 这让大家很不爽, 网上有修改Cancel键的上文字的办法, 就是取UISearchBar的子视图上的控件, 进行遍历, 个人认为这个办法不可取, 因为除了取消按钮外, 还有全选,粘贴显示的还是英文, 你是不是也要遍历一下呢? 我也做了这个操作，但是结果没有达到想要的。

### [正确的处理方法:](#1)

点击工程名, 打开如下图界面  
在Localizations默认只有English这一项, 我们只需在Localizations上添加Chinese就可以了, 你还可以根据你的需要添加其他的语言.

如果用户把手机语言设成英文, 那么显示的就是英文, 设置成中文,那么显示的就是中文.

正确的解决的方法, 可以让我们节省很多事情, 不是么?
