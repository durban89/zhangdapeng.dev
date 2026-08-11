---
title: "iOS自定义UISearchBar的背景图"
date: "2025-06-13 10:13:24"
slug: "ios-zi-ding-yi-uisearchbar-de-bei-jing-tu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS自定义UISearchBar的背景图/"
  - "/2025/06/13/iOS自定义UISearchBar的背景图.html"
  - "/iOS自定义UISearchBar的背景图/"
  - "/iOS自定义UISearchBar的背景图.html"
  - "/2025/06/13/ios-zi-ding-yi-uisearchbar-de-bei-jing-tu/"
  - "/2025/06/13/ios-zi-ding-yi-uisearchbar-de-bei-jing-tu.html"
  - "/ios-zi-ding-yi-uisearchbar-de-bei-jing-tu.html"
---
关于自定义的UISearchBar的背景图设置，在经过自己查找资料的情况下，发现的问题是，只有代码段，其采用的方式是，重写UISearchBar，然后调用layoutSubviews这个方法。

那么关于自定UISearchBar我采用的方法是类似自定义UITableviewCell的方法，那么接下来这个layoutSubviews的方法，我想大家也就知道该在那里实现了，实现代码如下：


```objectivec personSearch.h
//
//  personSearch.h
//  xunYi6
//
//  Created by david on 13-5-22.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface personSearch : UISearchBar

@end
```


```objectivec personSearch.m
//
//  personSearch.m
//  xunYi6
//
//  Created by david on 13-5-22.
//  Copyright (c) 2013年 david. All rights reserved.
//

#import "personSearch.h"
#import <QuartzCore/QuartzCore.h>

@implementation personSearch

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
        self.tintColor = [UIColor whiteColor];
    }
    return self;
}

-(void) layoutSubviews
{
    
    UITextField *searchField;
	NSUInteger numViews = [self.subviews count];
	for(int i = 0; i < numViews; i++) {
		if([[self.subviews objectAtIndex:i] isKindOfClass:[UITextField class]]) { //conform?
			searchField = [self.subviews objectAtIndex:i];
		}
	}
	if(!(searchField == nil)) {
        searchField.placeholder = @"输入要查找的艺人的名字";

        [searchField setBorderStyle:UITextBorderStyleRoundedRect];
        [searchField setBackgroundColor:[UIColor whiteColor]];

        //自己的搜索图标
        NSString *path = [[NSBundle mainBundle] pathForResource:@"GUI_search" ofType:@"png"];
        UIImage *image = [UIImage imageWithContentsOfFile:path];
		UIImageView *iView = [[UIImageView alloc] initWithImage:image];
        [iView setFrame:CGRectMake(0.0, 0.0, 30.0, 30.0)];
		searchField.leftView = iView;


	}
    
	[super layoutSubviews];
}


/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    // Drawing code
}
*/

@end
```

OK！实现过程就是这样的，漂亮的结果就出来了
