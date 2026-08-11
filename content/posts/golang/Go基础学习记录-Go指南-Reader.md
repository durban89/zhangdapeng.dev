---
title: "Go基础学习记录 - Go指南 - Reader"
date: "2025-07-31 10:26:16"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-reader"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-Reader/"
  - "/2025/07/31/Go基础学习记录-Go指南-Reader.html"
  - "/Go基础学习记录-Go指南-Reader/"
  - "/Go基础学习记录-Go指南-Reader.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-reader/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-reader.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-reader.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **Reader**

io 包指定了 io.Reader 接口， 它表示从数据流的末尾进行读取。

Go 标准库包含了该接口的许多实现， 包括文件、网络连接、压缩和加密等等。

io.Reader 接口有一个 Read 方法：

```go
func (T) Read(b []byte) (n int, err error)
```

Read 用数据填充给定的字节切片并返回填充的字节数和错误值。 在遇到数据流的结尾时，它会返回一个 io.EOF 错误。实例演示如下

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    r := strings.NewReader("Come! World!")
    b := make([]byte, 8)
    for {
        n, err := r.Read(b)
        fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
        fmt.Printf("b[:n] = %q\n", b[:n])
        if err == io.EOF {
            break
        }
    }
}
```

示例代码创建了一个 strings.Reader 并以每次 8 字节的速度读取它的输出。

### **练习：Reader**

实现一个 Reader 类型，它产生一个 ASCII 字符 'A' 的无限流。

```go
package main

import "github.com/Go-zh/tour/reader"

type MyReader struct{}

// TODO: Add a Read([]byte) (int, error) method to MyReader.

func (a MyReader) Read(b []byte) (int, error) {
    b[0] = 'A'
    return 1, nil // 1表示一个字符
}

func main() {
    reader.Validate(MyReader{})
}
```

### **练习：rot13Reader**

有种常见的模式是一个 io.Reader 包装另一个 io.Reader ，然后通过某种方式修改其数据流。

例如，gzip.NewReader 函数接受一个 io.Reader （已压缩的数据流）并返回一个同样实现了 io.Reader 的 \*gzip.Reader （解压后的数据流）。

编写一个实现了 io.Reader 并从另一个 io.Reader 中读取数据的 rot13Reader ， 通过应用 rot13 代换密码对数据流进行修改。

rot13Reader 类型已经提供。实现 Read 方法以满足 io.Reader 。关于rot13的解释，可以到[ROT13](https://en.wikipedia.org/wiki/ROT13)了解。我的练习如下

```go
package main

import (
    "io"
    "os"
    "strings"
)

type rot13Reader struct {
    r io.Reader
}

func (r *rot13Reader) Read(b []byte) (int, error) {
    n, err := r.r.Read(b)

    if err != nil {
        return n, err
    }

    for i := 0; i < len(b); i++ {
        if (b[i] >= 'A' && b[i] <= 'M') || (b[i] >= 'a' && b[i] <= 'm') {
            b[i] += 13
        } else if (b[i] >= 'N' && b[i] <= 'Z') || (b[i] >= 'n' && b[i] <= 'z') {
            b[i] -= 13
        }
    }

    return n, err
}

func main() {
    s := strings.NewReader("Lbh penpxrq gur pbqr!")
    r := rot13Reader{s}
    io.Copy(os.Stdout, &r)
}
```

我们主要实现的逻辑是下面的逻辑

```bash
---------------------------------------------------------
输入|ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
---------------------------------------------------------
输出|NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm
---------------------------------------------------------
```

输入A的时候我们要转换N，依次类推
