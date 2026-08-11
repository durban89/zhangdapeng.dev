---
title: "Golang 解决国内下载慢的问题（goproxy 代理）"
date: "2025-08-04 18:08:23"
slug: "golang-jie-jue-guo-nei-xia-zai-man-de-wen-ti-goproxy-dai-li"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang-解决国内下载慢的问题（goproxy-代理）/"
  - "/2025/08/04/Golang-解决国内下载慢的问题（goproxy-代理）.html"
  - "/Golang-解决国内下载慢的问题（goproxy-代理）/"
  - "/Golang-解决国内下载慢的问题（goproxy-代理）.html"
  - "/2025/08/04/Golang-解决国内下载慢的问题-goproxy-代理/"
  - "/2025/08/04/Golang-解决国内下载慢的问题-goproxy-代理.html"
  - "/2025/08/04/golang-jie-jue-guo-nei-xia-zai-man-de-wen-ti-goproxy-dai-li/"
  - "/2025/08/04/golang-jie-jue-guo-nei-xia-zai-man-de-wen-ti-goproxy-dai-li.html"
  - "/golang-jie-jue-guo-nei-xia-zai-man-de-wen-ti-goproxy-dai-li.html"
---
解决方案 **GOPROXY 环境变量**

GOPROXY 环境变量。如果设置了该变量，下载源代码时将会通过这个环境变量设置的代理地址，而不再是以前的直接从代码库下载

下面看下如何设置

```bash
export GOPROXY=https://goproxy.io
```

也可以通过置空这个环境变量来关闭，

```bash
export GOPROXY=
```

不过使用GOPROXY的前提是要开启下面这个

```bash
export GO111MODULE=on
```

如果你使用的 Golang 版本>=1.13, 你可以通过设置`GOPRIVATE`环境变量来控制哪些私有仓库和依赖(公司内部仓库)不通过 proxy 来拉取，直接走本地，设置如下：

```bash
go env -w GOPROXY=https://goproxy.io,direct
# 设置不走 proxy 的私有仓库，多个用逗号相隔
go env -w GOPRIVATE=*.corp.example.com
```

另外再推荐一个国内的 <https://goproxy.cn>
