---
title: "Nodejs开发部署环节整理"
date: "2025-07-02 15:40:44"
slug: "nodejs-kai-fa-bu-shu-huan-jie-zheng-li"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/02/Nodejs开发部署环节整理/"
  - "/2025/07/02/Nodejs开发部署环节整理.html"
  - "/Nodejs开发部署环节整理/"
  - "/Nodejs开发部署环节整理.html"
  - "/2025/07/02/nodejs-kai-fa-bu-shu-huan-jie-zheng-li/"
  - "/2025/07/02/nodejs-kai-fa-bu-shu-huan-jie-zheng-li.html"
  - "/nodejs-kai-fa-bu-shu-huan-jie-zheng-li.html"
---
做web网站开发一般都会分为三个环节:开发阶段【开发模式】、调试阶段【调试模式】、部署阶段【部署模式】

在Node的环境中：

---

开发阶段我们希望能够即使响应我们的开发速度，node启动的方式大家都知道 node app.js ,如果中间有修改的话，就不能即使响应了，需要我们自己再去重新启动。

所以我们的开发阶段最好是安装一下supervisor

安装

```bash
npm install --save-dev supervisor
```

启动

```bash
supervisor app.js or supervisor www/bin
```

【此种方法启动，需要作为一个全局去安装supervisor】

我的实践是把package.json里的start

```js
"scripts": {
  "d": "node-debug app.js",
  "start": "./node_modules/.bin/supervisor app.js"
}
```

然后

```bash
npm start
```

---

调试阶段，我们肯定是希望监测每个请求的响应结果，一旦出现问题可以直接更加友好的展示给我们：

推荐node-inspector

安装

```bash
npm install --save node-inspector
```

启动

```bash
node-inspector app.js or node-debug www/bin
```

【此种方法启动，需要作为一个全局去安装supervisor】

我的实践是把package.json里的d里

```js
"scripts": {
  "d": "./node_modules/.bin/node-debug app.js",
  "start": "./node_modules/.bin/supervisor app.js"
}
```

然后执行

```bash
npm run d
```

---

部署阶段就是我们通常所说的生产环境或者是产品上线

推荐使用pm2

pm2是非常优秀工具，它提供对基于node.js的项目运行托管服务。它基于命令行界面，提供很多特性：

> 内置的负载均衡器（使用nodecluster module）
>
> 以守护进程运行
>
> 0s(不间断)重启
>
> 为ubuntu/ CentOS 提供启动脚本
>
> 关闭不稳定的进程（避免无限死循环）
>
> 基于控制台监控
>
> HTTP API
>
> 远程控制以及实时监控接口

pm2使用nodecluster构建一个内置的负载均衡器。部署多个app的实例来达到分流的目的以减轻单app处理的压力。

安装pm2

```bash
npm install -g pm2
```

查看基本帮助文档

>   Basic Examples:
>
>     Start an app using all CPUs available + set a name :
>
>     $ pm2 start app.js -i 0 --name "api"
>
>     Restart the previous app launched, by name :
>
>     $ pm2 restart api
>
>     Stop the app :
>
>     $ pm2 stop api
>
>     Restart the app that is stopped :
>
>     $ pm2 restart api
>
>     Remove the app from the process list :
>
>     $ pm2 delete api
>
>     Kill daemon pm2 :
>
>     $ pm2 kill
>
>     Update pm2 :
>
>     $ npm install pm2@latest -g ; pm2 updatePM2
>
>     More examples in https://github.com/Unitech/pm2#usagefeatures
>
>   Deployment help:
>
>     $ pm2 deploy help

上面基本是我们比较常用的

我们也可以把启动信息写入到json配置文件中->ecosystem.json

```json
{
  "apps": [
    {
      "name": "web.0",
      "max_memory_restart": "1024M",
      "log_date_format": "YYYY-MM-DD HH:mm:ss SSS",
      "script": "/var/www/web/bundle/main.js",
      "out_file": "/var/log/web/app.0.log",
      "error_file": "/var/log/web/err.0.log",
      "port": "8080",
      "env": {
        "CDN_PREFIX": "//dbde4sd21oahf.cloudfront.net",
        "MONGO_URL": "mongodb://localhost:27017/web",
        "MONGO_OPLOG_URL": "mongodb://localhost:27017/local",
        "ROOT_URL": "http://web.com",
        "PORT": "8080"
      }
    },
    {
      "name": "web.1",
      "max_memory_restart": "1024M",
      "log_date_format": "YYYY-MM-DD HH:mm:ss SSS",
      "script": "/var/www/web/bundle/main.js",
      "out_file": "/var/log/web/app.1.log",
      "error_file": "/var/log/web/err.1.log",
      "port": "8081",
      "env": {
        "CDN_PREFIX": "//dbde4sd21oahf.cloudfront.net",
        "MONGO_URL": "mongodb://localhost:27017/web",
        "MONGO_OPLOG_URL": "mongodb://localhost:27017/local",
        "ROOT_URL": "http://web.com",
        "PORT": "8081"
      }
    },
    {
      "name": "web.2",
      "max_memory_restart": "1024M",
      "log_date_format": "YYYY-MM-DD HH:mm:ss SSS",
      "script": "/var/www/web/bundle/main.js",
      "out_file": "/var/log/web/app.2.log",
      "error_file": "/var/log/web/err.2.log",
      "port": "8082",
      "env": {
        "CDN_PREFIX": "//dbde4sd21oahf.cloudfront.net",
        "MONGO_URL": "mongodb://localhost:27017/web",
        "MONGO_OPLOG_URL": "mongodb://localhost:27017/local",
        "ROOT_URL": "http://web.com",
        "PORT": "8082"
      }
    },
    {
      "name": "web.3",
      "max_memory_restart": "1024M",
      "log_date_format": "YYYY-MM-DD HH:mm:ss SSS",
      "script": "/var/www/web/bundle/main.js",
      "out_file": "/var/log/web/app.3.log",
      "error_file": "/var/log/web/err.3.log",
      "port": "8083",
      "env": {
        "CDN_PREFIX": "//dbde4sd21oahf.cloudfront.net",
        "MONGO_URL": "mongodb://localhost:27017/web",
        "MONGO_OPLOG_URL": "mongodb://localhost:27017/local",
        "ROOT_URL": "http://web.com",
        "PORT": "8083"
      }
    }
  ]
}
```

pm2的当然还有一些其他的用法：

1、pm2远程部署

```bash
pm2 deploy ecosystem.json production setup
```

2、pm2 cluster启动

```bash
pm2 start app.js -i 0 --name "apps"
```

3、pm2 重启实例

```bash
pm2 reload <name>
```

4、pm2 命令行监测

```bash
pm2 monit
```

5、pm2 查看实例日志

```bash
pm2 logs 或 pm2 logs <name> 或 pm2 flush
```

6、pm2 开机启动

```bash
pm2 startup <ubuntu|centos|gentoo|systemd>
```

7、pm2 web方式监测

```bash
pm2 web
```

之后要考虑的就是服务器的监测以及如果给node做反向代理

比如：

> nginx或haproxy的部署，也可以使用nginx+passenger进行部署
>
> mongodb的部署
>
> mysql的部署
>
> redis的部署
>
> 还要对服务器进行压测
>
> apache ab
>
> wrk
>
> 以及性能调优和监控


