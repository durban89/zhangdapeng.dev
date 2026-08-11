---
title: "Genymotion启动失败原因排查记录"
date: "2025-08-21 10:08:19"
slug: "genymotion-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu"
categories: ["技术"]
tags: ["Genymotion", "Ubuntu", "QEMU", "Hypervisor"]
aliases:
  - "/2025/08/21/Genymotion启动失败原因排查记录/"
  - "/2025/08/21/Genymotion启动失败原因排查记录.html"
  - "/Genymotion启动失败原因排查记录/"
  - "/Genymotion启动失败原因排查记录.html"
  - "/2025/08/21/genymotion-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu/"
  - "/2025/08/21/genymotion-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu.html"
  - "/genymotion-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu.html"
---
启动 Genymotion 报错 内容如下

```
Virtualization technology (VT-X, SVM, AMD-V) may be unavailable or disabled. Please verify your BIOS/UEFI settings.If it is available and enabled, please verify that no other hypervisor (QEMU) is currently in use.
```

大概意思是 没有启用虚拟化技术，也就是没有打开SVM 或者没有打开AMD-V 或者是没有打开VT-X，具体如果打开不同主板不一样，具体可以咨询“豆包”，另外一个原因是启用了虚拟化技术但是有其他的hypervisor在使用需要关闭掉


为了确认我确实打开了，其重启电脑确认了下，我的是SVM，确实是开启了

然后打开电脑通过命令行是可以确认的（可以在重启前先查下）

```bash
sudo lscpu

```

结果如下

```
架构：                       x86_64
  CPU 运行模式：             32-bit, 64-bit
  Address sizes:             48 bits physical, 48 bits virtual
  字节序：                   Little Endian
CPU:                         12
  在线 CPU 列表：            0-11
厂商 ID：                    AuthenticAMD
  BIOS Vendor ID:            Advanced Micro Devices, Inc.
  型号名称：                 AMD Ryzen 5 5600G with Radeon Graphics
    BIOS Model name:         AMD Ryzen 5 5600G with Radeon Graphics          Unknown CPU @ 3.9GHz
    BIOS CPU family:         107
    CPU 系列：               25
    型号：                   80
    每个核的线程数：         2
    每个座的核数：           6
    座：                     1
    步进：                   0
    Frequency boost:         enabled
    CPU(s) scaling MHz:      75%
    CPU 最大 MHz：           4465.0000
    CPU 最小 MHz：           400.0000
    BogoMIPS：               7785.51
    标记：                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc r
                             ep_good nopl xtopology nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c r
                             drand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mw
                             aitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsa
                             veopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nri
                             p_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflo
                             w_recov succor smca fsrm debug_swap
Virtualization features:     
  虚拟化：                   AMD-V
Caches (sum of all):         
  L1d:                       192 KiB (6 instances)
  L1i:                       192 KiB (6 instances)
  L2:                        3 MiB (6 instances)
  L3:                        16 MiB (1 instance)
NUMA:                        
  NUMA 节点：                1
  NUMA 节点0 CPU：           0-11
Vulnerabilities:             
  Gather data sampling:      Not affected
  Ghostwrite:                Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Mitigation; Safe RET
  Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:                Mitigation; Retpolines; IBPB conditional; IBRS_FW; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
  Srbds:                     Not affected
  Tsx async abort:           Not affected

```

可以注意到 

```
Virtualization features:     
  虚拟化：                   AMD-V
```

说明是启用了的


排除了没有开启这个因素就可以排查另外一个问题了，就是有其他的hypervisor在使用

检查步骤如下

1. 检查 QEMU 进程

打开终端，输入以下命令查找是否有 QEMU 相关进程：
```
ps -ef | grep qemu
```
若输出包含 qemu-system 等进程，说明 QEMU 正在运行。

结束进程：使用 kill -9 <进程ID>（将<进程ID>替换为实际的进程编号）。

2. 检查 Hypervisor 是否加载

输入命令查看内核是否加载了 Hypervisor 模块：

```lsmod | grep kvm```

（KVM 是 Linux 常见的虚拟化模块，QEMU 常基于 KVM 运行）

若有输出，说明 KVM 模块已加载，可能有虚拟化程序在使用。

若需关闭，可卸载模块（需管理员权限）：

`sudo rmmod kvm_intel`（Intel 处理器）或 `sudo rmmod kvm_amd`（AMD 处理器），再执行 `sudo rmmod kvm`。


最终我的问题是第二个情况，于是通过执行命令解决了

我的CPU是AMD的，于是运行命令

```
sudo rmmod kvm_amd

sudo rmmod kvm
```

问题解决

