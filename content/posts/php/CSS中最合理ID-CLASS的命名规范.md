---
title: "CSS中最合理ID/CLASS的命名规范"
date: "2025-06-17 15:36:21"
slug: "css-zhong-zui-he-li-idclass-de-ming-ming-gui-fan"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/06/17/CSS中最合理ID/CLASS的命名规范/"
  - "/2025/06/17/CSS中最合理ID/CLASS的命名规范.html"
  - "/CSS中最合理ID/CLASS的命名规范/"
  - "/CSS中最合理ID/CLASS的命名规范.html"
  - "/2025/06/17/CSS中最合理ID-CLASS的命名规范/"
  - "/2025/06/17/CSS中最合理ID-CLASS的命名规范.html"
  - "/2025/06/17/css-zhong-zui-he-li-idclass-de-ming-ming-gui-fan/"
  - "/2025/06/17/css-zhong-zui-he-li-idclass-de-ming-ming-gui-fan.html"
  - "/css-zhong-zui-he-li-idclass-de-ming-ming-gui-fan.html"
---
先看一个例子：

```css
.l-123f { color: red; }
```

　　如果你第一次看到这个类名，你能在css文件立刻找到这个class吗？估计很难，因为这个类的名称只是某一个人能理解的符号再没有其他意义，所以这里没有一个准确的方法能够让你立即说出来。

让我们来看下这个类名定义：

```css
.right-red { color:red; }
```

你可能很明确的知道这个class选择符的所起的作用。但是这里还有个问题，当你在一星期的时间需要重新设计。在重新设计的时候，这个模块被放置到了左边，而且还是绿色。这个类就不再有存在的价值。所以现在不得不选择，要么改变所有的属性值，要么放着它不动，这可能导致混乱。

最好不要在你的类名或者ID名中去加入颜色或者长宽的尺寸等带有属性的名字。你应该避免任何的属性值都是直接的词汇。（如box）直接属性可能会导致内容的分离。

让我们来看看最合理ID/CLASS的命名规范：

```css
.product-description { color: red; }
```

　　用这种样式定义的product-description（产品描述），不管你怎么改变，她都是那么的干净清晰。

总结为：**最好不要在你的类名或者ID名中去加入颜色或者长宽的尺寸等带有属性的名字。**

