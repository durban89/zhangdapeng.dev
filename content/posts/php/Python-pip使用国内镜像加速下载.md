---
title: "Python-pip使用国内镜像加速下载"
date: "2025-07-01 11:54:20"
slug: "python-pip-shi-yong-guo-nei-jing-xiang-jia-su-xia-zai"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/07/01/Python-pip使用国内镜像加速下载/"
  - "/2025/07/01/Python-pip使用国内镜像加速下载.html"
  - "/Python-pip使用国内镜像加速下载/"
  - "/Python-pip使用国内镜像加速下载.html"
  - "/2025/07/01/python-pip-shi-yong-guo-nei-jing-xiang-jia-su-xia-zai/"
  - "/2025/07/01/python-pip-shi-yong-guo-nei-jing-xiang-jia-su-xia-zai.html"
  - "/python-pip-shi-yong-guo-nei-jing-xiang-jia-su-xia-zai.html"
---
pipy国内镜像目前有：  
  
http://pypi.douban.com/simple/  豆瓣

http://mirrors.aliyun.com/pypi/simple/ 阿里云

https://pypi.tuna.tsinghua.edu.cn/simple 清华大学开源软件镜像站

对于pip这种在线安装的方式来说，很方便，但网络不稳定的话很要命。使用国内镜像相对好一些，  
如果想手动指定源，可以在pip后面跟-i 来指定源，比如用豆瓣的源来安装web.py框架：

```bash
pip install web.py -i http://pypi.douban.com/simple
```

**注意后面要有/simple目录！！！**  
  
如果提示：

> The repository located at pypi.douban.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS it is recommended to use HTTPS instead, otherwise you may silence this warning and allow it anyways with '--trusted-host pypi.douban.com'.

请试试这个的办法

```bash
pip install virtualenv  --trusted-host pypi.douban.com -i http://pypi.douban.com/simple
```

要配制成默认的话，需要创建或修改配置文件  
编辑`~/.pip/pip.conf`:

```bash
nano ~/.pip/pip.conf
```

添加

```bash
[global]
index-url = http://pypi.douban.com/simple
```


