---
title: "Go基础学习记录 - 编写Web应用程序 - 文件上传"
date: "2025-08-01 10:31:25"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wen-jian-shang-chuan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-文件上传/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-文件上传.html"
  - "/Go基础学习记录-编写Web应用程序-文件上传/"
  - "/Go基础学习记录-编写Web应用程序-文件上传.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wen-jian-shang-chuan/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wen-jian-shang-chuan.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-wen-jian-shang-chuan.html"
---
本次分享下 -- 文件上传

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.7
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.7
```

这些我觉得 够清晰了。OK！

继续分享"`文件上传`"的分享。

## 文件上传

假设你有一个像Instagram这样的网站，你希望用户上传他们漂亮的照片。  
你会如何实现这个功能？  
您必须将属性enctype添加到要用于上传照片的表单。  
此属性有三个可能的值：

* application/x-www-form-urlencoded   上传前对所有字符进行转码（默认）
* multipart/form-data   没有转码。当表单具有文件上传控件时，您必须使用此值
* text/plain   将空格转换为“+”，但不对特殊字符进行转码

因此，文件上传表单的HTML内容应如下所示：

```html
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Upload File</title>
  <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
    crossorigin="anonymous">
</head>

<body>
  <div class="container">
    <div class="col-md-12">
      <div class="text-center">
        <h1>Upload File</h1>
      </div>
      <form enctype="multipart/form-data" action="/upload/" method="POST">
        <div class="form-group">
          <input type="file" name="uploadfile" />
        </div>

        <input type="hidden" name="token" value="{{.Token}}">

        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
  <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin="anonymous"></script>
  <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
  <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>
</body>

</html>
```

添加路由处理函数UploadHandler

```go
// UploadHandler 上传文件
func UploadHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method)

	if r.Method == "GET" {
		p := &helpers.Page{Title: "Upload File"}

		crutime := time.Now().Unix()
		h := md5.New()
		io.WriteString(h, strconv.FormatInt(crutime, 10))
		token := fmt.Sprintf("%x", h.Sum(nil))
		p.Token = token
		helpers.RenderTemplate(w, "upload", p)
	} else {
		fmt.Println("Uploading ....")
		r.ParseMultipartForm(32 << 20)
		file, handler, err := r.FormFile("uploadfile")
		if err != nil {
			fmt.Println(err)
			return
		}

		defer file.Close()

		fmt.Fprintf(w, "%v", handler.Header)

		fmt.Println("handler.Filename", handler.Filename)
		time := fmt.Sprintf("%d", time.Now().Unix())
		targetFileName := "data/" + time + handler.Filename

		f, err := os.OpenFile(targetFileName, os.O_WRONLY|os.O_CREATE, 0666)
		if err != nil {
			fmt.Println(err)
		}

		defer f.Close()

		// 写入到文件中
		io.Copy(f, file)
	}

}
```

并且将我们的路由函数添加到主路由中

```go
http.HandleFunc("/upload/", controllers.UploadHandler)
```

重新编译项目并运行打开/upload/页面，选择文件并提交后会在浏览器中看到类似如下的输出

```go
map[Content-Disposition:[form-data; name="uploadfile"; filename="Y_1.jpg"] Content-Type:[image/jpeg]]
```

这里我其实是没有做对文件的类型进行限制的，实际的操作中需要根据情况做具体处理。

上面的代码中，我们需要调用r.ParseMultipartForm来上传文件。  
函数ParseMultipartForm采用maxMemory参数。  
调用ParseMultipartForm后，该文件将以maxMemory大小保存在服务器内存中。  
如果文件大小大于maxMemory，则其余数据将保存在系统临时文件中。  
您可以使用r.FormFile获取文件句柄并使用io.Copy保存到文件系统。  
当您访问表单中的其他非文件字段时，您不需要调用r.ParseForm，因为Go会在必要时调用它。  
此外，调用ParseMultipartForm一次就足够了 - 多次调用没有区别。

我们使用三个步骤上传文件，如下所示：

1. 将enctype ="multipart/form-data"添加到表单中。
2. 在服务器端调用r.ParseMultipartForm将文件保存到内存或临时文件。
3. 调用r.FormFile获取文件句柄并保存到文件系统。

文件处理程序是multipart.FileHeader。  
它使用以下结构：

```go
type FileHeader struct {
  Filename string
  Header   textproto.MIMEHeader
  // contains filtered or unexported fields
}
```

上面展示了使用表单上传文件的示例。还可以模拟客户端表单来上传文件，示例如下  
首先添加一个PostFileHandler方法，这个方法是用来模拟表单上传文件的，代码如下

```go
// PostFileHandler 模拟客户端表单提交
func PostFileHandler(w http.ResponseWriter, r *http.Request) {

  filename := r.URL.Query().Get("filename")
  targetURL := r.URL.Query().Get("targetURL")
  // filename string, targetURL string

  fmt.Println("filename = ", filename)
  fmt.Println("targetUrl = ", targetURL)

  // 获取本地源文件
  sourceFileName := "data/" + filename

  buf := &bytes.Buffer{}
  writer := multipart.NewWriter(buf)

  // 这一步非常重要 创建Form表单 文件名是 filename
  fileWriter, err := writer.CreateFormFile("uploadfile", filename)
  if err != nil {
    fmt.Println("error writing to writer")
    return
  }

  // 打开文件， 这里使用只读模式 os.O_RDONLY
  f, err := os.OpenFile(sourceFileName, os.O_RDONLY, 0666)
  if err != nil {
    fmt.Println("error open file")
    return
  }
  defer f.Close()

  // 将文件copy到模拟的表单里面
  _, err = io.Copy(fileWriter, f)
  if err != nil {
    fmt.Println("error copy file")
    fmt.Println(err)
    return
  }

  contentType := writer.FormDataContentType()
  writer.Close()

  // 表单上传文件的提交
  resp, err := http.Post(targetURL, contentType, buf)
  if err != nil {
    fmt.Println("error post file")
    return
  }

  defer resp.Body.Close()

  respBody, err := ioutil.ReadAll(resp.Body)

  if err != nil {
    fmt.Println("error read file")
    return
  }

  // 上传后返回的状态码
  fmt.Println(resp.Status)
  // 上传后返回的body信息
  fmt.Println(string(respBody))  return
}
```

同时修改下UploadHandler函数，稍微做下处理，加入如下代码

```go
fmt.Println("handler.Filename", handler.Filename)
time := fmt.Sprintf("%d", time.Now().Unix())
targetFileName := "data/" + time + handler.Filename

f, err := os.OpenFile(targetFileName, os.O_WRONLY|os.O_CREATE, 0666)
```

然后将PostFileHandler加入路由方便测试，如下

```go
http.HandleFunc("/postFile/", controllers.PostFileHandler)
```

这个逻辑主要是为了在示例测试中区分下文件，防止文件名重复上传失败，在实际的情况下，是不允许上传重复的内容的，会对服务器空间造成浪费

重新编译程序并运行，访问路由`http://localhost:8090/postFile/?filename=Y_1.jpg&targetURL=http://localhost:8090/upload/`，会看到如下的输出，我这里是

```bash
filename =  Y_1.jpg
targetUrl =  http://localhost:8090/upload/
method: POST
Uploading ....
handler.Filename Y_1.jpg
200 OK
map[Content-Type:[application/octet-stream] Content-Disposition:[form-data; name="uploadfile"; filename="Y_1.jpg"]]
```

上面的示例显示了如何使用客户端上传文件。  
它使用multipart.Write将文件写入缓存并通过POST方法将它们发送到服务器。  
如果您有其他需要写入数据的字段，例如用户名，请根据需要调用multipart.WriteField。

今天就分享到这里，如果你有其他疑问请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.8
```
