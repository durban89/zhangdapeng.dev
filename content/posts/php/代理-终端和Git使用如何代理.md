---
title: "代理 - 终端和Git使用如何代理"
date: "2025-07-03 17:37:24"
slug: "dai-li-zhong-duan-he-git-shi-yong-ru-he-dai-li"
categories: ["技术"]
tags: ["Git", "代理"]
aliases:
  - "/2025/07/03/代理-终端和Git使用如何代理/"
  - "/2025/07/03/代理-终端和Git使用如何代理.html"
  - "/代理-终端和Git使用如何代理/"
  - "/代理-终端和Git使用如何代理.html"
  - "/2025/07/03/dai-li-zhong-duan-he-git-shi-yong-ru-he-dai-li/"
  - "/2025/07/03/dai-li-zhong-duan-he-git-shi-yong-ru-he-dai-li.html"
  - "/dai-li-zhong-duan-he-git-shi-yong-ru-he-dai-li.html"
---
## GIT

设置HTTP协议

* socks5方式

```bash
git config --global http.proxy 'socks5://127.0.0.1:1080' 
git config --global https.proxy 'socks5://127.0.0.1:1080'
```

* http方式

```bash
git config --global http.proxy "http://127.0.0.1:6667"
git config --global https.proxy "http://127.0.0.1:6667"
```

* 取消设置

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

设置SSH协议

创建文件 ~/.ssh/config 【如果存在可忽略】

```bash
Host bitbucket.org
	User git
 	HostName altssh.bitbucket.org
 	Port 443
 	ProxyCommand connect -S 127.0.0.1:1080 %h %p

Host github.com
 	User git
 	HostName ssh.github.com
 	Port 443
 	ProxyCommand connect -S 127.0.0.1:1080 %h %p%
```

## 终端 terminal

打开终端执行下面命令即可，无须重启终端

```bash
export http_proxy="socks5://127.0.0.1:1080"
export https_proxy="socks5://127.0.0.1:1080"
```

设置完后 执行下面命令查看自己的IP

```bash
curl -i http://ip.cn
```

有个问题就是设置完代理，上面的命令无法测试自己的IP了，应该是这个地址也同时被墙了。

参考：https://blog.kelu.org/tech/2017/06/19/setting-socks5-proxy.html
