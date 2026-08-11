---
title: "mac关闭指定端口"
date: "2025-06-11 11:06:53"
slug: "mac-guan-bi-zhi-ding-duan-kou"
categories: ["技术"]
tags: ["Unix", "MacOS"]
aliases:
  - "/2025/06/11/mac关闭指定端口/"
  - "/2025/06/11/mac关闭指定端口.html"
  - "/mac关闭指定端口/"
  - "/mac关闭指定端口.html"
  - "/2025/06/11/Mac关闭指定端口/"
  - "/2025/06/11/Mac关闭指定端口.html"
  - "/2025/06/11/mac-guan-bi-zhi-ding-duan-kou/"
  - "/2025/06/11/mac-guan-bi-zhi-ding-duan-kou.html"
  - "/mac-guan-bi-zhi-ding-duan-kou.html"
---
先执行如下命令:

```sh
lsof -i:端口号
```

会有类似下面的结果：

```shell
COMMAND     PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
WebProces 42624 davidzhang    5u  IPv4 0x907152bbf7b2a875      0t0  TCP localhost:64438->localhost:radan-http (ESTABLISHED)
WebProces 42624 davidzhang   10u  IPv4 0x907152bbf7b64a05      0t0  TCP localhost:64439->localhost:radan-http (ESTABLISHED)
```

然后执行：

```sh
kill -9 42624
```

结束进程就搞定了
