---
title: "在Ubuntu 12.04 Server上安装部署Ruby on Rails应用"
date: "2025-06-25 10:09:40"
slug: "zai-ubuntu-1204-server-shang-an-zhuang-bu-shu-ruby-on-rails-ying-yong"
categories: ["技术"]
tags: ["Ubuntu", "Linux", "Ruby", "Rails"]
aliases:
  - "/2025/06/25/在Ubuntu-12.04-Server上安装部署Ruby-on-Rails应用/"
  - "/2025/06/25/在Ubuntu-12.04-Server上安装部署Ruby-on-Rails应用.html"
  - "/在Ubuntu-12.04-Server上安装部署Ruby-on-Rails应用/"
  - "/在Ubuntu-12.04-Server上安装部署Ruby-on-Rails应用.html"
  - "/2025/06/25/在Ubuntu-12-04-Server上安装部署Ruby-on-Rails应用/"
  - "/2025/06/25/在Ubuntu-12-04-Server上安装部署Ruby-on-Rails应用.html"
  - "/2025/06/25/zai-ubuntu-1204-server-shang-an-zhuang-bu-shu-ruby-on-rails-ying-yong/"
  - "/2025/06/25/zai-ubuntu-1204-server-shang-an-zhuang-bu-shu-ruby-on-rails-ying-yong.html"
  - "/zai-ubuntu-1204-server-shang-an-zhuang-bu-shu-ruby-on-rails-ying-yong.html"
---
最近我对新知识手痒痒啦，嘿嘿，ruby，对不起了，骚扰一下你哈，想自己自己在本机安装一个Ruby on Rails用用（玩玩）。搜索了好多的文章，嘿嘿，结果还挺多的

这里简单罗列一下我参考的文章地址

> <http://ruby-china.org/wiki/install-rails-on-ubuntu-12-04-server>
>
> <http://ruby-china.org/wiki/install_ruby_guide>

基本上过程就是这样这个样子的。如下：（环境：Ubuntu Server 12.04）

第一步：配置 Ubuntu Server 系统

如果你是国内服务器，推荐修改网易的源

1、输入 sudo vi /etc/apt/sources.list 将里面的内容替换成：

```bash
deb http://mirrors.163.com/ubuntu/ precise main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
```

然后更新一下:

```bash
$ sudo apt-get update#(一定要执行)
```

2、安装必要的三方库

```bash
$ sudo apt-get install -y wget vim build-essential openssl libreadline6 libreadline6-dev libmysqlclient-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libxml2-dev libxslt-dev libcurl4-openssl-dev autoconf automake libtool imagemagick libmagickwand-dev libpcre3-dev nodejs libpq-dev
```

第二步：安装 Ruby, Rails 及相关

1、安装 RVM

```bash
$ curl -L https://get.rvm.io | bash -s stable
$ echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"' >>~/.bashrc
$ source ~/.bashrc
$ rvm -v
```

2、安装 Ruby

如果你是国内服务器，推荐将 RVM 的安装源替换成 Taobao 的镜像服务器，这样安装能更快！

```bash
$ sed -i -e 's/ftp\.ruby-lang\.org\/pub\/ruby/ruby\.taobao\.org\/mirrors\/ruby/g' ~/.rvm/config/db
```

3、用 RVM 安装 Ruby:

```bash
$ rvm pkg install readline openssl
$ rvm install 2.0.0
$ rvm use 2.0.0 --default
$ ruby -v
ruby 2.0.0p247
```

国内服务器推荐替换 RubyGems 的到淘宝镜像:

```bash
$ gem sources --remove https://rubygems.org/
$ gem sources -a http://ruby.taobao.org/
$ gem sources -l
*** CURRENT SOURCES ***
http://ruby.taobao.org
```

4、安装 Rails

```bash
$ gem install rails
$ rails -v
Rails 4.0.0
```

第三步：部署你的网站

接下来你可以通过 Git 或其他方式将你项目的源代码提交到服务器上面，建议放到用户的 ~/www 下面。

为了方便教程，我们假设，用户是 jason (拥有 sudo 权限), 项目名 gitlab 后面遇到类似的地方请更具自己的情况修改

```bash
$ cd ~/
$ pwd
/home/jason/
$ mkdir www
$ cd www
$ git clone xx@xx:gitlab.git
$ cd gitlab
$ bundle install
```

修改你的数据库配置，创建数据库，合并 migration ...这些是 Rails 开发的基础，这里就不细说了，重点是最后你能让你的项目能用 rails s 跑起来！

```bash
$ rails s -e production
```

第四步：安装 Passenger 用于部署 Rails 应用

```bash
$ gem install passenger
$ passenger -v
Phusion Passenger version 4.0.10
```

由于 Passenger 需要重新编译 Nginx，如果你之前有安装 Nginx 需要卸载掉！

nginx -v，有的话卸载

```bash
$ sudo apt-get remove nginx-common nginx-full nginx
```

用 Passenger 安装 Nginx

```bash
$ sudo passenger-install-nginx-module
```

接下来会出现提示，选择 Yes: download, compile and install Nginx for me. (recommended) ，对于后面的提示一直选默认哪项，敲回车。

最后看到

Nginx with Passenger support was successfully installed.

表示你人品很好 Nginx 安装成功！否则请看 Passenger 官方安装文档 自行解决……

第五步：安装 Nginx init script

接下来你需要安装 Nginx 的启动脚本，以及配置开机自动启动

```bash
$ cd ~/
$ git clone git://github.com/jnstq/rails-nginx-passenger-ubuntu.git
$ sudo mv rails-nginx-passenger-ubuntu/nginx/nginx /etc/init.d/nginx
$ sudo chmod +x /etc/init.d/nginx
```

配置 Nginx 开机自启动

```bash
$ sudo update-rc.d nginx defaults
```

配置 Nginx 与网站

打开 Nginx 的 nginx.conf

```bash
$ sudo vim /opt/nginx/conf/nginx.conf
```

PS: 如果你不是 Passenger 安装的 Nginx，这个配置文件还有可能在 /usr/local/nginx/ 或 /etc/nginx 下面

请参考下面的例子修改：

```ini
user jason; # 修改成你的系统帐号名，不然项目目录 /home/jason/www 这里没有权限
worker_processes 8; # 修改成和你 CPU 核数一样
pid /var/run/nginx.pid;
http {
 include       mime.types;
 default_type  application/octet-stream;
 client_max_body_size 50m;
 sendfile        on;
 access_log /var/log/nginx/access.log;
 error_log /var/log/nginx/error.log;
 gzip on;
 gzip_disable "msie6";
 ## ------------ 重点修改内容 --------
 server {    
   # 此处用于防止其他的域名绑定到你的网站上面
   listen 80 default;
   return 403;
 }
 server {
   listen       80;
   server_name  you.host.name; # 请替换成你网站的域名
   rails_env    production;
   root         /home/jason/www/gitlab/public;
   passenger_enabled on;
   location ~ ^(/assets) {
     access_log        off;
     # 设置 assets 下面的浏览器缓存时间为最大值（由于 Rails Assets Pipline 的文件名是根据文件修改产生的 MD5 digest 文件名，所以此处可以放心开启）
     expires           max; 
   }
 }
 ## ---------------------------------
}
```

以上几个步骤经过我的测试是困难重重啊，毕竟是参看别人的文章，我会在评论中，将相应的错误付给大家的

