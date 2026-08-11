---
title: "自定义UITableViewCell（使用xib文件），处理UITextField的键盘隐藏"
date: "2025-06-12 17:45:19"
slug: "zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-chu-li-uitextfield-de-jian-pan-yin-cang"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/12/自定义UITableViewCell（使用xib文件），处理UITextField的键盘隐藏/"
  - "/2025/06/12/自定义UITableViewCell（使用xib文件），处理UITextField的键盘隐藏.html"
  - "/自定义UITableViewCell（使用xib文件），处理UITextField的键盘隐藏/"
  - "/自定义UITableViewCell（使用xib文件），处理UITextField的键盘隐藏.html"
  - "/2025/06/12/自定义UITableViewCell-使用xib文件-处理UITextField的键盘隐藏/"
  - "/2025/06/12/自定义UITableViewCell-使用xib文件-处理UITextField的键盘隐藏.html"
  - "/2025/06/12/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-chu-li-uitextfield-de-jian-pan-yin-can/"
  - "/2025/06/12/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-chu-li-uitextfield-de-jian-pan-yin.html"
  - "/zi-ding-yi-uitableviewcell-shi-yong-xib-wen-jian-chu-li-uitextfield-de-jian-pan-yin-cang.html"
---
查找好多了资料，对这个如果将自己定义的cell中的textfield实现，失去焦点触发键盘隐藏的功能，我这里简单的贴出自己的代码

第一部分是我的自定义的cell


```objectivec nameCell.h
//
//  nameCell.h
//  xunYi6
//
//  Created by david on 13-5-20.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface nameCell : UITableViewCell<UITextFieldDelegate>
@property (strong, nonatomic) IBOutlet UIImageView *markPic;
@property (strong, nonatomic) IBOutlet UILabel *teleplayName;
@property (strong, nonatomic) IBOutlet UITextField *teleplayInput;

@property (copy, nonatomic) UIImage *teleplayImage;
@property (copy, nonatomic) NSString *teleplayTitle;
@property (copy, nonatomic) NSString *name;

@end
```


```objectivec nameCell.m
//
//  nameCell.m
//  xunYi6
//
//  Created by david on 13-5-20.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "nameCell.h"

@implementation nameCell

@synthesize teleplayImage = _teleplayImage;
@synthesize teleplayTitle = _teleplayTitle;
@synthesize name = _name;


- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        // Initialization code
        self.teleplayInput.delegate = self;
    }
    return self;
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

-(void) setTeleplayImage:(UIImage *)value
{
    if(![value isEqual:_teleplayImage])
    {
        _teleplayImage = [value copy];
        self.markPic.image = _teleplayImage;
    }
}

-(void) setTeleplayTitle:(NSString *)value
{
    if(![value isEqualToString:_teleplayTitle])
    {
        _teleplayTitle = [value copy];
        self.teleplayName.text = _teleplayTitle;
    }
}

-(void) setName:(NSString *)value
{
    if(![value isEqualToString:_name])
    {
        
        _name = [value copy];
        self.teleplayInput.text = _name;
    }
}

@end
```

实现的方法我实在`-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section`这个方法中实现的，代码如下：

```objectivec 
-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [self.dataDic count];
}

-(UITableViewCell *) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    
    
    NSUInteger row = [indexPath row];
    
    if(row == 0)
    {
        static NSString *nameCellIdentifier = @"nameCell";
        UINib *nib = [UINib nibWithNibName:@"nameCell" bundle:nil];
        [self.publicChanceTable registerNib:nib forCellReuseIdentifier:nameCellIdentifier];
        
        nameCell *cell = [self.publicChanceTable dequeueReusableCellWithIdentifier:nameCellIdentifier];
        
        if(cell == nil)
        {
            cell = [[nameCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:nameCellIdentifier];
        }
        
        cell.teleplayInput.delegate = self;
        
        cell.accessoryType = UITableViewCellAccessoryNone;
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
        return cell;
    }
    
    static NSString *cellIdentifier = @"cellIdentifier";
    
    UITableViewCell *cell = [self.publicChanceTable dequeueReusableCellWithIdentifier:cellIdentifier];
    
    if(cell == nil)
    {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:cellIdentifier];
    }
    
    NSDictionary *dic = [self.dataDic objectForKey:[NSString stringWithFormat:@"%d",row]];
    cell.textLabel.text = [dic valueForKey:@"detail"];
    
    return cell;
}
```

重要的一点是我加入了这条语句

```objectivec
cell.teleplayInput.delegate = self;
```

同时在你的.h文件中要做的是：

```objectivec
@interface chancePublicViewController : UIViewController<UITableViewDataSource, UITableViewDelegate, UITextFieldDelegate>
```

没错要引入UITextFieldDelegate协议
