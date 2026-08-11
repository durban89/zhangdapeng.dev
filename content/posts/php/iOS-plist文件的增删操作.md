---
title: "iOS plist文件的增删操作"
date: "2025-06-10 15:46:27"
slug: "ios-plist-wen-jian-de-zeng-shan-cao-zuo"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-plist文件的增删操作/"
  - "/2025/06/10/iOS-plist文件的增删操作.html"
  - "/iOS-plist文件的增删操作/"
  - "/iOS-plist文件的增删操作.html"
  - "/2025/06/10/ios-plist-wen-jian-de-zeng-shan-cao-zuo/"
  - "/2025/06/10/ios-plist-wen-jian-de-zeng-shan-cao-zuo.html"
  - "/ios-plist-wen-jian-de-zeng-shan-cao-zuo.html"
---
我最近在使用plist存数数据，方便后面的数据浏览

很是苦恼于是自己就查遍各方资料，弄了一个简单的类函数,方便自己的更新数据



```objectivec detailViewController.h
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

@interface personIndex : NSObject

@property (strong, nonatomic) NSArray *personArr;
@property (strong, nonatomic) NSMutableArray *personMulArr;

//清空原有数据
-(void) deletePlist;
//响应错误
-(void) showAlert;
//获取远端数据
-(void) getRemoteData;
//创建plist文件
-(void) createPlist;
//写入数据到plist文件
-(void) writePlist;
//解析json数据
-(NSArray *) readJsonData:(NSMutableData *)data;
//下载数据
-(void) executeDown;

@end
```



```objectivec detailViewController.m
#import "personIndex.h"

@implementation personIndex

@synthesize personArr;
@synthesize personMulArr;


-(void) executeDown{
    [self deletePlist];
    [self getRemoteData];
    [self createPlist];
    [self writePlist];
}

//将数据写入plist
-(void) writePlist{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *path = [documentsDirectory stringByAppendingPathComponent:@"test.plist"];
    NSFileManager *fileManager = [NSFileManager defaultManager];
    
    if ([fileManager fileExistsAtPath: path]){//如果文件存在，写入数据
        //创建字典
        NSMutableDictionary *dictplist = [[NSMutableDictionary alloc ] init];
        for(id item in self.personArr){
            //设置属性值
            [dictplist setValue:[NSString stringWithFormat:@"%@",[item valueForKey:@"zh_name"]]
                         forKey:[NSString stringWithFormat:@"%@",[item valueForKey:@"id"]]];
        }
        
        //写入文件
        if(![dictplist writeToFile:path atomically:YES]){
            [self showAlert:@"同步数据失败"];
        }
    }else{
        NSString *appFile = [documentsDirectory stringByAppendingPathComponent: [NSString stringWithFormat: @"test.plist"] ];
        //创建字典
        NSMutableDictionary *dictplist = [[NSMutableDictionary alloc ] init];
            
        for(id item in self.personArr){
            //设置属性值
            [dictplist setValue:[NSString stringWithFormat:@"%@",[item valueForKey:@"zh_name"]]
                         forKey:[NSString stringWithFormat:@"%@",[item valueForKey:@"id"]]];
        }

        ///写入文件
        if(![dictplist writeToFile:appFile atomically:YES]){
            [self showAlert:@"同步数据失败"];
        }
    }
}


-(void) deletePlist{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *path = [documentsDirectory stringByAppendingPathComponent:@"test.plist"];
    
    NSFileManager *fileManager = [NSFileManager defaultManager];
    [fileManager removeItemAtPath:path error:nil];
}


-(NSMutableDictionary *) readPlist{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *path = [documentsDirectory stringByAppendingPathComponent:@"test.plist"];
    NSFileManager *fileManager = [NSFileManager defaultManager];
    
    NSMutableDictionary *data = [[NSMutableDictionary alloc] initWithContentsOfFile: path];
    
    
    if ([fileManager fileExistsAtPath: path]){//如果文件存在，写入数据
        data = [[NSMutableDictionary alloc] initWithContentsOfFile: path];
    }else{
        // If the file doesn’t exist, create an empty dictionary
        data = [[NSMutableDictionary alloc] init];
    }
    return data;
}

//创建plist文件
-(void) createPlist{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [paths objectAtIndex:0];
    NSString *path = [documentsDirectory stringByAppendingPathComponent:@"test.plist"];
    NSFileManager *fileManager = [NSFileManager defaultManager];
    
    if (![fileManager fileExistsAtPath: path]){
        [documentsDirectory stringByAppendingPathComponent: [NSString stringWithFormat: @"test.plist"]];
    }
}

-(void) getRemoteData{
    NSURL *url = [[NSURL alloc] initWithString:@"http://222.73.93.70:3002/person/actorlist?order_by=index&start_date=2012-06-01&end_date=2012-07-01&start=1&offset=10&app_key=KSKdzSyeb99YdLwTMrzvuLumNYCM6pzT4Z3f27R4L3qq6jCs"];
    NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                  cachePolicy:NSURLRequestUseProtocolCachePolicy
                                              timeoutInterval:60];
    
    NSURLResponse *response = [[NSURLResponse alloc] init];
    NSError *error = [[NSError alloc] init];
    
    NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&error];
    
    self.personArr = [self readJsonData:receivedData];
}

-(NSArray *) readJsonData:(NSMutableData *)data{
    //NSJSONSerialization提供了将JSON数据转换为Foundation对象（一般都是NSDictionary和NSArray）
    //和Foundation对象转换为JSON数据（可以通过调用isValidJSONObject来判断Foundation对象是否可以转换为JSON数据）。
    NSArray *personList = [[NSArray alloc] init];
    if(data == nil){
        [self showAlert:@"更新数据失败"];
    }else{
        NSError *error;
        NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:data
                                                                         options:NSJSONReadingMutableContainers
                                                                           error:&error];
        NSDictionary *personInfo = [personDictionary objectForKey:@"data"];
        
        personList = [personInfo objectForKey:@"list"];
    }
    
    
    return personList;
}

-(NSArray *) readStringJsonData:(NSMutableData *)data{
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

-(void) showAlert:(NSString *)stringData{
    UIAlertView *alrt = [[UIAlertView alloc] initWithTitle:@"同步数据失败"
                                                   message:[NSString stringWithFormat:@"%@",stringData]
                                                  delegate:self
                                         cancelButtonTitle:@"OK"
                                         otherButtonTitles:nil];
    [alrt show];
}

@end
```
