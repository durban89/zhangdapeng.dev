---
title: "Go基础学习记录 - 如何写Go代码 - 代码组织(导入路径、第一个程序)"
date: "2025-07-30 14:59:01"
slug: "go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-dao-ru-lu-jing-di-yi-ge-cheng-xu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(导入路径、第一个程序)/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(导入路径、第一个程序).html"
  - "/Go基础学习记录-如何写Go代码-代码组织(导入路径、第一个程序)/"
  - "/Go基础学习记录-如何写Go代码-代码组织(导入路径、第一个程序).html"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-导入路径-第一个程序/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-导入路径-第一个程序.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-dao-ru-lu-jing-di-yi-ge-cheng-/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-dao-ru-lu-jing-di-yi-ge-ch.html"
  - "/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-dao-ru-lu-jing-di-yi-ge-cheng-xu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **导入路径**

导入路径是唯一标识包的字符串。程序包的导入路径对应于其在工作区内或远程存储库中的位置（如下所述）。

标准库中的软件包被赋予短的导入路径，如"fmt"和"net/http"。对于你自己的软件包，你必须选择一个基本路径，这个基本路径不可能与未来添加到标准库或其他外部库中相冲突。

如果您将代码保存在某个源代码库中，那么您应该使用该代码源的根目录作为您的基本路径。例如，如果您在github.com/user上有GitHub帐户，那应该是您的基本路径。

请注意，在构建它之前，您不需要将代码发布到远程存储库。组织代码就好像你将在某天发布一样，这只是一个好习惯。在实践中，您可以选择任意路径名称，只要它是标准库和更大的Go生态系统所特有的即可。

我们将使用github.com/user作为我们的基本路径。在您的工作空间内创建一个目录以保留源代码：

```bash
$ mkdir -p $GOPATH/src/github.com/durban.zhang
```

### **第一个程序**

要编译并运行一个简单的程序，首先选择一个包路径（我将使用github.com/user/hello）并在工作区内创建一个相应的包目录：

```bash
$ mkdir $GOPATH/src/github.com/durban.zhang/hello
```

接下来，在该目录内创建一个名为hello.go的文件，其中包含以下Go代码。

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello, world.\n")
}
```

现在，可以使用go tool来构建和安装该程序：

```bash
$ go install github.com/durban.zhang/hello
```

请注意，您可以从系统上的任何位置运行此命令。go tool通过在GOPATH指定的工作区内查找github.com/user/hello包来查找源代码。

如果从软件包目录运行go install，也可以省略软件包路径：

```bash
$ cd $GOPATH/src/github.com/durban.zhang/hello

$ go install
```

该命令构建hello命令，生成可执行的二进制文件。然后，它会以hello的形式将该二进制文件安装到工作区的bin目录中（或者在Windows下，hello.exe）。

在我们的例子中，这将是$GOPATH/bin/hello，它是$HOME/go/bin/hello。

go tool只会在发生错误时打印输出，因此如果这些命令不产生任何输出，代表将成功执行。

现在可以通过在命令行键入完整路径来运行该程序：

```bash
$ $GOPATH/bin/hello

Hello, world.
```

或者，如果已将$GOPATH/bin添加到您的PATH中，请输入二进制名称

```bash
$ hello

Hello, world.
```

如果使用的是源代码管理系统，现在可以进行初始化存储库，添加文件以及提交第一项更改。这一步是可选的：也可以不需要使用源代码控制来编写Go代码。

```bash
$ cd $GOPATH/src/github.com/durban.zhang/hello

$ git init

Initialized empty Git repository in /home/xxx/work/src/github.com/durban.zhang/hello/.git/

$ git add hello.go

$ git commit -m "initial commit"

[master (root-commit) 0b4507d] initial commit

1 file changed, 1 insertion(+)

create mode 100644 hello.go
```

将代码推送到远程存储库作为自己的练习

这里使用的是官方的例子，本地实践操作顺利通过。
