---
title: "NSNotification广播实现视图跳转传递数据"
date: "2025-06-19 09:58:19"
slug: "nsnotification-guang-bo-shi-xian-shi-tu-tiao-zhuan-chuan-di-shu-ju"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/NSNotification广播实现视图跳转传递数据/"
  - "/2025/06/19/NSNotification广播实现视图跳转传递数据.html"
  - "/NSNotification广播实现视图跳转传递数据/"
  - "/NSNotification广播实现视图跳转传递数据.html"
  - "/2025/06/19/nsnotification-guang-bo-shi-xian-shi-tu-tiao-zhuan-chuan-di-shu-ju/"
  - "/2025/06/19/nsnotification-guang-bo-shi-xian-shi-tu-tiao-zhuan-chuan-di-shu-ju.html"
  - "/nsnotification-guang-bo-shi-xian-shi-tu-tiao-zhuan-chuan-di-shu-ju.html"
---
NSNotification广播实现视图跳转传递数据  
广播机制分为：注册->发送->接收(接收方)  
第一步，在要发送数据的视图页面.m文件处理发送逻辑的方法里注册+发送

```objectivec
- (IBAction)pressed:(id)sender {
    
//    [self performSegueWithIdentifier:@"second" sender:self];
    NSLog(@"send message:%@",firstField.text);

    
    
    //页面跳转传值方法二：利用notification
    NSDictionary *dicts = [NSDictionary dictionaryWithObjectsAndKeys:@"one1",@"one",@"two2",@"two",@"three3",@"three", nil];
    //注册(第一步)
    NSNotification *notification  =[NSNotification notificationWithName:@"mynotification" object:firstField.text];
    //发送（第二步）
    [[NSNotificationCenter defaultCenter] postNotification:notification];
    
    //注册+发送也可以一行完成(等效于以上两行)
    [[NSNotificationCenter defaultCenter] postNotificationName:@"mynotification2" object:dicts];//发送一个字典过去
}
```

notificationWithName:参数的值是自己定义，接收方以此名称为接收标识。  
第二步，在跳转后，接收数据视图页面.m文件中处理逻辑的方法里 接收

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    //接受端：接受（第一步）
   
 [[NSNotificationCenter defaultCenter] addObserver:self 
selector:@selector(notificationHandler:) name:@"mynotification" 
object:nil];
    
    
    [[NSNotificationCenter 
defaultCenter] addObserver:self 
selector:@selector(notificationHandler2:) name:@"mynotification2" 
object:nil];

}
//自定义接收信息和处理的方法（第二步）
-(void) notificationHandler:(NSNotification *) notification{
    
    secondField.text = [notification object];//收到消息后在UItextField中显示出来

}
//自定义接收字典信息的方法
-(void) notificationHandler2:(NSNotification *) notification2{

    NSDictionary *dict = [notification2 object];
     NSLog(@"receive dict :%@,forkey:%@",dict,[dict objectForKey:@"one"]);

}
```

注意：如果注册的notification在目标视图没有收到或名称写错，目标视图的相关方法就不会执行
