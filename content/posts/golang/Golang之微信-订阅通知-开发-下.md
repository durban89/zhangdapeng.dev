---
title: "Golang之微信【订阅通知】开发 - 下"
date: "2025-08-05 11:37:08"
slug: "golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-xia"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang之微信【订阅通知】开发-下/"
  - "/2025/08/05/Golang之微信【订阅通知】开发-下.html"
  - "/Golang之微信【订阅通知】开发-下/"
  - "/Golang之微信【订阅通知】开发-下.html"
  - "/2025/08/05/Golang之微信-订阅通知-开发-下/"
  - "/2025/08/05/Golang之微信-订阅通知-开发-下.html"
  - "/2025/08/05/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-xia/"
  - "/2025/08/05/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-xia.html"
  - "/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-xia.html"
---
想要开发订阅通知的功能先要了解订阅通知开发的流程

第一步：发消息给用户  
第二步：用户通过消息交互订阅通知  
第三步：如果用户同意订阅通知，给用户发送通知消息

前面两步可以回顾前面发的文章

* [微信公众号消息接收与回复golang代码演示](https://www.xiaorongmao.com/blog/159 "微信公众号消息接收与回复golang代码演示")
* [Golang之微信【订阅通知】开发 -](https://www.xiaorongmao.com/blog/159 "微信公众号消息接收与回复golang代码演示")[上](https://www.xiaorongmao.com/blog/164)

这里要说下，如何给订阅的用户发送消息

上一篇文章已经提到过如何处理用户的订阅信息

```go
var wxSubscribe wx_subscribe.WxSubscribe

mysql.MasterCon().Where("openid = ?", openid).First(&wxSubscribe)

if wxSubscribe.Autokid == 0 {
    mysql.MasterCon().Create(&wx_subscribe.WxSubscribe{
        Action:     action,
        Openid:     openid,
        Scene:      scene,
        TemplateId: templateId,
        Ctime:      time.Now().Unix(),
    })
} else if wxSubscribe.Autokid > 0 && wxSubscribe.TheStatus == 1 {
    wxSubscribe.TheStatus = 0
    wxSubscribe.Ctime = time.Now().Unix()
    mysql.MasterCon().Save(wxSubscribe)
}
```

根据状态the\_status查到订阅未发送消息的记录，根据记录中的openid，进行用户消息的发送

```go
var wxSubscribe wx_subscribe.WxSubscribe
mysql.MasterCon().Where("the_status = ?", 0).First(&wxSubscribe)
```

进行下一步操作之前先看下需要什么接口，并且接口需要什么参数

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1711605780/xiaorongmao/2024-03-20_19-32.png "" %}

看下参数的说明

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1711605487/xiaorongmao/2024-03-20_19-32_1.png "" %}

先来获取下token

```go
accessToken := getAccessToken()
```

关于获取token的方法参考这篇文章 [Golang之微信【获取接口调用凭据】开发](https://www.xiaorongmao.com/blog/163 "Golang之微信【获取接口调用凭据】开发")

```go
url := "https://api.weixin.qq.com/cgi-bin/message/template/subscribe"
params := utils.H{
	"touser":      openid,
	"template_id": templateId,
	"scene":       scene,
	"title":       "订阅测试",
	"data": utils.H{
		"content": utils.H{
			"value": "VALUE",
			"color": "COLOR",
		},
	},
}
```

创建请求地址和请求需要传递的参数

```go
jsonEncodeData := utils.JsonEncode(params)
requestBody := strings.NewReader(jsonEncodeData)
```

参数类型转换

```go
request, err := http.NewRequest("POST", url, requestBody)

if err != nil {
	log.ErrorLogger.H(tag, utils.H{"error": err})
	return
}
```

创建请求，同时检测是否有异常

```go
q := request.URL.Query()
q.Add("access_token", accessToken)
request.URL.RawQuery = q.Encode()
```

添加token的请求参数，我用这个方式，是比较“科学”的方式，也可以在前面创建url参数的时候拼接下
