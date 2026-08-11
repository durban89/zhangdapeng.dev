---
title: "swift基础知识（6）- List（类似Table）"
date: "2025-07-14 14:50:46"
slug: "swift-ji-chu-zhi-shi-6-list-lei-si-table"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/14/swift基础知识（6）-List（类似Table）/"
  - "/2025/07/14/swift基础知识（6）-List（类似Table）.html"
  - "/swift基础知识（6）-List（类似Table）/"
  - "/swift基础知识（6）-List（类似Table）.html"
  - "/2025/07/14/Swift基础知识-6-List-类似Table/"
  - "/2025/07/14/Swift基础知识-6-List-类似Table.html"
  - "/2025/07/14/swift-ji-chu-zhi-shi-6-list-lei-si-table/"
  - "/2025/07/14/swift-ji-chu-zhi-shi-6-list-lei-si-table.html"
  - "/swift-ji-chu-zhi-shi-6-list-lei-si-table.html"
---
最近在了解swift这个语言，试着学习一些SwiftUI

前期看了一些SwiftUI的一些基础的内容，比如Text、Image

今天了解了下列表（List），应该可以类比与Object-c的Table相关的功能

但是使用起来真的很方便，尤其是用过React的话，会更加了解

使用React的时候，应该多多少少都用过react-router，里面有Route组件，其实里面就是html中类似a标签的封装或者history的逻辑封装（大概是基于hash，也只是猜测，源码并没有了解过）

不过在SwiftUI中也用到了类似的组件，但是名字叫做Navigation，嗯，突然想起来如果用过ReactNative的话，里面也有Navigation类似名字的组件，巧

下面看下代码

```cpp
import SwiftUI

struct CategoryHome: View {
    var categories: [String: [Landmark]] {
        Dictionary(
            grouping: landmarkData,
            by: { $0.category.rawValue }
        )
    }

    var body: some View {
        NavigationView{
            List {
                ForEach(categories.keys.sorted(), id: \.self) { key in
                    CategoryRow(categoryName: key, items: self.categories[key]!)
                }
            }
            .navigationBarTitle(Text("Featured"))
        }

    }
}

struct CategoryHome_Previews: PreviewProvider {
    static var previews: some View {
        CategoryHome()
    }
}
```

注意里面的NavigationView这个组件（其实还有一个是NavigationLink的组件），下面看下效果图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1600010197/gowhich/WX20200913-231508_2x.png)

是不是表格的效果就出来了，如果我没记错的话，如果用Object-c的话，实现这个效果，要实现相关协议的几个方法，对比现在，简直不要很简单
