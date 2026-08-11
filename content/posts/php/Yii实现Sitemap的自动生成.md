---
title: "Yii实现Sitemap的自动生成"
date: "2025-06-24 14:46:07"
slug: "yii-shi-xian-sitemap-de-zi-dong-sheng-cheng"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/24/Yii实现Sitemap的自动生成/"
  - "/2025/06/24/Yii实现Sitemap的自动生成.html"
  - "/Yii实现Sitemap的自动生成/"
  - "/Yii实现Sitemap的自动生成.html"
  - "/2025/06/24/yii-shi-xian-sitemap-de-zi-dong-sheng-cheng/"
  - "/2025/06/24/yii-shi-xian-sitemap-de-zi-dong-sheng-cheng.html"
  - "/yii-shi-xian-sitemap-de-zi-dong-sheng-cheng.html"
---
我根据自己博客的性质，进行了自己网站的Sitemap的开发。实现过程比较简单，效果还是比较令我满意的。关键是格式比较重要，还有在生成的过程中，有个在查看的时候，能够有个比较好的ui效果的设置。下面把我的Sitemap的生成代码记录如下：

```php
<?php
class Sitemap extends CController{
    protected $webSiteTitle = '';
    protected $changefreq = '';
    protected $content = '';
    protected $priority = '';
    protected $blogItems = array();
    protected $tagItems = array();
    protected $categoryItems = array();
    protected $items = array();
    /**
     * 添加基本信息
     * @param string $title
     * @param string $link
     * @param string $description
     */
    public function __construct() {
       	$this->webSiteTitle = 'http://'.$_SERVER['SERVER_NAME'];
       	$this->changefreq = 'daily';//always hourly daily weekly monthly yearly never
       	$this->priority = 0.5;
   	}

    /**
     * 分类
     */
    private function categorySitemap(){
        $criteria = new CDbCriteria();
        $criteria->condition = 'category=:category';
        $criteria->params = array(':category'=>'blog');
        $criteria->order = 'create_date DESC';
        $result = Type::model()->findAll($criteria);

        foreach($result as $k=>$v){
            $this->categoryItems[] = array(
                'url'=>$this->webSiteTitle.'/category/'.urlencode($v->name),
                'date'=>date(DATE_W3C, strtotime($v->update_date))
            );
        }
    }

    /**
     * 文章
     */
    private function blogSitemap(){
        $criteria = new CDbCriteria();
        $criteria->condition = 'is_lock=0 and is_delete=0';
        $criteria->select = 'id, tag, update_date';
        $criteria->order = 'create_date DESC';
        $model = Blog::model()->findAll($criteria);
        foreach($model as $k=>$v){
            $this->blogItems[] = array(
                'url'=>$this->webSiteTitle.'/blog/'.$v->id,
                'date'=>date(DATE_W3C, strtotime($v->update_date))
            );

            $tagArr = preg_split('#,|，#i', $v->tag);

            if(!empty($tagArr)){
                foreach($tagArr as $k=>$v){
                    if(!in_array($v,$this->tagItems)){
                        $this->tagItems[] = $v;
                    }
                }
            }
        }

        //创建临时函数数组
        $tmp = array();
        $tmp = $this->tagItems;
        $this->tagItems = array();
        foreach($tmp as $k=>$v){
            $this->tagItems[] = array(
                'url'=>$this->webSiteTitle.'/tag/'.urlencode($v),
                'date'=>date(DATE_W3C, time())
            );
        }
        unset($tmp);
    }


    /**
     * 构建xml元素
     */
     public function buildSitemap() {
        $blogitem = '';
        foreach($this->blogItems as $k=>$v){
            $blogitem .= <<<BLOG
            <url>\r\n
                <loc>{$v['url']}</loc>\r\n
                <lastmod>{$v['date']}</lastmod>\r\n
                <changefreq>{$this->changefreq}</changefreq>\r\n
                <priority>{$this->priority}</priority>\r\n
            </url>\r\n
BLOG;

        }

        $categoryitem = '';
        foreach($this->categoryItems as $k=>$v){
            $categoryitem .= <<<BLOG
            <url>\r\n
                <loc>{$v['url']}</loc>\r\n
                <lastmod>{$v['date']}</lastmod>\r\n
                <changefreq>{$this->changefreq}</changefreq>\r\n
                <priority>{$this->priority}</priority>\r\n
            </url>\r\n
BLOG;

        }
        $tagitem = '';
        foreach($this->tagItems as $k=>$v){
            $tagitem .= <<<BLOG
            <url>\r\n
                <loc>{$v['url']}</loc>\r\n
                <lastmod>{$v['date']}</lastmod>\r\n
                <changefreq>{$this->changefreq}</changefreq>\r\n
                <priority>{$this->priority}</priority>\r\n
            </url>\r\n
BLOG;

        }


        $this->content = <<<SITEMAP
<?xml version='1.0' encoding='UTF-8'?>\r\n
<?xml-stylesheet type="text/xsl" href="{$this->webSiteTitle}/sitemap.xsl"?>
<!-- generator="GoWhich/1.0" -->
<!-- sitemap-generator-url="{$this->webSiteTitle}" sitemap-generator-version="1.0.0" -->
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"\r\n
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\r\n
            {$blogitem}
            {$categoryitem}
            {$tagitem}
</urlset>\r\n
SITEMAP;
   	}

	/**
	 * 输出sitemap内容
	 */
	function show() {
        $this->blogSitemap();
        $this->categorySitemap();
    	if (empty($this->content)) {
    		$this->buildSitemap();
    	}
       	return $this->content;
	}


	/**
	 * 将rss保存为文件
	 * @param String $fname
	 * @return boolean
	 */
   	function saveToFile($fname) {
       	$handle = fopen($fname, 'wb');
       	if ($handle === false){
       		return false;
       	}
       	fwrite($handle, $this->content);
       	fclose($handle);
   	}

   	/**
   	 * 获取文件的内容
   	 * @param String $fname
   	 * @return boolean
   	 */
   	function getFile($fname) {
       	$handle = fopen($fname, 'r');
       	if ($handle === false){
       		return false;
       	}
    	while(!feof($handle)){
            echo fgets($handle);
    	}
       	fclose($handle);
   	}
}
?>
```

Controller中我建立了两个action

```php
/**
 * sitemap列表
 */
public function actionSitemap(){

    //rss创建
    $obj = new Sitemap();

    $this->render('sitemap',array('rss'=>$obj->show()));
}

public function actionSitemapXsl(){
    $this->render('sitemapxsl');
}
```

View的两个文件的代码如下

sitemap.php

```php
<?php
/* @var $this FeedController */
header("Content-Type: text/xml; charset=utf-8");
echo $rss;
exit;
?>
```

sitemapxsl.php

```xml
<?php
header("Content-Type: text/xml; charset=utf-8");
?>
<?php
$xml = <<<XML
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>XML Sitemap</title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
                body {
                    font-family:"Lucida Grande","Lucida Sans Unicode",Tahoma,Verdana;
                    font-size:13px;
                }

                #intro {
                    background-color:#CFEBF7;
                    border:1px #2580B2 solid;
                    padding:5px 13px 5px 13px;
                    margin:10px;
                }

                #intro p {
                    line-height:	16.8667px;
                }

                td {
                    font-size:11px;
                }

                th {
                    text-align:left;
                    padding-right:30px;
                    font-size:11px;
                }

                tr.high {
                    background-color:whitesmoke;
                }

                #footer {
                    padding:2px;
                    margin:10px;
                    font-size:8pt;
                    color:gray;
                }

                #footer a {
                    color:gray;
                }

                a {
                    color:black;
                }
            </style>
        </head>
        <body>
        <h1>XML Sitemap</h1>
        <div id="intro">
            <p>
                This is a XML Sitemap which is supposed to be processed by search engines like <a href="http://www.google.com">Google</a>, <a href="http://search.msn.com">MSN Search</a> and <a href="http://www.yahoo.com">YAHOO</a>.<br />
                It was generated using the Blogging-Software <a href="http://gowhich.com/">GoWhich</a> and the <a href="http://www.gowhich.com/sitemap.xml" title="Google Sitemap Generator Plugin for GoWhich">Google Sitemap Generator Plugin</a> by <a href="http://www.gowhich.com/">GoWhich</a>.<br />
                You can find more information about XML sitemaps on <a href="http://sitemaps.org">sitemaps.org</a> and Google's <a href="http://code.google.com/sm_thirdparty.html">list of sitemap programs</a>.
            </p>
        </div>
        <div id="content">
            <table cellpadding="5">
                <tr style="border-bottom:1px black solid;">
                    <th>URL</th>
                    <th>Priority</th>
                    <th>Change Frequency</th>
                    <th>LastChange (GMT)</th>
                </tr>
                <xsl:variable name="lower" select="'abcdefghijklmnopqrstuvwxyz'"/>
                <xsl:variable name="upper" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'"/>
                <xsl:for-each select="sitemap:urlset/sitemap:url">
                    <tr>
                        <xsl:if test="position() mod 2 != 1">
                            <xsl:attribute  name="class">high</xsl:attribute>
                        </xsl:if>
                        <td>
                            <xsl:variable name="itemURL">
                                <xsl:value-of select="sitemap:loc"/>
                            </xsl:variable>
                            <a href="{\$itemURL}">
                                <xsl:value-of select="sitemap:loc"/>
                            </a>
                        </td>
                        <td>
                            <xsl:value-of select="concat(sitemap:priority*100,'%')"/>
                        </td>
                        <td>
                            <xsl:value-of select="concat(translate(substring(sitemap:changefreq, 1, 1),concat(\$lower, \$upper),concat(\$upper, \$lower)),substring(sitemap:changefreq, 2))"/>
                        </td>
                        <td>
                            <xsl:value-of select="concat(substring(sitemap:lastmod,0,11),concat(' ', substring(sitemap:lastmod,12,5)))"/>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>
        </div>
        <div id="footer">
            Generated with <a href="http://www.gowhich.com/sitemap.xml" title="Google Sitemap Generator Plugin for GoWhich">Google Sitemap Generator Plugin for GoWhich</a> by <a href="http://www.gowhich.com/">GoWhich</a>. This XSLT template is released under GPL.
        </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
XML;
echo $xml;
exit;
?>
```

为了使得url看起来好看一点。

我做了一下路由设置

```php
'sitemap.xsl'=>'site/sitemapxsl',
'sitemap.xml'=>'site/sitemap',
```

