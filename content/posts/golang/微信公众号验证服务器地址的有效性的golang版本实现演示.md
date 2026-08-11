---
title: "微信公众号验证服务器地址的有效性的golang版本实现演示"
date: "2025-08-05 09:49:11"
slug: "wei-xin-gong-zhong-hao-yan-zheng-fu-wu-qi-di-zhi-de-you-xiao-xing-de-golang-ban-ben-shi-xian-yan-shi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/微信公众号验证服务器地址的有效性的golang版本实现演示/"
  - "/2025/08/05/微信公众号验证服务器地址的有效性的golang版本实现演示.html"
  - "/微信公众号验证服务器地址的有效性的golang版本实现演示/"
  - "/微信公众号验证服务器地址的有效性的golang版本实现演示.html"
  - "/2025/08/05/wei-xin-gong-zhong-hao-yan-zheng-fu-wu-qi-di-zhi-de-you-xiao-xing-de-golang-ban-ben-shi/"
  - "/2025/08/05/wei-xin-gong-zhong-hao-yan-zheng-fu-wu-qi-di-zhi-de-you-xiao-xing-de-golang-ban-ben.html"
  - "/wei-xin-gong-zhong-hao-yan-zheng-fu-wu-qi-di-zhi-de-you-xiao-xing-de-golang-ban-ben-shi-xian-y.html"
---
微信公众号验证服务器地址的有效性的golang版本代码实现演示

接入微信公众平台开发，填写服务器配置是必须的步骤，也是第一步

下面用Golang实现验证的环节

这里使用的是gin框架，免去了自己做服务底层的麻烦

首先看下，我们要写的接口具体接收哪些参数

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709541130/xiaorongmao/2024-03-04_16-12.png "" %}

从文档的上可以总结出，微信会发送四个参数

* echostr
* nonce
* signature
* timestamp

要注意这里是使用GET请求的

```go
echostr := c.Request.URL.Query().Get("echostr")
nonce := c.Request.URL.Query().Get("nonce")
signature := c.Request.URL.Query().Get("signature")
timestamp := c.Request.URL.Query().Get("timestamp")
```

看下加密/校验流程：

1）将token、timestamp、nonce三个参数进行字典序排序

```go
tmpSlice := []string{
    token,
    timestamp,
    nonce,
}

sort.Strings(tmpSlice)
```

2）将三个参数字符串拼接成一个字符串进行sha1加密

```go
tmpStr := strings.Join(tmpSlice, "")

h := sha1.New()
_, err := io.WriteString(h, tmpStr)
if err != nil {
    return
}
sign := hex.EncodeToString(h.Sum(nil))
```

3）开发者获得加密后的字符串可与signature对比，标识该请求来源于微信， 并且返回 echostr

```go
if sign == signature {
    c.Data(200, "text/html; charset=utf-8", []byte(echostr))
    return
}
```

完整的代码如下

```go
import (
	"crypto/sha1"
	"xxx/config"
	"xxx/modules/log"
	"xxx/modules/server"
	"xxx/modules/utils"
	"encoding/hex"
	"io"
	"sort"
	"strings"
)

func Check(c *server.Context) {
	log.InfoLogger.H("Check", utils.H{
		"query": c.Request.URL.Query(),
	})

	echostr := c.Request.URL.Query().Get("echostr")
	nonce := c.Request.URL.Query().Get("nonce")
	signature := c.Request.URL.Query().Get("signature")
	timestamp := c.Request.URL.Query().Get("timestamp")

	token := config.Token

	tmpSlice := []string{
		token,
		timestamp,
		nonce,
	}

	sort.Strings(tmpSlice)

	tmpStr := strings.Join(tmpSlice, "")

	h := sha1.New()
	_, err := io.WriteString(h, tmpStr)
	if err != nil {
		return
	}
	sign := hex.EncodeToString(h.Sum(nil))

	if sign == signature {
		log.InfoLogger.H("Check", utils.H{
			"status": "ok",
		})

		c.Data(200, "text/html; charset=utf-8", []byte(echostr))
		return
	}

	c.Data(200, "text/html; charset=utf-8", []byte("fail"))
	return
}
```
