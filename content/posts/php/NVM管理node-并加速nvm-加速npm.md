---
title: "NVM管理node，并加速nvm、加速npm"
date: "2025-07-01 11:54:15"
slug: "nvm-guan-li-node-bing-jia-su-nvm-jia-su-npm"
categories: ["技术"]
tags: ["NVM"]
aliases:
  - "/2025/07/01/NVM管理node，并加速nvm、加速npm/"
  - "/2025/07/01/NVM管理node，并加速nvm、加速npm.html"
  - "/NVM管理node，并加速nvm、加速npm/"
  - "/NVM管理node，并加速nvm、加速npm.html"
  - "/2025/07/01/NVM管理node-并加速nvm-加速npm/"
  - "/2025/07/01/NVM管理node-并加速nvm-加速npm.html"
  - "/2025/07/01/nvm-guan-li-node-bing-jia-su-nvm-jia-su-npm/"
  - "/2025/07/01/nvm-guan-li-node-bing-jia-su-nvm-jia-su-npm.html"
  - "/nvm-guan-li-node-bing-jia-su-nvm-jia-su-npm.html"
---
nvm的安装请转到这里：

https://github.com/creationix/nvm

**下面先说nvm的加速**

nvm 默认是从 http://nodejs.org/dist/ 下载的, 国外服务器, 必然很慢,

好在 nvm 以及支持从镜像服务器下载包, 于是我们可以方便地从七牛的 node dist 镜像下载:

```bash
$ NVM_NODEJS_ORG_MIRROR=http://dist.u.qiniudn.com nvm install 0.12.7
```

于是你就会看到一段非常快速进度条:

```bash
######################################################################## 100.0%
Now using node v0.12.7
```

如果你不想每次都输入环境变量 NVM\_NODEJS\_ORG\_MIRROR, 那么我建议你加入到 .bashrc 文件中:

```bash
# nvm
export NVM_NODEJS_ORG_MIRROR=http://dist.u.qiniudn.com
source ~/git/nvm/nvm.sh
```

然后你可以继续非常方便地安装各个版本的 node 了, 你可以查看一下你当前已经安装的版本:

```bash
nvm ls
```

查看远端的

```bash
nvm ls-remote
```

**下面再说下npm加速**

同理 nvm , npm 默认是从国外的源获取和下载包信息, 不慢才奇怪.

可以通过简单的 ---registry 参数, 使用国内的镜像 http://r.cnpmjs.org :

```bash
$ npm --registry=http://r.cnpmjs.org install koa
```

但是毕竟镜像跟官方的 npm 源还是会有一个同步时间差异, 目前 cnpm 的默认同步时间间隔是 15 分钟.

如果你是模块发布者, 或者你想马上同步一个模块, 那么推荐你安装 cnpm cli:

```bash
$ npm --registry=http://r.cnpmjs.org install cnpm -g
```

通过 cnpm 命令行, 你可以快速同步任意模块:

```bash
$ cnpm sync koa connect mocha
```

呃, 我就是不想安装 cnpm cli 怎么办? 哈哈, 早就想到你会这么懒了, 于是我们还有一个 web 页面:

例如我想马上同步 koa, 直接打开浏览器: http://cnpmjs.org/sync/koa

或者你是命令行控, 通过 open 命令打开:

```bash
$ open http://cnpmjs.org/sync/koa
```


