---
title: "在UIToolBar上添加按钮，并调整按钮位置"
date: "2025-06-13 15:32:51"
slug: "zai-uitoolbar-shang-tian-jia-an-niu-bing-tiao-zheng-an-niu-wei-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/在UIToolBar上添加按钮，并调整按钮位置/"
  - "/2025/06/13/在UIToolBar上添加按钮，并调整按钮位置.html"
  - "/在UIToolBar上添加按钮，并调整按钮位置/"
  - "/在UIToolBar上添加按钮，并调整按钮位置.html"
  - "/2025/06/13/在UIToolBar上添加按钮-并调整按钮位置/"
  - "/2025/06/13/在UIToolBar上添加按钮-并调整按钮位置.html"
  - "/2025/06/13/zai-uitoolbar-shang-tian-jia-an-niu-bing-tiao-zheng-an-niu-wei-zhi/"
  - "/2025/06/13/zai-uitoolbar-shang-tian-jia-an-niu-bing-tiao-zheng-an-niu-wei-zhi.html"
  - "/zai-uitoolbar-shang-tian-jia-an-niu-bing-tiao-zheng-an-niu-wei-zhi.html"
---
我是第一次使用这个东西，经过自己资料的查找，终于有了我觉得比较好用的方法

如下代码

```objectivec
UIButton *nextStep = [[UIButton alloc] initWithFrame:CGRectMake(0.0, 10.0, 70.0, 30.0)];
[nextStep setImage:[UIImage imageNamed:@"button-下一步.png"] forState:UIControlStateNormal];
[nextStep addTarget:self action:@selector(doneAction:) forControlEvents:UIControlEventTouchUpInside];
UIBarButtonItem *nextStepBarBtn = [[UIBarButtonItem alloc] initWithCustomView:nextStep];
//[nextStepBarBtn setWidth:1080];
UIBarButtonItem *spaceButtonItem = [[UIBarButtonItem alloc]initWithBarButtonSystemItem:      UIBarButtonSystemItemFixedSpace target:nil action:nil];
[spaceButtonItem setWidth:540];
[myToolBar setItems:[NSArray arrayWithObjects:spaceButtonItem,nextStepBarBtn,nil]  animated:YES];
```

这里面用的是横屏的，我针对于自己的项目，需要的是竖屏的，结果的代码如下：

```objectivec
UIToolbar *attentionToolBar = [[UIToolbar alloc] initWithFrame:CGRectMake(0.0, self.view.frame.size.height - 100.0, self.view.frame.size.width, 60.0)];
attentionToolBar.tintColor = [UIColor redColor];
attentionToolBar.backgroundColor = [UIColor redColor];
[self.view addSubview:attentionToolBar];


UIButton *attentionBar = [[UIButton alloc] initWithFrame:CGRectMake(200.0, 10.0, 80.0, 30.0)];
[attentionBar setTitle:@"添加关注" forState:UIControlStateNormal];
[attentionBar addTarget:self action:@selector(addAttention:) forControlEvents:UIControlEventTouchUpInside];
UIBarButtonItem *nextStepBarBtn = [[UIBarButtonItem alloc] initWithCustomView:attentionBar];

UIBarButtonItem *spaceButtonItem = [[UIBarButtonItem alloc]initWithBarButtonSystemItem:      UIBarButtonSystemItemFixedSpace target:nil action:nil];
[spaceButtonItem setWidth:(self.view.frame.size.width - attentionBar.frame.size.width)/2];

[attentionToolBar setItems:[NSArray arrayWithObjects:spaceButtonItem,nextStepBarBtn,nil] animated:YES];
```
