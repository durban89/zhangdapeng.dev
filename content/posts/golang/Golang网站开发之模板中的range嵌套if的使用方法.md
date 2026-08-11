---
title: "Golang网站开发之模板中的range嵌套if的使用方法"
date: "2025-08-04 18:08:07"
slug: "golang-wang-zhan-kai-fa-zhi-mu-ban-zhong-de-range-qian-tao-if-de-shi-yong-fang-fa"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之模板中的range嵌套if的使用方法/"
  - "/2025/08/04/Golang网站开发之模板中的range嵌套if的使用方法.html"
  - "/Golang网站开发之模板中的range嵌套if的使用方法/"
  - "/Golang网站开发之模板中的range嵌套if的使用方法.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-mu-ban-zhong-de-range-qian-tao-if-de-shi-yong-fang-fa/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-mu-ban-zhong-de-range-qian-tao-if-de-shi-yong-fang-fa.html"
  - "/golang-wang-zhan-kai-fa-zhi-mu-ban-zhong-de-range-qian-tao-if-de-shi-yong-fang-fa.html"
---
### 情况介绍

我有一个分类想要在前端展示出来，并将选中的数组项进行特殊处理

开始我以为是这样的

> 选中的数组值存在CategoryID中 分类数组列表存在Cate中

```html
<div class="form-group">
  <label for="category">分类</label>
  <select class="form-control" id="category_id" name="category_id">
    {{range .Cate}}
    <option value="{{ .autokid }}" {{if eq .autokid .CategoryID}}selected{{end}}>{{ .name }}</option>
    {{ end }}
  </select>
</div>
```

结果前端运行的时候提示我

> template: update.html:54:48: executing "content" at <eq .autokid .CategoryID>: error calling eq: invalid type for comparison

看不懂也不了解，但是看官方文档也是没有什么特殊提示的地方，可能是我没有找到吧，不过在搜索的过程中我隐约记得似乎需要进行赋值操作，我试着改了下，结果如下

```html
<div class="form-group">
  <label for="category">分类</label>
  <select class="form-control" id="category_id" name="category_id">
    {{ $categoryID := .CategoryID }}
    {{range .Cate}}
    <option value="{{ .autokid }}" {{if eq .autokid $categoryID}}selected{{end}}>{{ .name }}</option>
    {{ end }}
  </select>
</div>
```

再次运行下试试，果然可以了，是什么原因要重新创建一个变量赋值后才能调用

期间我试过这样的操作

```html
CategoryID {{.CategoryID}}

{{range .Cate}}
CategoryID {.CategoryID}
autokid
{{ .autokid }}
{{ end }}
```

会得到下面的结果

```bash
CategoryID - 1

CategoryID - 
autokid - 1
```

说明确实要重新创建一个变量来使用，否则直接在range范围内是无法调用的
