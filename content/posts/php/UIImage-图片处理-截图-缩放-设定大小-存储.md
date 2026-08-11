---
title: "UIImage 图片处理：截图，缩放，设定大小，存储"
date: "2025-06-25 09:57:50"
slug: "uiimage-tu-pian-chu-li-jie-tu-suo-fang-she-ding-da-xiao-cun-chu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/UIImage-图片处理：截图，缩放，设定大小，存储/"
  - "/2025/06/25/UIImage-图片处理：截图，缩放，设定大小，存储.html"
  - "/UIImage-图片处理：截图，缩放，设定大小，存储/"
  - "/UIImage-图片处理：截图，缩放，设定大小，存储.html"
  - "/2025/06/25/UIImage-图片处理-截图-缩放-设定大小-存储/"
  - "/2025/06/25/UIImage-图片处理-截图-缩放-设定大小-存储.html"
  - "/2025/06/25/uiimage-tu-pian-chu-li-jie-tu-suo-fang-she-ding-da-xiao-cun-chu/"
  - "/2025/06/25/uiimage-tu-pian-chu-li-jie-tu-suo-fang-she-ding-da-xiao-cun-chu.html"
  - "/uiimage-tu-pian-chu-li-jie-tu-suo-fang-she-ding-da-xiao-cun-chu.html"
---
图片的处理大概分 截图(capture),  缩放(scale), 设定大小(resize),  存储(save)

1.等比率缩放

```objectivec
- (UIImage *)scaleImage:(UIImage *)image toScale:(float)scaleSize
{
    UIGraphicsBeginImageContext(CGSizeMake(image.size.width * scaleSize, image.size.height * scaleSize);
    [image drawInRect:CGRectMake(0, 0, image.size.width * scaleSize, image.size.height * scaleSize)];
    UIImage *scaledImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return scaledImage;
}
```

2.自定长宽

```objectivec
- (UIImage *)reSizeImage:(UIImage *)image toSize:(CGSize)reSize
{
    UIGraphicsBeginImageContext(CGSizeMake(reSize.width, reSize.height));
    [image drawInRect:CGRectMake(0, 0, reSize.width, reSize.height)];
    UIImage *reSizeImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return reSizeImage;
}
```

3.处理某个特定View

只要是继承UIView的object 都可以处理

必须先import QuzrtzCore.framework

```objectivec
-(UIImage*)captureView:(UIView *)theView
{
    CGRect rect = theView.frame;
    UIGraphicsBeginImageContext(rect.size);
    CGContextRef context = UIGraphicsGetCurrentContext();
    [theView.layer renderInContext:context];
    UIImage *img = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return img;
}
```

4.储存图片

储存图片这里分成储存到app的文件里和储存到手机的图片库里

1) 储存到app的文件里

```objectivec
NSString *path = [[NSHomeDirectory()stringByAppendingPathComponent:@"Documents"]stringByAppendingPathComponent:@"image.png"];
[UIImagePNGRepresentation(image) writeToFile:pathatomically:YES];
```

把要处理的图片, 以image.png名称存到app home下的Documents目录里

2)储存到手机的图片库里(必须在真机使用，模拟器无法使用)

```objectivec
CGImageRef screen = UIGetScreenImage();
UIImage* image = [UIImage imageWithCGImage:screen];
CGImageRelease(screen);
UIImageWriteToSavedPhotosAlbum(image, self, nil, nil);
UIGetScreenImage(); // 原来是private(私有)api, 用来截取整个画面,不过SDK 4.0后apple就开放了
```

//====================================================================

以下代码用到了Quartz Framework 和 Core Graphics Framework. 在workspace的framework目录里添加这两个framework.在UIKit里，图像类UIImage和CGImageRef的画图操作都是通过Graphics Context来完成。Graphics Context封装了变换的参数，使得在不同的坐标系里操作图像非常方便。缺点就是，获取图像的数据不是那么方便。下面会给出获取数据区的代码。

1. 从UIView中获取图像相当于窗口截屏。

(ios提供全局的全屏截屏函数UIGetScreenView(). 如果需要特定区域的图像，可以crop一下)

```objectivec
CGImageRef screen = UIGetScreenImage();
UIImage* image = [UIImage imageWithCGImage:screen];
```

2. 对于特定UIView的截屏。

（可以把当前View的layer，输出到一个ImageContext中，然后利用这个ImageContext得到UIImage）

```objectivec
-(UIImage*)captureView: (UIView *)theView
{
    CGRect rect = theView.frame;
    UIGraphicsBeginImageContext(rect.size);
    CGContextRef context =UIGraphicsGetCurrentContext();
    [theView.layer renderInContext:context];
    UIImage *img = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    return img;
}
```

3. 如果需要裁剪指定区域。

（可以path & clip，以下例子是建一个200x200的图像上下文，再截取出左上角）

```objectivec
UIGraphicsBeginImageContext(CGMakeSize(200,200));
CGContextRefcontext=UIGraphicsGetCurrentContext();
UIGraphicsPushContext(context);
// ...把图写到context中，省略[indent]CGContextBeginPath();
CGContextAddRect(CGMakeRect(0,0,100,100));
CGContextClosePath();[/indent]CGContextDrawPath();
CGContextFlush(); // 强制执行上面定义的操作
UIImage* image = UIGraphicGetImageFromCurrentImageContext();
UIGraphicsPopContext();
```

4. 存储图像。

（分别存储到home目录文件和图片库文件。）

存储到目录文件是这样

```objectivec
NSString *path = [[NSHomeDirectory() stringByAppendingPathComponent:@"Documents"] stringByAppendingPathComponent:@"image.png"];
[UIImagePNGRepresentation(image) writeToFile:path atomically:YES];
```

若要存储到图片库里面

```objectivec
UIImageWriteToSavedPhotosAlbum(image, nil, nil, nil);
```

5.  互相转换UImage和CGImage。

（UImage封装了CGImage, 互相转换很容易）

```objectivec
UIImage* imUI=nil;
CGImageRef imCG=nil;
imUI = [UIImage initWithCGImage:imCG];
imCG = imUI.CGImage;
```

6. 从CGImage上获取图像数据区。

（在apple dev上有QA, 不过好像还不支持ios）

下面给出一个在ios上反色的例子

```objectivec
-(id)invertContrast:(UIImage*)img
{
    CGImageRef inImage = img.CGImage;
    CGContextRef ctx;
    CFDataRef m_DataRef;
    m_DataRef = CGDataProviderCopyData(CGImageGetDataProvider(inImage));
    int width = CGImageGetWidth( inImage );
    int height = CGImageGetHeight( inImage );
    int bpc = CGImageGetBitsPerComponent(inImage);
    int bpp = CGImageGetBitsPerPixel(inImage);
    int bpl = CGImageGetBytesPerRow(inImage);
    UInt8 * m_PixelBuf = (UInt8 *) CFDataGetBytePtr(m_DataRef);
    int length = CFDataGetLength(m_DataRef);
    NSLog(@"len %d", length);
    NSLog(@"width=%d, height=%d", width, height);
    NSLog(@"1=%d, 2=%d, 3=%d", bpc, bpp,bpl);
    for (int index = 0; index < length; index += 4)
    { 
        m_PixelBuf[index + 0] = 255 - m_PixelBuf[index + 0];// b
        m_PixelBuf[index + 1] = 255 - m_PixelBuf[index + 1];// g
        m_PixelBuf[index + 2] = 255 - m_PixelBuf[index + 2];// r
    }
    ctx = CGBitmapContextCreate(m_PixelBuf, width, height, bpb, bpl, CGImageGetColorSpace( inImage ), kCGImageAlphaPremultipliedFirst );
    CGImageRef imageRef = CGBitmapContextCreateImage (ctx);
    UIImage* rawImage = [UIImage imageWithCGImage:imageRef];
    CGContextRelease(ctx);
    return rawImage;
}
```

7. 显示图像数据区。

（显示图像数据区，也就是`unsigned char*`转为`graphics context`或者`UIImage`或和`CGImageRef`）

```objectivec
CGContextRef ctx = CGBitmapContextCreate(pixelBuf,width,height, bitsPerComponent,bypesPerLine, colorSpace,kCGImageAlphaPremultipliedLast );
CGImageRef imageRef = CGBitmapContextCreateImage (ctx);
UIImage* image = [UIImage imageWithCGImage:imageRef];
NSString* path = [[NSHomeDirectory() stringByAppendingPathComponent:@"Documents"] stringByAppendingPathComponent:@"ss.png"];
[UIImagePNGRepresentation(self.image) writeToFile:path atomically:YES];
CGContextRelease(ctx);
```

得到图像数据区后就可以很方便的实现图像处理的算法。

