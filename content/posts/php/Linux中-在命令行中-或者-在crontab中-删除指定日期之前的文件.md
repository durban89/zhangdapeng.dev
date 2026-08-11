---
title: "Linux中 在命令行中 或者 在crontab中 删除指定日期之前的文件"
date: "2025-06-19 13:54:50"
slug: "linux-zhong-zai-ming-ling-xing-zhong-huo-zhe-zai-crontab-zhong-shan-chu-zhi-ding-ri-qi-zhi-qian-de-wen-jian"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/19/Linux中-在命令行中-或者-在crontab中-删除指定日期之前的文件/"
  - "/2025/06/19/Linux中-在命令行中-或者-在crontab中-删除指定日期之前的文件.html"
  - "/Linux中-在命令行中-或者-在crontab中-删除指定日期之前的文件/"
  - "/Linux中-在命令行中-或者-在crontab中-删除指定日期之前的文件.html"
  - "/2025/06/19/linux-zhong-zai-ming-ling-xing-zhong-huo-zhe-zai-crontab-zhong-shan-chu-zhi-ding-ri-qi-/"
  - "/2025/06/19/linux-zhong-zai-ming-ling-xing-zhong-huo-zhe-zai-crontab-zhong-shan-chu-zhi-ding-ri.html"
  - "/linux-zhong-zai-ming-ling-xing-zhong-huo-zhe-zai-crontab-zhong-shan-chu-zhi-ding-ri-qi-zhi-qia.html"
---
前面一篇文章说的，主要是讲解了一些关于find命令的参数的信息，这里说下如果去使用，先看看我在别处引用的说法

> 要删除系统中就的备份文件，就需要使用命令了：  
>   
> #find /tmp -mtime +30 -type f -name \*.sh[ab] -exec rm -f {} \;  
>   
> 假如在一个目录中保留最近30天的文件，30天前的文件自动删除  
>   
> #find /tmp -mtime +30 -type f -name \*.sh[ab] -exec rm -f {} \;  
>   
> /tmp --设置查找的目录;  
>   
> -mtime +30 --设置时间为30天前;
>
> -type f --设置查找的类型为文件;  
>   
> -name \*.sh[ab] --设置文件名称中包含sha或者shb;  
>   
> 　　-exec rm -f --查找完毕后执行删除操作;  
>   
> 　　提示：将此命令写入crontab后即可自动完成查找并删除的工作  
>   
> 　　另外的方法大同小异  
>   
> 　　#find . -mtime +30 -type f | xargs rm -rf  
>   
> 　　我的操作是：先ls -ltr 查看时间，没有太久的所以就用 -cmin n查找系统中最后N分钟被改变文件状态的文件。具体命令：$ find /home/oracle/test6 -cmin +20 -type f -name \*.xml -exec rm -f { } \;  
>   
> 　　另外的方法大同小异  
>   
> 　　#find . -mtime +30 -type f | xargs rm -rf  
>   
> 　　$find . -type f -cmin +10 -exec rm -rf \*.xml {} \;  
>   
> 　　find . type f -name "debug\*" -atime +3 -exec rm -f {} \;  
>   
> 　　首先cd进入目录：  
>   
> 　　find . -name "\*~" -exec rm {} \;  
>   
> 　　find . -ctime +n -exec -exec rm -vi {} \;  
>   
> 　　这里的+n是指多少天以前，比如：+7  
>   
> 　　find . -ctime +7 -exec -exec rm -vi {} \;  
>   
> 　　如果不想手动确认，把命令中的-vi改成-fv  
>   
> 　　请详查find命令。  
>   
> 　　使用find时要区分清楚atime,ctime,mtime的区别，一般都使用mtime来查找，因为在ls -al显示出来的就是mtime时间戳，可以使用： # find $PAHT -mtime +3 -ok rm {} \;  
>   
> 　　在交互模式下删除比较保险。  
>   
> 　　一、按照一定日期格式命名文件  
>   
> 　　1、按照一定的格式输出日期：  
>   
> 　　date +"%y%m%d"  
>   
> 　　格式说明：  
>   
> 　　% : 印出 %  
>   
> 　　%n : 下一行  
>   
> 　　%t : 跳格  
>   
> 　　%H : 小时(00-23)  
>   
> 　　%I : 小时(01-12)  
>   
> 　　%k : 小时(0-23)  
>   
> 　　%l : 小时(1-12)  
>   
> 　　%M : 分钟(00-59)  
>   
> 　　%p : 显示本地 AM 或 PM  
>   
> 　　%r : 直接显示时间 (12 小时制，格式为 hh:mm:ss [AP]M)  
>   
> 　　%s : 从 1970 年 1 月 1 日 00:00:00 UTC 到目前为止的秒数  
>   
> 　　%S : 秒(00-60)  
>   
> 　　%T : 直接显示时间 (24 小时制)  
>   
> 　　%X : 相当于 %H:%M:%S  
>   
> 　　%Z : 显示时区  
>   
> 　　日期方面 :  
>   
> 　　%a : 星期几 (Sun-Sat)  
>   
> 　　%A : 星期几 (Sunday-Saturday)  
>   
> 　　%b : 月份 (Jan-Dec)  
>   
> 　　%B : 月份 (January-December)  
>   
> 　　%c : 直接显示日期与时间  
>   
> 　　%d : 日 (01-31)  
>   
> 　　%D : 直接显示日期 (mm/dd/yy)  
>   
> 　　%h : 同 %b  
>   
> 　　%j : 一年中的第几天 (001-366)  
>   
> 　　%m : 月份 (01-12)  
>   
> 　　%U : 一年中的第几周 (00-53) (以 Sunday 为一周的第一天的情形)  
>   
> 　　%w : 一周中的第几天 (0-6)  
>   
> 　　%W : 一年中的第几周 (00-53) (以 Monday 为一周的第一天的情形)  
>   
> 　　%x : 直接显示日期 (mm/dd/yy)  
>   
> 　　%y : 年份的最后两位数字 (00.99)  
>   
> 　　%Y : 完整年份 (0000-9999)  
>   
> 　　2、命名带有日期的文件：filename`date +%y%m%d`,此处的"`"不是单引号。  
>   
> 　　二、以创建文件日期为界线删除文件  
>   
> 　　1、find命令简解  
>   
> 　　find pathname -options [-print -exec -ok …]  
>   
> 　　pathname: find命令所查找的目录路径。例如用。来表示当前目录，用/来表示系统根目录。  
>   
> 　　-print: find命令将匹配的文件输出到标准输出。  
>   
> 　　-exec: find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'command' { } \;,注意{ }和\;之间的空格。  
>   
> 　　-ok: 和-exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，都会给出提示，让用户来确定是否执行。  
>   
> 　　options:  
>   
> 　　-name  
>   
> 　　按照文件名查找文件。  
>   
> 　　-perm  
>   
> 　　按照文件权限来查找文件。  
>   
> 　　-prune  
>   
> 　　使用这一选项可以使find命令不在当前指定的目录中查找，如果同时使用-depth选项，那么-prune将被find命令忽略。  
>   
> 　　-user  
>   
> 　　按照文件属主来查找文件。  
>   
> 　　-group  
>   
> 　　按照文件所属的组来查找文件。  
>   
> 　　-mtime -n +n  
>   
> 　　按照文件的更改时间来查找文件， - n表示文件更改时间距现在n天以内，+ n表示文件更改时间距现在n天以前。find命令还有-atime和-ctime 选项，但它们都和-m time选项。  
>   
> 　　-nogroup  
>   
> 　　查找无有效所属组的文件，即该文件所属的组在/etc/groups中不存在。  
>   
> 　　-nouser  
>   
> 　　查找无有效属主的文件，即该文件的属主在/etc/passwd中不存在。  
>   
> 　　-newer file1 ! file2  
>   
> 　　查找更改时间比文件file1新但比文件file2旧的文件。  
>   
> 　　-type  
>   
> 　　查找某一类型的文件，诸如：  
>   
> 　　b - 块设备文件。  
>   
> 　　d - 目录。  
>   
> 　　c - 字符设备文件。  
>   
> 　　p - 管道文件。  
>   
> 　　l - 符号链接文件。  
>   
> 　　f - 普通文件。  
>   
> 　　-size n:[c] 查找文件长度为n块的文件，带有c时表示文件长度以字节计。  
>   
> 　　-depth:在查找文件时，首先查找当前目录中的文件，然后再在其子目录中查找。  
>   
> 　　-fstype:查找位于某一类型文件系统中的文件，这些文件系统类型通常可以在配置文件/etc/fstab中找到，该配置文件中包含了本系统中有关文件系统的信息。  
>   
> 　　-mount:在查找文件时不跨越文件系统mount点。  
>   
> 　　-follow:如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。  
>   
> 　　-cpio:对匹配的文件使用cpio命令，将这些文件备份到磁带设备中。  
>   
> 　　对于时间相关的参数，有以下补充：  
>   
> 　　-amin n  
>   
> 　　查找系统中最后N分钟访问的文件  
>   
> 　　-atime n  
>   
> 　　查找系统中最后n\*24小时访问的文件  
>   
> 　　-cmin n  
>   
> 　　查找系统中最后N分钟被改变文件状态的文件  
>   
> 　　-ctime n  
>   
> 　　查找系统中最后n\*24小时被改变文件状态的文件  
>   
> 　　-mmin n  
>   
> 　　查找系统中最后N分钟被改变文件数据的文件  
>   
> 　　-mtime n  
>   
> 　　查找系统中最后n\*24小时被改变文件数据的文件  
>   
> 　　2、删除固定日期以前的文件  
>   
> 　　find logs -type f -mtime +5 -exec rm { } \;
