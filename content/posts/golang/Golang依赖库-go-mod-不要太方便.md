---
title: "Golang依赖库“go mod”不要太方便"
date: "2025-08-04 18:07:58"
slug: "golang-yi-lai-ku-go-mod-bu-yao-tai-fang-bian"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang依赖库“go-mod”不要太方便/"
  - "/2025/08/04/Golang依赖库“go-mod”不要太方便.html"
  - "/Golang依赖库“go-mod”不要太方便/"
  - "/Golang依赖库“go-mod”不要太方便.html"
  - "/2025/08/04/Golang依赖库-go-mod-不要太方便/"
  - "/2025/08/04/Golang依赖库-go-mod-不要太方便.html"
  - "/2025/08/04/golang-yi-lai-ku-go-mod-bu-yao-tai-fang-bian/"
  - "/2025/08/04/golang-yi-lai-ku-go-mod-bu-yao-tai-fang-bian.html"
  - "/golang-yi-lai-ku-go-mod-bu-yao-tai-fang-bian.html"
---
Golang依赖库“go mod”不要太方便，记录下使用过程

我是在用两个版本在开发的

`go1.13.1` 和 `go1.13.5`

之前一直也没有使用什么版本库，你如govendor也只是在另外一个项目接触过

下面记录下我是如何使用的

先在go1.13.1版本下，在项目目录中`~/go/src/github.com/durban89/wiki`执行

```bash
$ export GO111MODULE=on
$ go mod init github.com/durban89/wiki
go: creating new go.mod: module github.com/durban89/wiki
```

**请注意**这里的`init`后面的目录，并不是不填写或者是项目`wiki`的名称

然后发现项目根目录下面会多两个文件

```bash
go.mod
go.sum
```

第一次使用当然好奇里面是什么了，打开看下

```bash
$ cat go.mod
module github.com/durban89/wiki

go 1.13
```

哎，为什么没有我们的依赖包，好吧，请执行下面的命令

```bash
go build ./...
```

然后会看到如下的输出

```bash
go: finding github.com/mattn/go-sqlite3 v2.0.2+incompatible
go: finding github.com/lib/pq v1.3.0
go: finding github.com/go-sql-driver/mysql v1.4.1
go: downloading github.com/mattn/go-sqlite3 v2.0.2+incompatible
go: downloading github.com/lib/pq v1.3.0
go: downloading github.com/go-sql-driver/mysql v1.4.1
go: extracting github.com/go-sql-driver/mysql v1.4.1
go: extracting github.com/lib/pq v1.3.0
go: extracting github.com/mattn/go-sqlite3 v2.0.2+incompatible
```

就是找到了三个依赖库并下载了三个并解开了三个，为什么解开？我不是已经安装了吗？这里留个*疑问*

再开下`go.mod`

```bash
$ cat go.mod
module github.com/durban89/wiki

go 1.13

require (
        github.com/go-sql-driver/mysql v1.4.1
        github.com/lib/pq v1.3.0
        github.com/mattn/go-sqlite3 v2.0.2+incompatible
)
```

再看下`go.sum`

```bash
$ cat go.sum
github.com/go-sql-driver/mysql v1.4.1 h1:g24URVg0OFbNUTx9qqY1IRZ9D9z3iPyi5zKhQZpNwpA=
github.com/go-sql-driver/mysql v1.4.1/go.mod h1:zAC/RDZ24gD3HViQzih4MyKcchzm+sOG5ZlKdlhCg5w=
github.com/lib/pq v1.3.0 h1:/qkRGz8zljWiDcFvgpwUpwIAPu3r07TDvs3Rws+o/pU=
github.com/lib/pq v1.3.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/mattn/go-sqlite3 v2.0.2+incompatible h1:qzw9c2GNT8UFrgWNDhCTqRqYUSmu/Dav/9Z58LGpk7U=
github.com/mattn/go-sqlite3 v2.0.2+incompatible/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
```

吓，终于有内容了。切换下版本试试，看看会不会自动安装

```bash
$ gvm use go1.13.5 --default
Now using version go1.13.5
```

先build下

```bash
$ go build
go: downloading github.com/go-sql-driver/mysql v1.4.1
go: downloading github.com/lib/pq v1.3.0
go: downloading github.com/mattn/go-sqlite3 v2.0.2+incompatible
go: extracting github.com/lib/pq v1.3.0
go: extracting github.com/go-sql-driver/mysql v1.4.1
go: extracting github.com/mattn/go-sqlite3 v2.0.2+incompatible
go: finding github.com/go-sql-driver/mysql v1.4.1
go: finding github.com/lib/pq v1.3.0
go: finding github.com/mattn/go-sqlite3 v2.0.2+incompatible
```

然后运行下项目

```bash
$ go run main.go
2019/12/27 18:28:52 Starting web server on :8090
```

果然很爽，爽的不要不要的，今后再也不用担心我的依赖库没有办法方便的转移了。

另外，使用go mod之后，项目之后的新的依赖库的通过命令

```bash
go get xxxxx
```

如果使用

```bash
go install xxxx
```

的话会导致新的依赖不会自动添加到go.mod文件中
