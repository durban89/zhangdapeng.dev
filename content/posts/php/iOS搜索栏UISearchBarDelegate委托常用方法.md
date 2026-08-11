---
title: "iOS搜索栏UISearchBarDelegate委托常用方法"
date: "2025-06-06 18:07:30"
slug: "ios-sou-suo-lan-uisearchbardelegate-wei-tuo-chang-yong-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/06/iOS搜索栏UISearchBarDelegate委托常用方法/"
  - "/2025/06/06/iOS搜索栏UISearchBarDelegate委托常用方法.html"
  - "/iOS搜索栏UISearchBarDelegate委托常用方法/"
  - "/iOS搜索栏UISearchBarDelegate委托常用方法.html"
  - "/2025/06/06/ios-sou-suo-lan-uisearchbardelegate-wei-tuo-chang-yong-fang-fa/"
  - "/2025/06/06/ios-sou-suo-lan-uisearchbardelegate-wei-tuo-chang-yong-fang-fa.html"
  - "/ios-sou-suo-lan-uisearchbardelegate-wei-tuo-chang-yong-fang-fa.html"
---
请看下面的实例代码：

```c
//点击键盘上的search按钮时调用

- (void) searchBarSearchButtonClicked:(UISearchBar *)searchBar

{

    NSString *searchTerm = searchBar.text;

    [self handleSearchForTerm:searchTerm];

}


//输入文本实时更新时调用

- (void) searchBar:(UISearchBar *)searchBar textDidChange:(NSString *)searchText

{

    if (searchText.length == 0) {

        [self resetSearch];

        [table reloadData];

        return;

    }

    

    [self handleSearchForTerm:searchText];

}


//cancel按钮点击时调用

- (void) searchBarCancelButtonClicked:(UISearchBar *)searchBar

{

    isSearching = NO;

    search.text = @"";

    [self resetSearch];

    [table reloadData];

    [searchBar resignFirstResponder];

}


//点击搜索框时调用

- (void) searchBarTextDidBeginEditing:(UISearchBar *)searchBar

{

    isSearching = YES;

    [table reloadData];

}
```

UISearchBar上按钮的默认文字为Cancel，如果想改为其他文字请调用以下代码

```c
for(id cc in [searchtext subviews]){  
   if([cc isKindOfClass:[UIButton class]]){  
       UIButton *btn = (UIButton *)cc;  
       [btn setTitle:@"取消"  forState:UIControlStateNormal];  
   }  
}
 
```
