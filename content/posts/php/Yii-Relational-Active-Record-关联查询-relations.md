---
title: "Yii Relational Active Record（关联查询）relations"
date: "2025-06-09 12:03:20"
slug: "yii-relational-active-record-guan-lian-cha-xun-relations"
categories: ["技术"]
tags: ["Yii"]
aliases:
  - "/2025/06/09/Yii-Relational-Active-Record（关联查询）relations/"
  - "/2025/06/09/Yii-Relational-Active-Record（关联查询）relations.html"
  - "/Yii-Relational-Active-Record（关联查询）relations/"
  - "/Yii-Relational-Active-Record（关联查询）relations.html"
  - "/2025/06/09/Yii-Relational-Active-Record-关联查询-relations/"
  - "/2025/06/09/Yii-Relational-Active-Record-关联查询-relations.html"
  - "/2025/06/09/yii-relational-active-record-guan-lian-cha-xun-relations/"
  - "/2025/06/09/yii-relational-active-record-guan-lian-cha-xun-relations.html"
  - "/yii-relational-active-record-guan-lian-cha-xun-relations.html"
---
在使用关联AR之前，首先要在数据库中建立关联的数据表之间的主键-外键关联，AR需要通过分析数据库中的定义数据表关联的元信息，来决定如何连接数据。

### [如何声明关联](#1)

在使用AR进行关联查询之前，我们需要告诉AR各个AR类之间有怎样的关联。
AR类之间的关联直接反映着数据库中这个类所代表的数据表之间的关联。从关系数据库的角度来说，两个数据表A，B之间可能的关联有三种：一对多，一对一，多对多。而在AR中，关联有以下四种：
`BELONGS_TO`: 如果数据表A和B的关系是一对多，那我们就说B属于A（B belongs to A）。
`HAS_MANY`: 如果数据表A和B的关系是多对一，那我们就说B有多个A（B has many A）。
`HAS_ONE`: 这是‘HAS_MANY’关系中的一个特例，当A最多有一个的时候，我们说B有一个A （B has one A）。
`MANY_MANY`: 这个相当于关系数据库中的多对多关系。因为绝大多数关系数据库并不直接支持多对多的关系，这时通常都需要一个单独的关联表，把多对多的关系分解为两个一对
多的关系。用AR的方式去理解的话，我们可以认为 MANY_MANY关系是由BELONGS_TO和HAS_MANY组成的。
在AR中声明关联，是通过覆盖（Override）父类CActiveRecord中的relations()方法来实现的。这个方法返回一个包含了关系定义的数组，数组中的每一组键值代表一个关联：
`'VarName'=>array('RelationType', 'ClassName', 'ForeignKey', ...additional options)`
这里的VarName是这个关联的名称；
RelationType指定了这个关联的类型，有四个常量代表了四种关联的类型：`self::BELONGS_TO`，`self::HAS_ONE`，`self::HAS_MANY`和`self::MANY_MANY`
ClassName是这个关系关联到的AR类的类名；
ForeignKey指定了这个关联是通过哪个外键联系起来的。后面的additional
options可以加入一些额外的设置，后面会做介绍。

下面的代码演示了如何定义User和Post之间的关联。

```php
<?php
class Post extends CActiveRecord
{
    public function relations()
    {
        return [
            'author' => [
                self::BELONGS_TO,
                'User',
                'authorID',
            ],
            'categories' => [
                self::MANY_MANY,
                'Category',
                'PostCategory(postID, categoryID)',
            ],
        ];
    }
}

class User extends CActiveRecord
{
    public function relations()
    {
        return [
            'posts' => [
                self::HAS_MANY,
                'Post',
                'authorID',
            ],
            'profile' => [
                self::HAS_ONE,
                'Profile',
                'ownerID',
            ],
        ];
    }
}
```

说明: 有时外键可能由两个或更多字段组成，在这里可以将多个字段名由逗号或空格分隔，一并写在这里。对于多对多的关系，关联表必须在外键中注明，例如在Post类的categories关联中，外键就需要写成PostCategory(postID, categoryID)。
在AR类中声明关联时，每个关联会作为一个属性添加到AR类中，属性名就是关联的名称。在进行关联查询时，这些属性就会被设置为关联到的AR类的实例，例如在查询取得一个Post实例时，它的$author属性就是代表Post作者的一个User类的实例。

### [关联查询](#2)

进行关联查询最简单的方式就是访问一个关联AR对象的某个关联属性。如果这个属性之前没有被访问过，这时就会启动一个关联查询，
通过当前AR对象的主键连接相关的表，来取得关联对象的值，然后将这些数据保存在对象的属性中。这种方式叫做“延迟加载”，也就是只有等到访问到某个属性时，
才会真正到数据库中把这些关联的数据取出来。下面的例子描述了延迟加载的过程：

```php
// retrieve the post whose ID is 10
$post=Post::model()->findByPk(10);
// retrieve the post's author: a relational query will be performed here
$author=$post->author;
```

在不同的关联情况下，如果没有查询到结果，其返回的值也不同：BELONGS_TO 和 HAS_ONE 关联，无结果时返回null; HAS_MANY 和 MANY_MANY, 无结果时返回空数组。
延迟加载方法使用非常方便，但在某些情况下并不高效。例如，若我们要取得N个post的作者信息，使用延迟方法将执行N次连接查询。此时我们应当使用所谓的急切加载方法。
急切加载方法检索主要的 AR 实例及其相关的 AR 实例. 这通过使用 with() 方法加上 find 或 findAll 方法完成。例如，
`$posts=Post::model()->with('author')->findAll();`
上面的代码将返回一个由 Post 实例组成的数组. 不同于延迟加载方法，每个Post 实例中的author 属性在我们访问此属性之前已经被关联的User 实例填充。
不是为每个post 执行一个连接查询, 急切加载方法在一个单独的连接查询中取出所有的 post 以及它们的author!
我们可以在with()方法中指定多个关联名字。例如, 下面的代码将取回 posts 以及它们的作者和分类:

`$posts=Post::model()->with('author','categories')->findAll();`
我们也可以使用嵌套的急切加载。不使用一个关联名字列表, 我们将关联名字以分层的方式传递到 with() 方法, 如下,

```php
$posts = Post::model()->with(
    'author.profile',
    'author.posts',
    'categories'
)->findAll();
```

上面的代码将取回所有的 posts 以及它们的作者和分类。它也将取出每个作者的profile和 posts.
急切加载也可以通过指定 CDbCriteria::with 属性被执行, 如下:

```php
$criteria = new CDbCriteria;
$criteria->with = [
    'author.profile',
    'author.posts',
    'categories',
];
$posts = Post::model()->findAll($criteria);
```

或
```php
$posts = Post::model()->findAll(['with' => ['author.profile', 'author.posts', 'categories']];
```

### [关联查询选项](#3)

之前我们提到额外的参数可以被指定在关联声明中。这些选项，指定为 name-value 对，被用来定制关联查询。它们被概述如下：

>
>select: 为关联 AR 类查询的字段列表。默认是 '*', 意味着所有字段。查询的字段名字可用别名表达式来消除歧义（例如：COUNT(??.name) AS nameCount）。
>condition: WHERE 子语句。默认为空。注意, 列要使用别名引用（例如：??.id=10）。
>params: 被绑定到 SQL 语句的参数. 应当为一个由 name-value 对组成的数组（）。
>on: ON 子语句. 这里指定的条件将使用 and 操作符被追加到连接条件中。此选项中的字段名应被消除歧义。此选项不适用于 MANY_MANY 关联。
>order: ORDER BY 子语句。默认为空。注意, 列要使用别名引用（例如：??.age DESC）。
>with: 应当和此对象一同载入的子关联对象列表. 注意, 不恰当的使用可能会形成一个无穷的关联循环。
>joinType: 此关联的连接类型。默认是 LEFT OUTER JOIN。
>aliasToken：列前缀占位符。默认是“??.”。
>alias: 关联的数据表的别名。默认是 null, 意味着表的别名和关联的名字相同。
>together: 是否关联的数据表被强制与主表和其他表连接。此选项只对于HAS_MANY 和 MANY_MANY 关联有意义。若此选项被设置为 false, ......(此处原文出错!).默认为空。此选项中的字段名以被消除歧义。
>having: HAVING 子语句。默认是空。注意, 列要使用别名引用。
>index: 返回的数组索引类型。确定返回的数组是关键字索引数组还是数字索引数组。不设置此选项, 将使用数字索引数组。此选项只对于HAS_MANY 和 MANY_MANY 有意义
>

此外, 下面的选项在延迟加载中对特定关联是可用的:
>
>group: GROUP BY子句。默认为空。注意, 列要使用别名引用(例如：??.age)。 本选项仅应用于HAS_MANY 和 MANY_MANY 关联。
>having: HAVING子句。默认为空。注意, 列要使用别名引用(例如：??.age)。本选项仅应用于HAS_MANY 和 MANY_MANY 关联。
>limit: 限制查询的行数。本选项不能用于BELONGS_TO关联。
>offset: 偏移。本选项不能用于BELONGS_TO关联。
>

下面我们改变在 User 中的 posts 关联声明,通过使用上面的一些选项:

```php
<?php
class User extends CActiveRecord
{
    public function relations()
    {
        return [
            'posts' => [self::HAS_MANY, 'Post', 'author_id',
                'order' => 'posts.create_time DESC',
                'with' => 'categories',
            ],
            'profile' => [self::HAS_ONE, 'Profile', 'owner_id'],
        ];
    }
}
```

现在若我们访问 $author->posts, 我们将得到用户的根据发表时间降序排列的 posts. 每个 post 实例也载入了它的分类。

### [为字段名消除歧义](#4)

当一个字段的名字出现在被连接在一起的两个或更多表中，需要消除歧义(disambiguated)。可以通过使用表的别名作为字段名的前缀实现。
在关联AR查询中，主表的别名确定为 t，而一个关联表的别名和相应的关联的名字相同(默认情况下)。 例如，在下面的语句中，Post 的别名是 t ，而 Comment 的别名是 comments:
`$posts=Post::model()->with('comments')->findAll();`
现在假设 Post 和 Comment 都有一个字段 create_time , 我们希望取出 posts 及它们的 comments,
排序方式是先根据 posts 的创建时间,然后根据 comment 的创建时间。
我们需要消除create_time 字段的歧义，如下:

```php
$posts = Post::model()
    ->with('comments')
    ->findAll([
        'order' => 't.create_time, comments.create_time';,
    ]);
```

默认情况下,Yii 自动为每个关联表产生一个表别名，我们必须使用此前缀 ??. 来指向这个自动产生的别名。 主表的别名是表自身的名字。

### [动态关联查询选项](#5)
我们使用 with()和 with 均可使用动态关联查询选项。 动态选项将覆盖在 relations() 方法中指定的已存在的选项。
例如，使用上面的 User 模型， 若我们想要使用急切加载方法以升序来取出属于一个作者的 posts(关联中的order 选项指定为降序)， 我们可以这样做:

```php
User::model()->with(
    [
        'posts' => [
            'order' => 'posts.create_time ASC',
        ],
        'profile',
    ]
)->findAll();
```
动态查询选项也可以在使用延迟加载方法时使用以执行关联查询。 要这样做，我们应当调用一个方法，它的名字和关联的名字相同，并传递动态查询选项 作为此方法的参数。例如，下面的代码返回一个用户的 status 为 1 的 posts :
```php
$user = User::model()->findByPk(1);
$posts = $user->posts(['condition' => 'status=1']);
```

### [关联查询的性能](#6)
如上所述，急切加载方法主要用于当我们需要访问许多关联对象时。 通过连接所有所需的表它产生一个大而复杂的 SQL 语句。
一个大的 SQL 语句在许多情况下是首选的。然而在一些情况下它并不高效。考虑一个例子，若我们需要找出最新的文章以及它们的评论。
假设每个文章有 10 条评论，使用一个大的 SQL  语句，我们将取回很多多余的 post
数据， 因为每个post 将被它的每条评论反复使用。现在让我们尝试另外的方法：我们首先查询最新的文章，
然后查询它们的评论。用新的方法，我们需要执行执行两条 SQL 语句。有点是在查询结果中没有多余的数据。
因此哪种方法更加高效？没有绝对的
答案。执行一条大的 SQL 语句也许更加高效，因为它需要更少的花销来解析和执行 SQL 语句。另一方面，使用单条 SQL语句，我们得到更多冗余的数据，因此需要更多时间来阅读和处理它们。
因为这个原因，Yii 提供了 together 查询选项以便我们在需要时选择两种方法之一。
默认下， Yii 使用第一种方式，即产生一个单独的 SQL语句来执行急切加载。我们可以在关联声明中设置 together 选项为 false 以便一些表被连接在单独的 SQL语句中。
例如，为了使用第二种方法来查询最新的文章及它们的评论，我们可以在 Post 类中声明 comments 关联如下,

```php
function relations()
{
    return [
        'comments' => [self::HAS_MANY, 'Comment', 'post_id', 'together' => false],
    ];
}
```

当我们执行急切加载时，我们也可以动态地设置此选项:

```php
$posts = Post::model()->with(['comments' => ['together' => false]])->findAll();
```

### [统计查询](#7)
除了上面描述的关联查询，Yii 也支持所谓的统计查询(或聚合查询)。 它指的是检索关联对象的聚合信息，例如每个 post的评论的数量，每个产品的平均等级等。
统计查询只被 HAS_MANY(例如，一个 post 有很多评论) 或 MANY_MANY (例如，一个 post 属于很多分类和一个 category 有很多 post) 关联对象执行。
执行统计查询非常类似于之前描述的关联查询。我们首先需要在 CActiveRecord 的 relations() 方法中声明统计查询。

```php
class Post extends CActiveRecord
{
    public function relations()
    {
        return [
            'commentCount' => [self::STAT, 'Comment', 'post_id'],
            'categoryCount' => [self::STAT, 'Category', 'post_category(post_id,category_id)'],
        ];
    }
}
```
在上面，我们声明了两个统计查询：commentCount 计算属于一个 post 的评论的数量，categoryCount 计算一个 post所属分类的数量。
注意 Post 和 Comment 之间的关联类型是 HAS_MANY， 而 Post 和 Category 之间的关联类型是 MANY_MANY (使用连接表 PostCategory)。
如我们所看到的，声明非常类似于之间小节中的关联。唯一的不同是这里的关联类型是STAT。
有了上面的声明，我们可以检索使用表达式 $post->commentCount 检索一个 post 的评论的数量。
当我们首次访问此属性，一个 SQL 语句将被隐含地执行并检索 对应的结果。我们已经知道，这是所谓的 lazy loading方法。若我们需要得到多个post 的评论数目，我们也可以使用 eager loading 方法:
`$posts=Post::model()->with('commentCount', 'categoryCount')->findAll();`
上面的语句将执行三个 SQL 语句以取回所有的 post 及它们的评论数目和分类数目。使用延迟加载方法， 若有 N 个 post ,我们使用 2*N+1 条 SQL 查询完成。
默认情况下，一个统计查询将计算 COUNT 表达式(and thus the comment count and category countin the above example).
当我们在 relations()中声明它时，通过 指定额外的选项，可以定制它。可用的选项简介如下。
select: 统计表达式。默认是 COUNT(*)，意味着子对象的个数。
defaultValue: 没有接收一个统计查询结果时被赋予的值。例如，若一个 post 没有任何评论，它的 commentCount 将接收此值。此选项的默认值是 0。
condition: WHERE 子语句。默认是空。
params: 被绑定到产生的SQL 语句中的参数。它应当是一个 name-value 对组成的数组。
order: ORDER BY 子语句。默认是空。
group: GROUP BY 子语句。默认是空。
having: HAVING 子语句。默认是空。

### [关联查询命名空间](#8)
关联查询也可以和 命名空间一起执行。有两种形式。第一种形式，命名空间被应用到主模型。第二种形式，命名空间被应用到关联模型。
下面的代码展示了如何应用命名空间到主模型。
`$posts=Post::model()->published()->recently()->with('comments')->findAll();`
这非常类似于非关联的查询。唯一的不同是我们在命名空间后使用了 with() 调用。 此查询应当返回最近发布的 post和它们的评论。
下面的代码展示了如何应用命名空间到关联模型。
`$posts=Post::model()->with('comments:recently:approved')->findAll();`
上面的查询将返回所有的 post 及它们审核后的评论。注意 comments 指的是关联名字，而 recently 和 approved 指的是 在 Comment 模型类中声明的命名空间。关联名字和命名空间应当由冒号分隔。
命名空间也可以在 CActiveRecord::relations() 中声明的关联规则的 with 选项中指定。在下面的例子中， 若我们访问 $user->posts，它将返回此post 的所有审核后的评论。

```php
class User extends CActiveRecord
{
    public function relations()
    {
        return [
            'posts' => [self::HAS_MANY, 'Post', 'author_id', 'with' => 'comments:approved'],
        ];
    }
}
```

注意: 应用到关联模型的命名空间必须在 CActiveRecord::scopes 中指定。结果，它们不能被参数化。
