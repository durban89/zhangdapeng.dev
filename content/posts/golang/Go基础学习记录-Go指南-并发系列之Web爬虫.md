---
title: "Go基础学习记录 - Go指南 - 并发系列之Web爬虫"
date: "2025-07-31 10:27:06"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-web-pa-chong"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之Web爬虫/"
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之Web爬虫.html"
  - "/Go基础学习记录-Go指南-并发系列之Web爬虫/"
  - "/Go基础学习记录-Go指南-并发系列之Web爬虫.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-web-pa-chong/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-web-pa-chong.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-web-pa-chong.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

## **Web爬虫**

在这个实例练习中将会使用 Go 的并发特性来并行化一个 Web 爬虫。修改 Crawl 函数来并行地抓取 URL，并且保证不重复。提示： 可以用一个 map 来缓存已经获取的 URL，但是要注意 map 本身并不是并发安全的！官方的给的实例演示如下

```go
package main

import (
    "fmt"
)

type Fetcher interface {
    // Fetch 返回 URL 的 body 内容，并且将在这个页面上找到的 URL 放到一个 slice 中。
    Fetch(url string) (body string, urls []string, err error)
}

// Crawl 使用 fetcher 从某个 URL 开始递归的爬取页面，直到达到最大深度。
func Crawl(url string, depth int, fetcher Fetcher) {
    // TODO: 并行的抓取 URL。
    // TODO: 不重复抓取页面。
    // 下面并没有实现上面两种情况：
    if depth <= 0 {
        return
    }
    body, urls, err := fetcher.Fetch(url)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Printf("found: %s %q\n", url, body)
    for _, u := range urls {
        Crawl(u, depth-1, fetcher)
    }
    return
}

func main() {
    Crawl("http://golang.org/", 4, fetcher)
}

// fakeFetcher 是返回若干结果的 Fetcher。
type fakeFetcher map[string]*fakeResult

type fakeResult struct {
    body string
    urls []string
}

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
    if res, ok := f[url]; ok {
        return res.body, res.urls, nil
    }
    return "", nil, fmt.Errorf("not found: %s", url)
}

// fetcher 是填充后的 fakeFetcher。
var fetcher = fakeFetcher{
    "http://golang.org/": &fakeResult{
        "The Go Programming Language",
        []string{
            "http://golang.org/pkg/",
            "http://golang.org/cmd/",
        },
    },
    "http://golang.org/pkg/": &fakeResult{
        "Packages",
        []string{
            "http://golang.org/",
            "http://golang.org/cmd/",
            "http://golang.org/pkg/fmt/",
            "http://golang.org/pkg/os/",
        },
    },
    "http://golang.org/pkg/fmt/": &fakeResult{
        "Package fmt",
        []string{
            "http://golang.org/",
            "http://golang.org/pkg/",
        },
    },
    "http://golang.org/pkg/os/": &fakeResult{
        "Package os",
        []string{
            "http://golang.org/",
            "http://golang.org/pkg/",
        },
    },
}
```

官方给的例子实际上并没有做抓取的操作这个，后面学习深入后跟大家分享，其实就是一个简单的，数组循环而已，但是模仿着写一下会增进自己对golang的掌握，下面是我自己模仿的

```go
package main

import "fmt"

// FetcherResult 抓取结果
type FetcherResult struct {
    body string
    urls []string
}

// Fetcher 接口
type Fetcher interface {
    // 通过给定的url地址，返回抓取的body并返回body中的url地址
    Fetch(url string) (body string, urls []string, err error)
}

type runFetcher map[string]*FetcherResult

func (r runFetcher) Fetch(url string) (body string, urls []string, err error) {
    if res, ok := r[url]; ok {
        return res.body, res.urls, nil
    }

    return "", nil, fmt.Errorf("not found: %s", url)
}

// Crawl 抓取每个url地址
func Crawl(url string, depth int, fetcher Fetcher) {
    if depth < 0 {
        return
    }

    body, urls, err := fetcher.Fetch(url)

    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Printf("Found %s %q \n", url, body)

    for _, nurl := range urls {
        Crawl(nurl, depth, fetcher)
    }

    return
}

// 结果存储器
var fakeFecher = runFetcher{
    "https://baidu.com": &FetcherResult{
        "page1",
        []string{
            "https://baidu.com/page1",
            "https://baidu.com/page2",
            "https://baidu.com/page3",
        },
    },
    "https://baidu.com/page1": &FetcherResult{
        "page1",
        []string{
            "https://baidu.com/page1/11",
        },
    },
    "https://baidu.com/page2": &FetcherResult{
        "page2",
        []string{
            "https://baidu.com/page2/21",
        },
    },
    "https://baidu.com/page3": &FetcherResult{
        "page3",
        []string{
            "https://baidu.com/page31",
        },
    },
}

func main() {
    // 启动抓取某个网站，这里抓取百度
    Crawl("https://baidu.com", 2, fakeFecher)
}
```

开始的时候并没有看到这里

```go
if res, ok := r[url]; ok {
    return res.body, res.urls, nil
}
```

这部分

```go
r[url]
```

最后自己写完之后，突然醒悟原来就是数组里取值而已。  
到这里基本上官网的基础教程也学习完毕了，光掌握知识是不够的，咱们还是要做一些实践加深下对golang的掌握，接下来我会以官方文档为参考做一个小的博客，已分享给大家，且为自己掌握golang做进一步深入学习。
