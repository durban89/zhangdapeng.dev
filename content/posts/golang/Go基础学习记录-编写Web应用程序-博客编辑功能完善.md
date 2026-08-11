---
title: "Go基础学习记录 - 编写Web应用程序 - 博客编辑功能完善"
date: "2025-08-01 10:32:00"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-wan-shan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能完善/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能完善.html"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能完善/"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能完善.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-wan-shan/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-wan-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-wan-shan.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.0
```

一般我们在进行博客文章编辑的时候都要进行查询数据库，查找要编辑的文章是否存在，最后将查询出来的内容传到前端进行展示。

## 第一步 完善Model的查询逻辑

修改 `models/blog.go` 文件的QueryOne函数，代码修改如下

```go
// QueryOne 获取一条数据
func (blog *Blog) QueryOne() (*helpers.Page, error) {
	var selectString = strings.Join(blog.Select, ", ")
	var whereString = strings.Join(blog.MergeWhere(), " AND ")

	sql := fmt.Sprintf("SELECT %s FROM %s WHERE %s LIMIT 0, 1", selectString, tableName, whereString)

	rows, err := Conn.Query(sql)

	if err != nil {
		return nil, err
	}

	var res = helpers.Page{}

	for rows.Next() {
		var autokid int
		var title string
		err = rows.Scan(&autokid, &title)

		if err != nil {
			return nil, err
		}

		p := helpers.Page{
			ID:    autokid,
			Title: title,
		}

		res = p
	}

	if res.ID == 0 {
		return nil, errors.New("文章不存在")
	}

	return &res, nil
}
```

从上面的方法中我们可以看出，使用了一个非常笨拙的方法，就是拼接SQL，然后执行SQL查询。

我们在看下Blog结构体是个什么样的设计

```go
type Blog struct {
	Select []string
	Where  []db.Where
}
```

我当初的设计想法是，一个Model在进行查询操作的时候，唯一需要的用的到而且比较多的常用的也就只有select部分和where部分，其他复杂的部分这里暂时不做设计，后面会一步一步进行设计

再看下db.Where结构体的样子

```go
type Where struct {
	Name     string
	Value    string
	Operator string
}
```

同时加了一个Merge方法，这个方法主要是用来进行将where条件的字段名和值进行拼接组成一个能在查询中使用的where条件字段值。

## 第二步 完善路由调动方法

完成这些，一个基本的查询就完成了，下面看下如何来调用这个操作，使得我们的博客能够跟数据库打通，后面的编辑提交跟添加之类的操作就比较方便了。看下ArticleEdit函数的修改如下

```go
// ArticleEdit 编辑文章
func ArticleEdit(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")
	if id == "" {
		http.NotFound(w, r)
		return
	}

	where := []db.Where{}

	where = append(where, db.Where{
		Name:  "autokid",
		Value: id,
	})

	blogModel := &models.Blog{
		Select: []string{"*"},
		Where:  where,
	}

	p, err := blogModel.QueryOne()

	if err != nil {
		http.NotFound(w, r)
		return
	}

	crutime := time.Now().Unix()
	h := md5.New()
	io.WriteString(h, strconv.FormatInt(crutime, 10))
	token := fmt.Sprintf("%x", h.Sum(nil))

	p.Token = token
	helpers.RenderTemplate(w, "edit", p)
}
```

首先是根据传进来的参数id，查询数据库blog表，如果文章存在则进行渲染模板，如果不存在则渲染不存在的页面。

## 第三步 重新编译并运行

项目目录下执行并运行

```bash
go install && wiki
```

想要看完成实例，请到这里，如下

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.0
```
