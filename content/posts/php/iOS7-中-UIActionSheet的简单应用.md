---
title: "iOS7 中 UIActionSheet的简单应用"
date: "2025-06-27 09:45:21"
slug: "ios7-zhong-uiactionsheet-de-jian-dan-ying-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-中-UIActionSheet的简单应用/"
  - "/2025/06/27/iOS7-中-UIActionSheet的简单应用.html"
  - "/iOS7-中-UIActionSheet的简单应用/"
  - "/iOS7-中-UIActionSheet的简单应用.html"
  - "/2025/06/27/ios7-zhong-uiactionsheet-de-jian-dan-ying-yong/"
  - "/2025/06/27/ios7-zhong-uiactionsheet-de-jian-dan-ying-yong.html"
  - "/ios7-zhong-uiactionsheet-de-jian-dan-ying-yong.html"
---
UIActionSheet简单的应用

```objectivec
UIActionSheet *actionSheet = [[UIActionSheet alloc] initWithTitle:@"请选择背景图片的来源"
                                                         delegate:self
                                                cancelButtonTitle:@"取消"
                                           destructiveButtonTitle:nil
                                                otherButtonTitles:@"拍照",@"相册",@"图片库",nil];

actionSheet.actionSheetStyle = UIActionSheetStyleDefault;
[actionSheet showInView: self.view];
```

