---
title: "scopeButtonTitles 的小测试"
date: "2025-06-19 10:48:47"
slug: "scopebuttontitles-de-xiao-ce-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/scopeButtonTitles-的小测试/"
  - "/2025/06/19/scopeButtonTitles-的小测试.html"
  - "/scopeButtonTitles-的小测试/"
  - "/scopeButtonTitles-的小测试.html"
  - "/2025/06/19/scopebuttontitles-de-xiao-ce-shi/"
  - "/2025/06/19/scopebuttontitles-de-xiao-ce-shi.html"
  - "/scopebuttontitles-de-xiao-ce-shi.html"
---
scopeButtonTitles的使用很简单，就像吃苹果一样。

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];
    
    // create a mutable array to contain products for the search results table
    self.searchResults = [NSMutableArray arrayWithCapacity:[self.products count]];

    // set up the search scope buttons with titles using products' localized display names
    NSMutableArray *scopeButtonTitles = [[NSMutableArray alloc] init];
    [scopeButtonTitles addObject:NSLocalizedString(@"All", @"Title for the All button in the search display controller.")];

    for (NSString *deviceType in [APLProduct deviceTypeNames])
    {
        NSString *displayName = [APLProduct displayNameForType:deviceType];
        [scopeButtonTitles addObject:displayName];
    }

    self.searchDisplayController.searchBar.scopeButtonTitles = scopeButtonTitles;
}
```

上面的代码APLProduct这个类你可以在这篇文章中找到答案。[NSCoding解释  initWithCoder:  encodeWithCoder:](https://www.gowhich.com/blog/288)

更详细的可以看这里啦

> 昨天研究了UISearchBar，今天遇到了showsScopeBar问题， 还是继续说一下UISearchBar 吧
>
> UIBarStyle barStyle  
>     控件的样式
>
> id<UISearchBarDelegate> delegate  
>     设置控件的委托
>
> NSString \*text  
>     控件上面的显示的文字
>
> NSString \*prompt  
>     显示在顶部的单行文字，通常作为一个提示行
>
> NSString \*placeholder  
>     半透明的提示文字，输入搜索内容消失
>
> BOOL showsBookmarkButton  
>     是否在控件的右端显示一个书的按钮(没有文字的时候)
>
> BOOL showsCancelButton  
>     是否显示cancel按钮
>
> BOOL showsSearchResultsButton  
>     是否在控件的右端显示搜索结果按钮(没有文字的时候)
>
> BOOL searchResultsButtonSelected  
>     搜索结果按钮是否被选中
>
> UIColor \*tintColor  
>     bar的颜色(具有渐变效果)
>
> BOOL translucent  
>     指定控件是否会有透视效果
>
> UITextAutocapitalizationType  
> autocapitalizationType  
>     设置在什么的情况下自动大写
>
> UITextAutocorrectionType  
> autocorrectionType  
>     对于文本对象自动校正风格
>
> UIKeyboardType  
> keyboardType  
>     键盘的样式
>
> NSArray \*scopeButtonTitles  
>     搜索栏下部的选择栏，数组里面的内容是按钮的标题
>
> NSInteger selectedScopeButtonIndex  
>     搜索栏下部的选择栏按钮的个数
>
> BOOL showsScopeBar  
>     控制搜索栏下部的选择栏是否显示出来
>
> 代理列表：
>
> 编辑代理
>
> – searchBar:textDidChange:
>
> – searchBar:shouldChangeTextInRange:replacementText:
>
> – searchBarShouldBeginEditing:
>
> – searchBarTextDidBeginEditing:
>
> – searchBarShouldEndEditing:
>
> – searchBarTextDidEndEditing:
>
> 点击按钮
>
> – searchBarBookmarkButtonClicked:
>
> – searchBarCancelButtonClicked:
>
> – searchBarSearchButtonClicked:
>
> – searchBarResultsListButtonClicked:
>
> 范围代理
>
> – searchBar:selectedScopeButtonIndexDidChange:
>
> searchBar的范围控件showsScopeBar，官方学名叫Scope Buttons。  
> 首先就要设置这个属性：  
> self.searchBar.showsScopeBar = YES;  
> 然后要给他添加按钮。比如说，这样：self.searchBar.scopeButtonTitles = [NSArray arrayWithObjects:@"BOY",@"GIRL",@"ALL",nil];  
> 还有一个很重要的事情就是我们要实现这个代理UISearchBarDelegate里的这个方法searchBar:selectedScopeButtonIndexDidChange:。告诉表格，你选择的范围是啥。  
> 还有要是设置默认选择哪个按钮的话，要设置这个属性,像这样就是默认选中第1个啦。  
> self.searchBar.selectedScopeButtonIndex = 0;

```objectivec
- (BOOL)searchDisplayController:(UISearchDisplayController *)controller 
shouldReloadTableForSearchString:(NSString *)searchString
{
    NSLog(@"shouldReloadTableForSearchString: %@", searchString);    
    if ((controller.searchBar.selectedScopeButtonIndex != 0) || // 第一个search条件
        (searchString && [searchString length])) {
        [self maybeBeginSearch];
        return NO;
    } else {        
        self.currentResult = nil;
        return YES;
    }
}


- (BOOL)searchDisplayController:(UISearchDisplayController *)controller shouldReloadTableForSearchScope:(NSInteger)searchOption
{
    NSLog(@"shouldReloadTableforSearchScope: %d", searchOption);
    if ((searchOption != 0) || 
        (controller.searchBar.text && [controller.searchBar.text length])) {
        [self maybeBeginSearch];
        return NO;
    } else {        
        self.currentResult = nil;
        return YES;
    }
}

- (void)searchDisplayController:(UISearchDisplayController *)controller didShowSearchResultsTableView:(UITableView *)tableView
{
    // make the activity indicator a sibling of the tableView, so that it can 
    // be displayed on top of it
    [[tableView superview] addSubview:_activityView];
}

- (void)maybeBeginSearch
{
    // cancel any existing timer
    if (_searchTimer) {
        NSLog(@"Cancelling existing timer");
        [_searchTimer invalidate];
        [_searchTimer release];
    }
    

    // 创建一个timer
    _searchTimer = [[NSTimer scheduledTimerWithTimeInterval:0.3 
                                                     target:self 
                                                   selector:@selector(beginTimerSearch:)
                                                   userInfo:nil 
                                                    repeats:NO] retain];    
}

- (void)beginTimerSearch:(NSTimer*)timer 
{
    if (timer == _searchTimer) {
        [_searchTimer invalidate];
        [_searchTimer release];
        _searchTimer = nil;
        [self beginSearch];
    }
}


- (void)beginSearch
{    
    NSLog(@"Begin search for %@ with scope %d", self.searchDisplayController.searchBar.text,
          self.searchDisplayController.searchBar.selectedScopeButtonIndex);
    
    // in case one is running already
    [self.currentRequest cancel];
    self.currentRequest = nil;
    
    NSInteger scopeIndex = self.searchDisplayController.searchBar.selectedScopeButtonIndex;
    if (scopeIndex == 0) {
        NSString* searchString = self.searchDisplayController.searchBar.text;
        
        if (searchString && [searchString length]) {
            _activityView.hidden = NO;
            if ([searchString length]>5 && 
                ![searchString hasSuffix:@"*"])
                searchString = [NSString stringWithFormat:@"%@*", searchString];
            self.currentRequest = [[FreebaseSession session] search:searchString 
                                                               name:@"suggest" 
                                                           delegate:self 
                                                  didFinishSelector:@selector(searchFinished:)
                                                            options:[NSDictionary dictionaryWithObjectsAndKeys:
                                                                     @"/common/topic", @"type",
                                                                     nil]];            
        }
        else
            NSLog(@"No search string: %@", searchString);
    }
    else {
        [self beginGeosearch];
    }
}


- (void)beginGeosearch {
    NSLog(@"beginGeosearch");
    _activityLabel.text = @"Locating...";
    _activityView.hidden = NO;
    
    // this is what I want to do:
    // self.searchDisplayController.searchResultsTableView.hidden = NO;
    
    // this is moronic, but it makes the table display :(
    NSString* searchString;
    if (![self.searchDisplayController.searchBar.text length])
        self.searchDisplayController.searchBar.text = @" ";
    else
        searchString = self.searchDisplayController.searchBar.text;
    
    if (!_awaitingLocation) {
        NSLog(@"Awaiting location, so queing up a search");
        _awaitingLocationForSearch = YES;
        _awaitingLocation = YES;
        [_locationManager startUpdatingLocation];
    } else if (!_currentLocation) {
        NSLog(@"Not awaiting, but still missing _currentLocation");
        // we're awaiting a location, but haven't yet started searching
        _awaitingLocationForSearch = YES;
    } else {
        NSLog(@"Kicking off a geosearch...");
        _activityLabel.text = @"Loading...";
        _awaitingLocationForSearch = NO;
        // ok, we have a location, lets search!
        CLLocationDegrees latitude = _currentLocation.coordinate.latitude;
        CLLocationDegrees longtitude = _currentLocation.coordinate.longitude;
        NSDictionary* geoJsonLocation = [NSDictionary dictionaryWithObjectsAndKeys:
                                        @"Point", @"type",
                                        [NSArray arrayWithObjects:
                                         [NSNumber numberWithDouble:longtitude],
                                         [NSNumber numberWithDouble:latitude], nil],
                                         @"coordinates",
                                         nil];
        NSString* locationString = [geoJsonLocation JSONRepresentation];
        
        NSArray *mql_output = [NSArray arrayWithObject:
                               [NSDictionary dictionaryWithObjectsAndKeys:
                                [NSNull null], @"id",
                                [NSNull null], @"name",
                                [NSArray arrayWithObject:
                                 [NSDictionary dictionaryWithObjectsAndKeys:
                                  [NSNull null], @"id",
                                  [NSNull null], @"name",
                                  [NSNumber numberWithBool:YES], @"optional", nil]], @"type",
                                nil]];
                
        NSString *mql_output_string = [[mql_output JSONRepresentation] retain];
        //[{"type": {"optional": "forbidden",
        //          "id|=": ["/location/country", "/location/us_state", "/location/continent", "/location/us_county"]}}]
        
        NSString* distance = [NSString stringWithFormat:@"%f", 
                              DISTANCES[self.searchDisplayController.searchBar.selectedScopeButtonIndex]];
        
        NSString *searchString = [self.searchDisplayController.searchBar.text 
                                  stringByTrimmingCharactersInSet:
                                  [NSCharacterSet whitespaceAndNewlineCharacterSet]];
        
        if (searchString && [searchString length]) {
            NSString *geo_filter = [[NSDictionary dictionaryWithObjectsAndKeys:
                                     distance, @"within",
                                     locationString, @"location",
                                     @"relevance", @"order_by",
                                     @"/common/topic", @"type",
                                     @"point", @"geometry_type",
                                     nil] JSONRepresentation];
            NSMutableDictionary*
            options = [NSMutableDictionary dictionaryWithObjectsAndKeys:
                       geo_filter, @"geo_filter",
                       @"/common/topic", @"type",
                       nil];
            if (self.mqlFilter)
                [options setObject:self.mqlFilter forKey:@"mql_filter"];
            
            NSLog(@"Search with geo_filter for %@ using %@", searchString, options);
            if ([searchString length]>5 && 
                ![searchString hasSuffix:@"*"])
                searchString = [NSString stringWithFormat:@"%@*", searchString];
            self.currentRequest = [[FreebaseSession session] search:searchString
                                                               name:@"geo_relevance" 
                                                           delegate:self 
                                                  didFinishSelector:@selector(searchFinished:)
                                                            options:options];
                                     
        } else {
            NSMutableDictionary*
            options = [NSMutableDictionary dictionaryWithObjectsAndKeys:
                       distance, @"within",
                       @"relevance", @"order_by",
                       mql_output_string, @"mql_output",
                       @"/common/topic", @"type",
                       @"point", @"geometry_type",
                       nil];
            if (self.mqlFilter)
                [options setObject:self.mqlFilter forKey:@"mql_filter"];
            NSLog(@"Searching geo-only");
            self.currentRequest = [[FreebaseSession session] geosearch:locationString
                                                                  name:@"suggest" 
                                                              delegate:self 
                                                     didFinishSelector:@selector(geoSearchFinished:)
                                                               options:options];
        }
        
        [mql_output_string release];
    }
}

-
 (void)locationManager:(CLLocationManager *)manager 
didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation 
*)oldLocation
{
    self.currentLocation = newLocation;
    NSLog(@"New location! %@", [newLocation description]);
    
    if (_awaitingLocationForSearch) {
        _awaitingLocationForSearch = NO;
        [self beginGeosearch];
    } else {
        // ok, we can simply stop at this point - 
        // it means we've gotten a second location marker, 
        // possibly more accurate than before - no sense in 
        // burning the battery. We don't set _awaitingLocation now,
        // because the one we've got is good enough
        NSLog(@"Got a second location, that's good enough for now.");
        [manager stopUpdatingLocation];
    }
}



- (void)searchFinished:(id)result
{
    NSLog(@"Search complete, %d items", [result count]);
    self.currentResult = result;
    _activityView.hidden = YES;
    [self.searchDisplayController.searchResultsTableView reloadData];
}

- (void)geoSearchFinished:(NSDictionary*)result
{
    self.currentResult = [result valueForKeyPath:@"features.properties"];
    NSLog(@"Geosearch complete, %d items", [self.currentResult count]);
    _activityView.hidden = YES;
    [self.searchDisplayController.searchResultsTableView reloadData];
}

- (void)errorDidOccur:(id)result name:(NSString*)name
{
    NSLog(@"oops...search error: %@", result);
    _activityView.hidden = YES;
    self.currentResult = [NSArray arrayWithObject:
                          [NSDictionary dictionaryWithObjectsAndKeys:
                           [NSNull null], @"id",
                           [NSArray array], @"type",
                           [NSString stringWithFormat:@"Error: %@", result], @"name",
                           nil]];
    [self.searchDisplayController.searchResultsTableView reloadData];
}

/*
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}
*/

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    [self.searchDisplayController setActive:YES animated:YES];
    [self.searchDisplayController.searchBar becomeFirstResponder];
}

/*
- (void)viewWillDisappear:(BOOL)animated {
	[super viewWillDisappear:animated];
}
*/
/*
- (void)viewDidDisappear:(BOOL)animated {
	[super viewDidDisappear:animated];
}
*/
```
