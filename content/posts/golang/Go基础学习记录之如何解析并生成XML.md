---
title: "Go基础学习记录之如何解析并生成XML"
date: "2025-08-01 11:35:30"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-xml"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之如何解析并生成XML/"
  - "/2025/08/01/Go基础学习记录之如何解析并生成XML.html"
  - "/Go基础学习记录之如何解析并生成XML/"
  - "/Go基础学习记录之如何解析并生成XML.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-xml/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-xml.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-ru-he-jie-xi-bing-sheng-cheng-xml.html"
---
## XML

XML是Web服务中常用的数据通信格式。今天，它在Web开发中扮演着越来越重要的角色。本次分享将介绍如何通过Go的标准库使用XML。我不会尝试教授XML的语法或约定。你可以去阅读有关XML本身的更多文档。我只关注如何在Go中编码和解码XML文件。假设您在IT中工作，并且您必须处理以下XML配置文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<servers version="1">
    <server>
        <serverName>Shanghai_VPN</serverName>
        <serverIP>127.0.0.1</serverIP>
    </server>
    <server>
        <serverName>Beijing_VPN</serverName>
        <serverIP>127.0.0.2</serverIP>
    </server>
</servers>
```

上面的XML文档包含有关服务器的两种信息：服务器名称和IP。我们将在以下示例中使用此文档。

### 解析XML

如何解析这个XML文档？可以使用Go的xml包中的Unmarshal函数来执行此操作。

```go
func Unmarshal(data []byte, v interface{}) error
```

data参数从XML源接收数据流，v是要将解析后的XML输出到的结构中。它是一个接口，这意味着您可以将XML转换为您想要的任何结构。在这里，我们只讨论如何从XML转换为结构类型，因为它们共享相似的树结构。  
示例代码：

```go
package main

import (
    "encoding/xml"
    "fmt"
    "io/ioutil"
    "os"
)

type Server struct {
	XMLName    xml.Name `xml:"server"`
	ServerName string   `xml:"serverName"`
	ServerIP   string   `xml:"serverIP"`
}

type XMLServers struct {
	XMLName     xml.Name `xml:"servers"`
	Version     string   `xml:"version,attr"`
	Servers     []Server `xml:"server"`
	Description string   `xml:",innerxml"`
}

func main() {
    file, err := os.Open(config.TemplateDir + "/server.xml")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	data, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println(err)
		return
	}

	v := XMLServers{}
	err = xml.Unmarshal(data, &v)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Fprintln(w, v)
}
```

XML实际上是一个树数据结构，我们可以使用Go中的结构定义一个非常相似的结构，然后使用xml.Unmarshal从XML转换为我们的struct对象。示例代码将打印以下内容：

```html
{{ servers} 1 [{{ server} Shanghai_VPN 127.0.0.1} {{ server} Beijing_VPN 127.0.0.2}] 
    <server>
        <serverName>Shanghai_VPN</serverName>
        <serverIP>127.0.0.1</serverIP>
    </server>
    <server>
        <serverName>Beijing_VPN</serverName>
        <serverIP>127.0.0.2</serverIP>
    </server>
}
```

我们使用xml.Unmarshal将XML文档解析为相应的struct对象。您应该看到我们的结构中有xml:"serverName"。这是结构体的一个特征，称为结构标记，用于帮助反射。让我们再看一下Unmarshal的定义：

```go
func Unmarshal(data []byte, v interface{}) error
```

第一个参数是XML数据流。第二个参数是存储类型，支持struct，slice和string类型。Go的XML包使用反射进行数据映射，因此应该导出v中的所有字段。但是，这会导致一个问题：它如何知道哪个XML字段对应于映射的struct字段？答案是XML解析器按特定顺序解析数据。库将首先尝试查找匹配的struct标记。如果找不到匹配，则搜索结构字段名称。请注意，所有标记，字段名称和XML元素都区分大小写，因此您必须确保映射成功时存在一对一的对应关系。Go的反射机制允许您使用此标记信息将XML数据反映到结构对象。如果您想了解有关Go中反射的更多信息，请阅读有关struct标签和反射的包文档。

使用xml包将XML文档解析为结构时，以下是一些规则：

1. 如果字段类型是带有标签",innerxml"的字符串或[]字节，则Unmarshal将为其分配原始XML数据，如上例中的描述：  
Shanghai\_VPN127.0.0.1Beijing\_VPN

2. 如果一个字段被称为XMLName并且其类型是xml.Name，那么它将获取元素名称，就像上面示例中的servers一样。

3. 如果字段的标记包含相应的元素名称，那么它也会获取元素名称，如上例中的servername和serverip。

4. 如果字段的标记包含",attr"，则它获取相应元素的属性，如上例中的版本。

5. 如果字段的标记包含类似"a>b>c"的内容，则它获取节点a的节点b的元素c的值。

6. 如果字段的标记包含"="，那么它什么也得不到。

7. 如果字段的标记包含",any"，则它将获取所有不符合其他规则的子元素。

8.如果XML元素有一个或多个注释，则所有这些注释都将添加到包含",comments"的标记的第一个字段中。该字段类型可以是string或[]byte。如果此类字段不存在，则丢弃所有注释。

这些规则告诉您如何在结构中定义标记。一旦理解了这些规则，将XML映射到结构就像上面的示例代码一样简单。因为标签和XML元素具有一对一的对应关系，所以我们也可以使用切片来表示同一级别上的多个元素。请注意，结构中的所有字段都应导出(大写)，以便正确解析数据。

### 生成XML

如果我们想要生成XML文档而不是解析XML文档，该怎么办？我们如何在Go中做到这一点？xml包提供了两个函数，即Marshal和MarshalIndent，其中第二个函数自动缩进编组的XML文档。  
他们的定义如下：

```go
func Marshal(v interface{}) ([]byte, error)
func MarshalIndent(v interface{}, prefix, indent string) ([]byte, error)
```

这两个函数中的第一个参数用于存储编组的XML数据流。让我们看一个例子，看看它是如何工作的：

```go
package main

import (
    "encoding/xml"
    "fmt"
    "os"
)

type Server struct {
	XMLName    xml.Name `xml:"server"`
	ServerName string   `xml:"serverName"`
	ServerIP   string   `xml:"serverIP"`
}

type XMLServers struct {
	XMLName     xml.Name `xml:"servers"`
	Version     string   `xml:"version,attr"`
	Servers     []Server `xml:"server"`
	Description string   `xml:",innerxml"`
}

func main() {
    v := &XMLServers{
		Version: "1",
	}

	v.Servers = append(v.Servers, Server{
		ServerName: "Shanghai_VPN",
		ServerIP:   "127.0.0.1",
	})

	v.Servers = append(v.Servers, Server{
		ServerName: "Beijing_VPN",
		ServerIP:   "127.0.0.2",
	})

	output, err := xml.MarshalIndent(v, "", "    ")
	if err != nil {
		fmt.Println(err)
		return
	}

	os.Stdout.Write([]byte(xml.Header))
	os.Stdout.Write(output)
}
```

上面的示例打印以下信息：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<servers version="1">
    <server>
        <serverName>Shanghai_VPN</serverName>
        <serverIP>127.0.0.1</serverIP>
    </server>
    <server>
        <serverName>Beijing_VPN</serverName>
        <serverIP>127.0.0.2</serverIP>
    </server>
</servers>
```

正如我们之前定义的那样，我们有os.Stdout.Write([] byte(xml.Header))的原因是因为xml.MarshalIndent和xml.Marshal都没有自己输出XML头，所以我们必须明确  
打印它们以便正确生成XML文档。在这里我们可以看到Marshal还接收了一个类型为interface {}的v参数。那么编组XML文档时的规则是什么？  
1. 如果v是数组或切片，则它会打印所有元素，如value。  
2. 如果v是指针，则它打印v指向的内容，当v为nil时不打印任何内容。  
3. 如果v是一个接口，它也会处理接口。  
4. 如果v是其他类型之一，则打印该类型的值。

那么xml.Marshal如何决定元素的名称？它遵循随后的规则：  
1. 如果v是结构，则它在XMLName的标记中定义名称。  
2. 字段名称为XMLName，类型为xml.Name。  
3. struct中的字段标记。  
4. struct中的字段名称。  
5. 输入编组名称。

然后我们需要弄清楚如何设置标记以生成最终的XML文档。

1. 不会打印XMLName。  
2. 包含"-"标签的字段将不会被打印。  
3. 如果标记包含"name,attr"，则它使用name作为属性名称，使用字段值作为值，就像上面示例中的版本一样。  
4. 如果标记包含",attr"，则它使用字段的名称作为属性名称，将字段值作为其值。  
5. 如果标签包含",chardata"，则它会打印字符数据而不是元素。  
6. 如果标签包含",innerxml"，则打印原始值。  
7. 如果标记包含",comment"，则会将其作为注释打印而不进行转义，因此您的值不能包含"-"。  
8. 如果标记包含"omitempty"，则如果其值为零值，则忽略该字段，包括false，0，nil指针或nil接口，数组的长度为零，slice，map和string。  
9. 如果标签包含"a>b>c"，则打印三个元素，其中a包含b，b包含c
