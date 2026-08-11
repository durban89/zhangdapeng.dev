---
title: "Golang网站开发之跳转逻辑实现和模版if操作"
date: "2025-08-04 18:07:50"
slug: "golang-wang-zhan-kai-fa-zhi-tiao-zhuan-luo-ji-shi-xian-he-mo-ban-if-cao-zuo"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之跳转逻辑实现和模版if操作/"
  - "/2025/08/04/Golang网站开发之跳转逻辑实现和模版if操作.html"
  - "/Golang网站开发之跳转逻辑实现和模版if操作/"
  - "/Golang网站开发之跳转逻辑实现和模版if操作.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-tiao-zhuan-luo-ji-shi-xian-he-mo-ban-if-cao-zuo/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-tiao-zhuan-luo-ji-shi-xian-he-mo-ban-if-cao-zuo.html"
  - "/golang-wang-zhan-kai-fa-zhi-tiao-zhuan-luo-ji-shi-xian-he-mo-ban-if-cao-zuo.html"
---
当我们提交一个表单的时候，在遇到问题，需要跳转回去继续完善表单的时候，我们如何来处理这个跳转逻辑 首先我们要获取上个页面的地址当然如果你已经知道要跳转到哪个页面的话就会比较容易操作了

1、知道要跳转的地址

```go
http.Redirect(w, r, 'articles/create.html', http.StatusSeeOther)
```

这个方式能够很直观的进行跳转操作

2、不知道要跳转的地址，但是需要获取referer来跳转

首选获取referer

```go
referer := r.Referer()
```

然后解析获取里面的path，为什么不知道使用referer，如果referer中含有参数的话，我们直接拼接地址的话会出现参数混乱的问题，所以最好是通过解析后在重组的方式，这样有利于我们处理里面的参数

然后使用

```go
u, err := url.Parse(referer)
```

这样我们就拿到了`u`这个参数，里面有个Path键值，可以直接获取到Path值

```go
u.Path
```

之后稍加点逻辑处理下，将重组的URL赋值给Redirect的第三个参数

```go
// 获取Get参数
q := u.Query()

// 删除存在的err_msg参数
q.Del("err_msg")

// 重组
nu := &url.URL{
	Scheme:   u.Scheme,
	Host:     u.Host,
	Path:     u.Path,
	RawQuery: q.Encode() + "&err_msg=参数异常",
}
// 跳转吧
http.Redirect(w, r, nu.String(), http.StatusSeeOther)
```

上面的逻辑整理后得到下面的方法

```go
// BackWithQuery 回跳
func BackWithQuery(r \*http.Request, query string) string {
	u, err := url.Parse(r.Referer())
	if err != nil {
		log.Fatal("url Parse error:", err)
	}

	q := u.Query()

	q.Del("err_msg")

	nu := &url.URL{
		Scheme:   u.Scheme,
		Host:     u.Host,
		Path:     u.Path,
		RawQuery: q.Encode() + "&" + query,
	}

	return nu.String()
}
```

喜欢的拿走不谢

模板if操作

if操作举个例子，如下

```html
{{ if .Msg }}
<div class="row">
  <div class="col-md-12">
    <div class="alert alert-danger">
    {{ .Msg }}
    </div>
  </div>
</div>
{{ end }}
```

具体参考官方文档 https://golang.org/pkg/text/template/ 比如如果在if中判断两个值相等，则搜索下eq ,eq后面有个空格

```html
<select class="form-control" id="category_id" name="category_id">
  {{ if eq .autokid .CategoryID }}
  <option value="{{ .autokid }}" selected>{{ .name }}</option>
  {{ else }}
  <option value="{{ .autokid }}">{{ .name }}</option>
  {{ end }}
</select>
```
