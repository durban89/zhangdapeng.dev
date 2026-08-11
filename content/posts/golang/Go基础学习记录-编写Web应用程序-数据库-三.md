---
title: "Go基础学习记录 - 编写Web应用程序 - 数据库(三)"
date: "2025-08-01 10:31:35"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-san"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(三)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(三).html"
  - "/Go基础学习记录-编写Web应用程序-数据库(三)/"
  - "/Go基础学习记录-编写Web应用程序-数据库(三).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-三/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-三.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-san/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-san.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-san.html"
---
本次分享下 -- SQLite数据库驱动程序

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.9
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.9
```

这些我觉得 够清晰了。OK！

继续分享"数据库"的分享。

## **数据库**

对于Web开发人员而言，数据库是Web开发的核心。  
您几乎可以将任何内容保存到数据库中，并查询或更新其中的数据，如用户信息，产品或新闻文章。  
Go不提供任何数据库驱动程序，但它确实在database/sql包中定义了驱动程序接口。  
我们可以基于该接口开发数据库驱动程序。今天看下 “SQLite数据库驱动程序”

### **SQLite数据库驱动程序**

SQLite是一个开源的嵌入式关系数据库。它具有自包含，零配置和事务支持的数据库引擎。其特点是便携性高，使用方便，紧凑，高效，可靠。在大多数情况下，您只需要SQLite的二进制文件来创建，连接和操作数据库。如果您正在寻找嵌入式数据库解决方案，SQLite值得考虑。你可以说SQLite是Access的开源版本。

### **SQLite drivers**

SQL中有许多用于Go的数据库驱动程序，但其中许多不支持database/sql接口标准。

* https://github.com/mattn/go-sqlite3 基于cgo的， 支持database/sql
* https://github.com/feyeleanor/gosqlite3 基于cgo的， 不支持database/sql
* https://github.com/phf/go-sqlite3 基于cgo的， 不支持database/sql

第一个驱动程序是唯一一个在其SQLite驱动程序中支持database/sql接口标准的驱动程序，因此我在本次分享中使用它 - 具体的一些详细的逻辑可以拉取实例代码查看。

## **Samples 实例演示**

### **安装MySQL驱动**

如果本地没有安装的话，先去安装下这个包，安装命令如下

```bash
go get github.com/mattn/go-sqlite3
```

### **添加SQLites3驱动连接**

项目目录下创建一个文件夹db，db中创建一个文件 `sqlite.go`，文件内容如下

```go
package db

import (
    "database/sql"

    // Register SQLite
    _ "github.com/mattn/go-sqlite3"
)

// SQLiteDB Conn
var SQLiteDB *sql.DB

func init() {
    db, err := sql.Open("sqlite3", "../data/data.db")
    SQLiteDB = db
    checkSQLiteErr(err)
}

// CreateTable 创建数据库表
func CreateTable(sql string) {
    _, error := SQLiteDB.Exec(sql)

    checkSQLiteErr(error)
}

func checkSQLiteErr(err error) {
    if err != nil {
        panic(err)
    }
}
```

由于我是初学者，一些大胆的尝试，可能存在规范上或者架构上的问题，还请多多指教。  
我这里之所以这样建立，本着代码分离的原则，不希望在每个使用数据库的地方都重复写一边代码，这里会不会存在重复创建连接，导致内存崩溃还有待继续深入学习。  
好了，废话不多说了，这里创建了一个SQLiteDBB，首先说下init这个函数的作用

> init函数是用于程序执行前做包的初始化的函数，比如初始化包里的变量等

也就是所每次使用SQLiteDB的时候都会去连接下数据库

这就说明了，每次使用SQLiteDB的时候，SQLiteDB都是一个连接了的，方便后面的调用。

### **创建model**

由于以前都是写PHP的，大多数使用的也都是MVC，所以我这里在项目目录下建立了一个models文件夹，然后创建一个blog.go文件，里面的代码如下

```go
package models

import (
    "database/sql"

    "github.com/durban89/wiki/db"
    // Register MySQL
    _ "github.com/go-sql-driver/mysql"
)

// Conn 连接
var Conn *sql.DB

func init() {
    // Conn = db.DB
    Conn = db.SQLiteDB
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

### **数据库创建**

创建数据库blog

```sql
CREATE TABLE `blog` (
    `autokid` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(100) NULL
)
```

添加测试数据

```sql
insert into blog (title) values ('title1');
insert into blog (title) values ('title2');
```

### **单元测试**

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

基本的使用功能就介绍到这里，肯定会有一些更加复杂的，比如增删改查等等，只要我们知道了如何连接数据库，其实增删改查之类的操作，就可以进行简单的封装了。我这边会将这些小功能放到github上供大家参考

您可能已经注意到代码与上一篇文章【[Go基础学习记录 - 编写Web应用程序 - 数据库(二)](https://www.xiaorongmao.com/blog/62)】中的代码几乎相同，并且我们只更改了已注册驱动程序的名称并调用了sql.Open以不同的方式连接到SQLite。

上面的示例显示了如何从数据库中获取数据，但是当您想要编写Web应用程序时，不仅需要从数据库中获取数据，而且还需要将数据写入其中。  
为此，您应该使用事务，因为由于各种原因，例如具有访问数据库的多个go例程，数据库可能会被锁定。  
这在Web应用程序中是不可取的，并且使用事务可以有效地确保数据库活动完全通过或完全失败，具体取决于具体情况。  
很明显，使用事务可以防止Web应用程序出现很多问题，实例代理如下

```go
// Update 更新
func Update(autokid int) {
    trashSQL, err := SQLiteDB.Prepare("update blog set is_deleted='Y',last_modified_at=datetime() where id=?")
    if err != nil {
        checkSQLiteErr(err)
    }
    tx, err := SQLiteDB.Begin()
    if err != nil {
        checkSQLiteErr(err)
    }
    _, err = tx.Stmt(trashSQL).Exec(autokid)
    if err != nil {
        fmt.Println("doing rollback")
        tx.Rollback()
    } else {
        tx.Commit()
    }
}
```

从上面的代码块中可以清楚地看到，首先准备一个语句，然后根据该执行的输出执行它，然后将其回滚或提交。

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.10
```
