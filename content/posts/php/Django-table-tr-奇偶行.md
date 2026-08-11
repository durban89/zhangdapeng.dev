---
title: "Django table tr 奇偶行"
date: "2025-06-20 14:13:14"
slug: "django-table-tr-ji-ou-xing"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django-table-tr-奇偶行/"
  - "/2025/06/20/Django-table-tr-奇偶行.html"
  - "/Django-table-tr-奇偶行/"
  - "/Django-table-tr-奇偶行.html"
  - "/2025/06/20/django-table-tr-ji-ou-xing/"
  - "/2025/06/20/django-table-tr-ji-ou-xing.html"
  - "/django-table-tr-ji-ou-xing.html"
---
Method 1: The Cross-Browser CSS Way

The easiest way to do this is to make use of the built-in Django `{% raw %}{% cycle %}{% endraw %}` tag. Here’s how to use it for a table containing blog entries:

```html
<table>
<tbody>
{% for blog in blogs %}
  {% for entry in blog.entries %}
    <tr class="{% cycle 'odd' 'even' %}">
      {{entry.date}}
      {{entry.title}}
      {{entry.comments}}
    </tr>
  {% endfor %}
{% endfor %}
</tbody>
</table>
```

Method 2: The Pure CSS Way

```css
tbody tr:nth-child(even) td {background: #bbeebb;}
tbody tr:nth-child(odd) td {background: #e5f9e5;}
```

