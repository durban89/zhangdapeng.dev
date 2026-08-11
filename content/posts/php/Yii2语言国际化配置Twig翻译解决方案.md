---
title: "Yii2语言国际化配置Twig翻译解决方案"
date: "2025-07-08 16:02:09"
slug: "yii2-yu-yan-guo-ji-hua-pei-zhi-twig-fan-yi-jie-jue-fang-an"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/07/08/Yii2语言国际化配置Twig翻译解决方案/"
  - "/2025/07/08/Yii2语言国际化配置Twig翻译解决方案.html"
  - "/Yii2语言国际化配置Twig翻译解决方案/"
  - "/Yii2语言国际化配置Twig翻译解决方案.html"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-pei-zhi-twig-fan-yi-jie-jue-fang-an/"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-pei-zhi-twig-fan-yi-jie-jue-fang-an.html"
  - "/yii2-yu-yan-guo-ji-hua-pei-zhi-twig-fan-yi-jie-jue-fang-an.html"
---
我自己在写项目的时候，不喜欢使用php自身的模板，主要是各种PHP标签让我烦，而且对Html的标签兼容也不够友好，所以我后面采用了twig模板，配置之类的也是很方便，写起来也很顺手，但是在Yii2语言国际化翻译这块就遇到了坑，当我们指定文件类型，除了处理php扩展的之外，也处理twig扩展的文件的时候，就不会解析twig中的内容，因为不符合PHP的标签处理逻辑，在PHP中我们使用Yii::t()，但是在twig中使用的是Yii.t()这个函数在translator的配置中，显得很乏力，而且看源码也可以发现，实际上也只处理php文件，网上找了很多针对这个问题的处理方式，似乎也没有几个使用的。现在看下我是如何解决的

## 第一步 显示修改i18n配置

将twig扩展加入进去，修改后如下:

```php
return [
    'color' => null,
    'interactive' => true,
    'help' => null,
    'sourcePath' => '@app',
    'messagePath' => '@app/messages',
    'languages' => ['zh-CN', 'ru-RU'],
    'translator' => 'Yii::t', // 翻译器
    'sort' => false,
    'overwrite' => true,
    'removeUnused' => false,
    'markUnused' => true,
    'except' => [
        '.svn',
        '.git',
        '.gitignore',
        '.gitkeep',
        '.hgignore',
        '.hgkeep',
        '/messages',
        '/BaseYii.php',
        'vendor',
        'tests',
        'runtime',
        'migrations',
    ],
    'only' => [
        '*.php',
        '*.twig', // 添加模板扩展
    ],
    'format' => 'php',
    'db' => 'db',
    'sourceMessageTable' => '{&#8203;{%source_message}}',
    'messageTable' => '{&#8203;{%message}}',
    'catalog' => 'messages',
    'ignoreCategories' => [],
    'phpFileHeader' => '',
    'phpDocBlock' => null,
];
```

## 第二步 继承重写

创建文件app/commands/TranslatorController.php，内容如下

```php
<?php

namespace app\commands;

use yii\console\controllers\MessageController;
use yii\helpers\Console;

/**
 * Extracts messages to be translated from source files.
 *
 * @author durban.zhang <xx@xx>
 */
class TranslatorController extends MessageController
{
    public function init()
    {
        parent::init();
    }

    /**
     * This command echoes what you have entered as the message.
     * @param string $message the message to be echoed.
     */
    protected function extractMessages($fileName, $translator, $ignoreCategories = [])
    {
        $messages = [];

        $extInfo = pathinfo($fileName, PATHINFO_EXTENSION);

        if ('twig' == $extInfo) {
            $coloredFileName = Console::ansiFormat($fileName, [Console::FG_CYAN]);
            $this->stdout("Extracting messages from $coloredFileName...\n");
            $subject = file_get_contents($fileName);

            $preg = '/\{\{ Yii\.t\(\'(.*?)\', \'(.*?)\'\) \}\}/';

            $content = preg_replace($preg, "<?php Yii::t('$1', '$2'); ?>", $subject);

            $tokens = token_get_all($content);

            foreach ((array) $translator as $currentTranslator) {
                $translatorTokens = token_get_all('<?php ' . $currentTranslator);

                array_shift($translatorTokens);

                $messages = array_merge_recursive(
                    $messages,
                    $this->extractMessagesFromTokens(
                        $tokens,
                        $translatorTokens,
                        $ignoreCategories));
            }

            $this->stdout("\n");
        } else {
            $messages = parent::extractMessages($fileName, $translator, $ignoreCategories);
        }

        return $messages;
    }

    protected function extractMessagesFromTokens(array $tokens, array $translatorTokens, array $ignoreCategories)
    {
        $messages = [];
        $translatorTokensCount = count($translatorTokens);
        $matchedTokensCount = 0;
        $buffer = [];
        $pendingParenthesisCount = 0;foreach ($tokens as $token) {
            // finding out translator call
            if ($matchedTokensCount < $translatorTokensCount) {
                if ($this->tokensEqual($token, $translatorTokens[$matchedTokensCount])) {
                    $matchedTokensCount++;
                } else {
                    $matchedTokensCount = 0;
                }
            } elseif ($matchedTokensCount === $translatorTokensCount) {
                // translator found

                // end of function call
                if ($this->tokensEqual(')', $token)) {
                    $pendingParenthesisCount--;

                    if (0 === $pendingParenthesisCount) {
                        // end of translator call or end of something that we can't extract
                        if (isset($buffer[0][0], $buffer[1], $buffer[2][0]) && T_CONSTANT_ENCAPSED_STRING === $buffer[0][0] && ',' === $buffer[1] && T_CONSTANT_ENCAPSED_STRING === $buffer[2][0]) {
                            // is valid call we can extract
                            $category = stripcslashes($buffer[0][1]);
                            $category = mb_substr($category, 1, -1);

                            if (!$this->isCategoryIgnored($category, $ignoreCategories)) {
                                $message = stripcslashes($buffer[2][1]);
                                $message = mb_substr($message, 1, -1);

                                $messages[$category][] = $message;
                            }

                            $nestedTokens = array_slice($buffer, 3);
                            if (count($nestedTokens) > $translatorTokensCount) {
                                // search for possible nested translator calls
                                $messages = array_merge_recursive($messages, $this->extractMessagesFromTokens($nestedTokens, $translatorTokens, $ignoreCategories));
                            }
                        } else {
                            // invalid call or dynamic call we can't extract
                            $line = Console::ansiFormat($this->getLine($buffer), [Console::FG_CYAN]);
                            $skipping = Console::ansiFormat('Skipping line', [Console::FG_YELLOW]);
                            $this->stdout("$skipping $line. Make sure both category and message are static strings.\n");
                        }

                        // prepare for the next match
                        $matchedTokensCount = 0;
                        $pendingParenthesisCount = 0;
                        $buffer = [];
                    } else {
                        $buffer[] = $token;
                    }
                } elseif ($this->tokensEqual('(', $token)) {
                    // count beginning of function call, skipping translator beginning
                    if ($pendingParenthesisCount > 0) {
                        $buffer[] = $token;
                    }
                    $pendingParenthesisCount++;
                } elseif (isset($token[0]) && !in_array($token[0], [T_WHITESPACE, T_COMMENT])) {
                    // ignore comments and whitespaces
                    $buffer[] = $token;
                }
            }
        }

        return $messages;
    }
}
```

从上面的代码可以看出，实现了两个方法  
**extractMessages**和**extractMessagesFromTokens**  
本来是不需要实现extractMessagesFromTokens这个方法的，但是父类中的private，试过了实例化类，但是需要传递需要的参数，为了避免出现问题，暂时没用实例化的方式。  
最后extractMessagesFromTokens 这个只是父类的copy版本。那么重点就在extractMessages  
判断如果文件是twig文件，则进行处理，处理逻辑我写的也很简单，暂时能解决问题

```javascript
$preg = '/\{\{ Yii\.t\(\'(.*?)\', \'(.*?)\'\) \}\}/';
$content = preg_replace($preg, "<?php Yii::t('$1', '$2'); ?>", $subject);
$tokens = token_get_all($content);
```

主要是将Yii.t转为了含有PHP标签的字符串，实际上父类也只是针对代码进行字符串的过滤处理，以此类推的话，如果有其他模板的话也可以采用此方法

到这里就处理完了，

但是执行的命令不是下面这个

```bash
./yii message/extract @app/config/i18n.php
```

而是下面这个

```bash
./yii translator/extract @app/config/i18n.php
```

OK，问题解决，如您有其他方案，请指教
