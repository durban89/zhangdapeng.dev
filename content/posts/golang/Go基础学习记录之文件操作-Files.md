---
title: "Go基础学习记录之文件操作(Files)"
date: "2025-08-01 11:35:57"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-wen-jian-cao-zuo-files"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之文件操作(Files)/"
  - "/2025/08/01/Go基础学习记录之文件操作(Files).html"
  - "/Go基础学习记录之文件操作(Files)/"
  - "/Go基础学习记录之文件操作(Files).html"
  - "/2025/08/01/Go基础学习记录之文件操作-Files/"
  - "/2025/08/01/Go基础学习记录之文件操作-Files.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-wen-jian-cao-zuo-files/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-wen-jian-cao-zuo-files.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-wen-jian-cao-zuo-files.html"
---
文件是每台计算机设备上的基本对象。Web应用程序也会大量使用它们，这对您来说并不意外。如何在Go中操作文件。接下来一起学习。

## 目录

在Go中，大多数文件操作函数都位于os包中。以下是一些目录功能：

* func Mkdir(name string, perm FileMode) error // 创建一个名称目录。perm是目录权限，即0777
* func MkdirAll(path string, perm FileMode) error // 根据路径创建多个目录，如wiki/test1/test2
* func Remove(name string) error // 删除名称目录。如果它不是目录或不为空，则返回错误。
* func RemoveAll(path string) error // 根据路径删除多个目录。如果path是单个路径，则不会删除目录。

代码实例如下

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    os.Mkdir("gowhich", 0777)
    os.MkdirAll("gowhich/test1/test2", 0777)
    err := os.Remove("gowhich")
    if err != nil {
        fmt.Println(err)
    }
    os.RemoveAll("gowhich")
}
```

## 创建和打开文件

创建文件有两个功能：

* func Create(name string) (file \*File, err Error) // 创建一个带有name的文件，并返回一个具有权限0666的可读写文件对象。
* func NewFile(fd uintptr, name string) \*File // 创建一个文件并返回一个文件对象。

打开文件还有两个功能：

* func Open(name string) (file \*File, err Error) // 打开一个名为name且具有只读访问权限的文件，在封面下调用OpenFile。
* func OpenFile(name string, flag int, perm uint32) (file \*File, err Error) // 打开名为name的文件。flag是打开模式，如read-only, read-write等，perm是文件权限。

## 写文件

写文件的功能：

* func (file \*File) Write(b []byte) (n int, err Error) // 将字节类型内容写入文件。
* func (file \*File) WriteAt(b []byte, off int64) (n int, err Error) // 将字节类型内容写入文件的特定位置。
* func (file \*File) WriteString(s string) (ret int, err Error) // 将字符串写入文件。

代码实例如下

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    userFile := "gowhich.txt"
    fout, err := os.Create(userFile)        
    if err != nil {
        fmt.Println(userFile, err)
        return
    }
    defer fout.Close()
    for i := 0; i < 10; i++ {
        fout.WriteString("Only a test!\r\n")
        fout.Write([]byte("Only a test!\r\n"))
    }
}
```

## 读取文件

读取文件的功能：

* func (file \*File) Read(b []byte) (n int, err Error) // 读数据到b。
* func (file \*File) ReadAt(b []byte, off int64) (n int, err Error) // 从位置off到b读取数据。

代码实例演示如下

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    userFile := "gowhich.txt"
    fl, err := os.Open(userFile)        
    if err != nil {
        fmt.Println(userFile, err)
        return
    }
    defer fl.Close()
    buf := make([]byte, 1024)
    for {
        n, _ := fl.Read(buf)
        if 0 == n {
            break
        }
        os.Stdout.Write(buf[:n])
    }
}
```

## 删除文件

Go使用相同的功能删除文件和目录：

func Remove(name string) Error // 删除名为name的文件或目录（以/结尾的名称表示它是一个目录）
