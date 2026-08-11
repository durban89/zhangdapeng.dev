---
title: "Nodejs Async的使用实例"
date: "2025-06-30 12:01:09"
slug: "nodejs-async-de-shi-yong-shi-li"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-Async的使用实例/"
  - "/2025/06/30/Nodejs-Async的使用实例.html"
  - "/Nodejs-Async的使用实例/"
  - "/Nodejs-Async的使用实例.html"
  - "/2025/06/30/nodejs-async-de-shi-yong-shi-li/"
  - "/2025/06/30/nodejs-async-de-shi-yong-shi-li.html"
  - "/nodejs-async-de-shi-yong-shi-li.html"
---
最近在玩nodejs，里面使用了mysql，但是如果你用过php的话，就知道过你想得到一个结果，操作的办法是从上一个sql语句中得到某个需要的值，然后再进行下一个语句使用到，使用nodejs的话，里面设计到了异步，为了达到我们需要的效果，认识了下async这个工具包。看下实例吧

```js
module.exports.index = function(req,res){
    var id = req.query.id;
    var result;
 
    var sql = "select * from ?? order by id DESC";
    var options = ['user'];
    sql = mysql.format(sql,options);
 
    async.waterfall([
        function(done){
            var sql = "select * from ?? order by id DESC";
            var options = ['user'];
            sql = mysql.format(sql,options);
 
 
            DB.select(sql,function(error,result){
                if(!result){
                    result = '';
                }
                var templates_data = new Object();
                templates_data['title'] = 'Qeeniao Admin';
                templates_data['result'] = result;
 
                done(null,result);
            });
        },
        function(list1,done){
            var sql = "select * from ?? order by id DESC";
            var options = ['user'];
            sql = mysql.format(sql,options);
 
            var tmp = [];
            if(list1.length > 0){
                list1.map(function(item){
                    tmp.push(item);
                });
            }
 
            DB.select(sql,function(error,result){
                if(!result){
                    result = [];
                }
                var templates_data = new Object();
                templates_data['title'] = 'Qeeniao Admin';
                templates_data['result'] = result;
 
                if(result.length > 0){
                    result.map(function(item){
                        tmp.push(item);
                    });
                }
                done(null,tmp);
            });
        }
    ],function(error,result){
        if(!result){
            result = '';
        }
        var templates_data = new Object();
        templates_data['title'] = 'Qeeniao Admin';
        templates_data['result'] = result;
 
        res.render('admin/index',templates_data);
    });
};
```


参考文章:http://yijiebuyi.com/blog/be234394cd350de16479c583f6f6bcb6.html


