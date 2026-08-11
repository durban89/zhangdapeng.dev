---
title: "iOS7 ASIHTTPRequest documentation 实现各种请求，包括图片上传，put,get.post"
date: "2025-06-27 09:45:44"
slug: "ios7-asihttprequest-documentation-shi-xian-ge-zhong-qing-qiu-bao-kuo-tu-pian-shang-chuan-putgetpost"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-ASIHTTPRequest-documentation-实现各种请求，包括图片上传，put,get.post/"
  - "/2025/06/27/iOS7-ASIHTTPRequest-documentation-实现各种请求，包括图片上传，put,get.post.html"
  - "/iOS7-ASIHTTPRequest-documentation-实现各种请求，包括图片上传，put,get.post/"
  - "/iOS7-ASIHTTPRequest-documentation-实现各种请求，包括图片上传，put,get.post.html"
  - "/2025/06/27/iOS7-ASIHTTPRequest-documentation-实现各种请求-包括图片上传-put-get-post/"
  - "/2025/06/27/iOS7-ASIHTTPRequest-documentation-实现各种请求-包括图片上传-put-get-post.html"
  - "/2025/06/27/ios7-asihttprequest-documentation-shi-xian-ge-zhong-qing-qiu-bao-kuo-tu-pian-shang-chua/"
  - "/2025/06/27/ios7-asihttprequest-documentation-shi-xian-ge-zhong-qing-qiu-bao-kuo-tu-pian-shang-.html"
  - "/ios7-asihttprequest-documentation-shi-xian-ge-zhong-qing-qiu-bao-kuo-tu-pian-shang-chuan-putge.html"
---
关于ASIHTTPRequest的具体使用，这里不做详细记载，因为官方也有其示例

这里会列出几个简单的示例

#### [第一个：创建一个异步请求](#1)

Creating an asynchronous request（创建一个异步请求）

```objectivec
- (IBAction)grabURLInBackground:(id)sender
{
   NSURL *url = [NSURL URLWithString:@"http://allseeing-i.com/"];
   ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
   [request setDelegate:self];
   [request startAsynchronous];
} 
- (void)requestFinished:(ASIHTTPRequest *)request{
   // Use when fetching text data
   NSString *responseString = [request responseString];
 
   // Use when fetching binary data
   NSData *responseData = [request responseData];
} 
- (void)requestFailed:(ASIHTTPRequest *)request
{
   NSError *error = [request error];
}
```

#### [第二个：使用ASIFormDataRequest发送一个POST请求](#2)

Sending a form POST with ASIFormDataRequest（使用ASIFormDataRequest发送一个POST请求）

```objectivec
ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
[request setPostValue:@"Ben" forKey:@"first_name"];
[request setPostValue:@"Copsey" forKey:@"last_name"];
[request setFile:@"/Users/ben/Desktop/ben.jpg" forKey:@"photo"];
```

#### [第三个：直接下载文件](#3)

Downloading the response directly to a file（直接下载文件）

```objectivec
ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
[request setDownloadDestinationPath:@"/Users/ben/Desktop/my_file.txt"];
```

---

这里给出一个中文的文档地址和一个英文的文档地址，适用于初级入门者

官方文档网址：http://allseeing-i.com/ASIHTTPRequest/How-to-use

中文的文档网址：http://blog.csdn.net/zkdemon/article/details/7066807

---

