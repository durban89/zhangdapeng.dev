---
title: "iOS中正则表达式的使用"
date: "2025-06-17 12:01:13"
slug: "ios-zhong-zheng-ze-biao-da-shi-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS中正则表达式的使用/"
  - "/2025/06/17/iOS中正则表达式的使用.html"
  - "/iOS中正则表达式的使用/"
  - "/iOS中正则表达式的使用.html"
  - "/2025/06/17/ios-zhong-zheng-ze-biao-da-shi-de-shi-yong/"
  - "/2025/06/17/ios-zhong-zheng-ze-biao-da-shi-de-shi-yong.html"
  - "/ios-zhong-zheng-ze-biao-da-shi-de-shi-yong.html"
---
匹配9-15个由字母/数字组成的字符串的正则表达式：

```objectivec
NSString * regex = @"^[A-Za-z0-9]{9,15}$";
NSPredicate *pred = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", regex];
BOOL isMatch = [pred evaluateWithObject:txtfldPhoneNumber.text];
```

Cocoa用NSPredicate描述查询的方式，原理类似于在数据库中进行查询  
  
用BETWEEN，IN，BEGINWITH，ENDWITH，CONTAINS，LIKE这些谓词来构造NSPredicate，必要的时候使用SELF直接对自己进行匹配  
基本的查询

```objectivec
NSPredicate *predicate; 
predicate = [NSPredicate predicateWithFormat: @"name == 'Herbie'"]; 
BOOL match = [predicate evaluateWithObject: car]; 
NSLog (@"%s", (match) ? "YES" : "NO"); 
//在整个cars里面循环比较  
predicate = [NSPredicate predicateWithFormat: @"engine.horsepower > 150"]; 
NSArray *cars = [garage cars]; 
for (Car *car in [garage cars]) {
	if ([predicate evaluateWithObject: car]) { 
		NSLog (@"%@", car.name); 
	} 
}
```

输出完整的信息

```objectivec
predicate = [NSPredicate predicateWithFormat: @"engine.horsepower > 150"]; 
NSArray *results; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results); 
//含有变量的谓词  
NSPredicate *predicateTemplate = [NSPredicate predicateWithFormat:@"name == $NAME"]; 
NSDictionary *varDict; 
varDict = [NSDictionary dictionaryWithObjectsAndKeys: @"Herbie", @"NAME", nil]; 
predicate = [predicateTemplate predicateWithSubstitutionVariables: varDict]; 
NSLog(@"SNORGLE: %@", predicate); 
match = [predicate evaluateWithObject: car]; 
NSLog (@"%s", (match) ? "YES" : "NO");
```

注意不能使用$VARIABLE作为路径名，因为它值代表值

```objectivec
//谓词字符串还支持c语言中一些常用的运算符  
predicate = [NSPredicate predicateWithFormat: @"(engine.horsepower > 50) AND (engine.horsepower < 200)"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"oop %@", results); 
predicate = [NSPredicate predicateWithFormat: @"name < 'Newton'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", [results valueForKey: @"name"]); 
//强大的数组运算符  
predicate = [NSPredicate predicateWithFormat: @"engine.horsepower BETWEEN { 50, 200 }"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

```objectivec
NSArray *betweens = [NSArray arrayWithObjects: 
[NSNumber numberWithInt: 50], [NSNumber numberWithInt: 200], nil]; 
predicate = [NSPredicate predicateWithFormat: @"engine.horsepower BETWEEN %@", betweens]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results); 
predicateTemplate = [NSPredicate predicateWithFormat: @"engine.horsepower BETWEEN $POWERS"]; 
varDict = [NSDictionary dictionaryWithObjectsAndKeys: betweens, @"POWERS", nil]; 
predicate = [predicateTemplate predicateWithSubstitutionVariables: varDict]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

```objectivec
//IN运算符  
predicate = [NSPredicate predicateWithFormat: @"name IN { 'Herbie', 'Snugs', 'Badger', 'Flap' }"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", [results valueForKey: @"name"]); 
predicate = [NSPredicate predicateWithFormat: @"SELF.name IN { 'Herbie', 'Snugs', 'Badger', 'Flap' }"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", [results valueForKey: @"name"]);
```

```objectivec
names = [cars valueForKey: @"name"]; 
predicate = [NSPredicate predicateWithFormat: @"SELF IN { 'Herbie', 'Snugs', 'Badger', 'Flap' }"]; 
results = [names filteredArrayUsingPredicate: predicate];//这里限制了SELF的范围  
NSLog (@"%@", results); 
//BEGINSWITH,ENDSWITH,CONTAINS  
//附加符号，[c],[d],[cd],c表示不区分大小写，d表示不区分发音字符，cd表示什么都不区分  
predicate = [NSPredicate predicateWithFormat: @"name BEGINSWITH 'Bad'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

```objectivec
predicate = [NSPredicate predicateWithFormat: @"name BEGINSWITH 'HERB'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

```objectivec
predicate = [NSPredicate predicateWithFormat: @"name BEGINSWITH[cd] 'HERB'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

LIKE运算符（通配符）

```objectivec
predicate = [NSPredicate predicateWithFormat: @"name LIKE[cd] '*er*'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

```objectivec
predicate = [NSPredicate predicateWithFormat: @"name LIKE[cd] '???er*'"]; 
results = [cars filteredArrayUsingPredicate: predicate]; 
NSLog (@"%@", results);
```

参考资料：http://www.2cto.com/kf/201208/150608.html
