---
title: "iOS 项目开发 Application failed codesign verification.警告"
date: "2025-06-20 11:50:36"
slug: "ios-xiang-mu-kai-fa-application-failed-codesign-verification-jing-gao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS-项目开发-Application-failed-codesign-verification.警告/"
  - "/2025/06/20/iOS-项目开发-Application-failed-codesign-verification.警告.html"
  - "/iOS-项目开发-Application-failed-codesign-verification.警告/"
  - "/iOS-项目开发-Application-failed-codesign-verification.警告.html"
  - "/2025/06/20/iOS-项目开发-Application-failed-codesign-verification-警告/"
  - "/2025/06/20/iOS-项目开发-Application-failed-codesign-verification-警告.html"
  - "/2025/06/20/ios-xiang-mu-kai-fa-application-failed-codesign-verification-jing-gao/"
  - "/2025/06/20/ios-xiang-mu-kai-fa-application-failed-codesign-verification-jing-gao.html"
  - "/ios-xiang-mu-kai-fa-application-failed-codesign-verification-jing-gao.html"
---
关于这个问题，在项目中可以这样进行解决，其实很简单，

第一步：选中Target

第二步：找到Build Settings

第三步：搜索Validate

第四步：找到Validate Build Product

第五步：将所有项设置为No

解决。
