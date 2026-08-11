---
title: "Go基础学习记录 - 编写Web应用程序 - 博客编辑功能之Model的重新思考"
date: "2025-08-01 10:32:07"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-model-de-chong-xin-si-kao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能之Model的重新思考/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能之Model的重新思考.html"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能之Model的重新思考/"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能之Model的重新思考.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-mode/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-model-de-ch.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.2
```

上篇文章【[Go基础学习记录 - 编写Web应用程序 - 博客编辑完善更新功能](https://www.xiaorongmao.com/blog/72)】，在修改的过程中，遇到了一个问题就是Update函数与sqlite中的函数有冲突的提示，提示内容大概意思是重新定义了这个函数，这次我将更新的逻辑进行了更改，重新定义了下Model，同时将QueryOne函数也进行了更新。

第一步、重新定义Model

重新定义Model，主要是从概念上抽象了一些逻辑，比如一个查询语句最基本的where、select和更新中的update部分，我将这一部分作为一个小块来处理，处理代码逻辑如下，首先建立一个 `models/models.go` 文件，内容如下

```go
package models

import (
	"fmt"
	"strings"
)

// Model 模型
type Model interface {
	QueryOne()
	Update()
}

// WhereCondition where条件
type WhereCondition struct {
	Operator string
	Value    string
}

// WhereValues where条件值
type WhereValues map[string]WhereCondition

// UpdateValues update条件值
type UpdateValues map[string]string

// SelectValues select条件值
type SelectValues []string

// MergeWhere 合并where条件
func (w WhereValues) MergeWhere() string {
	where := []string{}
	for k, v := range w {
		if v.Operator == "" {
			s := fmt.Sprintf("%s = %s", k, v.Value)
			where = append(where, s)
		} else {
			s := fmt.Sprintf("%s %s %s", k, v.Operator, v.Value)
			where = append(where, s)
		}
	}

	return strings.Join(where, " AND ")
}

// MergeUpdate 合并update条件
func (u UpdateValues) MergeUpdate() string {
	update := []string{}
	for k, v := range u {
		s := fmt.Sprintf("%s = '%s'", k, v)
		update = append(update, s)
	}

	return strings.Join(update, ", ")
}

// MergeSelect  合并select条件
func (s SelectValues) MergeSelect() string {
	return strings.Join(s, ", ")
}
```

这样我觉得稍微清晰了一些，而且放在一个models.go文件，代表几乎所有的model都应该有这些方法。

修改完方法，就需要修改controller

第二步、修改Model

这里主要是先修改下models/blog.go，分别修改了QueryOne和Update两个函数，修改后的代码如下

```go
// QueryOne 获取一条数据
func (b *Blog) QueryOne(where WhereValues) (helpers.Page, error) {
	var selectString = SelectValues{
		"*",
	}.MergeSelect()

	var whereString = where.MergeWhere()

	sql := fmt.Sprintf("SELECT %s FROM %s WHERE %s LIMIT 0, 1", selectString, tableName, whereString)

	rows, err := Conn.Query(sql)

	var res = helpers.Page{}

	if err != nil {
		return res, err
	}

	for rows.Next() {
		var autokid int
		var title string
		err = rows.Scan(&autokid, &title)

		if err != nil {
			return res, err
		}

		p := helpers.Page{
			ID:    autokid,
			Title: title,
		}

		res = p
	}

	if res.ID == 0 {
		return res, errors.New("文章不存在")
	}

	return res, nil
}
```

另外Update函数内容如下

```go
// Update 更新数据
func (b *Blog) Update(update UpdateValues, where WhereValues) (int64, error) {
	var updateString = update.MergeUpdate()
	var whereString = where.MergeWhere()

	sql := fmt.Sprintf("UPDATE %s SET %s WHERE %s", tableName, updateString, whereString)

	stmt, err := Conn.Prepare(sql)
	if err != nil {
		return 0, err
	}

	res, err := stmt.Exec()
	if err != nil {
		return 0, err
	}

	affect, err := res.RowsAffected()
	if err != nil {
		return 0, err
	}

	return affect, nil
}
```

这里的话暂时没有写单元测试

第三步、修改Controller

controller的修改主要是修改article中ArticleEdit函数，内容如下

```go
// ArticleEdit 编辑文章
func ArticleEdit(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")
	if id == "" {
		http.NotFound(w, r)
		return
	}

	where := models.WhereValues{
		"autokid": models.WhereCondition{
			Operator: "=",
			Value:    id,
		},
	}

	update := map[string]string{}

	if strings.ToLower(r.Method) == "get" {

		blogModel := &models.Blog{}

		p, err := blogModel.QueryOne(where)

		if err != nil {
			http.NotFound(w, r)
			return
		}

		crutime := time.Now().Unix()
		h := md5.New()
		io.WriteString(h, strconv.FormatInt(crutime, 10))
		token := fmt.Sprintf("%x", h.Sum(nil))

		p.Token = token
		helpers.RenderTemplate(w, "edit", &p)
	} else if strings.ToLower(r.Method) == "post" {
		title := r.FormValue("title")
		if title == "" {
			http.Redirect(w, r, fmt.Sprintf("/edit?id=%s", id), http.StatusFound)
			return
		}

		update["title"] = title

		blogModel := &models.Blog{}

		_, err := blogModel.Update(update, where)

		if err != nil {
			http.NotFound(w, r)
			return
		}

		http.Redirect(w, r, fmt.Sprintf("/edit?id=%s", id), http.StatusFound)
		return
	}

}
```

经过前面的修改，自我觉得更加golang编程化了。

重新编辑代码并运行，一切正常，想要查看完整代码的，可以到下面引导去下载

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.3
```
