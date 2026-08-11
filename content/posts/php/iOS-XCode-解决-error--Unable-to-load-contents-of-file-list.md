---
title: "iOS XCode 解决 error: Unable to load contents of file list"
date: "2025-07-15 09:50:46"
slug: "ios-xcode-jie-jue-error-unable-to-load-contents-of-file-list"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/15/iOS-XCode-解决-error:-Unable-to-load-contents-of-file-list/"
  - "/2025/07/15/iOS-XCode-解决-error:-Unable-to-load-contents-of-file-list.html"
  - "/iOS-XCode-解决-error:-Unable-to-load-contents-of-file-list/"
  - "/iOS-XCode-解决-error:-Unable-to-load-contents-of-file-list.html"
  - "/2025/07/15/iOS-XCode-解决-error-Unable-to-load-contents-of-file-list/"
  - "/2025/07/15/iOS-XCode-解决-error-Unable-to-load-contents-of-file-list.html"
  - "/2025/07/15/ios-xcode-jie-jue-error-unable-to-load-contents-of-file-list/"
  - "/2025/07/15/ios-xcode-jie-jue-error-unable-to-load-contents-of-file-list.html"
  - "/ios-xcode-jie-jue-error-unable-to-load-contents-of-file-list.html"
---
问题：`error: Unable to load contents of file list ......`

原因是：升级了一下 cocoapods的版本后，由于版本不同导致

重新安装或者升级一下就好

```bash
gem install cocoapods --pre
```

然后把工程里面的 Pod 文件夹和 Podfile.lock 文件删掉，然后 cd 到项目根目录，然后重新运行一下 pod install 命令，重新编译即可。
