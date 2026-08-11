---
title: "【go语言技术积累】初步使用grpc"
date: "2025-08-05 11:36:55"
slug: "go-yu-yan-ji-shu-ji-lei-chu-bu-shi-yong-grpc"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/【go语言技术积累】初步使用grpc/"
  - "/2025/08/05/【go语言技术积累】初步使用grpc.html"
  - "/【go语言技术积累】初步使用grpc/"
  - "/【go语言技术积累】初步使用grpc.html"
  - "/2025/08/05/go语言技术积累-初步使用grpc/"
  - "/2025/08/05/go语言技术积累-初步使用grpc.html"
  - "/2025/08/05/go-yu-yan-ji-shu-ji-lei-chu-bu-shi-yong-grpc/"
  - "/2025/08/05/go-yu-yan-ji-shu-ji-lei-chu-bu-shi-yong-grpc.html"
  - "/go-yu-yan-ji-shu-ji-lei-chu-bu-shi-yong-grpc.html"
---
使用grpc的要求

1、需要安装go语言

2、需要本地安装 **[Protocol buffer](https://developers.google.com/protocol-buffers) compiler**

**新建项目grpc\_test并初始化git仓库**

```bash
mkdir grpc_test && cd grpc_test && git init
```

**进入到grpc\_test目录**

```bash
go mod init grpc_test
```

**安装需要依赖的库**

```bash
go get -u google.golang.org/grpc
```

**创建目录**hello\_world/client，hello\_world/server，hello\_world/base

```bash
mkdir -p hello_world/client hello_world/server hello_world/base
```

进入base，创建文件base.proto，代码内容如下

```proto
syntax = "proto3";

option go_package = "grpc_test/hello_world/base";
option java_multiple_files = true;
option java_package = "io.grpc.examples.base";
option java_outer_classname = "HelloWorldProto";

package base;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
  rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

在hello\_world目录下执行如下命令

```bash
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    base/base.proto
```

会自动生成 base\_grpc.pb.goh和base.pb.go

添加client端的代码

进入client，创建文件main.go，代码内容如下

```go
package main

import (
	"context"
	"flag"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	pb "grpc_test/hello_world/base"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	name = flag.String("name", defaultName, "Name to greet")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewGreeterClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.SayHello(ctx, &pb.HelloRequest{Name: *name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetMessage())

	r, err = c.SayHelloAgain(ctx, &pb.HelloRequest{Name: *name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetMessage())
}
```

进入server，创建文件main.go，代码内容如下

```go
package main

import (
	"context"
	"flag"
	"fmt"
	"google.golang.org/grpc"
	"log"
	"net"
	pb "grpc_test/hello_world/base"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

// server
type server struct {
	pb.UnimplementedGreeterServer
}

// SayHello implements base.GreeterServer
func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	log.Printf("Received: %v", in.GetName())
	return &pb.HelloReply{Message: "Hello " + in.GetName()}, nil
}

func (s *server) SayHelloAgain(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	log.Printf("Received: %v", in.GetName())
	return &pb.HelloReply{Message: "Hello again " + in.GetName()}, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
```

上述步骤完成后执行server端命令

```bash
go run server/main.go
```

然后在执行client端命令

```bash
go run client/main.go -name=durban
```

server端会输出

```bash
$ go run server/main.go
2023/12/05 16:52:36 server listening at [::]:50051
2023/12/05 16:52:51 Received: durban
2023/12/05 16:52:51 Received: durban
```

client端会输出

```bash
$ go run ./client/main.go -name=durban              
2023/12/05 16:52:51 Greeting: Hello durban
2023/12/05 16:52:51 Greeting: Hello again durban
```

注意这里的grpc\_test可以改为自己想用的名称

关于grpc的文章

[HTTP、WebSocket、gRPC 或 WebRTC：哪种通信协议最适合您的应用程序？](https://zhuanlan.zhihu.com/p/634534138)

[使用gRPC创建简单聊天程序](https://xiaochai.github.io/2018/04/29/grpc/)

[基于 gRPC 的聊天室实现](https://github.com/wxdao/chatroom)

[实战gRPC四种通信模式](https://cloud.tencent.com/developer/article/2352876)
