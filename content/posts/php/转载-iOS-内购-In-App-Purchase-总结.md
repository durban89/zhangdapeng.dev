---
title: "转载 - iOS 内购（In-App Purchase）总结"
date: "2025-07-11 10:40:18"
slug: "zhuan-zai-ios-nei-gou-in-app-purchase-zong-jie"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/07/11/转载-iOS-内购（In-App-Purchase）总结/"
  - "/2025/07/11/转载-iOS-内购（In-App-Purchase）总结.html"
  - "/转载-iOS-内购（In-App-Purchase）总结/"
  - "/转载-iOS-内购（In-App-Purchase）总结.html"
  - "/2025/07/11/转载-iOS-内购-In-App-Purchase-总结/"
  - "/2025/07/11/转载-iOS-内购-In-App-Purchase-总结.html"
  - "/2025/07/11/zhuan-zai-ios-nei-gou-in-app-purchase-zong-jie/"
  - "/2025/07/11/zhuan-zai-ios-nei-gou-in-app-purchase-zong-jie.html"
  - "/zhuan-zai-ios-nei-gou-in-app-purchase-zong-jie.html"
---
IAP 全称：`In-App Purchase`，是指苹果 App Store 的应用内购买，是苹果为 App 内购买虚拟商品或服务提供的一套交易系统

### **IAP 的适用范围**

在 App 内需要付费使用的产品功能或虚拟商品/服务，如游戏道具、电子书、音乐、视频、订阅会员、App的高级功能等需要使用 IAP，而在 App 内购买实体商品（如淘宝购买手机）或者不在 App 内使用的虚拟商品（如充话费）或服务（如滴滴叫车）则不适用于 IAP

简而言之，苹果规定：适用范围内的虚拟商品或服务，必须使用 IAP 进行购买支付，不允许使用支付宝、微信支付等其它第三方支付方式（包括Apple Pay），也不允许以任何方式（包括跳出App、提示文案等）引导用户通过应用外部渠道购买

### **iOS 内购的准备**

App 内集成内购代码之前需要先去开发账号的 Itunes Connect 后台填写银行账户信息、配置内购商品（包括产品ID、价格等），还需要配置沙盒账号用于 IAP 测试

**银行账户信息填写**

关于如何去 Itunes Connect 后台填写账户信息，本文不做讨论，可以参考以下文章：

[iOS内购一条龙—账户信息填写](https://www.jianshu.com/p/4f5f0b45b083)

**配置内购商品**

IAP 是一套商品交易系统，而非简单的支付系统，每一个购买项目都需要在开发者后台的Itunes Connect后台为 App 创建一个对应的商品，提交给苹果审核通过后，购买项目才会生效

Itunes Connect 后台选择 `我的APP`，选择需要内购 App，选择 `功能`，可以进入到配置内购商品的页面

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum1.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum1.png)

新建内购商品有四种选择分别是：

* **消耗型项目**：只可使用一次的产品，使用之后即失效，必须再次购买，如：游戏币、一次性虚拟道具等
* **非消耗型项目**：只需购买一次，不会过期或随着使用而减少的产品。如：电子书
* **自动续期订阅**：允许用户在固定时间段内购买动态内容的产品。除非用户选择取消，否则此类订阅会自动续期，如：Apple Music这类按月订阅的商品
* **非续期订阅**：允许用户购买有时限性服务的产品，此 App 内购买项目的内容可以是静态的。此类订阅不会自动续期

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum2.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum2.png)

一般情况下用的最多的是消耗型商品，根据 App 类型也会使用到非消耗型和自动续期订阅，以消耗型商品举例

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum3.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum3.png)

这里需要注意的是产品 ID 具有唯一性，建议使用项目的 `Bundle Identidier` 作为前缀后面拼接自定义的唯一的商品名或者 ID（字母、数字），这里有个坑：**一旦新建一个内购商品，它的产品ID将永远被占用，即使该商品已经被删除**，已创建的内购商品除了产品 ID 之外的所有信息都可以修改，如果删除了一个内购商品，将无法再创建一个相同产品 ID 的商品，也意味着该产品 ID 永久失效，一般来说产品ID有特定的命名规则，如果命名规则下有某个产品 ID 永久失效，可能会导致整个产品ID命名规则都要修改，这里千万要注意！

另外内购商品的定价只能从苹果提供的价格等级去选择，这个价格等级是固定的，同一价格等级会对应各个国家的货币，也就是说内购商品的价格是根据 Apple ID 所在区域的货币进行结算的，比如：一个内购商品你选择等级1，那么这个商品在美区是 0.66 美元，在中区是 6 元人民币，在香港去是 8 港币，这些价格一般是固定的，除非某些货币出现大的变动（印象中有过一次卢布大跌，苹果调整过俄区的价格），价格等级表可以点击上图右边的 `所有价格和货币` 查看

另外要注意：**苹果内购是需要抽取30%的分成**，实际结算是分成之前需要先扣除交易税，不同地区交易税不同，具体分成数额参看价格表

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum4.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum4.png)

iOS 11 用户可以在 App Store 内 App 的下载页面内直接购买应用的内购商品，这项功能苹果称作做 `Promoting In-App Purchases`，如果你的 App 需要在 App Store 推广自己的内购商品，则需要在上图的 `App Store 推广` 里上传推广用的图像，另外苹果也在 iOS11 SDK 里面新增了从 App Store 购买内购项目跳转到 App 的新方法

**配置沙箱测试账号**

内购也是需要测试的，但是内购涉及到钱，所以苹果为内购测试提供了 `沙箱测试账号` 的功能，Apple Pay 推出之后 `沙箱测试账号` 也可以用于 Apple Pay 支付的测试，`沙箱测试账号` 简单理解就是：只能用于内购和 Apple Pay 测试功能的 Apple ID，它并不是真实的 Apple ID，下面看如何创建 `沙箱测试账号`

Itunes Connect 后台选择 `用户和职能`，选择 `+` 添加测试账号

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum6.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum6.png)

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum7.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum7.png)

填写沙箱测试账号信息需要注意以下几点：

* 电子邮件不能是别人已经注册过 AppleID 的邮箱
* 电子邮箱可以不是真实的邮箱，但是必须符合邮箱格式
* App Store 地区的选择，测试的时候弹出的提示框以及结算的价格会按照沙箱账号选择的地区来，建议测试的时候新建几个不同地区的账号进行测试

配置好测试账号之后，看一下沙箱账号测试的时候如何使用：

* 首先沙箱测试账号必须在真机环境下进行测试，并且是 adhoc 证书或者 develop 证书签名的安装包，沙盒账号不支持直接从 App Store 下载的安装包
* 去真机的 App Store 退出真实的 Apple ID 账号，退出之后并不需要在App Store 里面登录沙箱测试账号
* 然后去 App 里面测试购买商品，会弹出登录框，选择 `使用现有的 Apple ID`，然后登录沙箱测试账号，登录成功之后会弹出购买提示框，点击 `购买`，然后会弹出提示框完成购买

[![](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum8.png)](https://blog-images-1256154150.cos.ap-guangzhou.myqcloud.com/iap_sum8.png)

上面说了这么多只是集成内购的一些准备，真正重要的是下面的内购代码的实现

### **iOS 内购具体代码**

写代码之前先来了解对比一下 IPA 和支付宝支付，首先看支付宝的支付流程：

* App 发起一笔支付交易，然后服务端根据支付宝的要求把订单信息进行加密签名
* 服务端把加密的交易信息返回给 App，App 拿到交易信息调用支付宝的 SDK，把支付信息给到支付宝的服务端验证
* 验证通过后，App 跳转到支付宝 App 或者网页版支付宝，用户使用支付宝进行支付
* 支付成功后从支付宝 App 跳转回到我们自己 APP，我们在 App 里处理回调结果刷新UI等
* 同时支付宝的服务器也会回调我们自己服务器，把收据传给服务器，支付宝服务器会一直回调我们的服务器直到我们的服务器确认收到收据
* 我们的服务器收到回调确认之后，确认订单支付成功
* 为了以防万一，App 上回调返回成功之后我们还需要去自己服务器验证是否真的支付成功（一切以服务器为准）

微信支付和支付宝支付的流程是类似的，来看看 IAP 的支付流程：

* App 发起一笔内购支付，然后服务端生成一个订单号并且返回给 App
* App 拿到交易订单之后调用 IPA 创建一个 IPA 交易，并且添加到支付队列
* 然后 IAP 会调用 Apple ID 支付页面等待用户确认支付，IPA 和苹果自己的 IPA 服务器通讯，回调购买成功，并且把收据写入 App 沙盒
* 然后 App 去沙盒获取收据并且上传到自己的服务器
* 服务器去 IAP 服务器查询收据的有效性并且对应到某个订单号，如果有效就通知 App，并且发放该内购商品，App 调用IAP 支付队列去结束该 IPA 交易

对比来看两者区别好像也不大，支付宝或者微信支付，一旦App 端支付成功，之后的验证工作就完全是我们的服务器和支付宝服务器之前的通讯了，服务端之间的通讯就保证了交易的可靠性，但是看看 IAP，同样的交易，服务端的验证却需要 App 端去驱动，由于 App 的网络环境比服务端复杂、用户操作的不确定性可能会导致 APP 无法正确的驱动服务端验证交易，另一方面 IAP 的服务器在美国，验证查询交易的延迟也很严重

苹果 IAP 的那些坑后面再讲，先按照上面的流程，我们把 IPA 代码的逻辑理一理：

```swift
import UIKit
import StoreKit
class ViewController: UIViewController, SKProductsRequestDelegate,SKPaymentTransactionObserver {
    override func viewDidLoad() {
        super.viewDidLoad()

        // 监听支付队列
        SKPaymentQueue.default().add(self as SKPaymentTransactionObserver)
    }
    deinit {

        SKPaymentQueue.default().remove(self as SKPaymentTransactionObserver)
    }

    // 点击购买
    @IBAction func buy(_ sender: UIButton) {

        if SKPaymentQueue.canMakePayments() {

            requestProductInfo("com.xiaovv.IAPDemo.vip1")

        }else {
            print("用户禁止购买")
        }
    }
    // 请求查询 iTunes Connect 后台配置的内购商品
    fileprivate func requestProductInfo (_ productId: String) {

        let identifiers: Set<String> = [productId]

        let request = SKProductsRequest(productIdentifiers: identifiers)

        request.delegate = self
        request.start()
    }

    fileprivate func transcationPurchasing(_ transcation: SKPaymentTransaction) {

        print("交易中...")
    }

    fileprivate func transcationPurchased(_ transcation: SKPaymentTransaction) {

        print("交易成功...")
        // 持久化订单信息
        if let receiptUrl = Bundle.main.appStoreReceiptURL {//获取收据地址

            let receipt = NSData(contentsOf: receiptUrl)

            let receiptStr = receipt?.base64EncodedString(options: NSData.Base64EncodingOptions(rawValue: 0))

            DispatchQueue.main.asyncAfter(deadline: DispatchTime(uptimeNanoseconds: 3)) {// 模拟上传收据到服务端

                print("receiptStr:\(String(describing: receiptStr))")
                print("applicationUsername:\(String(describing: transcation.payment.applicationUsername))")
                // 收据发送到服务器
                // 收据验证成功之后结束交易
                SKPaymentQueue.default().finishTransaction(transcation)
                // 删除保存的订单信息
            }   
        }
    }

    fileprivate func transcationFailed(_ transcation: SKPaymentTransaction) {

        print("交易失败...")
    }

    fileprivate func transcationRrestored(_ transcation: SKPaymentTransaction) {

        print("已经购买该商品...")
    }

    fileprivate func transcationDeferred(_ transcation: SKPaymentTransaction) {

        print("交易延期...")
    }

    //MARK: - SKPaymentTransactionObserver
    // 购买内购商品之后会调用的代理方法
    func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction]) {

        for transcation in transactions {

            switch (transcation.transactionState) {

                case .purchasing:
                    transcationPurchasing(transcation)
                case .purchased:
                    transcationPurchased(transcation)
                case .failed:
                    transcationFailed(transcation)
                case .restored:
                    transcationRrestored(transcation)
                case .deferred:
                    transcationDeferred(transcation)
                }
        }
    }

    //MARK: - SKProductsRequestDelegate
    // 查询iTunes Connect 后台内购商品的回调代理方法
    func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) {

        if response.products.count > 0 {

            let payment = SKMutablePayment(product: response.products.first!)

            // applicationUsername 可以把我们的自己订单和IAP的交易订单绑定
            payment.applicationUsername = "orderid，userid and so on"

        }else {
            print("没有可以购买的商品")
        }
    }
}
```

IAP 的代码看起来并不多流程也比较清晰，主要是下面几步：

* 根据内购商品的产品 ID 初始化一个 `SKProductsRequest` 对象，调用该对象的 `start()` 方法进行内购商品的请求
* 把商品请求中获取到的 `SKProduct` 对象生成一个 `SKPayment` 对象，并把它压入到 `SKPaymentQueue` 支付队列中
* 然后从支付队列的代理方法 `func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])` 里面获取到交易（transaction）的状态，交易完成后调用支付队列的 `finishTransaction()`完成内购支付

### **iOS 内购减少丢单处理**

上面说到 IAP 的坑，下面就列举一下 IAP 留给开发者的 “坑”：

1. 用户输入完 Apple ID 密码或者验证完指纹支付成功之后，网络突然中断导致 IAP 没有收到支付成功的通知，App 就无法在支付队列的代理方法中获取支付成功的通知，后续的发放内购商品也就不可能了
2. App 在代理方法里收到了支付成功的通知，但是 App 上传交易收据到我们服务器去查询的时候如果查询失败，那么服务器就无法发放内购商品，因为这个行为是 App 驱动服务器的行为，这里有个坑就是支付队列的代理方法 `func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])` 需要下次 App 重新启动才会重新调用，这个时候我们 App 才能重新去驱动服务器查询交易，由于用户操作的不确定性，不知道什么时候用户才会重新打开App，发放内购商品的周期自然也不确定
3. 之前有开发者反应，IAP 通知代理方法交易成功，但是沙盒里面取收据的时候发现为空，或者当前支付成功的订单并没有写入沙盒的收据，导致上传到服务器的收据查询不到结果
4. 如果用户支付成功，收据也上传服务器成功，但是在服务器验证阶段用户删除了App，导致App 无法去处理这些没有被验证完的订单
5. 如何处理越狱iOS手机内购的问题

以上问题都可能会导致用户支付成功了，却收不到我们发放的内购商品，统一起来称为：**内购丢单**

接下来讨论一下如何处理 IAP 支付的一些细节问题克服上述 IAP 的坑

**越狱问题**

我本人也折腾过 iOS 越狱，安装实用插件、美化主题等，自从iOS 9 之后越狱社区越来越不活跃了，能完美越狱的基本都是iPhone 5 以及更老的 32位设备了，这也侧面也说明了 iOS 在功能方面已经非常完善了，导致折腾越狱的人越来越少了，当前 iOS 版本是否越狱可以去这个网站查看：**[Can I jailbreak](https://canijailbreak.com/)**

回归正题，因为越狱之后会导致系统不确定的问题很多，我觉得可以采用宁可错杀一千也不放过一个原则，对于已越狱的iOS 设备全部不允许内购行为，简单粗暴有效，可以通过下面工具的方法判断iOS设备是否越狱

```objectivec
.h 文件
#import <Foundation/Foundation.h>
@interface JailbreakDetectTool : NSObject
/**
 * 检查当前设备是否已经越狱。
 */
+ (BOOL)detectCurrentDeviceIsJailbroken;
@end
.m 文件
#import "JailbreakDetectTool.h"
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])
@implementation JailbreakDetectTool
// 四种检查是否越狱的方法, 只要命中一个, 就说明已经越狱.
+ (BOOL)detectCurrentDeviceIsJailbroken {
    BOOL result =  NO;

    result = [self detectJailBreakByJailBreakFileExisted];

    if (!result) {
        result = [self detectJailBreakByAppPathExisted];
    }

    if (!result) {
        result = [self detectJailBreakByEnvironmentExisted];
    }

    if (!result) {
        result = [self detectJailBreakByCydiaPathExisted];
    }

    return result;
}
/**
 * 判定常见的越狱文件
 * /Applications/Cydia.app
 * /Library/MobileSubstrate/MobileSubstrate.dylib
 * /bin/bash
 * /usr/sbin/sshd
 * /etc/apt
 * 这个表可以尽可能的列出来，然后判定是否存在，只要有存在的就可以认为机器是越狱了。
 */
const char* jailbreak_tool_pathes[] = {
    "/Applications/Cydia.app",
    "/Library/MobileSubstrate/MobileSubstrate.dylib",
    "/bin/bash",
    "/usr/sbin/sshd",
    "/etc/apt"
};
+ (BOOL)detectJailBreakByJailBreakFileExisted {
    for (int i = 0; i<ARRAY_SIZE(jailbreak_tool_pathes); i++) {
        if ([[NSFileManager defaultManager] fileExistsAtPath:[NSString stringWithUTF8String:jailbreak_tool_pathes[i]]]) {
            NSLog(@"The device is jail broken!");
            return YES;
        }
    }
    NSLog(@"The device is NOT jail broken!");
    return NO;
}
/**
 * 判断cydia的URL scheme.
 */
+ (BOOL)detectJailBreakByCydiaPathExisted {
    if ([[UIApplication sharedApplication] canOpenURL:[NSURL URLWithString:@"cydia://"]]) {
        NSLog(@"The device is jail broken!");
        return YES;
    }
    NSLog(@"The device is NOT jail broken!");
    return NO;
}
/**
 * 读取系统所有应用的名称.
 * 这个是利用不越狱的机器没有这个权限来判定的。
 */
#define USER_APP_PATH                 @"/User/Applications/"
+ (BOOL)detectJailBreakByAppPathExisted {
    if ([[NSFileManager defaultManager] fileExistsAtPath:USER_APP_PATH]) {
        NSLog(@"The device is jail broken!");
        NSArray *applist = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:USER_APP_PATH error:nil];
        NSLog(@"applist = %@", applist);
        return YES;
    }
    NSLog(@"The device is NOT jail broken!");
    return NO;
}
/**
 * 这个DYLD_INSERT_LIBRARIES环境变量，在非越狱的机器上应该是空，越狱的机器上基本都会有Library/MobileSubstrate/MobileSubstrate.dylib.
 */
char* printEnv(void) {
    char *env = getenv("DYLD_INSERT_LIBRARIES");
    return env;
}
+ (BOOL)detectJailBreakByEnvironmentExisted {
    if (printEnv()) {
        NSLog(@"The device is jail broken!");
        return YES;
    }
    NSLog(@"The device is NOT jail broken!");
    return NO;
}
@end
```

**储存交易订单**

上述第1、2点坑都是因为交易订单支付成功了，但是没有完成服务器验证收据，所以我们非常有必要持久化我们的订单信息，IAP 支付成功的交易（transaction）只要没有调用 `finishTransaction()`，下次启动 App 重新监听支付队列的时候会重新调用 `func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])` 这个时候就可以重新获取到未完成的该交易（transaction）

支付成功后，我们持久化自己订单信息的目的就是和 IAP的交易（transaction）绑定起来，这样如果在App驱动服务器验证订单的时候出现了异常，App重新启动之后我们获取到未完成的 IAP的交易（transaction）之后依然可以和我们自己的订单联系起来，然后可以继续发送给后台服务器去去验证，直到验证成功完成 IAP 交易（transaction），购买结束

这里我的做法是：用户支付成功之后用 `UserDefault` 把该交易的交易标识（transactionIdentifier）和我们自己的交易订单作为字典的键值保存在沙盒内，然后把我们自己的订单号和支付收据发送给服务器去验证，服务器返回验证结果之后，删除 `UserDefault` 中的订单信息，并且完成该笔IAP 交易（transaction），如果在服务器返回验证结果之前出现异常（用户杀掉App、手机关机了，App崩溃等）订单信息便不会从`UserDefault` 中删除，该笔IAP 交易也不会被完成，App重新启动之后，重新监听支付队列的时候，可以重新获取到该笔交易（transaction），然后根据该笔交易（transaction）的交易标识（transactionIdentifier）找到 `UserDefault` 中对应的我们自己的订单号，重新把订单号和交易收据发送给后台服务器验证

我们自己的订单是后台生成并且和用户ID进行了绑定的，所以这里不担心用户支付成功之后，切换 App 账号会把内购商品发放给另一个用户

我的做法比较简单，实际上用户如果删除 App，`UserDefault` 的订单信息就会丢失，所以订单信息储存在钥匙串 `keychain` 才是相对最稳妥的，特别是如果你的项目以内购为主并且支付非常频繁，这里可以参看贝聊的做法 [贝聊 IAP 实战之见坑填坑](https://www.jianshu.com/p/8e5bf711f9f0)

**applicationUsername**

由于 IAP 支付成功之后我们只能从 IAP 的代理方法里面获取到支付成功的交易（transaction），所以我们就必须把自己的订单号和对应的 IAP 交易（transaction）绑定在一起，IAP 创建 `SKPayment` 对象，并把它压入到`SKPaymentQueue` 支付队列的时候，我们可以使用可变的 `SKMutablePayment`，它有一个属性叫做 `applicationUsername`，这个属性就可以用来储存我们自己生成的订单号信息，用户支付成功之后可以成功的交易（transaction）的 `payment` 中获取到绑定的订单号信息，这样就可以完美的把 IAP交易（transaction）和我们自己的订单号绑定在一起了

但是，但是！苹果在这个属性上面有个巨坑，前面说到如果某个IAP交易（transaction）支付成功但是并没有调用 `finishTransaction()`去完成这个交易的时候，下次启动 App 重新监听支付队列的时候会重新调用 `func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])` 这个时候就可以重新获取到这个未完成的交易（transaction），苹果的坑就是这个时候获取 transaction 的 payment 的  applicationUsername 会出现 nil 的情况，所以实际开发中不能完全去相信这个 `applicationUsername` 属性，这也是为什么上面我要把自己的订单号和 IAP 交易（transaction）的交易标识持久化下来的原因

**其他错漏问题**

第3点坑，用户支付成功之后从沙盒获取收据为空，IAP 提供了一个`SKReceiptRefreshRequest`类，通过这个类可以在收据无效或者丢失的时候申请到新的收据，`SKReceiptRefreshRequest`继承自 `SKRequest` 和 `SKProductsRequest` 都遵循 `SKRequestDelegate`

第4点坑，如果我们的订单信息是持久化到钥匙串中，那么即使 App 被删除，下次重新安装的时候依然可以拿到持久化的订单信息

实际上即使把上面的问题全部考虑到了依然还可能出问题，比如用户切换了 Apple ID 这个时候钥匙串里持久化的订单信息也会发生改变、或者验证成功之前用户换新的手机登录或者用户其他的不可预知的操作行为依然会导致错漏单的问题，但是我觉得内购大部分时候是用户一种强意识的行为，上面这些操作只能是认为用户在阻止自己购买成功，所以我们最终是无法百分之百避免错漏单的，手动去处理这些订单是非常有必要的

### **IAP 服务端的处理**

前面说到用户支付成功之后，我们拿到沙盒的收据信息去苹果的 IAP 服务器去验证，这里既可以直接在 App 端验证也可以让服务器去验证，实际上根据我的测试，App 端直接去IAP服务器验证比较快，毕竟中间少了很多步骤，但是考虑到越狱的 iOS 设备完全可以在系统层面跳过或者伪造收据，早期的 iOS 开发很多公司都是采用都是这种本地验证，但是现在基本都是通过后台验证的方式，具体的后台验证步骤如下：

* App端拿到沙盒的收据（receipt-data）,进行一次base64编码，上传给服务器
* 服务器拿到收据之后发到 IAP 服务器去验证，验证成功之后收据需要和自己的订单号进行映射并且记录在数据库，之后每次验证之前都需要先判断收据是否存在，防止 App 端重复上传相同的收据，重复发放内购商品
* 服务器发放内购商品，推送通知给用户等

由于 App 上线 App Store 之前我们是使用沙盒账号测试的，沙盒测试的收据验证也是要去沙盒收据的服务器验证

* 沙盒环境验证服务器：<https://sandbox.itunes.apple.com/verifyReceipt>
* 正式环境验证服务器：<https://buy.itunes.apple.com/verifyReceipt>

而且苹果在上线审核的时候也是使用沙盒账号测试的，那如何识别App端发过来的收据是沙盒测试还是正式环境用户的购买呢？这里服务端就要采用双重验证，即先把收据拿到正式环境的验证地址去验证，如果苹果的正式环境验证服务器返回的状态码 status 为 21007，则说明当前收据是沙盒环境产生，则再连接一次沙盒环境服务器进行验证，这样不管是我们自己采用沙盒账号测试还是苹果审核人员采用沙盒账号进行审核、或者用户购买都可以保证收据正常的验证成功

### **沙盒测试遇到的其他问题**

* 在进行沙盒测试的时候，遇到过 IAP 沙盒服务器出现异常，购买过程非常的慢，而且总是超时，返回购买失败，谷歌到有同行也出现过沙盒购买缓慢的问题（[iTunes Sandbox Extremely Slow](https://forums.developer.apple.com/thread/96389)），所以如果确定代码没有问题，多半就是 IAP 的沙盒服务器出现了问题，建议换个时间再测试，可以通过 [System Status - Apple Developer](https://developer.apple.com/system-status/) 查看苹果公司开发者相关的服务的服务状态
* 如果内购的时候提示 **`您已购买此 App 内购买项目。此项目将免费恢复。`**，说明有一个购买了同一商品 IAP 交易（transaction）没有调用 `finishTransaction()`去结束这个交易

### **Promoting In-App Purchases**

前面提到iOS 11 之后，开发者可以在 App Store 自己App的下载页面推广自己的内购商品，用户可以直接在App下载页面购买内购商品，这就涉及到从App Store跳转到自己App，所以苹果在 `SKPaymentTransactionObserver` 新增了一个代理方法：

```objectivec
func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment, 
for product: SKProduct) -> Bool {

    return false
}
```

用户如果在 App下载页面点击购买你推广的内购商品，如果用户已经安装过你的 App 则会直接跳转你的App并调用上述代理方法；如果用户还没有安装你的 App 那么就会去下载你的 App，下载完成之后系统会推送一个通知，如果用户点击该通知就会跳转到你的App并且调用上面的代理方法

上面的代理方法返回 `true` 则表示跳转到你的 App，IAP 继续完成交易，如果返回 `false` 则表示推迟或者取消购买，实际开发中因为可能还需要用户登录自己的账号、生成订单等，一般都是返回 `false`，之后自己手动把代理方法里面返回的 `SKPayment` 加入支付队列，然后在按照自己的支付、验证逻辑完成支付

**以上就是我做内购的时候从网上的资料以及官方文档总结的一些东西**

参考和推荐阅读：

[iOS内购一条龙——账户信息填写](https://www.jianshu.com/p/4f5f0b45b083)

[苹果应用内购买(IAP)—从入门到放弃](http://www.pmcaff.com/article/index/968640397863040?from=related&pmc_param%5Bentry_id%5D=975040810207296)

[iOS 贝聊 IAP 实战之满地是坑](https://www.jianshu.com/p/07b5ec193353)

[苹果IAP开发中的那些坑和掉单问题](http://zhangtielei.com/posts/blog-iap.html)

[Receipt Validation Programming Guide](https://developer.apple.com/library/content/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573-CH105-SW1)

[In-App Purchase Programming Guide](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

[收据验证编程指南](https://developer.apple.com/cn/app-store/Receipt-Validation-Programming-Guide-CN.pdf)

[iOS内购充值 服务器端处理](http://cwqqq.com/2017/12/05/ios_in-app_pay_server_side_code)

[iOS 内购服务器验票（漏单处理）](https://blog.csdn.net/goodeveningbaby/article/details/53372934)
