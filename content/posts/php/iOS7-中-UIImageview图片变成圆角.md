---
title: "iOS7 中 UIImageview图片变成圆角"
date: "2025-06-26 11:15:35"
slug: "ios7-zhong-uiimageview-tu-pian-bian-cheng-yuan-jiao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-中-UIImageview图片变成圆角/"
  - "/2025/06/26/iOS7-中-UIImageview图片变成圆角.html"
  - "/iOS7-中-UIImageview图片变成圆角/"
  - "/iOS7-中-UIImageview图片变成圆角.html"
  - "/2025/06/26/ios7-zhong-uiimageview-tu-pian-bian-cheng-yuan-jiao/"
  - "/2025/06/26/ios7-zhong-uiimageview-tu-pian-bian-cheng-yuan-jiao.html"
  - "/ios7-zhong-uiimageview-tu-pian-bian-cheng-yuan-jiao.html"
---
之前做图片的圆角是使用了一个别人写的类库叫做GBPathImageView，实现起来是相当的复杂啊，重写了UIImageview这个类，不过呢用起来也是很不错的，但是遇到的问题是，在进行图片异步加载的时候，要怎么处理呢，首先是要拿到这个图片，但是图片异步的话，图片首先是不在本地的，那么你重新绘制的话就是一张默认的空图片，最后你要获取新图片再进行绘制，导致的结果就是重复做了两次操作，但是在cell这样的操作，感觉起来是相当的复杂，在你进行这个操作的时候，滑动的cell要做什么呢？

好了，不多说说了，解决方法其实很简答，只怪自己对原生的类库不了解，也不怪别人的。

```objectivec
NSString *defaultImageString = [[NSBundle mainBundle] pathForResource:@"person_default" ofType:@"png"];
    UIImageView *imageView = [[UIImageView alloc] initWithFrame:CGRectMake(imageViewX,
                                                                           imageViewY,
                                                                           imageViewWidth,
                                                                           imageViewHeight)];
    [imageView setImageWithURL:[NSURL URLWithString:[storage fetchCelebrityPicWithId:_personId]]
              placeholderImage:[UIImage imageWithContentsOfFile:defaultImageString]
   usingActivityIndicatorStyle:UIActivityIndicatorViewStyleWhiteLarge];
    
    
    CALayer *lay  = imageView.layer;//获取ImageView的层
    [lay setMasksToBounds:YES];
    [lay setCornerRadius:45.0];
```

圆角的尺寸大家自己定义就好了。

效果很明显。大家可以尝试一下。

---

参考的文章：

<http://my.oschina.net/mejinke/blog/70634>

