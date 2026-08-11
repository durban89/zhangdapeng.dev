---
title: "微信公众号消息接收与回复golang代码演示"
date: "2025-08-05 09:49:14"
slug: "wei-xin-gong-zhong-hao-xiao-xi-jie-shou-yu-hui-fu-golang-dai-ma-yan-shi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/微信公众号消息接收与回复golang代码演示/"
  - "/2025/08/05/微信公众号消息接收与回复golang代码演示.html"
  - "/微信公众号消息接收与回复golang代码演示/"
  - "/微信公众号消息接收与回复golang代码演示.html"
  - "/2025/08/05/wei-xin-gong-zhong-hao-xiao-xi-jie-shou-yu-hui-fu-golang-dai-ma-yan-shi/"
  - "/2025/08/05/wei-xin-gong-zhong-hao-xiao-xi-jie-shou-yu-hui-fu-golang-dai-ma-yan-shi.html"
  - "/wei-xin-gong-zhong-hao-xiao-xi-jie-shou-yu-hui-fu-golang-dai-ma-yan-shi.html"
---
微信公众号消息接收与回复golang代码演示

首先如何解决收到的消息

先看一下接收到的消息结构体

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709118226/2024-02-28_18-02.png "" %}

根据上面的消息可以试着建立如下的结构体

```go
type ReceiveData struct {
    ToUserName   string `xml:"ToUserName"`
    FromUserName string `xml:"FromUserName"`
    CreateTime   string `xml:"CreateTime"`
    MsgType      string `xml:"MsgType"`
    Content      string `xml:"Content"`
    MsgId        string `xml:"MsgId"`
    MsgDataId    string `xml:"MsgDataId"`
    Idx          string `xml:"Idx"`
}
```

结构体建立后，如果来解析数据，这里我用到的是[gin](https://github.com/gin-gonic/gin)这个框架

```go
var receiveData ReceiveData
c.BindXML(&receiveData)
```

通过上面的代码直接绑定就可以了

调用变量的值可以通过receiveData.MsgType就可以了其他的类似

如果说接收到消息后就完事了，好像还是缺少点什么，那就是回复消息

根据回复消息的喜好，我比较喜欢图文的方式

来看下回复图文消息的结构

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709118226/2024-02-28_18-10.png "" %}

需要建立如下的结构体

图文消息信息是一个列表，那么列表中的单个结构体可以建立如下的结构

```go
type ReturnPicNewsItem struct {
    Title       string `xml:"Title"`
    Description string `xml:"Description"`
    PicUrl      string `xml:"PicUrl"`
    Url         string `xml:"Url"`
}
```

消息列表结构体如下

```go
type ReturnPicNewsNode struct {
    Item []ReturnPicNewsItem `xml:"item"`
}
```

整体的消息结构体如下

```go
type ReturnPicNewsData struct {
    XMLName      xml.Name          `xml:"xml"`
    ToUserName   string            `xml:"ToUserName"`
    FromUserName string            `xml:"FromUserName"`
    CreateTime   int64             `xml:"CreateTime"`
    MsgType      string            `xml:"MsgType"`
    ArticleCount int               `xml:"ArticleCount"`
    Articles     ReturnPicNewsNode `xml:"Articles"`
}
```

根据上面的逻辑 简单写一个小逻辑，比如根据消息的内容是”xxxxx“来返回一个图文消息

```go
if receiveData.MsgType == "text" && receiveData.Content == "xxxxx" {
    var item = []ReturnPicNewsItem{
        {
            Title:       "xxx",
            Description: "xxx",
            PicUrl:      "xxx.jpg",
            Url:         "https://mp.weixin.qq.com/mp/subscribemsg?action=get_confirm&appid=xxx&scene=1000&template_id=xxx&redirect_url=xxx&reserved=xxx#wechat_redirect",
        },
    }

    var node = ReturnPicNewsNode{
        Item: item,
    }

    var message = ReturnPicNewsData{
        ToUserName:   receiveData.FromUserName,
        FromUserName: receiveData.ToUserName,
        CreateTime:   time.Now().Unix(),
        MsgType:      "news",
        ArticleCount: 1,
        Articles:     node,
    }

    log.InfoLogger.H(tag, utils.H{
        "message": message,
    })

    c.XML(http.StatusOK, message)
} 
```

在gin的加持下，逻辑写起来还是比较顺手的

整体的代码逻辑如下，仅供参考

```go
import (
	"xxx/modules/log"
	"xxx/modules/server"
	"xxx/modules/utils"
	"encoding/xml"
	"net/http"
	"time"
)

func Message(c *server.Context) {
	type ReceiveData struct {
		ToUserName   string `xml:"ToUserName"`
		FromUserName string `xml:"FromUserName"`
		CreateTime   string `xml:"CreateTime"`
		MsgType      string `xml:"MsgType"`
		Content      string `xml:"Content"`
		MsgId        string `xml:"MsgId"`
		MsgDataId    string `xml:"MsgDataId"`
		Idx          string `xml:"Idx"`
	}

	var receiveData ReceiveData

	c.BindXML(&receiveData)

	tag := "Message"
	//body := c.Request.Body

	log.InfoLogger.H(tag, utils.H{
		"body": c.Request.Body,
		"xml":  receiveData,
	})

	type ReturnData struct {
		XMLName      xml.Name `xml:"xml"`
		ToUserName   string   `xml:"ToUserName"`
		FromUserName string   `xml:"FromUserName"`
		CreateTime   int64    `xml:"CreateTime"`
		MsgType      string   `xml:"MsgType"`
		Content      string   `xml:"Content"`
	}

	type ReturnPicNewsItem struct {
		Title       string `xml:"Title"`
		Description string `xml:"Description"`
		PicUrl      string `xml:"PicUrl"`
		Url         string `xml:"Url"`
	}

	type ReturnPicNewsNode struct {
		Item []ReturnPicNewsItem `xml:"item"`
	}

	type ReturnPicNewsData struct {
		XMLName      xml.Name          `xml:"xml"`
		ToUserName   string            `xml:"ToUserName"`
		FromUserName string            `xml:"FromUserName"`
		CreateTime   int64             `xml:"CreateTime"`
		MsgType      string            `xml:"MsgType"`
		ArticleCount int               `xml:"ArticleCount"`
		Articles     ReturnPicNewsNode `xml:"Articles"`
	}

	if receiveData.MsgType == "text" && receiveData.Content == "xxxxx" {
		var item = []ReturnPicNewsItem{
			{
				Title:       "xxx",
				Description: "xxx",
				PicUrl:      "xxx.jpg",
				Url:         "https://mp.weixin.qq.com/mp/subscribemsg?action=get_confirm&appid=xxx&scene=1000&template_id=xxx&redirect_url=xxx&reserved=xxx#wechat_redirect",
			},
		}

		var node = ReturnPicNewsNode{
			Item: item,
		}

		var message = ReturnPicNewsData{
			ToUserName:   receiveData.FromUserName,
			FromUserName: receiveData.ToUserName,
			CreateTime:   time.Now().Unix(),
			MsgType:      "news",
			ArticleCount: 1,
			Articles:     node,
		}

		log.InfoLogger.H(tag, utils.H{
			"message": message,
		})

		c.XML(http.StatusOK, message)
	} else {
		var message = ReturnData{
			ToUserName:   receiveData.FromUserName,
			FromUserName: receiveData.ToUserName,
			CreateTime:   time.Now().Unix(),
			MsgType:      "text",
			Content:      "欢迎",
		}

		c.XML(http.StatusOK, message)
	}
}
```
