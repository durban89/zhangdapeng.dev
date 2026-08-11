---
title: "Golang之微信【获取接口调用凭据】开发"
date: "2025-08-05 11:37:02"
slug: "golang-zhi-wei-xin-huo-qu-jie-kou-diao-yong-ping-ju-kai-fa"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang之微信【获取接口调用凭据】开发/"
  - "/2025/08/05/Golang之微信【获取接口调用凭据】开发.html"
  - "/Golang之微信【获取接口调用凭据】开发/"
  - "/Golang之微信【获取接口调用凭据】开发.html"
  - "/2025/08/05/Golang之微信-获取接口调用凭据-开发/"
  - "/2025/08/05/Golang之微信-获取接口调用凭据-开发.html"
  - "/2025/08/05/golang-zhi-wei-xin-huo-qu-jie-kou-diao-yong-ping-ju-kai-fa/"
  - "/2025/08/05/golang-zhi-wei-xin-huo-qu-jie-kou-diao-yong-ping-ju-kai-fa.html"
  - "/golang-zhi-wei-xin-huo-qu-jie-kou-diao-yong-ping-ju-kai-fa.html"
---
开始前先看下文档

接口是GET请求，请求的接口地址是https://api.weixin.qq.com/cgi-bin/token

参数如下

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1710494151/xiaorongmao/24033-x-8224919063099.png "" %}

返回的参数如下

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1710494151/xiaorongmao/2024-03-15_17-11.png "" %}

根据以上的文档我们需要建立一个结构体

```go
// TokenResponse 接收返回的参数 
type TokenResponse struct {
    AccessToken string `json:"access_token"`
    ExpiresIn   int    `json:"expires_in"`
    CurrentTime int64  `json:"current_time"` // 这个是逻辑需要，可以不加
}
```

这个TokenResponse就够用了，在golang中如何请求一个接口

```go
url := "https://api.weixin.qq.com/cgi-bin/token"
client := &http.Client{}
params := utils.H{
    "grant_type": "client_credential",
    "appid":      config.AppID,
    "secret":     config.AppSecret,
}

req, err := http.NewRequest("GET", url, nil)

q := req.URL.Query()
for key, value := range params {
    q.Add(key, value.(string))
}
req.URL.RawQuery = q.Encode()

resp, err := client.Do(req)
if err != nil {
    log.InfoLogger.H(tag, utils.H{
        "error": err.Error(), "url": url})
    return
}

defer func(Body io.ReadCloser) {
    err := Body.Close()
    if err != nil {
        log.ErrorLogger.H(tag, gin.H{"error": err})
    }
}(resp.Body)

body, err := ioutil.ReadAll(resp.Body)
if err != nil {
    log.InfoLogger.H(tag, utils.H{
        "error": err.Error(), "url": url})
    return
}
```

以上代码，拿到body我们就获得了响应数据，如何把body的数据与结构体TokenResponse做数据交换

```go
var res TokenResponse
err = json.Unmarshal(body, &res)

if err != nil {
    log.ErrorLogger.H(tag, gin.H{"error": err})
    return
}
```

以上的代码逻辑，就可以body的数据存到res中，之后就可以使用了，这块的底层逻辑大家喜欢的话可以自行查阅文档

```go
log.InfoLogger.H(tag, utils.H{
    "access_token": res.AccessToken,
    "expires_in":   res.ExpiresIn})
```

以上的逻辑看起来非常简单，其实主要是有几点  
一是对文档的分析，确定好需要的数据结构  
二是掌握http库的使用

以上只是部分代码 完整代码如下

```go
import (
	"xxx/config"
	"xxx/connections/redis"
	"xxx/modules/log"
	"xxx/modules/server"
	"xxx/modules/utils"
	"encoding/json"
	"github.com/gin-gonic/gin"
	"io"
	"io/ioutil"
	"net/http"
	"time"
)

type TokenResponse struct {
	AccessToken string `json:"access_token"`
	ExpiresIn   int    `json:"expires_in"`
	CurrentTime int64  `json:"current_time"`
}

func FetchAccessToken(c *server.Context) {
	tag := "FetchAccessToken"

	val, _ := redis.Get(tokenCacheKey(config.AppID))

	if val != "" {
		var res TokenResponse
		jsonErr := json.Unmarshal([]byte(val), &res)

		if jsonErr != nil {
			log.ErrorLogger.H(tag, gin.H{"error": jsonErr})
			return
		}

		log.InfoLogger.H(tag, utils.H{
			"cache_data": res})

		c.Success(res)
		return
	}

	url := "https://api.weixin.qq.com/cgi-bin/token"
	client := &http.Client{}
	params := utils.H{
		"grant_type": "client_credential",
		"appid":      config.AppID,
		"secret":     config.AppSecret,
	}

	req, err := http.NewRequest("GET", url, nil)

	q := req.URL.Query()
	for key, value := range params {
		q.Add(key, value.(string))
	}
	req.URL.RawQuery = q.Encode()

	resp, err := client.Do(req)
	if err != nil {
		log.InfoLogger.H(tag, utils.H{
			"error": err.Error(), "url": url})
		return
	}

	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			log.ErrorLogger.H(tag, gin.H{"error": err})
		}
	}(resp.Body)

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.InfoLogger.H(tag, utils.H{
			"error": err.Error(), "url": url})
		return
	}

	var res TokenResponse
	err = json.Unmarshal(body, &res)

	log.InfoLogger.H(tag, utils.H{
		"body":   body,
		"res":    res,
		"params": params,
		"query":  req.URL.String()})

	if err != nil {
		log.ErrorLogger.H(tag, gin.H{"error": err})
		return
	}

	log.InfoLogger.H(tag, utils.H{
		"access_token": res.AccessToken,
		"expires_in":   res.ExpiresIn})

	res.CurrentTime = time.Now().Unix()

	redis.Set(
		tokenCacheKey(config.AppID),
		utils.JsonEncode(res),
		time.Duration(res.ExpiresIn)*time.Second)

	c.Success(res)
	return
}
```

```go
func tokenCacheKey(appId string) string {
	return "wx:" + appId + ":access_token"
}
```

这里我整合了redis，将拿到的数据放到了redis中
