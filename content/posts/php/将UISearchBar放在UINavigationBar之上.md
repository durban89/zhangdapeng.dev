---
title: "将UISearchBar放在UINavigationBar之上"
date: "2025-06-13 10:13:44"
slug: "jiang-uisearchbar-fang-zai-uinavigationbar-zhi-shang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/将UISearchBar放在UINavigationBar之上/"
  - "/2025/06/13/将UISearchBar放在UINavigationBar之上.html"
  - "/将UISearchBar放在UINavigationBar之上/"
  - "/将UISearchBar放在UINavigationBar之上.html"
  - "/2025/06/13/jiang-uisearchbar-fang-zai-uinavigationbar-zhi-shang/"
  - "/2025/06/13/jiang-uisearchbar-fang-zai-uinavigationbar-zhi-shang.html"
  - "/jiang-uisearchbar-fang-zai-uinavigationbar-zhi-shang.html"
---
将UISearchBar放在UINavigationBar之上,实现的过程如下：

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    self.navigationController.navigationBar.tintColor = [UIColor redColor];

    //添加左侧的item
    UIBarButtonItem *leftItem = [[UIBarButtonItem alloc] initWithTitle:@"艺人"
                                                                 style:UIBarButtonItemStyleBordered target:self
                                                                action:@selector(showSelect)];
    self.navigationItem.leftBarButtonItem = leftItem;
    
    
    //导航条的搜索条
    _searchBar = [[UISearchBar alloc]initWithFrame:CGRectMake(0.0f,0.0f,255.0f,44.0f)];
    _searchBar.delegate = self;
    [_searchBar setTintColor:[UIColor redColor]];
    [_searchBar setPlaceholder:@"输入艺人名字"];
    
    //将搜索条放在一个UIView上
    UIView *searchView = [[UIView alloc]initWithFrame:CGRectMake(0, 0, 768, 44)];
    searchView.backgroundColor = [UIColor blueColor];
    [searchView addSubview:_searchBar];
    self.navigationItem.titleView = searchView;
    
    //设置tableview的代理
    self.dataTable.delegate = self;
    self.dataTable.dataSource = self;
    
    //加载数据
    NSString *path=[[NSBundle mainBundle] pathForResource:@"category" ofType:@"plist"];
    self.dataDic = [[NSMutableDictionary alloc] initWithContentsOfFile:path];
}
```

如果说你的searchbar的位置不对，那么好的我这里高速你应该如何去调整吧：

请你注意一下这条语句：

```objectivec
_searchBar = [[UISearchBar alloc]initWithFrame:CGRectMake(0.0f,0.0f,255.0f,44.0f)];
```

那么解决的办法就很简单了，只要你修改一个坐标和宽度，或者高度，你就可以任意的设置了。
