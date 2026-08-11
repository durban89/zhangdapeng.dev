---
title: "Redis 3 版本 集群配置"
date: "2025-07-03 11:08:07"
slug: "redis-3-ban-ben-ji-qun-pei-zhi"
categories: ["技术"]
tags: ["Redis"]
aliases:
  - "/2025/07/03/Redis-3-版本-集群配置/"
  - "/2025/07/03/Redis-3-版本-集群配置.html"
  - "/Redis-3-版本-集群配置/"
  - "/Redis-3-版本-集群配置.html"
  - "/2025/07/03/redis-3-ban-ben-ji-qun-pei-zhi/"
  - "/2025/07/03/redis-3-ban-ben-ji-qun-pei-zhi.html"
  - "/redis-3-ban-ben-ji-qun-pei-zhi.html"
---
最近项目需要，需要在服务器上做下redis的集群配置。

这里说下我自己的经验，应该是redis自3版本以后才支持redis，以前的版本也有集群，但是不是真正意义上的集群，从配置文件上就能够分别出来，3以前的版本是没有cluster的相关配置项的，从3版本以后才开始支持的。这个导致我一直以为3以前的版本也是支持的，折腾了好久，不过2版本可以通过master/slave的方式搭建类似集群的功能。

所以，如果你是想使用redis的集群功能，首先还是把自己的redis升级为至少是3版本的吧。

我这里记录的是redis 3.2.1版本的。

整个的配置流程事实上是可以直接使用redis自己提供的create-cluster进行创建，这个工具整个进行管理起来比较方便快捷，就是在配置上都不够便捷。

首先就是下载redis，下载地址：<http://download.redis.io/releases/redis-3.2.1.tar.gz>

下载后解压到目录/usr/local/redis目录【这里不熟悉tar 命令的自行google】

进入到redis目录后执行

```bash
make
```

如果需要root权限的话，执行

```bash
sudo make
```

我这里因为有人已经在系统里面安装了redis,我有不想去打扰他的，我就自己干一个独立的好了，事实上也是互不干扰的。

如果是独立安装的话，可以接着执行

```bash
make install
```

或

```bash
sudo make install
```

如果跟我一样的话，上面的环节就可以省略了。

接下来，我按照我的情况来说。

进入到src目录下面，应该会有很多你熟悉的命令文件了。

```bash
╭─zhangdapeng@qeeniao4-HZ /usr/local/redis/src  
╰─➤  ls
adlist.c     bio.h      db.c           intset.c         multi.c       rand.h             redis-cli.o     sds.o           sparkline.c  util.h
adlist.h     bio.o      db.o           intset.h         multi.o       rand.o             redis-sentinel  sentinel.c      sparkline.h  util.o
adlist.o     bitops.c   debug.c        intset.o         networking.c  rdb.c              redis-server    sentinel.o      sparkline.o  valgrind.sup
ae.c         bitops.o   debug.o        latency.c        networking.o  rdb.h              redis-trib.rb   server.c        syncio.c     version.h
ae_epoll.c   blocked.c  dict.c         latency.h        notify.c      rdb.o              release.c       server.h        syncio.o     ziplist.c
ae_evport.c  blocked.o  dict.h         latency.o        notify.o      redisassert.h      release.h       server.o        testhelp.h   ziplist.h
ae.h         cluster.c  dict.o         lzf_c.c          object.c      redis-benchmark    release.o       setproctitle.c  t_hash.c     ziplist.o
ae_kqueue.c  cluster.h  endianconv.c   lzf_c.o          object.o      redis-benchmark.c  replication.c   setproctitle.o  t_hash.o     zipmap.c
ae.o         cluster.o  endianconv.h   lzf_d.c          pqsort.c      redis-benchmark.o  replication.o   sha1.c          t_list.c     zipmap.h
ae_select.c  config.c   endianconv.o   lzf_d.o          pqsort.h      redis-check-aof    rio.c           sha1.h          t_list.o     zipmap.o
anet.c       config.h   fmacros.h      lzf.h            pqsort.o      redis-check-aof.c  rio.h           sha1.o          t_set.c      zmalloc.c
anet.h       config.o   geo.c          lzfP.h           pubsub.c      redis-check-aof.o  rio.o           slowlog.c       t_set.o      zmalloc.h
anet.o       crc16.c    geo.h          Makefile         pubsub.o      redis-check-rdb    scripting.c     slowlog.h       t_string.c   zmalloc.o
aof.c        crc16.o    geo.o          Makefile.dep     quicklist.c   redis-check-rdb.c  scripting.o     slowlog.o       t_string.o
aof.o        crc64.c    help.h         memtest.c        quicklist.h   redis-check-rdb.o  sdsalloc.h      solarisfixes.h  t_zset.c
asciilogo.h  crc64.h    hyperloglog.c  memtest.o        quicklist.o   redis-cli          sds.c           sort.c          t_zset.o
bio.c        crc64.o    hyperloglog.o  mkreleasehdr.sh  rand.c        redis-cli.c        sds.h           sort.o          util.c
```

太多了，我们重点关注几个就好了，redis-cli,redis-server,redis-trib.rb.

接下来让我们创建配置文件吧。

进入/usr/local/etc目录，没有的话，就自己建立一个，或者根据自己的情况来也是可以的。

建立一个redis的目录，在redis目录下，从原有的redis.conf复制一份改为redis\_7001.conf,由于这里我们需要用到6个，所以我们一次建立了6个redis配置文件

```bash
-rw-r--r-- 1 root root 45K 7月   7 18:32 redis_7001.conf
-rw-r--r-- 1 root root 45K 7月   7 18:32 redis_7002.conf
-rw-r--r-- 1 root root 45K 7月   7 18:33 redis_7003.conf
-rw-r--r-- 1 root root 45K 7月   7 18:33 redis_7004.conf
-rw-r--r-- 1 root root 45K 7月   7 18:33 redis_7005.conf
-rw-r--r-- 1 root root 45K 7月   7 18:34 redis_7006.conf
```

这里我简单的列出需要修改的项

```bash
bind 114.xxx.xxx.xxx 127.0.0.1//这里是你要绑定的ip地址【这里有料，下面解说】
port 7001//端口号
daemonize yes//
pidfile /var/run/redis_7001.pid
logfile "/var/log/redis/redis_7001.log"
appendonly yes
appendfilename "appendonly.aof"
cluster-enabled yes
cluster-config-file nodes-7001.conf
cluster-node-timeout 15000
```

这里只是展示了redis\_7001.conf这个文件需要修改的地址，其他5个同样的，只是将7001换成对应的数字就好了。

配置完后，就可以启动喽。

回到redis/src目录，执行

```bash
./redis-server /usr/local/etc/redis/redis_7001.conf
./redis-server /usr/local/etc/redis/redis_7002.conf
./redis-server /usr/local/etc/redis/redis_7003.conf
./redis-server /usr/local/etc/redis/redis_7004.conf
./redis-server /usr/local/etc/redis/redis_7005.conf
./redis-server /usr/local/etc/redis/redis_7006.conf
```

查看是否已经启动了。

`ps -ef | grep redis`

如果看到如下的结果说明，已经启动成功了，如果有问题，说明还是需要检查一下配置文件。

```bash
root     17979     1  0 7月07 ?       00:00:16 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7001 [cluster]
root     17988     1  0 7月07 ?       00:00:16 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7002 [cluster]
root     17997     1  0 7月07 ?       00:00:17 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7003 [cluster]
root     18006     1  0 7月07 ?       00:00:15 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7004 [cluster]
root     18015     1  0 7月07 ?       00:00:16 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7005 [cluster]
root     18024     1  0 7月07 ?       00:00:15 ../../../redis/src/redis-server 114.xxx.xxx.xxx:7006 [cluster]
```

奇怪了，我这里为啥会显示我自己服务器的ip呢？【就是下面要讲的猛料】

redis是启动成功了，但是我们还要进行一次设置，就是集群的设置，还是在redis/src目录

```bash
./redis-trib.rb create --replicas 1 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 127.0.0.1:7006
```

命令的意义如下：

1. 给定 redis-trib.rb 程序的命令是 create ， 这表示我们希望创建一个新的集群。
2. 选项 --replicas 1 表示我们希望为集群中的每个主节点创建一个从节点。
3. 之后跟着的其他参数则是实例的地址列表， 我们希望程序使用这些地址所指示的实例来创建新集群。

简单来说， 以上命令的意思就是让 redis-trib 程序创建一个包含三个主节点和三个从节点的集群。

接着， redis-trib 会打印出一份预想中的配置给你看， 如果你觉得没问题的话， 就可以输入 yes ， redis-trib 就会将这份配置应用到集群当中：

```bash
>>> Creating cluster
Connecting to node 127.0.0.1:7000: OK
Connecting to node 127.0.0.1:7001: OK
Connecting to node 127.0.0.1:7002: OK
Connecting to node 127.0.0.1:7003: OK
Connecting to node 127.0.0.1:7004: OK
Connecting to node 127.0.0.1:7005: OK
>>> Performing hash slots allocation on 6 nodes...
Using 3 masters:
127.0.0.1:7000
127.0.0.1:7001
127.0.0.1:7002
Adding replica 127.0.0.1:7003 to 127.0.0.1:7000
Adding replica 127.0.0.1:7004 to 127.0.0.1:7001
Adding replica 127.0.0.1:7005 to 127.0.0.1:7002
M: 2774f156af482b4f76a5c0bda8ec561a8a1719c2 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
M: 2d03b862083ee1b1785dba5db2987739cf3a80eb 127.0.0.1:7001
   slots:5461-10922 (5462 slots) master
M: 0456869a2c2359c3e06e065a09de86df2e3135ac 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
S: 37b251500385929d5c54a005809377681b95ca90 127.0.0.1:7003
   replicates 2774f156af482b4f76a5c0bda8ec561a8a1719c2
S: e2e2e692c40fc34f700762d1fe3a8df94816a062 127.0.0.1:7004
   replicates 2d03b862083ee1b1785dba5db2987739cf3a80eb
S: 9923235f8f2b2587407350b1d8b887a7a59de8db 127.0.0.1:7005
   replicates 0456869a2c2359c3e06e065a09de86df2e3135ac
Can I set the above configuration? (type 'yes' to accept):
```

输入 yes 并按下回车确认之后， 集群就会将配置应用到各个节点， 并连接起（join）各个节点 —— 也即是， 让各个节点开始互相通讯

```bash
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join......
>>> Performing Cluster Check (using node 127.0.0.1:7000)
M: 2774f156af482b4f76a5c0bda8ec561a8a1719c2 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
M: 2d03b862083ee1b1785dba5db2987739cf3a80eb 127.0.0.1:7001
   slots:5461-10922 (5462 slots) master
M: 0456869a2c2359c3e06e065a09de86df2e3135ac 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
M: 37b251500385929d5c54a005809377681b95ca90 127.0.0.1:7003
   slots: (0 slots) master
   replicates 2774f156af482b4f76a5c0bda8ec561a8a1719c2
M: e2e2e692c40fc34f700762d1fe3a8df94816a062 127.0.0.1:7004
   slots: (0 slots) master
   replicates 2d03b862083ee1b1785dba5db2987739cf3a80eb
M: 9923235f8f2b2587407350b1d8b887a7a59de8db 127.0.0.1:7005
   slots: (0 slots) master
   replicates 0456869a2c2359c3e06e065a09de86df2e3135ac
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

一切都正常的话会输出

```bash
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

到这里就一切万事大吉了，如果还是需要其他的额外的帮助，可以到这里看看<http://www.cnblogs.com/gomysql/p/4395504.html>

【猛料解析】

```bash
bind 114.xxx.xxx.xxx 127.0.0.1
```

这里我为哈把地址写成这样呢？主要是是因为，第一个是可以远程了解，换个位置的话也是可以的，但是在远程了解的情况下会出现一个问题，就是在做转向的时候，会由于第一个ip地址的不同而不同，如果是127.0.0.1的话，那么在远程链接的时候就跳转到127.0.0.1这个ip上来了，同理换成其他地址的话，就会跳转到其他地址，自己可以实验一下，可以使用类似node的ioredis的这样库测试，或者直接命令行链接，会比较明显，就是因为这里，如果配置不好的话，后面使用第三方库连接的话，会一直连接不上。


