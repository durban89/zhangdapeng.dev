---
title: "PHP如何连接sftp并下载文件"
date: "2025-07-09 09:59:24"
slug: "php-ru-he-lian-jie-sftp-bing-xia-zai-wen-jian"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/09/PHP如何连接sftp并下载文件/"
  - "/2025/07/09/PHP如何连接sftp并下载文件.html"
  - "/PHP如何连接sftp并下载文件/"
  - "/PHP如何连接sftp并下载文件.html"
  - "/2025/07/09/php-ru-he-lian-jie-sftp-bing-xia-zai-wen-jian/"
  - "/2025/07/09/php-ru-he-lian-jie-sftp-bing-xia-zai-wen-jian.html"
  - "/php-ru-he-lian-jie-sftp-bing-xia-zai-wen-jian.html"
---
首先我们要知道如何在命令行下连接，了解了之后就清楚大概的原理了  
命令行连接的方式如下

```bash
sftp -P port user@host
```

如果端口号默认是22的话就不需要端口号的参数，如下

```bash
sftp user@host
```

连接进去之后sftp支持大多数的linux命令，如ls、cd等，但是注意并不是所有的命令都支持，毕竟这是个文件传输的功能，没有太多复杂的命令  
上面了解之后我们看下PHP中如何链接

## 连接sftp

```php
$conf = [
    'channelId' => '',
    'host' => '',
    'port' => '',
    'user' => '',
    'password' => ''
];
$conn = ssh2_connect($conf['host'], $conf['port']);

if (!ssh2_auth_password($conn, $conf['user'], $conf['password'])) {
    var_dump('ftps 连接失败');
}
```

## 获取远程文件

第一步没有问题，说明我们已经进去了sftp里面，然后就可以进行文件下载

设置要获取的远程文件

```php
$remotFile = '/file/xxx/xxx/xxx.txt';
```

配置本地存储文件的路径

```php
$localPath = '/storage/data';

// 创建文件夹
if (!is_dir($localPath)) {
    $dir = mkdir($localPath, 0777, true);
    if (!$dir) {
        return false;
    }
}
```

设置本地要存储的文件

```php
// 如果文件已存在就覆盖
$localFile = 'xxxxx.txt';

$localRealFile = $localPath . '/' . $localFile;

// 如果文件存在则删除，当然这里也可以根据需求进行修改
if (is_file($localRealFile)) {
    unlink($localRealFile);
}
```

最后拉取文件并写到本地

```php
$sftp = ssh2_sftp($conn);

$resource = "ssh2.sftp://{$sftp}" . $remotFile;

//远程文件 拷贝到本地
copy($resource, $localRealFile);
```
