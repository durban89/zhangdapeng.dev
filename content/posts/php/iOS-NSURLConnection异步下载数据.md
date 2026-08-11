---
title: "iOS NSURLConnection异步下载数据"
date: "2025-06-10 15:14:42"
slug: "ios-nsurlconnection-yi-bu-xia-zai-shu-ju"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-NSURLConnection异步下载数据/"
  - "/2025/06/10/iOS-NSURLConnection异步下载数据.html"
  - "/iOS-NSURLConnection异步下载数据/"
  - "/iOS-NSURLConnection异步下载数据.html"
  - "/2025/06/10/ios-nsurlconnection-yi-bu-xia-zai-shu-ju/"
  - "/2025/06/10/ios-nsurlconnection-yi-bu-xia-zai-shu-ju.html"
  - "/ios-nsurlconnection-yi-bu-xia-zai-shu-ju.html"
---
异步下载支持应用程序在后台下载数据，在等待下载完成的过程中不会阻塞代码的运行

代码如下：



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

@end
```



```objectivec detailViewController.m
#import "vlinkagePersonViewController.h"

@interface vlinkagePersonViewController ()

@end

@implementation vlinkagePersonViewController

@synthesize content;
@synthesize personData;


- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.

    
    NSURL *url = [[NSURL alloc] initWithString:@"http://xxx.xxx.xxx.xxx:xxx/person/actorlist?order_by=index&start_date=2012-06-01&end_date=2012-07-01&start=1&offset=10&app_key=KSKdzSyeb99YdLwTMrzvuLumNYCM6pzT4Z3f27R4L3qq6jCs"];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestReloadIgnoringCacheData
                                              timeoutInterval:60];
    NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest:request delegate:self];
    
    if(!connection){
        NSLog(@"链接失败!");
    }else{
        self.personData = [NSMutableData data];
        self.content = [[NSDictionary alloc] init];
    }
    NSLog(@"content = %@",self.content);
}

//回掉方法
-(void) connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response{
    NSLog(@"didReceiveResponse");
    [self.personData setLength:0];
}

//将接收到的数据存储到字符串中
-(void) connection:(NSURLConnection *)connection didReceiveData:(NSData *)data{
    NSLog(@"didReceiveData");
    [self.personData appendData:data];
}

//下载已经完成
- (void)connectionDidFinishLoading: (NSURLConnection *) connection{
    NSLog(@"connectionDidFinishLoading");
    //调用函数解析下载到的json格式的数据
    [self readJsonData];
    NSLog(@"content %@",self.content);
}

//下载失败
-(void) connection:(NSURLConnection *)connection didFailWithError:(NSError *)error{
    UIAlertView *errorAlert = [[UIAlertView alloc] initWithTitle:[error localizedDescription]
                                                         message:[error localizedFailureReason]
                                                        delegate:self
                                               cancelButtonTitle:@"OK!"
                                               otherButtonTitles:nil];
    [errorAlert show];
    
}

-(void) readJsonData{
    //NSJSONSerialization提供了将JSON数据转换为Foundation对象（一般都是NSDictionary和NSArray）
    //和Foundation对象转换为JSON数据（可以通过调用isValidJSONObject来判断Foundation对象是否可以转换为JSON数据）。
    NSError *error;
    NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:self.personData
                                                               options:NSJSONReadingMutableContainers
                                                                 error:&error];
    NSDictionary *personInfo = [personDictionary objectForKey:@"data"];
    NSDictionary *personList = [personInfo objectForKey:@"list"];
    self.content = personList;
    NSLog(@"personList %@",personList);
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


-(NSInteger)tableView:(UITableView*)tableView numberOfRowsInSection:(NSInteger)section{
    return 1;
}


-(UITableViewCell*)tableView:(UITableView*)tableView cellForRowAtIndexPath:(NSIndexPath*)indexPath{
    
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell*cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if(cell == nil){
        cell = [[UITableViewCell alloc]initWithStyle:UITableViewCellStyleDefault
                                    reuseIdentifier:CellIdentifier];
        cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    }
    cell.textLabel.text=@"话题";
    
    return cell;
    
}
@end
```

输出的结果是：

```shell
2013-04-26 16:45:55.174 vlinkagePerson3[67809:c07] content = {
}
2013-04-26 16:45:55.501 vlinkagePerson3[67809:c07] didReceiveResponse
2013-04-26 16:45:55.501 vlinkagePerson3[67809:c07] didReceiveData
2013-04-26 16:45:55.502 vlinkagePerson3[67809:c07] connectionDidFinishLoading
2013-04-26 16:45:55.502 vlinkagePerson3[67809:c07] personList (
        {
        id = 175;
        "is_attention" = 0;
        score = "7.84948333";
        "zh_name" = "\U5b59\U4fea";
    },
        {
        id = 1582;
        "is_attention" = 0;
        score = "7.78961667";
        "zh_name" = "\U949f\U6c49\U826f";
    },
        {
        id = 17577;
        "is_attention" = 0;
        score = "7.69375000";
        "zh_name" = "\U5f20\U6839\U7855";
    },
        {
        id = 35;
        "is_attention" = 0;
        score = "7.60104167";
        "zh_name" = "\U6768\U5e42";
    },
        {
        id = 3880;
        "is_attention" = 0;
        score = "7.56774167";
        "zh_name" = "\U6797\U4f9d\U6668";
    },
        {
        id = 94;
        "is_attention" = 0;
        score = "7.56668333";
        "zh_name" = "\U674e\U5c0f\U7490";
    },
        {
        id = 504;
        "is_attention" = 0;
        score = "7.48178333";
        "zh_name" = "\U5f20\U6aac";
    },
        {
        id = 3571;
        "is_attention" = 0;
        score = "7.46722500";
        "zh_name" = "\U9a6c\U5929\U5b87";
    },
        {
        id = 228;
        "is_attention" = 0;
        score = "7.45210000";
        "zh_name" = "\U5b8b\U4e39\U4e39";
    },
        {
        id = 329;
        "is_attention" = 0;
        score = "7.44270833";
        "zh_name" = "\U80e1\U6b4c";
    }
)
2013-04-26 16:45:55.503 vlinkagePerson3[67809:c07] content (
        {
        id = 175;
        "is_attention" = 0;
        score = "7.84948333";
        "zh_name" = "\U5b59\U4fea";
    },
        {
        id = 1582;
        "is_attention" = 0;
        score = "7.78961667";
        "zh_name" = "\U949f\U6c49\U826f";
    },
        {
        id = 17577;
        "is_attention" = 0;
        score = "7.69375000";
        "zh_name" = "\U5f20\U6839\U7855";
    },
        {
        id = 35;
        "is_attention" = 0;
        score = "7.60104167";
        "zh_name" = "\U6768\U5e42";
    },
        {
        id = 3880;
        "is_attention" = 0;
        score = "7.56774167";
        "zh_name" = "\U6797\U4f9d\U6668";
    },
        {
        id = 94;
        "is_attention" = 0;
        score = "7.56668333";
        "zh_name" = "\U674e\U5c0f\U7490";
    },
        {
        id = 504;
        "is_attention" = 0;
        score = "7.48178333";
        "zh_name" = "\U5f20\U6aac";
    },
        {
        id = 3571;
        "is_attention" = 0;
        score = "7.46722500";
        "zh_name" = "\U9a6c\U5929\U5b87";
    },
        {
        id = 228;
        "is_attention" = 0;
        score = "7.45210000";
        "zh_name" = "\U5b8b\U4e39\U4e39";
    },
        {
        id = 329;
        "is_attention" = 0;
        score = "7.44270833";
        "zh_name" = "\U80e1\U6b4c";
    }
)
```

