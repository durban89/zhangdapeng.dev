---
title: "Ubuntu12.04 下SVN安装和配置"
date: "2025-06-24 15:04:45"
slug: "ubuntu1204-xia-svn-an-zhuang-he-pei-zhi"
categories: ["技术"]
tags: ["Ubuntu", "Linux", "SVN"]
aliases:
  - "/2025/06/24/Ubuntu12.04-下SVN安装和配置/"
  - "/2025/06/24/Ubuntu12.04-下SVN安装和配置.html"
  - "/Ubuntu12.04-下SVN安装和配置/"
  - "/Ubuntu12.04-下SVN安装和配置.html"
  - "/2025/06/24/Ubuntu12-04-下SVN安装和配置/"
  - "/2025/06/24/Ubuntu12-04-下SVN安装和配置.html"
  - "/2025/06/24/ubuntu1204-xia-svn-an-zhuang-he-pei-zhi/"
  - "/2025/06/24/ubuntu1204-xia-svn-an-zhuang-he-pei-zhi.html"
  - "/ubuntu1204-xia-svn-an-zhuang-he-pei-zhi.html"
---
### [Ubuntu12.04下SVN安装](#1)

1.安装包

```bash
$ sudo apt-get install subversion
```

2.创建项目目录

```bash
$ sudo mkdir /var/svnroot
$ cd /var/svnroot
$ sudo mkdir mypro
```

3.创建svn文件仓库

```bash
$ sudo svnadmin create /var/svnroot/mypro
```

4.导入项目到svn文件仓库 (可有可无)

```bash
$ sudo svn import -m "" 你的文件夹路径 file://var/svnroot/mypro
```

5.访问权限设置

修改 /var/svnroot/mypro/conf目录下：

svnserve.conf 、passwd 个文件,行最前端不允许有空格

编辑svnserve.conf文件,把如下面行取消注释，并需要顶格

```bash
anon-access = read
auth-access = write
password-db = passwd
```

编辑passwd  如下:

```bash
[users] 
andy = andy
```

6. 开启svnserve,以SVN根目录开启：

```bash
$ svnserve -d -r /var/svnroot
```

7.检查是否正常启动

```bash
$ netstat -ntlp
```

可以看到有一个端口为3690的地址，表示启动成功

（如果使用Apache连接，则跳过下步）

8.局域网访问，checkout出来SVN库的文件

```bash
svn checkout svn://svnIp地址/mypro
```

或者简写为：

```bash
svn co svn://svnIp地址/mypro
```

### [在Ubuntu12.04下使用Apache配置Subversion](#2)

1.安装必要软件

```bash
$ sudo apt-get install subversion libapache2-svn apache2
```

2.修改apache配置文件/etc/apache2/mods-available/dav\_svn.conf

```ini
<Location /var/svnroot/mypro>
DAV svn
SVNPath /var/svnroot/mypro
AuthType Basic
AuthName "myproject subversion repository"
AuthUserFile /etc/subversion/passwd
#<LimitExcept GET PROPFIND OPTIONS REPORT>
Require valid-user
#</LimitExcept>
</Location>
```

 如果需要用户每次登录时都进行用户密码验证，请将

<LimitExcept GET PROPFIND OPTIONS REPORT>与</LimitExcept>两行注释掉。

当您添加了上面的内容，您必须重新起动 Apache 2 Web 服务器，请输入下面的命令：

```bash
$ sudo /etc/init.d/apache2 restart
```

3.创建 /etc/subversion/passwd 文件，该文件包含了用户授权的详细信息

```bash
$ sudo htpasswd -c /etc/subversion/passwd user_name
```

它会提示您输入密码，当您输入了密码，该用户就建立了。“-c”选项表示创建新的/etc/subversion/passwd文件，所以user\_name所指的用户将是文件中唯一的用户。如果要添加其他用户，则去掉“-c”选项即可：

```bash
$ sudo htpasswd /etc/subversion/passwd other_user_name
```

4.您可以通过下面的命令来访问文件仓库：

```bash
$ svn co http://hostname/svn/myproject myproject --username user_name
```

或者通过浏览器：http://hostname/svn/myproject

### [Ubuntu12.04 SVN命令大全](#3)

1、将文件checkout到本地目录 svn checkout path（path 是服务器上的目录）

例如：

```bash
$ svn checkout svn://192.168.1.1/pro
```

简写：

```bash
$ svn co svn://192.168.1.1/pro
```

2、往版本库中添加新的文件

```bash
$ svnadd file
$ svn add test.php#(添加test.php)
$ svn add *.php#(添加当前目录下所有的php文件)
```

3、将改动的文件提交到版本库

```bash
$ svn commit -m "LogMessage" [-N] [--no-unlock] PATH(如果选择了保持锁,就使用–no- unlock开关)
```

例如：

```bash
$ svn commit -m 'add test file for my test' test.php
```

简写：

```bash
$ svn ci
```

4、更新到某个版本

```bash
$ svn update -rm path
```

例如：$ svn update如果后面没有目录，默认将当前目录以及子目录下的所有文件都更新到最新版本。

```bash
$ svn update -r 200 test.php#(将版本库中的文件test.php还原到版本200)
$ svn update test.php#(更新，于版本库同步。如果在提交的时候提示过期的话，是因为冲突，需要先update，修改文 件，然后清除$ svn resolved，最后再提交commit) 简写：svn up
```

5、删除文件

```bash
$ svn delete path -m 'delete test fle'
```

例如：

```bash
$ svn delete test.php
```

然后再

```bash
$ svn ci -m 'delete test file'
```

简写：

```bash
svn (del, remove, rm)
```

6、比较差异

```bash
$ svn diff path#(将修改的文件与基础版本比较)
```

例如：

```bash
$ svn diff test.php
$ svn diff -r m:n path#(对版本m和版本n比较差异)
```

例如：

```bash
svn diff -r 200:201 test.php
```

简写：

```bash
svn di
```

 7、查看文件或者目录状态

```bash
1）svn status path#（目录下的文件和子目录的状态，正常状态不显示）
```

 【?：不在svn的控制中；M：内容被修改；C：发生冲突；A：预定加入到版本库；K：被锁定】

```bash
 2）svn status -v path(显示 文件和子目录状态)
```

 第一列保持相同，第二列显示工作版本号，第三和第四列显示最后一次修改的版本号和修改人。

***注：svn status、svn diff和 svn revert这三条命令在没有网络的情况下也可以执行的，原因是svn在本地的.svn中保留了本地版本的原始拷贝。***

简写：

```bash
svn st
```

8、解决冲突

```bash
$ svn resolved# 移除工作副本的目录或文件的“冲突”状态。
```

用法: $ resolved PATH…

注意: 本子命令不会依语法来解决冲突或是移除冲突标记；它只是移除冲突的

相关文件，然后让 PATH 可以再次提交。

### [同步更新 [勾子]](#4)

同步程序思路：用户提交程序到SVN，SVN触发hooks,按不同的hooks进行处理，这里用到的是post-commit，利用post-commit到代码检出到SVN服务器的本地硬盘目录，再通过rsync同步到远程的WEB服务器上。

知识点：

1、SVN的hooks

- start-commit 提交前触发事务

- pre-commit 提交完成前触发事务

- post-commit 提交完成时触发事务

- pre-revprop-change 版本属性修改前触发事务

- post-revprop-change 版本属性修改后触发事务

通过上面这些名称编写的脚本就就可以实现多种功能了，相当强大。

2、同步命令rsync的具体参数使用

3、具有几个语言的编程能力bash python perl都可以实现

post-commit脚本

编辑文件：sudo vim /var/svnroot/mypro/hooks/post-commit

注意：编辑完成post-commit后，执行：$ sudo chmod 755 post-commit

内容：

```bash
#!/bin/sh 
export LANG=zh_CN.UTF-8 
sudo /usr/bin/svn update /var/www/myblog --username xxxxxx --password xxxxxx
```

或更加复杂的同步更新

```bash
#Set variable 
SVN=/usr/bin/svn 
WEB=/home/test_nokia/ 
RSYNC=/usr/bin/rsync 
LOG=/tmp/rsync_test_nokia.log 
WEBIP="192.168.0.23" 
export LANG=en_US.UTF-8 
  
#update the code from the SVN 
$SVN update $WEB --username user --password  password 
#If the previous command completed successfully, to continue the following 
if [ $? == 0 ] 
then 
    echo ""     >> $LOG 
    echo `date` >> $LOG 
    echo "##############################" >> $LOG 
    chown -R nobody:nobody /home/test_nokia/ 
    #Synchronization code from the SVN server to the WEB server, notes:by the key 
    $RSYNC -vaztpH  --timeout=90   --exclude-from=/home/svn/exclude.list $WEB root@$WEBIP:/www/ >> $LOG 
fi
```

以上是具体的post-commit程序

注意事项：

*1、一定要定义变量，主要是用过的命令的路径。因为SVN的考虑的安全问题，没有调用系统变量，如果手动执行是没有问题，但SVN自动执行就会无法执行了。*

*2、SVN update 之前一定要先手动checkout一份出来，还有这里一定要添加用户和密码如果只是手动一样会更新，但自动一样的不行。*

*3、加上了对前一个命令的判断，如果update的时候出了问题，程序没有退出的话还会继续同步代码到WEB服务器上，这样会造成代码有问题*

*4、记得要设置所属用户，因为rsync可以同步文件属性，而且我们的WEB服务器一般都不是root用户，用户不正确会造成WEB程序无法正常工作。*

*5、建议最好记录日志，出错的时候可以很快的排错*

*6、最后最关键的数据同步，rsync的相关参数一定要清楚，这个就不说了。注意几个场景：*

*这里的环境是SVN服务器与WEB服务器是分开的*

把SVN服务器定义为源服务器 WEB服务器为目的服务器

***场景一、***如果目的WEB服务器为综合的混杂的，像只有一个WEB静态资源，用户提交的，自动生成的都在WEB的一个目录下，建议不要用–delete这个参数

上面这个程序就是这样，实现的是源服务器到目的服务器的更新和添加，而没有删除操作，WEB服务器的内容会多于源SVN的服务器的

***场景二、***实现镜像，即目的WEB服务器与源SVN服务器一样的数据，SVN上任何变化WEB上一样的变化，就需要–delete参数

***场景三、***不需要同步某些子目录，可能有些目录是缓存的临时垃圾目录，或者是专用的图片目录（而不是样式或者排版的）要用exclude这个参数

注意：这个参数的使用不用写绝对路径，只要目录名称就行 aa代表文件 aa/ 代表目录 ，缺点就是如果有多个子目录都是一样的名称那么这些名称就都不会被同步

建议用–exclude-from=/home/svn/exclude.list 用文件的形式可以方便的添加和删除

exclude.list

.svn/

images/

利用SVN的钩子还可以写出很多的程序来控制SVN 如代码提交前查看是否有写日志，是否有tab，有将换成空格，是否有不允许上传的文件，是否有超过限制大小的文件等等。


