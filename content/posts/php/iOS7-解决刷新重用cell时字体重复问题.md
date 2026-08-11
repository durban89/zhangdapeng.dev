---
title: "iOS7 解决刷新重用cell时字体重复问题"
date: "2025-06-26 10:32:40"
slug: "ios7-jie-jue-shua-xin-zhong-yong-cell-shi-zi-ti-chong-fu-wen-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-解决刷新重用cell时字体重复问题/"
  - "/2025/06/26/iOS7-解决刷新重用cell时字体重复问题.html"
  - "/iOS7-解决刷新重用cell时字体重复问题/"
  - "/iOS7-解决刷新重用cell时字体重复问题.html"
  - "/2025/06/26/ios7-jie-jue-shua-xin-zhong-yong-cell-shi-zi-ti-chong-fu-wen-ti/"
  - "/2025/06/26/ios7-jie-jue-shua-xin-zhong-yong-cell-shi-zi-ti-chong-fu-wen-ti.html"
  - "/ios7-jie-jue-shua-xin-zhong-yong-cell-shi-zi-ti-chong-fu-wen-ti.html"
---
不知道为啥刷新Cell的时候出现字体的重复，字体的覆盖现象。

google了下，发现解决的方法很简单的。如下代码

```objectivec
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"CelebrityCheckTableCell";
    
    //注册要使用的cell
    [tableView registerClass:[UITableViewCell class]
      forCellReuseIdentifier:CellIdentifier];
    
    //创建cell
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier forIndexPath:indexPath];
    
    if(cell == nil)
    {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleValue1
                                      reuseIdentifier:CellIdentifier];
    }
    
    //解决刷新重用cell事字体重复问题
    NSArray *subviews = [[NSArray alloc] initWithArray:cell.contentView.subviews];
    for(UIView *subview in subviews) {
        [subview removeFromSuperview];
    }
    
    //获取行的个数
    NSInteger row = [indexPath row];
    NSDictionary *dict = [_dataDic objectAtIndex:row];
//    NSLog(@"dict = %@",dict);
    
    //cell高度参数
    CGFloat cellHeight = cell.frame.size.height;
    UIColor *rankBgColor = [[UIColor alloc] initWithRed:178.0/255.0 green:178.0/255.0 blue:178.0/255.0 alpha:1.0];
    if(row <= 2){
        rankBgColor = [[UIColor alloc] initWithRed:218.0/255.0 green:118.0/255.0 blue:159.0/255.0 alpha:1.0];
    }
    
    //排名 计算x,y
    CGFloat rankWidth = 21.0;
    CGFloat rankHeight = 21.0;
    CGFloat rankX = 5.0;
    CGFloat rankY = (cellHeight - rankHeight) / 2;
    UILabel *rank = [[UILabel alloc] init];
    [rank setFrame:CGRectMake(rankX, rankY, rankWidth, rankHeight)];
    rank.backgroundColor = rankBgColor;
    rank.textColor = [UIColor whiteColor];
    rank.font = [UIFont boldSystemFontOfSize:17.0];
    rank.textAlignment = NSTextAlignmentCenter;
    [rank.layer setCornerRadius:2.0];
    rank.text = [NSString stringWithFormat:@"%d",row+1];
    [cell.contentView addSubview:rank];
    
    //名称 计算x,y
    CGFloat nameWidth = 150.0;
    CGFloat nameHeight = 21.0;
    CGFloat nameX = rankX + rankWidth + 5.0;
    CGFloat nameY = (cellHeight - nameHeight) / 2;
    UILabel *name = [[UILabel alloc] init];
    [name setFrame:CGRectMake(nameX, nameY, nameWidth, nameHeight)];
    name.textColor = [UIColor blackColor];
    name.font = [UIFont boldSystemFontOfSize:17.0];
    name.textAlignment = NSTextAlignmentLeft;
    [name.layer setCornerRadius:2.0];
    name.text = [NSString stringWithFormat:@"%@",[dict valueForKey:@"title"]];
    [cell.contentView addSubview:name];
    
    //分数 计算x,y
    CGFloat scoreWidth = 100.0;
    CGFloat scoreHeight = 21.0;
    CGFloat scoreX = nameX + nameWidth + 5.0;
    CGFloat scoreY = (cellHeight - scoreHeight) / 2;
    UILabel *score = [[UILabel alloc] init];
    [score setFrame:CGRectMake(scoreX, scoreY, scoreWidth, scoreHeight)];
    score.textColor = [UIColor blackColor];
    score.font = [UIFont boldSystemFontOfSize:16.0];
    score.textAlignment = NSTextAlignmentRight;
    [score.layer setCornerRadius:2.0];
    score.text = [NSString stringWithFormat:@"%@",[dict valueForKey:@"check_sum"]];
    [cell.contentView addSubview:score];
    
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    cell.selectionStyle = UITableViewCellSelectionStyleNone;
    return cell;
}
```

---

得到的结果是，效果很好，解决了我的问题。

参考文章：

<http://blog.csdn.net/developer_zhang/article/details/15026097>

<http://justcoding.iteye.com/blog/1476197>

<http://ddkangfu.blog.51cto.com/311989/465557/>

