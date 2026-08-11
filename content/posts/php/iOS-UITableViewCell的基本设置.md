---
title: "iOS UITableViewCell的基本设置"
date: "2025-06-11 14:00:39"
slug: "ios-uitableviewcell-de-ji-ben-she-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-UITableViewCell的基本设置/"
  - "/2025/06/11/iOS-UITableViewCell的基本设置.html"
  - "/iOS-UITableViewCell的基本设置/"
  - "/iOS-UITableViewCell的基本设置.html"
  - "/2025/06/11/ios-uitableviewcell-de-ji-ben-she-zhi/"
  - "/2025/06/11/ios-uitableviewcell-de-ji-ben-she-zhi.html"
  - "/ios-uitableviewcell-de-ji-ben-she-zhi.html"
---
### [系统默认的颜色设置](#1)

```objectivec
//无色  
cell.selectionStyle = UITableViewCellSelectionStyleNone;  
//蓝色  
cell.selectionStyle = UITableViewCellSelectionStyleBlue;  
//灰色  
cell.selectionStyle = UITableViewCellSelectionStyleGray;
```

### [自定义颜色和背景设置](#2)

改变UITableViewCell选中时背景色：

```objectivec
UIColor *color = [[UIColoralloc]initWithRed:0.0 green:0.0 blue:0.0 alpha:1];//通过RGB来定义自己的颜色
cell.selectedBackgroundView = [[[UIView alloc] initWithFrame:cell.frame] autorelease];  
cell.selectedBackgroundView.backgroundColor = [UIColor xxxxxx];
```

### [自定义UITableViewCell选中时背景](#3)

```objectivec
cell.selectedBackgroundView = [[[UIImageView alloc] initWithImage:[UIImage imageNamed:@"cellart.png"]] autorelease];
```

还有字体颜色

```objectivec
cell.textLabel.highlightedTextColor = [UIColor xxxcolor];  [cell.textLabel setTextColor:color];//设置cell的字体的颜色
```

### [设置tableViewCell间的分割线的颜色](#4)

```objectivec
[theTableView setSeparatorColor:[UIColor xxxx ]];
UITableViewCellSeparatorStyle有如下几种
typedef enum {
  UITableViewCellSeparatorStyleNone,
  UITableViewCellSeparatorStyleSingleLine,
  UITableViewCellSeparatorStyleSingleLineEtched
} UITableViewCellSeparatorStyle;
```

### [设置cell中字体的颜色](#5)

```objectivec
// Customize the appearance of table view cells.
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    if(0 == indexPath.row)
    {
        cell.textLabel.textColor = [UIColor redColor];
        cell.textLabel.highlightedTextColor = [UIColor redColor];
    }
}
```

### [定义UITableViewCell的样式](#6)

```
cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
accessoryType有如下几种
typedef enum {
  UITableViewCellAccessoryNone,
  UITableViewCellAccessoryDisclosureIndicator,
  UITableViewCellAccessoryDetailDisclosureButton,
  UITableViewCellAccessoryCheckmark
} UITableViewCellAccessoryType;
```

### [设置UITableViewCell之间分隔线的颜色](#7)

```objectivec
[chatTableViewsetSeparatorColor:[UIColor blueColor]];
```

### [Cell 样式](#8)

```objectivec
An enumeration for the various styles of cells.
typedef enum {
  UITableViewCellStyleDefault,
  UITableViewCellStyleValue1,
  UITableViewCellStyleValue2,
  UITableViewCellStyleSubtitle
} UITableViewCellStyle;
```
