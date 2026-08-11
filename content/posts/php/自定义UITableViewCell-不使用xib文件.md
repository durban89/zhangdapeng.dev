---
title: "自定义UITableViewCell 不使用xib文件"
date: "2025-06-18 11:28:44"
slug: "zi-ding-yi-uitableviewcell-bu-shi-yong-xib-wen-jian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/18/自定义UITableViewCell-不使用xib文件/"
  - "/2025/06/18/自定义UITableViewCell-不使用xib文件.html"
  - "/自定义UITableViewCell-不使用xib文件/"
  - "/自定义UITableViewCell-不使用xib文件.html"
  - "/2025/06/18/zi-ding-yi-uitableviewcell-bu-shi-yong-xib-wen-jian/"
  - "/2025/06/18/zi-ding-yi-uitableviewcell-bu-shi-yong-xib-wen-jian.html"
  - "/zi-ding-yi-uitableviewcell-bu-shi-yong-xib-wen-jian.html"
---
以前经常使用xib做自定义的UITableViewCell，但是最近因为老是闪退，于是想知道是不是因为xib的问题，因为之前意识到一个问题就是兼容的问题，这里涉及到一个AutoLayout的问题。于是想不用xib文件试试。

代码：

```objectivec
NSString *personImagePath = [[NSBundle mainBundle] pathForResource:@"Icon_NMI" ofType:@"png"];
UIImageView *personView = [[UIImageView alloc] initWithImage:[[UIImage alloc] initWithContentsOfFile:personImagePath]];
[personView setFrame:CGRectMake(imageViewX,
                                imageViewY,
                                imageViewWidth,
                                imageViewHeight)];
[cell.contentView addSubview:personView];

UILabel *personLabel = [[UILabel alloc] initWithFrame:CGRectMake(titleLabelX,
                                                                 personView.frame.origin.y, self.view.frame.size.width - personView.frame.size.width,
                                                                 titleLabelHeight)];
personLabel.text = [dic valueForKey:@"title"];
personLabel.font = [UIFont systemFontOfSize:18.0];
[cell.contentView addSubview:personLabel];
```

很简单的就实现了，如果想增加其他的东西，也是很方面的，只要将自己的组建添加到cell.contentView就好了。
