---
title: "iPhone 自定义 UITableViewCell 行缩进（修正版）"
date: "2025-06-12 17:45:06"
slug: "iphone-zi-ding-yi-uitableviewcell-xing-suo-jin-xiu-zheng-ban"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iPhone-自定义-UITableViewCell-行缩进（修正版）/"
  - "/2025/06/12/iPhone-自定义-UITableViewCell-行缩进（修正版）.html"
  - "/iPhone-自定义-UITableViewCell-行缩进（修正版）/"
  - "/iPhone-自定义-UITableViewCell-行缩进（修正版）.html"
  - "/2025/06/12/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin-xiu-zheng-ban/"
  - "/2025/06/12/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin-xiu-zheng-ban.html"
  - "/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin-xiu-zheng-ban.html"
---
这篇文章跟我之前讲的一篇文章是一样的，唯独不同的一点是，在编辑的状态进行拖动的时候，cell有重载的现象，这样导致的结果是，编辑状态缩进的cell又回复了原来的状态，使得原来的效果又回复了，这次，经过资料的查找，找打解决的办法，代码贴到下面了。至于自定的cell的话，大家可以自己去模仿制作一个，应该是没什么区别的。


```objectivec attentionListCell.h
//
//  attentionListCell.h
//  xunYi6
//
//  Created by david on 13-5-16.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface attentionListCell : UITableViewCell
@property (strong, nonatomic) IBOutlet UIImageView *imageViewPic;
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
@end
```


```objectivec attentionListCell.m
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
            _checkImageView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"Unselected.png"]];
            [self addSubview:_checkImageView];
            [_checkImageView setFrame:CGRectMake(5.0, self.index.frame.origin.y, 30.0, 30.0)];
        }
        [self setChecked:_checked];
	}
	else
	{
		_checked = NO;
        
        
        if(_checkImageView == nil){
            _checkImageView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"Selected.png"]];
            [self addSubview:_checkImageView];
            [_checkImageView setFrame:CGRectMake(5.0, self.index.frame.origin.y, 30.0, 30.0)];
        }
	}
    
}

- (void) setChecked:(BOOL)checked
{
	if (checked)
	{
		_checkImageView.image = [UIImage imageNamed:@"Selected.png"];
		self.backgroundView.backgroundColor = [UIColor colorWithRed:223.0/255.0 green:230.0/255.0 blue:250.0/255.0 alpha:1.0];
	}
	else
	{
		_checkImageView.image = [UIImage imageNamed:@"Unselected.png"];
		self.backgroundView.backgroundColor = [UIColor whiteColor];
	}
	_checked = checked;
}

@end
```
