---
title: "Flutter入门之安装Flutter"
date: "2025-08-01 09:22:22"
slug: "flutter-ru-men-zhi-an-zhuang-flutter"
categories: ["技术"]
tags: ["Flutter"]
aliases:
  - "/2025/08/01/Flutter入门之安装Flutter/"
  - "/2025/08/01/Flutter入门之安装Flutter.html"
  - "/Flutter入门之安装Flutter/"
  - "/Flutter入门之安装Flutter.html"
  - "/2025/08/01/flutter-ru-men-zhi-an-zhuang-flutter/"
  - "/2025/08/01/flutter-ru-men-zhi-an-zhuang-flutter.html"
  - "/flutter-ru-men-zhi-an-zhuang-flutter.html"
---
最近Flutter很火的样子，了解了一下，据说是比ReactNative方便开发，今天分享下如何安装

## 1、安装Flutter

**系统要求**

要安装和运行Flutter，您的开发环境必须满足以下最低要求：

* Operating Systems: macOS (64-bit)
* Disk Space: 700 MB (does not include disk space for IDE/tools).
* Tools: Flutter取决于您的环境中可用的这些命令行工具.bash, mkdir, rm, git, curl, unzip, which

**国内安装流程**

```bash
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
git clone -b master https://github.com/flutter/flutter.git
export PATH="$PWD/flutter/bin:$PATH"
cd ./flutter
```

运行以下命令以查看是否需要安装任何依赖项才能完成设置：

```bash
flutter doctor
```

安装过程中会遇到类似下面的问题

```bash
Because flutter_tools depends on file_testing 2.0.3 which doesn't match any versions, version solving failed.
Error: Unable to 'pub upgrade' flutter tool. Retrying in five seconds... (9 tries left)
```

要解决这个问题，多数是网络问题，设置下代理就好了，如下

```bash
export https_proxy="proxyserver"
```

设置后再次执行`flutter doctor`如果代理没有问题就可以正常安装了，执行完的结果类似如下

```bash
$ flutter doctor                            
Building flutter tool...

  ╔════════════════════════════════════════════════════════════════════════════╗
  ║                 Welcome to Flutter! - https://flutter.io                   ║
  ║                                                                            ║
  ║ The Flutter tool anonymously reports feature usage statistics and crash    ║
  ║ reports to Google in order to help Google contribute improvements to       ║
  ║ Flutter over time.                                                         ║
  ║                                                                            ║
  ║ Read about data we send with crash reports:                                ║
  ║ https://github.com/flutter/flutter/wiki/Flutter-CLI-crash-reporting        ║
  ║                                                                            ║
  ║ See Google's privacy policy:                                               ║
  ║ https://www.google.com/intl/en/policies/privacy/                           ║
  ║                                                                            ║
  ║ Use "flutter config --no-analytics" to disable analytics and crash         ║
  ║ reporting.                                                                 ║
  ╚════════════════════════════════════════════════════════════════════════════╝

Flutter assets will be downloaded from https://storage.flutter-io.cn. Make sure you trust this source!
Downloading Material fonts...                                5.1s
Downloading package sky_engine...                            4.5s
Downloading common tools...                                 20.8s
Downloading darwin-x64 tools...                             77.2s
Downloading android-arm-profile/darwin-x64 tools...          6.6s
Downloading android-arm-release/darwin-x64 tools...          5.3s
Downloading android-arm64-profile/darwin-x64 tools...        5.5s
Downloading android-arm64-release/darwin-x64 tools...        6.6s
Downloading android-x86 tools...                            23.6s
Downloading android-x64 tools...                            15.0s
Downloading android-arm tools...                             9.4s
Downloading android-arm-profile tools...                     6.9s
Downloading android-arm-release tools...                    12.8s
Downloading android-arm64 tools...                           7.3s
Downloading android-arm64-profile tools...                   7.8s
Downloading android-arm64-release tools...                   5.7s
Downloading android-arm-dynamic-profile tools...             7.4s
Downloading android-arm-dynamic-release tools...             5.4s
Downloading android-arm64-dynamic-profile tools...           6.8s
Downloading android-arm64-dynamic-release tools...           6.2s
Downloading ios tools...                                    15.1s
Downloading ios-profile tools...                            38.4s
Downloading ios-release tools...                            14.4s
Downloading Gradle Wrapper...                                1.4s
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel master, v0.5.9-pre.83, on Mac OS X 10.12.6 16G1314, locale zh-Hans-CN)
[✗] Android toolchain - develop for Android devices
    ✗ Unable to locate Android SDK.
      Install Android Studio from: https://developer.android.com/studio/index.html
      On first launch it will assist you in installing the Android SDK components.
      (or visit https://flutter.io/setup/#android-setup for detailed instructions).
      If Android SDK has been installed to a custom location, set $ANDROID_HOME to that location.
[!] iOS toolchain - develop for iOS devices (Xcode 9.0)
    ✗ libimobiledevice and ideviceinstaller are not installed. To install, run:
        brew install --HEAD libimobiledevice
        brew install ideviceinstaller
    ✗ ios-deploy not installed. To install:
        brew install ios-deploy
    ! CocoaPods out of date (1.5.0 is recommended).
        CocoaPods is used to retrieve the iOS platform side's plugin code that responds to your plugin usage on the Dart side.
        Without resolving iOS dependencies with CocoaPods, plugins will not work on iOS.
        For more info, see https://flutter.io/platform-plugins
      To upgrade:
        brew upgrade cocoapods
        pod setup
[✗] Android Studio (not installed)
[!] IntelliJ IDEA Ultimate Edition (version 2017.3.5)
    ✗ Flutter plugin not installed; this adds Flutter specific functionality.
    ✗ Dart plugin not installed; this adds Dart specific functionality.
[!] VS Code (version 1.26.1)
[!] Connected devices
    ! No devices available

! Doctor found issues in 6 categories.
```

**将Flutter永久添加到您的路径**

为了在任何终端会话中都能运行flutter命令。  
通常，只需在打开新窗口时执行的文件中添加一行。  
例如：

1. 确定放置Flutter SDK的目录。您将在步骤3中使用此功能。
2. 打开（或创建）$HOME/.bash\_profile或者$HOME~/.zshrc。您的计算机上的文件路径和文件名可能不同。
3. 添加以下行并将[PATH\_TO\_FLUTTER\_GIT\_DIRECTORY]更改为克隆Flutter的git repo的路径：

```bash
export PATH=[PATH_TO_FLUTTER_GIT_DIRECTORY]/flutter/bin:$PATH
```

运行`source $HOME/.bash_profile`或`source $HOME/.zshrc`刷新当前窗口.  
通过运行验证flutter/bin目录现在位于PATH中，如下

```bash
echo $PATH
```

如果输出有如下内容说明配置成功

```bash
/xxx/xxx/flutter/bin:/xxx/xxx/xxxx/otherpath
```
