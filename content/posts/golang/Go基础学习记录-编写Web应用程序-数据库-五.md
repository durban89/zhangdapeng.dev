---
title: "Go基础学习记录 - 编写Web应用程序 - 数据库(五)"
date: "2025-08-01 10:31:49"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-wu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(五)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库(五).html"
  - "/Go基础学习记录-编写Web应用程序-数据库(五)/"
  - "/Go基础学习记录-编写Web应用程序-数据库(五).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-五/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据库-五.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-wu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-wu.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-ku-wu.html"
---
本次分享下 -- NoSQL数据库 - Redis数据库驱动程序

## **NoSQL数据库**

NoSQL数据库提供了一种存储和检索数据的机制，该机制使用比典型的关系数据库更松散的一致性模型，以实现水平扩展和更高的可用性。  
一些作者将它们称为“不仅仅是SQL”，以强调某些NoSQL系统确实允许使用类似SQL的查询语言。  
作为21世纪的C语言，Go对NoSQL数据库提供了很好的支持，包括流行的redis，mongoDB，Cassandra和Membase NoSQL数据库。

## Redis

redis是一个像Memcached这样的键值存储系统，它支持string，list，set和zset（有序集）值类型。  
redis有一些Go数据库驱动程序：

> https://github.com/gomodule/redigo  
> https://github.com/go-redis/redis  
> https://github.com/hoisie/redis  
> https://github.com/alphazero/Go-Redis  
> https://github.com/simonz05/godis

让我们看看如何使用redigo驱动程序在数据库上运行：

安装redigo：

```bash
go get github.com/gomodule/redigo
```

使用方式如下

```go
package main

import (
    "fmt"
    "github.com/gomodule/redigo"
    "os"
    "os/signal"
    "syscall"
    "time"
)

var (
    Pool *redis.Pool
)

func init() {
    redisHost := ":6379"
    Pool = newPool(redisHost)
    close()
}

func newPool(server string) *redis.Pool {

    return &redis.Pool{

        MaxIdle:     3,
        IdleTimeout: 240 * time.Second,

        Dial: func() (redis.Conn, error) {
            c, err := redis.Dial("tcp", server)
            if err != nil {
                return nil, err
            }
            return c, err
        },

        TestOnBorrow: func(c redis.Conn, t time.Time) error {
            _, err := c.Do("PING")
            return err
        },
    }
}

func close() {
    c := make(chan os.Signal, 1)
    signal.Notify(c, os.Interrupt)
    signal.Notify(c, syscall.SIGTERM)
    signal.Notify(c, syscall.SIGKILL)
    go func() {
        <-c
        Pool.Close()
        os.Exit(0)
    }()
}

func Get(key string) ([]byte, error) {

    conn := Pool.Get()
    defer conn.Close()

    var data []byte
    data, err := redis.Bytes(conn.Do("GET", key))
    if err != nil {
        return data, fmt.Errorf("error get key %s: %v", key, err)
    }
    return data, err
}

func main() {
    test, err := Get("test")
    fmt.Println(test, err)
}
```

我们可以看到在Go中操作redis非常容易，并且它具有很高的性能。  
它的客户端命令几乎与redis的内置命令相同。

## MongoDB

MongoDB（来自“humongous”）是一个由10gen开发和支持的面向文档的开源数据库系统。  
它是NoSQL系列数据库系统的一部分。MongoDB不是像在“经典”关系数据库中那样在表中存储数据，而是将结构化数据存储为具有动态模式的类似JSON的文档（MongoDB调用BSON格式），使得在某些类型的应用程序中的数据集成更容易，更快捷。

MongoDB的最佳驱动程序称为mgo，将来它可能会包含在标准库中。  
安装mgo：

```bash
go get gopkg.in/mgo.v2
```

使用方式如下

```go
package main

import (
    "fmt"
    "gopkg.in/mgo.v2"
    "gopkg.in/mgo.v2/bson"
    "log"
)

type Person struct {
    Name  string
    Phone string
}

func main() {
    session, err := mgo.Dial("server1.example.com,server2.example.com")
    if err != nil {
        panic(err)
    }
    defer session.Close()

    // Optional. Switch the session to a monotonic behavior.
    session.SetMode(mgo.Monotonic, true)

    c := session.DB("test").C("people")
    err = c.Insert(&Person{"Ale", "+55 53 8116 9639"},
        &Person{"Cla", "+55 53 8402 8510"})
    if err != nil {
        log.Fatal(err)
    }

    result := Person{}
    err = c.Find(bson.M{"name": "Ale"}).One(&result)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Phone:", result.Phone)
}
```

我们可以看到，在mgo数据库上运行时没有太大的区别;它们都是基于结构的。这是Go的做事方式。

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流
