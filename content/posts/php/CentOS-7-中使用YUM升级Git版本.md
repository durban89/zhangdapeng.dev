---
title: "Centos 7 中使用YUM升级Git版本"
date: "2025-07-07 16:41:37"
slug: "centos-7-zhong-shi-yong-yum-sheng-ji-git-ban-ben"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/07/Centos-7-中使用YUM升级Git版本/"
  - "/2025/07/07/Centos-7-中使用YUM升级Git版本.html"
  - "/Centos-7-中使用YUM升级Git版本/"
  - "/Centos-7-中使用YUM升级Git版本.html"
  - "/2025/07/07/CentOS-7-中使用YUM升级Git版本/"
  - "/2025/07/07/CentOS-7-中使用YUM升级Git版本.html"
  - "/2025/07/07/centos-7-zhong-shi-yong-yum-sheng-ji-git-ban-ben/"
  - "/2025/07/07/centos-7-zhong-shi-yong-yum-sheng-ji-git-ban-ben.html"
  - "/centos-7-zhong-shi-yong-yum-sheng-ji-git-ban-ben.html"
---
正确安装思路是

```bash
sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum erase git
sudo yum install epel-release 
sudo yum install git2u
```

没有问题的话可以正常安装，但是意外总是难以预料我将我遇到的情况记录下

执行第一个命令的时候遇到如下提示

```bash
Loaded plugins: langpacks
Cannot open: https://centos7.iuscommunity.org/ius-release.rpm. Skipping.
Error: Nothing to do
```

执行不了，我能力有限，我直接下载吧

```bash
curl https://centos7.iuscommunity.org/ius-release.rpm
```

还是不行呀，提示这个

那我换个wget

```bash
wget https://centos7.iuscommunity.org/ius-release.rpm
```

我去还是不行，提示如下

```bash
--2018-06-19 11:27:21--  https://centos7.iuscommunity.org/ius-release.rpm
Resolving centos7.iuscommunity.org (centos7.iuscommunity.org)... 162.242.221.48, 2001:4802:7801:102:be76:4eff:fe21:14aa
Connecting to centos7.iuscommunity.org (centos7.iuscommunity.org)|162.242.221.48|:443... connected.
ERROR: cannot verify centos7.iuscommunity.org's certificate, issued by ‘/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=Thawte TLS RSA CA G1’:
  Unable to locally verify the issuer's authority.
To connect to centos7.iuscommunity.org insecurely, use `--no-check-certificate'.
```

OK，咱来个暴力点的加`--no-check-certificate`

```bash
wget https://centos7.iuscommunity.org/ius-release.rpm --no-check-certificate
```

终于可以了，那就继续安装

```bash
sudo yum install ius-release.rpm
sudo yum erase git
```

好吧，问题又来了，我们执行下面这个命令的时候

```bash
sudo yum install epel-release
```

我还是遇到了证书的问题

```bash
Could not retrieve mirrorlist https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7&arch=x86_64&protocol=http error was
14: curl#60 - "Peer's Certificate issuer is not recognized."

 One of the configured repositories failed (Unknown),
 and yum doesn't have enough cached data to continue. At this point the only
 safe thing yum can do is fail. There are a few ways to work "fix" this:

     1. Contact the upstream for the repository and get them to fix the problem.

     2. Reconfigure the baseurl/etc. for the repository, to point to a working
        upstream. This is most often useful if you are using a newer
        distribution release than is supported by the repository (and the
        packages for the previous distribution release still work).

     3. Disable the repository, so yum won't use it by default. Yum will then
        just ignore the repository until you permanently enable it again or use
        --enablerepo for temporary usage:

            yum-config-manager --disable <repoid>

     4. Configure the failing repository to be skipped, if it is unavailable.
        Note that yum will try to contact the repo. when it runs most commands,
        so will have to try and fail each time (and thus. yum will be be much
        slower). If it is a very temporary problem though, this is often a nice
        compromise:

            yum-config-manager --save --setopt=<repoid>.skip_if_unavailable=true

Cannot find a valid baseurl for repo: ius/x86_64
```

老子也不知道咋回事，先说说解决办法，按照如下操作

```bash
sudo mv /etc/yum.repos.d/ius-archive.repo /etc/yum.repos.d/ius-archive.repo.backup
sudo mv /etc/yum.repos.d/ius-dev.repo /etc/yum.repos.d/ius-dev.repo.backup
sudo mv /etc/yum.repos.d/ius.repo /etc/yum.repos.d/ius.repo.backup
sudo mv /etc/yum.repos.d/ius-testing.repo /etc/yum.repos.d/ius-testing.repo.backup
sudo touch /etc/yum.repos.d/ius.repo
```

/etc/yum.repos.d/ius.repo的内容如下

```bash
[ius]
name=IUS Community Packages for Enterprise Linux 7 - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/ius/stable/CentOS/7/$basearch
#mirrorlist=https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7&arch=$basearch&protocol=http
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY

[ius-debuginfo]
name=IUS Community Packages for Enterprise Linux 7 - $basearch - Debug
baseurl=https://mirrors.tuna.tsinghua.edu.cn/ius/stable/CentOS/7/$basearch/debuginfo
#mirrorlist=https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7-debuginfo&arch=$basearch&protocol=http
failovermethod=priority
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY

[ius-source]
name=IUS Community Packages for Enterprise Linux 7 - $basearch - Source
baseurl=https://mirrors.tuna.tsinghua.edu.cn/ius/stable/CentOS/7/SRPMS
#mirrorlist=https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7-source&arch=source&protocol=http
failovermethod=priority
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY
```

然后在执行

```bash
sudo yum install epel-release 
sudo yum install git2u
```

安装成功，可喜可贺。

其实我们打开https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7&arch=x86\_64&protocol=http 这个地址就可以发现，里面的内容全部都是镜像相关的地址信息，我们可以将baseurl中的mirrors.tuna.tsinghua.edu.cn这个地址换成其他的镜像地址，应该也是可以的，这个我就没有做过测试了，有兴趣的可以试下。

原因是由于什么呢？  
其实安装的过程中提示已经说的很清楚了，就是证书的问题，但是在我的其他机器为什么又没有这个问题呢。
