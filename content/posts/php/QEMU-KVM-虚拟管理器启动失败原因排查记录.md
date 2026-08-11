---
title: "QEMU/KVM-虚拟管理器启动失败原因排查记录"
date: "2025-08-22 15:34:55"
slug: "qemukvm-xu-ni-guan-li-qi-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu"
categories: ["技术"]
tags: ["QEMU", "KVM", "Genymotion"]
aliases:
  - "/2025/08/22/QEMU/KVM-虚拟管理器启动失败原因排查记录/"
  - "/2025/08/22/QEMU/KVM-虚拟管理器启动失败原因排查记录.html"
  - "/QEMU/KVM-虚拟管理器启动失败原因排查记录/"
  - "/QEMU/KVM-虚拟管理器启动失败原因排查记录.html"
  - "/2025/08/22/QEMU-KVM-虚拟管理器启动失败原因排查记录/"
  - "/2025/08/22/QEMU-KVM-虚拟管理器启动失败原因排查记录.html"
  - "/2025/08/22/qemukvm-xu-ni-guan-li-qi-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu/"
  - "/2025/08/22/qemukvm-xu-ni-guan-li-qi-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu.html"
  - "/qemukvm-xu-ni-guan-li-qi-qi-dong-shi-bai-yuan-yin-pai-cha-ji-lu.html"
---
**总结：**

为什么 Genymotion 和 QEMU/KVM 不能同时使用

**豆包给的答案是：**

CPU 虚拟化资源独占：Genymotion 通常基于 VirtualBox 进行虚拟化，而 KVM 是直接利用 CPU 虚拟化功能的内核模块。CPU 的虚拟化功能（如 Intel 的 VT-x 或 AMD 的 AMD-V）一般只能被一个虚拟化管理程序独占使用。当 Genymotion 通过 VirtualBox 占用了这些资源后，QEMU/KVM 就无法再获取到所需的 CPU 虚拟化资源，从而无法正常工作，反之亦然。

---

昨天因为使用Genymotion所以执行了`rmmod kvm`和`rmmod kvm_amd`，导致今天使用QEMU/KVM的时候，虚拟系统管理器报错了

> 启动域时出错: unsupported configuration: Domain requires KVM, but it is not available. Check that virtualization is enabled in the host BIOS, and host configuration is setup to load the kvm modules.
>
>Traceback (most recent call last):
>  File "/usr/share/virt-manager/virtManager/asyncjob.py", line 71, in cb_wrapper
>    callback(asyncjob, *args, **kwargs)
>    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
>  File "/usr/share/virt-manager/virtManager/asyncjob.py", line 107, in tmpcb
>    callback(*args, **kwargs)
>    ~~~~~~~~^^^^^^^^^^^^^^^^^
>  File "/usr/share/virt-manager/virtManager/object/libvirtobject.py", line 57, in newfn
>    ret = fn(self, *args, **kwargs)
>  File "/usr/share/virt-manager/virtManager/object/domain.py", line 1384, in startup
>    self._backend.create()
>    ~~~~~~~~~~~~~~~~~~~~^^
>  File "/usr/lib/python3/dist-packages/libvirt.py", line 1379, in create
>    raise libvirtError('virDomainCreate() failed')
>libvirt.libvirtError: unsupported configuration: Domain requires KVM, but it is not available. Check that virtualization is enabled in the host BIOS, and host configuration is setup to load the kvm modules.
>
>

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1755848862/gowhich/2025-08-22_15-42.png "" %}

**解决方案：**

通过命令重新加载一下就可以了

```

modprobe kvm

modprobe kvm_amd

```
