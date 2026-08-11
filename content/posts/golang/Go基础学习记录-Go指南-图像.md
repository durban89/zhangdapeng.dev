---
title: "Go基础学习记录 - Go指南 - 图像"
date: "2025-07-31 10:26:33"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-tu-xiang"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-图像/"
  - "/2025/07/31/Go基础学习记录-Go指南-图像.html"
  - "/Go基础学习记录-Go指南-图像/"
  - "/Go基础学习记录-Go指南-图像.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-tu-xiang/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-tu-xiang.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-tu-xiang.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **图像**

image 包定义了 Image 接口：

```go
package image

type Image interface {
    ColorModel() color.Model
    Bounds() Rectangle
    At(x, y int) color.Color
}
```

***注意***： Bounds 方法的返回值 Rectangle 实际上是一个 image.Rectangle， 它在 image 包中声明。

color.Color 和 color.Model 类型也是接口，但是通常因为直接使用预定义的实现 image.RGBA 和 image.RGBAModel 而被忽视了。这些接口和类型由image/color包定义。

下面看下具体该如何使用

```go
package main

import (
    "fmt"
    "image"
)

func main() {
    m := image.NewRGBA(image.Rect(0, 0, 100, 100))
    fmt.Println(m.Bounds())
    fmt.Println(m.At(0, 0).RGBA())
}
```

### **练习：图像**

还记得之前编写的图片生成器吗？我们再来编写另外一个，不过这次它将会返回一个 image.Image 的实现而非一个数据切片。

定义自己的 Image 类型，实现必要的方法并调用 pic.ShowImage 。

* Bounds 应当返回一个 image.Rectangle ，例如 `image.Rect(0, 0, w, h)` 。
* ColorModel 应当返回 color.RGBAModel 。
* At 应当返回一个颜色。上一个图片生成器的值 v 对应 `color.RGBA{v, v, 255, 255}` 。

实例演示如下

```go
package main

import "golang.org/x/tour/pic"
import "image"
import "image/color"

type Image struct{}

func (m Image) ColorModel() color.Model {
    return color.RGBAModel
}

func (m Image) Bounds() image.Rectangle {
    return image.Rect(0, 0, 50, 100)
}

func (m Image) At(x, y int) color.Color {
    return color.RGBA{200, 200, 255, 255}
}

func main() {
    m := Image{}
    pic.ShowImage(m)
}
```

运行后输出的结果如下  
![Gowhich](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAABkCAIAAABLivQMAAAAgElEQVR4nOzOMRGAMBRAMY7Dv67vihro8qZ2SBTkm/mf+7ynA3tahVahVWgVWoVWoVVoFVqFVqFVaBVahVahVWgVWoVWoVVoFVqFVqFVaBVahVahVWgVWoVWoVVoFVqFVqFVaBVahVahVWgVWoVWoVVoFVqFVqFVaBVaxQoAAP//5gEDWviXpIEAAAAASUVORK5CYII=)
