---
title: "Linux查看文件系统类型"
date: "2025-06-06 10:27:33"
slug: "linux-cha-kan-wen-jian-xi-tong-lei-xing"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/06/Linux查看文件系统类型/"
  - "/2025/06/06/Linux查看文件系统类型.html"
  - "/Linux查看文件系统类型/"
  - "/Linux查看文件系统类型.html"
  - "/2025/06/06/linux-cha-kan-wen-jian-xi-tong-lei-xing/"
  - "/2025/06/06/linux-cha-kan-wen-jian-xi-tong-lei-xing.html"
  - "/linux-cha-kan-wen-jian-xi-tong-lei-xing.html"
---
### [1. mount](#mount)

```shell
:~$ mount
/dev/sda1 on / type ext4 (rw,errors=remount-ro,user_xattr)
proc on /proc type proc (rw,noexec,nosuid,nodev)
none on /sys type sysfs (rw,noexec,nosuid,nodev)
none on /sys/fs/fuse/connections type fusectl (rw)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
none on /dev type devtmpfs (rw,mode=0755)
none on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
none on /dev/shm type tmpfs (rw,nosuid,nodev)
none on /var/run type tmpfs (rw,nosuid,mode=0755)
none on /var/lock type tmpfs (rw,noexec,nosuid,nodev)
none on /lib/init/rw type tmpfs (rw,nosuid,mode=0755)
none on /var/lib/ureadahead/debugfs type debugfs (rw,relatime)
none on /proc/fs/vmblock/mountPoint type vmblock (rw)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,noexec,nosuid,nodev)
gvfs-fuse-daemon on /home/kysnail/.gvfs type fuse.gvfs-fuse-daemon (rw,nosuid,nodev,user=kysnail)
:~$
```

### [2. df](#df)

```shell
:~$ df -lhT
文件系统      类型    容量  已用 可用 已用% 挂载点
/dev/sda1     ext4     19G   11G  7.8G  57% /
none      devtmpfs    498M  248K  497M   1% /dev
none         tmpfs    502M  252K  501M   1% /dev/shm
none         tmpfs    502M   96K  502M   1% /var/run
none         tmpfs    502M     0  502M   0% /var/lock
none         tmpfs    502M     0  502M   0% /lib/init/rw
none       debugfs     19G   11G  7.8G  57% /var/lib/ureadahead/debugfs
:~$
```

### [3. fdisk](#fdisk)

```shell
:~$ sudo fdisk /dev/sda

WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
         switch off the mode (command 'c') and change display units to
         sectors (command 'u').

Command (m for help): c
DOS Compatibility flag is not set

Command (m for help): u
Changing display/entry units to sectors

Command (m for help): p

Disk /dev/sda: 21.5 GB, 21474836480 bytes
 heads, 63 sectors/track, 2610 cylinders, total 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00077544

Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    40105983    20051968   83  Linux
/dev/sda2        40108030    41940991      916481    5  Extended
/dev/sda5        40108032    41940991      916480   82  Linux swap / Solaris

Command (m for help): q
```

### [4. file](#file)

```shell
:~$ sudo file -s /dev/sda
/dev/sda: x86 boot sector; partition 1: ID=0x83, active, starthead 32, startsector 2048, 40103936 sectors; partition 2: ID=0x5, starthead 254, startsector 40108030, 1832962 sectors, code offset 0x63
kysnail@ubunkysnail:~$ sudo file -s /dev/sda1
/dev/sda1: Linux rev 1.0 ext4 filesystem data, UUID=4942da40-8a49-4bfd-9dc2-45c906d48413 (needs journal recovery) (extents) (large files) (huge files)
:~$
```

### [5. parted](#parted)
```shell 
:~$ sudo parted
GNU Parted 2.2
使用 /dev/sda
欢迎使用 GNU Parted! 输入 'help'可获得命令列表.
(parted) p                                                                
Model: VMware, VMware Virtual S (scsi)
磁盘 /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
分区表：msdos

数字  开始：  End     大小    类型      文件系统        标志
    1049kB  20.5GB  20.5GB  primary   ext4            启动
    20.5GB  21.5GB  938MB   extended
    20.5GB  21.5GB  938MB   logical   linux-swap(v1)

(parted)
```

### [6. 查看 fstab](#fstab)

```shell
# /etc/fstab: static file system information.
#
# Use 'blkid -o value -s UUID' to print the universally unique identifier
# for a device; this may be used with UUID= as a more robust way to name
# devices that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    nodev,noexec,nosuid 0       0
# / was on /dev/sda1 during installation
UUID=4942da40-8a49-4bfd-9dc2-45c906d48413 /               ext4    errors=remount-ro,user_xattr 0       1
# swap was on /dev/sda5 during installation
UUID=935fb95d-771f-448e-9d23-4820106e1783 none            swap    sw              0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0
```
