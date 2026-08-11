---
title: "CodeSign error: code signing is required for product type 'Application' in SDK 'iOS 5.0'"
date: "2025-06-12 09:56:44"
slug: "codesign-error-code-signing-is-required-for-product-type-application-in-sdk-ios-50"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/CodeSign-error:-code-signing-is-required-for-product-type-'Application'-in-SDK-'iOS-5.0/"
  - "/2025/06/12/CodeSign-error:-code-signing-is-required-for-product-type-'Application'-in-SDK-'iOS.html"
  - "/CodeSign-error:-code-signing-is-required-for-product-type-'Application'-in-SDK-'iOS-5.0'/"
  - "/CodeSign-error:-code-signing-is-required-for-product-type-'Application'-in-SDK-'iOS-5.0'.html"
  - "/2025/06/12/CodeSign-error-code-signing-is-required-for-product-type-Application-in-SDK-iOS-5.0/"
  - "/2025/06/12/CodeSign-error-code-signing-is-required-for-product-type-Application-in-SDK-iOS-5.0.html"
  - "/2025/06/12/codesign-error-code-signing-is-required-for-product-type-application-in-sdk-ios-50/"
  - "/2025/06/12/codesign-error-code-signing-is-required-for-product-type-application-in-sdk-ios-50.html"
  - "/codesign-error-code-signing-is-required-for-product-type-application-in-sdk-ios-50.html"
---
解决方法如下:

选择工程－>Build Settings -> Code Signing -> Code Signing Identity -> Debug -> Any ios SDK 将选项改为：iPhone Developer
