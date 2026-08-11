---
title: "配置多个ssh key的遇到的问题"
date: "2025-07-01 15:04:13"
slug: "pei-zhi-duo-ge-ssh-key-de-yu-dao-de-wen-ti"
categories: ["技术"]
tags: ["Git", "SSH"]
aliases:
  - "/2025/07/01/配置多个ssh-key的遇到的问题/"
  - "/2025/07/01/配置多个ssh-key的遇到的问题.html"
  - "/配置多个ssh-key的遇到的问题/"
  - "/配置多个ssh-key的遇到的问题.html"
  - "/2025/07/01/pei-zhi-duo-ge-ssh-key-de-yu-dao-de-wen-ti/"
  - "/2025/07/01/pei-zhi-duo-ge-ssh-key-de-yu-dao-de-wen-ti.html"
  - "/pei-zhi-duo-ge-ssh-key-de-yu-dao-de-wen-ti.html"
---
# [配置多个ssh key的遇到的问题](#1)

1，Bad owner or permissions on .ssh/config

2，进行测试的时候总会出现提示输入密码

以上两个问题多数是由于权限的问题

解决问题一：

将config的执行权限修改为600

```bash
sudo chmod 600 ~/.ssh/config
```

解决问题二:

这个问题在我这里出现的原因是由于我将config拥有权限改成了root，导致出现的问题

如果你也遇到这样的问题的话，可以试着改成拥有权限为自己就可以了。

```bash
sudo chown xxx ~/.ssh/config
```

[xxx]为linux的当前用户

执行完之后在测试下，是不是已经就成功了，没有的话可以加群沟通


