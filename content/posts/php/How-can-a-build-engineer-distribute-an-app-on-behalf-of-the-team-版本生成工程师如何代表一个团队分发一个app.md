---
title: "How can a build engineer distribute an app on behalf of the team? (版本生成工程师如何代表一个团队分发一个app)"
date: "2025-06-13 11:34:59"
slug: "how-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-ban-ben-sheng-cheng-gong-cheng-shi-ru-he-dai-biao-yi-ge-tuan-dui-fen-fa-yi-ge-app"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team?-(版本生成工程师如何代表一个团队分发一个a/"
  - "/2025/06/13/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team?-(版本生成工程师如何代表一个团队分.html"
  - "/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team?-(版本生成工程师如何代表一个团队分发一个app)/"
  - "/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team?-(版本生成工程师如何代表一个团队分发一个app).html"
  - "/2025/06/13/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-版本生成工程师如何代表一个团队分发一个app/"
  - "/2025/06/13/How-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-版本生成工程师如何代表一个团队分发一.html"
  - "/2025/06/13/how-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-ban-ben-sheng-cheng-go/"
  - "/2025/06/13/how-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-ban-ben-sheng-chen.html"
  - "/how-can-a-build-engineer-distribute-an-app-on-behalf-of-the-team-ban-ben-sheng-cheng-gong-chen.html"
---
由于自己也在学习ios开发，也经常的会关注developer.app.com，因此今天有幸看到这篇文章，自己英语也不是很好，综合google和海词，大概了解了一下标题的意思，（`https://developer.apple.com/library/ios/#qa/qa1763/_index.html#//apple_ref/doc/uid/DTS40012165`）这个是文章的地址，这里算是做个笔记，方便自己下次看看。这篇文章整体就是说代表一个团队分发一个app，应该是用于这个团队的测试使用吧。（也许有错，还希望大牛看到后 指点一下）。

那么接下来的结局方案就是如下了：

1) Add the build engineer to the development team with the role of Admin through the [Member Center](https://developer.apple.com/membercenter/index.action). For more information on defining team roles, see [Managing Your Team](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ManagingYourTeam/ManagingYourTeam.html#/apple_ref/doc/uid/TP40012582-CH16-SW1). The Admin role is required to manage the team distribution certificate.

2) If the distribution build will be submitted to the App Store, add the build engineer to the team users on [iTunes Connect](https://itunesconnect.apple.com/) with the role of Technical User. This allows the build engineer to log into iTunes Connect with their own credentials while submitting the app. Skip this step if the build is being used for Ad Hoc beta testing. For more info about the Technical User role in iTunes Connect, see [Managing Users](http://developer.apple.com/library/mac/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/7_ManagingYourTeam/ManagingYourTeam.html#/apple_ref/doc/uid/TP40011225-CH2-SW1) in the iTunes Connect Developer Guide.

3) The build engineer should then…

* Create a new distribution certificate according to [Creating Your Certificates](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/CodeSigningYourApps/CodeSigningYourApps.html#/apple_ref/doc/uid/TP40012582-CH23-SW1). If the team distribution certificate already exists, it must be revoked and recreated by the build engineer according to [Re-Creating Certificates and Updating Related Provisioning Profiles](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingCertificatesandProvisioningAssets/MaintainingCertificatesandProvisioningAssets.html#/apple_ref/doc/uid/TP40012582-CH20-SW8).
* Create a distribution profile using the steps in [Creating Store Provisioning Profiles](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#/apple_ref/doc/uid/TP40012582-CH9-SW12).
* Download and install the distribution provisioning profile by dragging it onto the Xcode or iTunes icons on the dock.
* Define a Bundle Identifier in Xcode that is compatible with the App ID for the app using the steps in [Setting the Bundle ID](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringYourApp/ConfiguringYourApp.html#/apple_ref/doc/uid/TP40012582-CH13-SW16).
* Assign the distribution provisioning profile to the 'Release' Code Signing Identity with the Xcode project Target level Build Settings.
* Depending on your intended distribution method, follow the steps in [Submitting Your App](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/SubmittingYourApp/SubmittingYourApp.html#/apple_ref/doc/uid/TP40012582-CH9-SW1) or [Beta Testing your iOS App](http://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/TestingYouriOSApp/TestingYouriOSApp.html#/apple_ref/doc/uid/TP40012582-CH8-SW1) respectively.

我就直接复制了一下，其实步骤很简单的，基本上能够看的明白。

只不过这里提到了几点Importment：

This Q&A is exclusively for iOS App Store apps. The process within this document should not be followed for the Enterprise Developer Program. Please consult [Apple DTS](https://developer.apple.com/support/technical/submit/) with any questions before leveraging this document, or if you are unsure of your developer program type.

这条就是说这个需求不适合企业开发者项目，显然不是企业开发者，就是个人的喽，呵呵。

另外一点就是

A single email address has access to only one iTunes Connect account, unlike the Member Center, which supports multiple teams per Apple ID. Therefore the build engineer must supply a new unique email address that is not already associated to another iTunes Connect account.

一个email地址只允许链接一个iTunes账户，作为一个bulid enginner 必须有一个email，这个email没有链接多个iTunes账户。好了就这么多了。有不懂的大家一起探讨
