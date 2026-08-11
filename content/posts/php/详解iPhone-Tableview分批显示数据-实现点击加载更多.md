---
title: "详解iPhone Tableview分批显示数据 实现点击加载更多"
date: "2025-06-27 10:07:25"
slug: "xiang-jie-iphone-tableview-fen-pi-xian-shi-shu-ju-shi-xian-dian-ji-jia-zai-geng-duo"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/详解iPhone-Tableview分批显示数据-实现点击加载更多/"
  - "/2025/06/27/详解iPhone-Tableview分批显示数据-实现点击加载更多.html"
  - "/详解iPhone-Tableview分批显示数据-实现点击加载更多/"
  - "/详解iPhone-Tableview分批显示数据-实现点击加载更多.html"
  - "/2025/06/27/xiang-jie-iphone-tableview-fen-pi-xian-shi-shu-ju-shi-xian-dian-ji-jia-zai-geng-duo/"
  - "/2025/06/27/xiang-jie-iphone-tableview-fen-pi-xian-shi-shu-ju-shi-xian-dian-ji-jia-zai-geng-duo.html"
  - "/xiang-jie-iphone-tableview-fen-pi-xian-shi-shu-ju-shi-xian-dian-ji-jia-zai-geng-duo.html"
---
其实这个实现起来，开始是啥思路也木有的，但是明白了之后，其实很简单的。

iPhone屏幕尺寸是有限的，如果需要显示的数据很多，可以先数据放到一个table中，先显示10条，table底部有一察看更多选项，点击察看更多查看解析的剩余数据。基本上就是数据源里先只放10条, 点击最后一个cell时, 添加更多的数据到数据源中. 比如:

数据源是个array:

`NSMutableArray *items;`

ViewController的这个方法返回数据条数: +1是为了显示"加载更多"的那个cell

```objectivec
- (NSInteger)tableViewUITableView *)tableView numberOfRowsInSectionNSInteger)section 
{  
    int count = [items count];  
    return  count + 1;  
}
```

这个方法定制cell的显示, 尤其是"加载更多"的那个cell:

```objectivec
- (UITableViewCell *)tableViewUITableView *)tableView cellForRowAtIndexPathNSIndexPath *)indexPath {  
    if([indexPath row] == ([items count])) 
	{  
        //创建loadMoreCell  
        return loadMoreCell;  
    }  
    //create your data cell  
    return cell;  
}
```

还要处理"加载更多"的那个cell的选择事件,触发一个方法来加载更多数据到列表

```objectivec
- (void)tableViewUITableView *)tableView didSelectRowAtIndexPathNSIndexPath *)indexPath {  
      
    if (indexPath.row == [items count]) 
{  
        [loadMoreCell setDisplayText:@"loading more ..."];  
        [loadMoreCell setAnimating:YES];  
        [self performSelectorInBackgroundselector(loadMore) withObject:nil];  
        //[loadMoreCell setHighlighted:NO];  
        [tableView deselectRowAtIndexPath:indexPath animated:YES];  
        return;  
    }  
    //其他cell的事件  
}
```

加载数据的方法:

```objectivec
-(void)loadMore  
{  
    NSMutableArray *more;   
    //加载你的数据  
    [self performSelectorOnMainThreadselector(appendTableWith withObject:more waitUntilDone:NO];  
}
```

添加数据到列表:

```objectivec
-(void) appendTableWithNSMutableArray *)data  
{  
	for (int i=0;i<[data count];i++) 
	{  
		[items addObject:[data objectAtIndex:i]];  
	}  
	NSMutableArray *insertIndexPaths = [NSMutableArray arrayWithCapacity:10];  
	for (int ind = 0; ind < [data count]; ind++) 
	{ 
		NSIndexPath *newPath =  [NSIndexPath indexPathForRow:[items indexOfObject:[data objectAtIndex:ind]] inSection:0];   
	    [insertIndexPaths addObject:newPath];  
	}  
	[self.tableView insertRowsAtIndexPaths:insertIndexPaths withRowAnimation:UITableViewRowAnimationFade];  
}
```

