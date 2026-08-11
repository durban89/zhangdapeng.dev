---
title: "Ubuntu下配置swap，增加程序运行速度"
date: "2025-07-15 10:28:54"
slug: "ubuntu-xia-pei-zhi-swap-zeng-jia-cheng-xu-yun-xing-su-du"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/07/15/Ubuntu下配置swap，增加程序运行速度/"
  - "/2025/07/15/Ubuntu下配置swap，增加程序运行速度.html"
  - "/Ubuntu下配置swap，增加程序运行速度/"
  - "/Ubuntu下配置swap，增加程序运行速度.html"
  - "/2025/07/15/Ubuntu下配置swap-增加程序运行速度/"
  - "/2025/07/15/Ubuntu下配置swap-增加程序运行速度.html"
  - "/2025/07/15/ubuntu-xia-pei-zhi-swap-zeng-jia-cheng-xu-yun-xing-su-du/"
  - "/2025/07/15/ubuntu-xia-pei-zhi-swap-zeng-jia-cheng-xu-yun-xing-su-du.html"
  - "/ubuntu-xia-pei-zhi-swap-zeng-jia-cheng-xu-yun-xing-su-du.html"
---
前提是我用的是ubuntu

![Image](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1675926044/2023-02-09_15-00.png)

通过增加swap的大小，就能提升程序运行速度，对于程序开发的我，还是被耍了一下，我居然不知道

最近运行浏览器google chrome,无意间打开了多个tab，然后就发现电脑卡住了

无意间最近观察了下进程发现swap在卡住的时候是占用满了的，然后还是2G我发现不对，于是想着这玩意以前接触过，应该可以扩容于是搞起来

```bash
sudo fallocate -l 8G /swapfile8 # 创建命令
```

```bash
sudo mkswap /swapfile8 # 格式化命令
```

```bash
sudo swapon /swapfile8 # 挂载swap
```

如果swap在使用中，需要先进行卸载swap操作

```bash
sudo swapoff /swapfile # 卸载swap
```

注意我是卸载的*/swapfile*不是*/swapfile8*
