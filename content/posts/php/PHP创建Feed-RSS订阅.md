---
title: "PHP创建Feed/RSS订阅"
date: "2025-06-10 11:23:00"
slug: "php-chuang-jian-feedrss-ding-yue"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/10/PHP创建Feed/RSS订阅/"
  - "/2025/06/10/PHP创建Feed/RSS订阅.html"
  - "/PHP创建Feed/RSS订阅/"
  - "/PHP创建Feed/RSS订阅.html"
  - "/2025/06/10/PHP创建Feed-RSS订阅/"
  - "/2025/06/10/PHP创建Feed-RSS订阅.html"
  - "/2025/06/10/php-chuang-jian-feedrss-ding-yue/"
  - "/2025/06/10/php-chuang-jian-feedrss-ding-yue.html"
  - "/php-chuang-jian-feedrss-ding-yue.html"
---
好多都是第三方的，自己闲麻烦，自己就整理了一套自己一个rss类，对需要的朋友给个帮助吧，也方便了自己，呵呵

直接贴代码：

```php
<?php
class Rss extends CController
{
    //public
    public $rss_ver = "2.0";
    public $channel_title = '';
    public $channel_link = '';
    public $channel_description = '';
    public $language = 'zh_CN';
    public $copyright = '';
    public $webMaster = '';
    public $pubDate = '';
    public $lastBuildDate = '';
    public $generator = 'GoWhich RSS Generator';
    public $content = '';
    public $items = [];

    /**
     * 添加基本信息
     * @param string $title
     * @param string $link
     * @param string $description
     */
    public function __construct($title, $link, $description)
    {
        $this->channel_title = $title;
        $this->channel_link = $link;
        $this->channel_description = $description;
        $this->pubDate = Date('Y-m-d H:i:s', time());
        $this->lastBuildDate = Date('Y-m-d H:i:s', time());
    }

    /**
     * 添加一个节点
     * @param string $title
     * @param string $link
     * @param string $description
     * @param date $pubDate
     */
    public function addItem($title, $link, $description, $pubDate)
    {
        $this->items[] = ['title' => $title,
            'link' => $link,
            'descrīption' => $description,
            'pubDate' => $pubDate];
    }

    /**
     * 构建xml元素
     */
    public function buildRSS()
    {
        $s = <<<RSS
<?xml version='1.0' encoding='utf-8'?>\n
<rss version="2.0">\n
RSS;

        // start channel
        $s .= "<channel>\n";
        $s .= "<title><![CDATA[{$this->channel_title}]]></title>\n";
        $s .= "<link><![CDATA[{$this->channel_link}]]></link>\n";
        $s .= "<descrīption><![CDATA[{$this->channel_description}]]></descrīption>\n";
        $s .= "<language>{$this->language}</language>\n";
        if (!empty($this->copyright)) {
            $s .= "<copyright><![CDATA[{$this->copyright}]]></copyright>\n";
        }
        if (!empty($this->webMaster)) {
            $s .= "<webMaster><![CDATA[{$this->webMaster}]]></webMaster>\n";
        }
        if (!empty($this->pubDate)) {
            $s .= "<pubDate>{$this->pubDate}</pubDate>\n";
        }
        if (!empty($this->lastBuildDate)) {
            $s .= "<lastBuildDate>{$this->lastBuildDate}</lastBuildDate>\n";
        }
        if (!empty($this->generator)) {
            $s .= "<generator>{$this->generator}</generator>\n";
        }
        // start items
        for ($i = 0; $i < count($this->items); $i++) {
            $s .= "<item>\n";
            $s .= "<title><![CDATA[{$this->items[$i]['title']}]]></title>\n";
            $s .= "<link><![CDATA[{$this->items[$i]['link']}]]></link>\n";
            $s .= "<descrīption><![CDATA[{$this->items[$i]['descrīption']}]]></descrīption>\n";
            $s .= "<pubDate>{$this->items[$i]['pubDate']}</pubDate>\n";
            $s .= "</item>\n";
        }
        // close channel
        $s .= "</channel>\n</rss>";
        $this->content = $s;
    }

    /**
     * 输出rss内容
     */
    public function show()
    {
        if (empty($this->content)) {
            $this->buildRSS();
        }
        return $this->content;
    }

    /**
     * 设置版权
     * @param unknown $copyright
     */
    public function setCopyRight($copyright)
    {
        $this->copyright = $copyright;
    }

    /**
     * 设置管理员
     * @param unknown $master
     */
    public function setWebMaster($master)
    {
        $this->webMaster = $master;
    }

    /**
     * 设置发布时间
     * @param date $date
     */
    public function setpubDate($date)
    {
        $this->pubDate = $date;
    }

    /**
     * 设置建立时间
     * @param unknown $date
     */
    public function setLastBuildDate($date)
    {
        $this->lastBuildDate = $date;
    }

    /**
     * 将rss保存为文件
     * @param String $fname
     * @return boolean
     */
    public function saveToFile($fname)
    {
        $handle = fopen($fname, 'wb');
        if (false === $handle) {
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
    public function getFile($fname)
    {
        $handle = fopen($fname, 'r');
        if (false === $handle) {
            return false;
        }
        while (!feof($handle)) {
            echo fgets($handle);
        }
        fclose($handle);
    }
}
```

如果还是不都清楚可以到github上自己下载好了

github地址：https://github.com/zhangda89/php-library/blob/master/Rss.php
