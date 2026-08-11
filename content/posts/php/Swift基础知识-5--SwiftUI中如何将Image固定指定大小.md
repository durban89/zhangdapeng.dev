---
title: "swift基础知识（5）- SwiftUI中如何将Image固定指定大小"
date: "2025-07-14 14:50:42"
slug: "swift-ji-chu-zhi-shi-5-swiftui-zhong-ru-he-jiang-image-gu-ding-zhi-ding-da-xiao"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/14/swift基础知识（5）-SwiftUI中如何将Image固定指定大小/"
  - "/2025/07/14/swift基础知识（5）-SwiftUI中如何将Image固定指定大小.html"
  - "/swift基础知识（5）-SwiftUI中如何将Image固定指定大小/"
  - "/swift基础知识（5）-SwiftUI中如何将Image固定指定大小.html"
  - "/2025/07/14/Swift基础知识-5-SwiftUI中如何将Image固定指定大小/"
  - "/2025/07/14/Swift基础知识-5-SwiftUI中如何将Image固定指定大小.html"
  - "/2025/07/14/swift-ji-chu-zhi-shi-5-swiftui-zhong-ru-he-jiang-image-gu-ding-zhi-ding-da-xiao/"
  - "/2025/07/14/swift-ji-chu-zhi-shi-5-swiftui-zhong-ru-he-jiang-image-gu-ding-zhi-ding-da-xiao.html"
  - "/swift-ji-chu-zhi-shi-5-swiftui-zhong-ru-he-jiang-image-gu-ding-zhi-ding-da-xiao.html"
---
SwiftUI中如何将Image固定指定大小

需求将指定图片做圆角处理，并且最终图片指定大小比如300\*300

这里给一个关于最终可以使用的代码

```cpp
Image("xxx")
            .resizable()
            .scaledToFit()
            .clipShape(Circle())
            .overlay(Circle().stroke(Color.white, lineWidth: 4))
            .shadow(radius: 10)
            .frame(maxWidth: 300, maxHeight: 300)
```

效果如如下

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1599923947/gowhich/%E6%88%AA%E5%B1%8F2020-09-12_%E4%B8%8B%E5%8D%8811.17.28.png)
