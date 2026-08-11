---
title: "NodeJS命令行下调试运行代码初体验"
date: "2025-07-11 10:40:27"
slug: "nodejs-ming-ling-xing-xia-tiao-shi-yun-xing-dai-ma-chu-ti-yan"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/11/NodeJS命令行下调试运行代码初体验/"
  - "/2025/07/11/NodeJS命令行下调试运行代码初体验.html"
  - "/NodeJS命令行下调试运行代码初体验/"
  - "/NodeJS命令行下调试运行代码初体验.html"
  - "/2025/07/11/nodejs命令行下调试运行代码初体验/"
  - "/2025/07/11/nodejs命令行下调试运行代码初体验.html"
  - "/2025/07/11/nodejs-ming-ling-xing-xia-tiao-shi-yun-xing-dai-ma-chu-ti-yan/"
  - "/2025/07/11/nodejs-ming-ling-xing-xia-tiao-shi-yun-xing-dai-ma-chu-ti-yan.html"
  - "/nodejs-ming-ling-xing-xia-tiao-shi-yun-xing-dai-ma-chu-ti-yan.html"
---
今天发现一个我很久不知道的功能，虽然我用了很久nodejs，但是这个命令行的功能还是第一次发现，记录下

```bash
$ node -v
v10.17.0
```

简单的测试如下

```bash
$ node
> .help
.break    Sometimes you get stuck, this gets you out
.clear    Alias for .break
.editor   Enter editor mode
.exit     Exit the repl
.help     Print this help message
.load     Load JS from a file into the REPL session
.save     Save all evaluated commands in this REPL session to a file
> .editor
// Entering editor mode (^D to finish, ^C to cancel)
let a = 2
b = a
console.log(b)

2
undefined
> .editor
// Entering editor mode (^D to finish, ^C to cancel)
'use strict';
let a = 2
b = a
console.log(b)

Thrown:
SyntaxError: Identifier 'a' has already been declared
> b = a
2
> .editor
// Entering editor mode (^D to finish, ^C to cancel)
'use strict'

let m = 2
n = m
console.log(n)

Thrown:
ReferenceError: n is not defined
>
```

如果你使用v12.18.1或者更高的版本应该体验会更好一些，不知道v10.17.0 - v12.18.1之间的版本有没有区别，这个没有测试过 试下v12.18.1版本的

```bash
$ node
Welcome to Node.js v12.18.1.
Type ".help" for more information.
> process.version
'v12.18.1'
> os.type()
'Darwin'
> os.arch()
'x64'
>
(To exit, press ^C again or ^D or type .exit)
>
```

很明显的是进入命令行之后，多了

```bash
Welcome to Node.js v12.18.1.
Type ".help" for more information.
```

是不是nodejs变的很友好

```bash
$ node
Welcome to Node.js v12.18.1.
Type ".help" for more information.
> .help
.break    Sometimes you get stuck, this gets you out
.clear    Alias for .break
.editor   Enter editor mode
.exit     Exit the repl
.help     Print this help message
.load     Load JS from a file into the REPL session
.save     Save all evaluated commands in this REPL session to a file

Press ^C to abort current expression, ^D to exit the repl
> .editor
// Entering editor mode (^D to finish, ^C to cancel)
let a = 1;
let b = a;
console.log(b);

1
undefined
> .exit
```

`.load`这个命令感觉很有意思，尝试下

文件代码如下

```javascript
let hash = "83108adff87ba432cd03d15f9f82db16";
function enHash(key) {
  key = key instanceof Buffer ? key : new Buffer(key);
  var p = 16777619; // 32
  var hash = 0x811C9DC5;

  for (var i = 0; i < key.length; i++) {
    console.log(hash * p + '======' + key[i]);
    console.log((hash * p) ^ key[i]);
    hash = (hash * p) ^ key[i];
  }

  hash += hash << 13;
  hash ^= hash >> 7;
  hash += hash << 3;
  hash ^= hash >> 17;
  hash += hash << 5;

  return hash;
}

let enHashStr = enHash(hash);
console.log('enHashStr =',enHashStr);
```

启动加载下试试

```bash
$ node
Welcome to Node.js v12.18.1.
Type ".help" for more information.
> .load
Failed to load:
> .load /Users/durban/nodejs/test.js
let hash = "83108adff87ba432cd03d15f9f82db16";
function enHash(key) {
  key = key instanceof Buffer ? key : new Buffer(key);
    var p = 16777619; // 32
      var hash = 0x811C9DC5;

        for (var i = 0; i < key.length; i++) {
            console.log(hash * p + '======' + key[i]);
                console.log((hash * p) ^ key[i]);
                    hash = (hash * p) ^ key[i];
                      }

                        hash += hash << 13;
                          hash ^= hash >> 7;
                            hash += hash << 3;
                              hash ^= hash >> 17;
                                hash += hash << 5;

                                  return hash;
                                  }

                                  let enHashStr = enHash(hash);
                                  console.log('enHashStr =',enHashStr);
36342608889142560======56
84696344
1421002990324936======51
175541499
2945168388910881======49
1939861264
32546253200250416======48
348476928
5846613128274432======56
-1297718728
-21772630387548630======97
1944886857
32630570684853484======100
-964875128
-16188307280160232======102
-15918466
-267073957612454======102
-6245316
-104781532382604======56
-1510229428
-25338053945571932======55
-1757002349
-29478315993627030======98
-1231059446
-20654246351339070======97
-2027945567
-34024098075864972======52
1482854464
24878767229441216======51
1663636723
27911863092902536======50
212597434
3566878748029646======99
-1396985171
-23438084947687850======100
-1736817092
-29139655442263948======48
1149014084
19277720526985996======51
337058623
5655041157358637======100
-547363767
-9183460737130772======49
-319529251
-5360940032633369======53
-508471854
-8530947038635626======102
472521200
7927780663022800======57
1179047145
19781603781847756======102
-1971246422
-33072821423429216======56
-1286198888
-21579354901087670======50
-391939462
-6575810964500978======100
-1285960086
-21575348372115230======98
-1067454334
-17909342115750746======49
1493671063
25060244006338996======54
-1107590782
enHashStr = 389970291
undefined
> (node:37594) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.

>
>
```

有点像Python了，OMG。
