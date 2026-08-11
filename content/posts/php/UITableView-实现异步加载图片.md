---
title: "UITableView 实现异步加载图片"
date: "2025-06-17 14:43:34"
slug: "uitableview-shi-xian-yi-bu-jia-zai-tu-pian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/UITableView-实现异步加载图片/"
  - "/2025/06/17/UITableView-实现异步加载图片.html"
  - "/UITableView-实现异步加载图片/"
  - "/UITableView-实现异步加载图片.html"
  - "/2025/06/17/uitableview-shi-xian-yi-bu-jia-zai-tu-pian/"
  - "/2025/06/17/uitableview-shi-xian-yi-bu-jia-zai-tu-pian.html"
  - "/uitableview-shi-xian-yi-bu-jia-zai-tu-pian.html"
---
问题描述：

我在用UITableView的时候，滑动的时候，会出现卡的现象，原因是因为每次滑动的时候都会去远程加载图片，导致了这样的结果。

解决方案：

在网上找的时候找到了这样的一个类，名字叫做AsynImageView,下载地址为：http://vdisk.weibo.com/s/GcAN3

这个类文件就可以解决问题了

解决问题的过程：

自定义一个UITableViewCell，我的自定义代码如下：

`attentionListCell.h`

```objectivec
//
//  attentionListCell.h
//  xunYi6
//
//  Created by david on 13-5-16.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "AsynImageView.h"

@interface attentionListCell : UITableViewCell
@property (strong, nonatomic) IBOutlet AsynImageView *imageViewPic;
@property (strong, nonatomic) IBOutlet UILabel *name;
@property (strong, nonatomic) IBOutlet UILabel *index;
@property (strong, nonatomic) IBOutlet UILabel *rank;

@property (copy, nonatomic) UIImage *listImage;
@property (copy, nonatomic) NSString *listName;
@property (copy, nonatomic) NSString *listIndex;
@property (copy, nonatomic) NSString *listRank;
//--------------------------
//编辑操作
//--------------------------
@property (strong, nonatomic) UIImageView *checkImageView;
@property (nonatomic) BOOL checked;
- (void) setChecked:(BOOL)checked;

-(void) setSubViewsFrameEdit;
-(void) setSubViewsFrameNormal;

@end
```

attentionListCell.m

```objectivec
//
//  attentionListCell.m
//  xunYi6
//
//  Created by david on 13-5-16.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "attentionListCell.h"

@implementation attentionListCell

@synthesize listImage = _listImage;
@synthesize listName = _listName;
@synthesize listIndex = _listIndex;
@synthesize listRank = _listRank;

@synthesize checkImageView = _checkImageView;
@synthesize checked = _checked;

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

-(void) setListImage:(UIImage *)value
{
    if(![value isEqual:_listImage])
    {
        _listImage = [value copy];
        self.imageViewPic.image = _listImage;
    }
}

-(void) setListName:(NSString *)value
{
    if(![value isEqualToString:_listName])
    {
        _listName = [value copy];
        self.name.text = _listName;
    }
}

-(void) setListIndex:(NSString *)value
{
    if(![value isEqualToString:_listIndex])
    {
        _listIndex = [value copy];
        self.index.text = _listIndex;
    }

}

-(void) setListRank:(NSString *)value
{
    if(![value isEqualToString:_listRank])
    {
        _listRank = [value copy];
        self.rank.text = _listRank;
    }
}

-(void) willTransitionToState:(UITableViewCellStateMask)state{
    [UIView beginAnimations:@"ResetFrame" context:nil];
    [UIView setAnimationDuration:0.7];
    [UIView setAnimationTransition:UIViewAnimationTransitionNone forView:self cache:NO];


    if(state == UITableViewCellStateDefaultMask)
    {
        [self setSubViewsFrameNormal];
    }
    else if(state == UITableViewCellStateShowingEditControlMask)
    {
        [self setSubViewsFrameEdit];
    }
    else if(state == UITableViewCellStateShowingDeleteConfirmationMask)
    {
        [self setSubViewsFrameEdit];
    }

    [UIView commitAnimations];
}

-(void) setSubViewsFrameEdit{
    CGFloat offset = 10.0;
    
    CGFloat imageX = 5.0 + offset;
    CGFloat imageY = 5.0;
    CGFloat imageWidth = 60.0;
    CGFloat imageHeight = 60.0;
    
    CGFloat nameX = 70.0 + offset;
    CGFloat nameY = 5.0;
    CGFloat nameWidth = 240.0 - offset;
    CGFloat nameHeight = 15.0;
    
    CGFloat indexX = 70.0 + offset;
    CGFloat indexY = 25.0;
    CGFloat indexWidth = 240.0 - offset;
    CGFloat indexHeight = 15.0;
    
    CGFloat rankX = 70.0 + offset;
    CGFloat rankY = 45.0;
    CGFloat rankWidth = 240.0 - offset;
    CGFloat rankHeight = 15.0;
    
    [self.imageViewPic setFrame:CGRectMake(imageX, imageY, imageWidth, imageHeight)];

    [self.name setFrame:CGRectMake(nameX, nameY, nameWidth, nameHeight)];

    [self.index setFrame:CGRectMake(indexX, indexY, indexWidth, indexHeight)];

    [self.rank setFrame:CGRectMake(rankX, rankY, rankWidth, rankHeight)];
}


-(void) setSubViewsFrameNormal{
    CGFloat offset = 0.0;
    
    CGFloat imageX = 5.0 + offset;
    CGFloat imageY = 5.0;
    CGFloat imageWidth = 60.0;
    CGFloat imageHeight = 60.0;
    
    CGFloat nameX = 70.0 + offset;
    CGFloat nameY = 30.0;
    CGFloat nameWidth = 240.0 - offset;
    CGFloat nameHeight = 15.0;
    
    CGFloat indexX = 70.0 + offset;
    CGFloat indexY = 25.0;
    CGFloat indexWidth = 240.0 - offset;
    CGFloat indexHeight = 15.0;
    
    CGFloat rankX = 70.0 + offset;
    CGFloat rankY = 45.0;
    CGFloat rankWidth = 240.0 - offset;
    CGFloat rankHeight = 15.0;
    
    [self.imageViewPic setFrame:CGRectMake(imageX, imageY, imageWidth, imageHeight)];
    
    [self.name setFrame:CGRectMake(nameX, nameY, nameWidth, nameHeight)];
    
    [self.index setFrame:CGRectMake(indexX, indexY, indexWidth, indexHeight)];
    
    [self.rank setFrame:CGRectMake(rankX, rankY, rankWidth, rankHeight)];
    [self.checkImageView setFrame:CGRectMake(0.0, 0.0, 0.0, 0.0)];
    
}

//-------------------------------
// 重新定义editing的设置
//-------------------------------
-(void) setEditing:(BOOL)editing animated:(BOOL)animated{
    
    if (self.editing == editing)
	{
		return;
	}
	
	[super setEditing:editing animated:animated];
	
	if (editing)
	{
        CGFloat offset = 10.0;
        
        CGFloat imageX = 5.0 + offset;
        CGFloat imageY = 5.0;
        CGFloat imageWidth = 60.0;
        CGFloat imageHeight = 60.0;
        
        CGFloat nameX = 70.0 + offset;
        CGFloat nameY = 5.0;
        CGFloat nameWidth = 240.0 - offset;
        CGFloat nameHeight = 15.0;
        
        CGFloat indexX = 70.0 + offset;
        CGFloat indexY = 25.0;
        CGFloat indexWidth = 240.0 - offset;
        CGFloat indexHeight = 15.0;
        
        CGFloat rankX = 70.0 + offset;
        CGFloat rankY = 45.0;
        CGFloat rankWidth = 240.0 - offset;
        CGFloat rankHeight = 15.0;
        
        [self.imageViewPic setFrame:CGRectMake(imageX, imageY, imageWidth, imageHeight)];
        
        [self.name setFrame:CGRectMake(nameX, nameY, nameWidth, nameHeight)];
        
        [self.index setFrame:CGRectMake(indexX, indexY, indexWidth, indexHeight)];
        
        [self.rank setFrame:CGRectMake(rankX, rankY, rankWidth, rankHeight)];
        
        if(_checkImageView == nil){
            self.checkImageView = [[UIImageView alloc] initWithFrame:CGRectMake(5.0, self.index.frame.origin.y, 20.0, 20.0)];
            NSString *unselectedPath = [[NSBundle mainBundle] pathForResource:@"attention_unselect" ofType:@"png"];
            _checkImageView.image = [UIImage imageWithContentsOfFile:unselectedPath];
            _checkImageView.backgroundColor = [UIColor whiteColor];
            [self addSubview:_checkImageView];
        }
        
        [self setChecked:_checked];
	}
	else
	{
		_checked = NO;
        
//        if(_checkImageView == nil){
//            self.checkImageView = [[UIImageView alloc] initWithFrame:CGRectMake(5.0, self.index.frame.origin.y, 20.0, 20.0)];
//            NSString *selectedPath = [[NSBundle mainBundle] pathForResource:@"attention_select" ofType:@"png"];
//            _checkImageView.image = [UIImage imageWithContentsOfFile:selectedPath];
//            _checkImageView.backgroundColor = [UIColor whiteColor];
//            [self addSubview:_checkImageView];
//        }        
	}
    
}


- (void) setChecked:(BOOL)checked
{
	if (checked)
    {
        NSString *selectedPath = [[NSBundle mainBundle] pathForResource:@"attention_select" ofType:@"png"];
		_checkImageView.image = [UIImage imageWithContentsOfFile:selectedPath];
		self.backgroundView.backgroundColor = [UIColor whiteColor];
	}
	else
	{
        NSString *unselectedPath = [[NSBundle mainBundle] pathForResource:@"attention_unselect" ofType:@"png"];
		_checkImageView.image = [UIImage imageWithContentsOfFile:unselectedPath];
		self.backgroundView.backgroundColor = [UIColor whiteColor];
	}
	_checked = checked;
}

@end
```

实现的操作如下：

```objectivec
-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *attentionListCellIdentifier = @"attentionListCell";
    
    UINib *nib = [UINib nibWithNibName:@"attentionListCell" bundle:nil];
    [self.dataTable registerNib:nib forCellReuseIdentifier:attentionListCellIdentifier];
    
    attentionListCell *cell = [self.dataTable dequeueReusableCellWithIdentifier:attentionListCellIdentifier];
    
    NSUInteger row = [indexPath row];
    
    if(cell == nil)
    {
        cell = [[attentionListCell alloc] initWithStyle:UITableViewCellStyleSubtitle
                                      reuseIdentifier:attentionListCellIdentifier];
    }
    
    NSDictionary *dic = [self.dataDic objectForKey:[NSString stringWithFormat:@"%d",row]];

    //艺人头像
    cell.imageViewPic.imageURL = [NSString stringWithFormat:@"http://xxx.xxxxx.xxx/xxxxx/xxxxxx-%@-zfx.jpg",[dic valueForKey:@"person_id"]];
    
    cell.name.text = [NSString stringWithFormat:@"%@",[dic valueForKey:@"title"]];
    
    cell.index.text = [NSString stringWithFormat:@"Vlink指数: %.1f",[[NSString stringWithFormat:@"%@",[dic valueForKey:@"current_index"]] doubleValue]];
    
    cell.index.textColor = [UIColor lightGrayColor];
    cell.rank.text = [NSString stringWithFormat:@"排名:%@",[dic valueForKey:@"current_rank"]];
    cell.rank.textColor = [UIColor lightGrayColor];
    
    Item* item = [_items objectAtIndex:row];
	[cell setChecked:item.isChecked];
    
    
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    
    return cell;
}
```

参考：http://blog.csdn.net/enuola/article/details/8639404
