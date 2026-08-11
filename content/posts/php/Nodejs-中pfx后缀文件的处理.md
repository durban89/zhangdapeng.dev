---
title: "Nodejs 中pfx后缀文件的处理"
date: "2025-07-03 11:08:16"
slug: "nodejs-zhong-pfx-hou-zhui-wen-jian-de-chu-li"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-中pfx后缀文件的处理/"
  - "/2025/07/03/Nodejs-中pfx后缀文件的处理.html"
  - "/Nodejs-中pfx后缀文件的处理/"
  - "/Nodejs-中pfx后缀文件的处理.html"
  - "/2025/07/03/nodejs-zhong-pfx-hou-zhui-wen-jian-de-chu-li/"
  - "/2025/07/03/nodejs-zhong-pfx-hou-zhui-wen-jian-de-chu-li.html"
  - "/nodejs-zhong-pfx-hou-zhui-wen-jian-de-chu-li.html"
---
nodejs中，在做加密解密的时候，会得到第三方的各种各样的加密文件，其后缀也就那么几种吧，.key/.pem/.pfx等，是不是可以自定义，反正就是一个文件。

但是今天我看了很多的nodejs库好像也没有找到与java keytool这样的工具，因为在java里面，完全是可以读取pfx,然户进行在进行处理的，如果在nodejs中要如何操作，目前不知道，使用openssl做个转换处理先。

第一个命令是:

```bash
openssl pkcs12 -in xxxx.pfx -nocerts -nodes -out domain_encrypted.key
```

第二个命令是:

```bash
openssl rsa -in domain_encrypted.key -out private.key
```

哪位大神知道的，可以告知下，谢谢了。

==================补充=================

google上有个办法可以解析出两种格式的文件

第一种格式文件的方式

extract private key from .pfx file

```bash
# openssl pkcs12 -in myfile.pfx -nocerts -out private_key.pem -nodes
Enter Import Password:
MAC verified OK
```

第二种格式文件的方式

extract certificate from .pfx file

```bash
# openssl pkcs12 -in myfile.pfx -nokeys -out certificate_file.crt 
Enter Import Password:
MAC verified OK
```

详细的可到这里：<http://tecadmin.net/extract-private-key-and-certificate-files-from-pfx-file/>

==========================================

==========================================强烈补充

多日奋战，终于解决了这个问题，因为一直是一个私钥解密的问题

```bash
openssl pkcs12 -in xxxx_private.pfx -out xxxx_private.pem -nodes
openssl x509 -in xxxx_public.crt -inform der -outform pem -out xxxx_public.pem
```

这里主要是针对具体情况具体描述，可以变通取处理

因为对方给过来的是一个在window环境下，使用工具生成的pfx和crt文件。

经过对方给过来的生成工具的描述，这个crt文件还是一个cer后缀文件自己修改的cer->crt。可见这里如果对文件内容不了解，光从后缀来看会坑了很多人。

先来看第一行的命令语句.

经过文档的查询pfx文件是一个带有私钥跟证书的合体文件，通过上面的命令就可以得到一个文件就是private.pem，里面是一个含有证书和私钥的。

不知道的我这里举例。

私钥是以

```bash
-----BEGIN RSA PRIVATE KEY-----
```

开头的。

证书是以

```bash
-----BEGIN CERTIFICATE-----
```

开头的。对不起不方便把所有内容同时贴出来。很容易辨别的。

然后对方还会给你一个crt文件，这个事实上就是一个x509对应的证书，需要解出来，但是对于是java的应该就不需要了，不过是php的或这是node的就需要了。

当然是证书的话，就必须是以

```bash
-----BEGIN CERTIFICATE-----
```

开头的。

好了，如果你跟别人对接接口，遇到私钥公钥的问题，但是对方给了你pfx和crt文件的话，就按照这个命令去操作的吧，我已经在php和node环境下试过了。不过具体的算法还是要针对具体的情况来实施。

================2016-11-11补充================

```bash
REM export the ssl cert (normal cases)
openssl pkcs12 -in aa.pfx -out aa.pem -nokeys -clcerts

REM export the ssl cert (Crescendo load balancers)

openssl pkcs12 -in aa.pfx -out aa_tmp_cn.pem -nodes
openssl x509 -in aa_tmp_cn.pem -out aa_cn.pem -text
```


