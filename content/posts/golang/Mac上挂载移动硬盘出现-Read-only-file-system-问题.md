---
title: "Mac上挂载移动硬盘出现&quot;Read-only file system&quot;问题"
date: "2025-08-01 09:21:54"
slug: "mac-shang-gua-zai-yi-dong-ying-pan-chu-xian-quotread-only-file-systemquot-wen-ti"
categories: ["技术"]
tags: ["移动硬盘"]
aliases:
  - "/2025/08/01/Mac上挂载移动硬盘出现&quot;Read-only-file-system&quot;问题/"
  - "/2025/08/01/Mac上挂载移动硬盘出现&quot;Read-only-file-system&quot;问题.html"
  - "/Mac上挂载移动硬盘出现&quot;Read-only-file-system&quot;问题/"
  - "/Mac上挂载移动硬盘出现&quot;Read-only-file-system&quot;问题.html"
  - "/2025/08/01/Mac上挂载移动硬盘出现-Read-only-file-system-问题/"
  - "/2025/08/01/Mac上挂载移动硬盘出现-Read-only-file-system-问题.html"
  - "/2025/08/01/mac-shang-gua-zai-yi-dong-ying-pan-chu-xian-quotread-only-file-systemquot-wen-ti/"
  - "/2025/08/01/mac-shang-gua-zai-yi-dong-ying-pan-chu-xian-quotread-only-file-systemquot-wen-ti.html"
  - "/mac-shang-gua-zai-yi-dong-ying-pan-chu-xian-quotread-only-file-systemquot-wen-ti.html"
---
解决步骤如下

1. 确保移动硬盘链接，查看硬盘挂在的节点，操作如下

```bash
diskutil info /Volumes/YOUR_NTFS_DISK_NAME
```

找到 Device Node

```bash
Device Node:              /dev/disk1s1
```

比如我这里的硬盘默认挂在在/Volumes/Elements  
我查看我的硬盘挂在节点信息如下

```bash
$ diskutil info /Volumes/Elements
   Device Identifier:        disk2s1
   Device Node:              /dev/disk2s1
   Whole:                    No
   Part of Whole:            disk2

   Volume Name:              Elements
   Mounted:                  Yes
   Mount Point:              /Volumes/Elements

   Partition Type:           Microsoft Basic Data
   File System Personality:  NTFS
   Type (Bundle):            ntfs
   Name (User Visible):      Windows NT File System (NTFS)

   OS Can Be Installed:      No
   Media Type:               Generic
   Protocol:                 USB
   SMART Status:             Not Supported
   Disk / Partition UUID:    F082E054-36E6-419F-A2CD-5B9A82576C4F

   Disk Size:                1.0 TB (1000168488960 Bytes) (exactly 1953454080 512-Byte-Units)
   Device Block Size:        512 Bytes

   Volume Total Space:       1.0 TB (1000168484864 Bytes) (exactly 1953454072 512-Byte-Units)
   Volume Used Space:        424.7 GB (424701173760 Bytes) (exactly 829494480 512-Byte-Units) (42.5%)
   Volume Available Space:   575.5 GB (575467311104 Bytes) (exactly 1123959592 512-Byte-Units) (57.5%)
   Allocation Block Size:    4096 Bytes

   Read-Only Media:          No
   Read-Only Volume:         Yes

   Device Location:          External
   Removable Media:          Fixed
```

找到

```bash
Device Node:              /dev/disk2s1
```

这个信息保留下来，后面会使用

2. 然后将硬盘弹出，但是不要拔掉移动硬盘连接，操作如下

```bash
hdiutil eject /Volumes/YOUR_NTFS_DISK_NAME
```

我这里的执行如下

```bash
$  hdiutil eject /Volumes/MYHD/
"disk2" unmounted.
"disk2" ejected.
```

3. 创建一个目录，稍后将mount到这个目录

```bash
sudo mkdir /Volumes/MYHD
```

4. 将NTFS硬盘 挂载 mount 到mac

```bash
sudo mount_ntfs -o rw,nobrowse /dev/disk2s1 /Volumes/MYHD/
```

5.可以进行任意的写入操作了，比如我这里进行了copy操作

```bash
cp ~/Movies/小XXX黄XXX片.mp4 /Volumes/MYHD/xx/xxx/
```
