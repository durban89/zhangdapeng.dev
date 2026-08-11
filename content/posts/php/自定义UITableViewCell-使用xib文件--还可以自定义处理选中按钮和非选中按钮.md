---
title: "自定义UITableViewCell（使用xib文件），还可以自定义处理选中按钮和非选中按钮"
date: "2025-06-18 11:28:48"
slug: "zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-hai-ke-yi-zi-ding-yi-chu-li-xuan-zhong-an-niu-he-fei-xuan-zhong-an-niu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/18/自定义UITableViewCell（使用xib文件），还可以自定义处理选中按钮和非选中按钮/"
  - "/2025/06/18/自定义UITableViewCell（使用xib文件），还可以自定义处理选中按钮和非选中按钮.html"
  - "/自定义UITableViewCell（使用xib文件），还可以自定义处理选中按钮和非选中按钮/"
  - "/自定义UITableViewCell（使用xib文件），还可以自定义处理选中按钮和非选中按钮.html"
  - "/2025/06/18/自定义UITableViewCell-使用xib文件-还可以自定义处理选中按钮和非选中按钮/"
  - "/2025/06/18/自定义UITableViewCell-使用xib文件-还可以自定义处理选中按钮和非选中按钮.html"
  - "/2025/06/18/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-hai-ke-yi-zi-ding-yi-chu-li-xuan-zhong/"
  - "/2025/06/18/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-hai-ke-yi-zi-ding-yi-chu-li-xuan-z.html"
  - "/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-hai-ke-yi-zi-ding-yi-chu-li-xuan-zhong-an-niu.html"
---
最近在做自定义的cell的操作，由于之前是在网上找的一个类似的东东，结果拿来用的时候就出现了很多的问题，呵呵，结果我还是自己研究了一下，原因就是我之前是使用自定义的cell的问题是，在删除和非删除的过程中进行切换，有个选中和非选中的图片总是迟一步退去，导致的问题是，挡住了后面的内容，‍使得整个看起来不美观，结果我就是使用了UIImageView的隐藏功能，代码我放在下面，github也有的。在使用的时候最好是参照我的另一片博文：[IPhone 自定义 UITableViewCell 行缩进（修正版）](https://www.gowhich.com/blog/135)。好了，看代码。

attentionListCell.h

```objectivec
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
@property (strong, nonatomic) IBOutlet UIImageView *selectImageView;


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

@synthesize selectImageView = _selectImageView;

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
    [UIView beginAnimations:@"View Flip" context:nil];
    [UIView setAnimationDuration:1.25];
    [UIView setAnimationCurve:UIViewAnimationCurveEaseInOut];
    
    CGFloat offset = 10.0;
    
    //
    CGFloat selectImageX = -25.0;
    CGFloat selectImageY = 19.5;
    CGFloat selectImageWidth = 30.0;
    CGFloat selectImageHeight = 30.0;
    
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
    
    [self.selectImageView setFrame:CGRectMake(selectImageX, selectImageY, selectImageWidth, selectImageHeight)];
    _selectImageView.hidden = NO;
    
    [UIView commitAnimations];
}


-(void) setSubViewsFrameNormal{
    if(_checkImageView != nil){
        [_checkImageView setFrame:CGRectMake(0.0, 20.0, 0.0, 0.0)];
    }
    
    CGFloat offset = 0.0;
    //
    CGFloat selectImageX = 1.0;
    CGFloat selectImageY = 19.5;
    CGFloat selectImageWidth = 30.0;
    CGFloat selectImageHeight = 30.0;
    
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
    
    [self.selectImageView setFrame:CGRectMake(selectImageX, selectImageY, selectImageWidth, selectImageHeight)];
    _selectImageView.hidden = YES;
}

//-------------------------------
// 重新定义editing的设置
//-------------------------------
-(void) setEditing:(BOOL)editing animated:(BOOL)animated{
    
    if (self.editing == editing){
        return;
    }
    
    [super setEditing:editing animated:animated];
    
    if (editing){
        CGFloat offset = 10.0;
        //
        CGFloat selectImageX = -25.0;
        CGFloat selectImageY = 19.5;
        CGFloat selectImageWidth = 30.0;
        CGFloat selectImageHeight = 30.0;
        
        
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
        
        [self.selectImageView setFrame:CGRectMake(selectImageX, selectImageY, selectImageWidth, selectImageHeight)];
        
        _selectImageView.hidden = NO;
        
        NSString *unselectedPath = [[NSBundle mainBundle] pathForResource:@"attention_unselect" ofType:@"png"];
        _selectImageView.image = [UIImage imageWithContentsOfFile:unselectedPath];

        
        [self setChecked:_checked];
    }else{
        _checked = NO;
   
    }
}


- (void) setChecked:(BOOL)checked{
    if (checked){
        NSString *selectedPath = [[NSBundle mainBundle] pathForResource:@"attention_select" ofType:@"png"];
        _selectImageView.image = [UIImage imageWithContentsOfFile:selectedPath];
        self.backgroundView.backgroundColor = [UIColor whiteColor];
    }else{
        NSString *unselectedPath = [[NSBundle mainBundle] pathForResource:@"attention_unselect" ofType:@"png"];
        _selectImageView.image = [UIImage imageWithContentsOfFile:unselectedPath];
        self.backgroundView.backgroundColor = [UIColor whiteColor];
    }
    _checked = checked;
}

@end
```

代码就是这样的。
