---
title: "使用Linode vps的ssh功能来翻墙"
date: "2025-06-23 16:26:50"
slug: "shi-yong-linode-vps-de-ssh-gong-neng-lai-fan-qiang"
categories: ["技术"]
tags: ["Linode", "Linux", "SSH"]
aliases:
  - "/2025/06/23/使用Linode-vps的ssh功能来翻墙/"
  - "/2025/06/23/使用Linode-vps的ssh功能来翻墙.html"
  - "/使用Linode-vps的ssh功能来翻墙/"
  - "/使用Linode-vps的ssh功能来翻墙.html"
  - "/2025/06/23/shi-yong-linode-vps-de-ssh-gong-neng-lai-fan-qiang/"
  - "/2025/06/23/shi-yong-linode-vps-de-ssh-gong-neng-lai-fan-qiang.html"
  - "/shi-yong-linode-vps-de-ssh-gong-neng-lai-fan-qiang.html"
---
如果你购买了linode 的vps，就可以使用它做代理上国外的网站，比如facebook，twitter等，不用代理，这些网站在国内是无法否则的，原因不用多说。下面是linode设置代理上网的方法：

1, 打开PuTTY，输入主机名或IP地址。

2, 切换到Connection -> SSH -> Tunnels ，设定Source port: 7070（端口号随你喜欢,autoproxy有一条7070端口的记录，设置成这个后面就不用加了）; Destination: 空白, Dynamic，设定完记得按Add。

3，如有需要，可回到Session保存(Save)设定值，以后运行PuTTY时可直接加载(Load)设定值。在任何时候按”Open”即可以目前设定进行连接。

4，登录SSH后，将PuTTY界面最小化，保持SSH连接。

5，设置firefox使用putty生成的socks5代理服务器上网。我们先使用firefox试用一下，autoproxy插件根据个人爱好安装。

运行firefox，选择“工具”->“选项”，选择“高级”->“网络”，

点击“配置Firefox如何连接至因特网”后的“设置…”，弹出对话框，选择sock5，端口填7070。

6，这一步很关键：

经过上面的设置，firefox已经能够访问大部分网站了，但仍然不能访问非死不可和推特，这是为什么呢？原 来，非死不可的 dns查询被动了手脚，无论你向哪个dns服务器查询非死不可的ip地址，都会返回一个错误的结果。幸运的是firefox支持让远程服务器解析 dns地址，但是这个功能默认是关闭的。而IE目前却缺少远程解析dns的功能。

在firefox的地址栏输入“about:config”进入firefox的高级设置页面，过滤器处输入dns后搜索，找到“network.proxy.socks\_remote\_dns”项，把它的值改为“true”，然后重新启动firefox：

好了，现在我们终于能访问久违了的推特。

7，高级：让firefox自动选择代理服务器（这节不是必须的，可以不看）：

使用ssh是占用我们vps的流量的，如果你访问完推特又访问新浪微博、百度，访问国内网站的时候会很慢，还占用了流量，firefox的AutoProxy插件就是解决这个问题的。

AutoProxy会维护一个不能正常访问的网站列表，一旦用户访问列表中的网站，就自动调用代理服务器，而访问不在列表上的网站时，就不会使用代理服务器。

