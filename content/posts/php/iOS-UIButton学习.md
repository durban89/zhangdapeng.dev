---
title: "iOS UIButton学习"
date: "2025-06-11 11:31:49"
slug: "ios-uibutton-xue-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/11/iOS-UIButton学习/"
  - "/2025/06/11/iOS-UIButton学习.html"
  - "/iOS-UIButton学习/"
  - "/iOS-UIButton学习.html"
  - "/2025/06/11/ios-uibutton-xue-xi/"
  - "/2025/06/11/ios-uibutton-xue-xi.html"
  - "/ios-uibutton-xue-xi.html"
---
本文实现的是一个不用拖控件，而是用代码写出一个按钮，然后点击弹出一个警告信息，有人问那么好的IB工具不用却去苦逼的写代码呢？因为IB高度集成开发工具，拖出的控件帮我省了很大麻烦，这个过程农民工也可以干，但是作为初学者，IB是个比较高层的东西，我们是不是应该了解一下IB底层的东西呢，如果一味追求方便快捷，哪天突然有人问怎么用代码写出来，咱岂不是要被鄙视了；所以吧，初学者不要学懒，多写代码提高我们的编程能力，当我们在开发项目或者在公司工作去用IB，来帮我们节省时间提高效率； 初始化视图代码，绘制了一个距原点(100,100)的140x50像素的按钮，有一点需要注意的是iphone的远点坐标是在左上角，屏幕640x480像素，不过现在用个是Retina分辨率，画质更加细腻；

```objectivec
- (void)viewDidLoad
{    
    [super viewDidLoad];
    
    //设置按钮类型，此处为圆角按钮
    UIButton *writeButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    //设置和大小
    CGRect frame = CGRectMake(100.0f, 100.0f, 140.0f, 50.0f);
    //将frame的位置大小复制给Button
    writeButton.frame = frame;

    //给Button添加标题  
        [writeButton setTitle:@"代码按钮" forState:UIControlStateNormal];
    //设置按钮背景颜色 
        writeButton.backgroundColor = [UIColor clearColor];
    //设置按钮标题文字对齐方式，此处为左对齐
    writeButton.contentHorizontalAlignment =UIControlContentHorizontalAlignmentLeft;
    //使文字距离做边框保持10个像素的距离。
    writeButton.contentEdgeInsets = UIEdgeInsetsMake(0,30, 0, 0);

    //此处类容目的掩饰代码代码操作按钮一些属性，如果设置按钮背景为图片可以将此处注释取消，注释掉上没横线范围类代码，进行测试
    //设置按钮背景图片
    UIImage *image= [UIImage imageNamed:@"background.png"];
    
    [writeButton setBackgroundImage:image forState:UIControlStateNormal];
    //按钮的相应事件  
    [writeButton addTarget:self action:@selector(buttonClicked:)forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:writeButton];
    UIButton *writeButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
}
```

设置按钮类型，按钮类型定义在一个枚举类型中

```objectivec
typedef enum {
 UIButtonTypeCustom = 0,    // 没有风格
 UIButtonTypeRoundedRect,   // 圆角风格按钮
 UIButtonTypeDetailDisclosure, // 详情信息按钮
 UIButtonTypeInfoLight,   // 明亮背景的信息按钮
 UIButtonTypeInfoDark,   // 黑暗背景的信息按钮
 UIButtonTypeContactAdd,   // 添加按钮
} UIButtonType;
```

但是考虑的ios开发中，为了界面美观一般设置背景图片，代替按钮的标题设置，此处推荐一个所搜icon的网址，里面有基本用的icon素材，个人觉得不错，给分享下  ~~http://www.easyicon.cn/~~ 点击打开链接 （已经不存在了）；

在点击按钮是按钮是凹下去，然后弹起才触发起事件，按钮的状态有：

```objectivec
UIControlEventTouchDown // 按下 
UIControlEventTouchDownRepeat // 多次按下 
UIControlEventTouchDragInside // 保持按下然后在按钮及其一定的外围拖动
UIControlEventTouchDragOutside // 保持按下,在按钮外面拖动
UIControlEventTouchDragEnter // DragOutside进入DragInside触发
UIControlEventTouchDragExit // in到out触发
UIControlEventTouchUpInside // 在按钮及其一定外围内松开
UIControlEventTouchUpOutside // 按钮外面松开
UIControlEventTouchCancel // 点击取消
```

弹出一个警告，一般都这样写

```objectivec
-(void) buttonClicked:(id)sender
{
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"提示" message:@"你点击了一个按钮" delegate:self cancelButtonTitle:@"OK" otherButtonTitles: nil]; 
    [alert show];
}
```

此处弹出的一个警告，主要用到UIAlertView这个类，initWithTitle初始化标题，message是弹出警告类容，提示你做了什么事，delegate是委托代理，此处不需要其他类做什么事，自个完全能搞定，所以设置为self，类似于C++中的this指针，cancelButtonTitle这个一看就能明白，取消按钮的标题是什么了，otherButtonTitles设置其他按钮，也就是说你需要更多按钮支持的时候，此处不需要，只要一个nil就好了，就如还需要其他的，你可以添加代码假如：otherButtonTitles:@"test1",@"test2",@"test3",@"test4",nil
