---
title: "自定义UITableViewCell"
date: "2025-06-12 17:18:57"
slug: "zi-ding-yi-uitableviewcell"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/自定义UITableViewCell/"
  - "/2025/06/12/自定义UITableViewCell.html"
  - "/自定义UITableViewCell/"
  - "/自定义UITableViewCell.html"
  - "/2025/06/12/zi-ding-yi-uitableviewcell/"
  - "/2025/06/12/zi-ding-yi-uitableviewcell.html"
  - "/zi-ding-yi-uitableviewcell.html"
---
自己的应用中需要一种非普通格式的cell，于是自己就定义了一下；基本上的代码类似如下：

```objectivec
static NSString *captionCellWithIdentifier = @"captionCell";

//使用自定义的cell模板
static BOOL nibRegistered = NO;
if(!nibRegistered){
    UINib *nib = [UINib nibWithNibName:@"captionCell" bundle:nil];
    [self.personTable registerNib:nib forCellReuseIdentifier:captionCellWithIdentifier];
    nibRegistered = YES;
}


captionCell *cell = [self.personTable dequeueReusableCellWithIdentifier:captionCellWithIdentifier];
if(cell == nil){
    cell = [[captionCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:captionCellWithIdentifier];
}


cell.contentView.backgroundColor = [UIColor grayColor];

cell.firstTitle.text = @"3月4日 艺人新媒体指数";
cell.firstTitle.textColor = [UIColor whiteColor];
cell.secondTitle.text = @"www.vlinkage.com";
cell.secondTitle.textColor = [UIColor whiteColor];
cell.selectionStyle=UITableViewCellSelectionStyleNone;
return cell;
```
