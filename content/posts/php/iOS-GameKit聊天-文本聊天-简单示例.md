---
title: "iOS GameKit聊天 文本聊天  简单示例"
date: "2025-06-20 11:50:58"
slug: "ios-gamekit-liao-tian-wen-ben-liao-tian-jian-dan-shi-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/iOS-GameKit聊天-文本聊天-简单示例/"
  - "/2025/06/20/iOS-GameKit聊天-文本聊天-简单示例.html"
  - "/iOS-GameKit聊天-文本聊天-简单示例/"
  - "/iOS-GameKit聊天-文本聊天-简单示例.html"
  - "/2025/06/20/ios-gamekit-liao-tian-wen-ben-liao-tian-jian-dan-shi-li/"
  - "/2025/06/20/ios-gamekit-liao-tian-wen-ben-liao-tian-jian-dan-shi-li.html"
  - "/ios-gamekit-liao-tian-wen-ben-liao-tian-jian-dan-shi-li.html"
---
最近看了一下关于手机蓝牙的相关东西，涉及到了GameKit这个东西，不知道干嘛用的，一眼望过去以为是游戏的东西，不过看过文档后，其实也可以用在游戏中的。不过这里主要是蓝牙这方面的

关于聊天，其实就是就几个过程1，连接；2，传输数据和处理数据

关于这个过程其实我们可以直接自己写一个辅助类来解决就好了

我这边摘录了以为大牛的帮助类

GameKitHelper.h

```objectivec
//
//  GameKitHelper.h
//  Simple GameKit
//
//  Created by david on 13-8-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <GameKit/GameKit.h>

#define DO_DATA_CALLBACK(X, Y) if (self.dataDelegate && [self.dataDelegate respondsToSelector:@selector(X)]) [self.dataDelegate performSelector:@selector(X) withObject:Y];
#define showAlert(format, ...) myShowAlert(__LINE__, (char *)__FUNCTION__, format, ##__VA_ARGS__)
#define BARBUTTON(TITLE, SELECTOR) [[UIBarButtonItem alloc] initWithTitle:TITLE style:UIBarButtonItemStylePlain target:self action:SELECTOR]



@protocol GameKitHelperDataDelegate <NSObject>
@optional
-(void) connectionEstablished;
-(void) connectionLost;
-(void) sentData: (NSString *) errorMessage;
-(void) receivedData: (NSData *)data;
@end


@interface GameKitHelper : NSObject<GKPeerPickerControllerDelegate, GKSessionDelegate>
{
    NSString *sessionID;
    id<GameKitHelperDataDelegate> dataDelegate;
    UIViewController *viewController;
    
    GKSession *session;
    BOOL isConnected;
}

@property (retain) id dataDelegate;
@property (retain) UIViewController *viewController;
@property (retain) NSString *sessionID;
@property (retain) GKSession *session;
@property (assign) BOOL isConnected;

+(void) connect;
+(void) disconnect;
+(void) sendData: (NSData *)data;
+(void) assignViewController: (UIViewController *) aViewController;
+(GameKitHelper *) sharedInstance;
@end
```

GameKitHelper.m

```objectivec
//
//  GameKitHelper.m
//  Simple GameKit
//
//  Created by david on 13-8-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "GameKitHelper.h"

@implementation GameKitHelper
@synthesize dataDelegate;
@synthesize viewController;
@synthesize session;
@synthesize sessionID;
@synthesize isConnected;


//Simple Alert Utility
void myShowAlert(int line, char *functname, id formatstring, ...)
{
    va_list arglist;
    if(!formatstring)return;
    va_start(arglist, formatstring);
    id outstring = [[NSString alloc] initWithFormat:formatstring
                                          arguments:arglist];
    va_end(arglist);
    UIAlertView *av = [[UIAlertView alloc] initWithTitle:outstring
                                                 message:nil
                                                delegate:nil
                                       cancelButtonTitle:@"OK"
                                       otherButtonTitles: nil];
    [av show];
}

#pragma mark - Shared Instance
static GameKitHelper *sharedInstance = nil;

+(GameKitHelper *) sharedInstance
{
    if(!sharedInstance)
    {
        sharedInstance = [[self alloc] init];
    }
    return sharedInstance;
}

#pragma mark - Data Sharing
-(void) sendDataToPeers: (NSData *)data
{
    NSError *error;
    BOOL didSend = [self.session sendDataToAllPeers:data
                                       withDataMode:GKSendDataReliable
                                              error:&error];
    if(!didSend)
    {
        NSLog(@"Error sending data to peers: %@", [error localizedDescription]);
    }
    DO_DATA_CALLBACK(sentData:, (didSend ? nil : [error localizedDescription]));
}

-(void) receiveData:(NSData *)data fromPeer:(NSString *)peer inSession:(GKSession *)session context:(void *)context
{
    DO_DATA_CALLBACK(receivedData:, data);
}

#pragma mark - Connections
-(void) startConnection
{
    if(self.isConnected)
    {
        GKPeerPickerController *picker = [[GKPeerPickerController alloc] init];
        picker.delegate = self;
        picker.connectionTypesMask = GKPeerPickerConnectionTypeNearby;
        [picker show];
        if(self.viewController)
        {
            self.viewController.navigationItem.rightBarButtonItem = nil;
        }
    }
}

//Dismiss the peeer picker on cancel
-(void) peerPickerControllerDidCancel:(GKPeerPickerController *)picker
{
    if(self.viewController)
    {
        self.viewController.navigationItem.rightBarButtonItem = BARBUTTON(@"Connect", @selector(startConnection));
    }
}

-(void) peerPickerController:(GKPeerPickerController *)picker didConnectPeer:(NSString *)peerID toSession:(GKSession *)session
{
    [picker dismiss];
    [self.session setDataReceiveHandler:self
                            withContext:nil];
    isConnected = YES;
    DO_DATA_CALLBACK(connectionEstablished, nil);
}

-(GKSession *) peerPickerController:(GKPeerPickerController *)picker sessionForConnectionType:(GKPeerPickerConnectionType)type
{
    if(!self.session)
    {
        self.session = [[GKSession alloc] initWithSessionID:(self.sessionID ? self.sessionID : @"Sample Session")
                                                displayName:nil
                                                sessionMode:GKSessionModePeer];
        self.session.delegate = self;
    }
    
    return self.session;
    
}

#pragma mark - Session Handling
-(void) disconnect
{
    [self.session disconnectFromAllPeers];
    self.session = nil;
}

-(void) session:(GKSession *)session peer:(NSString *)peerID didChangeState:(GKPeerConnectionState)state
{
    /* STATES: GKPeerStateAvailable, = 0, GKPeerStateUnavailable, = 1, GKPeerStateConnected, = 2,
     GKPeerStateDisconnected, = 3, GKPeerStateConnecting = 4 */
    NSArray *states = [NSArray arrayWithObjects:@"Available", @"Unavailable", @"Connected", @"Disconnected", @"Connecting", nil];
    NSLog(@"Peer state is now %@",[states objectAtIndex:state]);
    
    if(state == GKPeerStateConnected)
    {
        if(self.viewController)
        {
            self.viewController.navigationItem.rightBarButtonItem = BARBUTTON(@"Disconnect", @selector(disconnect));
        }
        
        
        if(state  == GKPeerStateDisconnected)
        {
            self.isConnected = NO;
            showAlert(@"Lost connection with peer. You are no longer connected to another device.");
            [self disconnect];
            if(self.viewController)
            {
                self.viewController.navigationItem.rightBarButtonItem = BARBUTTON(@"Connect", @selector(startConnection));
                DO_DATA_CALLBACK(connectionLost, nil);
            }
        }
    }
    
}

-(void) assignViewController: (UIViewController *)aViewController
{
    self.viewController = aViewController;
    self.viewController.navigationItem.rightBarButtonItem = BARBUTTON(@"Connect", @selector(startConnection));
}

#pragma mark - Class utility methods
+(void) connect
{
    [[self sharedInstance] startConnection];
}

+(void) disconnect
{
    [[self sharedInstance] disconnect];
}

+(void) sendData: (NSData *)data
{
    [[self sharedInstance] sendDataToPeers:data];
}

+(void) assignViewController: (UIViewController *) aViewController
{
    [[self sharedInstance] assignViewController:aViewController];
}



@end
```

然后使用这里类，做了一个简单的示例，我因为就一个iphone，真实的两个手机之间的连接与信息通讯我没有测试过，这个在项目中是不可取的，不过这里我们就是做一个如何来使用这个GameKit的工具，如何实现这个过程，先感受一下，看下面的代码吧：

GameKitHelperViewController.h

```objectivec
//
//  GameKitHelperViewController.h
//  Simple GameKit
//
//  Created by david on 13-8-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GameKitHelper.h"

@interface GameKitHelperViewController : UIViewController<GameKitHelperDataDelegate,UITextViewDelegate>
@property (strong, nonatomic) IBOutlet UITextView *sendView;
@property (strong, nonatomic) IBOutlet UITextView *receviceView;

@end
```

GameKitHelperViewController.m

```objectivec
//
//  GameKitHelperViewController.m
//  Simple GameKit
//
//  Created by david on 13-8-22.
//  Copyright (c) 2013年 WalkerFree. All rights reserved.
//

#import "GameKitHelperViewController.h"
#define COOKBOOK_PURPLE_COLOR    [UIColor colorWithRed:0.20392f green:0.19607f blue:0.61176f alpha:1.0f]


@interface GameKitHelperViewController ()

@end

@implementation GameKitHelperViewController
@synthesize sendView;
@synthesize receviceView;

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    self.navigationController.navigationBar.tintColor = COOKBOOK_PURPLE_COLOR;
    self.navigationItem.leftBarButtonItem = BARBUTTON(@"Clear", @selector(clear));
    
    [GameKitHelper sharedInstance].sessionID = @"Typing Together";
    [GameKitHelper sharedInstance].dataDelegate = self;
    [GameKitHelper assignViewController:self];
    [sendView becomeFirstResponder];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


-(void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    
}

#pragma mark - methods of textview
-(void) textViewDidChange:(UITextView *)textView
{
    if(![GameKitHelper sharedInstance].isConnected)
    {
        return;
    }
    
    NSString *text = self.sendView.text;
    
    if(!text || (text.length == 0))
    {
        text = @"clear";
    }
    NSData *textData = [text dataUsingEncoding:NSUTF8StringEncoding];
    [GameKitHelper sendData:textData];
}

-(void) receivedData:(NSData *)data
{
    NSString *text = [[NSString alloc] initWithData:data
                                           encoding:NSUTF8StringEncoding];
    receviceView.text = [text isEqualToString:@"clear"] ? @"" : text;
}

-(void) clear
{
    sendView.text = @"";
}

@end
```

这里我是使用了storyboard，然后里面加了两个UITextView
