---
title: "iOS与JavaScript交互: MessageHandler"
date: "2025-07-15 09:51:00"
slug: "ios-yu-javascript-jiao-hu-messagehandler"
categories: ["技术"]
tags: ["iOS", "JavaScript"]
aliases:
  - "/2025/07/15/iOS与JavaScript交互:-MessageHandler/"
  - "/2025/07/15/iOS与JavaScript交互:-MessageHandler.html"
  - "/iOS与JavaScript交互:-MessageHandler/"
  - "/iOS与JavaScript交互:-MessageHandler.html"
  - "/2025/07/15/iOS与JavaScript交互-MessageHandler/"
  - "/2025/07/15/iOS与JavaScript交互-MessageHandler.html"
  - "/2025/07/15/ios-yu-javascript-jiao-hu-messagehandler/"
  - "/2025/07/15/ios-yu-javascript-jiao-hu-messagehandler.html"
  - "/ios-yu-javascript-jiao-hu-messagehandler.html"
---
WKWebView有一个内容交互控制器，该对象提供了通过JS向WKWebView发送消息的途径。需要设置MessageHandler，我把这个功能简称为MessageHandler。

首先了解下iOS开发中需要调用的方法

`- (void)addScriptMessageHandler:(id <WKScriptMessageHandler>)scriptMessageHandler name:(NSString *)name;`

和

`- (void)removeScriptMessageHandlerForName:(NSString *)name;`

下面看下如何调用

添加MessageHandler

```objectivec
[self.webView.configuration.userContentController addScriptMessageHandler:self name:@"showAlert"];
```

移除MessageHandler

```objectivec
[self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"showAlert"];
```

### JS调用

`window.webkit.messageHandlers.<name>.postMessage(<messageBody>)`

这个name就是设置MessageHandler的第二个参数

```objectivec
window.webkit.messageHandlers.getString.postMessage(null);
```

### 注意点

在JS中写起来简单，不用再用创建URL的方式那么麻烦了。

JS传递参数更方便。使用拦截URL的方式传递参数，只能把参数拼接在后面，如果遇到要传递的参数中有特殊字符，如&、=、?等，必须得转换，否则参数解析肯定会出错。

### 示例演示

html代码部分

四个按钮分别演示JS传NULL给WKWebView，然后WKWebView调用JS方法；JS传字符串、JS传数组、JS传字典改变导航背景。

```html
<!DOCTYPE html>
<html lang="zh-cn">

<head>
  <meta charset="UTF-8">
  <title>Title</title>
  <script>
  function loadURL(url) {
    var iFrame;
    iFrame = document.createElement("iframe");
    iFrame.setAttribute("src", url);
    iFrame.setAttribute("style", "display:none;");
    iFrame.setAttribute("height", "0px");
    iFrame.setAttribute("width", "0px");
    iFrame.setAttribute("frameborder", "0");
    document.body.appendChild(iFrame);
    // 发起请求后这个iFrame就没用了，所以把它从dom上移除掉
    iFrame.parentNode.removeChild(iFrame);
    iFrame = null;
  }

  function asyncAlert(content) {
    setTimeout(function(){
      alert(content);
    },1);
  }

  function showAlert() {
    window.webkit.messageHandlers.showAlert.postMessage(null);
  }

  function alertWithMessage(content) {
    asyncAlert(content);
    document.getElementById("returnValue").value = content;
  }

  function postString() {
    window.webkit.messageHandlers.postString.
    postMessage('r=10,g=170,b=250,a=0.5');
  }

  function postArray() {
    window.webkit.messageHandlers.postArray.
    postMessage([Math.floor(Math.random()*255),
           Math.floor(Math.random()*255),
           Math.floor(Math.random()*255),0.5]);
  }

  function postDictionary() {
    window.webkit.messageHandlers.postDictionary.
    postMessage({red: Math.floor(Math.random()*255), 
           green: Math.floor(Math.random()*255),
           blue: Math.floor(Math.random()*255),
           alpha: 0.5});
  }

  </script>
</head>

<body>
  <input type="button" value="OC调用JS方法" onclick="showAlert()">
  <input type="button" value="JS传字符串" onclick="postString()">
  <input type="button" value="JS传数组" onclick="postArray()">
  <input type="button" value="JS传字典" onclick="postDictionary()">
</body>

</html>
```

object-c代码部分

- 加载WKWebView

```objectivec
- (void)loadWebView {
    // 偏好配置
    WKWebViewConfiguration *config = [WKWebViewConfiguration new];
    config.preferences = [WKPreferences new];
    config.preferences.minimumFontSize = 30.0f;
    config.preferences.javaScriptCanOpenWindowsAutomatically = YES;

    self.webView = [[WKWebView alloc] initWithFrame:self.view.bounds configuration:config];
    self.webView.UIDelegate = self; // 设置交互代理
    [self.view addSubview:self.webView];

    // 加载HTML
    NSString *path = [[NSBundle mainBundle] pathForResource:@"index2" ofType:@"html"];
    NSString *htmlStr = [NSString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil];
    [self.webView loadHTMLString:htmlStr baseURL:nil];
}
```

- 添加和移除处理

```objectivec
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    [self.webView.configuration.userContentController addScriptMessageHandler:self name:@"showAlert"];
    [self.webView.configuration.userContentController addScriptMessageHandler:self name:@"postString"];
    [self.webView.configuration.userContentController addScriptMessageHandler:self name:@"postArray"];
    [self.webView.configuration.userContentController addScriptMessageHandler:self name:@"postDictionary"];
}

- (void)dealloc {
    [self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"showAlert"];
    [self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"postString"];
    [self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"postArray"];
    [self.webView.configuration.userContentController removeScriptMessageHandlerForName:@"postDictionary"];
}
```

- 实现协议

我这里实现了两个协议 WKUIDelegate,WKScriptMessageHandler，WKUIDelegate是因为我在JS中弹出了alert。WKScriptMessageHandler是因为我们要处理JS调用OC方法的请求。

```objectivec
#pragma mark - WKScriptMessageHandler
- (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message {
    if ([message.name isEqualToString:@"showAlert"]) {
        [self alert];
    }
    else if ([message.name isEqualToString:@"postString"]) {
        [self changeColorWithString:message.body];
    }
    else if ([message.name isEqualToString:@"postArray"]) {
        [self changeColorWithArray:message.body];
    }
    else if ([message.name isEqualToString:@"postDictionary"]) {
        [self changeColorWithDictionary:message.body];
    }
}

- (void)alert {
    // OC调用JS
    NSString *jsStr = [NSString stringWithFormat:@"alertWithMessage('%@')", @"OC调用JS的方法"];
    [self.webView evaluateJavaScript:jsStr completionHandler:^(id _Nullable result, NSError * _Nullable error) {
        NSLog(@"%@----%@",result, error);
    }];
}

- (void)changeColorWithString:(NSString *)string {
    NSArray *params =[string componentsSeparatedByString:@","];

    NSMutableDictionary *tempDic = [NSMutableDictionary dictionary];
    for (NSString *paramStr in params) {
        NSArray *dicArray = [paramStr componentsSeparatedByString:@"="];
        if (dicArray.count > 1) {
            NSString *decodeValue = [dicArray[1] stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
            [tempDic setObject:decodeValue forKey:dicArray[0]];
        }
    }
    CGFloat r = [[tempDic objectForKey:@"r"] floatValue];
    CGFloat g = [[tempDic objectForKey:@"g"] floatValue];
    CGFloat b = [[tempDic objectForKey:@"b"] floatValue];
    CGFloat a = [[tempDic objectForKey:@"a"] floatValue];

    self.navigationController.navigationBar.backgroundColor = [UIColor colorWithRed:r/255.0 green:g/255.0 blue:b/255.0 alpha:a];
}

- (void)changeColorWithArray:(NSArray *)array {
    CGFloat r = [array[0] floatValue]/255.0;
    CGFloat g = [array[1] floatValue]/255.0;
    CGFloat b = [array[2] floatValue]/255.0;
    CGFloat alpha = [array[3] floatValue];
    self.navigationController.navigationBar.backgroundColor = [UIColor colorWithRed:r green:g blue:b alpha:alpha];
}

- (void)changeColorWithDictionary:(NSDictionary *)dict {
    CGFloat r = [dict[@"red"] floatValue]/255.0;
    CGFloat g = [dict[@"green"] floatValue]/255.0;
    CGFloat b = [dict[@"blue"] floatValue]/255.0;
    CGFloat alpha = [dict[@"alpha"] floatValue];
    self.navigationController.navigationBar.backgroundColor = [UIColor colorWithRed:r green:g blue:b alpha:alpha];
}
```

- WKWebView中使用弹窗

```objectivec
#pragma mark - WKUIDelegate
- (void)webView:(WKWebView *)webView runJavaScriptAlertPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(void))completionHandler {
    UIAlertController *alertCrontroller = [UIAlertController alertControllerWithTitle:@"提示" message:message preferredStyle:UIAlertControllerStyleAlert];
    [alertCrontroller addAction:[UIAlertAction actionWithTitle:@"知道了" style:UIAlertActionStyleCancel handler:^(UIAlertAction * _Nonnull action) {
        completionHandler();
    }]];
    [self presentViewController:alertCrontroller animated:YES completion:nil];
}
```

文章参考：https://www.jianshu.com/p/160f529e16fa
