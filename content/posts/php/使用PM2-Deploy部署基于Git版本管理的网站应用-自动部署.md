---
title: "使用PM2 Deploy部署基于Git版本管理的网站应用 自动部署"
date: "2025-06-30 15:15:39"
slug: "shi-yong-pm2-deploy-bu-shu-ji-yu-git-ban-ben-guan-li-de-wang-zhan-ying-yong-zi-dong-bu-shu"
categories: ["技术"]
tags: ["PM2", "Git"]
aliases:
  - "/2025/06/30/使用PM2-Deploy部署基于Git版本管理的网站应用-自动部署/"
  - "/2025/06/30/使用PM2-Deploy部署基于Git版本管理的网站应用-自动部署.html"
  - "/使用PM2-Deploy部署基于Git版本管理的网站应用-自动部署/"
  - "/使用PM2-Deploy部署基于Git版本管理的网站应用-自动部署.html"
  - "/2025/06/30/shi-yong-pm2-deploy-bu-shu-ji-yu-git-ban-ben-guan-li-de-wang-zhan-ying-yong-zi-dong-bu-/"
  - "/2025/06/30/shi-yong-pm2-deploy-bu-shu-ji-yu-git-ban-ben-guan-li-de-wang-zhan-ying-yong-zi-dong.html"
  - "/shi-yong-pm2-deploy-bu-shu-ji-yu-git-ban-ben-guan-li-de-wang-zhan-ying-yong-zi-dong-bu-shu.html"
---
按照官方介绍，PM2是一款用于生产环境Node.js应用进程管理的工具。按照民间介绍，它主要有这样几个功能：保证Node.js应用永远在线（挂掉自动重启）、自动负载均衡、零中断重启应用等。

鉴于它是如此优秀，这里还是简要介绍一下前两个功能。

**安装**

首先，它是一个Node.js写的工具，使用npm即可安装使用：

```bash
npm install -g pm2
```

运行Node.js程序

如果不使用pm2，运行Node.js程序是这样：

```bash
node xxx.js
```

使用pm2，是这样：

```bash
pm2 start xxx.js
```

监视模式

如果你正在开发Node.js应用，需要在代码变更后自动重启应用，只需要在pm2的参数中加上--watch即可：

```bash
pm2 start xxx.js --watch
```

cluster模式

默认情况下pm2是以fork模式启动应用的，如果以cluster模式启动的话，则可以使用pm2自带的负载均衡、零间断重启等功能。

```bash
pm2 start xxx.js -i 4
```

上面的命令会以cluster模式启动4个应用进程，并自动为它们提供负载均衡，并且可以使用gracefulReload达到更新应用时不中断服务的效果。

关于cluster模式，可参见朴灵《深入浅出Node.js》一书。

pm2低版本默认是以cluster模式启动的。

**部署应用**

官方文档:https://github.com/Unitech/PM2/blob/master/ADVANCED_README.md#deployment

这才是本文的重点。PM2的部署功能可以实现网站应用的半自动部署功能。注意本文标题没有加“Node.js”，意味着这个功能并不只适用于Node.js网站应用，事实上它部署功能是用shell写的，跟网站使用什么语言没什么关系。

PM2的部署功能与版本管理工具（Git，不确定是否支持SVN，下文以Git为例）结合比较紧，因此需要保证网站项目使用版本管理工具管理代码，并且服务器可以访问到版本管理服务器。

部署功能是在新版本（0.12）中才添加进来的。如果你使用的是旧版本的，需要先升级：

```bash
npm install -g pm2@latest
pm2 updatePM2
```

接下来需要建立一个部署的配置文件，这个文件在本机（操作发布的机器）和服务器上都需要有，因此最好放入Git版本管理中，并且推送到远程代码库（Git服务器）。

切换到项目目录下，然后执行

```bash
pm2 ecosystem
```

即可得到一个示例json文件（例如我得到的是ecosystem.json5），将它做对应的修改，大致如下：

```json
{
  "apps" : [{
    "name"      : "API",
    "script"    : "app.js",
    "env": {
      "COMMON_VARIABLE": "true"
    },
    "env_production" : {
      "NODE_ENV": "production"
    }
  },{
    "name"      : "WEB",
    "script"    : "web.js"
  }],
  "deploy" : {
    "production" : {
      "user" : "node",//登录账号
      "host" : "212.83.163.1",//服务器地址
      "ref"  : "origin/master",//git 分支
      "repo" : "xx@xx:repo.git",//git地址
      "path" : "/var/www/production",//服务器项目目录
      "post-deploy" : "pm2 startOrRestart ecosystem.json5 --env production"
    },
    "dev" : {
      "user" : "node",
      "host" : "212.83.163.1",
      "ref"  : "origin/master",
      "repo" : "xx@xx:repo.git",
      "path" : "/var/www/development",
      "post-deploy" : "pm2 startOrRestart ecosystem.json5 --env dev",
      "env"  : {
        "NODE_ENV": "dev"
      }
    }
  }
}
```

需要注意：

apps.name和apps.script应该与PM2识别应用有关，后续执行`pm2 restart`的时候可以对应到进程（未证实）

deploy中可以含有多个环境，需要能够通过SSH（公钥认证）登录服务器

web目录并不是真正的放版本库文件的目录，PM2会再建立一个source子目录，这个才是真正放代码的目录

post-deploy是指代码部署完之后执行的命令，这里以Node.js为例子，执行依赖安装，然后重启PM2中的进程

然后就可以使用

首先需要安装一下

```bash
pm2 deploy ecosystem.json5 production setup
```

这个过程中可能会涉及到权限的问题，不过都是一些小的问题

如果已经安装可以运行下面这个命令

```bash
pm2 deploy ecosystem.json5 production
```

自动发布网站项目了，非常方便。

```bash
xx@xx:~/nodejs/node-react$ pm2 deploy ecosystem.json5 production
--> Deploying to production environment
--> on host 205.209.156.140
  ○ deploying
  ○ hook pre-deploy
  ○ fetching updates
xx@xx's password: 
Fetching origin
From https://git.oschina.net/zhangdapeng89/node-react
   4456ce1..c45f87c  master     -> origin/master
  ○ resetting HEAD to origin/master
xx@xx's password: 
HEAD is now at c45f87c 添加eco
xx@xx's password: 
xx@xx's password: 
  ○ executing post-deploy `pm2 startOrRestart ecosystem.json5 --env production`
xx@xx's password: 
┌──────────┬────┬──────┬───────┬────────┬─────────┬────────┬──────────────┬──────────┐
│ App name │ id │ mode │ pid   │ status │ restart │ uptime │ memory       │ watching │
├──────────┼────┼──────┼───────┼────────┼─────────┼────────┼──────────────┼──────────┤
│ app      │ 0  │ fork │ 5843  │ online │ 958     │ 11D    │ 133.094 MB   │ disabled │
│ API      │ 1  │ fork │ 22700 │ online │ 0       │ 0s     │ 12.219 MB    │ disabled │
│ WEB      │ 2  │ fork │ 22705 │ online │ 0       │ 0s     │ 11.746 MB    │ disabled │
└──────────┴────┴──────┴───────┴────────┴─────────┴────────┴──────────────┴──────────┘
 Use `pm2 show <id|name>` to get more details about an app
  ○ hook test
  ○ successfully deployed origin/master
--> Success
```


