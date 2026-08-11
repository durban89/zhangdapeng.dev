---
title: "iOS 数据存储 NSData存储转为NSDictionary存储"
date: "2025-06-19 09:58:08"
slug: "ios-shu-ju-cun-chu-nsdata-cun-chu-zhuan-wei-nsdictionary-cun-chu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS-数据存储-NSData存储转为NSDictionary存储/"
  - "/2025/06/19/iOS-数据存储-NSData存储转为NSDictionary存储.html"
  - "/iOS-数据存储-NSData存储转为NSDictionary存储/"
  - "/iOS-数据存储-NSData存储转为NSDictionary存储.html"
  - "/2025/06/19/ios-shu-ju-cun-chu-nsdata-cun-chu-zhuan-wei-nsdictionary-cun-chu/"
  - "/2025/06/19/ios-shu-ju-cun-chu-nsdata-cun-chu-zhuan-wei-nsdictionary-cun-chu.html"
  - "/ios-shu-ju-cun-chu-nsdata-cun-chu-zhuan-wei-nsdictionary-cun-chu.html"
---
最近做app，涉及到关于数据的存储，对于远程数据的请求，有个问题就是，对于同样的请求，不做重复的操作，但是又能够保证，获取的数据在本地，并且即使的进行解析，之前是NSdata，这样的话，转换数据的话，就要涉及到一个中间步骤，就是将数据转换为json格式，在转换为NSdictionary，解析的过程会出现的可能性，导致数据不能及时响应，最近几次的闪退，估计是这个原因，于是做了调整，闪退的现象果然概率不再频繁。

这次主要是分享一下，修改后的封装类，主要是在里面添加了几个关于存储NSDictionary的方法

代码托管在[github](https://github.com/zhangda89/IOS-StorageData)：https://github.com/zhangda89/IOS-StorageData



```objectivec StorageData.m
//
//  StorageData.m
//  xunYi7
//
//  Created by david on 13-6-28.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <CommonCrypto/CommonDigest.h>
#import "StorageData.h"
#import "xunYi7AppDelegate.h"


@implementation StorageData


-(void) connection:(NSURLConnection *)connection didReceiveData:(NSData *)data{
    NSLog(@"开始结didReceiveData搜数据");
}

-(void) connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response{
    NSLog(@"开始结didReceiveResponse搜数据");
}

-(void) connection:(NSURLConnection *)connection didFailWithError:(NSError *)error{
    NSLog(@"didFailWithError");
}

-(void) connectionDidFinishLoading:(NSURLConnection *)connection{
    NSLog(@"connectionDidFinishLoading");
}

+(NSMutableData *)remoteFetchData:(NSString *)dataUrl{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@.plist",[self md5:dataUrl]]];
    
    if([xunYi7AppDelegate isReachable]){
        NSURL *url = [[NSURL alloc] initWithString:dataUrl];
        NSURLRequest *request = [[NSURLRequest alloc] initWithURL:url
                                                      cachePolicy:NSURLRequestUseProtocolCachePolicy
                                                  timeoutInterval:60];
        
        NSURLResponse *response = [[NSURLResponse alloc] init];
        NSError *receiveDataError = [[NSError alloc] init];
        
        NSMutableData *receivedData = (NSMutableData *)[NSURLConnection sendSynchronousRequest:request
                                                                             returningResponse:&response
                                                                                         error:&receiveDataError];
        [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
        
        if(receivedData != nil){
            if([self storageDataToFile:receivedData fileName:currentDataFilePath]){
                [self removeDirectory];
            }
        }
        
        return receivedData;
    }else{
        [xunYi7AppDelegate showNetworkMessage];
    }

    return nil;
}

+(NSMutableData *)localFetchData:(NSString *)dataUrl{
    
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@.plist",[self md5:dataUrl]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@.plist",[self md5:dataUrl]]];
    
    NSMutableData *localData = [self fromFilenamePathFetchLocalData:currentDataFilePath];
    
    if(localData != nil){//本地数据
        return localData;
        
    }else{//远程获取数据
        
        NSMutableData *receivedData = [self remoteFetchData:dataUrl];
        
        if(receivedData != nil){
            if([self storageDataToFile:receivedData fileName:currentDataFilePath]){
//                NSLog(@"保存成功");
                [self removeDirectory];
            }else{
//                NSLog(@"保存失败");
            }
        }else{
            if((localData = [self fromFilenamePathFetchLocalData:yesterdayDataFilePath]) != nil){
                return localData;
            }
        }
        return receivedData;
    }
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-艺人排行版
+(NSDictionary *) localFetchPersonRankDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 Dictionary 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 Dictionary 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];

        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                             options:NSJSONReadingMutableContainers
                                                                               error:&jsonError];
            
            NSDictionary *personInfo = [personDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:personInfo fileName:currentDataFilePath]){
//                NSLog(@"远程数据存储成功");
                return personInfo;
                [self removeDirectory];
            }else{
//                NSLog(@"远程数据存储失败");s
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-关注列表
+(NSDictionary *) localFetchAttentionListDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchAttentionListDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchAttentionListDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *attentionDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                             options:NSJSONReadingMutableContainers
                                                                               error:&jsonError];
            
            NSDictionary *attentionData = [attentionDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:attentionData fileName:currentDataFilePath]){
//                NSLog(@"localFetchAttentionListDictionayData 远程数据存储成功");
                return attentionData;
                [self removeDirectory];
            }else{
                return attentionData;
//                NSLog(@"localFetchAttentionListDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取远程数据的Dcitionary格式-关注列表
+(NSDictionary *) remoteFetchAttentionListDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];

    NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
    
    if(receivedData != nil){
        [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
        NSError *jsonError = [[NSError alloc] init];
        NSDictionary *attentionDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                            options:NSJSONReadingMutableContainers
                                                                              error:&jsonError];
        
        NSDictionary *attentionData = [attentionDictionary objectForKey:@"data"];
        
        if([self storageDictionaryDataToFile:attentionData fileName:currentDataFilePath]){
            //                NSLog(@"localFetchAttentionListDictionayData 远程数据存储成功");
            return attentionData;
            [self removeDirectory];
        }else{
            return attentionData;
            //                NSLog(@"localFetchAttentionListDictionayData 远程数据存储失败");
        }
    }
    
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-机会列表
+(NSDictionary *) localFetchChanceListDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchChanceListDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchChanceListDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *chanceDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                                options:NSJSONReadingMutableContainers
                                                                                  error:&jsonError];
            
            NSMutableDictionary *chanceData = [chanceDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:chanceData fileName:currentDataFilePath]){
//                NSLog(@"localFetchChanceListDictionayData 远程数据存储成功");
                return chanceData;
                [self removeDirectory];
            }else{
                return chanceData;
//                NSLog(@"localFetchChanceListDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-电视剧排行榜
+(NSDictionary *) localFetchTeleplayRankDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchTeleplayRankDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchTeleplayRankDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *teleplayDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                             options:NSJSONReadingMutableContainers
                                                                               error:&jsonError];
            
            NSMutableDictionary *teleplayData = [teleplayDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:teleplayData fileName:currentDataFilePath]){
//                NSLog(@"localFetchTeleplayRankDictionayData 远程数据存储成功");
                return teleplayData;
                [self removeDirectory];
            }else{
                return teleplayData;
//                NSLog(@"localFetchTeleplayRankDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-艺人签单排行榜
+(NSDictionary *) localFetchStarkCheckDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchStarkCheckDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchStarkCheckDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *starkCheckDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                               options:NSJSONReadingMutableContainers
                                                                                 error:&jsonError];
            
            NSMutableDictionary *starkCheckData = [starkCheckDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:starkCheckData fileName:currentDataFilePath]){
//                NSLog(@"localFetchStarkCheckDictionayData 远程数据存储成功");
                return starkCheckData;
                [self removeDirectory];
            }else{
                return starkCheckData;
//                NSLog(@"localFetchStarkCheckDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取本地数据的Dcitionary格式-hotTeleplay
+(NSDictionary *) localFetchHotTeleplayDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchHotTeleplayDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchHotTeleplayDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *starkCheckDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                                 options:NSJSONReadingMutableContainers
                                                                                   error:&jsonError];
            
            NSMutableDictionary *starkCheckData = [starkCheckDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:starkCheckData fileName:currentDataFilePath]){
//                NSLog(@"localFetchHotTeleplayDictionayData 远程数据存储成功");
                return starkCheckData;
                [self removeDirectory];
            }else{
                return starkCheckData;
//                NSLog(@"localFetchHotTeleplayDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 获取远程数据的Dcitionary格式-找演员
+(NSDictionary *) remoteFetchFindPerformersDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    //远程获取数据
    NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
    
    if(receivedData != nil){
        [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
        NSError *jsonError = [[NSError alloc] init];
        NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                         options:NSJSONReadingMutableContainers
                                                                           error:&jsonError];
        
        NSMutableDictionary *searchPersonResult = [personDictionary objectForKey:@"data"];
        
        if([self storageDictionaryDataToFile:searchPersonResult fileName:currentDataFilePath]){
            //                NSLog(@"localFetchFindPerformersDictionayData 远程数据存储成功");
            return searchPersonResult;
            [self removeDirectory];
        }else{
            return searchPersonResult;
            //                NSLog(@"localFetchFindPerformersDictionayData 远程数据存储失败");
        }
    }
    return nil;
}


+(NSDictionary *) localFetchFindPerformersDictionayData:(NSString *)dataUrlString{
    NSString *currentDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchTodayDate]];
    NSString *yesterdayDataFilePath = [[self dataPath] stringByAppendingPathComponent:[self fetchYesterdayDate]];
    
    //创建目录
    currentDataFilePath = [self createDirectory:currentDataFilePath];
    
    currentDataFilePath = [currentDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    yesterdayDataFilePath = [yesterdayDataFilePath stringByAppendingPathComponent:[NSString stringWithFormat:@"%@-dictionary.plist",[self md5:dataUrlString]]];
    
    NSDictionary *localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:currentDataFilePath];
    
    if(localDictionaryData != nil){//本地数据
//        NSLog(@"本地数据 localFetchFindPerformersDictionayData 数据");
        return localDictionaryData;
    }else{//远程获取数据
//        NSLog(@"远程获取数据 localFetchFindPerformersDictionayData 数据");
        NSMutableData *receivedData = [self remoteFetchData:dataUrlString];
        
        if(receivedData != nil){
            [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
            NSError *jsonError = [[NSError alloc] init];
            NSDictionary *personDictionary = [NSJSONSerialization JSONObjectWithData:receivedData
                                                                                 options:NSJSONReadingMutableContainers
                                                                                   error:&jsonError];
            
            NSMutableDictionary *searchPersonResult = [personDictionary objectForKey:@"data"];
            
            if([self storageDictionaryDataToFile:searchPersonResult fileName:currentDataFilePath]){
//                NSLog(@"localFetchFindPerformersDictionayData 远程数据存储成功");
                return searchPersonResult;
                [self removeDirectory];
            }else{
                return searchPersonResult;
//                NSLog(@"localFetchFindPerformersDictionayData 远程数据存储失败");
            }
        }else{
            if((localDictionaryData = [self fromFilenamePathFetchLocalDictionaryData:yesterdayDataFilePath]) != nil){
                return localDictionaryData;
            }
        }
    }
    return nil;
}

#pragma mark - 存储Dictionary格式的数据到本地-艺人排行版
+(void) savePersonRankDictionaryToLocal:(NSMutableDictionary *)data dataUrlString:(NSString *)urlString{
    
}

//md5加密字符串
+(NSString *)md5:(NSString *)str{
    const char *cStr = [str UTF8String];
    unsigned char result[16];
    CC_MD5(cStr, strlen(cStr), result); // This is the md5 call
    return [NSString stringWithFormat:
            @"%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x",
            result[0], result[1], result[2], result[3],
            result[4], result[5], result[6], result[7],
            result[8], result[9], result[10], result[11],
            result[12], result[13], result[14], result[15]
            ]; 
}
//上传图片存储
+(void) saveUploadImage:(UIImage *)image withName:(NSString *)imageName{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSError *error;
    
    // 获取沙盒目录
    NSString *fullPath = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents"];
    fullPath = [fullPath stringByAppendingPathComponent:@"tmpImage"];
    if(![fileManager fileExistsAtPath:fullPath]){
        [fileManager createDirectoryAtPath:fullPath
               withIntermediateDirectories:YES
                                attributes:nil
                                     error:&error];
    }
   
    fullPath = [fullPath stringByAppendingPathComponent:imageName];
    NSData *imageData = UIImageJPEGRepresentation(image, 0.5);
    
    // 将图片写入文件
    [imageData writeToFile:fullPath atomically:NO];
}

//上传图片删除
+(void) removeUploadImage:(UIImage *)image withName:(NSString *)imageName{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSError *error;
    
    // 获取沙盒目录
    NSString *fullPath = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents"];
    fullPath = [fullPath stringByAppendingPathComponent:@"tmpImage"];
    if(![fileManager fileExistsAtPath:fullPath]){
        [fileManager removeItemAtPath:fullPath error:&error];
    }
}

//获取存储的图片
+(NSString *)fetchUploadImagePath:(NSString *)imageName{
    NSString *fullPath = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents"];
    fullPath = [fullPath stringByAppendingPathComponent:@"tmpImage"];
    fullPath = [fullPath stringByAppendingPathComponent:imageName];
    return fullPath;
}

//判断文件是否存在
+(NSString *)isFileExists:(NSString *)fullpath{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    if([fileManager fileExistsAtPath:fullpath]){
        return fullpath;
    }
    return nil;
}

//数据存储
//+(void)

//获取存储文件的目录
+(NSString *)dataPath{
    //此处首先指定了图片存取路径（默认写到应用程序沙盒 中）
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,NSUserDomainMask, YES);
    
    //并给文件起个文件名
    NSString *filePathDerectory = [paths objectAtIndex:0];
    
    return filePathDerectory;
}

//获取指定文件的数据
+(NSMutableData *)fromFilenamePathFetchLocalData:(NSString *)filename{
    //保存数据到指定文件中
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    if([fileManager fileExistsAtPath:filename]){
        NSData *data = [fileManager contentsAtPath:filename];
        return [data mutableCopy];
    }
    
    return nil;
}

+(NSDictionary *)fromFilenamePathFetchLocalDictionaryData:(NSString *)filename{

    NSDictionary *dicData = [[NSDictionary alloc] initWithContentsOfFile:filename];
    
    if(dicData != nil){
        return dicData;
    }

    
    return nil;
}

//存储数据到指定文件
+(BOOL) storageDataToFile:(NSData *)data fileName:(NSString *)fileName{
    //保存数据到指定文件中
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    if([fileManager createFileAtPath:fileName contents:data attributes:nil]){
        return YES;
    }else{
        return NO;
    }
}

#pragma mark - 存储Dictionary格式的数据
+(BOOL) storageDictionaryDataToFile:(NSDictionary *)dicData fileName:(NSString *)fileName{
    //保存数据到指定文件中
    if([dicData writeToFile:fileName atomically:YES]){
        return YES;
    }else{
        return NO;
    }
}

//删除文件
+(void) deleteFile:(NSString *)fileName{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSError *error;
    [fileManager removeItemAtPath:fileName error:&error];
}

//获取今天的日期
+(NSString *) fetchTodayDate{
    NSDate *currentDate = [NSDate date];
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateStyle:NSDateFormatterMediumStyle];
    return [dateFormatter stringFromDate:currentDate];
}

//获取前天的日期
+(NSString *) fetchYesterdayBeforeDate{
    NSDate *yesterdayDate = [NSDate dateWithTimeIntervalSinceNow:-(2 * (24 * 60 * 60))];
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateStyle:NSDateFormatterMediumStyle];
    return [dateFormatter stringFromDate:yesterdayDate];
}

//获取存储文件的数据

//创建文件

//创建目录
+(NSString *) createDirectory:(NSString *)directoryName{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSError *error;
    if(![fileManager fileExistsAtPath:directoryName]){
        [fileManager createDirectoryAtPath:directoryName
               withIntermediateDirectories:YES
                                attributes:nil
                                     error:&error];
        if(error == nil){
            return directoryName;
        }else{
            return directoryName;
        }
    }else{
        return directoryName;
    }
}
//删除文件
+(void) removeFile:(NSString *)filePath{
    NSError *error;
    
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    if([fileManager fileExistsAtPath:filePath]){
        [fileManager removeItemAtPath:filePath error:&error];
    }
    if(error){
        NSLog(@"error = %@",error);
    }
}

//删除目录
+(void) removeDirectory{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsPath = [paths objectAtIndex:0];
    NSString *removeDirectoryPath = [documentsPath stringByAppendingPathComponent:[self fetchYesterdayBeforeDate]];
    NSError *error;
    
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    if([fileManager fileExistsAtPath:removeDirectoryPath]){
        [fileManager removeItemAtPath:removeDirectoryPath error:&error];
    }
    if(error){
        NSLog(@"error = %@",error);
    }
}
@end
```
