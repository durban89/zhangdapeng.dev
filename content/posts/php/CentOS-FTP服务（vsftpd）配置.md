---
title: "CentOS FTP服务（vsftpd）配置"
date: "2025-06-11 11:39:24"
slug: "centos-ftp-fu-wu-vsftpd-pei-zhi"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/11/CentOS-FTP服务（vsftpd）配置/"
  - "/2025/06/11/CentOS-FTP服务（vsftpd）配置.html"
  - "/CentOS-FTP服务（vsftpd）配置/"
  - "/CentOS-FTP服务（vsftpd）配置.html"
  - "/2025/06/11/centos-ftp-fu-wu-vsftpd-pei-zhi/"
  - "/2025/06/11/centos-ftp-fu-wu-vsftpd-pei-zhi.html"
  - "/centos-ftp-fu-wu-vsftpd-pei-zhi.html"
---
## [安装](#1)

一般在CentOS上都自动安装了vsftd，若没有安装则可以使用以下步骤进行安装

```shell
yum -y install vsftpd

touch /var/log/vsftpd.log # 创建vsftp的日志文件
```

在CentOS中，这样就可以完成了一个简单的匿名FTP的搭建。你可以通过访问ftp://yourip 来进行，不过这个FTP没有任何权限。

## [基于匿名的FTP架设](#2)

参考其他关于Vsftpd的CentOS FTP服务配置文章。

3.基于虚拟用户的FTP架设

所谓虚拟用户就是没有使用真实的帐户，只是通过某种手段达到映射帐户和设置权限的目的。

1）我们在/etc/vsftpd/vsftpd.conf中做如下CentOS FTP服务配置：

anonymous\_enable=NO 设定不允许匿名访问

chroot\_list\_enable=YES 使用户不能离开主目录

xferlog\_file=/var/log/vsftpd.log 设定vsftpd的服务日志保存路径。注意，该文件默认不存在。必须要手动touch出来

ascii\_upload\_enable=YES

ascii\_download\_enable=YES 设定支持ASCII模式的上传和下载功能。

local\_enable=YES 设定本地用户可以访问。注：如使用虚拟宿主用户，在该项目设定为NO的情况下所有虚拟用户将无法访问。

pam\_service\_name=vsftpd PAM认证文件名。PAM将根据/etc/pam.d/vsftpd进行认证

以下这些是关于Vsftpd虚拟用户支持的重要CentOS FTP服务配置项目。默认vsftpd.conf中不包含这些设定项目，需要自己手动添加CentOS FTP服务配置。

guest\_enable=YES 设定启用虚拟用户功能。

guest\_username=ftp 指定虚拟用户的宿主用户。-CentOS中已经有内置的ftp用户了

user\_config\_dir=/etc/vsftpd/vuser\_conf 设定虚拟用户个人vsftp的CentOS FTP服务文件存放路径。存放虚拟用户个性的CentOS FTP服务文件(配置文件名=虚拟用户名)

2）创建chroot list，将用户ftp加入其中：

```sh
touch /etc/vsftpd/chroot_list

echo ftp >> /etc/vsftpd/chroot_list
```

3）进行认证：

首先，安装Berkeley DB工具，很多人找不到db\_load的问题就是没有安装这个包。

```sh
yum install db4 db4-utils
```

然后，创建用户密码文本/etc/vsftpd/vuser\_passwd.txt ，注意奇行是用户名，偶行是密码

ftpuser1  
ftppass1  
ftpuser2  
ftppass2

接着，生成虚拟用户认证的db文件

```sh
db_load -T -t hash -f /etc/vsftpd/vuser_passwd.txt /etc/vsftpd/vuser_passwd.db
```

随后，编辑认证文件/etc/pam.d/vsftpd，全部注释掉原来语句  
再增加以下两句

```sh
auth required pam_userdb.so db=/etc/vsftpd/vuser_passwd
account required pam_userdb.so db=/etc/vsftpd/vuser_passwd
```

最后，创建虚拟用户个性CentOS FTP服务文件

```sh
mkdir /etc/vsftpd/vuser_conf/
vi /etc/vsftpd/vuser_conf/ftpuser1
```

内容如下：

```sh
local_root=/opt/var/ftp1 虚拟用户的根目录(根据实际修改)
write_enable=YES 可写
anon_umask=022 掩码
anon_world_readable_only=NO
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
```

## [启动vsftp服务器](#3)

```sh
mkdir /opt/var/ftp/ftpuser1
chmod 777 /opt/var/ftp/ftpuser1
service vsftpd start
```

## [常见错误：](#1)

### [553 Could not create file](#1-1)

一般都是SELinux的问题，设置SELinux的一个值，重启服务器即可。

```sh
setsebool -P ftpd_disable_trans 1
service vsftpd restart
```

### [500 OOPS: bad bool value in config file for: write\_enable](#1-2)

注意你的CentOS FTP服务文件中保证每一行最后没有任何空格，一般出错就是在多余的空格上。  
更改端口号：listen\_port=端口号 （需要自己添加）  
欢迎信息：ftpd\_banner=欢迎信息  
\====================================================================  
权限问题：  
当virtual\_use\_local\_privs=YES时，虚拟用户和本地用户有相同的权限；  
当virtual\_use\_local\_privs=NO时，虚拟用户和匿名用户有相同的权限，默认是NO。  
当virtual\_use\_local\_privs=YES，write\_enable=YES时，虚拟用户具有写权限（上传、下载、删除、重命名）。  
当virtual\_use\_local\_privs=NO，write\_enable=YES，anon\_world\_readable\_only=YES，  
anon\_upload\_enable=YES时，虚拟用户不能浏览目录，只能上传文件，无其他权限。  
当virtual\_use\_local\_privs=NO，write\_enable=YES，anon\_world\_readable\_only=NO，  
anon\_upload\_enable=NO时，虚拟用户只能下载文件，无其他权限。  
当virtual\_use\_local\_privs=NO，write\_enable=YES，anon\_world\_readable\_only=NO，  
anon\_upload\_enable=YES时，虚拟用户只能上传和下载文件，无其他权限。  
当virtual\_use\_local\_privs=NO，write\_enable=YES，anon\_world\_readable\_only=NO，  
anon\_mkdir\_write\_enable=YES时，虚拟用户只能下载文件和创建文件夹，无其他权限。  
当virtual\_use\_local\_privs=NO，write\_enable=YES，anon\_world\_readable\_only=NO，  
anon\_other\_write\_enable=YES时，虚拟用户只能下载、删除和重命名文件，无其他权限。  
一些RadHat版本是默认打开SeLinux的。这个东西有加强安全性的同时很讨厌，比如让配置好的vsftpd无法正常登录。

```sh
#setsebool -P ftpd_disable_trans 1
```

重启FTP服务~  
**IP限制的方法**

vsftpd中的配置需要 tcp\_wrappers=YES

/etc/hosts.allow 中加入允许的IP

```sh
vsftpd : IP1 IP2 : allow
```

/etc/hosts.deny 中屏蔽所有IP

```sh
vsftpd : ALL : deny
```

重启服务 `service xinetd restart` （此服务应该开机启动！）

来源：http://blog.sina.com.cn/s/blog\_50e52c230100l9sx.html
