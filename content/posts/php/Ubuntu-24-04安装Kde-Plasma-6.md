---
title: "Ubuntu 24.04安装Kde Plasma 6"
date: "2025-07-18 09:38:41"
slug: "ubuntu-2404-an-zhuang-kde-plasma-6"
categories: ["技术"]
tags: ["Ubuntu", "Linux", "Kde", "Plasma"]
aliases:
  - "/2025/07/18/Ubuntu-24.04安装Kde-Plasma-6/"
  - "/2025/07/18/Ubuntu-24.04安装Kde-Plasma-6.html"
  - "/Ubuntu-24.04安装Kde-Plasma-6/"
  - "/Ubuntu-24.04安装Kde-Plasma-6.html"
  - "/2025/07/18/Ubuntu-24-04安装Kde-Plasma-6/"
  - "/2025/07/18/Ubuntu-24-04安装Kde-Plasma-6.html"
  - "/2025/07/18/ubuntu-2404-an-zhuang-kde-plasma-6/"
  - "/2025/07/18/ubuntu-2404-an-zhuang-kde-plasma-6.html"
  - "/ubuntu-2404-an-zhuang-kde-plasma-6.html"
---
网上查到资料显示 从Ubuntu 22.04 升级到Ubuntu 24.04后可以安装Kde Plasma 6

于是找到了一个升级的[指南](https://ryanraposo.github.io/guides/markdown/plasma6.html)

但是按照这个流程来 发现 kde-builder 在使用的时候 配置文件找不到 看了下官网的资料提示 配置文件用的是 `~/.config/kde-builder.yaml`，以yaml结为的文件

里面的内容也与指南中提到的不一样，我用了默认的方案，通过使用`kde-builder --generate-config`，生成了默认的配置文件，唯一要修改的地方是qt的安装路径

我安装qt的时候没有使用默认的`/opt/qt`，我用的是`~/Qt`，所以唯一要修改的地方也就这里的，其他的都不需要修改

然后在执行`kde-builder workspace`的时候，也遇到了问题

```bash
Building frameworks/kcoreaddons (frameworks/kcoreaddons) (5/153)
        Fetching remote changes to kcoreaddons
        Merging kcoreaddons changes from branch master
        Source update complete for kcoreaddons: 1 commit pulled.
        Preparing build system for kcoreaddons.
        Removing files in build directory for kcoreaddons
        Old build system cleaned, starting new build system.
        Running cmake targeting Ninja...
        Unable to configure kcoreaddons with KDE CMake

kcoreaddons didn't build, stopping here.
[monitor process] recv SIGHUP, will end after updater process finishes.
[updater process] recv SIGHUP, will end after updating kwidgetsaddons project.

<<<  PROJECTS FAILED TO BUILD  >>>
kcoreaddons - /home/durban/kde/log/2025-07-18_01/kcoreaddons/cmake.log

Possible solution: Install the build dependencies for the projects:
kcoreaddons
You can use "sudo apt build-dep <source_package>", "sudo dnf builddep <package>", "sudo zypper --plus-content repo-source source-install --build-deps-only <source_package>" or a similar command for your distro of choice.
See https://develop.kde.org/docs/getting-started/building/help-dependencies

Important notification for kcoreaddons:
    kcoreaddons has failed to build 5 times.

:-(
Your logs are saved in /home/durban/kde/log/2025-07-18_01
  (additional logs are saved in /home/durban/.local/state/log/2025-07-18_02)
```
查看日志文件`/home/durban/kde/log/2025-07-18_01/kcoreaddons/cmake.log`

发现一个问题

```
-- Found Python3: /usr/bin/python3 (found suitable version "3.12.3", minimum required is "3.9") found components: Interpreter Development Development.Module Development.Embed 
CMake Error at CMakeLists.txt:102 (find_package):
  By not providing "FindShiboken6.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "Shiboken6", but CMake did not find one.

  Could not find a package configuration file provided by "Shiboken6" with
  any of the following names:

    Shiboken6Config.cmake
    shiboken6-config.cmake

  Add the installation prefix of "Shiboken6" to CMAKE_PREFIX_PATH or set
  "Shiboken6_DIR" to a directory containing one of the above files.  If
  "Shiboken6" provides a separate development package or SDK, be sure it has
  been installed.
```

说明需要 Shiboken6 这个库，但是我查了下，在目前Ubuntu 24.04这个版本 只有 Shiboken2 这个库

可以通过 https://packages.ubuntu.com/ 这个网站查到制定版本的Ubuntu对应的库是否存在

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1752805780/2025-07-18_09-56_1_cuuhda.png "点击查看大图: 查询条件" %}

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1752805780/2025-07-18_09-56_xf5hw2.png "点击查看大图: 查询结果" %}

如果是查询 Shiboken2 这个库 是有的

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1752806228/2025-07-18_10-35_ahcyrw.png "点击查看大图: 查询结果" %}

所以我总结，暂时Ubuntu 24.04 不适合安装 Kde Plasma 6

测试了下 Ubuntu的 24.10 和 25.04 这两个版本是有 Shiboken6 这个库的

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1752806234/2025-07-18_10-36_1_rwtleq.png "点击查看大图: 查询结果" %}

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1752806230/2025-07-18_10-36_abbvzj.png "点击查看大图: 查询结果" %}

等待下个LTS版本吧 24.04是没有希望了，其实也可以升级到 24.10 或者更后面的版本

