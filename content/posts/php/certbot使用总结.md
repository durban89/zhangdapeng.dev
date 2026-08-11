---
title: "certbot使用总结"
date: "2025-07-10 10:57:46"
slug: "certbot-shi-yong-zong-jie"
categories: ["技术"]
tags: ["Certbot"]
aliases:
  - "/2025/07/10/certbot使用总结/"
  - "/2025/07/10/certbot使用总结.html"
  - "/certbot使用总结/"
  - "/certbot使用总结.html"
  - "/2025/07/10/certbot-shi-yong-zong-jie/"
  - "/2025/07/10/certbot-shi-yong-zong-jie.html"
  - "/certbot-shi-yong-zong-jie.html"
---
官方宣称certbot

> 使用EFF的Certbot在您的网站上自动启用HTTPS，部署Let's Encrypt的证书。

> Automatically enable HTTPS on your website with EFF's Certbot, deploying Let's Encrypt certificates.

## 给指定域名生成免费ssl证书方式

举个例子比如我要给我的www.gowhich.com生成证书可以使用如下，命令

```bash
certbot certonly --webroot -w /home/wwwroot/gowhich/web -d www.gowhich.com
```

和

```bash
certbot certonly --standalone --preferred-challenges http -d www.gowhich.com
```

前提，你的域名必须已经解析成功，是否解析成功可以通过下面命令测试

```bash
nslookup www.gowhich.com
```

会得到类似如下信息

```bash
Server:		172.18.0.1
Address:	172.18.0.1#53

Non-authoritative answer:
Name:	www.gowhich.com
Address: xxx.xxx.xxx.xxx # ip地址
```

下面说生成证书的命令

第一个命令，certbot会到你项目创建一个文件，然后通过访问你的域名来访问进行网站验证，通过后则生成证书 第二个命令则是通过启动内部服务，来检测验证网站，最后生成一个证书

我个人的项目比较多，使用的语言也多，Yii开发的项目在使用第一个命令生成证书的时候是没有问题的，但是第一个命令在Flask开发的项目中会遇到问题，提示访问不了文件，可能是路由的问题导致的，暂时没有找到解决思路，但是我们不可能因为一个证书去修改一个项目，如果改的话我觉得也是大费周折，还好certbot提供了第二种方式，只不过会需要暂时停止80端口的访问，这个对于跟人项目而言问题还好不是很严重，所以这里推荐第二种命令的方式。
