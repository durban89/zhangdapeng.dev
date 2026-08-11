---
title: "iOS NSURLConnection 同步下载获取数据"
date: "2025-06-10 15:14:52"
slug: "ios-nsurlconnection-tong-bu-xia-zai-huo-qu-shu-ju"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-NSURLConnection-同步下载获取数据/"
  - "/2025/06/10/iOS-NSURLConnection-同步下载获取数据.html"
  - "/iOS-NSURLConnection-同步下载获取数据/"
  - "/iOS-NSURLConnection-同步下载获取数据.html"
  - "/2025/06/10/ios-nsurlconnection-tong-bu-xia-zai-huo-qu-shu-ju/"
  - "/2025/06/10/ios-nsurlconnection-tong-bu-xia-zai-huo-qu-shu-ju.html"
  - "/ios-nsurlconnection-tong-bu-xia-zai-huo-qu-shu-ju.html"
---
同步下载（交互不好，容易出现卡死现象，一般下载数据较小或有特定需求才使用）。  发送同步请求后，程序将停止用户交互，直到服务器返回数据完成后，才进行下一步的操作。  
  
步骤：

### [创建NSURL](#1)

```objectivec
NSURL *url = [[NSURL alloc] initWithString:@"http://www.baidu.com/"];
```

### [通过URL创建NSURLRequest](#2)

```objectivec
NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval:15];
```

cachePolicy 缓存协议是个枚举类型：  
  
NSURLRequestUseProtocolCachePolicy 基础策略  
  
NSURLRequestReloadIgnoringLocalCacheData 忽略本地缓存  
  
NSURLRequestReturnCacheDataElseLoad 首先使用缓存，如果没有本地缓存，才从原地址下载  
  
NSURLRequestReturnCacheDataDontLoad 使用本地缓存，从不下载，如果本地没有缓存，则请求失败。此策略多用于离线操作  
  
NSURLRequestReloadIgnoringLocalAndRemoteCacheData 无视任何的缓存策略，无论是本地还是远程，总是从原地址重新下载  
  
NSURLRequestReloadRevalidatingCacheData 如果本地缓存是有效的则不下载。其他任何情况都从原地址重新下载  
  
[建立网络连接NSURLConnection，同步请求数据](#3)

```objectivec
NSData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRwquest:request returningResponse:&response error:&error];
```

以上三步后，就需要将receivedData进行解析，一般是XML/JSON

实例演示：



```objectivec detailViewController.h
#import <UIKit/UIKit.h>

@interface vlinkagePersonViewController : UIViewController<UITableViewDelegate,UITableViewDataSource>

//生成content的key值
@property (strong, nonatomic) NSArray *keys;
//生成content的value值
@property (strong, nonatomic) NSArray *objects;
//列表内容
@property (strong, nonatomic) NSDictionary *content;

//艺人的数据
@property (retain, nonatomic) NSMutableData *personData;

//艺人的数组数据
@property (retain, nonatomic) NSArray *person;
@end
```


```objectivec detailViewController.m
#import "vlinkagePersonViewController.h"

@interface vlinkagePersonViewController ()

@end

@implementation vlinkagePersonViewController

@synthesize content;
@synthesize personData;
@synthesize person;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    
    NSURL *url = [[NSURL alloc] initWithString:@"http://xxx.xxx.xxx.xxx:xxx/person/actorlist?order_by=index&start_date=2012-06-01&end_date=2012-07-01&start=1&offset=10&app_key=KSKdzSyeb99YdLwTMrzvuLumNYCM6pzT4Z3f27R4L3qq6jCs"];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestUseProtocolCachePolicy
                                              timeoutInterval:60];
    
    NSURLResponse *response = [[NSURLResponse alloc] init];
    NSError *error = [[NSError alloc] init];
    
    NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&error];
    
    
    self.person = [self readJsonData:receivedData];
    
    if([self.person isKindOfClass:[NSDictionary class]]){
        NSLog(@"NSDictionary");
    }
    
    if([self.person isKindOfClass:[NSArray class]]){
        NSLog(@"NSArray");
    }

}

-(NSArray *) readJsonData:(NSMutableData *)data{
    //NSJSONSerialization提供了将JSON数据转换为Foundation对象（一般都是NSDictionary和NSArray）
    //和Foundation对象转换为JSON数据（可以通过调用isValidJSONObject来判断Foundation对象是否可以转换为JSON数据）。
    NSError *error;
    NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:data
                                                               options:NSJSONReadingMutableContainers
                                                                 error:&error];
    NSDictionary *personInfo = [personDictionary objectForKey:@"data"];
    
    NSArray *personList = [personInfo objectForKey:@"list"];
    
    return personList;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


-(NSInteger)tableView:(UITableView*)tableView numberOfRowsInSection:(NSInteger)section{
    return [self.person count];
}


-(UITableViewCell*)tableView:(UITableView*)tableView cellForRowAtIndexPath:(NSIndexPath*)indexPath{
    
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell*cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if(cell == nil){
        cell = [[UITableViewCell alloc]initWithStyle:UITableViewCellStyleDefault
                                     reuseIdentifier:CellIdentifier];
        
    }

    NSDictionary *dic=[self.person objectAtIndex:indexPath.row];
    NSString *name=[dic objectForKey:@"zh_name"];
    
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    cell.textLabel.text = name;
    
    return cell;
    
}
@end
```

结果还会将数据显示到table中
