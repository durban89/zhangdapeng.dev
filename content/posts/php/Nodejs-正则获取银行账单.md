---
title: "Nodejs 正则获取银行账单"
date: "2025-06-30 14:31:06"
slug: "nodejs-zheng-ze-huo-qu-yin-hang-zhang-dan"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-正则获取银行账单/"
  - "/2025/06/30/Nodejs-正则获取银行账单.html"
  - "/Nodejs-正则获取银行账单/"
  - "/Nodejs-正则获取银行账单.html"
  - "/2025/06/30/nodejs-zheng-ze-huo-qu-yin-hang-zhang-dan/"
  - "/2025/06/30/nodejs-zheng-ze-huo-qu-yin-hang-zhang-dan.html"
  - "/nodejs-zheng-ze-huo-qu-yin-hang-zhang-dan.html"
---
Nodejs正则获取银行账单的消费记录，其实就这么简单：

```js
'use strict';
var _ = require('lodash');
var moment = require('moment');
module.exports.execute = function (str) {
  /**
   * 清理数组
   * @param  {[type]} arr   [description]
   * @param  {[type]} value [description]
   * @return {[type]}       [description]
   */
  var clean = function(arr,value) {  
    for (var i = 0; i < arr.length; i++) {  
      if (arr[i] == value) {           
        arr.splice(i, 1);//返回指定的元素  
        i--;  
      }  
    }  
    return arr;  
  };  

  var result = {};
  var parts = str.match(/<tbody>(.+?)<\/tbody>/g);

  parts = parts.map(function (p) {
    var t =  p.replace(/ /g,'')//去掉全部中文字符间的空格
              .replace(/<[^>]*>/g, ' ')//去掉全部html标签
              .replace(/&nbsp;/g,' ')//将&nbsp;替换为一个空格
              .replace(/ +/g, ' ');//将多个空格替换为一个空格
    return t.split(' ').length > 13 ? t : '';
  });

  
  parts = clean(parts,'');
  var parts1 = parts[3].split(' ');
  parts1 = parts1.slice(13,parts.length - 1);
  var records1 = _.chunk(parts1,7);

  var parts2 = parts[4].split(' ');
  parts2 = parts2.slice(13,parts2.length - 1);
  var records2 = _.chunk(parts2,7);
  
  result.records = [];
  _.forEach([records1,records2], function (t) {
    _.forEach(t,function(r){
      var record = new Record();

      record.rtime = moment([r[1], '00:00:00'].join(' '), 'YYYY/MM/DD HH:mm:ss').unix();
      record.money = r[4];
      record.content = r[2].replace(/&nbsp;/g,'');
      result.records.push(record);
    })
  });

  return result;
};
```

推荐使用mocha进行测试一下。


