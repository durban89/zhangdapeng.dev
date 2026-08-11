---
title: "Can't connect to MySQL server on 'xxx.xxx.xxx.xxx' (61)"
date: "2025-06-05 17:37:45"
slug: "cant-connect-to-mysql-server-on-xxxxxxxxxxxx-61"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/05/Can't-connect-to-MySQL-server-on-'xxx.xxx.xxx.xxx'-(61)/"
  - "/2025/06/05/Can't-connect-to-MySQL-server-on-'xxx.xxx.xxx.xxx'-(61).html"
  - "/Can't-connect-to-MySQL-server-on-'xxx.xxx.xxx.xxx'-(61)/"
  - "/Can't-connect-to-MySQL-server-on-'xxx.xxx.xxx.xxx'-(61).html"
  - "/2025/06/05/Can-t-connect-to-MySQL-server-on-xxx-xxx-xxx-xxx-61/"
  - "/2025/06/05/Can-t-connect-to-MySQL-server-on-xxx-xxx-xxx-xxx-61.html"
  - "/2025/06/05/cant-connect-to-mysql-server-on-xxxxxxxxxxxx-61/"
  - "/2025/06/05/cant-connect-to-mysql-server-on-xxxxxxxxxxxx-61.html"
  - "/cant-connect-to-mysql-server-on-xxxxxxxxxxxx-61.html"
---
我要在本机链接我本机上虚拟机的mysql，我使用mac下的workbench，就就是连接不上，报错信息为：“Can't connect to MySQL server on '10.211.55.5' (61)”，查了好多资料，有一种方法解决了我的问题：

第一步：查看是都3306端口开启
使用ufw（不会安装的，请与我联系），

```shell
sudo ufw status
```
或者直接使用命令

```shell
netstat -an | grep 3306
```
如果结果显示类似：
```shell
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN
```

从结果可以看出3306端口只是在IP 127.0.0.1上监听，所以拒绝了其他IP的访问。

第二步：修改配置文件
修改文件 /etc/mysql/my.cnf文件，打开文件，找到下面内容：
```shell
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address  = 127.0.0.1
```

把上面这一行注释掉或者把127.0.0.1换成合适的IP，建议注释掉。
重新启动后，重新使用netstat检测：
```shell
~# netstat -an | grep 3306
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN
```

第三步：

使用创建的用户登录一下，成功。
