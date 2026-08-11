---
title: "iOS7 视频播放 MPMoviePlayerController"
date: "2025-06-27 10:26:01"
slug: "ios7-shi-pin-bo-fang-mpmovieplayercontroller"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-视频播放-MPMoviePlayerController/"
  - "/2025/06/27/iOS7-视频播放-MPMoviePlayerController.html"
  - "/iOS7-视频播放-MPMoviePlayerController/"
  - "/iOS7-视频播放-MPMoviePlayerController.html"
  - "/2025/06/27/ios7-shi-pin-bo-fang-mpmovieplayercontroller/"
  - "/2025/06/27/ios7-shi-pin-bo-fang-mpmovieplayercontroller.html"
  - "/ios7-shi-pin-bo-fang-mpmovieplayercontroller.html"
---
IOS7 视频播放 需要使用 MPMoviePlayerController

首先是加在一下库文件MediaPlayer.framework

然后实现如下的代码就好了

```objectivec
#pragma mark - 视频播放
-(void) showMovie:(UIGestureRecognizer *)tap
{
    NSLog(@"视频播放");
    UIImageView * nanshanImage=[[UIImageView alloc]initWithFrame:CGRectMake(0,0,1024,699)];
    nanshanImage.image=[UIImage imageNamed:@"boy.jpg"];
    [self.view addSubview:nanshanImage];
    
    UIButton* playButton= [[UIButton alloc]initWithFrame:CGRectMake(145, 250, 70, 80)];
    [playButton addTarget:self action:@selector(PlayMovieAction:) forControlEvents:UIControlEventTouchUpInside];
    playButton.backgroundColor=[UIColor redColor];
    [self.view addSubview:playButton];
}

-(void)PlayMovieAction:(id)sender
{
    
    //视频文件路径，此视频已经存入项目包中。属于本地播放
    NSString *path = [[NSBundle mainBundle] pathForResource:@"jinxiuMovie" ofType:@"mp4"];
    //视频URL
    NSURL *url = [NSURL fileURLWithPath:path];
    //视频播放对象
    MPMoviePlayerController *movie = [[MPMoviePlayerController alloc] initWithContentURL:url];
    movie.controlStyle = MPMovieControlStyleFullscreen;
    [movie.view setFrame:self.view.bounds];
    movie.initialPlaybackTime = -1;
    [self.view addSubview:movie.view];
    // 注册一个播放结束的通知，当播放结束时，监听到并且做一些处理
    //播放器自带有播放结束的通知，在此仅仅只需要注册观察者监听通知即可。
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(myMovieFinishedCallback:)
                                                 name:MPMoviePlayerPlaybackDidFinishNotification
                                               object:movie];
    [movie play];
}

-(void)myMovieFinishedCallback:(NSNotification*)notify
{
    //视频播放对象
    MPMoviePlayerController* theMovie = [notify object];
    //销毁播放通知
    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:MPMoviePlayerPlaybackDidFinishNotification
                                                  object:theMovie];
    [theMovie.view removeFromSuperview];
    // 释放视频对象，此对象由上面建立视频对象时候所alloc,在此做释放操作

    NSLog(@"视频播放完成");
}
```

里面的播放文件是MP4格式的，格式支持：MOV、MP4、M4V、与3GP等格式，还支持多种音频格式。

---

刚开始接触先记录一下

参考文章：

http://www.oschina.net/question/213217\_40625

