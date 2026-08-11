---
title: "acme.sh配置ssl证书，以后不需要在去各大平台去申请了"
date: "2025-07-15 10:29:16"
slug: "acmesh-pei-zhi-ssl-zheng-shu-yi-hou-bu-xu-yao-zai-qu-ge-da-ping-tai-qu-shen-qing-le"
categories: ["技术"]
tags: ["SSL"]
aliases:
  - "/2025/07/15/acme.sh配置ssl证书，以后不需要在去各大平台去申请了/"
  - "/2025/07/15/acme.sh配置ssl证书，以后不需要在去各大平台去申请了.html"
  - "/acme.sh配置ssl证书，以后不需要在去各大平台去申请了/"
  - "/acme.sh配置ssl证书，以后不需要在去各大平台去申请了.html"
  - "/2025/07/15/acme-sh配置ssl证书-以后不需要在去各大平台去申请了/"
  - "/2025/07/15/acme-sh配置ssl证书-以后不需要在去各大平台去申请了.html"
  - "/2025/07/15/acmesh-pei-zhi-ssl-zheng-shu-yi-hou-bu-xu-yao-zai-qu-ge-da-ping-tai-qu-shen-qing-le/"
  - "/2025/07/15/acmesh-pei-zhi-ssl-zheng-shu-yi-hou-bu-xu-yao-zai-qu-ge-da-ping-tai-qu-shen-qing-le.html"
  - "/acmesh-pei-zhi-ssl-zheng-shu-yi-hou-bu-xu-yao-zai-qu-ge-da-ping-tai-qu-shen-qing-le.html"
---
ssl证书在当代是一个比较流行的技术

但是配置起来可谓是很麻烦，尤其是各大平台有免费的也是要自己去申请下，然后绑定dns验证，通过后在审批证书而且每年要自己去申请

技术是用来方便生活的，为何大家总想着为难自己也去为难别人

记录下使用经历

初次体验下来，最后的理想效果是能够进行自动更新免去了手动配置的烦恼

https://github.com/acmesh-official/acme.sh

这里是官方的地址，可以自行访问下

我记录下自己的使用心得

我用的是nginx

安装完acme.sh就可以生成证书了

```bash
acme.sh --issue -d gowhich.com -d www.gowhich.com -w /var/www/gowhich/web
```

我的博客是用Yii2搭建的，项目目录在/var/www/gowhich

如果你是其他的项目请自行查资料或者关注我交流下

```bash
[2023年 04月 13日 星期四 15:49:50 CST] Your cert is in: /home/dpzhang/.acme.sh/gowhich.com_ecc/gowhich.com.cer
[2023年 04月 13日 星期四 15:49:50 CST] Your cert key is in: /home/dpzhang/.acme.sh/gowhich.com_ecc/gowhich.com.key
[2023年 04月 13日 星期四 15:49:50 CST] The intermediate CA cert is in: /home/dpzhang/.acme.sh/gowhich.com_ecc/ca.cer
[2023年 04月 13日 星期四 15:49:50 CST] And the full chain certs is there: /home/dpzhang/.acme.sh/gowhich.com_ecc/fullchain.cer
```

最后生成的文件是这样的

我想的是就算后面到期的话，如果要手动进行操作的话，文件的存放还是一样的路径，所以我觉得直接用软链接就好了，这个就不用以后每次都去copy了

```bash
sudo ln -s /home/dpzhang/.acme.sh/gowhich.com_ecc/fullchain.cer ./gowhich.com.crt
sudo ln -s /home/dpzhang/.acme.sh/gowhich.com_ecc/gowhich.com.key ./gowhich.com.key
```

nginx的配置

```bash
ssl_certificate ssl/gowhich.com/gowhich.com.crt;
ssl_certificate_key ssl/gowhich.com/gowhich.com.key;
```

对应的路径可以根据具体的配置来配置

配置完之后重启下nginx就好了
