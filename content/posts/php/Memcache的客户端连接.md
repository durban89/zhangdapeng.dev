---
title: "Memcache的客户端连接"
date: "2025-06-09 16:30:09"
slug: "memcache-de-ke-hu-duan-lian-jie"
categories: ["技术"]
tags: ["Memcache"]
aliases:
  - "/2025/06/09/Memcache的客户端连接/"
  - "/2025/06/09/Memcache的客户端连接.html"
  - "/Memcache的客户端连接/"
  - "/Memcache的客户端连接.html"
  - "/2025/06/09/memcache-de-ke-hu-duan-lian-jie/"
  - "/2025/06/09/memcache-de-ke-hu-duan-lian-jie.html"
  - "/memcache-de-ke-hu-duan-lian-jie.html"
---
许多语言都实现了连接memcached的客户端，其中以Perl、PHP为主。 仅仅memcached网站上列出的语言就有

- Perl
- PHP
- Python
- Ruby
- C#
- C/C++
- Lua

等等。

memcached客户端API：http://www.danga.com/memcached/apis.bml
这里介绍通过mixi正在使用的Perl库链接memcached的方法。

### [使用Cache::Memcached](#1)

Perl的memcached客户端有

- Cache::Memcached
- Cache::Memcached::Fast
- Cache::Memcached::libmemcached

等几个CPAN模块。这里介绍的Cache::Memcached是memcached的作者Brad Fitzpatric的作品， 应该算是memcached的客户端中应用最为广泛的模块了。

Cache::Memcached – search.cpan.org: http://search.cpan.org/dist/Cache-Memcached/

### [使用Cache::Memcached连接memcached](#2)
 

下面的源代码为通过Cache::Memcached连接刚才启动的memcached的例子。

```perl
#!/usr/bin/perl

use strict;
use warnings;
use Cache::Memcached;

my $key = "foo";
my $value = "bar";
my $expires = 3600; # 1 hour
my $memcached = Cache::Memcached->new({
    servers => ["127.0.0.1:11211"],
    compress_threshold => 10_000
});

$memcached->add($key, $value, $expires);
my $ret = $memcached->get($key);
print "$ret\n";
```

在这里，为Cache::Memcached指定了memcached服务器的IP地址和一个选项，以生成实例。 Cache::Memcached常用的选项如下所示。

选项 | 说明
|--|--
|servers | 用数组指定memcached服务器和端口
|compress_threshold |  数据压缩时使用的值
|namespace | 指定添加到键的前缀

另外，Cache::Memcached通过Storable模块可以将Perl的复杂数据序列化之后再保存， 因此散列、数组、对象等都可以直接保存到memcached中。

### [保存数据](#3)

向memcached保存数据的方法有

- add
- replace
- set

它们的使用方法都相同：

```perl
my $add = $memcached->add( '键', '值', '期限' );
my $replace = $memcached->replace( '键', '值', '期限' );
my $set = $memcached->set( '键', '值', '期限' );
my $val = $memcached->get('键');
my $val = $memcached->get_multi('键1', '键2', '键3', '键4', '键5');
```

一次取得多条数据时使用getmulti。getmulti可以非同步地同时取得多个键值， 其速度要比循环调用get快数十倍。

### [删除数据](#4)

删除数据使用delete方法，不过它有个独特的功能。

```perl
$memcached->delete('键', '阻塞时间(秒)');
```

删除第一个参数指定的键的数据。第二个参数指定一个时间值，可以禁止使用同样的键保存新数据。 此功能可以用于防止缓存数据的不完整。但是要注意，set函数忽视该阻塞，照常保存数据

### [增一和减一操作](#5)

可以将memcached上特定的键值作为计数器使用。

```perl
my $ret = $memcached->incr('键');
$memcached->add('键', 0) unless defined $ret;
```

增一和减一是原子操作，但未设置初始值时，不会自动赋成0。因此， 应当进行错误检查，必要时加入初始化操作。而且，服务器端也不会对 超过2 SUP(32)时的行为进行检查。
