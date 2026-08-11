---
title: "Could not chdir to home directory /home/USER: Permission denied"
date: "2025-06-18 11:28:27"
slug: "could-not-chdir-to-home-directory-homeuser-permission-denied"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/18/Could-not-chdir-to-home-directory-/home/USER:-Permission-denied/"
  - "/2025/06/18/Could-not-chdir-to-home-directory-/home/USER:-Permission-denied.html"
  - "/Could-not-chdir-to-home-directory-/home/USER:-Permission-denied/"
  - "/Could-not-chdir-to-home-directory-/home/USER:-Permission-denied.html"
  - "/2025/06/18/Could-not-chdir-to-home-directory-home-USER-Permission-denied/"
  - "/2025/06/18/Could-not-chdir-to-home-directory-home-USER-Permission-denied.html"
  - "/2025/06/18/could-not-chdir-to-home-directory-homeuser-permission-denied/"
  - "/2025/06/18/could-not-chdir-to-home-directory-homeuser-permission-denied.html"
  - "/could-not-chdir-to-home-directory-homeuser-permission-denied.html"
---
> We changed the home folder to /data/home/USER.
>
> When I ssh to our centos server. It shows error “Could not chdir to home directory /home/USER: Permission denied”, however loggin ok. I must manually run cd ~ to go to the home directory.
>
> Googled around, and found it is caused by selinux. The solution:
>
> To disabling selinux or change it from enforcing to permissive.  
> vi /etc/sysconfig/selinux  
> change SELINUX from enforcing to permissive: SELINUX=permissive, then reboot.
>
> For server could not be rebooted:  
> #setenforce permissive
>
> You can check if set correctly  
> #getenforce

上面就是解决的办法

其实就是修改一下`/etc/sysconfig/selinux`

将SELINUX修改为`permissive`

如果不想重启机器来使配置起作用，可以直接执行

```bash
setenforce permissive
```

如果没有实现，先确定一下是否是root权限
