---
title: "Go基础学习记录 - 编写Web应用程序 - 数据库(二)"
date: "2025-08-01 10:31:32"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(二)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(二).html"
  - "/Go基础学习记录-编写Web应用程序-数据库(二)/"
  - "/Go基础学习记录-编写Web应用程序-数据库(二).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-二/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-er/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-er.html"
---
本次分享下 -- MySQL数据库驱动程序

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.8
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.8
```

这些我觉得 够清晰了。OK！

继续"MySQL数据库驱动程序"的分享。

## 数据库

对于Web开发人员而言，数据库是Web开发的核心。  
您几乎可以将任何内容保存到数据库中，并查询或更新其中的数据，如用户信息，产品或新闻文章。  
Go不提供任何数据库驱动程序，但它确实在database/sql包中定义了驱动程序接口。  
我们可以基于该接口开发数据库驱动程序。首先先看下 “MySQL的数据库驱动程序”

### MySQL数据库驱动程序

LAMP堆栈近年来在互联网上非常流行，而LAMP中的M代表MySQL。  
MySQL很有名，因为它是开源的，易于使用。  
因此，它已成为许多网站后端的事实上的数据库。

### **MySQL drivers**

在Go中有几个支持MySQL的驱动程序。  
其中一些实现了database/sql接口，而另一些则使用自己的接口标准。

* https://github.com/go-sql-driver/mysql 支持用纯Go编写的database/sql.
* https://github.com/ziutek/mymysql 支持用纯Go编写的database/sql和用户定义的接口。

我将在以下示例中使用第一个驱动程序（我也在我的个人项目中使用此驱动程序），并且我还建议您使用它，原因如下：

* 它是一个新的数据库驱动程序，支持更多功能。
* 它完全支持database/sql接口标准。
* 支持keep-alive，长线程与线程安全。

### **Samples 实例演示**

**安装MySQL驱动**

如果本地没有安装的话，先去安装下这个包，安装命令如下

```bash
go get github.com/go-sql-driver/mysql
```

**添加MySQL驱动连接**项目目录下创建一个文件夹db，db中创建一个文件mysql.go，文件内容如下

```go
package db

import (
    "database/sql"

    // Register MySQL
    _ "github.com/go-sql-driver/mysql"
)

// DB Conn
var DB *sql.DB

func init() {
    db, err := sql.Open("mysql", "root:123456@/wiki?charset=utf8")
    DB = db
    checkErr(err)
}

func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}
```

由于我是初学者，一些大胆的尝试，可能存在规范上或者架构上的问题，还请多多指教。  
我这里之所以这样建立，本着代码分离的原则，不希望在每个使用数据库的地方都重复写一边代码，这里会不会存在重复创建连接，导致内存崩溃还有待继续深入学习。  
好了，废话不多说了，这里创建了一个DB，首先说下init这个函数的作用

> init函数是用于程序执行前做包的初始化的函数，比如初始化包里的变量等

也就是所每次使用DB的时候都会去连接下数据库

这就说明了，每次使用DB的时候，DB都是一个连接了的，方便后面的调用。

**创建model**由于以前都是写PHP的，大多数使用的也都是MVC，所以我这里在项目目录下建立了一个models文件夹，然后创建一个blog.go文件，里面的代码如下

```go
package models

import (
    "github.com/durban89/wiki/db"
    // Register MySQL
    _ "github.com/go-sql-driver/mysql"
)

// Query 获取数据
func Query() ([]string, error) {
    rows, err := db.DB.Query("SELECT * FROM blog")

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

**数据库创建**

创建数据库blog

```sql
CREATE TABLE `blog` (
  `autokid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`autokid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
```

添加测试数据

```sql
INSERT INTO `blog` (`autokid`, `title`)
VALUES
    (1, 'title1'),
    (2, 'title2');
```

**单元测试**下面创建测试单元，测试下我们的Query函数是否能获取到数据，创建blog\_test.go文件，跟blog.go文件放在一起，代码内容如下

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

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.9
```
