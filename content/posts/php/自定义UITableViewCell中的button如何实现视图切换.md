---
title: "自定义UITableViewCell中的button如何实现视图切换"
date: "2025-06-17 14:43:53"
slug: "zi-ding-yi-uitableviewcell-zhong-de-button-ru-he-shi-xian-shi-tu-qie-huan"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/自定义UITableViewCell中的button如何实现视图切换/"
  - "/2025/06/17/自定义UITableViewCell中的button如何实现视图切换.html"
  - "/自定义UITableViewCell中的button如何实现视图切换/"
  - "/自定义UITableViewCell中的button如何实现视图切换.html"
  - "/2025/06/17/zi-ding-yi-uitableviewcell-zhong-de-button-ru-he-shi-xian-shi-tu-qie-huan/"
  - "/2025/06/17/zi-ding-yi-uitableviewcell-zhong-de-button-ru-he-shi-xian-shi-tu-qie-huan.html"
  - "/zi-ding-yi-uitableviewcell-zhong-de-button-ru-he-shi-xian-shi-tu-qie-huan.html"
---
问题如题，原理很简单，只要在cell中给对应的button添加操作事件就好了。

示例代码如下：


```objectivec navigationTableCell.h
//
//  navigationTableCell.h
//  xunYi7
//
//  Created by david on 13-6-18.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface navigationTableCell : UITableViewCell

@property (strong, nonatomic) IBOutlet UIButton *directorBtn;
@property (strong, nonatomic) IBOutlet UIButton *writerBtn;
@property (strong, nonatomic) IBOutlet UIButton *performerBtn;
@property (strong, nonatomic) IBOutlet UIButton *otherBtn;


@property (strong, nonatomic) IBOutlet UIButton *chancePerformerBtn;
@property (strong, nonatomic) IBOutlet UIButton *chanceOtherBtn;

@end
```


```objectivec navigationTableCell.m
//
//  navigationTableCell.m
//  xunYi7
//
//  Created by david on 13-6-18.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "navigationTableCell.h"

@implementation navigationTableCell

- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        // Initialization code
    }
    return self;
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}



@end
```

功能实现过程

```objectivec
-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    NSUInteger row = [indexPath row];
    
    if(row == 0)
    {
        static NSString *navigationTableCellIdentifier = @"navigationTableCell";
        
        UINib *navigationTableCellNib = [UINib nibWithNibName:@"navigationTableCell" bundle:nil];
        [_dataTable registerNib:navigationTableCellNib forCellReuseIdentifier:navigationTableCellIdentifier];
        
        navigationTableCell *cell = [self.dataTable dequeueReusableCellWithIdentifier:navigationTableCellIdentifier];
        if(cell == nil)
        {
            cell = [[navigationTableCell alloc] initWithStyle:UITableViewCellStyleDefault
                                              reuseIdentifier:navigationTableCellIdentifier];
        }
        
        
        [cell.directorBtn addTarget:self
                             action:@selector(directorPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.directorBtn];
        
        
        [cell.writerBtn addTarget:self
                             action:@selector(writerPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.writerBtn];
        
        [cell.performerBtn addTarget:self
                             action:@selector(performerPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.performerBtn];
        
        [cell.otherBtn addTarget:self
                             action:@selector(otherPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.otherBtn];
        
        [cell.chancePerformerBtn addTarget:self
                             action:@selector(chancePerformerPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.chancePerformerBtn];
        
        [cell.chanceOtherBtn addTarget:self
                             action:@selector(chanceOtherPush:)
                   forControlEvents:UIControlEventTouchUpInside];
        [self giveButtonDrawCorner:cell.chanceOtherBtn];
        
        return cell;
    }
    static NSString *cellIdentifier = @"cellIdentifier";
    UITableViewCell *cell = [self.dataTable dequeueReusableCellWithIdentifier:cellIdentifier];
    if(cell == nil)
    {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:cellIdentifier];
    }
    
    NSDictionary *dic = [self.dataDic objectForKey:[NSString stringWithFormat:@"%d",row]];
    
    CGRect cellFrame = [cell frame];
    cellFrame.size.height = 50.0;
    [cell setFrame:cellFrame];
    cell.textLabel.text = [dic valueForKey:@"title"];
    cell.textLabel.font = [UIFont systemFontOfSize:18.0];
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    return cell;
    
}
```
