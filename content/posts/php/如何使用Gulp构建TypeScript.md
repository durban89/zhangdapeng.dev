---
title: "如何使用Gulp构建TypeScript"
date: "2025-07-08 15:16:23"
slug: "ru-he-shi-yong-gulp-gou-jian-typescript"
categories: ["技术"]
tags: ["Gulp", "TypeScript"]
aliases:
  - "/2025/07/08/如何使用Gulp构建TypeScript/"
  - "/2025/07/08/如何使用Gulp构建TypeScript.html"
  - "/如何使用Gulp构建TypeScript/"
  - "/如何使用Gulp构建TypeScript.html"
  - "/2025/07/08/ru-he-shi-yong-gulp-gou-jian-typescript/"
  - "/2025/07/08/ru-he-shi-yong-gulp-gou-jian-typescript.html"
  - "/ru-he-shi-yong-gulp-gou-jian-typescript.html"
---
**1、创建目录**  
选择一个你认为适合开发项目的目录，然后参考下面创建项目目录

```bash
mkdir typescript_demo && ce typescript_demo
```

**2、npm初始化项目**  
进入的项目目录后，执行

```bash
npm init -y
```

**3、安装依赖库**

```bash
npm install gulp-cli gulp typescript gulp-typescript --save-dev
```

gulp-typescript是TypeScript的一个Gulp插件。

**4、配置项目**

***4.1、在项目目录下面创建目录src和dist***  
src目录用来存储原始的文件也即是这里的.ts文件，dist用来存放编辑后的文件。  
在src目录下添加main.ts文件，内容如下

```ts
function hello(compiler: string) {
    console.log(`Hello from ${compiler}`);
}
hello("TypeScript");
```

***4.2、在项目目录下新建一个tsconfig.json文件，配置内容如下***

```json
{
    "files": [
        "src/main.ts"
    ],
    "compilerOptions": {
        "noImplicitAny": true,
        "target": "es5"
    }
}
```

4.3、在项目目录下新建一个gulpfile.js文件，配置内容如下

```js
const gulp = require("gulp");
const ts = require("gulp-typescript");
const tsProject = ts.createProject("tsconfig.json");

gulp.task("default", function () {
  return tsProject.src()
    .pipe(tsProject())
    .js.pipe(gulp.dest("dist"));
});
```

***4.4、试试gulp是否起作用，执行如下***

```bash
npx gulp
```

得到类似如下的输出

```bash
[13:29:14] Using gulpfile ~/nodejs/typescript_demo/gulpfile.js
[13:29:14] Starting 'default'...
[13:29:15] Finished 'default' after 1.52 s
```

查看下dist目录下是否生成了一个main.js文件  
执行如下命令 确保代码运行正常

```bash
node dist/main.js
```

执行后输出类似如下结果

```bash
Hello from TypeScript
```

***4.5、配置package.json***  
修改package.json中main对一个的值，如下

```json
"main": "./dist/mian.js",
```

如果有其他想要的修改的话，可以继续修改其他符合自己需求的项

**5、模块添加**  
创建文件src/greet.ts文件，内容如下

```ts
export function sayHello(name: string) {
    return `Hello from ${name}`;
}
```

然后在src/main.ts代码中调用，修改后结果如下

```ts
import { sayHello } from './greet';

console.log(sayHello("TypeScript"));
```

最后，将src/greet.ts添加到tsconfig.json，结果如下

```json
{
    "files": [
        "src/main.ts",
        "src/greet.ts"
    ],
    "compilerOptions": {
        "noImplicitAny": true,
        "target": "es5"
    }
}
```

通过gulp编译代码

```bash
npx gulp
```

得到类似如下的输出

```bash
[13:38:59] Using gulpfile ~/nodejs/typescript_demo/gulpfile.js
[13:38:59] Starting 'default'...
[13:39:01] Finished 'default' after 1.6 s
```

执行如下命令 确保代码运行正常

```bash
node dist/main.js
```

执行后输出类似如下结果

```bash
Hello from TypeScript
```

**6、Browserify**

注意，即使我们使用了ES2015的模块语法，TypeScript还是会生成Node.js使用的CommonJS模块。 我们在这个教程里会一直使用CommonJS模块，但是你可以通过修改 module选项来改变这个行为。

现在，让我们把这个工程由Node.js环境移到浏览器环境里。 因此，我们将把所有模块捆绑成一个JavaScript文件。 所幸，这正是Browserify要做的事情。 更方便的是，它支持Node.js的CommonJS模块，这也正是TypeScript默认生成的类型。 也就是说TypeScript和Node.js的设置不需要改变就可以移植到浏览器里。

首先，安装Browserify，tsify和vinyl-source-stream。 tsify是Browserify的一个插件，就像gulp-typescript一样，它能够访问TypeScript编译器。 vinyl-source-stream会将Browserify的输出文件适配成gulp能够解析的格式，它叫做 vinyl。  
安装命令如下

```bash
npm install browserify tsify vinyl-source-stream --save-dev
```

**6.1、在src目录下新建一个index.html文件，内容如下：**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Hello World!</title>
    </head>
    <body>
        <p id="greeting">Loading ...</p>
        <script src="bundle.js"></script>
    </body>
</html>
```

**6.2、修改main.ts文件，修改后内容如下**

```ts
import { sayHello } from "./greet";

function showHello(idName: string, name: string) {
    const elt = document.getElementById(idName);
    elt.innerText = sayHello(name);
}

showHello("greeting", "TypeScript");
```

调用sayHello函数更改页面上段落的文字  
**6.3、配置gulpfile.js，修改后内容如下**

```js
const gulp = require("gulp");
const browserify = require("browserify");
const source = require('vinyl-source-stream');
const tsify = require("tsify");
const paths = {
  pages: ['src/*.html']
};

gulp.task("copy-html", function () {
  return gulp.src(paths.pages)
    .pipe(gulp.dest("dist"));
})

gulp.task("browserify", function() {
  return browserify({
      basedir: '.',
      debug: true,
      entries: ['src/main.ts'],
      cache: {},
      packageCache: {}
    })
    .plugin(tsify)
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(gulp.dest("dist"));
})

gulp.task("default", gulp.series('copy-html', 'browserify'));
```

这里的gulp配置可能与以往的不同，需要稍加注意下，这里使用的是[xx@xx](/cdn-cgi/l/email-protection)这个版本  
这里增加了copy-html任务并且把它加作default的依赖项。 这样，当 default执行时，copy-html会被首先执行。 我们还修改了 default任务，让它使用tsify插件调用Browserify，而不是gulp-typescript。 方便的是，两者传递相同的参数对象到TypeScript编译器。

调用bundle后，我们使用source（vinyl-source-stream的别名）输出文件命名为bundle.js。

测试此页面，运行npx gulp，然后在浏览器里打开dist/index.html。 你应该能在页面上看到“Hello from TypeScript”。

注意，我们为Broswerify指定了debug: true。 这会让 tsify在输出文件里生成source maps。 source maps允许我们在浏览器中直接调试TypeScript源码，而不是在合并后的JavaScript文件上调试。 你要打开调试器并在 main.ts里打一个断点，看看source maps是否能工作。 当你刷新页面时，代码会停在断点处，从而你就能够调试 greet.ts。

**7、Watchify、Babel和Uglify**  
现在代码已经用Browserify和tsify捆绑在一起了，还可以使用Browserify插件为构建添加一些新的特性。

> Watchify启动Gulp并保持运行状态，当你保存文件时自动编译。 帮你进入到编辑-保存-刷新浏览器的循环中。

> Babel是个十分灵活的编译器，将ES2015及以上版本的代码转换成ES5和ES3。 你可以添加大量自定义的TypeScript目前不支持的转换器。

> Uglify帮你压缩代码，将花费更少的时间去下载它们。

***7.1、Watchify***  
启动Watchify，让它在后台帮我们编译：

```javascript
npm install watchify gulp-util --save-dev
```

修改gulpfile.js文件，修改后内容如下：

```js
const gulp = require("gulp");
const browserify = require("browserify");
const source = require('vinyl-source-stream');
const tsify = require("tsify");
const watchify = require("watchify");
const gutil = require("gulp-util");
const paths = {
  pages: ['src/*.html']
};

const watchedBrowserify = watchify(browserify({
  basedir: '.',
  debug: true,
  entries: ['src/main.ts'],
  cache: {},
  packageCache: {}
}).plugin(tsify));

gulp.task("copy-html", function () {
  return gulp.src(paths.pages)
    .pipe(gulp.dest("dist"));
})

function browserifyBundle() {
  return watchedBrowserify
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(gulp.dest("dist"));
}

gulp.task("browserify", function() {
  return browserifyBundle();
})

gulp.task("default", gulp.series('copy-html', 'browserify'));
watchedBrowserify.on("update", browserifyBundle);
watchedBrowserify.on("log", gutil.log);
```

共有三处改变，但是需要你略微重构一下代码。

1. 将browserify实例包裹在watchify的调用里，控制生成的结果。
2. 调用watchedBrowserify.on("update", bundle)每次TypeScript文件改变时Browserify会执行bundle函数。
3. 调用watchedBrowserify.on("log", gutil.log);将日志打印到控制台。

(1)和(2)在一起意味着我们要将browserify调用移出default任务。 然后给函数起个名字，因为Watchify和Gulp都要调用它。 (3)是可选的，但是对于调试来讲很有用。

现在当你执行gulp，它会启动并保持运行状态。 试着改变 main.ts文件里showHello的代码并保存。 你会看到这样的输出：

***7.2、Uglify***  
首先安装Uglify。 因为Uglify是用于混淆你的代码，所以我们还要安装vinyl-buffer和gulp-sourcemaps来支持sourcemaps。

```bash
npm install gulp-uglify vinyl-buffer gulp-sourcemaps --save-dev
```

修改gulpfile.js文件，修改后内容如下

```js
const gulp = require("gulp");
const browserify = require("browserify");
const source = require('vinyl-source-stream');
const tsify = require("tsify");
const watchify = require("watchify");
const gutil = require("gulp-util");
const uglify = require('gulp-uglify');
const sourcemaps = require('gulp-sourcemaps');
const buffer = require('vinyl-buffer');
const paths = {
  pages: ['src/*.html']
};

const watchedBrowserify = watchify(browserify({
  basedir: '.',
  debug: true,
  entries: ['src/main.ts'],
  cache: {},
  packageCache: {}
}).plugin(tsify));

gulp.task("copy-html", function () {
  return gulp.src(paths.pages)
    .pipe(gulp.dest("dist"));
})

function browserifyBundle() {
  return watchedBrowserify
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({
      loadMaps: true
    }))
    .pipe(uglify())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest("dist"));
}

gulp.task("browserify", function() {
  return browserifyBundle();
})

gulp.task("default", gulp.series('copy-html', 'browserify'));
watchedBrowserify.on("update", browserifyBundle);
watchedBrowserify.on("log", gutil.log);
```

注意uglify只是调用了自己。buffer和sourcemaps的调用是用于确保sourcemaps可以工作。 这些调用让我们可以使用单独的sourcemap文件，而不是之前的内嵌的sourcemaps。 你现在可以执行 gulp来检查bundle.js是否被压缩了：

***7.3、Babel***  
首先安装Babelify和ES2015的Babel预置程序。 和Uglify一样，Babelify也会混淆代码，因此我们也需要vinyl-buffer和gulp-sourcemaps。 默认情况下Babelify只会处理扩展名为 .js，.es，.es6和.jsx的文件，因此我们需要添加.ts扩展名到Babelify选项。

```bash
npm install babelify babel-core babel-preset-env vinyl-buffer gulp-sourcemaps --save-dev
```

修改gulpfile.js文件，修改后内容如下：

```js
const gulp = require("gulp");
const browserify = require("browserify");
const source = require('vinyl-source-stream');
const tsify = require("tsify");
const watchify = require("watchify");
const gutil = require("gulp-util");
const uglify = require('gulp-uglify');
const sourcemaps = require('gulp-sourcemaps');
const buffer = require('vinyl-buffer');
const paths = {
  pages: ['src/*.html']
};

const watchedBrowserify = watchify(browserify({
  basedir: '.',
  debug: true,
  entries: ['src/main.ts'],
  cache: {},
  packageCache: {}
}).plugin(tsify));

gulp.task("copy-html", function () {
  return gulp.src(paths.pages)
    .pipe(gulp.dest("dist"));
})

function browserifyBundle() {
  return watchedBrowserify
    .transform('babelify', {
      presets: ['env'],
      extensions: ['.ts']
    })
    .bundle()
    .pipe(source('bundle.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({
      loadMaps: true
    }))
    .pipe(uglify())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest("dist"));
}

gulp.task("browserify", function () {
  return browserifyBundle();
})

gulp.task("default", gulp.series('copy-html', 'browserify'));
watchedBrowserify.on("update", browserifyBundle);
watchedBrowserify.on("log", gutil.log);
```

我们需要设置TypeScript目标为ES2015。 Babel稍后会从TypeScript生成的ES2015代码中生成ES5。 修改 tsconfig.json:

```json
{
    "files": [
        "src/*.ts"
    ],
    "compilerOptions": {
        "noImplicitAny": true,
        "target": "es2015"
    }
}
```

对于这样一段简单的代码来说，Babel的ES5输出应该和TypeScript的输出相似。

实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.2
```
