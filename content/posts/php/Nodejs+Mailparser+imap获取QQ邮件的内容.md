---
title: "Nodejs+Mailparser+imap获取QQ邮件的内容"
date: "2025-06-30 14:09:13"
slug: "nodejsmailparserimap-huo-qu-qq-you-jian-de-nei-rong"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs+Mailparser+imap获取QQ邮件的内容/"
  - "/2025/06/30/Nodejs+Mailparser+imap获取QQ邮件的内容.html"
  - "/Nodejs+Mailparser+imap获取QQ邮件的内容/"
  - "/Nodejs+Mailparser+imap获取QQ邮件的内容.html"
  - "/2025/06/30/nodejsmailparserimap-huo-qu-qq-you-jian-de-nei-rong/"
  - "/2025/06/30/nodejsmailparserimap-huo-qu-qq-you-jian-de-nei-rong.html"
  - "/nodejsmailparserimap-huo-qu-qq-you-jian-de-nei-rong.html"
---
Nodejs 通过imap获取QQ email邮箱的内容：代码实现过程如下

```js
var UTIL = require("util");
var HTTP = require("http");
var HTTPS = require("https");
var URL = require("url");
var HTMLPARSER = require("htmlparser2");
var FORMDATA = require("form-data");
var IMAP = require('imap');
var INSPECT = require('util').inspect;
var MAILPARSER = require('mailparser').MailParser;
var fs = require('fs'), fileStream;


var imap = new IMAP({
	user:'xx@xx',
	password:'password',
	host:'imap.qq.com',
	port:'993',
	tls:true
});

function openInbox(cb){
	imap.openBox('INBOX',true,cb);
}

imap.once('ready', function() {
    openInbox(function(err, box) {
        //邮件搜索
        imap.search([ 'SEEN', ['BEFORE', '2015-05-10'] ], function(err, results) {
            console.log(results);
            if (err) throw err;
            
            var f = imap.fetch(results, { 
                bodies: '',
                struct: true
            });
            
            f.on('message', function(msg, seqno) {
                console.log('Message #%d', seqno);
                var prefix = '(#' + seqno + ') ';
                msg.on('body', function(stream, info) {
                    console.log('INFO WHICH:',info.which);
                    if (info.which === 'TEXT'){
                        console.log(prefix + 'Body [%s] found, %d total bytes', INSPECT(info.which), info.size);
                    }
                    
                    var mailparser = new MAILPARSER();
                    stream.pipe(mailparser);
                    mailparser.on("end",function( mail ){
                        fs.writeFile('msg-' + seqno + '-body.html', mail.text, function (err) {
                            if (err) throw err;
                            console.log(prefix + 'saved!');
                        });
                    });
                });
                
                msg.once('attributes', function(attrs) {
                    console.log(prefix + 'Attributes: %s', INSPECT(attrs, false, 8));
                });
                msg.once('end', function() {
                    console.log(prefix + 'Finished');
                });
            });

            f.once('error', function(err) {
                console.log('Fetch error: ' + err);
            });

            f.once('end', function() {
                console.log('Done fetching all messages!');
                imap.end();
            });
        });
    });
});
 
imap.once('error', function(err) {
  console.log(err);
});
 
imap.once('end', function() {
  console.log('Connection ended');
});
 
imap.connect();
```

执行

```bash
node app.js
```

即可在根目录下看到一个html的文件，打开就可以看到内容

这里使用的是mail.text，可以替换成mail.html就可以获取到有图文的html页面

