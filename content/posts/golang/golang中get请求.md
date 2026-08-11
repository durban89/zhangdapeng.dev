---
title: "golang中get请求"
date: "2025-08-05 09:48:48"
slug: "golang-zhong-get-qing-qiu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/golang中get请求/"
  - "/2025/08/05/golang中get请求.html"
  - "/golang中get请求/"
  - "/golang中get请求.html"
  - "/2025/08/05/golang-zhong-get-qing-qiu/"
  - "/2025/08/05/golang-zhong-get-qing-qiu.html"
  - "/golang-zhong-get-qing-qiu.html"
---
调用第三方的接口服务的时候，有时候会发现明明我发起的是带有参数的get请求为什么对方收不到参数，我自己测试了下也有遇到过类似的情况

主要原因是对请求参数的数据格式傻傻分不清

下面记录了一段代码

```go
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	client := &http.Client{}

	params := map[string]interface{}{
		"p1": "",
		"p2": "",
	}

	data := jsonEncode(params)

	payload := strings.NewReader(data)
	req, reqError := http.NewRequest("GET", "https://goplay.tools/", payload)

	if reqError != nil {
		fmt.Println(reqError.Error())
		return
	}

	resp, doError := client.Do(req)

	if doError != nil {
		fmt.Println(doError.Error())
		return
	}

	defer resp.Body.Close()

	body, readError := ioutil.ReadAll(resp.Body)

	if readError != nil {
        fmt.Println(readError.Error())
		return
	}

	var res interface{}

	json.Unmarshal(body, &res)

	fmt.Println("output")
	fmt.Println(res)

}

func jsonEncode(v interface{}) string {
	bt, err := json.Marshal(v)

	if err != nil {
		return ""
	}

	return string(bt)
}
```

本来的意思是，我像给这个网址发送一个请求，并且带上参数p1和p2

但是实际上那个网址什么也没有收到，经过几次排查，这段代码是给指定网址发送了一个get请求，body的部分是一个json字符串

正确的操作如下

```go
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	client := &http.Client{}

	params := map[string]interface{}{
		"p1": "",
		"p2": "",
	}

	req, reqError := http.NewRequest("GET", "https://goplay.tools/", nil)

	if reqError != nil {
		fmt.Println(reqError.Error())
		return
	}

	query := req.URL.Query()
	for key, value := range params {
		query.Add(key, value.(string))	
	}
	req.URL.RawQuery = query.Encode()

	resp, doError := client.Do(req)

	if doError != nil {
		fmt.Println(doError.Error())
		return
	}

	defer resp.Body.Close()

	body, readError := ioutil.ReadAll(resp.Body)

	if readError != nil {
        fmt.Println(readError.Error())
		return
	}

	var res interface{}

	json.Unmarshal(body, &res)

	fmt.Println("output")
	fmt.Println(res)

}

func jsonEncode(v interface{}) string {
	bt, err := json.Marshal(v)

	if err != nil {
		return ""
	}

	return string(bt)
}
```
