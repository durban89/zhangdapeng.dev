---
title: "hexo默认处理heading的标题为id的异常解决方案"
date: "2025-05-29 17:08:34"
slug: "hexo-mo-ren-chu-li-heading-de-biao-ti-wei-id-de-yi-chang-jie-jue-fang-an"
categories: ["技术"]
tags: ["Hexo"]
aliases:
  - "/2025/05/29/hexo默认处理heading的标题为id的异常解决方案/"
  - "/2025/05/29/hexo默认处理heading的标题为id的异常解决方案.html"
  - "/hexo默认处理heading的标题为id的异常解决方案/"
  - "/hexo默认处理heading的标题为id的异常解决方案.html"
  - "/2025/05/29/hexo-mo-ren-chu-li-heading-de-biao-ti-wei-id-de-yi-chang-jie-jue-fang-an/"
  - "/2025/05/29/hexo-mo-ren-chu-li-heading-de-biao-ti-wei-id-de-yi-chang-jie-jue-fang-an.html"
  - "/hexo-mo-ren-chu-li-heading-de-biao-ti-wei-id-de-yi-chang-jie-jue-fang-an.html"
---
hexo在处理markdown文档的时候，默认将heading的内容作为了id来处理锚点，如果是英文是没有问题的。

```
## 我的标题
```

处理后的html内容

```html
<h2 id="我的标题"><a href="#我的标题" class="headerlink" title="我的标题"></a><a href="#我的标题">我的标题</a></h2>
```

但是作为标题是中文的话就会有问题，以为在js的代码中，id是中文是不支持的，这会导致很多js库无法正常运行

找了很多资料，其中就有安装`hexo-renderer-markdown-it`

但是我自己亲自测试下来，还是很复杂，然后也没有解决我的问题，于是我思考这个hexo不会烂到这个程度吧

于是我看到了一种写法

```
## [我的标题](#custom-id)
```

处理后的html内容
```html
<h2 id="custom-id"><a href="#custom-id" class="headerlink" title="我的标题"></a><a href="#custom-id">我的标题</a></h2>
```

哎，可以，就这么轻松的解决了，不需要什么卸载安装什么的
