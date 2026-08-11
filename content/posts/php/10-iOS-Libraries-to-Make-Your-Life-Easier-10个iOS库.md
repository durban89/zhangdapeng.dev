---
title: "10 iOS Libraries to Make Your Life Easier(10个iOS库)"
date: "2025-06-11 10:34:26"
slug: "10-ios-libraries-to-make-your-life-easier10-ge-ios-ku"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/11/10-iOS-Libraries-to-Make-Your-Life-Easier(10个iOS库)/"
  - "/2025/06/11/10-iOS-Libraries-to-Make-Your-Life-Easier(10个iOS库).html"
  - "/10-iOS-Libraries-to-Make-Your-Life-Easier(10个iOS库)/"
  - "/10-iOS-Libraries-to-Make-Your-Life-Easier(10个iOS库).html"
  - "/2025/06/11/10-iOS-Libraries-to-Make-Your-Life-Easier-10个iOS库/"
  - "/2025/06/11/10-iOS-Libraries-to-Make-Your-Life-Easier-10个iOS库.html"
  - "/2025/06/11/10-ios-libraries-to-make-your-life-easier10-ge-ios-ku/"
  - "/2025/06/11/10-ios-libraries-to-make-your-life-easier10-ge-ios-ku.html"
  - "/10-ios-libraries-to-make-your-life-easier10-ge-ios-ku.html"
---
The iOS SDK that developers use to build iPhone and iPad apps is relatively low level, requiring the developer to do a lot of work to get their app up and running. Fortunately there are lots of third party libraries available that provide useful functionality that can make your life as an iOS developer much easier. Here we discuss 10 of the best:（阐述IOS库的是很有用的）

**[MBProgressHUD](https://github.com/jdg/MBProgressHUD) – Progress Indicator Library（进展指示符库）**

Many official Apple apps have a nice translucent progress display. Unfortunately it’s an undocumented API, and therefore using it is likely to get your app rejected from the app store. This library provides a drop in replacement that looks almost identical. It also provides some additional options, such as a visual progress indicator, and a progress completion message. Integrating it into your project is as simple as adding a couple of files, so you’ve got no excuse not to!

**[ASIHttpRequest](http://allseeing-i.com/ASIHTTPRequest/) – HTTP Network Library（HTTP Network库）**

The iPhone’s network API can be a little verbose. the ASI library simplifies network communication greatly, and offers advanced tools such as file uploads, redirect handling, authentication, form submission, and caching. If you’re doing anything HTTP related in your iPhone app then this library will make your life so much easier! Here’s how simple it makes fetching a website asynchronously:

```objectivec
- (void) loadAppDevMag
{
   NSURL *url = [NSURL URLWithString:@"http://www.appdevmag.com"];
   ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
   [request setDelegate:self];
   [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
   // Use when fetching text data
   NSString *responseString = [request responseString];
}
```

**[JSON Framework](https://stig.github.com/json-framework/) – JSON Support（JSON支持）**

If your app interacts with any web services you’ll more than likely come across JSON encoded data. Surprisingly there’s no support for JSON in the native iOS libraries, but the JSON framework provides everything you need, including a parser to turn JSON strings into objects, and a generator to create JSON strings from objects. This library is so popular, and JSON so common, that it’s actually included in many of the other libraries features in this post already. Here’s a quick example:

```objectivec
// JSON string -> NSDictionary
NSString *jsonString = @"{\"foo\": \"bar\"}";
NSDictionary *dictionary = [jsonString JSONValue];
NSLog(@"Dictionary value for \"foo\" is \"%@\"", [dictionary objectForKey:@"foo"]);
// NSDictionary -> JSON string
NSString *newJsonString = [dictionary JSONRepresentation];
```

**[Flurry](http://www.flurry.com/product/analytics/index.html) – Detailed Usage Statistics（详尽的使用统计）**

By adding the flurry SDK to your project you’ll automatically get a load of usage statistics about your application, such as how many users you have, how active they are, and where they are in the world. The real power of flurry though is that it allows you to specify your own events to track, and log errors. All of this information is then available in a Google Analytics style dashboard, so you can see what your users are doing with your app, and what problems they’re running into. You really should be using some kind of usage tracking library, and although alternatives do exist, such as [Google Analytics for Mobile](https://code.google.com/mobile/analytics/download.html) and [Localytics](http://www.localytics.com/), Flurry has worked really well for me.

[**RegexKitLite**](http://regexkit.sourceforge.net/RegexKitLite/) – **Regular Expression Support（正则表达式支持）**

Regular Expressions are a really powerful tool, and the absence of support for regular expressions in the iPhone SDK seems to be a glaring omission. Fortunately the RexexKitLite library is here to help. It’s a powerful fully featured regex library that’s simple to use. Here’s the sample code to match a phone number:

```objectivec
// finds phone number in format nnn-nnn-nnnn
NSString *regEx = @"[0-9]{3}-[0-9]{3}-[0-9]{4}";
for(NSString *match in [textView.text componentsMatchedByRegex:regEx]) {
    NSLog(@"Phone number is %@", match);
}
```

**[Facebook iOS SDK](https://github.com/facebook/facebook-ios-sdk) – Facebook API Library（Facebook API 库）**

Facebook login (previously called Facebook Connect) is used all over the web as a way for users to login to services by using their existing Facebook account, saving them from having to create lots of separate accounts. This library allows you to do the same with your iPhone apps. It also has full support for both the Facebook Graph API and the older REST api, which give you access to the social graph and related Facebook information of your users, and make it easy to implement features such as friend finders and inviters. This library is used by a lot of big name apps for their Facebook integration, so if you want to use Facebook as your primary authentication method or you’d just like to add a friend invite feature this library is well worth checking out.

**[SDWebImage](https://github.com/rs/SDWebImage) – Simple Web Image Support（网络图片支持）**

SDWebImage is a library for dealing with images on the web. It allows you to use images on the web as easily as local files already packaged with your application. It automatically handles caching, and also supports advanced features such as placeholder images and a download queue. Once you’ve added it to your project you can set the image for a UIWebView as simply as:

```objectivec
[imageView setImageWithURL:[NSURL URLWithString:@"http://example.com/image.png"]];
```

Similar functionality is provided by the Three20 library, mentioned later, but if you’re after a simple library that focuses on doing one thing well, and you’re using web based images in your project, then SDBWebImage is what you need.

**[GData client](https://code.google.com/p/gdata-objectivec-client/) – iPhone library for all of Google’s services（iPhone上所有Google相关服务的类库）**

Google’s official GData library allows you to access many of Google’s services, including contacts, calendar, analytics, picasa, translate and YouTube. The project is well documented, and contains lots of example applications. With all of the great services Google offer there are so many different ways that this library could be used to enhance an existing application, and there are probably lots of interesting apps that could be built off the back of the example apps included in this library. If you’re an iOS developer stuck for ideas then this is where I’d suggest you look!

**[CorePlot](https://code.google.com/p/core-plot/) – 2D Graph Plotter（2D图形绘图仪）**

CorePlot makes makes it extremely easy to visualize your data in a variety of ways, and produces very attractive graphs. It supports bar graphs, pie charts, line graphs, and complex mathematical function plotting among others. The library is well documented, and the website contains lots of examples of where it’s already being used, including stock price applications, game scores, personal finance apps, and for web analytics visualization.

**[Three20](https://github.com/facebook/three20) – General iOS Library（通用iOS库）**

The Three20 library came out of the official Facebook iPhone app. It’s a fairly big and full featured library, including low level components such as a HTTP cache, and many higher level UI components such as a photo viewer and web based table view. It can be a little tricky to integrate Three20 into existing projects, but if you’re starting a project from scratch Three20 can really give you a big head start, especially for projects that make heavy use of the web.

Whether it’s interacting with a web API, visualizing data, loading images from the web, or creating social features in your app, the libraries listed here make developing such features easier and less time consuming. If you’re an iOS developer and you haven’t made use of any of these libraries then you should definitely check them out before starting your next project. If you have used any of them, or one that we haven’t mentioned, then please let us know your experiences in the comments.（有了更多的库，会让你的开发更容易，生活更美好）

