---
title: "Certbot免费https证书安装"
date: "2025-07-03 17:37:31"
slug: "certbot-mian-fei-https-zheng-shu-an-zhuang"
categories: ["技术"]
tags: ["Certbot"]
aliases:
  - "/2025/07/03/Certbot免费https证书安装/"
  - "/2025/07/03/Certbot免费https证书安装.html"
  - "/Certbot免费https证书安装/"
  - "/Certbot免费https证书安装.html"
  - "/2025/07/03/certbot-mian-fei-https-zheng-shu-an-zhuang/"
  - "/2025/07/03/certbot-mian-fei-https-zheng-shu-an-zhuang.html"
  - "/certbot-mian-fei-https-zheng-shu-an-zhuang.html"
---
## Install certbot 安装certbot

安装步骤可到这里 https://certbot.eff.org/#debianjessie-nginx 根据自己的服务器情况选择具体的安装版本

## 配置证书

可以使用如下命令，这样的好处是我们可以在下次进行自动更新证书的话，可以方便的处理证书

```bash
certbot certonly --webroot -w /home/wwwroot/www1.gowhich.com/web -d gowhich.com -d www.gowhich.com
```

注意这里的webroot路径一定是你静态文件能够被访问到的，不然，无法进行证书验证

比如我的另外一个域名可以这样设置【Flask项目】

```bash
certbot certonly --webroot -w /home/wwwroot/www.walkerfree.com/walkerfree/static -d walkerfree.com -d www.walkerfree.com
```

输出如下：

```bash
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Starting new HTTPS connection (1): acme-v01.api.letsencrypt.org
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for walkerfree.com
http-01 challenge for www.walkerfree.com
Using the webroot path /home/wwwroot/www.walkerfree.com/walkerfree/static for all unmatched domains.
Waiting for verification...
Cleaning up challenges
Generating key (2048 bits): /etc/letsencrypt/keys/0003_key-certbot.pem
Creating CSR: /etc/letsencrypt/csr/0003_csr-certbot.pem

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/walkerfree.com/fullchain.pem. Your cert will
   expire on 2018-01-22. To obtain a new or tweaked version of this
   certificate in the future, simply run certbot again. To
   non-interactively renew *all* of your certificates, run "certbot
   renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

然后就可以进行nginx配置了

当我们不希望每次都来自己更新，或者自己忘记了更新，证书过期了，不就很危险了，执行下面的命令试试 是否可以正常的自动更新，如果可以的话 我们就把此命令加入我们的定时任务中就可以了

```bash
sudo certbot renew --dry-run
```

加入定时任务

```bash
30 2 * * 1 /usr/bin/certbot renew  >> /var/log/certbot-renew.log
```

每周一半夜2点30分执行renew任务。

---

**2019-02-20补充**

通过下面命令可以通过certbot自己的服务器来验证证书 - 这个只在自己的网站不支持验证证书的情况下使用

```bash
certbot certonly --standalone --preferred-challenges http -d walkerfree.com -d www.walkerfree.com
```

注意：前提可能需要将自己本地监听80端口的服务器暂时停掉一会
