---
title: "Nodejs 实现 通过 POP3 协议获取邮件列表【yapople】"
date: "2025-06-30 14:30:58"
slug: "nodejs-shi-xian-tong-guo-pop3-xie-yi-huo-qu-you-jian-lie-biao-yapople"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-实现-通过-POP3-协议获取邮件列表【yapople】/"
  - "/2025/06/30/Nodejs-实现-通过-POP3-协议获取邮件列表【yapople】.html"
  - "/Nodejs-实现-通过-POP3-协议获取邮件列表【yapople】/"
  - "/Nodejs-实现-通过-POP3-协议获取邮件列表【yapople】.html"
  - "/2025/06/30/Nodejs-实现-通过-POP3-协议获取邮件列表-yapople/"
  - "/2025/06/30/Nodejs-实现-通过-POP3-协议获取邮件列表-yapople.html"
  - "/2025/06/30/nodejs-shi-xian-tong-guo-pop3-xie-yi-huo-qu-you-jian-lie-biao-yapople/"
  - "/2025/06/30/nodejs-shi-xian-tong-guo-pop3-xie-yi-huo-qu-you-jian-lie-biao-yapople.html"
  - "/nodejs-shi-xian-tong-guo-pop3-xie-yi-huo-qu-you-jian-lie-biao-yapople.html"
---
让我们使用yapople获取一下，你的邮件列表吧

代码如下：

```js
var Client = require('yapople').Client;
var _ = require('lodash');
var async = require('async');
var iconv = require('iconv-lite');

var Fetcher = module.exports = function(options){
    this.options = _.assign(options,{port:995,tls:true,mailparser:true})
    this.client = new Client(this.options)
    this.mails = []
}

Fetcher.prototype.count = function(cb){
    var self = this
    self.client.connect(function(){
        self.client.count(cb);
        self.client.quit();
    });
}

Fetcher.prototype.fetch = function(nums,cb){
    var self = this;
    self.client.connect(function(){
        self.client.retrieve(nums,function(err,messages){
            cb(err,messages);
            self.client.quit();
        })
    });
}

Fetcher.prototype.list = function(number,cb){
    var self = this;
    self.client.connect(function(){
        self.client.list(number,function(err,info){
            cb(err,info);
            self.client.quit();
        })
    });
}

Fetcher.prototype.getContent = function(date,cb){
    var self = this;
    self.client.connect(function(){
        async.waterfall([
            function(done){
                self.client.count(function(err,count){
                    done(err,count);
                });
            },
            function(count,done){
                var nums = [];
                var tmp = [];
                for(var i=0;i<count;i++){
                    nums.push(i+1);
                }

                self.client.retrieve(nums,function(err,res){
                    console.log('res length',res.length);
                    done(err,tmp);
                    // done(err,res);
                });
            }
        ],function(err,results){
            // console.log('results:',results);
            cb(err,results);
            self.client.quit();
        });
    });
}

Fetcher.prototype._connect = function(cb){
    var self = this;
    self.client.connect(function(){
        self.client.retrieve([2],function(err,messages){
            cb(err,messages);
            self.client.quit();
        })
    })
}
```

测试一下：

```js
var should = require('should');
var moment = require('moment');
var POP3 = require(__dirname + '/../lib/mail_fetcher/pop3');
var iconv = require('iconv-lite');

var conf = {
  hostname: 'pop.126.com',
  username: 'xxx@xxx.com',
  password: 'mmmmmm'
};

describe('pop3 test', function(){
  it('should get mailbox count', function(done){
    var pop3 = new POP3(conf);
    pop3.count(function(err,count){
      console.log('count:',count);
      return done();
    })
  });
  it('should fetch nums messages',function(done){
    var pop3 = new POP3(conf);
    pop3.fetch([1,2,3],function(err,messages){
      messages.forEach(function(i){
        // console.log('ALL:',i);
        console.log('SUBJECT:',i.subject);
      })
      return done();
    });
  });
  // it('should return date condition messages',function(done){
  //   var pop3 = new POP3(conf);
  //   pop3.getContent('2015-01-03',function(err,messages){
  //     console.log('MESSAGES:',messages);
  //     return done();
  //   })
  // });
  // it('pop3 list',function(done){
  //   var pop3 = new POP3(conf);
  //   pop3.list(function(err,info){
  //     // console.log('list info:',info);
  //     return done();
  //   })
  // })
});
```

password和username换成你自己的。


