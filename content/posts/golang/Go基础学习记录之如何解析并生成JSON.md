---
title: "Go基础学习记录之如何解析并生成JSON"
date: "2025-08-01 11:35:39"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-json"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之如何解析并生成JSON/"
  - "/2025/08/01/Go基础学习记录之如何解析并生成JSON.html"
  - "/Go基础学习记录之如何解析并生成JSON/"
  - "/Go基础学习记录之如何解析并生成JSON.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-json/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-json.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-json.html"
---
## JSON

JSON（JavaScript Object Notation）是一种基于文本描述的轻量级数据交换语言。  
它的优点包括自我描述，易于理解等。即使它是JavaScript的一个子集，JSON使用不同的文本格式，结果是它可以被视为一种独立的语言。  
JSON与C系列语言具有相似性。  
JSON和XML之间最大的区别在于XML是一种完整的标记语言，而JSON则不是。  
JSON比XML更小更快，因此在浏览器中解析更加容易和快捷，这也是许多开放平台选择使用JSON作为数据交换接口语言的原因之一。  
由于JSON在Web开发中变得越来越重要，让我们来看看Go对JSON的支持程度。  
你会发现Go的标准库对编码和解码JSON有很好的支持。

```bash
{"servers":[{"serverName":"Shanghai_VPN","serverIP":"127.0.0.1"},{"serverName":"Beijing_VPN","serverIP":"127.0.0.2"}]}
```

后面的部分将使用此JSON数据在Go中引入JSON概念。

### **解析JSON**

### 解析为Struct

假设我们在上面的例子中有JSON。  
我们如何解析这些数据并将其映射到Go中的结构？Go为此提供了以下功能：

```go
func Unmarshal(data []byte, v interface{}) error
```

我们可以像这样使用这个函数：

```go
package controllers

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type JsonServer struct {
    ServerName string
    StringIP   string
}

type JsonServers struct {
    Servers []JsonServer
}

func Json(w http.ResponseWriter, r *http.Request) {
    var s JsonServers
    str := `{"servers":[{"serverName":"Shanghai_VPN","serverIP":"127.0.0.1"},{"serverName":"Beijing_VPN","serverIP":"127.0.0.2"}]}`
    json.Unmarshal([]byte(str), &s)
    fmt.Println(str)
}
```

运行后得到如下结果

```bash
{[{Shanghai_VPN 127.0.0.1} {Beijing_VPN 127.0.0.2}]}
```

在上面的示例中，我们在Go中为JSON定义了相应的结构，使用slice作为JSON对象数组，使用字段名作为JSON键。  
但Go如何知道哪个JSON对象对应于哪个特定结构域？  
假设我们在JSON中有一个名为Foo的键。  
我们如何找到相应的字段？  
1. 首先，Go尝试查找标签包含Foo的（大写）导出字段。  
2. 如果找不到匹配项，请查找名称为Foo的字段。  
3. 如果仍然没有匹配，请查找类似FOO或FoO的内容，忽略区分大小写。  
您可能已经注意到，应该导出要分配的所有字段，并且Go仅分配可以找到的字段，而忽略所有其他字段。  
如果您需要处理大块的JSON数据，但只有它的一个特定子集，这可能很有用。  
您不需要的数据很容易被丢弃。

### 解析为接口

当我们事先知道期望什么样的JSON时，我们可以将它解析为特定的结构。  
但是，如果我们不知道怎么办？  
我们知道interface{}可以是Go中的任何内容，因此它是保存未知格式的JSON的最佳容器。  
JSON包使用map[string]interface{}和[]interface{}来保存各种JSON对象和数组。  
以下是JSON映射关系列表：

1. bool代表JSON布尔值，  
2. float64代表JSON数字，  
3. string表示JSON字符串，  
4. nil表示JSON null。

假设我们有以下JSON数据：

```go
b := []byte(`{"Name":"Wednesday","Age":6,"Parents":["Gomez","Morticia"]}`)
```

现在我们将这个JSON解析为interface{}：

```go
var f interface{}
err := json.Unmarshal(b, &f)
```

f存储一个映射，其中键是字符串，值是interface{}'s'。

```go
f = map[string]interface{}{
    "Name": "Wednesday",
    "Age":  6,
    "Parents": []interface{}{
        "Gomez",
        "Morticia",
    },
}
```

那么，我们如何访问这些数据？键入断言。

```go
m := f.(map[string]interface{})
```

断言后，您可以使用以下代码访问数据:

```go
for k, v := range m {
    switch vv := v.(type) {
    case string:
        fmt.Println(k, "is string", vv)
    case int:
        fmt.Println(k, "is int", vv)
    case float64:
        fmt.Println(k,"is float64",vv)
    case []interface{}:
        fmt.Println(k, "is an array:")
        for i, u := range vv {
            fmt.Println(i, u)
        }
    default:
        fmt.Println(k, "is of a type I don't know how to handle")
    }
}
```

如您所见，我们现在可以通过interface{}解析未知格式的JSON并键入断言。  
以上示例是官方解决方案，但类型断言并不总是方便。  
因此，我推荐一个名为simplejson的开源项目，由bitly创建和维护。  
以下是如何使用此项目处理未知格式的JSON的示例：

```go
js, err := NewJson([]byte(`{
    "test": {
        "array": [1, "2", 3],
        "int": 10,
        "float": 5.150,
        "bignum": 9223372036854775807,
        "string": "simplejson",
        "bool": true
    }
}`))

arr, _ := js.Get("test").Get("array").Array()
i, _ := js.Get("test").Get("int").Int()
ms := js.Get("test").Get("string").MustString()
```

不难看出这是多么方便。  
查看存储库以查看更多信息：  
https://github.com/bitly/go-simplejson.

### **生成JSON**

在许多情况下，我们需要生成JSON数据并响应客户端。  
在Go中，JSON包有一个名为Marshal的函数来执行以下操作：

```go
func Marshal(v interface{}) ([]byte, error)
```

假设我们需要生成服务器信息列表。  
我们有以下样本：

```go
package controllers

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type JsonServer struct {
    ServerName string
    ServerIP   string
}

type JsonServers struct {
    Servers []JsonServer
}

func JsonProcess(w http.ResponseWriter, r *http.Request) {
    var s JsonServers
    s.Servers = append(s.Servers, JsonServer{
        ServerName: "Shanghai_VPN",
        ServerIP:   "127.0.0.1",
    })

    s.Servers = append(s.Servers, JsonServer{
        ServerName: "Beijing_VPN",
        ServerIP:   "127.0.0.2",
    })

    b, err := json.Marshal(s)

    if err != nil {
        fmt.Println("json err:", err)
        return
    }

    fmt.Println(string(b))
}
```

输出结果如下:

```bash
{"Servers":[{"ServerName":"Shanghai_VPN","ServerIP":"127.0.0.1"},{"ServerName":"Beijing_VPN","ServerIP":"127.0.0.2"}]}
```

如您所知，所有字段名称都是大写的，但如果您希望JSON键名以小写字母开头，则应使用struct标签。  
否则，Go将不会为内部字段生成数据。

```go
type JsonServer struct {
    ServerName string `json:"serverName"`
    ServerIP   string `json:"serverIP"`
}

type JsonServers struct {
    Servers []JsonServer `json:"servers"`
}
```

在此修改之后，我们可以生成与以前相同的JSON数据。  
在尝试生成JSON时，您需要记住以下几点：

1. 不输出包含“ - ”的字段标签。  
2. 如果标记包含自定义名称，则Go使用此名称而不是字段名称，如上例中的serverName。  
3. 如果标签包含omitempty，则如果该字段为零值，则不会输出该字段。  
4. 如果字段类型是bool，string，int，int64等，并且其标记包含",string"，则Go会将此字段转换为其对应的JSON类型。  
示例如下

```go
type TestJsonServer struct {
	// ID不会被输出
	ID int `json:"-"`

	// ServerName2 不会转换为JSON类型
	ServerName  string `json:"serverName"`
	ServerName2 string `json:"serverName2,string"`

	// 如果ServerIP是空的将不会被输出
	ServerIP string `json:"serverIP,omitempty"`
}

func JsonToTest(w http.ResponseWriter, r *http.Request) {
	s := TestJsonServer{
		ID:          3,
		ServerName:  `Go "1.0" `,
		ServerName2: `Go "1.0" `,
		ServerIP:    ``,
	}

	b, _ := json.Marshal(s)
	os.Stdout.Write(b)
}
```

输出如下

```bash
{"serverName":"Go \"1.0\" ","serverName2":"\"Go \\\"1.0\\\" \""}
```

Marshal函数只有在成功时返回数据，所以这里有一些我们需要记住的要点：

1. JSON仅支持字符串作为键，因此如果要对映射进行编码，则其类型必须为map[string]T，其中T是Go中的类型。  
2. 通道，复杂类型和函数等类型无法编码为JSON。  
3. 不要尝试编码循环数据，它会导致无限递归。  
4. 如果该字段是指针，则Go输出它指向的数据，否则如果指向nil则输出null。
