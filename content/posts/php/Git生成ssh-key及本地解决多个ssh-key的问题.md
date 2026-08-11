---
title: "Git生成ssh key及本地解决多个ssh key的问题"
date: "2025-07-01 15:04:16"
slug: "git-sheng-cheng-ssh-key-ji-ben-di-jie-jue-duo-ge-ssh-key-de-wen-ti"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/01/Git生成ssh-key及本地解决多个ssh-key的问题/"
  - "/2025/07/01/Git生成ssh-key及本地解决多个ssh-key的问题.html"
  - "/Git生成ssh-key及本地解决多个ssh-key的问题/"
  - "/Git生成ssh-key及本地解决多个ssh-key的问题.html"
  - "/2025/07/01/git-sheng-cheng-ssh-key-ji-ben-di-jie-jue-duo-ge-ssh-key-de-wen-ti/"
  - "/2025/07/01/git-sheng-cheng-ssh-key-ji-ben-di-jie-jue-duo-ge-ssh-key-de-wen-ti.html"
  - "/git-sheng-cheng-ssh-key-ji-ben-di-jie-jue-duo-ge-ssh-key-de-wen-ti.html"
---
ssh是一种网络协议，用于计算机之间的加密登录。ssh原理及应用可参考：

SSH原理与运用（一）：远程登录

# [生成ssh key步骤](#1)

这里以配置github的ssh key为例：

1. 生成ssh key

```bash
ssh-keygen -t rsa -C "邮箱"
```

然后根据提示连续回车即可在~/.ssh目录下得到id_rsa和id_rsa.pub两个文件，id_rsa.pub文件里存放的就是我们要使用的key。

2. 上传key到github

```bash
clip < ~/.ssh/id_rsa.pub
```

复制key到剪贴板

登录github

点击右上方的Accounting settings图标

选择 SSH key

点击 Add SSH key

3. 测试是否配置成功

```bash
ssh -T xxx@xxx.com
```

如果配置成功，则会显示：

```bash
Hi username! You’ve successfully authenticated, but GitHub does not provide shell access.
```

# [解决本地多个ssh key问题](#2)

有的时候，不仅github使用ssh key，工作项目或者其他云平台可能也需要使用ssh key来认证，如果每次都覆盖了原来的id_rsa文件，那么之前的认证就会失效。这个问题我们可以通过在~/.ssh目录下增加config文件来解决。

下面以配置git oschina的ssh key为例。

1. 生成ssh key时同时指定保存的文件名,这里也可以不用指定，只需要在创建的时候根据提示修改就可以，这里使用直接指定路径文件名的方式

```bash
ssh-keygen -t rsa -f ~/.ssh/oschina/id_rsa -C "email"
```

这时~/.ssh目录下会多出oschina/id_rsa和oschina/id_rsa.pub两个文件，id_rsa.pub里保存的就是我们要使用的key。

2. 新增并配置config文件

添加config文件

如果config文件不存在，先添加；存在则直接修改

```bash
touch ~/.ssh/config
```

在config文件里添加如下内容(User表示你的用户名)

```bash
Host git.oschina.net
    HostName git.oschina.net
    IdentityFile ~/.ssh/oschina/id_rsa
    User git
```

3. 上传key到oschina <http://git.oschina.net/profile/sshkeys>

4. 测试ssh key是否配置成功

```bash
ssh -T xx@xx
```

成功的话会显示：

```bash
Welcome to Git@OSC, 张大鹏!
```

至此，本地便成功配置多个ssh key。日后如需添加，则安装上述配置生成key，并修改config文件即可。

提示：在此过程中会出现如下问题

1，Bad owner or permissions on .ssh/config

2，进行测试的时候总会出现提示输入密码

解决办法参照另外一篇文章[点击这里](http://gowhich.com/blog/687)


