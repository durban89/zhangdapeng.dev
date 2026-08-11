---
title: "iOS 自制tableview的cell-可任意自定义的UITableViewCell"
date: "2025-06-11 14:00:35"
slug: "ios-zi-zhi-tableview-de-cell-ke-ren-yi-zi-ding-yi-de-uitableviewcell"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-自制tableview的cell-可任意自定义的UITableViewCell/"
  - "/2025/06/11/iOS-自制tableview的cell-可任意自定义的UITableViewCell.html"
  - "/iOS-自制tableview的cell-可任意自定义的UITableViewCell/"
  - "/iOS-自制tableview的cell-可任意自定义的UITableViewCell.html"
  - "/2025/06/11/ios-zi-zhi-tableview-de-cell-ke-ren-yi-zi-ding-yi-de-uitableviewcell/"
  - "/2025/06/11/ios-zi-zhi-tableview-de-cell-ke-ren-yi-zi-ding-yi-de-uitableviewcell.html"
  - "/ios-zi-zhi-tableview-de-cell-ke-ren-yi-zi-ding-yi-de-uitableviewcell.html"
---
UITableView的强大更多程度上来自于可以任意自定义 UITableViewCell单元格。通常，UITableView中的Cell是动态的，在使用过程中，会创建一个Cell池，根据每个cell的高 度（即tableView:heightForRowAtIndexPath:返回值），以及屏幕高度计算屏幕中可显示几个cell。而进行自定义 TableViewCell无非是采用代码实现或采用IB编辑nib文件来实现两种方式，本文主要收集代码的方式实现各种cell自定义。

### [如何动态调整Cell高度](#1)

```objectivec
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
 
    static NSString *CellIdentifier = @"Cell";
 
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[[UITableViewCell alloc] initWithFrame:CGRectZero reuseIdentifier:CellIdentifier] autorelease];
        UILabel *label = [[UILabel alloc] initWithFrame:CGRectZero];
        label.tag = 1;
        label.lineBreakMode = UILineBreakModeWordWrap;
        label.highlightedTextColor = [UIColor whiteColor];
        label.numberOfLines = 0;
        label.opaque = NO; // 选中Opaque表示视图后面的任何内容都不应该绘制
        label.backgroundColor = [UIColor clearColor];
        [cell.contentView addSubview:label];
        [label release];
    }
 
    UILabel *label = (UILabel *)[cell viewWithTag:1];
    NSString *text;
    text = [textArray objectAtIndex:indexPath.row];
    CGRect cellFrame = [cell frame];
    cellFrame.origin = CGPointMake(0, 0);
 
    label.text = text;
    CGRect rect = CGRectInset(cellFrame, 2, 2);
    label.frame = rect;
    [label sizeToFit];
    if (label.frame.size.height > 46) {
        cellFrame.size.height = 50 + label.frame.size.height - 46;
    }
    else {
        cellFrame.size.height = 50;
    }
    [cell setFrame:cellFrame];
 
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [self tableView:tableView cellForRowAtIndexPath:indexPath];
    return cell.frame.size.height;
}
```

### [如何用图片自定义Table Separeator分割线](#2)

一般地，利用类似`[tableView setSeparatorColor:[UIColor redColor]];`语句即可修改cell中间分割线的颜色。那又如何用一个图片作为分割线背景呢？可以尝试如下：  
方法一：  
先设置cell separatorColor为clear，然后把图片做的分割线添加到自定义的custom cell上。  
方法二：  
在cell里添加一个像素的imageView后将图片载入进，之后设置`tableView.separatorStyle = UITableViewCellSeparatorStyleNone`

### [自定义首行Cell与其上面导航栏间距](#3)

```objectivec
tableView.tableHeaderView = [[[UIView alloc] initWithFrame:CGRectMake(0,0,5,20)] autorelease];
```

自定义UITableViewCell的accessory样式

默认的accessoryType属性有四种取值：
- UITableViewCellAccessoryNone
- UITableViewCellAccessoryDisclosureIndicator
- UITableViewCellAccessoryDetailDisclosureButton
- UITableViewCellAccessoryCheckmark

如果想使用自定义附件按钮的其他样式，则需使用UITableView的accessoryView属性来指定。

```objectivec
UIButton *button;
if(isEditableOrNot) {
    UIImage *image = [UIImage imageNamed:@"delete.png"];
    button = [UIButton buttonWithType:UIButtonTypeCustom];
    CGRect frame = CGRectMake(0.0,0.0,image.size.width,image.size.height);
    button.frame = frame;
    [button setBackgroundImage:image forState:UIControlStateNormal];
    button.backgroundColor = [UIColor clearColor];
    cell.accessoryView = button;
}else{
    button = [UIButton buttonWithType:UIButtonTypeCustom];
    button.backgroundColor = [UIColor clearColor];
    cell.accessoryView = button;
}
```

以上代码仅仅是定义了附件按钮两种状态下的样式，问题是现在这个自定义附件按钮的事件仍不可用。即事件还无法传递到 `UITableViewDelegate`的`accessoryButtonTappedForRowWithIndexPath`方法上。当我们在上述代码 中在加入以下语句：

```objectivec
[button addTarget:self action:@selector(btnClicked:event:) forControlEvents:UIControlEventTouchUpInside];
```

虽然可以捕捉到每个附件按钮的点击事件，但我们还无法进行区别到底是哪一行的附件按钮发生了点击动作！因为addTarget:方法最多允许传递两个参 数：target和event，这两个参数都有各自的用途了（target指向事件委托对象，event指向所发生的事件）。看来只依靠Cocoa框架已 经无法做到了。  
但我们还是可以利用event参数，在自定义的btnClicked方法中判断出事件发生在UITableView的哪一个cell上。因为UITableView有一个很关键的方法indexPathForRowAtPoint，可以根据触摸发生的位置，返回触摸发生在哪一个cell的indexPath。而且通过event对象，正好也可以获得每个触摸在视图中的位置。

```objectivec
// 检查用户点击按钮时的位置，并转发事件到对应的accessory tapped事件
- (void)btnClicked:(id)sender event:(id)event
{
     NSSet *touches = [event allTouches];
     UITouch *touch = [touches anyObject];
     CGPoint currentTouchPosition = [touch locationInView:self.tableView];
     NSIndexPath *indexPath = [self.tableView indexPathForRowAtPoint:currentTouchPosition];
     if(indexPath != nil)
     {
         [self tableView:self.tableView accessoryButtonTappedForRowWithIndexPath:indexPath];
     }
}
```

这样，UITableView的accessoryButtonTappedForRowWithIndexPath方法会被触发，并且获得一个indexPath参数。通过这个indexPath参数，我们即可区分到底哪一行的附件按钮发生了触摸事件。

```objectivec
- (void)tableView:(UITableView *)tableView accessoryButtonTappedForRowWithIndexPath:(NSIndexPath *)indexPath
{
    int  *idx = indexPath.row;
   //这里加入自己的逻辑
}
```

摘自：http://www.cnblogs.com/ownerblood/archive/2012/08/02/2620173.html
