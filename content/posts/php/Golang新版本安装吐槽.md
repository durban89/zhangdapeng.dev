---
title: "Golang新版本安装吐槽"
date: "2025-06-03 17:14:58"
slug: "golang-xin-ban-ben-an-zhuang-tu-cao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/06/03/Golang新版本安装吐槽/"
  - "/2025/06/03/Golang新版本安装吐槽.html"
  - "/Golang新版本安装吐槽/"
  - "/Golang新版本安装吐槽.html"
  - "/2025/06/03/golang-xin-ban-ben-an-zhuang-tu-cao/"
  - "/2025/06/03/golang-xin-ban-ben-an-zhuang-tu-cao.html"
  - "/golang-xin-ban-ben-an-zhuang-tu-cao.html"
---
我是打算使用一下最新版本的Golang，然后使用下Hugo，结果安装的时候提示要安装上一个版本，我感觉没啥问题，我就安装了要求安装的版本，结果还是有问题
继续安装要求安装的版本
结果就是一个套着一个，我服了

这个机制头一次见到

```sh
$ gvm install go1.24.3
Updating Go source...
Installing go1.24.3...
 * Compiling...
ERROR: Failed to compile. Check the logs at /home/durban/.gvm/logs/go-go1.24.3-compile.log
ERROR: Failed to use installed version

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:13:01] C:130
$ tail -f -n 100 ~/.gvm/logs/go-go1.24.3-compile.log 
Building Go cmd/dist using /home/durban/.gvm/gos/go1.14.15. (go1.14.15 linux/amd64)
can't load package: package ./cmd/dist: found packages main (build.go) and building_Go_requires_Go_1_22_6_or_later (notgo122.go) in /home/durban/.gvm/gos/go1.24.3/src/cmd/dist

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:13:25] C:130
$ gvm install go1.22.6                              
Installing go1.22.6...
 * Compiling...
ERROR: Failed to compile. Check the logs at /home/durban/.gvm/logs/go-go1.22.6-compile.log
ERROR: Failed to use installed version

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:13:35] C:1
$ tail -f -n 100 ~/.gvm/logs/go-go1.22.6-compile.log
Building Go cmd/dist using /home/durban/.gvm/gos/go1.14.15. (go1.14.15 linux/amd64)
can't load package: package ./cmd/dist: found packages main (build.go) and building_Go_requires_Go_1_20_6_or_later (notgo120.go) in /home/durban/.gvm/gos/go1.22.6/src/cmd/dist

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:13:49] C:130
$ gvm install go1.20.6                              
Installing go1.20.6...
 * Compiling...
ERROR: Failed to compile. Check the logs at /home/durban/.gvm/logs/go-go1.20.6-compile.log
ERROR: Failed to use installed version

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:13:53] C:1
$ tail -f -n 100 ~/.gvm/logs/go-go1.20.6-compile.log
Building Go cmd/dist using /home/durban/.gvm/gos/go1.14.15. (go1.14.15 linux/amd64)
can't load package: package ./cmd/dist: found packages main (build.go) and building_Go_requires_Go_1_17_13_or_later (notgo117.go) in /home/durban/.gvm/gos/go1.20.6/src/cmd/dist

# durban @ durban-amd-workspace in ~/Downloads/ubuntu_software [17:14:02] C:130
$ gvm install go1.17.13                             
Installing go1.17.13...
 * Compiling...
go1.17.13 successfully installed!

```

笑死人

这个安装逻辑就是按照这个顺序依次安装

```sh
gvm install go1.17.13
gvm install go1.20.6
gvm install go1.22.6
gvm install go1.24.3
```

为了体验下新版本我这是招谁了
