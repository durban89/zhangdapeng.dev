---
title: "iOS7 下使用UITapGestureRecognizer 实现图片放大缩小的原理（自创）"
date: "2025-06-25 11:35:08"
slug: "ios7-xia-shi-yong-uitapgesturerecognizer-shi-xian-tu-pian-fang-da-suo-xiao-de-yuan-li-zi-chuang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理（自创）/"
  - "/2025/06/25/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理（自创）.html"
  - "/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理（自创）/"
  - "/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理（自创）.html"
  - "/2025/06/25/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理-自创/"
  - "/2025/06/25/iOS7-下使用UITapGestureRecognizer-实现图片放大缩小的原理-自创.html"
  - "/2025/06/25/ios7-xia-shi-yong-uitapgesturerecognizer-shi-xian-tu-pian-fang-da-suo-xiao-de-yuan-li-z/"
  - "/2025/06/25/ios7-xia-shi-yong-uitapgesturerecognizer-shi-xian-tu-pian-fang-da-suo-xiao-de-yuan-.html"
  - "/ios7-xia-shi-yong-uitapgesturerecognizer-shi-xian-tu-pian-fang-da-suo-xiao-de-yuan-li-zi-chuan.html"
---
关于在IOS7下实现点击UIImageView是实现放大图片的原理（完全是自己参考其他的文脏，自己总结出来的，如有雷同，那咱就是心有灵犀啦）

我这里的情况是，在UITableView中的UITableviewCell中使用UIImageView，UIImageView是放在cell中的。这里的实现代码如下

```objectivec
NSString *imagepath = [[NSBundle mainBundle] pathForResource:@"girl"
                                                      ofType:@"jpg"];
UIImage *image = [UIImage imageWithContentsOfFile:imagepath];


GBPathImageView *headImageView = [[GBPathImageView alloc] initWithFrame:CGRectMake(imageX,
                                                                                   imageY,
                                                                                   imageWidth,
                                                                                   imageHeight)
                                                                  image:image
                                                               pathType:GBPathImageViewTypeCircle
                                                              pathColor:[UIColor whiteColor]
                                                            borderColor:[UIColor whiteColor]
                                                              pathWidth:1.0];
headImageView.userInteractionEnabled = YES;
headImageView.multipleTouchEnabled = YES;
headImageView.tag = row;
UITapGestureRecognizer *tap = [[UITapGestureRecognizer alloc] initWithTarget:self
                                                                      action:@selector(showBigImage:)];
tap.view.tag= (int)headImageView.image;
tap.delegate = self;
[headImageView addGestureRecognizer:tap];

[cell.contentView addSubview:headImageView];
```

这里就是使用了UITapGestureRecognizer，添加了排击的事件。

注意点：

* 第一点：UIImageview的userInteractionEnabled和multipleTouchEnabled的设置，不然不起作用
* 第二点：代理UIGestureRecognizerDelegate的引入
* 第三点：tag的使用，这个是为了后面的操作，主要是因为加了tag我们就会知道是哪个UIImageView被点击了，从而做一些其他的处理。

那么关于方法图片和缩小图片的方法如下：

放大图片的代码：

```objectivec
-(void) showBigImage:(id)sender
{
    UITapGestureRecognizer *tap = (UITapGestureRecognizer*)sender;
    NSLog(@"tag = %d",tap.view.tag);
    
    UIImageView *imageViewer=[[UIImageView alloc] init];
    UITapGestureRecognizer *closeTap = [[UITapGestureRecognizer alloc] initWithTarget:self
                                                                              action:@selector(hideBigImage:)];
    closeTap.delegate = self;
    imageViewer.multipleTouchEnabled = YES;
    imageViewer.userInteractionEnabled = YES;
    [imageViewer addGestureRecognizer:closeTap];
    imageViewer.animationDuration = 2.0;
    imageViewer.animationRepeatCount = 1;
    [imageViewer setFrame:CGRectMake(0.0,
                                     _tableview.frame.origin.y,
                                     _tableview.frame.size.width,
                                     _tableview.frame.size.height)];
    [imageViewer startAnimating];
    NSString *imagepath = [[NSBundle mainBundle] pathForResource:@"girl"
                                                          ofType:@"jpg"];
    UIImage *image = [UIImage imageWithContentsOfFile:imagepath];
    [imageViewer setImage:image];
    UIWindow *mainWindow=[UIApplication sharedApplication].delegate.window;
    [mainWindow.rootViewController.view addSubview:imageViewer];
}
```

缩小图片的方法：

```objectivec
-(void) hideBigImage:(id)sender
{
    UITapGestureRecognizer *tap = (UITapGestureRecognizer*)sender;
    [tap.view removeFromSuperview];
}
```

大概的原理全在代码中了，如何放大图片，如何做出图片更加好的效果，这个是后面优化要做的。

参考文章：

* <http://hi.baidu.com/jt_one/item/95babe35583f3598b80c0316>
* <http://www.cocoachina.com/bbs/simple/?t70503.html>
* <http://stackoverflow.com/questions/11552184/uitapgesturerecognizer-not-working-in-uiimageview>
* <http://blog.csdn.net/zjwen1006/article/details/6916591>
* <http://hi.baidu.com/moon_2009/item/b3eca83262582d86c2cf291f>
