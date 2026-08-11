---
title: "知识点鸡肋 - /bin/bash^M: bad interpreter: No such file or directory"
date: "2025-07-15 09:51:13"
slug: "zhi-shi-dian-ji-lei-binbashm-bad-interpreter-no-such-file-or-directory"
categories: ["技术"]
tags: ["Bash"]
aliases:
  - "/2025/07/15/知识点鸡肋-/bin/bash^M:-bad-interpreter:-No-such-file-or-directory/"
  - "/2025/07/15/知识点鸡肋-/bin/bash^M:-bad-interpreter:-No-such-file-or-directory.html"
  - "/知识点鸡肋-/bin/bash^M:-bad-interpreter:-No-such-file-or-directory/"
  - "/知识点鸡肋-/bin/bash^M:-bad-interpreter:-No-such-file-or-directory.html"
  - "/2025/07/15/知识点鸡肋-bin-bash-bad-interpreter-No-such-file-or-directory/"
  - "/2025/07/15/知识点鸡肋-bin-bash-bad-interpreter-No-such-file-or-directory.html"
  - "/2025/07/15/zhi-shi-dian-ji-lei-binbashm-bad-interpreter-no-such-file-or-directory/"
  - "/2025/07/15/zhi-shi-dian-ji-lei-binbashm-bad-interpreter-no-such-file-or-directory.html"
  - "/zhi-shi-dian-ji-lei-binbashm-bad-interpreter-no-such-file-or-directory.html"
---
知识点鸡肋 - /bin/bash^M: bad interpreter: No such file or directory

执行一个脚本start.sh 时, 一直是提示我:

```bash
-bash: ./start.sh: /bin/bash^M: bad interpreter: No such file or directory
```

出现上面错误的原因:

脚本文件是DOS格式的, 即每一行的行尾以\r\n来标识, 使用vim编辑器打开脚本, 运行:

```bash
:set ff?
```

可以看到DOS或UNIX的字样. 使用`set ff=unix` 或 `set fileformat=unix`把它强制为unix格式的, 然后存盘(`:wq`)退出, 即可。
