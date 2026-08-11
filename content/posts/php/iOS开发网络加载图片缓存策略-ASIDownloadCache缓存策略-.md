---
title: "iOS开发网络加载图片缓存策略(ASIDownloadCache缓存策略)"
date: "2025-06-17 12:01:09"
slug: "ios-kai-fa-wang-luo-jia-zai-tu-pian-huan-cun-ce-lve-asidownloadcache-huan-cun-ce-lve"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS开发网络加载图片缓存策略(ASIDownloadCache缓存策略)/"
  - "/2025/06/17/iOS开发网络加载图片缓存策略(ASIDownloadCache缓存策略).html"
  - "/iOS开发网络加载图片缓存策略(ASIDownloadCache缓存策略)/"
  - "/iOS开发网络加载图片缓存策略(ASIDownloadCache缓存策略).html"
  - "/2025/06/17/iOS开发网络加载图片缓存策略-ASIDownloadCache缓存策略/"
  - "/2025/06/17/iOS开发网络加载图片缓存策略-ASIDownloadCache缓存策略.html"
  - "/2025/06/17/ios-kai-fa-wang-luo-jia-zai-tu-pian-huan-cun-ce-lve-asidownloadcache-huan-cun-ce-lve/"
  - "/2025/06/17/ios-kai-fa-wang-luo-jia-zai-tu-pian-huan-cun-ce-lve-asidownloadcache-huan-cun-ce-lv.html"
  - "/ios-kai-fa-wang-luo-jia-zai-tu-pian-huan-cun-ce-lve-asidownloadcache-huan-cun-ce-lve.html"
---
很多情况需要从网络上加载图片，然后将图片在imageview中显示出来，但每次都要从网络上请求，会严重影响用户体验，为了不是每次显示都需要从网上下载数据，希望将图片放到本地缓存，因此我们需要一个好的的缓存策略，今天我将我在项目工程中的实际经验分享给大家，我这里主要介绍一下强大的ASIHTTPRequest的缓存策略，以及使用方法：

下面是具体步骤：  
一、设置缓存策略  
首先在SplitDemoAppDelegate委托代理中，实现如下代码：  
在SplitDemoAppDelegate.h文件中，代码如下：

```objectivec
#import <UIKit/UIKit.h>
@class ASIDownloadCache;

@interface SplitDemoAppDelegate : NSObject <UIApplicationDelegate,UITabBarControllerDelegate> {

    UIWindow *_window;

    ASIDownloadCache*_downloadCache;            //下载缓存策略

}

@property (nonatomic, retain) ASIDownloadCache*downloadCache;

@end
```

在SplitDemoAppDelegate.m文件中，代码如下:

```objectivec
#import "SplitDemoAppDelegate.h"
 
@implementation SplitDemoAppDelegate

@synthesize window=_window;

@synthesize downloadCache = _downloadCache;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions

{

    //初始化ASIDownloadCache缓存对象

    ASIDownloadCache *cache = [[ASIDownloadCache alloc] init];

    self.downloadCache = cache;

    [cache release];

    //路径

    NSArray *paths =NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,NSUserDomainMask, YES);

    NSString *documentDirectory = [paths objectAtIndex:0];

    //设置缓存存放路径

    [self.downloadCache setStoragePath:[documentDirectorystringByAppendingPathComponent:@"resource"]];

    //设置缓存策略

    [self.downloadCache setDefaultCachePolicy:ASIOnlyLoadIfNotCachedCachePolicy];

    // Override point for customization after application launch.

    [self.window makeKeyAndVisible];

    return YES;

}


- (void)dealloc

{

    [_window release];

    [_downloadCache release];

    [super dealloc];

}
@end
```

二、创建缓存线程  
  
这一步是创建一个NSOperation类，实现缓存的方法，代码如下：  
  
ResourceContainer.h文件实现

```objectivec
#import <Foundation/Foundation.h>

#import "ASIHTTPRequest.h"

#import "SplitDemoAppDelegate.h"

@interface ResourceContainer : NSOperation {

NSURL*_resourceURL;            //资源请求url

NSObject*_hostObject;             

SEL_resourceDidReceive;      //资源接手响应方法  

SplitDemoAppDelegate*_appDelegate;            //应用委托对象

ASIHTTPRequest*_httpRequest;            

UIImageView*_imageView;              

}

@property (nonatomic, retain) NSURL*resourceURL;

@property (nonatomic, retain) NSObject*hostObject;

@property (nonatomic, assign) SELresourceDidReceive;

@property (nonatomic, assign) SplitDemoAppDelegate   *appDelegate;

@property (nonatomic, retain) ASIHTTPRequest*httpRequest;

@property (nonatomic, retain) UIImageView*imageView;

//http请求回调方法

-(void)didStartHttpRequest:(ASIHTTPRequest *)request;

-(void)didFinishHttpRequest:(ASIHTTPRequest *)request;

-(void)didFailedHttpRequest:(ASIHTTPRequest *)request;

//取消资源请求

-(void)cancelReourceGet;

//资源接收回调方法

-(void)resourceDidReceive:(NSData *)resource;

@end
```

ResourceContainer.m文件实现：

```objectivec
#import "ResourceContainer.h"
#import "HttpConstant.h"
#import "ASIDownloadCache.h"
@implementation ResourceContainer
@synthesize resourceURL = _resourceURL;
@synthesize hostObject = _hostObject;
@synthesize resourceDidReceive = _resourceDidReceive;
@synthesize appDelegate = _appDelegate;
@synthesize httpRequest = _httpRequest;
@synthesize imageView = _imageView;

-(id)init{

    if(self == [super init]){
        self.appDelegate = (SplitDemoAppDelegate *)[[UIApplication sharedApplication] delegate];
    }
    return self;
}


-(void)main{

    if(self.hostObject == nil)
    return;

    if(self.resourceURL == nil){
        [self resourceDidReceive:nil];
        return;
    }

    ASIHTTPRequest *request = [ASIHTTPRequest     requestWithURL:self.resourceURL]
    self.httpRequest = request;



    [self.httpRequest setDownloadCache:self.appDelegate.downloadCache];
    [self.httpRequest setDelegate:self];
    [self.httpRequest setDidStartSelector:@selector(didStartHttpRequest:)];
    [self.httpRequest setDidFinishSelector:@selector(didFinishHttpRequest:)];
    [self.httpRequest setDidFailSelector:@selector(didFailedHttpRequest:)];

    //发异步请求

    [self.httpRequest startAsynchronous];

}

- (void)dealloc {

    [_resourceURL release];
    [_hostObject release];
    [_httpRequest release];
    [_imageView release];
    [super dealloc];

}

//开始请求

-(void)didStartHttpRequest:(ASIHTTPRequest *)request{

    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:YES];

}

//请求成功返回处理结果

-(void)didFinishHttpRequest:(ASIHTTPRequest *)request{

    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:NO];

    if([request responseStatusCode] == 200 || [request responseStatusCode] == 304){

        //判断是否来自缓存

        if([request didUseCachedResponse]){
            NSLog(@"=========资源请求：%@ 来自缓存============",[self.resourceURL absoluteURL]);
        }
        else{
            NSLog(@"=========资源请求：图片不来自缓存============");
        }
        [self resourceDidReceive:[request responseData]];

    }
    else
    {

        [self resourceDidReceive:nil];

    }

}

//失败请求返回处理结果

-(void)didFailedHttpRequest:(ASIHTTPRequest *)request{

    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:NO];

    [self resourceDidReceive:nil];

}

//取消资源请求

-(void)cancelReourceGet{

    [self.httpRequest cancel];

}

//资源接收处理方法

-(void)resourceDidReceive:(NSData *)resource{

    if([self.hostObject respondsToSelector:self.resourceDidReceive]){

        if(resource != nil && self.imageView != nil){

            self.imageView.image = [UIImage imageWithData:resource];

        }

        [self.hostObject performSelectorOnMainThread:self.resourceDidReceive withObject:self.imageViewwaitUntilDone:NO];

    }

}
@end
```

到第二步，我们的缓存策略的设置，以及资源请求和接收数据方法已经构建完毕，下面介绍一下如何使用我们上面创建的NSOperation类  
三、图片请求（利用上面创建的类）  
这里以我的工程为例进行分析：  
在DetailViewController.h声明文件中:

```objectivec
#import <UIKit/UIKit.h>

@interface DetailViewController :UIViewController {

    NSURL                         *_imageURL;                    //图片url

    NSMutableArray            *_originalIndexArray;        //保存请求图片的号

    NSMutableDictionary     *_originalOperationDic;     //保存图片请求队列

    NSOperationQueue        *_requestImageQueue;    //图片请求队列

}

@property (nonatomic, retain) NSURL                       *imageURL;
@property (nonatomic, retain) NSMutableArray          *originalIndexArray;
@property (nonatomic, retain) NSMutableDictionary   *originalOperationDic;
@property (nonatomic, retain) NSOperationQueue      * requestImageQueue;

//显示图片信息

-(void)displayProductImage;

//根据图片序号显示请求图片资源

-(void)displayImageByIndex:(NSInteger)index ByImageURL:(NSURL *)url;

//处理图片请求返回信息

-(void)imageDidReceive:(UIImageView *)imageView;

@end
```

在DetailViewController.m实现文件中:

```objectivec
#import "ProductDetailViewController.h"
//这里引入在第二步中，我们创建的对象
#import "ResourceContainer.h"

@implementation DetailViewController
@synthesize imageURL = _imageURL;
@synthesize originalIndexArray = _originalIndexArray;
@synthesize originalOperationDic = _originalOperationDic;
@synthesize requestImageQueue = _requestImageQueue;


- (void)viewDidLoad
{

    [super viewDidLoad];
    NSOperationQueue *tempQueue = [[NSOperationQueue alloc] init];

    self.requsetImageQueue = tempQueue;
    [tempQueue release];

    NSMutableArray *array = [[NSMutableArray alloc] init];

    self.originalIndexArray = array;
    [array release];

    NSMutableDictionary *dic = [[NSMutableDictionary alloc] init];

    self.originalOperationDic = dic;
    [dic release];

}

//显示图片信息

-(void)displayProductImage
{
    NSURL *url = [NSURL URLWithString:@"http://xxx.xxx.xxx.xxx"];

    //这个是从器返回有图片数目，self.xxxx根据具体的场合

    int imageCount = [self.xxxx.imageNum intValue];

    for (int i=0; i<imageCount; i++) {

        NSString *str1 = @"这里是拼图片请求url，根据实际需求";

        self.imageURL = [url URLByAppendingPathComponent:str1];

        //根据图片号请求资源

        [self displayImageByIndex:i ByImageURL:self.productImageURL];

    }

}

//根据图片序号显示请求图片资源

-(void) displayImageByIndex:(NSInteger)index ByImageURL:(NSURL *)url

{

 NSString *indexForString = [NSString stringWithFormat:@"%d",index];

 //若数组中已经存在该图片编号，说明图片加载完毕，直接返回

 if ([self.originalIndexArray containsObject:indexForString]) {

      return;

 }

 //创建UIImageView对象

 UIImageView *imageView = [[UIImageView alloc] init];

 imageView.tag = index;

 //创建资源请求对象

 ResourceContainer  *imageOperation = [[ResourceContainer alloc] init];

 imageOperation.resourceURL = url;

 imageOperation.hostObject = self;

 //设置收到图片信息处理理方法

 imageOperation.resourceDidReceive = @selector(imageDidReceive:);

 imageOperation.imageView = imageView;

 [imageView release];

 //将图片请求对象加入图片请求队列中

 [self.requsetImageQueue addOperation:imageOperation];

 [self.originalOperationDic setObject:imageOperation forKey:indexForString];

 [imageOperation release];

}
 
//处理图片请求返回信息

-(void)imageDidReceive:(UIImageView *)imageView
{

    if (imageView == nil||imageView.image == nil) {
        imageView.image = [UIImage imageNamed:@"no-pic-300-250.png"];
    }
    //将图片信息加载到前台，self.openFlowView是我用的coverFlow，coverFlow的使用方法网上很多，自己找吧

    [self.openFlowView setImage:imageView.image forIndex:imageView.tag];

    [self.originalIndexArray addObject:[NSString stringWithFormat:@"%d",imageView.tag]];

    [self.originalOperationDic removeObjectForKey:[NSString stringWithFormat:@"%d",imageView.tag]];
}
 
- (void)dealloc
{
    [_requestImageQueue release];

    [_originalIndexArray release];

    [_originalOperationDic release];

    [_imageURL release];

    [super dealloc];
}
 
@end
```

经过上述步骤，我们实现了加载网络图片时缓存功能，增强了用户体验效果。  
参考:http://www.cnblogs.com/pengyingh/articles/2343061.html
