---
title: "如何使用Cocos2D制作一款简单的iphone游戏"
date: "2025-06-24 11:24:39"
slug: "ru-he-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/24/如何使用Cocos2D制作一款简单的iphone游戏/"
  - "/2025/06/24/如何使用Cocos2D制作一款简单的iphone游戏.html"
  - "/如何使用Cocos2D制作一款简单的iphone游戏/"
  - "/如何使用Cocos2D制作一款简单的iphone游戏.html"
  - "/2025/06/24/ru-he-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi/"
  - "/2025/06/24/ru-he-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi.html"
  - "/ru-he-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi.html"
---
Cocos2D是一款功能强大的iphone游戏引擎，它可以很大程度上节约你的游戏开发时间。它包含sprite（精灵），绚丽的特效，animations（动画），物理引擎，声音引擎，以及其他一些相当实用的功能。

我也是刚接触Cocos2D，虽然目前市面上有很多cocos2d相关的教程，但我没能找到我想到的那种入门级别的教程-如何制作一款非常简单但是功能齐全的游戏。对于入门教程，这款游戏应当仅仅包含一些较为基础的功能，如animation（动画）, collisions（碰撞）和声音。

### [下载并安装Cocos2D](#1)

你可以从以下地址下载到最新的[Cocos2Dthe Cocos2D Google Code page](https://code.google.com/p/cocos2d-iphone/).

下载完成后，你需要安装实用的project templates（工程模板）。在mac下打开一个终端窗口，

进入到刚刚下载到的Cocos2D的目录并输入以下指令： ./install-templates.sh -f -u

注意，如果xcode没有安装在默认目录下，在这里你可以选择性的在指令后添加参数（如果你的机器曾经安装过多个版本的SDK的话，那么很可能之前你已经会用这种方法了）。

### [Hello, Cocos2D!](#2)

让我们从建立一个简单的Hello World程序开始吧！

启动Xcode，选择cocos2d Application template建立一个新工程。将其命名为 “Cocos2DSimpleGame”。

编译(Cmd+B)并运行(Cmd+R)

Cocos2D是以场景（scenes）组织的，对一个游戏来说，场景可以是关卡或者是屏幕。比如游戏一开始的主菜单场景，游戏中运行起来的场景，还有游戏结束game over的场景。在场景中，可以有很多的层layers（很像photoshop中的层），层中又可以包含很多节点nodes比如精灵sprite，文本labels，菜单menus和其他的。同时每个节点又可以包含其他的节点（例如一个sprite节点可以包含另一个sprite节点作为他的child）。

观察下Hello World示例工程，会发现里边只有一个层-HelloWorldLayer-我们准备在这儿实现我们主要的游戏逻辑。打开这个文件，会看到在init方法里边被加入了一个写着”Hello World”的label，现在删除掉它，我们以后将用一个sprite来替换它。

### [添加一个Sprite](#3)

在添加一个sprie之前，我们需要一些图片，你可以使用自己创建的，或者直接使用我（ray）可爱的妻子为这个项目制作的图片资源： [a Player image](http://d1xzuxjlafny7l.cloudfront.net/downloads/Player.png), [a Projectile image](http://d1xzuxjlafny7l.cloudfront.net/downloads/Projectile.png), and [a Target image](http://d1xzuxjlafny7l.cloudfront.net/downloads/Target.png).

获得这些图片后，把它们从finder里拖拽进Xcode工程的resources文件夹下，确保”Copy items into destination group’s folder （if needed）是选中的。

好的，现在有了图片资源，下面要计算出该往哪里放置我们的主人公。需要注意的是在Cocos2D里，屏幕的左下角是(0,0)点，随着你往右上方向移动，x和y值会随之增加。因为本项目是landscape模式的（手机横向放置），所以这意味着右上角的坐标是(480,320)。

还需要注意的是，每当设置一个对象的坐标，默认情况下设置的是该对象自身中心的位置。所以如果想把主人公sprite放置到屏幕的横向左边缘，纵向屏幕一半的位置，需要执行以下两步：

x坐标，设置其为`[player sprite's width]/2`。

y坐标，设置其为`[window height]/2`。

这就试试看！打开Classes文件夹并点击HelloWorldLayer.m，用以下内容替换掉init方法：

```objectivec
-(id) init
{
  if( (self=[super init] )) {
    CGSize winSize = [[CCDirector sharedDirector] winSize];
    CCSprite *player = [CCSprite spriteWithFile:@"Player.png" 
      rect:CGRectMake(0, 0, 27, 40)];
    player.position = ccp(player.contentSize.width/2, winSize.height/2);
    [self addChild:player];
  }
  return self;
}
```

编译并运行，主人公sprite跃然屏幕之上，但注意背景默认是黑色的，白色看起来也许会更好点儿。使用CCLayerColor class可以简单的完成这一目标。打开HelloWorldLayer.h并修改其interface 声明部分：

```objectivec
@interface HelloWorldLayer : CCLayerColor
```

然后打开HelloWorldLayer.m，对init方法做一个轻微的修改：

```objectivec
if( (self=[super initWithColor:ccc4(255,255,255,255)] )) {
```

背景就顺利变为了白色。

编译并运行，主人公出现在白色背景之上了，哈哈，我们的小忍者看起来跃跃欲试了！

### [移动靶子Moving Targets](#4)

接下来为了让我们的忍者不至于独孤求败，我们加入一些靶子，为了让游戏更有趣，可以让靶子移动起来-否则游戏将不会有很好的挑战性。将这些靶子稍微向右移出屏幕一点儿，并给他们设置一个向左移动的动作。

在init方法之前添加以下方法：

```objectivec
-(void)addTarget {
 
  CCSprite *target = [CCSprite spriteWithFile:@"Target.png" 
    rect:CGRectMake(0, 0, 27, 40)]; 
 
  // Determine where to spawn the target along the Y axis
  CGSize winSize = [[CCDirector sharedDirector] winSize];
  int minY = target.contentSize.height/2;
  int maxY = winSize.height - target.contentSize.height/2;
  int rangeY = maxY - minY;
  int actualY = (arc4random() % rangeY) + minY;
 
  // Create the target slightly off-screen along the right edge,
  // and along a random position along the Y axis as calculated above
  target.position = ccp(winSize.width + (target.contentSize.width/2), actualY);
  [self addChild:target];
 
  // Determine speed of the target
  int minDuration = 2.0;
  int maxDuration = 4.0;
  int rangeDuration = maxDuration - minDuration;
  int actualDuration = (arc4random() % rangeDuration) + minDuration;
 
  // Create the actions
  id actionMove = [CCMoveTo actionWithDuration:actualDuration 
    position:ccp(-target.contentSize.width/2, actualY)];
  id actionMoveDone = [CCCallFuncN actionWithTarget:self 
    selector:@selector(spriteMoveFinished:)];
  [target runAction:[CCSequence actions:actionMove, actionMoveDone, nil]];
 
}
```

为了让事情更容易理解，我使用了有点儿冗长的方式来讲解。这一部分其实就是和之前主人公sprite同样的方式来计算对象该放到哪儿，设置坐标并将其加入到场景中去。

唯一不同的是这里加入了actions（动作）。Cocos2D内部提供了许多极为便利的动作来给你的sprite动起来，例如move actions（移动），jump actions（跳跃），fade actions（渐隐渐现），animation actions（动画）等等，这里我们只用其中的三个action：

* CCMoveTo: 使用CCMoveTo action来让对象从右侧屏幕外移动到屏幕左侧。注意可以通过指定duration参数控制这一过程需要多久，这里我们随机给他2-4秒的时间。
* CCCallFuncN: CCCallFuncN action 允许我们指定一个在动作执行完成后执行的回调函数。暂时写一个空的回调“spriteMoveFinished”，以后再填入内容。
* CCSequence: CCSequence action 允许将一系列动作按先后顺序组合成一个动作，一次执行，这里，让CCMoveTo首先执行，当它完成时，再执行CCCallFuncN动作。

接下来，添加上文提到的那个CCCallFuncN action中需要的回调函数，在addTarget:方法之前添加以下内容：

```objectivec
-(void)spriteMoveFinished:(id)sender {
  CCSprite *sprite = (CCSprite *)sender;
  [self removeChild:sprite cleanup:YES];
}
```

此方法的目的是一旦sprite超出屏幕范围，就将其从屏幕上移除。随着靶子数量的不断增加，如果不及时清理之，将会有严重的内存泄漏问题出现。解决这个问题也可以使用另一种更为高端的手段-使用数组存储一系列可以重复使用的sprites对象，但对于这篇初学者教学来说，我们用目前这个基础的方法即可。

在继续前还有一件事儿要做。我们需要实际调用创建靶子的方法。为了让游戏更有趣，我们让靶子每隔一小段时间就出现。通过每隔一段时间就会被调用的schedule（调度）回调函数，就能完成这个目标。每隔一秒刷新一个靶子，在init方法里的return之前加入以下内容：

```objectivec
[self schedule:@selector(gameLogic:) interval:1.0];
```

接下来在回调函数里填入如下内容：

```objectivec
-(void)gameLogic:(ccTime)dt {
  [self addTarget];
}
```

编译并运行，你会看到靶子们欢快地在屏幕上移动着：

### [射击Shooting Projectiles](#5)

到这里，主人公忍者多么渴望着被添加一个射击动作。虽然有很多方法可以实现射击，但是这个游戏里，我们希望每当用户触摸屏幕时，让主人公向着触摸的方向发射一个飞镖。

我使用CCMoveTo action来让所有逻辑尽量简单，但是使用它还是需要一丁点儿数学计算。CCMoveTo需要被指定一个目标点，我们不能直接使用用户触摸屏幕的点，因为这个点仅仅能表示主人公射击靶子的方向，实际上我们想让飞镖持续飞行到一直飞出屏幕为止。

首先我们在层里启用触摸，在init方法中加入：

```objectivec
self.isTouchEnabled = YES;
```

由于启用了触摸，在层里会接收到相应的触摸回调函数。每当用户的手指从屏幕抬起，将会触发ccTouchesEnded方法，我们这就实现它：

```objectivec
- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
 
  // Choose one of the touches to work with
  UITouch *touch = [touches anyObject];
  CGPoint location = [touch locationInView:[touch view]];
  location = [[CCDirector sharedDirector] convertToGL:location];
 
  // Set up initial location of projectile
  CGSize winSize = [[CCDirector sharedDirector] winSize];
  CCSprite *projectile = [CCSprite spriteWithFile:@"Projectile.png" 
    rect:CGRectMake(0, 0, 20, 20)];
  projectile.position = ccp(20, winSize.height/2);
 
  // Determine offset of location to projectile
  int offX = location.x - projectile.position.x;
  int offY = location.y - projectile.position.y;
 
  // Bail out if we are shooting down or backwards
  if (offX <= 0) return;
 
  // Ok to add now - we've double checked position
  [self addChild:projectile];
 
  // Determine where we wish to shoot the projectile to
  int realX = winSize.width + (projectile.contentSize.width/2);
  float ratio = (float) offY / (float) offX;
  int realY = (realX * ratio) + projectile.position.y;
  CGPoint realDest = ccp(realX, realY);
 
  // Determine the length of how far we're shooting
  int offRealX = realX - projectile.position.x;
  int offRealY = realY - projectile.position.y;
  float length = sqrtf((offRealX*offRealX)+(offRealY*offRealY));
  float velocity = 480/1; // 480pixels/1sec
  float realMoveDuration = length/velocity;
 
  // Move projectile to actual endpoint
  [projectile runAction:[CCSequence actions:
    [CCMoveTo actionWithDuration:realMoveDuration position:realDest],
    [CCCallFuncN actionWithTarget:self selector:@selector(spriteMoveFinished:)],
    nil]];
 
}
```

在第一部分里，我们从touches对象集合中选择一个，得到他在当前屏幕上的坐标，通过调用convertToGL来把此坐标转换为当前屏幕模式适应的，这一点很重要，因为我们使用的是landscape模式。

接下来加载飞镖sprite并像往常一样设置其初始坐标。根据之前讨论过的相似三角形算法，我们计算得到飞镖的终点。

注意这个算法并不完美。即使飞镖的Y坐标已经出了屏幕，它还是会被强制移动到X坐标移出屏幕为止。想解决这个有很多手段，包括检测射击点到屏幕边缘的最短距离，在游戏逻辑的回调里检测飞镖坐标是否在屏幕之外（比如visit），虽然这些方法都可以解决它，但简单起见，这篇初学者教程还是会使用之前的方式。

最后一件事儿是决定运动所需的时间。飞镖最好是能以固定的速率射出，所以我们还需要一丁点儿数学计算。使用 勾股定理可以轻松地得到斜边的长度。

一旦有了距离，只需要将其除以一个固定的速率，便可得到时间。

剩余部分就像我们之前做的，给靶子设置上actions。编译并运行，哈哈，你的忍者能给予冲过来的鬼头靶子致命打击了！

### [碰撞检测Collision Detection](#6)

飞镖四处飞，但我们的小忍者并没有看到飞镖击倒鬼头靶子。是时候加入一些检测飞镖与靶子碰撞检测的代码了。

使用Cocos2D有很多途径解决这个，包括使用其中一个引擎包含的物理引擎：Box2D或者Chipmunk。为了有效说明问题的本质并使事情简单，我们将自己实现一个简单的碰撞检测。

首先，我们需要记录所有在当前场景里的靶子和飞镖对象。在HelloWorldLayer类的声明中加入：

```objectivec
NSMutableArray *_targets;
NSMutableArray *_projectiles;
```

并在init方法里加入初始化数组的代码：

```objectivec
_targets = [[NSMutableArray alloc] init];
_projectiles = [[NSMutableArray alloc] init];
```

在dealloc方法里边清理之：

```objectivec
[_targets release];
_targets = nil;
[_projectiles release];
_projectiles = nil;
```

现在，修改addTarget方法，在靶子数组中加入一个新靶子并设置其标识（tag）留待后用：

```objectivec
target.tag = 1;
[_targets addObject:target];
```

同样的，把在ccTouchesEnded里新建的飞镖加入到飞镖数组中并设置tag留待后用：

```objectivec
projectile.tag = 2;
[_projectiles addObject:projectile];
```

最后，修改spriteMoveFinished方法，根据tag分类把即将删除的对象从数组中也移除掉：

```objectivec
if (sprite.tag == 1) { // target
  [_targets removeObject:sprite];
} else if (sprite.tag == 2) { // projectile
  [_projectiles removeObject:sprite];
}
```

编译并运行，确保到目前为止一切都OK。虽然目前还看不到什么显著的变化，但我们已经有了做碰撞检测的基础了。

添加以下方法到HelloWorldLayer：

```objectivec
- (void)update:(ccTime)dt {
 
  NSMutableArray *projectilesToDelete = [[NSMutableArray alloc] init];
  for (CCSprite *projectile in _projectiles) {
    CGRect projectileRect = CGRectMake(
      projectile.position.x - (projectile.contentSize.width/2), 
      projectile.position.y - (projectile.contentSize.height/2), 
      projectile.contentSize.width, 
      projectile.contentSize.height);
 
    NSMutableArray *targetsToDelete = [[NSMutableArray alloc] init];
    for (CCSprite *target in _targets) {
      CGRect targetRect = CGRectMake(
        target.position.x - (target.contentSize.width/2), 
        target.position.y - (target.contentSize.height/2), 
        target.contentSize.width, 
        target.contentSize.height);
 
      if (CGRectIntersectsRect(projectileRect, targetRect)) {
        [targetsToDelete addObject:target];
      }
    }
 
    for (CCSprite *target in targetsToDelete) {
      [_targets removeObject:target];
      [self removeChild:target cleanup:YES];
    }
 
    if (targetsToDelete.count > 0) {
      [projectilesToDelete addObject:projectile];
    }
    [targetsToDelete release];
  }
 
  for (CCSprite *projectile in projectilesToDelete) {
    [_projectiles removeObject:projectile];
    [self removeChild:projectile cleanup:YES];
  }
  [projectilesToDelete release];
}
```

以上内容很清晰。我们遍历了一下飞镖和靶子数组，在遍历中得到每一个对象的bounding box（碰撞框），使用CGRectIntersectsRect来检测两个矩形是否相交。如果有相交，则将飞镖和靶子分别从场景和数组中移除。注意我们必须将这些对象加入到“toDelete”结尾的数组中，因为我们没法在当前循环中从数组中删掉它。还是一样，有很多更优的方法来解决这类问题，简单起见，我使用最简单的方法。

你仅仅需要一步就可以欢呼了，使用schedule调度这个方法，使其在每一帧都执行：

```objectivec
[self schedule:@selector(update:)];
```

编译并运行，所有和飞镖碰撞的靶子都会灰飞烟灭了！

### [完成触摸Finishing Touches](#7)

我们已经非常接近制作出一个成品（但很简单）的游戏了。只需要再加入一些音效和音乐（没有游戏不带声音的！）以及一些简单的游戏逻辑。

如果你阅读过我的blog series on audio programming for the iPhone这篇教程，你会非常欣喜地发现在Cocos2D中播放声音原来如此简单。

首先，把背景音乐和一个射击音效拖拽进你的工程的resources文件夹。你可以随意使用以下资源cool background music I made or my awesome pew-pew sound effect, 或者制作你自己的。

接下来在HelloWorldLayer.m的一开头导入头文件：

```objectivec
#import "SimpleAudioEngine.h"
```

在init方法中，如下所示播放背景音乐：

```objectivec
[[SimpleAudioEngine sharedEngine] playBackgroundMusic:@"background-music-aac.caf"];
```

在ccTouchesEnded方法中播放音效：

```objectivec
[[SimpleAudioEngine sharedEngine] playEffect:@"pew-pew-lei.caf"];
```

现在，我们加入一个提示“You Win”或者“You Lose”的游戏结束场景。右键点击Classes文件夹，选择FileNew File，并选择Objective-C class，确保继承的类是NSObject。点击Next，在filename位置输入GameOverScene作为文件名，确保“Also create GameOverScene.h”是选中的。

用以下内容替换掉GameOverScene.h：

```objectivec
#import "cocos2d.h"
 
@interface GameOverLayer : CCLayerColor {
  CCLabelTTF *_label;
}
@property (nonatomic, retain) CCLabelTTF *label;
@end
 
@interface GameOverScene : CCScene {
  GameOverLayer *_layer;
}
@property (nonatomic, retain) GameOverLayer *layer;
@end
```

用以下内容替换掉GameOverScene.m：

```objectivec
#import "GameOverScene.h"
#import "HelloWorldLayer.h"
 
@implementation GameOverScene
@synthesize layer = _layer;
 
- (id)init {
 
  if ((self = [super init])) {
    self.layer = [GameOverLayer node];
    [self addChild:_layer];
  }
  return self;
}
 
- (void)dealloc {
  [_layer release];
  _layer = nil;
  [super dealloc];
}
 
@end
 
@implementation GameOverLayer
@synthesize label = _label;
 
-(id) init
{
  if( (self=[super initWithColor:ccc4(255,255,255,255)] )) {
 
    CGSize winSize = [[CCDirector sharedDirector] winSize];
    self.label = [CCLabelTTF labelWithString:@"" fontName:@"Arial" fontSize:32];
    _label.color = ccc3(0,0,0);
    _label.position = ccp(winSize.width/2, winSize.height/2);
    [self addChild:_label];
 
    [self runAction:[CCSequence actions:
      [CCDelayTime actionWithDuration:3],
      [CCCallFunc actionWithTarget:self selector:@selector(gameOverDone)],
      nil]];
 
  }
  return self;
}
 
- (void)gameOverDone {
 
  [[CCDirector sharedDirector] replaceScene:[HelloWorldLayer scene]];
 
}
 
- (void)dealloc {
  [_label release];
  _label = nil;
  [super dealloc];
}
@end
```

注意这里有两个不同的对象：一个scene和一个layer。一个scene可以包含很多layer。不过目前这个只有一个，这个layer只是放置了一个label在屏幕中心，并schedule了一个3秒会自动返回Hello World场景的事件。

最后，加入一些极为简单的游戏逻辑进去。首先，记录一下被主人公的飞镖干掉的靶子。在HelloWorldLayer类中加入一个成员变量，在HelloWorldLayer.h中的@interface块儿加入如下：

```objectivec
int _projectilesDestroyed;
```

在HelloWorldLayer.m里，导入GameOverScene类：

```objectivec
#import "GameOverScene.h"
```

在update方法中，增加飞镖摧毁靶子的数量并检测获得胜利的条件，在removeChild:target:之后加入:

```objectivec
_projectilesDestroyed++;
if (_projectilesDestroyed > 30) {
  GameOverScene *gameOverScene = [GameOverScene node];
  _projectilesDestroyed = 0;
  [gameOverScene.layer.label setString:@"You Win!"];
  [[CCDirector sharedDirector] replaceScene:gameOverScene];
}
```

当有鬼头靶子越过了屏幕左侧，你就输了，修改spriteMoveFinished方法，在tag == 1 case中removeChild:sprite:方法之后加入：

```objectivec
GameOverScene *gameOverScene = [GameOverScene node];
[gameOverScene.layer.label setString:@"You Lose :["];
[[CCDirector sharedDirector] replaceScene:gameOverScene];
```

编译并执行，现在你胜利或失败后会进入game over场景中，根据条件的不同会显示相应信息。

源码拿来！[Gimme The Code!](http://d1xzuxjlafny7l.cloudfront.net/downloads/Cocos2DSimpleGame.zip)

就到这里！这是到目前为止所有的源码下载地址simple Cocos2D iPhone game

