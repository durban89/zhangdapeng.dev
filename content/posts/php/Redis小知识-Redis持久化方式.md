---
title: "Redis小知识 - Redis持久化方式"
date: "2025-07-11 11:14:46"
slug: "redis-xiao-zhi-shi-redis-chi-jiu-hua-fang-shi"
categories: ["技术"]
tags: ["Redis"]
aliases:
  - "/2025/07/11/Redis小知识-Redis持久化方式/"
  - "/2025/07/11/Redis小知识-Redis持久化方式.html"
  - "/Redis小知识-Redis持久化方式/"
  - "/Redis小知识-Redis持久化方式.html"
  - "/2025/07/11/redis-xiao-zhi-shi-redis-chi-jiu-hua-fang-shi/"
  - "/2025/07/11/redis-xiao-zhi-shi-redis-chi-jiu-hua-fang-shi.html"
  - "/redis-xiao-zhi-shi-redis-chi-jiu-hua-fang-shi.html"
---
redis持久化方式

### 第一种方式：快照

快照是默认的持久化方式。这种方式是就是将内存中数据以快照的方式写入到二进制文件中,默认的文件名为dump.rdb。

可以通过配置设置自动做快照持久化的方式。我们可以配置 redis在 n 秒内如果超过 m 个 key 被修改就自动做快照，下面是默认的快照保存配置：

* save 900 1 #900 秒内如果超过 1 个 key 被修改，则发起快照保存
* save 300 10 #300 秒内容如超过 10 个 key 被修改，则发起快照保存
* save 60 10000

**快照保存过程**

1. redis 调用 fork,现在有了子进程和父进程。
2. 父进程继续处理 client 请求，子进程负责将内存内容写入到临时文件。由于 os 的实时复制机制（ copy on write)父子进程会共享相同的物理页面，当父进程处理写请求时 os 会为父进程要修改的页面创建副本，而不是写共享的页面。所以子进程地址空间内的数据是 fork时刻整个数据库的一个快照。
3. 当子进程将快照写入临时文件完毕后，用临时文件替换原来的快照文件，然后子进程退出。client 也可以使用 save 或者 bgsave 命令通知 redis 做一次快照持久化。 save 操作是在主线程中保存快照的，由于 redis 是用一个主线程来处理所有 client 的请求，这种方式会阻塞所有client 请求。所以不推荐使用。另一点需要注意的是，每次快照持久化都是将内存数据完整写入到磁盘一次，并不是增量的只同步变更数据。如果数据量大的话，而且写操作比较多，必然会引起大量的磁盘 io 操作，可能会严重影响性能。

### 第一种方式：aof

由于快照方式是在一定间隔时间做一次的，所以如果 redis 意外 down 掉的话，就会丢失最后一次快照后的所有修改。如果应用要求不能丢失任何修改的话，可以采用 aof 持久化方式。  
aof 比快照方式有更好的持久化性，是由于在使用 aof 持久化方式时,redis 会将每一个收到的写命令都通过 write 函数追加到文件中(默认是 appendonly.aof)。当 redis 重启时会通过重新执行文件中保存的写命令来在内存中重建整个数据库的内容。  
当然由于 os 会在内核中缓存 write 做的修改，所以可能不是立即写到磁盘上。这样 aof 方式的持久化也还是有可能会丢失部分修改。不过我们可以通过配置文件告诉 redis 我们想要通过 fsync 函数强制 os 写入到磁盘的时机。有三种方式如下（默认是：每秒 fsync 一次）

* appendonly yes // 启用 aof 持久化方式
* appendfsync always // 收到写命令就立即写入磁盘，最慢，但是保证完全的持久化
* appendfsync everysec // 每秒钟写入磁盘一次，在性能和持久化方面做了很好的折中
* appendfsync no // 完全依赖 os，性能最好,持久化没保证

aof 的方式也同时带来了另一个问题。持久化文件会变的越来越大。例如我们调用 incr test命令 100 次，文件中必须保存全部的 100 条命令，其实有 99 条都是多余的。因为要恢复数据库的状态其实文件中保存一条 set test 100 就够了。为了压缩 aof 的持久化文件。 redis 提供了 bgrewriteaof 命令。收到此命令 redis 将使用与快照类似的方式将内存中的数据以命令的方式保存到临时文件中，最后替换原来的文件。
