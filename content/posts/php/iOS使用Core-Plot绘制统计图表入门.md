---
title: "iOS使用Core Plot绘制统计图表入门"
date: "2025-06-10 11:34:31"
slug: "ios-shi-yong-core-plot-hui-zhi-tong-ji-tu-biao-ru-men"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS使用Core-Plot绘制统计图表入门/"
  - "/2025/06/10/iOS使用Core-Plot绘制统计图表入门.html"
  - "/iOS使用Core-Plot绘制统计图表入门/"
  - "/iOS使用Core-Plot绘制统计图表入门.html"
  - "/2025/06/10/ios-shi-yong-core-plot-hui-zhi-tong-ji-tu-biao-ru-men/"
  - "/2025/06/10/ios-shi-yong-core-plot-hui-zhi-tong-ji-tu-biao-ru-men.html"
  - "/ios-shi-yong-core-plot-hui-zhi-tong-ji-tu-biao-ru-men.html"
---
iOS(iPhone/iPad) 下图形组件有两个有名的，**s7graphview** 和 **Core Plot** ，它们都是在Google上托管的代码，听说 Core Plot 比较强，因为前者仅支持曲线图，后者呢曲线图、饼图、柱状图等通吃，且较活跃。那就专注下 Core Plot 的使用。它提供了 MacOSX 和 iOS 下的组件库，我只用到它的 iOS 图表库。

Core Plot能画出来图表的效果应该多看看：`http://code.google.com/p/core-plot/wiki/PlotExamples`，相信看过之后绝大多数的 iOS下的图表可以用它来满足你了。

配置其实很简单的，先从 `http://code.google.com/p/core-plot/downloads/list`下载最新版的CorePlot，比如当前是：CorePlot_0.4.zip，解压开，然后就两步：

- 把目录 CorePlot_0.4/Binaries/

iOS中的libCorePlotCocoaTouch.a和整个子目录CorePlotHeaders从Finder中一并拖入到当前项目中，选择Copyitem into destination group's folder (if needed)，Add to targets里选上相应的target。此时你可以在项目的target中Build Phases页里 Link Binary With Libraries中看到有了libCorePlot-CocoaTouch.a.

- 再到相应Target的 Build Settings页里，Other Linker Flags项中加上 -ObjC -all\_load

- 选择新项目的“info->Build”，在“Header Search Paths”中添加Core Plot头文件搜索路径，如：/Users/davidzhang/project/core-plot/framework。注意要选中“Recursive”小勾（英文原文中没有提这一点）。同时，在Other Linker Flags中要增加两个选项：-ObjC和-all\_load（英文原文中遗漏了第2个选项）。

原文档的安装说明是：

Install Binaries for iOS

1. Copy the **CorePlotHeaders** to your Xcode project

2. Copy **libCorePlotCocoaTouch.a** to your Xcode project

3. Add to **Other Linker Flags** in your target build settings:

-ObjC -all\_load

4. Add the **QuartzCore** framework to the project.

5. Add a **CPTGraph** to your application. See the example apps in Source Code to see how, or read the documentation.

贴一下我的实例代码：



```objectivec DetailViewController.h
#import <UIKit/UIKit.h>
#import "CorePlot-CocoaTouch.h"
@interface DetailsViewController : UIViewController<CPTPlotDataSource, CPTAxisDelegate>
@property (strong, nonatomic) NSString *title;
@property (strong, nonatomic) NSMutableArray *dataArray;
@end
```



```objectivec DetailViewController.m
#import "DetailsViewController.h"


@interface DetailsViewController ()

@end

@implementation DetailsViewController

@synthesize title,dataArray;

-(void)viewDidAppear:(BOOL)animated{
    //初始化数组，并放入十个 0 － 20 间的随机数
    self.dataArray = [[NSMutableArray alloc] init];
    for(int i=0; i< 10; i++){
        [self.dataArray addObject:[NSNumber numberWithInt:rand()%20]];
    }
    
    CGRect frame = CGRectMake(10,10, 300,100);
    
    //图形要放在一个 CPTGraphHostingView 中，CPTGraphHostingView 继承自 UIView
    CPTGraphHostingView *hostView = [[CPTGraphHostingView alloc] initWithFrame:frame];
    
    //把 CPTGraphHostingView 加到你自己的 View 中
    [self.view addSubview:hostView];
    hostView.backgroundColor = [UIColor blueColor];
    
    //在 CPTGraph 中画图，这里的 CPTXYGraph 是个曲线图
    //要指定 CPTGraphHostingView 的 hostedGraph 属性来关联
    CPTXYGraph *graph = [[CPTXYGraph alloc] initWithFrame:hostView.frame];
    hostView.hostedGraph = graph;
    
    CPTScatterPlot *scatterPlot = [[CPTScatterPlot alloc] initWithFrame:graph.bounds];
    [graph addPlot:scatterPlot];
    scatterPlot.dataSource = self; //设定数据源，需应用 CPTPlotDataSource 协议
    
    //设置 PlotSpace，这里的 xRange 和 yRange 要理解好，它决定了点是否落在图形的可见区域
    //location 值表示坐标起始值，一般可以设置元素中的最小值
    //length 值表示从起始值上浮多少，一般可以用最大值减去最小值的结果
    //其实我倒觉得，CPTPlotRange:(NSRange) range 好理解些，可以表示值从 0 到 20
    CPTXYPlotSpace *plotSpace = (CPTXYPlotSpace *) scatterPlot.plotSpace;
    plotSpace.xRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(0)
                                                    length:CPTDecimalFromFloat([self.dataArray count]-1)];
    plotSpace.yRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(0)
                                                    length:CPTDecimalFromFloat(20)];
    
    //下面省去了坐标与线型及其他图形风格的代码
//    
//    [plotSpace release];
//    [graph release];
//    [hostView release];
}

//询问有多少个数据，在 CPTPlotDataSource 中声明的
- (NSUInteger) numberOfRecordsForPlot:(CPTPlot *)plot {
    return [self.dataArray count];
}

//询问一个个数据值，在 CPTPlotDataSource 中声明的
- (NSNumber *) numberForPlot:(CPTPlot *)plot field:(NSUInteger)fieldEnum recordIndex:(NSUInteger)index {
    if(fieldEnum == CPTScatterPlotFieldY){    //询问 Y 值时
        return [self.dataArray objectAtIndex:index];
    }else{                                    //询问 X 值时
        return [NSNumber numberWithInt:index];
    }
}


- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    NSLog(@"title = %@",self.title);
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
```
