---
title: "Go基础学习记录之Web开发的博客编辑功能之Model查询重构"
date: "2025-08-01 10:32:15"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-bian-ji-gong-neng-zhi-model-cha-xun-zhong-gou"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Web开发的博客编辑功能之Model查询重构/"
  - "/2025/08/01/Go基础学习记录之Web开发的博客编辑功能之Model查询重构.html"
  - "/Go基础学习记录之Web开发的博客编辑功能之Model查询重构/"
  - "/Go基础学习记录之Web开发的博客编辑功能之Model查询重构.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-bian-ji-gong-neng-zhi-model-cha-xun-zhon/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-bian-ji-gong-neng-zhi-model-cha-xun-.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-bian-ji-gong-neng-zhi-model-cha-xun-zhong-gou.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.4
```

上篇文章【[Go基础学习记录 - 编写Web应用程序 - 博客编辑功能之Model重构](https://www.xiaorongmao.com/blog/75)】，只更新了Updaet方法，这次分享下，查询相关的实现  
说实话，这个查询本来以为很简单，跟以前写PHP或者Python一样，直接返回查询结果，实际上也可能跟我使用的MySQL库有关系吧，不过这个不是重点，重点是我们找到解决问题的办法  
开始之前先说下golang的interface的知识点

`...interface{}`这个要了解，知道这个是什么意思

先看下`...string`，这个代表string参数，具体函数的例子

```go
func music(m ...string) {
    // other 实现
}
```

调用的时候我们这样调用

```go
music("a", "b", "c")
```

我现在只是传入了三个参数，也可以传入更多的参数，当然还有另外一种调用方式

```go
var args = []string{
    "a",
    "b",
    "c",
}
music(args...)
```

上面是个很好理解的例子，那么...interface{}的使用跟...string的使用差不多的，下面开始说下我是如何优化我的查询方法的。

## 第一步、Model层修改

这里优化了两个Query和QueryOne，先看下QueryOne，代码如下

```go
// QueryOne 获取一条数据
func (p *ModelProperty) QueryOne(s SelectValues, where WhereValues) error {
    var selectString = s.MergeSelect()

    var whereString = where.MergeWhere()

    sql := fmt.Sprintf("SELECT %s FROM %s WHERE %s LIMIT 0, 1", selectString, tableName, whereString)

    rows, err := Conn.Query(sql)

    if err != nil {
        return err
    }

    selectField := make([]interface{}, len(s))

    var i = 0
    for _, v := range s {
        selectField[i] = v
        i++
    }

    for rows.Next() {
        err = rows.Scan(selectField...)

        if err != nil {
            return err
        }

        var i = 0
        for _, v := range s {
            ref := reflect.ValueOf(v)
            fmt.Println(ref.Elem())
            i++
        }
    }

    return nil
}
```

同时修改了SelectValues的结构，如下

```go
// SelectValues select条件值
type SelectValues map[string]interface{}
```

重点的修改是这里

```go
selectField := make([]interface{}, len(s))

var i = 0
for _, v := range s {
    selectField[i] = v
    i++
}
```

和函数MergeSelect

```go
// MergeSelect  合并select条件
func (s SelectValues) MergeSelect() string {
    value := []string{}
    for k := range s {
        v := fmt.Sprintf("`%s`", k)
        value = append(value, v)
    }

    return strings.Join(value, ", ")
}
```

第一部分的修改是为了符合`rows.Scan(selectField...)`的函数调用，所以需要进行转换一下，同时需要为了控制层方便获取数据，需要通过指针的方式，将查到的数据回传到控制层  
第二部分的修改是为了配合查询语句的生成，所以第二个修改是将key值进行了处理，最后也是修改SelectValues的原因，改过之后，其实整体上方便了查询，很多逻辑觉得实现的也很顺利

## 第二步、控制层调用

QueryOne查询的调用如下

```go
var autokid int64
var title string
selectField := models.SelectValues{
    "autokid": &autokid,
    "title":   &title,
}

err := blogModel.QueryOne(selectField, where)

if err != nil {
    http.NotFound(w, r)
    return
}

p := helpers.Page{
    Title: title,
    ID:    autokid,
}
```

Query查询的调用

```go
var blogModel models.BlogModel

var autokid int64
var title string
selectField := models.SelectValues{
    "autokid": &autokid,
    "title":   &title,
}

where := models.WhereValues{}

qr, err := blogModel.Query(selectField, where, 1, 10)

if err != nil {
    http.NotFound(w, r)
    return
}

fmt.Println(qr)
```

从区别上可以看出，其实QueryOne直接查出来需要的数据，Query查询则直接返回具体的结果集。

今天分享就到这里，有问题可以留言或加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.5
```
