---
title: "Go基础学习记录 - 编写Web应用程序 - 完善Blog Model"
date: "2025-08-01 10:31:41"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wan-shan-blog-model"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-完善Blog-Model/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-完善Blog-Model.html"
  - "/Go基础学习记录-编写Web应用程序-完善Blog-Model/"
  - "/Go基础学习记录-编写Web应用程序-完善Blog-Model.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wan-shan-blog-model/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wan-shan-blog-model.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wan-shan-blog-model.html"
---
## 完善Blog Model

前面的章节 我们分别介绍了MySQL、SQLite、PostgreSQL等数据库的使用  
本节简单介绍并完善下我们自己的小博客的Model部分，这部分暂时先分享下Blog Model部分  
这部分的完善其实很简单，但是对于像我这样的初学者，还是稍微费力一点

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.11
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.11
```

这些我觉得 够清晰了。OK！

继续分享"完善Model"。

在完善Model层之前我们先想一下，再进行博客的数据交互上我们需要哪些基本功能，我列出如下

* 增加 - 博客空的，是不是我们需要增加的数据
* 更新 - 如果发布错了，是不是需要进行更新
* 删除 - 如果发表的文章违法了，是不是需要进行删除
* 查找 - 如果进行查看，是不是需要把数据对出来，但是这里有读多条和一条的时候

好了功能我们大概知道了，下面我们先写个增加的逻辑，修改 `blog.go` ，添加Create()函数

```go
// Create 添加数据
func Create(p *helpers.Page) (int64, error) {
    sql := fmt.Sprintf("INSERT %s SET title=?", tableName)
    stmt, err := Conn.Prepare(sql)
    if err != nil {
        return 0, err
    }

    res, err := stmt.Exec(p.Title)
    if err != nil {
        return 0, err
    }

    id, err := res.LastInsertId()
    if err != nil {
        return 0, err
    }

    return id, nil
}
```

首先说下参数这里参数的类型是Page，为什么要用Page，其实很好理解，我们前面已经大致列出了一篇文章的主要结构，其实一篇文章的结构的基本上就是我们需要存储的，Page的结构我这里只是简单加了一个ID，  
其他项没有修改，后面再继续完善，一下子完善了，是需要花费蛮多时间的。Page目前的结构如下

```go
type Page struct {
    ID     int         // 新加
    Title  string
    Body   []byte
    Script string
    Html   template.HTML
    Token  string
}
```

Create()函数暂时也存储了标题内容，其余的后期分享  
返回的参数，这里(int64, error)，也很好理解，就是返回我们创建记录的ID，其余的更新和删除功能都很类似下面列出如下

```go
// Update 更新数据
func Update(p *helpers.Page, id int64) (int64, error) {
    sql := fmt.Sprintf("UPDATE %s SET title=? WHERE autokid=?", tableName)
    stmt, err := Conn.Prepare(sql)
    if err != nil {
        return 0, err
    }

    res, err := stmt.Exec(p.Title, id)
    if err != nil {
        return 0, err
    }

    affect, err := res.RowsAffected()
    if err != nil {
        return 0, err
    }

    return affect, nil
}

// Delete 删除数据
func Delete(id int64) (int64, error) {
    sql := fmt.Sprintf("DELETE FROM %s WHERE autokid=?", tableName)
    stmt, err := Conn.Prepare(sql)
    if err != nil {
        return 0, err
    }

    res, err := stmt.Exec(id)
    if err != nil {
        return 0, err
    }

    affect, err := res.RowsAffected()
    if err != nil {
        return 0, err
    }

    return affect, nil
}

// Query 获取数据
func Query() ([]helpers.Page, error) {
    sql := fmt.Sprintf("SELECT * FROM %s", tableName)
    rows, err := Conn.Query(sql)

    if err != nil {
        return nil, err
    }

    var res = []helpers.Page{}

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

        res = append(res, p)
    }

    return res, nil
}

// QueryOne 获取一条数据
func QueryOne() ([]helpers.Page, error) {
    sql := fmt.Sprintf("SELECT * FROM %s LIMIT 0, 1", tableName)

    rows, err := Conn.Query(sql)

    if err != nil {
        return nil, err
    }

    var res = []helpers.Page{}

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

        res = append(res, p)
    }

    return res, nil
}
```

上面基本上就完成了Blog Model的基础数据交互搭建，下面开始写我们的测试单元，简单的写几个测试，看看功能是否能够运行，完整的测试后面来完善，测试单元代码如下

```go
package models

import (
    "testing"

    "github.com/durban89/wiki/helpers"
)

func TestCreate(t *testing.T) {
    p := helpers.Page{
        Title: "Test Create",
    }
    id, err := Create(&p)
    if err != nil {
        t.Error(err)
    }

    t.Log(id)
}

func TestUpdate(t *testing.T) {
    p := helpers.Page{
        Title: "Test Update",
    }

    effect, err := Update(&p, 2)
    if err != nil {
        t.Error(err)
    }

    t.Log(effect)
}

func TestDelete(t *testing.T) {
    effect, err := Delete(2)
    if err != nil {
        t.Error(err)
    }

    t.Log(effect)
}

func TestQueryOne(t *testing.T) {
    row, err := QueryOne()

    if err != nil {
        t.Error(err)
    } else {
        t.Log(row)
    }

    if len(row) == 1 {
        t.Log("正确")
    } else {
        t.Error("失败")
    }

    for i, k := range row {
        t.Log(i)
        t.Log(k)
    }
}

// TestQuery 测试获取数据
func TestQuery(t *testing.T) {
    row, err := Query()

    if err != nil {
        t.Error(err)
    } else {
        t.Log(row)
    }

    if len(row) > 0 {
        t.Log("正确")
    } else {
        t.Error("失败")
    }

    for i, k := range row {
        t.Log(i)
        t.Log(k)
    }
}
```

编译并进行测试，测试通过类似如下

```bash
$ go test -v
=== RUN   TestCreate
--- PASS: TestCreate (0.01s)
        blog_test.go:18: 6
=== RUN   TestUpdate
--- PASS: TestUpdate (0.00s)
        blog_test.go:31: 1
=== RUN   TestDelete
--- PASS: TestDelete (0.00s)
        blog_test.go:40: 1
=== RUN   TestQueryOne
--- PASS: TestQueryOne (0.00s)
        blog_test.go:49: [{3 title2 []   }]
        blog_test.go:53: 正确
        blog_test.go:59: 0
        blog_test.go:60: {3 title2 []   }
=== RUN   TestQuery
--- PASS: TestQuery (0.00s)
        blog_test.go:71: [{3 title2 []   } {4 Test Create []   } {5 Test Create []   } {6 Test Create []   }]
        blog_test.go:75: 正确
        blog_test.go:81: 0
        blog_test.go:82: {3 title2 []   }
        blog_test.go:81: 1
        blog_test.go:82: {4 Test Create []   }
        blog_test.go:81: 2
        blog_test.go:82: {5 Test Create []   }
        blog_test.go:81: 3
        blog_test.go:82: {6 Test Create []   }
PASS
ok      github.com/durban89/wiki/models 0.030s
```

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.12
```
