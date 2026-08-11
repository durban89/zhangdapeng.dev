---
title: "给vps设置ssh供翻墙使用"
date: "2025-06-23 16:26:54"
slug: "gei-vps-she-zhi-ssh-gong-fan-qiang-shi-yong"
categories: ["技术"]
tags: ["Linux", "SSH"]
aliases:
  - "/2025/06/23/给vps设置ssh供翻墙使用/"
  - "/2025/06/23/给vps设置ssh供翻墙使用.html"
  - "/给vps设置ssh供翻墙使用/"
  - "/给vps设置ssh供翻墙使用.html"
  - "/2025/06/23/gei-vps-she-zhi-ssh-gong-fan-qiang-shi-yong/"
  - "/2025/06/23/gei-vps-she-zhi-ssh-gong-fan-qiang-shi-yong.html"
  - "/gei-vps-she-zhi-ssh-gong-fan-qiang-shi-yong.html"
---
在服务器上建一个 username ：

添加用户：useradd -s /bin/false username，将用户的shell设置成/bin/false。这样用户就无法与系统进行交互。

设置密码：passwd username

（对已有帐号禁止其shell交互使用：usermod -s /bin/false username）

***小技巧：***

也可以使用 /usr/bin/passwd 作为用户的 shell ，这样用户就可以通过登录而来自主修改密码。需要注意的是，需要将 /usr/bin/passwd 这一行写进 /etc/shells文件。

sshd 认证通后之后，会检查设定的 shell 是否登记在 /etc/shells 文件中，若已经登记，则fork自己，然后fork出来的子进程再exec 设定的 shell 。而 ssh 的 -N 参数，则是告诉 sshd 不需要执行 shell。（ssh本身可以通过参数来设置连接到 sshd 但是不执行远程命令，默认是启动用户设定的 shell ）。

（此文章为转载，未做测试，使用请三思）

