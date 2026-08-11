---
title: "UIViewController 中的 willMoveToParentViewController和didMoveToParentViewController的使用"
date: "2025-06-27 10:07:05"
slug: "uiviewcontroller-zhong-de-willmovetoparentviewcontroller-he-didmovetoparentviewcontroller-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/UIViewController-中的-willMoveToParentViewController和didMoveToParentViewController的使用/"
  - "/2025/06/27/UIViewController-中的-willMoveToParentViewController和didMoveToParentViewController的使用.html"
  - "/UIViewController-中的-willMoveToParentViewController和didMoveToParentViewController的使用/"
  - "/UIViewController-中的-willMoveToParentViewController和didMoveToParentViewController的使用.html"
  - "/2025/06/27/uiviewcontroller-zhong-de-willmovetoparentviewcontroller-he-didmovetoparentviewcontroll/"
  - "/2025/06/27/uiviewcontroller-zhong-de-willmovetoparentviewcontroller-he-didmovetoparentviewcont.html"
  - "/uiviewcontroller-zhong-de-willmovetoparentviewcontroller-he-didmovetoparentviewcontroller-de-s.html"
---
关于这两个方法，也是IOS5之后才加上去的。

在iOS 5.0及以后，iOS为UIViewController类添加了新的属性和方法：

```objectivec
@property(nonatomic,readonly) NSArray *childViewControllers
- (void)addChildViewController:(UIViewController *)childController
- (void)removeFromParentViewController
- (void)transitionFromViewController：：：：：：
- (void)willMoveToParentViewController:(UIViewController *)parent
- (void)didMoveToParentViewController:(UIViewController *)parent
```

这样，就能够将一个页面中的UIViewController控制起来，而不是混乱的共用一个UIViewController，最重要的是，编程习惯的革命：降低了功能的耦合度！

这里看看这几个方法的使用：

#### [[父视图控制器 addChildViewController:子视图控制器];](#1)

在此，图控制器A添加了另一个图控制器B，那么A充当父视图控制器，B充当子视图控制器。父视图控制器充当了视图控制器容器的角色。

1、addChildViewController方法：

```objectivec
- (void)addChildViewController:(UIViewController *)childController
```

向视图控制器容器中添加子视图控制器

childController：子视图控制器

当要添加的子视图控制器已经包含在视图控制器容器中，那么，相当于先从父视图控制器中删除，然后重新添加到父视图控制器中。

2、removeFromParentViewController 方法

```objectivec
- (void)removeFromParentViewController
```

从父视图控制器中删除。

3、transitionFromViewController 方法

```objectivec
- (void)transitionFromViewController:(UIViewController *)fromViewController toViewController:(UIViewController *)toViewController duration:(NSTimeInterval)duration options:(UIViewAnimationOptions)options animations:(void (^)(void))animations completion:(void (^)(BOOL finished))completion
```

交换两个子视图控制器的位置（由于添加的顺序不同，所以子试图控制器在父视图控制器中存在层次关系）

fromViewController：当前显示的子试图控制器，将被替换为非显示状态

toViewController：将要显示的子视图控制器

duration：交换动画持续的时间，单位秒

options：动画的方式

animations：动画Block

completion：完成后执行的Block

4、willMoveToParentViewController 方法

```objectivec
- (void)willMoveToParentViewController:(UIViewController *)parent
```

当一个视图控制器从视图控制器容器中被添加或者被删除之前，该方法被调用parent：父视图控制器，如果没有父视图控制器，将为nil

注意点：

1. 当我们向我们的视图控制器容器中调用removeFromParentViewController方法时，必须要先调用该方法，且parent参数为nil：

   [将要删除的视图控制器 willMoveToParentViewController:nil];
2. 当我们调用addChildViewController方法时，在添加子视图控制器之前将自动调用该方法。所以，就不需要我们显示调用了。

5、didMoveToParentViewController 方法

```objectivec
- (void)didMoveToParentViewController:(UIViewController *)parent
```

当从一个视图控制容器中添加或者移除viewController后，该方法被调用。

parent：父视图控制器，如果没有父视图控制器，将为nil

当我们向我们的视图控制器容器（就是父视图控制器，它调用addChildViewController方法加入子视图控制器，它就成为了视图控制器的容器）中添加（或者删除）子视图控制器后，必须调用该方法，告诉iOS，已经完成添加（或删除）子控制器的操作。

removeFromParentViewController 方法会自动调用了该方法，所以，删除子控制器后，不需要在显示的调用该方法了。

其实，这几个方法中的API说明，看的还懂。

#### [关于willMoveToParentViewController方法和didMoveToParentViewController方法的使用](#2)

1.这两个方法用在子试图控制器交换的时候调用！即调用transitionFromViewController 方法时，调用。

2.当调用willMoveToParentViewController方法或didMoveToParentViewController方法时，要注意他们的参数使用：

当某个子视图控制器将从父视图控制器中删除时，parent参数为nil。

即：`[将被删除的子试图控制器 willMoveToParentViewController:nil];`

当某个子试图控制器将加入到父视图控制器时，parent参数为父视图控制器。

即：`[将被加入的子视图控制器 didMoveToParentViewController:父视图控制器];`

3.无需调用[子视图控制器 willMoveToParentViewController:父视图控制器]方法。因为我们调用[父视图控制器 addChildViewController:子视图控制器]时，已经默认调用了。

只需要在transitionFromViewController方法后，调用[子视图控制器didMoveToParentViewController:父视图控制器];

4.无需调用[子视图控制器 didMoveToParentViewController:父视图控制器]方法。因为我们调用

[子视图控制器 removeFromParentViewController]时，已经默认调用了。

只需要在transitionFromViewController方法之前调用：[子视图控制器 willMoveToParentViewController:nil]。

经过这几点说明，在一些视图切换的过程中，和视图的换位中，应该可以了解什么时候去调用对应的视图啦。

---

