---
title: "切换PHP版本的脚本"
date: "2025-07-17 09:42:49"
slug: "qie-huan-php-ban-ben-de-jiao-ben"
categories: ["技术"]
tags: ["Linux", "PHP"]
aliases:
  - "/2025/07/17/切换PHP版本的脚本/"
  - "/2025/07/17/切换PHP版本的脚本.html"
  - "/切换PHP版本的脚本/"
  - "/切换PHP版本的脚本.html"
  - "/2025/07/17/qie-huan-php-ban-ben-de-jiao-ben/"
  - "/2025/07/17/qie-huan-php-ban-ben-de-jiao-ben.html"
  - "/qie-huan-php-ban-ben-de-jiao-ben.html"
---
# 思路
本地安装多个PHP版本，默认的不同版本对应不同的路径

```bash
/usr/bin/php7.1
/usr/bin/php7.2
/usr/bin/php7.3
/usr/bin/php8.3
/usr/bin/php8.4
```

默认的PHP路径
```bash
/usr/bin/php -> /etc/alternatives/php -> /usr/bin/php7.1
```

于是想要切换PHP版本其实只要更改`/etc/alternatives/php`的指向即可

脚本记录如下

```bash
#!/bin/bash

# PHP版本切换脚本
# 该脚本通过修改/etc/alternatives/php软链接来切换PHP版本

# 定义PHP版本路径
PHP71_PATH="/usr/bin/php7.1"
PHP72_PATH="/usr/bin/php7.2"
PHP73_PATH="/usr/bin/php7.3"
PHP83_PATH="/usr/bin/php8.3"
PHP84_PATH="/usr/bin/php8.4"
ALTERNATIVES_PATH="/etc/alternatives/php"

# 检查是否以root权限运行
if [ "$(id -u)" -ne 0 ]; then
    echo "错误：此脚本需要以root权限运行，请使用sudo或切换到root用户。" >&2
    exit 1
fi

# 检查PHP可执行文件是否存在
check_php_exists() {
    if [ ! -f "$1" ]; then
        echo "错误：PHP可执行文件 $1 不存在。" >&2
        return 1
    fi
    return 0
}

# 切换PHP版本
switch_php_version() {
    local target_path=$1
    local version_name=$2
    
    # 检查目标文件是否存在
    if ! check_php_exists "$target_path"; then
        return 1
    fi
    
    # 移除现有软链接
    if [ -L "$ALTERNATIVES_PATH" ]; then
        rm -f "$ALTERNATIVES_PATH"
    elif [ -e "$ALTERNATIVES_PATH" ]; then
        echo "错误：$ALTERNATIVES_PATH 不是一个软链接。" >&2
        return 1
    fi
    
    # 创建新的软链接
    ln -s "$target_path" "$ALTERNATIVES_PATH"
    
    # 验证切换结果
    if [ $? -eq 0 ]; then
        echo "成功切换到PHP $version_name"
        echo "当前PHP版本："
        $ALTERNATIVES_PATH -v | head -n 1
        return 0
    else
        echo "切换PHP版本失败" >&2
        return 1
    fi
}

# 显示当前版本
show_current_version() {
    echo "当前PHP版本："
    if [ -L "$ALTERNATIVES_PATH" ]; then
        readlink "$ALTERNATIVES_PATH"
        $ALTERNATIVES_PATH -v | head -n 1
    else
        echo "未设置有效的PHP版本链接"
    fi
}

# 显示帮助信息
show_help() {
    echo "PHP版本切换工具"
    echo "用法: $0 [选项]"
    echo "选项:"
    echo "  7.1    切换到PHP 7.1版本"
    echo "  7.2    切换到PHP 7.2版本"
    echo "  7.3    切换到PHP 7.3版本"
    echo "  8.3    切换到PHP 8.3版本"
    echo "  8.4    切换到PHP 8.4版本"
    echo "  current 显示当前PHP版本"
    echo "  help    显示此帮助信息"
}

# 根据参数执行相应操作
case "$1" in
    "7.1")
        switch_php_version "$PHP71_PATH" "7.1"
        ;;
    "7.2")
        switch_php_version "$PHP72_PATH" "7.2"
        ;;
    "7.3")
        switch_php_version "$PHP73_PATH" "7.3"
        ;;
    "8.3")
        switch_php_version "$PHP83_PATH" "8.3"
        ;; 
    "8.4")
        switch_php_version "$PHP84_PATH" "8.4"
        ;;
    "current")
        show_current_version
        ;;
    "help")
        show_help
        ;;
    *)
        echo "无效的选项。请使用 '$0 help' 查看可用选项。" >&2
        exit 1
        ;;
esac

exit 0
```

# 使用说明：

- 将脚本保存为switch_php_version.sh
- 赋予执行权限：chmod +x switch_php_version.sh
- 使用方法：
  - 切换到 PHP 7.1：sudo ./switch_php_version.sh 7.1
  - 切换到 PHP 8.4：sudo ./switch_php_version.sh 8.4
  - 查看当前版本：./switch_php_version.sh current
  - 查看帮助：./switch_php_version.sh help

# 脚本特点：

- 需要 root 权限运行（因为要修改系统目录下的软链接）
- 会检查目标 PHP 版本文件是否存在
- 切换后会显示当前 PHP 版本信息进行验证
- 处理了软链接不存在或不是链接的异常情况
