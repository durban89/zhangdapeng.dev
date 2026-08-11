---
title: "UITableViewCell的seleced与deselect选中/取消选中"
date: "2025-06-17 18:57:10"
slug: "uitableviewcell-de-seleced-yu-deselect-xuan-zhong-qu-xiao-xuan-zhong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/UITableViewCell的seleced与deselect选中/取消选中/"
  - "/2025/06/17/UITableViewCell的seleced与deselect选中/取消选中.html"
  - "/UITableViewCell的seleced与deselect选中/取消选中/"
  - "/UITableViewCell的seleced与deselect选中/取消选中.html"
  - "/2025/06/17/UITableViewCell的seleced与deselect选中-取消选中/"
  - "/2025/06/17/UITableViewCell的seleced与deselect选中-取消选中.html"
  - "/2025/06/17/uitableviewcell-de-seleced-yu-deselect-xuan-zhong-qu-xiao-xuan-zhong/"
  - "/2025/06/17/uitableviewcell-de-seleced-yu-deselect-xuan-zhong-qu-xiao-xuan-zhong.html"
  - "/uitableviewcell-de-seleced-yu-deselect-xuan-zhong-qu-xiao-xuan-zhong.html"
---
首先要从一个我遇到的问题谈起，一个基于NavigationBar的App，开始时我有一个UITableViewController，其中每个UITableViewCell点击后都会push另一个ViewController，每次点击Cell的时候，Cell都会被选中，当从push的ViewController返回的时候选中的Cell便会自动取消选中（有动画效果）。后来由于某些原因我把这个UITableViewController改成了UIViewController，之后就产生了一个问题：每次返回到TableView的时候，之前选中的Cell不能自动取消选中，经过查找得知：  
  
UITableViewController有一个clearsSelectionOnViewWillAppear的property，  
  
而当把UITableViewController修改成UIViewController后，这个属性自然就不存在了，因此我们必须手动添加取消选中的功能，方法很简单，在viewWillAppear方法中加入：

```objectivec
[self.tableView deselectRowAtIndexPath:[self.tableView indexPathForSelectedRow] animated:YES];
```

即可，估计UITableViewController也是用类似的方法来实现取消选中的功能的。
