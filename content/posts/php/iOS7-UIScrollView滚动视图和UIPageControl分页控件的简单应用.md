---
title: "IOS7 UIScrollView滚动视图和UIPageControl分页控件的简单应用"
date: "2025-06-26 14:55:10"
slug: "ios7-uiscrollview-gun-dong-shi-tu-he-uipagecontrol-fen-ye-kong-jian-de-jian-dan-ying-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/IOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用/"
  - "/2025/06/26/IOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用.html"
  - "/IOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用/"
  - "/IOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用.html"
  - "/2025/06/26/iOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用/"
  - "/2025/06/26/iOS7-UIScrollView滚动视图和UIPageControl分页控件的简单应用.html"
  - "/2025/06/26/ios7-uiscrollview-gun-dong-shi-tu-he-uipagecontrol-fen-ye-kong-jian-de-jian-dan-ying-yo/"
  - "/2025/06/26/ios7-uiscrollview-gun-dong-shi-tu-he-uipagecontrol-fen-ye-kong-jian-de-jian-dan-yin.html"
  - "/ios7-uiscrollview-gun-dong-shi-tu-he-uipagecontrol-fen-ye-kong-jian-de-jian-dan-ying-yong.html"
---
我这里是使用故事版（storyboard）实现的。

创建一个简单的storyboard，在里面添加一个UIViewContoller，在view里面添加一个PageControl和一个ScrollView，并做链接。

```objectivec
@property (strong, nonatomic) IBOutlet UIScrollView *pageScroll;
@property (strong, nonatomic) IBOutlet UIPageControl *pageControl;
```

在监听一个pageControl的value change事件，这里不知道怎么添加的话，请关注这里341268380，我们的技术交流群。

同时添加一个存储要展示图片的数组变量

```objectivec
@property (strong, nonatomic) NSArray *photoList;
- (IBAction)changePage:(id)sender;
```

同时要加入

UIScrollViewDelegate

代理

基础工作做完之后，开始我们的过程实现

初始化的工作如下：

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    NSString *img1 = [[NSBundle mainBundle] pathForResource:@"bg_welcome1"
                                                     ofType:@"png"];
    NSString *img2 = [[NSBundle mainBundle] pathForResource:@"bg_welcome2"
                                                     ofType:@"png"];
    NSString *img3 = [[NSBundle mainBundle] pathForResource:@"bg_welcome3"
                                                     ofType:@"png"];
    
    
    
    
    _photoList = [[NSArray alloc] initWithObjects:
                  [UIImage imageWithContentsOfFile:img1],
                  [UIImage imageWithContentsOfFile:img2],
                  [UIImage imageWithContentsOfFile:img3],
                  [self getEmptyUIImage],nil];
    
    NSInteger pageCount = [_photoList count];
    _pageControl.currentPage = 0;
    _pageControl.numberOfPages = pageCount;
    
    _pageScroll.frame = CGRectMake(0.0,
                                   0.0,
                                   320.0,
                                   568.0);
    _pageScroll.delegate = self;
    for(NSInteger i=0;i<pageCount;i++)
    {
        CGRect frame;
        frame.origin.x = _pageScroll.frame.size.width * i;
        frame.origin.y = 0;
        frame.size = _pageScroll.frame.size;
//        frame = CGRectInset(frame, 10.0, 10.0);
        UIImageView *pageView = [[UIImageView alloc] initWithImage:[_photoList objectAtIndex:i]];
        pageView.contentMode = UIViewContentModeScaleAspectFill;
        pageView.frame = frame;
        [_pageScroll addSubview:pageView];
    }
}

-(void) viewWillAppear:(BOOL)animated
{
    CGSize pageScrollViewSize = _pageScroll.frame.size;
    _pageScroll.contentSize = CGSizeMake(pageScrollViewSize.width * _photoList.count, pageScrollViewSize.height);
}
```

监控PageControl的方法

```objectivec
- (IBAction)changePage:(id)sender {
    // 更新Scroll View到正确的页面
    CGRect frame;
    frame.origin.x = _pageScroll.frame.size.width * _pageControl.currentPage;
    frame.origin.y = 0;
    frame.size = _pageScroll.frame.size;
    [_pageScroll scrollRectToVisible:frame animated:YES];
}
```

视图滚动的方法

```objectivec
-(void) scrollViewDidScroll:(UIScrollView *)scrollView
{
    CGFloat pageWidth = _pageScroll.frame.size.width;
    // 在滚动超过页面宽度的50%的时候，切换到新的页面
    int page = floor((_pageScroll.contentOffset.x + pageWidth/2)/pageWidth) ;
    _pageControl.currentPage = page;

    if (page >= 3)
    {
        //点击登陆按钮后切换到storyboard界面
        UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboardIOS7Iphone5" bundle:nil];
        [self presentViewController:[storyboard instantiateInitialViewController]
                           animated:YES
                         completion:nil];
    }
}
```

从上面可以看出，其实我是加了一个空白的图片

```objectivec
-(UIImage *)getEmptyUIImage
{
    UIGraphicsBeginImageContextWithOptions(CGSizeMake(_pageScroll.frame.size.width,
                                                      _pageScroll.frame.size.height), NO, 0.0);
    UIImage *blank = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    
    return blank;
    
    
    CGColorSpaceRef colorSpace=CGColorSpaceCreateDeviceRGB();
    
    CGContextRef context=CGBitmapContextCreate(NULL,
                                               _pageScroll.frame.size.width,
                                               _pageScroll.frame.size.height,
                                               0.0,
                                               _pageScroll.frame.size.width*sizeof(uint32_t), colorSpace, kCGBitmapByteOrder32Little|kCGImageAlphaNoneSkipLast);
    [[UIColor clearColor] setFill];
    CGContextSetFillColorWithColor(context, [UIColor clearColor].CGColor);
    
    CGImageRef image=CGBitmapContextCreateImage(context);
    CGContextRelease(context);
    CGColorSpaceRelease(colorSpace);
    UIImage *emptyUIImage=[UIImage imageWithCGImage:image];
    CGImageRelease(image);
    
    return emptyUIImage;
}
```

基本上就可以了。github代码地址：https://github.com/zhangda89/UserGuid.git

---

参考文章

http://www.entlib.net/?p=2627

