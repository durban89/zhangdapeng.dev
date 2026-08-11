---
title: "Nodejs 之 Koa2 添加travis ci 持续集成工具"
date: "2025-07-03 16:50:05"
slug: "nodejs-zhi-koa2-tian-jia-travis-ci-chi-xu-ji-cheng-gong-ju"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-之-Koa2-添加travis-ci-持续集成工具/"
  - "/2025/07/03/Nodejs-之-Koa2-添加travis-ci-持续集成工具.html"
  - "/Nodejs-之-Koa2-添加travis-ci-持续集成工具/"
  - "/Nodejs-之-Koa2-添加travis-ci-持续集成工具.html"
  - "/2025/07/03/nodejs-zhi-koa2-tian-jia-travis-ci-chi-xu-ji-cheng-gong-ju/"
  - "/2025/07/03/nodejs-zhi-koa2-tian-jia-travis-ci-chi-xu-ji-cheng-gong-ju.html"
  - "/nodejs-zhi-koa2-tian-jia-travis-ci-chi-xu-ji-cheng-gong-ju.html"
---
最近使用koa2做项目测试开发，想整合下travis ci,网上资料也比较少，于是自己就整了个，做个记录。

先来看下travis.yml的配置

```yml
language: node_js
node_js:
    - "6"
before_script:
    - ./node_modules/.bin/knex migrate:latest --knexfile='./app/knexfile.js'
script:
    - npm run test
```

因为是接口测试，所以首先需要做表创建等操作。

测试的命令：

```bash
NODE_ENV=production NODE_CONFIG_DIR='./app/config/' ./node_modules/.bin/mocha --require 'babel-polyfill' --compilers js:babel-register  ./app/test/**/*.js
```

主要是测试这里，使用了supertest，大概看下是如何调用的。

```js
const request = require('supertest');
const should = require('should');
const index = require('../../index');

let app = request(index.listen());

describe('/api/persons', function() {
  let personId;

  it('POST /api/persons - create person success and respond with 200', function(done) {
    app.post('/api/persons')
      .send({
        'firstName': 'Jennifer',
        'lastName': 'Lawrence',
        'age': 24
      })
      .expect(200)
      .expect(function(res) {
        (res.body.id > 0).should.be.true;
      })
      .end(function(err, res) {
        if (err) {
          return done(err);
        }

        let resJson = JSON.parse(res.text);
        personId = resJson.id;

        done();
      })
  });

  it('GET /api/persons - fetch persons item', function(done) {
    app.get('/api/persons')
      .expect(200)
      .expect(function(res) {
        (res.body.length > 0).should.be.true;
      })
      .end(function(err, res) {
        if (err) {
          return done(err);
        }

        done();
      })
  });

  it('GET /api/persons/:id - fetch a person', function(done) {
    app.get(`/api/persons/${personId}`)
      .expect(200)
      .expect(function(res) {
        (res.body.id == personId).should.be.true;
      })
      .end(function(err, res) {
        if (err) {
          return done(err);
        }

        done();
      })
  });

  it('DELETE /api/persons/:id - delete a person', function(done) {
    app.delete(`/api/persons/${personId}`)
      .expect(200)
      .end(function(err, res) {
        if (err) {
          return done(err);
        }

        done();
      })
  });

  it('GET /api/persons/:id - fetch a person should 404', function(done) {
    app.get(`/api/persons/${personId}`)
      .expect(404)
      .end(function(err, res) {
        if (err) {
          return done(err);
        }

        done();
      })
  });

});
```

这里主要注意的是

```js
const index = require('../../index');
```

需要将koa实例暴漏出来，不然在做travis ci的集成后，启动了项目，测试的时候依然找不到具体访问地址。

来看下我的index.js

```js
import Knex from 'knex';
import {
  Model
} from 'objection';
import knexConfig from './knexfile';
import config from 'config';
import Koa from 'koa';
import koaLogger from 'koa-logger';
import bodyParser from 'koa-bodyparser';
import render from 'koa-ejs';
import co from 'co';
import koaStatic from "koa2-static"
import router from './router';

const path = require('path');

// initial knex
const knex = Knex(knexConfig.development);
Model.knex(knex);

// initial app
const app = new Koa();

// initial render
render(app, {
  root: path.join(__dirname + '/view'),
  layout: 'template',
  viewExt: 'ejs',
  cache: true,
  debug: true
});
app.context.render = co.wrap(app.context.render);

// initial static

app.use(koaLogger())
  .use(bodyParser())
  .use(router.routes())
  .use(koaStatic({
    path: '/web',
    root: __dirname + "/../static"
  }));

module.exports = app;
```

需要注意的是这里的

```js
module.exports = app;
```

暴漏出来，再supertest中才可以独立启动server测试。好的不明白的加群聊聊吧。
