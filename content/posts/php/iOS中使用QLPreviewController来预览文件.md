---
title: "iOS中使用QLPreviewController来预览文件"
date: "2025-06-20 14:34:11"
slug: "ios-zhong-shi-yong-qlpreviewcontroller-lai-yu-lan-wen-jian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS中使用QLPreviewController来预览文件/"
  - "/2025/06/20/iOS中使用QLPreviewController来预览文件.html"
  - "/iOS中使用QLPreviewController来预览文件/"
  - "/iOS中使用QLPreviewController来预览文件.html"
  - "/2025/06/20/ios-zhong-shi-yong-qlpreviewcontroller-lai-yu-lan-wen-jian/"
  - "/2025/06/20/ios-zhong-shi-yong-qlpreviewcontroller-lai-yu-lan-wen-jian.html"
  - "/ios-zhong-shi-yong-qlpreviewcontroller-lai-yu-lan-wen-jian.html"
---
Mac OS系统有一个很方便的功能就是文件预览，在Finder中选中一个文件，按下空格键就能够预览其中的内容。支持图片、文档、视频等类型。在iOS4.0系统中，官方SDK提供了一个QLPreviewController，使用它就可以让我们的App在iPhone/iPad中直接预览各个文件了。官方的开发文档中说明其支持的文件类型有：

1. iWork文档
2. 微软Office97以上版本的文档
3. RTF文档
4. PDF文件
5. 图片文件
6. 文本文件和CSV文件

使用方法也很简单，直接alloc出一个QLPreviewController对象，用presentModalViewController方法把它调出来即可。要指定QLPreviewController预览那个文件，只要直接实现它的代理方法previewItemAtIndex，返回一个NSURL对象即可：

```objectivec
- (id)previewController:(QLPreviewController *)previewController previewItemAtIndex:(NSInteger)idx
{   
    return [NSURL fileURLWithPath:[NSString stringWithFormat:@“%@/Documents/files/%@”, NSHomeDirectory(), [fileList objectAtIndex:currentIndex]]];
}
```

