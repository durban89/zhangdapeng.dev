---
title: "PM2启动配置文件参数"
date: "2025-07-03 11:59:49"
slug: "pm2-qi-dong-pei-zhi-wen-jian-can-shu"
categories: ["技术"]
tags: ["PM2"]
aliases:
  - "/2025/07/03/PM2启动配置文件参数/"
  - "/2025/07/03/PM2启动配置文件参数.html"
  - "/PM2启动配置文件参数/"
  - "/PM2启动配置文件参数.html"
  - "/2025/07/03/pm2-qi-dong-pei-zhi-wen-jian-can-shu/"
  - "/2025/07/03/pm2-qi-dong-pei-zhi-wen-jian-can-shu.html"
  - "/pm2-qi-dong-pei-zhi-wen-jian-can-shu.html"
---
PM2启动配置文件参数比较全的一个。如下：

```json
{
  "name"             : "node-app",
  "cwd"              : "/srv/node-app/current",
  "args"             : ["--toto=heya coco", "-d", "1"],
  "script"           : "bin/app.js",
  "node_args"        : ["--harmony", " --max-stack-size=102400000"],
  "log_date_format"  : "YYYY-MM-DD HH:mm Z",
  "error_file"       : "/var/log/node-app/node-app.stderr.log",
  "out_file"         : "log/node-app.stdout.log",
  "pid_file"         : "pids/node-geo-api.pid",
  "instances"        : 6, //or 0 => 'max'
  "min_uptime"       : "200s", // 200 seconds, defaults to 1000
  "max_restarts"     : 10, // defaults to 15
  "max_memory_restart": "1M", // 1 megabytes, e.g.: "2G", "10M", "100K", 1024 the default unit is byte.
  "cron_restart"     : "1 0 * * *",
  "watch"            : false,
  "ignore_watch"      : ["[\\/\\\\]\\./", "node_modules"],
  "merge_logs"       : true,
  "exec_interpreter" : "node",
  "exec_mode"        : "fork",
  "autorestart"      : false, // enable/disable automatic restart when an app crashes or exits
  "vizion"           : false, // enable/disable vizion features (versioning control)
  // Default environment variables that will be injected in any environment and at any start
  "env": {
    "NODE_ENV": "production",
    "AWESOME_SERVICE_API_TOKEN": "xxx"
  }
  "env_*" : {
    "SPECIFIC_ENV" : true
  }
}
```

比较有用的参数:

cron_restart:定时启动，解决重启能解决的问题

max_memory_restart：解决内容不够用的问题，不过会有风险【数据丢失】


