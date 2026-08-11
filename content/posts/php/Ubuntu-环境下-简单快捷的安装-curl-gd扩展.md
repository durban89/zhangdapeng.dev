---
title: "Ubuntu 环境下 简单快捷的安装 curl、gd扩展"
date: "2025-06-26 11:15:48"
slug: "ubuntu-huan-jing-xia-jian-dan-kuai-jie-de-an-zhuang-curl-gd-kuo-zhan"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/26/Ubuntu-环境下-简单快捷的安装-curl、gd扩展/"
  - "/2025/06/26/Ubuntu-环境下-简单快捷的安装-curl、gd扩展.html"
  - "/Ubuntu-环境下-简单快捷的安装-curl、gd扩展/"
  - "/Ubuntu-环境下-简单快捷的安装-curl、gd扩展.html"
  - "/2025/06/26/Ubuntu-环境下-简单快捷的安装-curl-gd扩展/"
  - "/2025/06/26/Ubuntu-环境下-简单快捷的安装-curl-gd扩展.html"
  - "/2025/06/26/ubuntu-huan-jing-xia-jian-dan-kuai-jie-de-an-zhuang-curl-gd-kuo-zhan/"
  - "/2025/06/26/ubuntu-huan-jing-xia-jian-dan-kuai-jie-de-an-zhuang-curl-gd-kuo-zhan.html"
  - "/ubuntu-huan-jing-xia-jian-dan-kuai-jie-de-an-zhuang-curl-gd-kuo-zhan.html"
---
总结了一个很简单安装方法

第一步：

```bash
# sudo apt-get install curl libcurl3 libcurl3-dev php5-curl
```

第二步：重启服务器，这里以Apache为例

```bash
# sudo /etc/init.d/apache2 restart
```

第三步：新建文件，进行phpinfo测试

```bash
phpinfo();
```

如果有curl扩展说明安装成功。如果木有，请邮件我，进行交流

