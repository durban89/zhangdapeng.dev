---
title: "weiboSDK登录分享"
date: "2025-06-17 18:57:35"
slug: "weibosdk-deng-lu-fen-xiang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/weiboSDK登录分享/"
  - "/2025/06/17/weiboSDK登录分享.html"
  - "/weiboSDK登录分享/"
  - "/weiboSDK登录分享.html"
  - "/2025/06/17/weibosdk-deng-lu-fen-xiang/"
  - "/2025/06/17/weibosdk-deng-lu-fen-xiang.html"
  - "/weibosdk-deng-lu-fen-xiang.html"
---
关于这个分享，也是考虑到很多开发者，在使用的过程中遇到的了很多的问题，对于这种情况我是这么理解的，微博也许是做事不认真吧，也许是我们真的不懂吧，但是我觉得解决问题，能达到自己想要的效果就好了。微博官方的weiboSDK我用的是最新的版本，截止到目前这个时刻，我是用的是最新的，开始的时候，我使用的时候，使用了最初的UIWebView的登录方式，主要是因为，使用客户端的方式，至今不知道什么原理，自己还是慢慢研究吧，呵呵。后来觉得样式不符合自己，于是今天就自己使用UIViewController，在里面使用UIWebView的方式，简单的实现了，至少现在的看起来不会感觉手机的登录看起来怪怪 的。我把代码留在下面：

github代码地址：

<https://github.com/zhangda89/IOS-weiboSDK>

<https://github.com/zhangda89/IOS-StorageData>


```objectivec ThirdPartyLoginController.m
//
//  ThirdPartyLoginController.m
//  xunYi7
//
//  Created by david on 13-7-10.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "ThirdPartyLoginController.h"
#import "UserCenter.h"


@interface ThirdPartyLoginController ()

@end

@implementation ThirdPartyLoginController

@synthesize weiboLoginWeb;
@synthesize indicatorView;
@synthesize authParams;
@synthesize appRedirectURI;
@synthesize sinaWeiboRequest;

@synthesize userID;
@synthesize accessToken;
@synthesize expirationDate;
@synthesize refreshToken;

@synthesize previousOrientation;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
        self.title = @"微博登录";
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    weiboLoginWeb.delegate = self;
    
    indicatorView = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:
                     UIActivityIndicatorViewStyleGray];
    indicatorView.autoresizingMask =
    UIViewAutoresizingFlexibleTopMargin | UIViewAutoresizingFlexibleBottomMargin
    | UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleRightMargin;
    [self.view addSubview:indicatorView];
}

-(void) viewWillAppear:(BOOL)animated{
    self.authParams = [NSMutableDictionary dictionaryWithObjectsAndKeys:
                            kAppKey, @"client_id",
                            @"code", @"response_type",
                            kAppRedirectURI, @"redirect_uri",
                            @"mobile", @"display", nil];
    self.appRedirectURI = kAppRedirectURI;
    self.sinaWeiboRequest = [[SinaWeiboRequest alloc] init];
    sinaWeiboRequest.delegate = self;
    
    [self show];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - SinaWeiboRequestDelegate Methods
- (void)request:(SinaWeiboRequest *)request didReceiveResponse:(NSURLResponse *)response{
    NSLog(@"response = %@",response);

}
- (void)request:(SinaWeiboRequest *)request didReceiveRawData:(NSData *)data{
    NSLog(@"data = %@",data);

}
- (void)request:(SinaWeiboRequest *)request didFailWithError:(NSError *)error{
    NSLog(@"error = %@",error);
}

- (void)request:(SinaWeiboRequest *)request didFinishLoadingWithResult:(id)result{
    NSLog(@"result = %@",result);
    if([UserCenter saveWeiboAuth:result]){
        [self.navigationController popViewControllerAnimated:YES];
    }
    
}

#pragma mark - Activity Indicator
- (void)showIndicator
{
    [indicatorView sizeToFit];
    [indicatorView startAnimating];
    indicatorView.center = weiboLoginWeb.center;
}

- (void)hideIndicator
{
    [indicatorView stopAnimating];
}

#pragma mark - Show / Hide
- (void)load{
    NSString *authPagePath = [SinaWeiboRequest serializeURL:kSinaWeiboWebAuthURL
                                                     params:authParams httpMethod:@"GET"];
    [weiboLoginWeb loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:authPagePath]]];
}

- (void)show
{
    [self load];
    [self showIndicator];
    [self addObservers];
}

- (void)hide
{
    [self removeObservers];
    
    [weiboLoginWeb stopLoading];
    
}

- (void)cancel
{
    [self hide];
}

#pragma mark - UIDeviceOrientationDidChangeNotification Methods
- (void)deviceOrientationDidChange:(id)object
{
	
}


#pragma mark Obeservers
- (void)addObservers
{
	[[NSNotificationCenter defaultCenter] addObserver:self
											 selector:@selector(deviceOrientationDidChange:)
												 name:@"UIDeviceOrientationDidChangeNotification" object:nil];
}

- (void)removeObservers{
	[[NSNotificationCenter defaultCenter] removeObserver:self
													name:@"UIDeviceOrientationDidChangeNotification" object:nil];
}


#pragma mark - UIWebView Delegate

- (void)webViewDidFinishLoad:(UIWebView *)aWebView{
	[self hideIndicator];
}

- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error{
    [self hideIndicator];
}


- (BOOL)webView:(UIWebView *)aWebView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType{
    NSString *url = request.URL.absoluteString;
    
    NSString *siteRedirectURI = [NSString stringWithFormat:@"%@%@", kSinaWeiboSDKOAuth2APIDomain, appRedirectURI];
    
    if ([url hasPrefix:appRedirectURI] || [url hasPrefix:siteRedirectURI]){
        NSString *error_code = [SinaWeiboRequest getParamValueFromUrl:url paramName:@"error_code"];
        
        if (error_code){
            NSString *error = [SinaWeiboRequest getParamValueFromUrl:url paramName:@"error"];
            NSString *error_uri = [SinaWeiboRequest getParamValueFromUrl:url paramName:@"error_uri"];
            NSString *error_description = [SinaWeiboRequest getParamValueFromUrl:url paramName:@"error_description"];
            
            NSDictionary *errorInfo = [NSDictionary dictionaryWithObjectsAndKeys:
                                       error, @"error",
                                       error_uri, @"error_uri",
                                       error_code, @"error_code",
                                       error_description, @"error_description", nil];
            NSLog(@"errorInfo = %@",errorInfo);
            
            [self hide];
            
        }else{
            NSString *code = [SinaWeiboRequest getParamValueFromUrl:url paramName:@"code"];
            if (code){
                [self hide];
                
                NSDictionary *params = [NSDictionary dictionaryWithObjectsAndKeys:
                                        kAppKey, @"client_id",
                                        kAppSecret, @"client_secret",
                                        @"authorization_code", @"grant_type",
                                        self.appRedirectURI, @"redirect_uri",
                                        code, @"code", nil];
                
                
                [sinaWeiboRequest disconnect];
                sinaWeiboRequest = nil;
                
                self.sinaWeiboRequest = [SinaWeiboRequest requestWithURL:kSinaWeiboWebAccessTokenURL
                                                 httpMethod:@"POST"
                                                     params:params
                                                   delegate:self];
                
                
                [sinaWeiboRequest connect];
            }
        }
        
        return NO;
    }
    
    return YES;
}

/**
 * @description 清空认证信息
 */
- (void)removeAuthData{
//    NSHTTPCookieStorage* cookies = [NSHTTPCookieStorage sharedHTTPCookieStorage];
//    NSArray* sinaweiboCookies = [cookies cookiesForURL:
//                                 [NSURL URLWithString:@"https://open.weibo.cn"]];
//    
//    for (NSHTTPCookie* cookie in sinaweiboCookies)
//    {
//        [cookies deleteCookie:cookie];
//    }
}
/**
 * @description 判断是否登录
 * @return YES为已登录；NO为未登录
 */
- (BOOL)isLoggedIn
{
    return userID && accessToken && expirationDate;
}

/**
 * @description 判断登录是否过期
 * @return YES为已过期；NO为未为期
 */
- (BOOL)isAuthorizeExpired
{
    NSDate *now = [NSDate date];
    return ([now compare:expirationDate] == NSOrderedDescending);
}


/**
 * @description 判断登录是否有效，当已登录并且登录未过期时为有效状态
 * @return YES为有效；NO为无效
 */
- (BOOL)isAuthValid
{
    return ([self isLoggedIn] && ![self isAuthorizeExpired]);
}
@end
```

```objectivec ThirdPartyLoginController.h
//
//  ThirdPartyLoginController.h
//  xunYi7
//
//  Created by david on 13-7-10.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "SinaWeiboRequest.h"
#import "SinaWeibo.h"
#import "SinaWeiboConstants.h"
#import <QuartzCore/QuartzCore.h>

#define kAppKey             @"xxxxxxxxx"
#define kAppSecret          @"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#define kAppRedirectURI     @"https://api.weibo.com/oauth2/default.html"

#ifndef kAppKey
#error
#endif

#ifndef kAppSecret
#error
#endif

#ifndef kAppRedirectURI
#error
#endif

@interface ThirdPartyLoginController : UIViewController<UIWebViewDelegate, SinaWeiboDelegate, SinaWeiboRequestDelegate>


@property (strong, nonatomic) IBOutlet UIWebView *weiboLoginWeb;
@property (retain, nonatomic) UIActivityIndicatorView *indicatorView;
@property (retain, nonatomic) NSDictionary *authParams;
@property (retain, nonatomic) NSString *appRedirectURI;
@property (retain, nonatomic) SinaWeiboRequest *sinaWeiboRequest;

@property (nonatomic, retain) NSString *userID;
@property (nonatomic, retain) NSString *accessToken;
@property (nonatomic, retain) NSDate *expirationDate;
@property (nonatomic, retain) NSString *refreshToken;

@property (nonatomic) UIInterfaceOrientation previousOrientation;

@end
```

还有一个简单的管理微博用户登录的信息的方法，很简单的


```objectivec UserCenter.h
//
//  UserCenter.h
//  xunYi7
//
//  Created by david on 13-7-10.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface UserCenter : NSObject
+(BOOL)saveWeiboAuth:(NSDictionary *)params;
+(NSDate *)fetchWeiboExpireDate;
+(NSString *)fetchWeiboAccessToken;
+(NSString *)fetchWeiboUid;
+(BOOL)isOutDate;
+(void)removeWeiboAuthCookieData;
+(void)removeWeiboAuthData;
@end
```

```objectivec UserCenter.m
//
//  UserCenter.m
//  xunYi7
//
//  Created by david on 13-7-10.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "UserCenter.h"

@implementation UserCenter

/**
 * @description 存储微博登录的信息
 */
+(BOOL)saveWeiboAuth:(NSDictionary *)params{
    NSDictionary *authData = [NSDictionary dictionaryWithObjectsAndKeys:
                              [params objectForKey:@"access_token"], @"AccessTokenKey",
                              [params objectForKey:@"expires_in"], @"ExpirationDateKey",
                              [params objectForKey:@"uid"], @"UserIDKey",
                              [params objectForKey:@"access_token"], @"refresh_token", nil];
    [[NSUserDefaults standardUserDefaults] setObject:authData forKey:@"SinaWeiboAuthData"];
    [[NSUserDefaults standardUserDefaults] synchronize];
    
    
    //微博的时间戳的转换
    NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
    NSLog(@"ExpirationDateKey = %@",[[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"]);
    return YES;
}

/**
 * @description 获取微博登录的过期时间
 */
+(NSDate *)fetchWeiboExpireDate{
    NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
    if([accountDefaults objectForKey:@"SinaWeiboAuthData"] != nil){
        return [[accountDefaults objectForKey:@"SinaWeiboAuthData"] valueForKey:@"ExpirationDateKey"];
    }
    return nil;
}

/**
 * @description 获取微博登录的AccessToken
 */
+(NSString *)fetchWeiboAccessToken{
    NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
    if([accountDefaults objectForKey:@"SinaWeiboAuthData"] != nil){
        return [[accountDefaults objectForKey:@"SinaWeiboAuthData"] valueForKey:@"AccessTokenKey"];
    }
    return nil;
}

/**
 * @description 获取登录的微博用户的id
 */
+(NSString *)fetchWeiboUid{
    NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
    if([accountDefaults objectForKey:@"SinaWeiboAuthData"] != nil){
        return [[accountDefaults objectForKey:@"SinaWeiboAuthData"] valueForKey:@"UserIDKey"];
    }
    return nil;
}

/**
 * @description 判断是否过期
 */
+(BOOL)isOutDate{
    //现在时刻的时间戳
    NSDate *newDate =[NSDate date];
    NSString *timeStamp =[NSString stringWithFormat:@"%lu", (long)[newDate timeIntervalSince1970]];
    
    //微博的时间戳的转换
    NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
    
    
    if([accountDefaults objectForKey:@"SinaWeiboAuthData"] == nil){
        return YES;
    }
    
    if([[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"] == nil){
        return YES;
    }
    
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd HH:mm:ss ZZZ"];
    NSDate *weiBoDate = [dateFormatter dateFromString:[NSString stringWithFormat:@"%@",[[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"]]];
    
    NSLog(@"weiBoDate ExpirationDateKey = %@",[[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"]);
//    NSString *weiBoDateStamp = [NSString stringWithFormat:@"%lu", (long) [weiBoDate timeIntervalSince1970]];
    NSString *weiBoDateStamp = [NSString stringWithFormat:@"%@",[[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"]];
    
    
    
    NSLog(@"weiBoDateStamp=%@, timeStamp = %@",[[accountDefaults objectForKey:@"SinaWeiboAuthData"] objectForKey:@"ExpirationDateKey"],timeStamp);
    if([timeStamp compare:weiBoDateStamp] < 0){//未过期
        return NO;
    }else{//已经过期
        [self removeWeiboAuthData];
        return YES;
    }
    return NO;
}

/**
 * @description 移出微博的登录的cookie信息
 */
+(void)removeWeiboAuthCookieData{
    NSHTTPCookieStorage* cookies = [NSHTTPCookieStorage sharedHTTPCookieStorage];
    NSArray* sinaweiboCookies = [cookies cookiesForURL:
                                 [NSURL URLWithString:@"https://open.weibo.cn"]];
    
    for (NSHTTPCookie* cookie in sinaweiboCookies)
    {
        [cookies deleteCookie:cookie];
    }
}


/**
 * @description 移出微博的登录的信息
 */
+(void)removeWeiboAuthData{
    [[NSUserDefaults standardUserDefaults] removeObjectForKey:@"SinaWeiboAuthData"];
}
@end
```
