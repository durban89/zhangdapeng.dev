---
title: "Yii CRUD操作"
date: "2025-06-03 15:11:26"
slug: "yii-crud-cao-zuo"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii-CRUD操作/"
  - "/2025/06/03/Yii-CRUD操作.html"
  - "/Yii-CRUD操作/"
  - "/Yii-CRUD操作.html"
  - "/2025/06/03/yii-crud-cao-zuo/"
  - "/2025/06/03/yii-crud-cao-zuo.html"
  - "/yii-crud-cao-zuo.html"
---
对于喜欢操作sql语句的人来说和对于sql语句基础不是很好的，能够明白每个CRUD操作是什么意思很重要，简单的介绍个例子，代码如下：

```php
<?php
class Post extends CActiveRecord
{
    public $fixtures = [
        'posts' => 'Post',
        'tags' => 'Tag',
    ];

    public function findPost()
    {
        //调用find时，我们使用$condition和$params指定查询条件。
        //此处$condition可以是SQL语句中的WHERE字符串，$params则是一个参数数组，
        //其中的值应绑定到$condation中的占位符。
        $post = $this->posts('post1');
        $fPost = Post::model()->find('id=:id', [':id' => $post->id]);
        //SELECT * FROM `tbl_post` `t` WHERE `t`.`id`=1 LIMIT 1

        $fPost = Post::model()->find('?', [$post->id]);
        //SELECT * FROM `tbl_post` `t` WHERE '1' LIMIT 1

        //find返回符合条件的第一条记录，而findAll会返回符合条件的所有行。
        $fAllPost = Post::model()->findAll('id=:id', [':id' => $post->id]);
        //SELECT * FROM `tbl_post` `t` WHERE id = '1'

        $fAllPost = Post::model()->findAll('?', [$post->id]);
        //SELECT * FROM `tbl_post` `t` WHERE '1'

        $criteria = new CDbCriteria();
        $criteria->condition = 'id=:id AND title=:title';
        $criteria->params = [':id' => $post->id, ':title' => $post->title];
        $fPost = Post::model()->find($criteria);
        //SELECT * FROM `tbl_post` `t` WHERE id = '1' AND title = 'post1' LIMIT 1

        $fAllPost = Post::model()->findAll($criteria);
        //SELECT * FROM `tbl_post` `t` WHERE id = '1' AND title = 'post1'

        $fPost = Post::model()->findByPk($post->id, 'title=:title', [':title' => $post->title]);
        //SELECT * FROM `tbl_post` `t` WHERE `t`.`id`=1 AND (title = 'post1') LIMIT 1

        $fPost = Post::model()->findByAttributes(['id' => $post->id, 'title' => $post->title]);
        //SELECT * FROM `tbl_post` `t` WHERE `t`.`id`='1' AND `t`.`title`='post1' LIMIT 1

        $sql = 'SELECT id, title from {{post}} WHERE id = ? AND title = ?'; //必须设置表前缀
        $fPost = Post::model()->findBySql($sql, [$post->id, $post->title]);

        $sql = 'SELECT id, title from {{post}} WHERE id = :id AND title = :title';
        $fPost = Post::model()->findBySql($sql, [':id' => $post->id, ':title' => $post->title]);

        //如果没有找到符合条件的行，find返回null，findAll返回array()。
    }

    public function countPost()
    {
        $post = $this->posts('post1');

        $cPost = Post::model()->count('?', [$post->title]);
        //SELECT COUNT(*) FROM `tbl_post` `t` WHERE 'post1' 无意义

        $cPost = Post::model()->countByAttributes(['title' => $post->title, 'content' => $post->content]);
        //SELECT COUNT(*) FROM `tbl_post` `t` WHERE `t`.`title`='post1' AND `t`.`content`='content1'

        $sql = "SELECT title from {{post}} WHERE title LIKE '%" . $post->title . "%'";
        $cPost = Post::model()->countBySql($sql);
        //至少有一条记录符合查询条件
        $ePost = Post::model()->exists('id=?ANDtitle=?', [$post->id, $post->title]);
        //SELECT 1 FROM `tbl_post` `t` WHERE id = '1' AND title = 'post1' LIMIT 1
    }

    public function updatePost()
    {
        $post = $this->posts('post1');
        $post->title = 'updatepost1';

        if ($post->isNewRecord) {
            $post->create_time = $post->update_time = new CDbExpression('NOW()');
            //UPDATE `tbl_post` SET `id`=1, `title`='update post 1', `content`='content1', `tags`=NULL, `status`=1, `create_time`=NULL, `update_time`=1302161123, `author_id`=1 WHERE `tbl_post`.`id`=1
        } else {
            $post->update_time = time();
        }

        $post->save();

        //updateAll
        $sql = "SELECT * FROM {{post}} WHERE title LIKE '%" . "post" . "%'";
        //SELECT * FROM tbl_post WHERE title LIKE '%post%'

        $post = Post::model()->findBySql($sql);
        $post->updateAll(['update_time' => time()], 'id<=?', ['2']);
        //UPDATE `tbl_post` SET `update_time`=1302161123 WHERE id <= '2'

        $post->updateByPk($post->id + 2, ['title' => 'updatepost3']);
        $post->updateByPk($post->id, ['title' => 'updatepost3'], 'id=?', ['3']);

        //updateCounter更新某个字段的数值，一般是计数器(+/-)。
        $tag = $this->tags('tag1');
        $uTag = Tag::model()->updateCounters(['frequency' => '3'], 'id=?', ['1']);
    }

    public function deletePost()
    {
        $post = $this->posts('post1');
        $post->delete();

        $this->assertEquals(1, $post->id); //删除数据库表中的记录，但是post的这个实例还在。
        $post2 = Post::model()->findByPk($post->id);
        $this->assertEquals(null, $post2);

        //多条记录
        $delete = Post::model()->deleteAll('(id = ? AND title = ?) || (id = \'4\') ', [1, 'post1']);
        $this->assertEquals(0, $delete);

        $delete = Post::model()->deleteAllByAttributes(['id' => '2'], 'content=?', ['content2']);
        //DELETE FROM `tbl_post` WHERE `tbl_post`.`id`='2' AND (content = 'content2')
        $this->assertEquals(1, $delete);
    }
}
```
