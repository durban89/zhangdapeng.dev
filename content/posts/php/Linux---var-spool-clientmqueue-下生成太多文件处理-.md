---
title: "Linux  “/var/spool/clientmqueue 下生成太多文件处理”"
date: "2025-06-13 14:36:30"
slug: "linux-varspoolclientmqueue-xia-sheng-cheng-tai-duo-wen-jian-chu-li"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/13/Linux-“/var/spool/clientmqueue-下生成太多文件处理”/"
  - "/2025/06/13/Linux-“/var/spool/clientmqueue-下生成太多文件处理”.html"
  - "/Linux-“/var/spool/clientmqueue-下生成太多文件处理”/"
  - "/Linux-“/var/spool/clientmqueue-下生成太多文件处理”.html"
  - "/2025/06/13/Linux-var-spool-clientmqueue-下生成太多文件处理/"
  - "/2025/06/13/Linux-var-spool-clientmqueue-下生成太多文件处理.html"
  - "/2025/06/13/linux-varspoolclientmqueue-xia-sheng-cheng-tai-duo-wen-jian-chu-li/"
  - "/2025/06/13/linux-varspoolclientmqueue-xia-sheng-cheng-tai-duo-wen-jian-chu-li.html"
  - "/linux-varspoolclientmqueue-xia-sheng-cheng-tai-duo-wen-jian-chu-li.html"
---
最近服务器空间总是越来越小，找不到原因，其中有一项是这样的

```bash
114648472	/var/spool/clientmqueue
```

始终不知道这个是什么文件，经过搜索，是一个与cron有关的文件

这篇文章是这样的解决方案也给了，贴到下面

---

一，问题现象:  
linux操作系统中的`/var/spool/clientmqueue/`目录下存在大量文件。  
原因分析：系统中有用户开启了cron，而cron中执行的程序有输出内容，输出内容会以邮件形式发给cron的用户，而sendmail没有启动所以就产生了这些文件；  
解决办法: 1、 将crontab里面的命令后面加上`> /dev/null 2>&1  `

二，知识点：  

- `2>`：重定向错误。  
- `2>&1`：把错误重定向到输出要送到的地方。即把上述命令的执行结果重定向到/dev/null，即抛弃，同时，把产生的错误也抛弃。  

三，具体代码： 

（1）、`# crontab -u cvsroot -l ` 
```bash 
01 01 * * * /opt/bak/backup  
01 02 * * * /opt/bak/backup2  
```

（2）、`# vi /opt/bak/backup  `
```bash 
#!/bin/sh  
cd /  
getfacl -R repository > /opt/bak/backup.acl  
```

（3）、`# vi /opt/bak/backup2 `
```bash 
#!/bin/sh  
week=`date +%w`  
tar zcvfp /opt/bak/cvs$week/cvs.tar.gz /repository >/dev/null 2>&1  
```

四，清除/var/spool/clientmqueue/目录下的文件：  

```bash 
# cd /var/spool/clientmqueue  
# rm -rf \*  
```

如果文件太多，占用空间太大，用上面命令删除慢的话，就执行下面的命令：  

```bash 
# cd /var/spool/clientmqueue  
# ls | xargs rm -f
```

---

话说删除这个大文件还是有说法的，接着下面看

rm 有最大一次刪除的數量，所以當一個目錄裡有太多的檔案或目錄時，就會出現錯誤，小弟試過應該是在二萬以下，而使用 `find ./ | xargs rm -rf` 的目的是先使用 find 列出檔案，再導向到 xargs，xargs 再喂給 rm，在這裡，xargs 會分批依照 rm 的最大數量餵給 rm，然後就可以順利刪除檔案了  
。

还举了一个实例

mk-file.sh的代码如下：

```bash
#!/bin/bash
for ((i=0;i<20000;i++))
do
	echo "This file id is $i." > test-file-${i};
done
```

(這個 shell script 會有目錄下產生 20000 個檔案。)  
接下來來做個小小測試：

```bash
root # mkfile.sh
```

會產生 20000 個小檔案，名稱為 test-file-{1~19999}  
直接使用 rm 去刪除：

```bash
root # rm -rf test-file-*
```

-bash: /bin/rm: Argument list too long (會回應引數過長的訊息)  
该搭配 find 來刪除

```bash
root # find ./ -iname 'test-file-*' | xargs rm -rf
```

這樣就順利被刪除了。
