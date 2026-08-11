---
title: "iOS 图表 CorePlot 折线图实例 填充图实例"
date: "2025-06-11 10:44:07"
slug: "ios-tu-biao-coreplot-zhe-xian-tu-shi-li-tian-chong-tu-shi-li"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-图表-CorePlot-折线图实例-填充图实例/"
  - "/2025/06/11/iOS-图表-CorePlot-折线图实例-填充图实例.html"
  - "/iOS-图表-CorePlot-折线图实例-填充图实例/"
  - "/iOS-图表-CorePlot-折线图实例-填充图实例.html"
  - "/2025/06/11/ios-tu-biao-coreplot-zhe-xian-tu-shi-li-tian-chong-tu-shi-li/"
  - "/2025/06/11/ios-tu-biao-coreplot-zhe-xian-tu-shi-li-tian-chong-tu-shi-li.html"
  - "/ios-tu-biao-coreplot-zhe-xian-tu-shi-li-tian-chong-tu-shi-li.html"
---
最近在搞数据展示，需要将数据用图表展示出来，结果还是没有达到自己理想的效果，先将自己的不完美版本，记录一下，直接贴出代码



```objectivec detailViewController.h
#import <UIKit/UIKit.h>
#import "CorePlot-CocoaTouch.h"
@interface DetailsViewController : UIViewController<CPTPlotDataSource, CPTAxisDelegate>
{
    CPTXYGraph                  *graph;             //画板
    CPTScatterPlot              *dataSourceLinePlot;//线
    NSMutableArray              *dataForPlot1;      //坐标数组
    NSTimer                     *timer1;            //定时器
    int                         j;
    int                         r;
    int                         maxX;
    int                         maxY;
    int                         minX;
    int                         minY;
}
@property (retain, nonatomic) NSMutableArray *dataForPlot1;
@property (strong, nonatomic) NSString *value;
@property (strong, nonatomic) NSString *key;
@property (strong, nonatomic) NSMutableArray *dataArray;
@property (strong, nonatomic) CPTXYGraph *graph;
@property (strong, nonatomic) NSMutableArray *points;
@property (strong, nonatomic) NSMutableArray *xArr;
@property (strong, nonatomic) NSMutableArray *yArr;
//折线图
-(void) lineChart;
//填充图
-(void) fillFigure;
@end
```

detailViewController.h（里面有两个函数，是分别调用折线图和填充图的）

```objectivec detailViewController.h
#import "DetailsViewController.h"

@interface DetailsViewController ()

@end

@implementation DetailsViewController

@synthesize value;
@synthesize key;
@synthesize dataForPlot1;
@synthesize graph;
@synthesize points;

@synthesize yArr;
@synthesize xArr;


- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        //构造数据
        self.points = [[NSMutableArray alloc] init];
        NSUInteger i;
        self.xArr = [[NSMutableArray alloc] init];
        self.yArr = [[NSMutableArray alloc] init];
        
        for(i=0;i<60;i++){
            id x = [NSNumber numberWithFloat: 1+i*0.5];
            id y = [NSNumber numberWithFloat: 1.2 * rand()/(float)RAND_MAX+1.2];
            
            [self.xArr addObject:x];
            [self.yArr addObject:y];
            [self.points addObject:[NSMutableDictionary dictionaryWithObjectsAndKeys:x,@"x",y,@"y", nil]];
            NSNumber *tmpX = [NSNumber numberWithFloat:[x intValue]];
            NSNumber *tmpY = [NSNumber numberWithFloat:[y intValue]];
            
            maxX = MAX([tmpX intValue], maxX);
            minX = MIN([tmpX intValue], minX);
            maxY = MAX([tmpY intValue], maxY);
            minY = MIN([tmpY intValue], minY);
        }
        NSLog(@"maxX = %d",maxX);
        NSLog(@"minX = %d",minX);
        NSLog(@"maxY = %d",maxY);
        NSLog(@"minY = %d",minY);
//        NSLog(@"xArr = %@",self.xArr);
//        NSLog(@"yArr = %@",self.yArr);
        
    }
    return self;
}

- (void)viewDidLoad{
    [super viewDidLoad];
    self.title = self.value;
    [self lineChart];
    

}

//GridLine
-(void) gridLine{
    
}

//折线图
-(void) lineChart{
    graph = [[CPTXYGraph alloc] initWithFrame:CGRectZero];
    CPTTheme *theme = [CPTTheme themeNamed:kCPTDarkGradientTheme];
    [graph applyTheme:theme];
    CPTGraphHostingView *hostingView = [[CPTGraphHostingView alloc] initWithFrame:self.view.bounds];
    
    //设置图表的边框
    //左边的padding设置为0
    graph.paddingLeft = 0;
    //顶部的的padding设置0
	graph.paddingTop = 0;
    //右边的padding设置为0
	graph.paddingRight = 0;
    //底部的padding设置为0
	graph.paddingBottom = 0;
    
    //坐标区域的边框设置
    //左边的padding设置为45.0
    graph.plotAreaFrame.paddingLeft = 40.0 ;
    //顶部的padding设置为40.0
    graph.plotAreaFrame.paddingTop = 10.0 ;
    //右边的padding设置为5.0
    graph.plotAreaFrame.paddingRight = 10.0 ;
    //底部的padding设置为80.0
    graph.plotAreaFrame.paddingBottom = 10.0 ;
    
    
    hostingView.hostedGraph = graph;
    
    //定义绘图空间
    CPTXYPlotSpace *plotSpace = (CPTXYPlotSpace *) graph.defaultPlotSpace;
    plotSpace.allowsUserInteraction = NO;
    //设置x，y坐标范围
    plotSpace.xRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(minX) length:CPTDecimalFromFloat(maxX)];
    plotSpace.yRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(minY) length:CPTDecimalFromFloat(maxY+2)];
    
    //散点图的绘制
    CPTScatterPlot *boundLinePlot = [[CPTScatterPlot alloc] init];
    CPTMutableLineStyle *lineStyle = [CPTMutableLineStyle lineStyle];
    lineStyle.miterLimit = 1.0f;
    lineStyle.lineWidth = 3.0f;
    lineStyle.lineColor = [CPTColor blueColor];
    
    boundLinePlot.dataLineStyle = lineStyle;
    boundLinePlot.identifier = @"lineChart";
    boundLinePlot.dataSource = self;
    [graph addPlot:boundLinePlot];
    
    //设置坐标轴
    CPTXYAxisSet *axisSet = (CPTXYAxisSet *) graph.axisSet;
    
    CPTXYAxis *x = axisSet.xAxis;
    x.majorIntervalLength = CPTDecimalFromString(@"10");
    x.orthogonalCoordinateDecimal = CPTDecimalFromString(@"0");
    x.minorTicksPerInterval = 10;
//    NSArray *xexclusionRanges = [NSArray arrayWithObjects:
//                                [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(1.99) length:CPTDecimalFromFloat(0.02)],
//                                [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(0.99) length:CPTDecimalFromFloat(0.02)],
//                                [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(2.99) length:CPTDecimalFromFloat(0.02)], nil];
//    x.labelExclusionRanges = xexclusionRanges;
    
    CPTXYAxis *y = axisSet.yAxis;
    y.majorIntervalLength = CPTDecimalFromString(@"1");
    y.orthogonalCoordinateDecimal = CPTDecimalFromString(@"1");
    y.minorTicksPerInterval = 1;
    
    
    
    
    [self.view addSubview:hostingView];

}

//填充图
-(void) fillFigure{
    //创建图表
    graph = [[CPTXYGraph alloc] initWithFrame:self.view.bounds];
    
    //给图表添加一个主题
    CPTTheme *theme = [CPTTheme themeNamed:kCPTDarkGradientTheme];
    [graph applyTheme:theme];
    
    //创建画板，将图表添加到画板
    CPTGraphHostingView *hostingView = [[CPTGraphHostingView alloc] initWithFrame:self.view.bounds];
    hostingView.hostedGraph = graph;
	[self.view addSubview:hostingView];
    
    //设置图表的边框
    //左边的padding设置为0
    graph.paddingLeft = 0;
    //顶部的的padding设置0
	graph.paddingTop = 0;
    //右边的padding设置为0
	graph.paddingRight = 0;
    //底部的padding设置为0
	graph.paddingBottom = 0;
    
    //坐标区域的边框设置
    //左边的padding设置为45.0
    graph.plotAreaFrame.paddingLeft = 40.0 ;
    //顶部的padding设置为40.0
    graph.plotAreaFrame.paddingTop = 40.0 ;
    //右边的padding设置为5.0
    graph.plotAreaFrame.paddingRight = 15.0 ;
    //底部的padding设置为80.0
    graph.plotAreaFrame.paddingBottom = 80.0 ;
    
    
    //设置坐标范围
    CPTXYPlotSpace *plotSpace = (CPTXYPlotSpace *)graph.defaultPlotSpace;
    plotSpace.allowsUserInteraction = YES;
    //    plotSpace.xRange = [CPTPlotRange ];
    plotSpace.xRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(0.0) length:CPTDecimalFromFloat(200.0)];
    plotSpace.yRange = [CPTPlotRange plotRangeWithLocation:CPTDecimalFromFloat(0.0) length:CPTDecimalFromFloat(200.0)];
    
    //设置坐标刻度大小
    CPTXYAxisSet *axisSet = (CPTXYAxisSet *) graph.axisSet ;
    CPTXYAxis *x = axisSet.xAxis ;
    //x 轴：不显示小刻度线
    x. minorTickLineStyle = nil ;
    // 大刻度线间距： 50 单位
    x. majorIntervalLength = CPTDecimalFromString (@"50");
    // 坐标原点： 0
    x. orthogonalCoordinateDecimal = CPTDecimalFromString ( @"0" );
    
    CPTXYAxis *y = axisSet.yAxis ;
    //y 轴：不显示小刻度线
    y. minorTickLineStyle = nil ;
    // 大刻度线间距： 50 单位
    y. majorIntervalLength = CPTDecimalFromString ( @"50" );
    // 坐标原点： 0
    y. orthogonalCoordinateDecimal = CPTDecimalFromString (@"0");
    
    //创建绿色区域
    dataSourceLinePlot = [[CPTScatterPlot alloc] init];
    dataSourceLinePlot.identifier = @"Green Plot";
    
    //设置绿色区域边框的样式
    CPTMutableLineStyle *lineStyle = [dataSourceLinePlot.dataLineStyle mutableCopy];
    //设置线的宽度
    lineStyle.lineWidth = 1.f;
    //设置线的颜色
    lineStyle.lineColor = [CPTColor greenColor];
    //添加线到绿色区域中
    dataSourceLinePlot.dataLineStyle = lineStyle;
    //设置透明实现添加动画
    dataSourceLinePlot.opacity = 0.0f;
    
    //设置数据元代理
    dataSourceLinePlot.dataSource = self;
    //绿色区域添加到图表中
    [graph addPlot:dataSourceLinePlot];
    
    // 创建一个颜色渐变：从 建变色 1 渐变到 无色
    CPTGradient *areaGradient = [ CPTGradient gradientWithBeginningColor :[CPTColor greenColor] endingColor :[CPTColor colorWithComponentRed:0.65 green:0.65 blue:0.16 alpha:0.2]];
    // 渐变角度： -90 度（顺时针旋转）
    areaGradient.angle = -90.0f ;
    // 创建一个颜色填充：以颜色渐变进行填充
    CPTFill *areaGradientFill = [ CPTFill fillWithGradient :areaGradient];
    // 为图形设置渐变区
    dataSourceLinePlot.areaFill = areaGradientFill;
    dataSourceLinePlot.areaBaseValue = CPTDecimalFromString ( @"0.0" );
    dataSourceLinePlot.interpolation = CPTScatterPlotInterpolationLinear ;
    
    
    dataForPlot1 = [[NSMutableArray alloc] init];
    //    j = 200;
    //    r = 0;
    //    timer1 = [NSTimer scheduledTimerWithTimeInterval:1 target:self selector:@selector(dataOpt) userInfo:nil repeats:YES];
    //    [timer1 fire];
    [self plotData];
}

//添加数据
-(void) plotData{
    if ([dataSourceLinePlot.identifier isEqual:@"Green Plot"]) {
        NSString *xp1 = [NSString stringWithFormat:@"%d",1];
        NSString *yp1 = [NSString stringWithFormat:@"%d",10];
        NSMutableDictionary *point1 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp1, @"x", yp1, @"y", nil];
        [dataForPlot1 insertObject:point1 atIndex:0];
        
        NSString *xp2 = [NSString stringWithFormat:@"%d",10];
        NSString *yp2 = [NSString stringWithFormat:@"%d",25];
        NSMutableDictionary *point2 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp2, @"x", yp2, @"y", nil];
        [dataForPlot1 insertObject:point2 atIndex:1];
        
        NSString *xp3 = [NSString stringWithFormat:@"%d",30];
        NSString *yp3 = [NSString stringWithFormat:@"%d",15];
        NSMutableDictionary *point3 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp3, @"x", yp3, @"y", nil];
        [dataForPlot1 insertObject:point3 atIndex:2];
        
        NSString *xp4 = [NSString stringWithFormat:@"%d",50];
        NSString *yp4 = [NSString stringWithFormat:@"%d",80];
        NSMutableDictionary *point4 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp4, @"x", yp4, @"y", nil];
        [dataForPlot1 insertObject:point4 atIndex:3];
        
        NSString *xp5 = [NSString stringWithFormat:@"%d",70];
        NSString *yp5 = [NSString stringWithFormat:@"%d",60];
        NSMutableDictionary *point5 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp5, @"x", yp5, @"y", nil];
        [dataForPlot1 insertObject:point5 atIndex:4];
        
        NSString *xp6 = [NSString stringWithFormat:@"%d",90];
        NSString *yp6 = [NSString stringWithFormat:@"%d",100];
        NSMutableDictionary *point6 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp6, @"x", yp6, @"y", nil];
        [dataForPlot1 insertObject:point6 atIndex:5];
        
        NSString *xp7 = [NSString stringWithFormat:@"%d",110];
        NSString *yp7 = [NSString stringWithFormat:@"%d",70];
        NSMutableDictionary *point7 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp7, @"x", yp7, @"y", nil];
        [dataForPlot1 insertObject:point7 atIndex:6];
        
        NSString *xp8 = [NSString stringWithFormat:@"%d",130];
        NSString *yp8 = [NSString stringWithFormat:@"%d",80];
        NSMutableDictionary *point8 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp8, @"x", yp8, @"y", nil];
        [dataForPlot1 insertObject:point8 atIndex:7];
        
        NSString *xp9 = [NSString stringWithFormat:@"%d",200];
        NSString *yp9 = [NSString stringWithFormat:@"%d",135];
        NSMutableDictionary *point9 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp9, @"x", yp9, @"y", nil];
        [dataForPlot1 insertObject:point9 atIndex:8];
    }
}
//使用CorePlot的委托方法 呈现图形 - lineChart
-(NSUInteger)numberOfRecordsForPlot:(CPTPlot *)plot{
    return [self.points count];
}

-(NSNumber *)numberForPlot:(CPTPlot *)plot field:(NSUInteger)fieldEnum recordIndex:(NSUInteger)index{
    NSString *key = (fieldEnum == CPTScatterPlotFieldX ? @"x" : @"y");
    NSNumber *num = [[self.points objectAtIndex:index] valueForKey:key];
    return num;
}


//使用CorePlot的委托方法 呈现图形 - fillFigure
//-(NSUInteger)numberOfRecordsForPlot:(CPTPlot *)plot{
//    return [dataForPlot1 count];
//}
//
//-(NSNumber *)numberForPlot:(CPTPlot *)plot field:(NSUInteger)fieldEnum recordIndex:(NSUInteger)index{
//    NSNumber *num;
//    //让视图偏移
//	if ( [(NSString *)plot.identifier isEqualToString:@"Green Plot"] ) {
//        NSString *key = (fieldEnum == CPTScatterPlotFieldX ? @"x" : @"y");
//        
//        num = [[dataForPlot1 objectAtIndex:index] valueForKey:key];
//        if ( fieldEnum == CPTScatterPlotFieldX ) {
//			num = [NSNumber numberWithDouble:[num doubleValue] - r];
//		}
//	}
//    //添加动画效果
//    CABasicAnimation *fadeInAnimation = [CABasicAnimation animationWithKeyPath:@"opacity"];
//	fadeInAnimation.duration = 1.0f;
//	fadeInAnimation.removedOnCompletion = NO;
//	fadeInAnimation.fillMode = kCAFillModeForwards;
//	fadeInAnimation.toValue = [NSNumber numberWithFloat:2.0];
//	[dataSourceLinePlot addAnimation:fadeInAnimation forKey:@"animateOpacity"];
//    return num;
//}


- (void) dataOpt{
    //添加随机数
    if ([dataSourceLinePlot.identifier isEqual:@"Green Plot"]) {
        NSString *xp = [NSString stringWithFormat:@"%d",j];
        NSString *yp = [NSString stringWithFormat:@"%d",(rand()%100)];
        NSMutableDictionary *point1 = [[NSMutableDictionary alloc] initWithObjectsAndKeys:xp, @"x", yp, @"y", nil];
        [dataForPlot1 insertObject:point1 atIndex:0];
    }
    //刷新画板
    [graph reloadData];
    j = j + 20;
    r = r + 20;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation{
    
    return (interfaceOrientation != UIInterfaceOrientationPortraitUpsideDown);
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
```
