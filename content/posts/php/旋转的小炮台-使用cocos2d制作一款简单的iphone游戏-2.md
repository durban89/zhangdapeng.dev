---
title: "旋转的小炮台：使用cocos2d制作一款简单的iphone游戏-2"
date: "2025-06-24 14:45:48"
slug: "xuan-zhuan-de-xiao-pao-tai-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi-2"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/24/旋转的小炮台：使用cocos2d制作一款简单的iphone游戏-2/"
  - "/2025/06/24/旋转的小炮台：使用cocos2d制作一款简单的iphone游戏-2.html"
  - "/旋转的小炮台：使用cocos2d制作一款简单的iphone游戏-2/"
  - "/旋转的小炮台：使用cocos2d制作一款简单的iphone游戏-2.html"
  - "/2025/06/24/旋转的小炮台-使用cocos2d制作一款简单的iphone游戏-2/"
  - "/2025/06/24/旋转的小炮台-使用cocos2d制作一款简单的iphone游戏-2.html"
  - "/2025/06/24/xuan-zhuan-de-xiao-pao-tai-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi-2/"
  - "/2025/06/24/xuan-zhuan-de-xiao-pao-tai-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-.html"
  - "/xuan-zhuan-de-xiao-pao-tai-shi-yong-cocos2d-zhi-zuo-yi-kuan-jian-dan-de-iphone-you-xi-2.html"
---
### [准备工作Getting Set Up](#1)

如果你跟着[如何使用Cocos2D制作一款简单的iphone游戏](https://www.gowhich.com/blog/409)并完成了上一篇教学，那么使用你目前的工程即可。

下一步，下载新的[player sprite](http://d1xzuxjlafny7l.cloudfront.net/downloads/Player2.jpg)和[projectile sprite](http://d1xzuxjlafny7l.cloudfront.net/downloads/Projectile2.jpg)图片，并把它们加入到你的工程，从工程中删除旧的Player.jpg和Projectile.jpg。把创建每个sprite的地方修改如下：

```objectivec
// In the init method
CCSprite *player = [CCSprite spriteWithFile:@"Player2.jpg"];
// In the ccTouchesEnded method
CCSprite *projectile = [CCSprite spriteWithFile:@"Projectile2.jpg"];
```

注意，这次我们没有特别指定sprite的高度和宽度，并让Cocos2D替我们处理之。

编译并运行工程，如果一切顺利你会看到一个不断射击的小炮台。不过，它看起来不是很好，因为他完全没有向着该冲着的方向射击-让我们来修复它！

### [旋转射击Rotating To Shoot](#2)

在我们让炮台转起来之前，先存储一个主人公（现在是炮台了）sprite的引用，以便之后可以旋转它。打开HelloWorldLayer.m并修改类使其包含以下成员变量：

```objectivec
CCSprite *_player;
```

然后修改init方法里边的代码，加入player对象到层中：

```objectivec
_player = [[CCSprite spriteWithFile:@"Player2.jpg"] retain];
_player.position = ccp(_player.contentSize.width/2, winSize.height/2);
[self addChild:_player];
```

最后一定要在我们忘记释放内存这件事之前释放内存，在dealloc中加入：

```objectivec
[_player release];
_player = nil;
```

好的，现在我们获得了player对象的引用，旋转它的时刻到啦！为了旋转它，我们必须先计算出它需要转到的角度。

回想一下中学时学过的三角几何学吧。还记得方便记忆的SOH CAH TOA（译者注：其实就是对应的sin cos和tan）吗？那么，tangent就是对边/临边

我们想要的角度即等于，Y offset除以X offset的结果的反正切arctangent。

然而有两件事儿我们要牢记在心，第一，当我们计算得到反正切arctangent(offY / offX)，结果是弧度，但是Cocos2D使用的是角度。幸运的是，Cocos2D提供了一个方便使用的弧度转角度的宏。

第二，我们一般会认为上图中的角度是正的（大概20度左右），但在Cocos2D里边正向是顺时针的（并不是平常认为的逆时针）。

所以为了得到正确的方向，我们需要把结果乘上-1。比如上图中的20度，乘上-1，就得到能表示逆时针的20度角了。

好了不多说了，让我们付诸代码！在ccTouchesEnded里你调用projectile的runAction之前加入以下代码：

```objectivec
CGPoint shootVector = ccpSub(location, _nextProjectile.position);
CGFloat shootAngle = ccpToAngle(shootVector);
CGFloat cocosAngle = CC_RADIANS_TO_DEGREES(-1 * shootAngle);

CGFloat curAngle = _player.rotation;
CGFloat rotateDiff = cocosAngle - curAngle;

if(rotateDiff > 180) rotateDiff -= 360;
if(rotateDiff < -180) rotateDiff += 360;

CGFloat rotateSpeed = 360;
CGFloat rotateDuration = fabs(rotateDiff / rotateSpeed);
_player.rotation = cocosAngle;
```

编译并运行，小炮台就可以自由地旋转着发射了！

### [旋转之后才射击Rotate Then Shoot](#3)

到目前为止都很好，除了有一点有点儿奇怪的，炮台会突然转到一个方向并射击，而不是缓慢的转动过去。我们可以修复这个，但是需要稍微重构下我们的代码。

首先打开HelloWorldLayer.h并在类中加入如下成员变量：

```objectivec
CCSprite *_nextProjectile;
```

然后修改ccTouchesEnded 并加入一个叫finishShoot的方法，如下所示：

```objectivec
- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    //播放音乐
    [[SimpleAudioEngine sharedEngine] playEffect:@"pew-pew-lei.caf"];
    
    if (_nextProjectile != nil) return;
    
    // Choose one of the touches to work with
    UITouch *touch = [touches anyObject];
    CGPoint location = [touch locationInView:[touch view]];
    location = [[CCDirector sharedDirector] convertToGL:location];
    
    // Set up initial location of projectile
    CGSize winSize = [[CCDirector sharedDirector] winSize];
    _nextProjectile = [CCSprite spriteWithFile:@"Projectile2.jpg"];
    _nextProjectile.position = _player.position;
    
    
    CGPoint shootVector = ccpSub(location, _nextProjectile.position);
    CGFloat shootAngle = ccpToAngle(shootVector);
    CGFloat cocosAngle = CC_RADIANS_TO_DEGREES(-1 * shootAngle);
    
    CGFloat curAngle = _player.rotation;
    CGFloat rotateDiff = cocosAngle - curAngle;
    
    if(rotateDiff > 180) rotateDiff -= 360;
    if(rotateDiff < -180) rotateDiff += 360;
    
    CGFloat rotateSpeed = 360;
    CGFloat rotateDuration = fabs(rotateDiff / rotateSpeed);
    
    [_player runAction:[CCSequence actions:
                        [CCRotateTo actionWithDuration:rotateDuration angle:cocosAngle],
                        [CCCallFunc actionWithTarget:self selector:@selector(finishShoot)],
                        nil]];
    
    ccTime delta = 1.0;
    CGPoint normalizedShootVector = ccpNormalize(shootVector);
    CGPoint overshotVector = ccpMult(normalizedShootVector, 420);
    CGPoint offscreenPoint = ccpAdd(_nextProjectile.position, overshotVector);
    
    
    // Move projectile to actual endpoint
    [_nextProjectile runAction:[CCSequence actions:
                           [CCMoveTo actionWithDuration:delta position:offscreenPoint],
                           [CCCallFuncN actionWithTarget:self selector:@selector(spriteMoveFinished:)],
                           nil]];
    _nextProjectile.tag = 2;
    [_projectiles addObject:_nextProjectile];
}


-(void) finishShoot
{
    [self addChild:_nextProjectile];
    [_projectiles addObject:_nextProjectile];
    
    [_nextProjectile release];
    _nextProjectile = nil;
}
```

代码有点儿多，不过我们实际上并没有做很大个改动，很大部分都是一些小小的重构而已。罗列一下我们所做的改动：

* 在一开始我们检查nextProjectile是否为nil，如果不为nil，则意味着炮台正在旋转到射击的移动过程中。
* 之前（[如何使用Cocos2D制作一款简单的iphone游戏](https://www.gowhich.com/blog/409)中），我们使用的是一个叫做projectile的局部变量，创建的时候就将其加入到场景中了。现在我们使用成员变量创建它，但是并不立即加入到场景，而是稍后再加入。
* 我们定义炮台旋转的速度，使其每半秒旋转半个圆的弧度，一个圆有2 PI个弧度。
* 我们用弧度乘上速度（译者注：这里指的速度实际上是速度的倒数，单位是秒/弧度），得到旋转需要的时间。
* 用以前学过的方法把这些actions组合成一个sequence，让炮台转动到正确的角度后，再把飞镖加到场景中去。

让我们试一试！编译并运行，现在炮台旋转的流畅的多了。

