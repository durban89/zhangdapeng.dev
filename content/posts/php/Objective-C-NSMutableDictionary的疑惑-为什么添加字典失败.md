---
title: "Objective-C NSMutableDictionary的疑惑（为什么添加字典失败）"
date: "2025-06-13 14:05:51"
slug: "objective-c-nsmutabledictionary-de-yi-huo-wei-shen-me-tian-jia-zi-dian-shi-bai"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/13/Objective-C-NSMutableDictionary的疑惑（为什么添加字典失败）/"
  - "/2025/06/13/Objective-C-NSMutableDictionary的疑惑（为什么添加字典失败）.html"
  - "/Objective-C-NSMutableDictionary的疑惑（为什么添加字典失败）/"
  - "/Objective-C-NSMutableDictionary的疑惑（为什么添加字典失败）.html"
  - "/2025/06/13/Objective-C-NSMutableDictionary的疑惑-为什么添加字典失败/"
  - "/2025/06/13/Objective-C-NSMutableDictionary的疑惑-为什么添加字典失败.html"
  - "/2025/06/13/objective-c-nsmutabledictionary-de-yi-huo-wei-shen-me-tian-jia-zi-dian-shi-bai/"
  - "/2025/06/13/objective-c-nsmutabledictionary-de-yi-huo-wei-shen-me-tian-jia-zi-dian-shi-bai.html"
  - "/objective-c-nsmutabledictionary-de-yi-huo-wei-shen-me-tian-jia-zi-dian-shi-bai.html"
---
我的情况是这样子的，由于我要远程获取数据然后呈现数据，但是首先我获取的远程数据是json格式的，然后我移动端将其转换为字典类型。

出问题的代码如下：

我在.h文件中这样的

```objectivec
@property (strong, nonatomic) NSMutableDictionary *dataDic;
```

我在.m文件中这样的

```objectivec
-(void) initData
{
    NSDate *date = [NSDate date];
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd"];
    
    NSString *dateString = [dateFormatter stringFromDate: [NSDate dateWithTimeInterval:-(2 * 24 * 60 * 60) sinceDate:date]];

    NSString *urlString = @"http://xxx.xxx.xxx.xxx:xxxxxxxxxx/xxxxx/xxxxxx?";
    urlString = [urlString stringByAppendingFormat:@"order_by=%@",@"index"];
    urlString = [urlString stringByAppendingFormat:@"&start_date=%@",dateString];
    urlString = [urlString stringByAppendingFormat:@"&end_date=%@",dateString];
    urlString = [urlString stringByAppendingFormat:@"&start=%@",@"1"];
    urlString = [urlString stringByAppendingFormat:@"&offset=%@",@"20"];
    urlString = [urlString stringByAppendingFormat:@"&app_key=%@",@""];
    
    
    NSURL *url = [[NSURL alloc] initWithString:urlString];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestUseProtocolCachePolicy
                                              timeoutInterval:60];
    
    NSURLResponse *response = [[NSURLResponse alloc] init];
    NSError *receiveDataError = [[NSError alloc] init];

    NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request
                                                                         returningResponse:&response
                                                                                     error:&receiveDataError];
    
    if(receivedData == nil)
    {
        NSLog(@"获取数据失败");
    }
    
    
    NSError *jsonError = [[NSError alloc] init];
    NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                     options:NSJSONReadingMutableContainers
                                                                       error:&jsonError];
    NSMutableDictionary *personInfo = [personDictionary objectForKey:@"data"];
    
    NSMutableDictionary *personList = [personInfo objectForKey:@"list"];
    
//    self.dataDic = [NSMutableDictionary dictionaryWithCapacity:20];
    
    if([personList isKindOfClass:[NSMutableArray class]])
    {
        int i = 0;
        for (NSDictionary *dic in personList) {
            [self.dataDic setObject:dic forKey:[NSString stringWithFormat:@"%d",i]];
            i++;
        }
    }
    
    
    if([personList isKindOfClass:[NSMutableDictionary class]])
    {
        NSLog(@"NSMutableDictionary 类");
    }
    
    NSLog(@"self.dataDic = %@",self.dataDic);
}
```

运行后，输出的结果如下:

```bash
2013-05-29 09:54:53.460 vlinkagePerson3[6359:907] self.dataDic = (null)
```

很奇怪，为什么结果为空呢，于是经过查找资料并进行尝试修改，结果就可以了

```objectivec
-(void) initData
{
    NSDate *date = [NSDate date];
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"yyyy-MM-dd"];
    
    NSString *dateString = [dateFormatter stringFromDate: [NSDate dateWithTimeInterval:-(2 * 24 * 60 * 60) sinceDate:date]];

    NSString *urlString = @"http://xxx.xxx.xxx.xxx:xxxxxxxxxx/xxxxx/xxxxxx?";
    urlString = [urlString stringByAppendingFormat:@"order_by=%@",@"index"];
    urlString = [urlString stringByAppendingFormat:@"&start_date=%@",dateString];
    urlString = [urlString stringByAppendingFormat:@"&end_date=%@",dateString];
    urlString = [urlString stringByAppendingFormat:@"&start=%@",@"1"];
    urlString = [urlString stringByAppendingFormat:@"&offset=%@",@"20"];
    urlString = [urlString stringByAppendingFormat:@"&app_key=%@",@""];
    
    
    NSURL *url = [[NSURL alloc] initWithString:urlString];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestUseProtocolCachePolicy
                                              timeoutInterval:60];
    
    NSURLResponse *response = [[NSURLResponse alloc] init];
    NSError *receiveDataError = [[NSError alloc] init];

    NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request
                                                                         returningResponse:&response
                                                                                     error:&receiveDataError];
    
    if(receivedData == nil)
    {
        NSLog(@"获取数据失败");
    }
    
    
    NSError *jsonError = [[NSError alloc] init];
    NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                     options:NSJSONReadingMutableContainers
                                                                       error:&jsonError];
    NSMutableDictionary *personInfo = [personDictionary objectForKey:@"data"];
    
    NSMutableDictionary *personList = [personInfo objectForKey:@"list"];
    
    self.dataDic = [NSMutableDictionary dictionaryWithCapacity:20];
    
    if([personList isKindOfClass:[NSMutableArray class]])
    {
        int i = 0;
        for (NSDictionary *dic in personList) {
            [self.dataDic setObject:dic forKey:[NSString stringWithFormat:@"%d",i]];
            i++;
        }
    }
    
    
    if([personList isKindOfClass:[NSMutableDictionary class]])
    {
        NSLog(@"NSMutableDictionary 类");
    }
    
    NSLog(@"self.dataDic = %@",self.dataDic);
}
```

关键一点是这里`self.dataDic = [NSMutableDictionary dictionaryWithCapacity:20];`应该是没有分配空间吧
