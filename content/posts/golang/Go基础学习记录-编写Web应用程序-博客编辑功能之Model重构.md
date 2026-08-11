---
title: "Go基础学习记录 - 编写Web应用程序 - 博客编辑功能之Model重构"
date: "2025-08-01 10:32:12"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-model-zhong-gou"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能之Model重构/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-博客编辑功能之Model重构.html"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能之Model重构/"
  - "/Go基础学习记录-编写Web应用程序-博客编辑功能之Model重构.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-mode/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-bo-ke-bian-ji-gong-neng-zhi-model-zhong.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.3
```

针对于前面的几篇分享，觉的还是要勇于创新，发现更好的，更利于自己的，更能提高写代码效率的方式。于是将model这块的逻辑进行了重构  
之前的文章【[Go基础学习记录 - 编写Web应用程序 - 博客编辑功能之Model的重新思考](https://www.xiaorongmao.com/blog/73)】也算是实现了一部分功能，小区域的是没有问题，比如只是针对Blog这一个model是没有问题的，但是如果在创建一个是不是要重新再写一遍Create、Update、Delete等方式。  
这个是很不方便的，在了解了创建一篇文章的时候大概就是需要添加、更新、删除、查询等功能的时候，其实应该写一个比较通用代码，具体需要更换的大概就是  
数据要存储到哪张表，需要哪些字段，而且这些字段又都是变化的，不应该写死，而是由初始化的时候或者调用的时候来具体操作，这个就是目前设计模式中经常提到的，我不说大家也都知道，嘿嘿，我就不说，自己百度去。  
有点类似于工厂模式

## 第一步、重新定义Model具体结构如下

```go
// ModelMethod 接口
type ModelMethod interface {
    Query(offset int64, limit int64) (map[string]string, error)
    Create() (int64, error)
    Delete() (int64, error)
    Update() (int64, error)
    QueryOne(int64) (map[string]string, error)
}

// ModelProperty 属性
type ModelProperty struct {
    TableName string
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

// InsertValues Insert值
type InsertValues map[string]string

// SelectValues select条件值
type SelectValues []string
```

目前做了一个简单规划，表名要有，查询的where条件能够支持比较稍微复杂的查询，同时update和select的字段也都做了具体的定义。下面看下QueryOne和Update功能

## 第二步、重新定义Model函数这里暂时主要是定义了Update的函数，其余几个也加了暂时未做测试，这里只拿实践过的进行分享

```go
// Update 更新
func (p *ModelProperty) Update(update UpdateValues, where WhereValues) (int64, error) {
    var updateString = update.MergeUpdate()
    var whereString = where.MergeWhere()

    sql := fmt.Sprintf("UPDATE %s SET %s WHERE %s", tableName, updateString, whereString)
    // 这里的tableName是有调用者设置的，也就是我们一般说的继承者设置的

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

**\*\*Tips\*\* 这里的tableName是有调用者设置的，也就是我们一般说的继承者设置的**

## 第三步、控制器调用修改

修改ArticleEdit函数  
将更新部分

```go
blogModel := &models.Blog{}
_, err := blogModel.Update(update, where)
```

替换为

```go
var blogInstance models.BlogModel
_, err := blogInstance.Update(update, where)
```

重新编译后运行功能正常

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.4
```
