---
title: "关于UIToolBar的学习"
date: "2025-06-13 15:32:56"
slug: "guan-yu-uitoolbar-de-xue-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/关于UIToolBar的学习/"
  - "/2025/06/13/关于UIToolBar的学习.html"
  - "/关于UIToolBar的学习/"
  - "/关于UIToolBar的学习.html"
  - "/2025/06/13/guan-yu-uitoolbar-de-xue-xi/"
  - "/2025/06/13/guan-yu-uitoolbar-de-xue-xi.html"
  - "/guan-yu-uitoolbar-de-xue-xi.html"
---
### [UIBbarButtonItem的初始化。](#1)

根据SDK的文档，我们可以发现UIBbarButtonItem有如下几种初始化的方法：  
  
- -initWithTitle  
- -initWithImage  
- -initWithBarButtonSystemItem  
- -initWithCustomView  
  
第4种方法就是我们添加各种作料的接口，所以今天的主角其它也是它。

### [在UIToolBar上面添加Title](#2)

```objectivec
UIToolbar *myToolBar = [[UIToolbar alloc] initWithFrame: CGRectMake(0.0f, 0.0f, 320.0f, 44.0f)];
NSMutableArray *myToolBarItems = [NSMutableArray array];
[myToolBarItems addObject:[[[UIBarButtonItem alloc] initWithTitle:@"myTile" style:UIBarButtonItemStylePlain target:self action:@selector(action)] autorelease]];
[myToolBar setItems:myToolBarItems animated:YES];
[myToolBar release];
[myToolBarItems];
```

setItems传入值或者说items是一个对象数组。

### [在UIToolBar上面添加image](#3)

```objectivec
[myToolBarItems addObject:[[[UIBarButtonItem alloc] initWithImage:[UIImage imageNamed:@"myImage.png"] style:UIBarButtonItemStylePlain target:self action:@selector(action)]];
```

### [在UIToolBar上面添加SystemItem](#4)

```objectivec
[myToolBarItems addObject:[[[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemPlay target:self action:@selector(action)] autorelease]];
```

Note:  
  
initWithBarButtonSystemItem初始化：  
  
`- (id)initWithBarButtonSystemItem:(UIBarButtonSystemItem)systemItem target:(id)target action:(SEL)action`  
  
Defines system defaults for commonly used items.  
  
typedef enum {   
  UIBarButtonSystemItemDone,   
  UIBarButtonSystemItemCancel,   
  UIBarButtonSystemItemEdit,   
  UIBarButtonSystemItemSave,   
  UIBarButtonSystemItemAdd,   
  UIBarButtonSystemItemFlexibleSpace,   
  UIBarButtonSystemItemFixedSpace,   
  UIBarButtonSystemItemCompose,   
  UIBarButtonSystemItemReply,   
  UIBarButtonSystemItemAction,   
  UIBarButtonSystemItemOrganize,   
  UIBarButtonSystemItemBookmarks,   
  UIBarButtonSystemItemSearch,   
  UIBarButtonSystemItemRefresh,   
  UIBarButtonSystemItemStop,   
  UIBarButtonSystemItemCamera,   
  UIBarButtonSystemItemTrash,   
  UIBarButtonSystemItemPlay,   
  UIBarButtonSystemItemPause,   
  UIBarButtonSystemItemRewind,   
  UIBarButtonSystemItemFastForward,   
  UIBarButtonSystemItemUndo,    // iPhoneOS 3.0   
  UIBarButtonSystemItemRedo,    // iPhoneOS 3.0   
} UIBarButtonSystemItem;

### [在UIToolBar上面添加其它各种控件](#5)

最自由意义，最有意思的，我把它放在最后来讲。我们使用initWithCustomView来完成，

这里需要看一下initWithCustomView的定义：

```objectivec
- (id)initWithCustomView:(UIView *)customView
```

可以看出，它的参数是一个VIEW，所以我们给它的配料要正确哦才行哦，否则，你就等着时间DIDADIDA的流失吧.  
  
A>加一个开关switch：

```objectivec
[myToolBarItems addObject:[[[UIBarButtonItem alloc]   
                initWithCustomView:[[[UISwitch alloc] init] autorelease]]  
                autorelease]];
```

B>加一个按钮UIBarButtonItem

```objectivec
UIBarButtonItem *myButton = [[[UIBarButtonItem alloc]  
             initWithTitle:@"myButton"  
             style:UIBarButtonItemStyleBordered  
             target:self   
             action:@selector(action)]autorelease];  
get1Button.width = 50;  
[myToolBarItems addObject:myButton];
```

C>加一个文本Label

```objectivec
UILabel *myLabel = [[UILabel alloc] initWithFrame:CGRectMake(40.0f, 20.0f, 45.0f, 10.0f)];  
myLabel.font=[UIFont systemFontOfSize:10];  
//myLabel.backgroundColor = [UIColor clearColor];  
//myLabel.textAlignment=UITextAlignmentCenter;  
UIBarButtonItem *myButtonItem = [[UIBarButtonItem alloc]initWithCustomView:myLabel];  
[myToolBarItems addObject: myButtonItem];     
[mylabel release];  
[myButtonItem release];
```

D>加一个进度条UIProgressView

```objectivec
UIProgressView *myProgress = [[UIProgressView alloc] initWithFrame:CGRectMake(65.0f, 20.0f, 90.0f, 10.0f)];  
UIBarButtonItem *myButtonItem = [[UIBarButtonItem alloc]initWithCustomView:myProgress];  
[myToolBarItems addObject: myButtonItem];  
[myProgress release];                                             
[myButtonItem release];
```

可以加使用initWithCustomView制作各种button，这里就不在这里一个一个在加了。我想你应该也已经掌握了如何添加各种buttonItem的方法了。
