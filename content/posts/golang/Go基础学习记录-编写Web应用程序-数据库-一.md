---
title: "Go基础学习记录 - 编写Web应用程序 - 数据库(一)"
date: "2025-08-01 10:31:29"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(一)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(一).html"
  - "/Go基础学习记录-编写Web应用程序-数据库(一)/"
  - "/Go基础学习记录-编写Web应用程序-数据库(一).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-一/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-yi.html"
---
本次分享下 - 数据库 - Go中的数据库驱动程序接口设计

## 数据库

对于Web开发人员而言，数据库是Web开发的核心。  
您几乎可以将任何内容保存到数据库中，并查询或更新其中的数据，如用户信息，产品或新闻文章。  
Go不提供任何数据库驱动程序，但它确实在database/sql包中定义了驱动程序接口。  
我们可以基于该接口开发数据库驱动程序。首先先看下 “Go中的数据库驱动程序接口设计”

### Go中的数据库驱动程序接口设计

Go不提供任何官方数据库驱动程序，不像PHP这样的其他语言。  
但是，它确实有一些数据库驱动程序接口标准，供开发人员使用。  
优点是，如果您的代码是根据这些接口标准开发的，那么如果您的数据库发生更改，则无需更改任何代码。  
让我们看看这些数据库接口标准是什么。

### **sql.Register**

当您使用第三方数据库驱动程序时，此函数位于database/sql包中，用于注册数据库驱动程序。  
所有这些都应该在init()中调用Register(name string，driver driver.Driver)函数以便自己注册。  
我们来看看相应的mymysql和sqlite3驱动代码：

```go
// https://github.com/mattn/go-sqlite3 driver
func init() {
    sql.Register("sqlite3", &SQLiteDriver{})
}

// https://github.com/mikespook/mymysql driver
// Driver automatically registered in database/sql
var d = Driver{proto: "tcp", raddr: "127.0.0.1:3306"}
func init() {
    Register("SET NAMES utf8")
    sql.Register("mymysql", &d)
}
```

我们看到所有第三方数据库驱动程序都实现了这个函数来自我注册，Go使用map来保存database/sql中的用户驱动程序。

```go
var drivers = make(map[string]driver.Driver)
drivers[name] = driver
```

因此，此注册功能可以根据需要注册多个驱动程序，每个驱动程序具有不同的名称。  
当我们使用第三方驱动程序时，我们总是会看到以下代码：

```go
import (
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
)
```

对于许多初学者来说，下划线（也称为'空白'）```\_```可能会让人感到困惑，但这是Go中的一个很棒的功能。  
我们已经知道这个下划线标识符用于从函数返回中丢弃值，并且还必须使用在Go中的代码中导入的所有包。  
因此，当空白与导入一起使用时，这意味着您需要执行该包的init()函数而不直接使用它，这非常适合注册数据库驱动程序的用例。

### **driver.Driver**

Driver是一个包含Open（名称字符串）方法的接口，该方法返回Conn接口。

```go
type Driver interface {
    Open(name string) (Conn, error)
}
```

这是一次性Conn，这意味着每个goroutine只能使用一次。  
以下代码将导致错误发生：

```go
go goroutineA (Conn)  // query
go goroutineB (Conn)  // insert
```

因为Go不知道哪个goroutine执行哪个操作，查询操作可能会得到插入操作的结果，反之亦然。  
所有第三方驱动程序都应该使用此函数来解析Conn的名称并返回正确的结果。

### **driver.Conn**

这是一个带有一些方法的数据库连接接口，正如我上面所说的，每个goroutine只能使用一次相同的Conn。

```go
type Conn interface {
    Prepare(query string) (Stmt, error)
    Close() error
    Begin() (Tx, error)
}
```

1. Prepare 返回相应SQL命令的准备状态，用于查询和删除等。
2. Close 关闭当前连接并清理资源。大多数第三方驱动程序实现某种连接池，因此您不需要缓存可能导致意外错误的连接。
3. Begin 返回表示事务句柄的Tx。您可以使用它来查询，更新，回滚事务等。

### **driver.Stmt**

这是一个与Conn对应的就绪状态，因此每个goroutine只能使用一次（与Conn一样）。

```go
type Stmt interface {
    Close() error
    NumInput() int
    Exec(args []Value) (Result, error)
    Query(args []Value) (Rows, error)
}
```

1. Close 关闭当前连接但如果正在执行查询操作，仍会返回行数据。NumInput返回专性参数的数量。数据库驱动程序应在结果大于0时检查其调用者的参数，并在数据库驱动程序不知道任何可能的参数时返回-1。
2. Exec 执行在Prepare中准备的update/insert SQL命令，返回Result。
3. Query 执行Prepare中准备的select SQL命令，返回行数据。

### **driver.Tx**

通常，事务句柄只有提交或回滚方法，而数据库驱动程序只需要实现这两种方法。

```go
type Tx interface {
    Commit() error
    Rollback() error
}
```

### **driver.Execer**

这是一个可选的接口。

```go
type Execer interface {
    Exec(query string, args []Value) (Result, error)
}
```

如果驱动程序没有实现此接口，则在调用DB.Exec时，它将自动调用Prepare，然后返回Stmt。之后，它执行Stmt的Exec方法，然后关闭Stmt。

### **driver.Result**

这是update/insert操作结果的接口。

```go
type Result interface {
    LastInsertId() (int64, error)
    RowsAffected() (int64, error)
}
```

* LastInsertId 在数据库插入操作后返回自动增量Id编号。
* RowsAffected 返回受查询操作影响的行。

### **driver.Rows**

这是查询操作结果的接口。

```go
type Rows interface {
    Columns() []string
    Close() error
    Next(dest []Value) error
}
```

* Columns 返回数据库表的字段信息。切片仅与SQL查询字段一一对应，并且不返回该数据库表的所有字段。
* Close 关闭行迭代器。
* Next 返回下一个数据并分配给dest，将所有字符串转换为字节数组，如果没有更多可用数据，则会收到io.EOF错误。

### **driver.RowsAffected**

这是int64的别名，但它实现了Result接口。

```go
type RowsAffected int64

func (RowsAffected) LastInsertId() (int64, error)

func (v RowsAffected) RowsAffected() (int64, error)
```

### **driver.Value**

这是一个空接口，可以包含任何类型的数据。

```go
type Value interface{}
```

值必须是驱动程序可以运行的值或者为零，因此它应该是以下类型之一：

```bash
int64
float64
bool
[]byte
string   [*] Except Rows.Next which cannot return string
time.Time
```

### **driver.ValueConverter**

这定义了一个用于将正常值转换为driver.Value的接口。

```go
type ValueConverter interface {
    ConvertValue(v interface{}) (Value, error)
}
```

此接口通常用于数据库驱动程序，并具有许多有用的功能：

* 将driver.Value转换为相应的数据库字段类型，例如将int64转换为uint16。
* 将数据库查询结果转换为driver.Value。
* 将driver.Value转换为scan函数中的用户定义值。

### **driver.Valuer**

这定义了一个返回driver.Value的接口。

```go
type Valuer interface {
    Value() (Value, error)
}
```

许多类型实现此接口以在driver.Value和其自身之间进行转换。

此时，您应该了解一下在Go中开发数据库驱动程序。  
一旦您可以为添加，删除，更新等操作实现接口，与特定数据库通信只会留下一些问题。

## database/sql

在database/sql/driver之上定义更多高级方法，以便更方便地进行数据库操作，并建议您实现连接池。

```go
type DB struct {
    driver   driver.Driver
    dsn      string
    mu       sync.Mutex // protects freeConn and closed
    freeConn []driver.Conn
    closed   bool
}
```

如您所见，Open函数返回一个具有freeConn的DB，这是一个简单的连接池。  
它的实现非常简单和丑陋。  
它在Db.prepare函数中使用延迟db.putConn(ci，err)将连接放入连接池。  
每次调用Conn函数时，它都会检查freeConn的长度。  
如果它大于0，则表示存在可重用的连接，并且它直接返回给您。  
否则，它会创建一个新连接并返回。

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流
