import os
import re
import sys
import json
from datetime import datetime
from pypinyin import lazy_pinyin, Style

# 兼容不同 Python 版本的 TOML 解析器
try:
    import tomllib  # Python 3.11+ 标准库
except ImportError:
    try:
        import toml as tomllib  # 第三方库 pip install toml
    except ImportError:
        import tomli as tomllib  # 第三方库 pip install tomli

def text_to_pinyin_slug(text):
    """仅用于 slug：将包含中文/英文的文本转换为全拼音 Slug"""
    if not text:
        return ""

    s = str(text).strip()

    # 1. 移除中英文括号（保留内部文字）
    s = re.sub(r'[（）\(\)]', ' ', s)

    # 2. 将非字母数字汉字替换为空格
    s = re.sub(r'[^\w\s-]', ' ', s)

    # 3. 使用 pypinyin 将中文字符转拼音，英文保持原样
    pinyin_list = lazy_pinyin(s, style=Style.NORMAL)

    # 4. 拼音列表拼接
    slug = "-".join(pinyin_list)

    # 5. 清理多余的连字符并转小写
    slug = re.sub(r'[-\s]+', '-', slug).strip('-').lower()

    return slug

def clean_chinese_alias_path(raw_path):
    """
    专门用于 aliases：保留中文，仅移除中英文括号并把英文转为小写
    """
    if not raw_path:
        return ""

    path_str = str(raw_path).strip()

    # 1. 仅移除中英文括号字符（保留内部中文/文本）
    path_str = re.sub(r'[（）\(\)]', '', path_str)

    # 2. 英文转换为小写
    path_str = path_str.lower()

    # 3. 清除前后多余空格与横线
    path_str = path_str.strip(" -_")

    return path_str

def extract_date_prefix(date_val):
    """从 Front Matter 的 date 字段提取 YYYY/MM/DD 字符串"""
    if not date_val:
        return None

    if isinstance(date_val, datetime):
        return date_val.strftime("%Y/%m/%d")

    date_str = str(date_val).strip()
    match = re.match(r'^(\d{4})[-/](\d{2})[-/](\d{2})', date_str)
    if match:
        year, month, day = match.groups()
        return f"{year}/{month}/{day}"

    return None

def generate_aliases(data, src_file_path):
    """提取现有 aliases，并自动生成【保留中文】的 YYYY/MM/DD/alias 别名"""
    aliases_list = []

    # 1. 提取显式声明的复数 aliases
    if 'aliases' in data:
        val = data['aliases']
        if isinstance(val, str):
            aliases_list.append(clean_chinese_alias_path(val))
        elif isinstance(val, list):
            aliases_list.extend([clean_chinese_alias_path(item) for item in val if item])

    # 2. 提取显式声明的单数 alias
    if 'alias' in data:
        val = data['alias']
        if isinstance(val, str):
            aliases_list.append(clean_chinese_alias_path(val))
        elif isinstance(val, list):
            aliases_list.extend([clean_chinese_alias_path(item) for item in val if item])
        del data['alias']

    # 3. 获取原始 slug 或文件名，构建保留中文的 alias 路径
    raw_slug = data.get('slug')
    if not raw_slug:
        raw_slug = os.path.splitext(os.path.basename(src_file_path))[0]
    
    cleaned_chinese_slug = clean_chinese_alias_path(raw_slug)

    # 4. 自动生成 /YYYY/MM/DD/中文slug 重定向路径
    date_prefix = extract_date_prefix(data.get('date'))

    if date_prefix and cleaned_chinese_slug:
        date_alias_without_slash = f"/{date_prefix}/{cleaned_chinese_slug}"
        date_alias_with_slash = f"/{date_prefix}/{cleaned_chinese_slug}/"
        
        aliases_list.append(date_alias_without_slash)
        aliases_list.append(date_alias_with_slash)

    # 5. 过滤与去重
    cleaned_aliases = []
    for a in aliases_list:
        a_str = str(a).strip()
        if a_str and a_str not in cleaned_aliases:
            cleaned_aliases.append(a_str)

    return cleaned_aliases

def parse_front_matter(content):
    """简单正则提取 Front Matter 文本，无需 YAML/TOML 解析器依赖"""
    # 尝试匹配 TOML (+++)
    toml_match = re.match(r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)$', content, re.DOTALL)
    if toml_match:
        raw_data, body = toml_match.group(1), toml_match.group(2)
        try:
            data = tomllib.loads(raw_data)
            return data, body
        except Exception as e:
            print(f"❌ TOML 解析失败: {e}")
            return None, body

    # 尝试匹配 YAML (---)
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if yaml_match:
        raw_data, body = yaml_match.group(1), yaml_match.group(2)
        # 用正则按行提简单的 key = value
        data = {}
        for line in raw_data.splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                k, v = line.split(':', 1)
                k = k.strip().strip('"\'')
                v = v.strip().strip('"\'')
                data[k] = v
        return data, body

    return None, content

def build_yaml_front_matter(data):
    """手写拼接出最标准的 YAML 字符串 Header"""
    lines = []

    for key, value in data.items():
        if value is None:
            continue

        # 1. categories 和 tags 输出为内联格式：categories: ["技术"]
        if key in ['categories', 'tags'] and isinstance(value, list):
            formatted_json_array = json.dumps(value, ensure_ascii=False)
            lines.append(f"{key}: {formatted_json_array}")

        # 2. aliases 输出为多行带 2 个空格缩进的格式
        elif key == 'aliases' and isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f'  - "{item}"')

        # 3. 布尔类型：draft: false
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")

        # 4. 其他字符串 Value（强制使用 json.dumps 加双引号且处理好转义）
        else:
            val_str = str(value)
            escaped_val = json.dumps(val_str, ensure_ascii=False)
            lines.append(f"{key}: {escaped_val}")

    return "\n".join(lines) + "\n"

def process_markdown_file(src_file_path, dest_file_path):
    with open(src_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data, body = parse_front_matter(content)

    if not data or not isinstance(data, dict):
        print(f"⚠️  [SKIP] 无法解析 Front Matter: {src_file_path}")
        return

    # 1. 仅 slug 字段转换为全拼音
    raw_slug = data.get('slug')
    if not raw_slug:
        raw_slug = os.path.splitext(os.path.basename(src_file_path))[0]
    pinyin_slug = text_to_pinyin_slug(raw_slug)

    # 2. aliases 字段保留中文（仅去除括号、转小写）
    aliases = generate_aliases(data, src_file_path)

    # 3. 清理 categories 和 tags 中的空项
    for key in ['categories', 'tags']:
        if key in data:
            if isinstance(data[key], list):
                data[key] = [str(item).strip() for item in data[key] if str(item).strip()]
            elif isinstance(data[key], str):
                data[key] = [data[key].strip()]

    # 4. 构建字典：slug 位于 categories 正上方
    ordered_data = {}
    
    for k in ['title', 'date', 'draft', 'description', 'image']:
        if k in data:
            # 布尔值处理
            if k == 'draft':
                val = data[k]
                ordered_data[k] = False if str(val).lower() == 'false' else True
            else:
                ordered_data[k] = data[k]

    # slug 赋拼音值
    ordered_data['slug'] = pinyin_slug

    if 'categories' in data:
        ordered_data['categories'] = data['categories']
    if 'tags' in data:
        ordered_data['tags'] = data['tags']

    if aliases:
        ordered_data['aliases'] = aliases

    for k, v in data.items():
        if k not in ordered_data and k != 'alias':
            ordered_data[k] = v

    # 5. 创建目标目录并写入
    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

    yaml_header = build_yaml_front_matter(ordered_data)

    with open(dest_file_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write(yaml_header)
        f.write("---\n\n")
        f.write(body.lstrip())

    print(f"✅ [OK] 已迁移: {os.path.basename(dest_file_path)}")

def main():
    if len(sys.argv) < 3:
        print("用法: python3 migrate.py <源目录> <目标目录>")
        print("示例: python3 migrate.py ../old-blog/content/posts content/posts/python-ts")
        sys.exit(1)

    src_dir = os.path.abspath(sys.argv[1])
    dest_dir = os.path.abspath(sys.argv[2])

    if not os.path.exists(src_dir):
        print(f"❌ 找不到源路径: {src_dir}")
        sys.exit(1)

    os.makedirs(dest_dir, exist_ok=True)

    count = 0
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                src_path = os.path.join(root, file)
                
                # 源文件名保持不动
                filename = os.path.basename(file)
                dest_path = os.path.join(dest_dir, filename)

                process_markdown_file(src_path, dest_path)
                count += 1

    print(f"\n🎉 迁移完成！共处理 {count} 篇文章。")

if __name__ == '__main__':
    main()