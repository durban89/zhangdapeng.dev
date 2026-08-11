#!/usr/bin/env python3
"""
Hexo 到 Hugo 自动化迁移脚本（终极防报错版）
修复：截断超长路径，彻底解决 Hugo build 报 'File name too long' 的问题
"""

import os
import re
import sys
from datetime import datetime

# 尝试导入拼音库
try:
    from pypinyin import Style, pinyin
except ImportError:
    print("❌ 错误: 未检测到 pypinyin 库！请务必先运行: pip install pypinyin")
    sys.exit(1)


def generate_chinese_slug(text: str) -> str:
    """将包含中文/英文/数字混合的字符串转为标准的拼音 URL Slug"""
    if not text:
        return ""

    text = str(text).strip()
    text = re.sub(
        r"[，。！？：；（）《》【】“”‘’、—…—]", " ", text
    )
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s_-]", "", text)

    if not text.strip():
        return ""

    py_list = pinyin(text, style=Style.NORMAL)
    slug_parts = []
    for item in py_list:
        word = item[0].strip().lower()
        if word:
            slug_parts.append(word)

    raw_slug = "-".join(slug_parts)
    clean_slug = re.sub(r"[\s_—-]+", "-", raw_slug)
    clean_slug = clean_slug.strip("-")

    return clean_slug


def sanitize_title_for_url(title: str) -> str:
    """清理中文标题中的多余空格，生成旧 URL 结构"""
    title = str(title).strip()
    clean_title = re.sub(r"[\s_—-]+", "-", title)
    return clean_title.strip("-")


def parse_yaml_front_matter(content: str) -> tuple[dict, str]:
    """Front Matter 解析器，容忍复杂的 Hexo 格式"""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    front_matter_str = match.group(1)
    body = match.group(2)

    data = {}
    current_key = None

    for line in front_matter_str.splitlines():
        line_raw = line.rstrip()
        line_str = line_raw.strip()

        if not line_str or line_str.startswith("#"):
            continue

        key_match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line_raw)
        if key_match:
            k = key_match.group(1).lower()
            v = key_match.group(2).strip()
            v_cleaned = re.sub(r"^['\"](.*)['\"]$", r"\1", v)

            current_key = k
            if v_cleaned:
                data[k] = v_cleaned
            else:
                data[k] = []
        elif current_key and (
            line_str.startswith("- ") or line_str.startswith("* ")
        ):
            item_val = line_str[2:].strip(" '\"")
            if isinstance(data.get(current_key), list):
                data[current_key].append(item_val)

    return data, body


def parse_list_item(val) -> list:
    """解析 Hexo 中各种形式的 Tags 或 Categories"""
    if not val:
        return []
    if isinstance(val, list):
        res = []
        for item in val:
            if isinstance(item, list):
                res.extend([str(x).strip() for x in item if x])
            elif item:
                res.append(str(item).strip())
        return list(dict.fromkeys(res))
    elif isinstance(val, str):
        cleaned = val.strip("[]'\" ").split(",")
        res = [x.strip(" '\"") for x in cleaned if x.strip(" '\"")]
        return list(dict.fromkeys(res))
    return []


def process_markdown_file(file_path: str, output_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    data, body = parse_yaml_front_matter(content)
    filename = os.path.basename(file_path).replace(".md", "")

    # 1. 提取标题
    title = data.get("title", "")
    if isinstance(title, list):
        title = " ".join(title)
    title = str(title).strip()
    display_title = title if title else filename

    # 2. 生成拼音 Slug
    slug = ""
    if data.get("slug"):
        slug = generate_chinese_slug(str(data.get("slug")))

    if not slug and title:
        slug = generate_chinese_slug(title)

    if not slug:
        clean_filename = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", filename)
        slug = generate_chinese_slug(clean_filename)

    if not slug:
        slug = f"article-{filename}"

    # 3. 解析日期
    date_str = str(data.get("date", "")).strip()
    parsed_date = None

    date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if date_match:
        parsed_date = date_match.groups()
    else:
        file_date_match = re.search(r"^(\d{4})-(\d{2})-(\d{2})", filename)
        if file_date_match:
            parsed_date = file_date_match.groups()
        else:
            now = datetime.now()
            parsed_date = (
                f"{now.year}",
                f"{now.month:02d}",
                f"{now.day:02d}",
            )

    year, month, day = parsed_date

    # 4. 提取与标准化 Tags / Categories
    tags = parse_list_item(data.get("tags"))
    categories = parse_list_item(data.get("categories"))

    # 5. 生成安全的 Aliases 重定向路径（严格防文件路径超长）
    aliases = []

    def safe_add_alias(path_str: str):
        clean_path = (
            str(path_str).replace("\\", "\\\\").replace('"', '\\"').strip()
        )
        # 截断路径防止 Linux/macOS 文件名触发 255 字节上限 (File name too long)
        if len(clean_path) > 100:
            if clean_path.endswith(".html"):
                clean_path = clean_path[:95] + ".html"
            elif clean_path.endswith("/"):
                clean_path = clean_path[:99] + "/"
            else:
                clean_path = clean_path[:100]

        if clean_path and clean_path not in aliases:
            aliases.append(clean_path)

    raw_cn_title = sanitize_title_for_url(display_title)
    if raw_cn_title:
        safe_add_alias(f"/{year}/{month}/{day}/{raw_cn_title}/")
        safe_add_alias(f"/{year}/{month}/{day}/{raw_cn_title}.html")
        safe_add_alias(f"/{raw_cn_title}/")
        safe_add_alias(f"/{raw_cn_title}.html")

    if filename != display_title:
        clean_fn = sanitize_title_for_url(filename)
        safe_add_alias(f"/{year}/{month}/{day}/{clean_fn}/")
        safe_add_alias(f"/{year}/{month}/{day}/{clean_fn}.html")

    # 拼音 Slug 路径
    safe_add_alias(f"/{year}/{month}/{day}/{slug}/")
    safe_add_alias(f"/{year}/{month}/{day}/{slug}.html")
    safe_add_alias(f"/{slug}.html")

    # --- 拼装 Hugo 规范的 YAML Front Matter ---
    hugo_front_matter = ["---"]

    clean_display_title = (
        display_title.replace("\\", "\\\\").replace('"', '\\"')
    )
    hugo_front_matter.append(f'title: "{clean_display_title}"')

    raw_date_full = date_str if date_str else f"{year}-{month}-{day}"
    hugo_front_matter.append(f'date: "{raw_date_full}"')
    hugo_front_matter.append(f'slug: "{slug}"')

    clean_categories = [
        c.replace("\\", "\\\\").replace('"', '\\"') for c in categories
    ]
    categories_str = ", ".join([f'"{c}"' for c in clean_categories])
    hugo_front_matter.append(f"categories: [{categories_str}]")

    clean_tags = [t.replace("\\", "\\\\").replace('"', '\\"') for t in tags]
    tags_str = ", ".join([f'"{t}"' for t in clean_tags])
    hugo_front_matter.append(f"tags: [{tags_str}]")

    hugo_front_matter.append("aliases:")
    for alias in aliases:
        hugo_front_matter.append(f'  - "{alias}"')

    hugo_front_matter.append("---\n")

    new_content = "\n".join(hugo_front_matter) + body

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ [成功] 文章: '{display_title[:15]}...' -> slug: '{slug}'")


def main():
    if len(sys.argv) < 3:
        print(
            "用法: python3 fix_hexo_to_hugo_final.py <Hexo源码路径>"
            " <Hugo目标路径>"
        )
        sys.exit(1)

    src_dir = sys.argv[1]
    dist_dir = sys.argv[2]

    if not os.path.exists(src_dir):
        print(f"❌ 错误: 源码路径 '{src_dir}' 不存在。")
        sys.exit(1)

    count = 0
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, src_dir)
                output_path = os.path.join(dist_dir, rel_path)

                process_markdown_file(file_path, output_path)
                count += 1

    print(
        f"\n🎉 迁移完成！共处理 {count} 篇文章，已修复超长路径引起的 File name too"
        " long 错误。"
    )


if __name__ == "__main__":
    main()