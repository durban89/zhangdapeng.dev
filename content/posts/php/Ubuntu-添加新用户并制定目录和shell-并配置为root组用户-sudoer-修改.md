---
title: "Ubuntu 添加新用户并制定目录和shell,并配置为root组用户,sudoer 修改"
date: "2025-06-24 15:04:36"
slug: "ubuntu-tian-jia-xin-yong-hu-bing-zhi-ding-mu-lu-he-shell-bing-pei-zhi-wei-root-zu-yong-hu-sudoer-xiu-gai"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/24/Ubuntu-添加新用户并制定目录和shell,并配置为root组用户,sudoer-修改/"
  - "/2025/06/24/Ubuntu-添加新用户并制定目录和shell,并配置为root组用户,sudoer-修改.html"
  - "/Ubuntu-添加新用户并制定目录和shell,并配置为root组用户,sudoer-修改/"
  - "/Ubuntu-添加新用户并制定目录和shell,并配置为root组用户,sudoer-修改.html"
  - "/2025/06/24/Ubuntu-添加新用户并制定目录和shell-并配置为root组用户-sudoer-修改/"
  - "/2025/06/24/Ubuntu-添加新用户并制定目录和shell-并配置为root组用户-sudoer-修改.html"
  - "/2025/06/24/ubuntu-tian-jia-xin-yong-hu-bing-zhi-ding-mu-lu-he-shell-bing-pei-zhi-wei-root-zu-yong-/"
  - "/2025/06/24/ubuntu-tian-jia-xin-yong-hu-bing-zhi-ding-mu-lu-he-shell-bing-pei-zhi-wei-root-zu-y.html"
  - "/ubuntu-tian-jia-xin-yong-hu-bing-zhi-ding-mu-lu-he-shell-bing-pei-zhi-wei-root-zu-yong-hu-sudo.html"
---
ubuntu新建的用户并有新建相应的home目录和对应的shell环境。

### [新建用户并创建home目录的命令和shell环境](#1)

```bash
useradd -r -m -s /bin/bash 用户名
```

修改密码

```bash
passwd 用户名
```

### [配置root权限](#2)

```bash
vi /etc/sudoers
```

添加代码

```bash
用户名 ALL=(ALL:ALL) ALL
```

之后进行root命令操作的时候，执行下面的命令

```bash
sudo 命令
```

然后输入密码，就可以执行

