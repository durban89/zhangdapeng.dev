---
title: "为LNMP设置空头主机防止恶意解析（Linux nginx MySQL PHP）"
date: "2025-06-23 15:27:53"
slug: "wei-lnmp-she-zhi-kong-tou-zhu-ji-fang-zhi-e-yi-jie-xi-linux-nginx-mysql-php"
categories: ["技术"]
tags: ["LNMP", "Linux"]
aliases:
  - "/2025/06/23/为LNMP设置空头主机防止恶意解析（Linux-nginx-MySQL-PHP）/"
  - "/2025/06/23/为LNMP设置空头主机防止恶意解析（Linux-nginx-MySQL-PHP）.html"
  - "/为LNMP设置空头主机防止恶意解析（Linux-nginx-MySQL-PHP）/"
  - "/为LNMP设置空头主机防止恶意解析（Linux-nginx-MySQL-PHP）.html"
  - "/2025/06/23/为LNMP设置空头主机防止恶意解析-Linux-nginx-MySQL-PHP/"
  - "/2025/06/23/为LNMP设置空头主机防止恶意解析-Linux-nginx-MySQL-PHP.html"
  - "/2025/06/23/wei-lnmp-she-zhi-kong-tou-zhu-ji-fang-zhi-e-yi-jie-xi-linux-nginx-mysql-php/"
  - "/2025/06/23/wei-lnmp-she-zhi-kong-tou-zhu-ji-fang-zhi-e-yi-jie-xi-linux-nginx-mysql-php.html"
  - "/wei-lnmp-she-zhi-kong-tou-zhu-ji-fang-zhi-e-yi-jie-xi-linux-nginx-mysql-php.html"
---
恶意解析 是指有人通过域名A记录直接解析别人IP地址，从而得到一个在访问者眼中完全相同网站,也会造成搜索引擎收录别人的域名  
主要被称作:PR劫持,恶意网站镜像,恶意克隆,恶意解析域名到自己的服务器等  
  
给lnmp环境设置空头主机是很有必要的,比如说lnmp环境默认的虚拟空间目录是”`/home/wwwroot`”当然不建议大家把站点绑定在这个目录里,因为处于安全考虑最好是自己新建一个目录!lnmp环境安装完后”phpmyadmin”和”FTP”默认是装在”`/home/wwwroot`” 的目录里,比如访问”phpmyadmin”那么路径应该是:”IP/phpmyadmin/” . 但有些无聊的人把自己的域名解析到你的IP上.这样通过他的域名可以直接访问你的站点,这点让人很不爽.所以,给lnmp设置空头主机是非常必要的,除非你为FTP和phpmyadmin分别绑定独立的域名,但这样不方便管理..
  
以下是空主机头设置方法:  
  
第一步: 使用 `/root/vhost.sh` 建立虚拟主机的命令来绑定你一开始设置的那个二级域名到 /home/wwwroot（wwwroot后面没有”/”）  
  
第二步: 通过SSH客户端，找到 `usr/local/nginx/conf/nginx.conf` （请看好这个目录，）把里面的

server段中的

```bash
server {
    listen       80;
    server_name www.xxx.com;
    index index.html index.htm index.php;
    root  /home/wwwroot;
}
```

改成

```bash
server {
    listen 80 default;
    return 500;
}
```

然后保存。  
  
第三步: 重新启动Nginx服务器，命令是   `/usr/local/nginx/sbin/nginx -s reload`
  
自己想管理”/home/wwwroot  ”目录内容只需要输入”域名/目录/”便可以了!别人解析到你的IP返回的是500错误

