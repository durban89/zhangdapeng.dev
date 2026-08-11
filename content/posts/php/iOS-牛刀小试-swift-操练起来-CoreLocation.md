---
title: "iOS 牛刀小试 swift- 操练起来【CoreLocation】"
date: "2025-06-30 11:49:13"
slug: "ios-niu-dao-xiao-shi-swift-cao-lian-qi-lai-corelocation"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/30/iOS-牛刀小试-swift-操练起来【CoreLocation】/"
  - "/2025/06/30/iOS-牛刀小试-swift-操练起来【CoreLocation】.html"
  - "/iOS-牛刀小试-swift-操练起来【CoreLocation】/"
  - "/iOS-牛刀小试-swift-操练起来【CoreLocation】.html"
  - "/2025/06/30/iOS-牛刀小试-swift-操练起来-CoreLocation/"
  - "/2025/06/30/iOS-牛刀小试-swift-操练起来-CoreLocation.html"
  - "/2025/06/30/ios-niu-dao-xiao-shi-swift-cao-lian-qi-lai-corelocation/"
  - "/2025/06/30/ios-niu-dao-xiao-shi-swift-cao-lian-qi-lai-corelocation.html"
  - "/ios-niu-dao-xiao-shi-swift-cao-lian-qi-lai-corelocation.html"
---
最近看了关于ios的另一门语言swift，找了个示例，操作了一下，遇到了点小问题，不过最终还是解决了。

先看代码

```objectivec
import UIKit
import CoreLocation
 
class ViewController: UIViewController,CLLocationManagerDelegate {
 
    let locationManager:CLLocationManager = CLLocationManager()
     
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
         
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
         
        if(ios8()){
            locationManager.requestAlwaysAuthorization()
        }
         
        locationManager.startUpdatingLocation()
    }
     
    func ios8() -> Bool{
        return UIDevice.currentDevice().systemVersion == "8.1"
    }
 
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
 
    func locationManager(manager: CLLocationManager!, didUpdateLocations locations: [AnyObject]!) {
         
        var location:CLLocation = locations[locations.count - 1] as CLLocation
         
        if(location.horizontalAccuracy > 0){
            println(location.coordinate.latitude)
            println(location.coordinate.longitude)
             
            locationManager.stopUpdatingLocation()
        }
    }
     
    func locationManager(manager: CLLocationManager!, didFailWithError error: NSError!){
        println(error)
    }
 
}
```

如果你把这段代码copy过去的话，运行发现没有出现预期的输出内容。

可以试试下面这个绝招：

在plist文件中增加如下两个参数

1、NSLocationWhenInUseUsageDescription

2、NSLocationAlwaysUsageDescription

然后再编译一次，保证成功，如果不成功，哈哈，反正我成功啦！

