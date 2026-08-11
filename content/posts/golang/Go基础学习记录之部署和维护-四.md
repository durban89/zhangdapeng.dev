---
title: "Go基础学习记录之部署和维护(四)"
date: "2025-08-04 18:07:26"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-si"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之部署和维护(四)/"
  - "/2025/08/04/Go基础学习记录之部署和维护(四).html"
  - "/Go基础学习记录之部署和维护(四)/"
  - "/Go基础学习记录之部署和维护(四).html"
  - "/2025/08/04/Go基础学习记录之部署和维护-四/"
  - "/2025/08/04/Go基础学习记录之部署和维护-四.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-si/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-si.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-si.html"
---
### 备份和恢复

今天分享下应用程序管理的另一个方面：生产服务器上的数据备份和恢复。 我们经常遇到生产服务器不像我们期望的那样运行的情况。 服务器网络中断，硬盘驱动器故障，操作系统崩溃和其他类似事件可能导致数据库不可用。 需要从这些类型的事件中恢复，导致出现了许多冷备用/热备用工具，这些工具可以帮助远程实现灾难恢复。 除了备份和恢复您可能正在使用的任何MySQL和Redis数据库之外，我们还将解释如何备份已部署的应用程序。

**应用备份**

在大多数群集环境中，不需要备份Web应用程序，因为它们实际上是来自本地开发环境或版本控制系统的代码副本。 但是，在许多情况下，我们需要备份由我们网站的用户提供的数据。 例如，当网站要求用户上传文件时，我们需要能够备份用户上传到我们网站的任何文件。 当前提供这种冗余的方法是利用所谓的云存储，其中用户文件和其他相关资源被持久存储到高度可用的服务器网络中。 如果我们的系统崩溃，只要用户数据持久存储到云端，我们至少可以确保不会丢失任何数据。

但是，我们没有将数据备份到云服务，或者云存储不是一种选择的情况呢？ 那么我们如何从我们的Web应用程序备份数据呢？ 在这里，我们描述了一个名为rsync的工具，它通常可以在类Unix系统上找到。 Rsync是一个可用于同步驻留在不同系统上的文件的工具，此功能的完美用例是保持我们的网站备份。

> 注意：Cwrsync是Windows环境的rsync实现

**Rsync安装**

您可以从其[官方网站](https://rsync.samba.org/can)上找到最新版本的rsync。 当然，因为rsync是非常有用的软件，所以许多Linux发行版默认都会安装它。

包安装：

```bash
# sudo apt-get install rsync ; Note: debian, ubuntu and other online installation methods ;
# yum install rsync ; Note: Fedora, Redhat, CentOS and other online installation methods ;
# rpm -ivh rsync ; Note: Fedora, Redhat, CentOS and other rpm package installation methods ;
```

对于其他Linux发行版，请使用适当的包管理方法进行安装。 或者，您可以从源代码自行构建它：

```bash
tar xvf rsync-xxx.tar.gz
cd rsync-xxx
./configure - prefix =/usr; make; make install
```

> 注意：如果要从源代码编译和安装rsync，则必须安装gcc编译器工具，例如job。

> 注意：在使用编译和安装的源包之前，必须安装gcc编译器工具，例如job

**Rsync配置**

可以从三个主要配置文件配置Rsync：rsyncd.conf（主要配置文件），rsyncd.secrets（保存密码）和rsyncd.motd（包含服务器信息）。

* 启动rsync守护程序服务器端：

  ```bash
  # /usr/bin/rsync --daemon --config=/etc/rsyncd.conf
  ```
* --daemon参数用于在服务器模式下运行rsync。 通过将其连接到rc.local文件，使其成为默认启动时设置：

  ```bash
  echo 'rsync --daemon' >> /etc/rc.d/rc.local
  ```

设置rsync用户名和密码，确保它仅由root拥有，以便本地未经授权的用户或漏洞利用者无权访问它。 如果未正确设置这些权限，rsync可能无法启动：

```bash
echo 'Your Username: Your Password' > /etc/rsyncd.secrets
chmod 600 /etc/rsyncd.secrets
```

* 客户端同步： 客户端可以使用以下命令同步服务器文件：

```bash
rsync -avzP --delete --password-file=rsyncd.secrets [email protected]::www /var/rsync/backup
```

让我们将其分解为几个关键点：

* -avzP是一些常见选项。 使用rsync --help来查看这些操作。
* --delete删除接收方的无关文件。 例如，如果在发送方删除文件，则下次两台机器同步时，接收方将自动删除相应的文件。
* --password-file指定用于访问rsync守护程序的密码文件。 在客户端，这通常是客户端/etc/rsyncd.secrets文件，在服务器端，它是/etc/rsyncd.secrets。 当使用像Cron这样的东西来自动化rsync时，您不需要手动输入密码。
* username指定与服务器端/etc/rsyncd.secrets密码一起使用的用户名
* 192.168.145.5是服务器的IP地址
* :: www（注意双冒号），指定直接通过TCP联系rsync守护进程，根据位于/etc/rsyncd.conf中的服务器端配置同步www模块。 如果仅使用单个冒号，则不直接联系rsync守护程序; 相反，远程shell程序（如ssh）用作传输。

为了定期同步文件，您可以设置一个crontab文件，该文件将根据需要经常运行rsync命令。 当然，用户可以根据保持某些目录或文件最新的重要程度来改变同步频率。

### MySQL备份

对于大多数Web应用程序，MySQL数据库仍然是主流的首选解决方案。 备份MySQL数据库的两种最常用方法是热备份和冷备份。 热备份通常与在主/从配置中设置的系统一起使用以备份实时数据（主/从同步模式通常用于分离数据库读/写操作，但也可用于备份实时数据）。 在线提供了大量信息，详细说明了实现此类方案的各种方法。 对于冷备份，传入数据不会像热备份那样实时备份。 而是定期执行数据备份。 这样，如果系统出现故障，仍然可以保证在一段时间之前数据的完整性。 例如，在系统故障导致数据丢失且主/从模型无法检索数据的情况下，冷备份可用于部分恢复。

shell脚本通常用于实现数据库的常规冷备份，在非本地模式下使用rsync执行同步任务。

以下是执行MySQL数据库的计划备份的备份脚本示例。 我们使用mysqldump程序，它允许我们将数据库导出到一个文件。

```bash
#!/bin/bash
# Configuration information; modify it as needed  
mysql_user="USER" #MySQL backup user
mysql_password="PASSWORD" # MySQL backup user's password
mysql_host="localhost"
mysql_port="3306"
mysql_charset="utf8" # MySQL encoding
backup_db_arr=("db1" "db2") # Name of the database to be backed up, separating multiple databases wih spaces ("DB1", "DB2" db3 ")
backup_location=/var/www/mysql # Backup data storage location; please do not end with a "/" and leave it at its default, for the program to automatically create a folder
expire_backup_delete="ON" # Whether to delete outdated backups or not
expire_days=3 # Set the expiration time of backups, in days (defaults to three days); this is only valid when the `expire_backup_delete` option is "ON"

# We do not need to modify the following initial settings below
backup_time=`date +%Y%m%d%H%M` # Define the backup time format 
backup_Ymd=`date +%Y-%m-%d` # Define the backup directory date time
backup_3ago=`date-d '3 days ago '+%Y-%m-%d` # 3 days before the date
backup_dir=$backup_location/$backup_Ymd # Full path to the backup folder
welcome_msg="Welcome to use MySQL backup tools!" # Greeting

# Determine whether to MySQL is running; if not, then abort the backup 
mysql_ps=`ps-ef | grep mysql | wc-l`
mysql_listen=`netstat-an | grep LISTEN | grep $mysql_port | wc-l`
if [[$mysql_ps==0]-o [$mysql_listen==0]]; then
  echo "ERROR: MySQL is not running! backup aborted!"
  exit
else
  echo $welcome_msg
fi

# Connect to the mysql database; if a connection cannot be made, abort the backup 
mysql-h $mysql_host-P $mysql_port-u $mysql_user-p $mysql_password << end
use mysql;
select host, user from user where user='root' and host='localhost';
exit
end

flag=`echo $?`
if [$flag!="0"]; then
  echo "ERROR: Can't connect mysql server! backup aborted!"
  exit
else
  echo "MySQL connect ok! Please wait......"
   # Determine whether a backup database is defined or not. If so, begin the backup; if not, then abort 
  if ["$backup_db_arr"!=""]; then
       # dbnames=$(cut-d ','-f1-5 $backup_database)
       # echo "arr is(${backup_db_arr [@]})"
      for dbname in ${backup_db_arr [@]}
      do
          echo "database $dbname backup start..."
          `mkdir -p $backup_dir`
          `mysqldump -h $mysql_host -P $mysql_port -u $mysql_user -p $mysql_password $dbname - default-character-set=$mysql_charset | gzip> $backup_dir/$dbname -$backup_time.sql.gz`
          flag=`echo $?`
          if [$flag=="0"]; then
              echo "database $dbname successfully backed up to $backup_dir/$dbname-$backup_time.sql.gz"
          else
              echo "database $dbname backup has failed!"
          fi

      done
  else
      echo "ERROR: No database to backup! backup aborted!"
      exit
  fi
   # If deleting expired backups is enabled, delete all expired backups 
  if ["$expire_backup_delete"=="ON" -a "$backup_location"!=""]; then
      # `find $backup_location/-type d -o -type f -ctime + $expire_days-exec rm -rf {} \;`
      `find $backup_location/ -type d -mtime + $expire_days | xargs rm -rf`
      echo "Expired backup data delete complete!"
  fi
  echo "All databases have been successfully backed up! Thank you!"
  exit
fi
```

修改shell脚本的属性，如下所示：

```bash
chmod 600 /root/mysql_backup.sh
chmod +x /root/mysql_backup.sh
```

然后添加crontab命令：

```bash
00 00 *** /root/mysql_backup.sh
```

这会在00:00每天定期将数据库备份到/var/www/mysql目录，然后可以使用rsync进行同步。

### MySQL恢复

我们刚刚介绍了一些常用的MySQL备份技术，即热备份和冷备份。 回顾一下，热备份的主要目标是能够在应用程序以某种方式发生故障后实时恢复数据，例如在服务器硬盘故障的情况下。 我们了解到，可以通过修改数据库配置文件来实现此类方案，以便将数据库复制到从属服务器上，从而最大限度地减少服务中断。

但有时我们需要执行SQL数据恢复的冷备份，与数据库备份一样，您可以通过命令导入：但是，热备份有时不够。 在某些情况下，执行数据恢复需要冷备份，即使它只是部分数据恢复。 对数据库进行冷备份时，可以使用以下MySQL命令导入它：

```bash
mysql -u username -p databse < backup.sql
```

如您所见，导入和导出数据库是一件相当简单的事情。 如果您需要管理管理权限或处理不同的字符集，此过程可能会变得有点复杂，尽管有许多命令可以帮助您执行此操作。

### Redis备份

Redis是最受欢迎的NoSQL数据库之一，热备份和冷备份技术也可以在使用它的系统中使用。 与MySQL一样，Redis也支持主/从模式，这是实现热备份的理想选择（请参阅Redis的官方文档以了解如何配置它;该过程非常简单）。 对于冷备份，Redis会定期将内存中的缓存数据保存到磁盘上的数据库文件中。 我们可以简单地使用上述rsync备份方法将其与非本地计算机同步。

### Redis恢复

同样，Redis恢复可分为热备份和冷备份恢复。 只要Redis应用程序使用适当的数据库连接，从Redis数据库的热备份恢复数据的方法和目标与上面提到的相同。

Redis冷备份恢复只需将备份的数据库文件复制到工作目录中，然后在其上启动Redis。 数据库文件在引导时自动加载到内存中; Redis引导的速度取决于数据库文件的大小。

### 小结

本次分享中主要研究了一些备份数据以及从部署应用程序后可能发生的灾难中恢复的技术。 我们还介绍了rsync，这是一种可用于同步不同系统上的文件的工具。 使用rsync，我们可以轻松地为MySQL和Redis数据库执行备份和恢复过程。 我们希望通过介绍其中一些概念，您将能够开发灾难恢复过程，以更好地保护Web应用程序中的数据。
