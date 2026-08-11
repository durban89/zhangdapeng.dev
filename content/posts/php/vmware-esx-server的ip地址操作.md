---
title: "VMware esx server的ip地址操作"
date: "2025-06-13 10:13:31"
slug: "vmware-esx-server-de-ip-di-zhi-cao-zuo"
categories: ["技术"]
tags: ["VMware"]
aliases:
  - "/2025/06/13/VMware-esx-server的ip地址操作/"
  - "/2025/06/13/VMware-esx-server的ip地址操作.html"
  - "/VMware-esx-server的ip地址操作/"
  - "/VMware-esx-server的ip地址操作.html"
  - "/2025/06/13/vmware-esx-server的ip地址操作/"
  - "/2025/06/13/vmware-esx-server的ip地址操作.html"
  - "/2025/06/13/vmware-esx-server-de-ip-di-zhi-cao-zuo/"
  - "/2025/06/13/vmware-esx-server-de-ip-di-zhi-cao-zuo.html"
  - "/vmware-esx-server-de-ip-di-zhi-cao-zuo.html"
---
### [第一次配置的时候可按照下面的操作进行：](#1)

- 首先，你必须访问物理控制台。  
- 把ESX主机设为维护模式并从Virtual Center中断开。  
- 连接到ESX主机的控制台。  
- 删除旧的IP（即删除vswif接口），"esxcfg-vswif -d vswif0" （vswif0 你的第一块网卡）  
- 建立一个新的vswif接口及相应的IP地址，  
`esxcfg-vswif -a vswif0 -p Service Console -i 192.168.0.100 -n 255.255.255.0 -b 192.168.0.255`  
这里:  
-i 是新的IP地址  
-n 是子网掩码  
-b 是广播地址  
- 更新默认网关，”nano /etc/sysconfig/network file”按CTRL+O和回车，然后CTRL+Q退出。  
- 重新启动接口。"esxcfg-vswif -s vswif0″ （禁用vswif0接口），然后"esxcfg-vswif -e vswif0″（开启该接口）。

### [重新修改下ESX Server 的IP地址，简单描述一下正确的操作过程：](#2)

只有简单几个步骤：  
命名一: `esxcfg-vswif -i 10.0.0.1 -n 255.255.255.0 vswif0`  # 修改 Service console 地址  
命令二：`vi /etc/hosts` # 修改机器IP地址  
命令三：`vi /etc/sysconfig/network` # 修改机器名和网关  
命令四：`service network restart`　  #使用此命令重启网卡  
其中命令四也可以通过重启实现，不建议  
IP 修改之后，使用新的IP登录就可以了.

**—————————————————————————————————————————————————**  
其他一些有用的命令，来源于网络：  
- 看你的esx版本。  
`vmware -v  `
- 列出esx里知道的服务  
`esxcfg-firewall -s  `
- 查看具体服务的情况  
`esxcfg-firewall -q sshclinet  `
- 重新启动vmware服务  
`service mgmt-vmware restart  `
- 修改root的密码  
`passwd root  `
- 列出你当前的虚拟交换机  
`esxcfg-vswitch -l  `
- 查看控制台的设置  
`esxcfg-vswif -l  `
- 列出系统的网卡  
`esxcfg-nics -l  `
- 添加一个虚拟交换机，名字叫（internal）连接到两块物理网卡，（重新启动服务，vi就能看见了）  
`esxcfg-vswitch -a vSwitch1 ` 
`esxcfg-vswitch -A internal vSwitch1  `
`esxcfg-vswitch -L vmnic1 vSwitch1 ` 
`esxcfg-vswitch -L vmnic2 vSwitch1  `
- 删除交换机,(注意，别把控制台的交换机也删了）  
`esxcfg-vswitch -D vSwitch1  `
- 删除交换机上的网卡  
`esxcfg-vswitch -u vmnic1 vswitch2  `
- 删除portgroup  
`esxcfg-vswitch -D internel vswitch1  `
- 创建 vmkernel switch ，如果你希望使用vmotion，iscsi的这些功能，你必须创建( 通常是不需要添加网关的）  
`esxcfg-vswitch -l ` 
`esxcfg-vswitch -a vswitch2  `
`esxcfg-vswitch -A “vm kernel” vswitch2 ` 
`esxcfg-vswitch -L vmnic3 vswitch2  `
`esxcfg-vmknic -a “vm kernel” -i 172.16.1.141 -n 255.255.252.0 ` 
`esxcfg-route 172.16.0.254  `
- 打开防火墙ssh端口  
`esxcfg-firewall -e sshClient  `
`esxcfg-firewall -d sshClient ` 
- 创建控制台  
`esxcfg-vswitch -a vSwitch0 ` 
`esxcfg-vswitch -A “service console” vSwitch0 ` 
`esxcfg-vswitch -L vmnic0 vSwitch0  `
`esxcfg-vswif -a vswif0 -p “service console” -i 172.16.1.140 -n 255.255.252.0 ` 
- 添加nas设备(a 添加标签，-o，是nas服务器的名字或ip，-s 是nas输入的共享名字）  
`esxcfg-nas -a isos -o nas.vmwar.cn -s isos  `
- 列出nas连接  
`esxcfg-nas -l  `
- 强迫esx去连接nas服务器(用esxcfg-nas -l 来看看结果）  
`esxcfg-nas -r ` 
`esxcfg-nas -l  `
- 连接iscsi 设备(e:enable q:查询 d：disable s:强迫搜索）  
`esxcfg-swiscsi -e  `
- 设置targetip  
`vmkiscsi-tool -D -a 172.16.1.133 vmhba40 ` 
- 列出和target的连接  
`vmkiscsi-tool -l -T vmhba40  `
- 列出当前的磁盘  
`ls -l mfs/devices/disks`
