---
title: "Golang之微信【订阅通知】开发 - 上"
date: "2025-08-05 11:37:05"
slug: "golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-shang"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang之微信【订阅通知】开发-上/"
  - "/2025/08/05/Golang之微信【订阅通知】开发-上.html"
  - "/Golang之微信【订阅通知】开发-上/"
  - "/Golang之微信【订阅通知】开发-上.html"
  - "/2025/08/05/Golang之微信-订阅通知-开发-上/"
  - "/2025/08/05/Golang之微信-订阅通知-开发-上.html"
  - "/2025/08/05/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-shang/"
  - "/2025/08/05/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-shang.html"
  - "/golang-zhi-wei-xin-ding-yue-tong-zhi-kai-fa-shang.html"
---
想要开发订阅通知的功能先要了解订阅通知开发的流程

第一步：发消息给用户  
第二步：用户通过消息交互订阅通知  
第三步：如果用户同意订阅通知，给用户发送通知消息

发消息给用户的操作可以看我前面讲过的文章

* [微信公众号消息接收与回复golang代码演示](https://www.xiaorongmao.com/blog/159 "微信公众号消息接收与回复golang代码演示")

这里要说下，需要发什么消息给用户

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1710936271/xiaorongmao/20240320/2024-03-20_19-20.png "" %}

前面文章的代码片段

```go
var item = []ReturnPicNewsItem{
    {
        Title:       "xxx",
        Description: "xxx",
        PicUrl:      "xxx.jpg",
        Url:         "https://mp.weixin.qq.com/mp/subscribemsg?action=get_confirm&appid=xxx&scene=1000&template_id=xxx&redirect_url=xxx&reserved=xxx#wechat_redirect",
    },
}
```

主要是注意这里面的Url值

```bash
https://mp.weixin.qq.com/mp/subscribemsg?action=get_confirm&appid=xxx&scene=1000&template_id=xxx&redirect_url=xxx&reserved=xxx#wechat_redirect
```

这个是请求订阅的

请注意里面的几个参数

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1710936271/xiaorongmao/20240320/2024-03-20_19-31.png "" %}

好了到这里，只要消息发出去用户就可以收到了

用户收到消息之后，用户同意或取消授权后会返回相关信息，并把结果返回给上面步骤请求时添加的redirect\_url对应的地址

会返回哪些参数

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1710936271/xiaorongmao/20240320/2024-03-20_19-31_1.png "" %}

下面看下如何来接收参数

```go
params := c.Request.URL.Query()
action := params.Get("action")
openid := params.Get("openid")
reserved := params.Get("reserved")
scene := params.Get("scene")
templateId := params.Get("template_id")
```

拿到参数之后就可以进行相应的逻辑处理

比如我这里的操作

如果不是同意订阅操作我就直接返回消息订阅失败的页面

```go
if action != "confirm" {
    c.HTML(http.StatusOK, "index.tmpl", gin.H{
        "title": "订阅未成功",
    })

    return
}
```

如果同意订阅的话，先判断是否曾经订阅过，没有订阅过，创建新的记录，并标记已订阅  
如果订阅过，并且已经处理回复了订阅消息，则进行消息的更新  
如果订阅过，并且还没进行回复，则直接返回消息订阅成功的页面

```go
// 查询是否已经有了一个未处理的 防止重复

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

c.HTML(http.StatusOK, "index.tmpl", gin.H{
    "title": "订阅成功",
})
```

index.tmpl文件代码如下

```html
<html>
    <head>
        <title>
        {{ .title }}
        </title>
    </head>

    <body>
        <h1 style='text-align:center'>
            {{ .title }}
        </h1>
        <p style='text-align:center'>订阅结果已收到，请关闭页面</p>
    </body>
</html>
```

接收订阅的消息逻辑处理步骤暂时就这些  
后面我们梳理下如何对已经订阅的用户进行消息回复处理
