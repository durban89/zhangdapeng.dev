---
title: "Go基础学习记录 - 编写Web应用程序 - 数据库(四)"
date: "2025-08-01 10:31:38"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-si"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(四)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(四).html"
  - "/Go基础学习记录-编写Web应用程序-数据库(四)/"
  - "/Go基础学习记录-编写Web应用程序-数据库(四).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-四/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-四.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-si/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-si.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-si.html"
---
本次分享下 -- PostgreSQL数据库驱动程序

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.10
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.10
```

这些我觉得 够清晰了。OK！

继续分享"数据库"的分享。

## 数据库

对于Web开发人员而言，数据库是Web开发的核心。  
您几乎可以将任何内容保存到数据库中，并查询或更新其中的数据，如用户信息，产品或新闻文章。  
Go不提供任何数据库驱动程序，但它确实在database/sql包中定义了驱动程序接口。  
我们可以基于该接口开发数据库驱动程序。首先先看下 “PostgreSQL数据库驱动程序”

### PostgreSQL

PostgreSQL是一个对象关系数据库管理系统，可用于许多平台，包括Linux，FreeBSD，Solaris，Microsoft Windows和Mac OS X.它是在MIT风格的许可下发布的，因此是免费的开源软件。  
它比MySQL大，因为它是为企业用作Oracle的替代品而设计的。  
Postgresql是企业类项目的不错选择。

### PostgreSQL drivers

PostgreSQL有许多可用的数据库驱动程序。以下是它们的三个例子

* https://github.com/lib/pq supports database/sql, written in pure Go.
* https://github.com/jbarham/gopgsqldriver supports database/sql, written in pure Go.
* https://github.com/lxn/go-pgsql supports database/sql, written in pure Go.

我将使用后面示例中的第一个。

## Samples 实例演示

## 安装PostgreSQL驱动

如果本地没有安装的话，先去安装下这个包，安装命令如下

```bash
https://github.com/lib/pq
```

### 添加PostgreSQL驱动连接

项目目录下创建一个文件夹db，db中创建一个文件 `pg.go`，文件内容如下

```go
package db

import (
    "database/sql"
    "fmt"

    // Register PostgreSQL
    _ "github.com/lib/pq"
)

const (
    // DBUser 用户名
    DBUser = "root"
    // DBPassword 密码
    DBPassword = "123456"
    // DBName  库名
    DBName = "test"
)

// PostgreSQLDB Conn
var PostgreSQLDB *sql.DB

func init() {
    dbinfo := fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable",
        DBUser, DBPassword, DBName)
    db, err := sql.Open("postgres", dbinfo)

    PostgreSQLDB = db
    checkPostgreSQLErr(err)
}

func checkPostgreSQLErr(err error) {
    if err != nil {
        panic(err)
    }
}
```

由于我是初学者，一些大胆的尝试，可能存在规范上或者架构上的问题，还请多多指教。  
我这里之所以这样建立，本着代码分离的原则，不希望在每个使用数据库的地方都重复写一边代码，这里会不会存在重复创建连接，导致内存崩溃还有待继续深入学习。  
好了，废话不多说了，这里创建了一个PostgreSQLDBB，首先说下init这个函数的作用

> init函数是用于程序执行前做包的初始化的函数，比如初始化包里的变量等

也就是所每次使用PostgreSQLDB的时候都会去连接下数据库

这就说明了，每次使用PostgreSQLDB的时候，PostgreSQLDB都是一个连接了的，方便后面的调用。

### 创建model

由于以前都是写PHP的，大多数使用的也都是MVC，所以我这里在项目目录下建立了一个models文件夹，然后创建一个blog.go文件，里面的代码如下

```go
package models

import (
    "database/sql"

    "github.com/durban89/wiki/db"
)

// Conn 连接
var Conn *sql.DB

func init() {
    // MySQL
    // Conn = db.DB
    // SQLite
    // Conn = db.SQLiteDB
    // PostgreSQL
    Conn = db.PostgreSQLDB
}

// Query 获取一条数据
func Query() ([]string, error) {
    rows, err := Conn.Query("SELECT * FROM blog")

    if err != nil {
        return nil, err
    }

    var res = []string{}

    for rows.Next() {
        var autokid int
        var title string
        err = rows.Scan(&autokid, &title)

        if err != nil {
            return nil, err
        }
        res = append(res, title)
    }

    return res, nil
}
```

### 数据库创建

创建数据库blog

```sql
CREATE TABLE blog (
    autokid SERIAL PRIMARY KEY,
    title VARCHAR(100)
);
```

添加测试数据

```sql
INSERT INTO blog(title) VALUES('title1');
INSERT INTO blog(title) VALUES('title2');
INSERT INTO blog(title) VALUES('title3');
```

### 单元测试

下面创建测试单元，测试下我们的Query函数是否能获取到数据，创建blog\_test.go文件(如果不存在)，跟blog.go文件放在一起，代码内容如下

```go
package models

import (
    "testing"
)

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

    }

    for i, k := range row {
        t.Log(i)
        t.Log(k)
    }
}
```

当我们在models目录下进行测试的时候，会得到如下输出，说明我们的功能是正常的

```bash
$ go test
PASS
ok      github.com/durban89/wiki/models 0.023s
```

请注意，PostgreSQL使用$1，$2格式而不是MySQL使用的?，它在sql.Open中有不同的DSN格式。另一件事是PostgreSQL驱动程序不支持sql.Result.LastInsertId()。所以不是这样，

```go
// Create 添加一条记录
func Create(title string) {
    var lastInsertID int
    err := PostgreSQLDB.QueryRow("INSERT INTO blog(title) VALUES($1) returning autokid;", title).Scan(&lastInsertID)
    checkPostgreSQLErr(err)
    fmt.Println("last inserted id =", lastInsertID)
}
```

使用db.QueryRow()和.Scan()来获取最后插入的id的值。

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.11
```
