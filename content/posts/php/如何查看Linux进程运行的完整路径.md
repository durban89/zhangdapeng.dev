---
title: "如何查看Linux进程运行的完整路径"
date: "2025-07-15 09:52:19"
slug: "ru-he-cha-kan-linux-jin-cheng-yun-xing-de-wan-zheng-lu-jing"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/15/如何查看Linux进程运行的完整路径/"
  - "/2025/07/15/如何查看Linux进程运行的完整路径.html"
  - "/如何查看Linux进程运行的完整路径/"
  - "/如何查看Linux进程运行的完整路径.html"
  - "/2025/07/15/ru-he-cha-kan-linux-jin-cheng-yun-xing-de-wan-zheng-lu-jing/"
  - "/2025/07/15/ru-he-cha-kan-linux-jin-cheng-yun-xing-de-wan-zheng-lu-jing.html"
  - "/ru-he-cha-kan-linux-jin-cheng-yun-xing-de-wan-zheng-lu-jing.html"
---
日常工作中查看进程的命令有ps和top，但是只能查看到相对路径，如果想看到详细的信息，如绝对路径等是比较困难的

不过可以通过如下的方法来查看进程的详细信息

Linux在启动一个进程的时候，系统会在`/proc`目录下面创建一个以`PID`命名的文件夹

比如以nginx为例

```bash
$ ps -ef | grep nginx
root      3882  3865  0  2020 pts/0    00:00:00 nginx: master process /usr/bin/openresty -g daemon off;
nobody    3969  3882  0  2020 pts/0    00:00:03 nginx: worker process
nobody    3970  3882  0  2020 pts/0    00:00:05 nginx: worker process
nobody    3971  3882  0  2020 pts/0    00:00:10 nginx: worker process
nobody    3972  3882  0  2020 pts/0    00:00:57 nginx: worker process
```

我们拿`PID 3882`查看下

```bash
$ ls /proc/3882
attr       cgroup      comm             cwd      fd       io        map_files  mountinfo   net        oom_adj        pagemap      root       sessionid  stack  status   timers
autogroup  clear_refs  coredump_filter  environ  fdinfo   limits    maps       mounts      ns         oom_score      personality  sched      setgroups  stat   syscall  uid_map
auxv       cmdline     cpuset           exe      gid_map  loginuid  mem        mountstats  numa_maps  oom_score_adj  projid_map   schedstat  smaps      statm  task     wchan
```

其中包括一个名为exe的文件，这个文件即记录了绝对路径，通过`ll`或`ls -l`命令即可查看。

里面的文件的含义，如下

* cwd 符号链接的是进程运行目录；
* exe 符号连接就是执行程序的绝对路径；
* cmdline 就是程序运行时输入的命令行命令；
* environ 记录了进程运行时的环境变量；
* fd 目录下是进程打开或使用的文件的符号连接。

其他的请自行搜索
