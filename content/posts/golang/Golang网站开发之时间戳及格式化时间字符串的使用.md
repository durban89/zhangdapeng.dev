---
title: "Golang网站开发之时间戳及格式化时间字符串的使用"
date: "2025-08-04 18:07:43"
slug: "golang-wang-zhan-kai-fa-zhi-shi-jian-chuo-ji-ge-shi-hua-shi-jian-zi-fu-chuan-de-shi-yong"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之时间戳及格式化时间字符串的使用/"
  - "/2025/08/04/Golang网站开发之时间戳及格式化时间字符串的使用.html"
  - "/Golang网站开发之时间戳及格式化时间字符串的使用/"
  - "/Golang网站开发之时间戳及格式化时间字符串的使用.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-shi-jian-chuo-ji-ge-shi-hua-shi-jian-zi-fu-chuan-de-shi-yon/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-shi-jian-chuo-ji-ge-shi-hua-shi-jian-zi-fu-chuan-de-shi.html"
  - "/golang-wang-zhan-kai-fa-zhi-shi-jian-chuo-ji-ge-shi-hua-shi-jian-zi-fu-chuan-de-shi-yong.html"
---
在其他语言中，进行web开发的时候，比如做创建一条记录的时候，需要我们自己传入时间戳或者是时间字符串的话，我们应该如何操作呢

如果是PHP的话

时间戳

```go
timestamp = time()
```

or

```go
timestamp = strtotime('2019-12-09 14:28:20')
```

格式化时间

```go
date = date('Y-m-d H:i:s', time())
```

那么在Python中的话

时间戳

```go
import time
timestamp = int(time.time())
```

or

```go
import time
t = time.strptime('2019-12-09 14:28:20', "%Y-%m-%d %H:%M:%S")
timestamp = int(time.mktime(t))
```

格式化时间

```go
from datetime import datetime
dt = datetime.today()
date = dt.strftime("%Y-%m-%d %H:%M:%S")
```

or

```go
from datetime import datetime
dt = datetime.fromtimestamp(1575872705)
date = dt.strftime("%Y-%m-%d %H:%M:%S")
```

那么在golang中应该如何实现时间戳与时间格式化字符串间的转换呢

时间戳

```go
import (
	"time"
)

t := time.Now()
timestamp := t.Unix()
```

or

```go
import (
	"time"
)

t1, _ := time.Parse("2006-01-02 15:04:05", "2019-12-09 13:49:53")
timestamp1 := t1.Unix()
```

格式化字符串

```go
import (
	"time"
)

t := time.Now()
timeStr := t.Format("2006-01-02 15:04:05")
```

or

```go
import (
	"time"
)

t1, _ := time.Parse("2006-01-02 15:04:05", "2019-12-09 13:49:53")
timeStr := t1.Format("2006-01-02 15:04:05")
```

这里你会发现个奇怪的问题就是，这里面的格式化字符串是一个数字组成的“2006-01-02 15:04:05”并不是“%Y-%m-%d %H:%M:%S”，也不是“Y-m-d H:i:s”

具体可以参考这里

<https://pkg.go.dev/time?tab=doc#pkg-constants>

也有网友给大家总结了下，详见<https://www.cnblogs.com/baiyuxiong/p/4349595.html>

我这里子列出下

> 月份 1,01,Jan,January

> 日　 2,02,\_2

> 时　 3,03,15,PM,pm,AM,am

> 分　 4,04

> 秒　 5,05

> 年　 06,2006

> 周几 Mon,Monday

> 时区时差表示 -07,-0700,Z0700,Z07:00,-07:00,MST

> 时区字母缩写 MST

官方原文的介绍如下

> The layout string used by the Parse function and Format method shows by example how the reference time should be represented. We stress that one must show how the reference time is formatted, not a time of the user's choosing. Thus each layout string is a representation of the time stamp,

> Jan 2 15:04:05 2006 MST

> An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above):

> 1 2 3 4 5 6 -7

> There are some wrinkles illustrated below.
