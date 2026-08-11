---
title: "iOS SearchBar的使用方法"
date: "2025-06-10 10:12:44"
slug: "ios-searchbar-de-shi-yong-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-SearchBar的使用方法/"
  - "/2025/06/10/iOS-SearchBar的使用方法.html"
  - "/iOS-SearchBar的使用方法/"
  - "/iOS-SearchBar的使用方法.html"
  - "/2025/06/10/ios-searchbar-de-shi-yong-fang-fa/"
  - "/2025/06/10/ios-searchbar-de-shi-yong-fang-fa.html"
  - "/ios-searchbar-de-shi-yong-fang-fa.html"
---
|     |     |
| --- | --- |
| 属性  | 作用  |
| UIBarStyle barStyle | 控件的样式 |
| id delegate | 设置控件的委托 |
| NSString \*text | 控件上面的显示的文字 |
| NSString \*prompt | 显示在顶部的单行文字，通常作为一个提示行 |
| NSString \*placeholder | 半透明的提示文字，输入搜索内容消失 |
| BOOL showsBookmarkButton | 是否在控件的右端显示一个书的按钮(没有文字的时候) |
| BOOL showsCancelButton | 是否显示cancel按钮 |
| BOOL showsSearchResultsButton | 是否在控件的右端显示搜索结果按钮(没有文字的时候) |
| BOOL searchResultsButtonSelected | 搜索结果按钮是否被选中 |
| UIColor \*tintColor | bar的颜色(具有渐变效果) |
| BOOL translucent | 指定控件是否会有透视效果 |
| UITextAutocapitalizationType  <br>autocapitalizationType | 设置在什么的情况下自动大写 |
| UITextAutocorrectionType  <br>autocorrectionType | 对于文本对象自动校正风格 |
| UIKeyboardType  <br>keyboardType | [键盘](#)的样式 |
| NSArray \*scopeButtonTitles | 搜索栏下部的选择栏，数组里面的内容是按钮的标题 |
| NSInteger selectedScopeButtonIndex | 搜索栏下部的选择栏按钮的个数 |
| BOOL showsScopeBar | 控制搜索栏下部的选择栏是否显示出来 |

### [代理列表：](#1)

编辑代理  
– searchBar:textDidChange:  
– searchBar:shouldChangeTextInRange:replacementText:  
– searchBarShouldBeginEditing:  
– searchBarTextDidBeginEditing:  
– searchBarShouldEndEditing:  
– searchBarTextDidEndEditing:  
  
点击按钮  
– searchBarBookmarkButtonClicked:  
– searchBarCancelButtonClicked:  
– searchBarSearchButtonClicked:  
– searchBarResultsListButtonClicked:  
  
范围代理  
– searchBar:selectedScopeButtonIndexDidChange:

### [searchBar使用小技巧](#2)

searchBar的范围控件showsScopeBar，官方学名叫Scope Buttons。  
首先就要设置这个属性：  
`self.searchBar.showsScopeBar = YES;`
然后要给他添加按钮。比如说，这样：`self.searchBar.scopeButtonTitles = [NSArray arrayWithObjects:@"BOY",@"GIRL",@"ALL",nil]; ` 
还有一个很重要的事情就是我们要实现这个代理UISearchBarDelegate里的这个方法`searchBar:selectedScopeButtonIndexDidChange:`。告诉表格，你选择的范围是啥。  
还有要是设置默认选择哪个按钮的话，要设置这个属性,像这样就是默认选中第1个啦。  
`self.searchBar.selectedScopeButtonIndex = 0;`
  
在实现搜索功能时，界面使用UISearchBar比较好，它实现了很多搜索时使用到的东西，但是默认的风格可能和现有的风格不一致，所以需要我们想办法去修改一下默认的外观。

#### [修改UISearchBar的背景颜色](#2-1)

UISearchBar是由两个subView组成的，一个是UISearchBarBackGround,另一个是UITextField. 要IB中没有直接操作背景的属性。  
方法是直接将 UISearchBarBackGround移去
第一种解决方案：

```objectivec
seachBar=[[UISearchBar alloc] init];  
seachBar.backgroundColor=[UIColor clearColor];  
for (UIView *subview in seachBar.subviews)   
{    
    if ([subview isKindOfClass:NSClassFromString(@"UISearchBarBackground")])  
    {    
        [subview removeFromSuperview];    
        break;  
    }   
}
```

第二种解决的方法：

```objectivec
[[searchbar.subviews objectAtIndex:0]removeFromSuperview];
```

#### [为UISearchBar添加背景图片](#2-2)

```objectivec
UISearchBar* m_searchBar = [[UISearchBar alloc] initWithFrame:CGRectMake(0, 44, 320, 41)];  
m_searchBar.delegate = self;  
m_searchBar.barStyle = UIBarStyleBlackTranslucent;  
m_searchBar.autocorrectionType = UITextAutocorrectionTypeNo;  
m_searchBar.autocapitalizationType = UITextAutocapitalizationTypeNone;  
m_searchBar.placeholder = _(@"Search");  
m_searchBar.keyboardType =  UIKeyboardTypeDefault;  
//为UISearchBar添加背景图片  
UIView *segment = [m_searchBar.subviews objectAtIndex:0];  
UIImageView *bgImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"Images/search_bar_bg.png"]];  
[segment addSubview: bgImage];  
//<---背景图片  
[self.view addSubview:m_searchBar];  
[m_searchBar release];
```

#### [取消UISearchBar调用的键盘](#2-3)

```objectivec
[searchBar resignFirstResponder];
```

第一种方法

```objectivec
UISearchBar *mySearchBar = [[UISearchBar alloc] 
initWithFrame:CGRectMake(0.0, 0.0, self.view.bounds.size.width, 45)];          
mySearchBar.delegate = self;          
mySearchBar.showsCancelButton = NO;          
mySearchBar.barStyle=UIBarStyleDefault;          
mySearchBar.placeholder=@"Enter Name or Categary";           
mySearchBar.keyboardType=UIKeyboardTypeNamePhonePad;           
[self.view addSubview:mySearchBar];          
[mySearchBar release];
```

第二种方法，在tableview上添加：

```objectivec
//add Table  
UITableView *myBeaconsTableView = [[UITableView alloc] initWithFrame:CGRectMake(0, 0, self.view.bounds.size.width, self.view.bounds.size.height-40) style:UITableViewStylePlain];  
myBeaconsTableView.backgroundColor = [UIColor whiteColor];  
myBeaconsTableView.delegate=self;  
myBeaconsTableView.dataSource=self;  
[myBeaconsTableView setRowHeight:40];  
// Add searchbar   
searchBar = [[UISearchBar alloc] initWithFrame:CGRectMake(0.0, 0.0, self.view.bounds.size.width, 40)];  
searchBar.placeholder=@"Enter Name";  
searchBar.delegate = self;  
myBeaconsTableView.tableHeaderView = searchBar;  
searchBar.autocorrectionType = UITextAutocorrectionTypeNo;  
searchBar.autocapitalizationType = UITextAutocapitalizationTypeNone;  
[searchBar release];  
[self.view addSubview:myBeaconsTableView];  
[myBeaconsTableView release];
```
