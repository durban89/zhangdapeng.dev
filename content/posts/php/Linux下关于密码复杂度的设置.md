---
title: "Linux下关于密码复杂度的设置"
date: "2025-07-11 11:15:16"
slug: "linux-xia-guan-yu-mi-ma-fu-za-du-de-she-zhi"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/11/Linux下关于密码复杂度的设置/"
  - "/2025/07/11/Linux下关于密码复杂度的设置.html"
  - "/Linux下关于密码复杂度的设置/"
  - "/Linux下关于密码复杂度的设置.html"
  - "/2025/07/11/linux-xia-guan-yu-mi-ma-fu-za-du-de-she-zhi/"
  - "/2025/07/11/linux-xia-guan-yu-mi-ma-fu-za-du-de-she-zhi.html"
  - "/linux-xia-guan-yu-mi-ma-fu-za-du-de-she-zhi.html"
---
在linux下设置密码复杂度办法：

(1)修改/etc/login.defs文件

```bash
PASS_MAX_DAYS   90  #密码最长过期天数
PASS_MIN_DAYS   80  #密码最小过期天数
PASS_MIN_LEN    10  #密码最小长度
PASS_WARN_AGE   7   #密码过期警告天数
```

(2)修改/etc/pam.d/system-auth文件

找到 `password requisite pam_cracklib.so` 这么一行替换成如下(如果没有的话自己添加下)：

```bash
password requisite pam_cracklib.so retry=5 difok=3 minlen=10 ucredit=-1 lcredit=-3 dcredit=-3 dictpath=/usr/share/cracklib/pw_dict
```

参数含义（依次如下）：

> 尝试次数：5    
> 最少不同字符：3   
> 最小密码长度：10    
> 最少大写字母：1   
> 最少小写字母：3   
> 最少数字：3   
> 密码字典：/usr/share/cracklib/pw\_dict

cracklib密码强度检测过程:

1. 首先检查密码是否是字典的一部分，如果不是，则进行下面的检查
2. 密码强度检测过程
3. 新密码是否旧密码的回文
4. 新密码是否只是就密码改变了大小写
5. 新密码是否和旧密码很相似
6. 新密码是否太短
7. 新密码的字符是否是旧密码字符的一个循环 例如旧密码：123 新密码：231
8. 这个密码以前是否使用过。
