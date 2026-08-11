---
title: "iPhone 自定义 UITableViewCell 行缩进"
date: "2025-06-12 17:44:58"
slug: "iphone-zi-ding-yi-uitableviewcell-xing-suo-jin"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iPhone-自定义-UITableViewCell-行缩进/"
  - "/2025/06/12/iPhone-自定义-UITableViewCell-行缩进.html"
  - "/iPhone-自定义-UITableViewCell-行缩进/"
  - "/iPhone-自定义-UITableViewCell-行缩进.html"
  - "/2025/06/12/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin/"
  - "/2025/06/12/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin.html"
  - "/iphone-zi-ding-yi-uitableviewcell-xing-suo-jin.html"
---
网上搜索了很多，不知道是我搜索技术问题还是怎么着，就是没有找到，不过经过自己的努力，还是发现了解决的办法，因为这种情况大多数是自定的UITableviewCell,那么肯定知道如何自己的自定的cell里面如何修改cell上面的元素，其实原理很简单，就是重新设置一下元素的frame大小就好了，我讲自己的代码贴到下面希望能够给大家一个指引。如果问题，可以联系我跟我继续探讨。

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

- (void) setCheckImageViewCenter:(CGPoint)pt alpha:(CGFloat)alpha animated:(BOOL)animated
{
	if (animated)
	{
		[UIView beginAnimations:nil context:nil];
		[UIView setAnimationBeginsFromCurrentState:YES];
		[UIView setAnimationCurve:UIViewAnimationCurveEaseInOut];
		[UIView setAnimationDuration:0.3];
		
		_checkImageView.center = pt;
		_checkImageView.alpha = alpha;
		
		[UIView commitAnimations];
	}
	else
	{
		_checkImageView.center = pt;
		_checkImageView.alpha = alpha;
	}
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
//        CGRect *imageFrame = self.imageViewPic.frame;
        
        
        [self.imageViewPic setFrame:CGRectMake(self.imageViewPic.frame.origin.x + 30, self.imageViewPic.frame.origin.y, self.imageViewPic.frame.size.width, self.imageViewPic.frame.size.height)];
        
        [self.name setFrame:CGRectMake(self.name.frame.origin.x + 30, self.name.frame.origin.y, self.name.frame.size.width, self.name.frame.size.height)];
        
        [self.index setFrame:CGRectMake(self.index.frame.origin.x + 30, self.index.frame.origin.y, self.index.frame.size.width, self.index.frame.size.height)];
        
        [self.rank setFrame:CGRectMake(self.rank.frame.origin.x + 30, self.rank.frame.origin.y, self.rank.frame.size.width, self.rank.frame.size.height)];
        
//        [self.imageViewPic setFrame:CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>)]
        
//		self.selectionStyle = UITableViewCellSelectionStyleNone;
//		self.backgroundView = [[UIView alloc] init];
//		self.backgroundView.backgroundColor = [UIColor redColor];
//		self.textLabel.backgroundColor = [UIColor clearColor];
//		self.detailTextLabel.backgroundColor = [UIColor clearColor];
//		
//		if (_checkImageView == nil)
//		{
//			_checkImageView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"Unselected.png"]];
//			[self addSubview:_checkImageView];
//		}
//		
//		[self setChecked:_checked];
//		_checkImageView.center = CGPointMake(-CGRectGetWidth(_checkImageView.frame) * 0.5,
//											  CGRectGetHeight(self.bounds) * 0.5);
//		_checkImageView.alpha = 0.0;
//		[self setCheckImageViewCenter:CGPointMake(20.5, CGRectGetHeight(self.bounds) * 0.5)
//								alpha:1.0 animated:animated];
	}
	else
	{
//		_checked = NO;
//		self.selectionStyle = UITableViewCellSelectionStyleBlue;
//		self.backgroundView = nil;
//		
//		if (_checkImageView)
//		{
//			[self setCheckImageViewCenter:CGPointMake(-CGRectGetWidth(_checkImageView.frame) * 0.5,
//													  CGRectGetHeight(self.bounds) * 0.5)
//									alpha:0.0
//								 animated:animated];
//		}
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
