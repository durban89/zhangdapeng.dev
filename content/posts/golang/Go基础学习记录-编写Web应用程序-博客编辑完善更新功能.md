---
title: "Go基础学习记录 - 编写Web应用程序 - 博客编辑完善更新功能"
date: "2025-08-01 10:32:04"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-wan-shan-geng-xin-gong-neng"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑完善更新功能/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑完善更新功能.html"
  - "/Go基础学习记录-编写Web应用程序-博客编辑完善更新功能/"
  - "/Go基础学习记录-编写Web应用程序-博客编辑完善更新功能.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-wan-shan-geng-xin-/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-wan-shan-geng-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-wan-shan-geng-xin-gong-ne.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.1
```

上篇文章【[Go基础学习记录 - 编写Web应用程序 - 博客编辑功能完善](https://www.xiaorongmao.com/blog/71)】我们只是将需要的文章从数据库读取出来，然后在前端展示，那么如果要修改的话，改如何操作，今天的分享继续上篇文章

### 第一步、添加更新Model

既然更新，就涉及到了更新的逻辑，即如何将更新写入数据库，这里我将之前的Update函数进行完善操作，将Update改为了UpdateData，主要原因是我在另外要给sqlite库中也写了一个Update的函数，go工具提示我重复了，这个不知道是不是go的机制的问题，同一个包下面不应该有相同的函数，暂时修改为UpdateData，不过这里也应该是设计的问题，后面再完善下，首先先将编辑更新的逻辑完善，UpdateData的函数实现如下

```go
// UpdateData 更新数据
func (b *Blog) UpdateData() (int64, error) {
	var updateString = strings.Join(b.MergeUpdate(), " , ")
	var whereString = strings.Join(b.MergeWhere(), " AND ")

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

当然这里也是有问题的，推荐将要修改的参数放入Exec中，这样应该可以预防SQL注入。

### 第二步、添加更新Controller

更新的Model有了，然后修改Controller的逻辑，修改函数ArticleEdit，代码实现如下

```go
// ArticleEdit 编辑文章
func ArticleEdit(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")
	if id == "" {
		http.NotFound(w, r)
		return
	}

	where := []db.Where{}
	update := []db.UpdateSection{}

	if strings.ToLower(r.Method) == "get" {

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
	} else if strings.ToLower(r.Method) == "post" {
		title := r.FormValue("title")
		if title == "" {
			http.Redirect(w, r, fmt.Sprintf("/edit?id=%s", id), http.StatusFound)
			return
		}

		update = append(update, db.UpdateSection{
			Name:  "title",
			Value: title,
		})

		where = append(where, db.Where{
			Name:  "autokid",
			Value: id,
		})

		blogModel := &models.Blog{
			Update: update,
			Where:  where,
		}

		_, err := blogModel.UpdateData()

		if err != nil {
			http.NotFound(w, r)
			return
		}

		http.Redirect(w, r, fmt.Sprintf("/edit?id=%s", id), http.StatusFound)
		return
	}

}
```

感觉有那么点像之前的写法了。

### 第三步、添加更新View

在来修改下模板，主要是修改提交的地址。将

```html
<form action="/save/{{.Title}}" method="POST">
```

更改为

```html
<form action="/edit/?id={{.ID}}" method="POST">
```

想要看完成实例，请到这里，如下

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.2
```
