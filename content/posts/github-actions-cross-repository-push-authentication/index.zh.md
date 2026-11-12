+++
title = "解决 GitHub Actions 跨仓库 Git Push 认证失败：Fine-grained PAT 与 SSH 配置指南"
slug = "github-actions-cross-repository-push-authentication"
date = 2026-11-12T09:41:00+08:00
lastmod = 2026-11-12T09:41:00+08:00
draft = false
description = "解决 GitHub Actions 使用 GITHUB_TOKEN 向其他仓库推送代码时出现的认证失败问题，详细介绍 Fine-grained Personal Access Token、GitHub Secrets 和 SSH Deploy Keys 的配置与安全实践。"
summary = "当 GitHub Actions 需要将自动抓取或生成的内容同步到另一个 GitHub 仓库时，默认 GITHUB_TOKEN 可能因仓库权限隔离而无法完成 git push。本文介绍问题排查、Fine-grained PAT、GitHub Secrets 和 SSH Deploy Keys 的完整配置方法。"
tags = ["GitHub Actions", "GitHub", "CI/CD", "Git", "DevOps", "Security"]
categories = ["Development"]
image = "cover.png"
image_alt = "GitHub Actions cross-repository synchronization authentication using Personal Access Tokens and SSH keys"
toc = true
+++

## 一、问题背景

在使用 GitHub Actions 实现自动化任务时，我们经常会遇到这样的需求：

- 定时抓取第三方网站的数据。
- 自动生成 Markdown 文件。
- 将生成的内容同步到个人博客仓库。
- 自动提交并推送代码，触发后续的部署流程。

例如，我有两个 GitHub 仓库：

| 仓库 | 用途 |
|---|---|
| Scraper Repository | 存放数据抓取程序和 GitHub Workflow |
| zhangdapeng.dev | 存放 Hugo 博客源码和文章 |

其中，Scraper Repository 每天定时运行抓取程序，将生成的 Markdown 文件同步到博客仓库的 `content/6-minute-english` 目录。

整个流程可以简化为：

```text
GitHub Actions
      |
      v
运行 Scraper
      |
      v
生成 Markdown 文件
      |
      v
Git Sync
      |
      v
git add / git commit
      |
      v
git push origin main
      |
      v
zhangdapeng.dev
```

最初使用 GitHub Actions 默认提供的 `GITHUB_TOKEN` 进行认证，但在执行推送操作时出现了以下错误。

```text
it push origin main failed (128):
fatal: could not read Password for
'https://***@github.com': No such device or address

ELIFECYCLE Command failed with exit code 1.
Error: Process completed with exit code 1.
```

这个问题表面上看起来是 Git 无法读取 HTTPS 密码，实际上需要从 GitHub Actions 的认证机制入手排查。

## 二、问题原因：GITHUB_TOKEN 的仓库权限限制

首先需要明确一个容易被忽略的事实：

**GitHub Actions 自动生成的 GITHUB_TOKEN 默认只具有当前 Workflow 所属仓库的访问权限，不会因为其他仓库属于同一个 GitHub 账号，就自动获得跨仓库写入权限。**

例如：

```text
GitHub Account: durban89

Repository A:
scraper-project

Repository B:
zhangdapeng.dev
```

假设 Workflow 运行在 Repository A 中：

```yaml
GIT_SYNC_REPO: "https://github.com/durban89/zhangdapeng.dev.git"
GIT_SYNC_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

这里的 `GITHUB_TOKEN` 是 GitHub 为当前 Workflow 运行实例生成的临时访问凭证。

它的权限受到当前仓库的 Actions 权限设置以及 Workflow 的 `permissions` 声明约束。

即使 Repository A 和 Repository B 都属于 `durban89`，也不代表 Repository A 生成的 `GITHUB_TOKEN` 可以直接向 Repository B 推送代码。

### 2.1 为什么同一个账号也不行？

这是 GitHub 的安全隔离机制。

GitHub 不会默认允许一个仓库中的自动化任务访问账号下的所有其他仓库。

否则，如果某个公开仓库中的 Workflow 被恶意修改，攻击者就可能利用自动化任务访问账号下的其他项目。

因此，GitHub 将 Workflow Token 的权限限制在特定仓库范围内。

### 2.2 如何判断是否是认证问题？

除了仓库权限不足，还需要检查以下情况：

1. Token 是否为空或者没有正确传入环境变量。
2. Token 是否已经过期或被撤销。
3. Token 是否拥有目标仓库的 Contents 写入权限。
4. Git 同步脚本是否正确处理了 HTTPS 认证地址。
5. 目标分支是否受到 Branch Protection Rules 限制。

特别注意：

```text
fatal: could not read Password
```

这个错误并不能单独证明是跨仓库权限不足。

它也可能意味着 Git 无法获取有效凭证，并尝试交互式询问密码，而 GitHub Actions 的运行环境没有可用的交互终端。

因此，应结合 Workflow 日志和 Token 配置一起判断。

## 三、解决方案一：使用 Fine-grained Personal Access Token

对于需要向其他仓库推送代码的场景，最直接的解决方案是创建一个 Fine-grained Personal Access Token（细粒度个人访问令牌）。

与传统的 Personal Access Token 相比，Fine-grained PAT 可以将访问权限限制在指定仓库，并且可以精确控制 Repository permissions。

### 3.1 创建 Fine-grained PAT

首先登录 GitHub，进入个人账号设置：

https://github.com/settings/personal-access-tokens

然后按照以下步骤操作：

1. 进入 Fine-grained tokens。
2. 点击 Generate new token。
3. 配置 Token 的基本信息。

推荐配置：

| 配置项 | 推荐值 |
|---|---|
| Token name | 6-Min-English-Sync |
| Expiration | 根据实际需求设置 |
| Resource owner | durban89 |
| Repository access | Only select repositories |
| Selected repositories | zhangdapeng.dev |

接下来配置 Repository permissions。

找到：

```text
Repository permissions
    └── Contents
          └── Read and write
```

将 Contents 设置为 `Read and write`。

这是执行以下 Git 操作所需要的主要权限：

```bash
git add .
git commit -m "Update content"
git push origin main
```

配置完成后，点击 Generate token。

**注意：生成的 Token 只会完整显示一次，请及时复制并安全保存。**

### 3.2 将 PAT 添加到 GitHub Secrets

不要将 Token 直接写入 Workflow YAML 文件。

正确的做法是将 Token 保存到运行 Workflow 的仓库中的 GitHub Secrets。

进入运行抓取程序的仓库：

```text
Repository
    └── Settings
          └── Secrets and variables
                └── Actions
```

点击 New repository secret。

推荐配置：

```text
Name:
SYNC_TOKEN

Secret:
刚刚生成的 Fine-grained PAT
```

保存之后，Workflow 就可以通过以下表达式读取该 Secret：

```yaml
${{ secrets.SYNC_TOKEN }}
```

### 3.3 修改 GitHub Workflow

将原来的：

```yaml
GIT_SYNC_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

修改为：

```yaml
GIT_SYNC_TOKEN: ${{ secrets.SYNC_TOKEN }}
```

完整的同步步骤如下：

```yaml
- name: Run Scraper and Sync
  run: pnpm start
  env:
    GIT_SYNC_ENABLED: "true"
    GIT_SYNC_REPO: "https://github.com/durban89/zhangdapeng.dev.git"
    GIT_SYNC_BRANCH: "main"
    GIT_SYNC_CONTENT_DIR: "content/6-minute-english"
    GIT_SYNC_TOKEN: ${{ secrets.SYNC_TOKEN }}
    GIT_SYNC_COMMIT_NAME: "durban89"
    GIT_SYNC_COMMIT_EMAIL: "zhangdapeng89@126.com"
```

这样，底层同步程序就可以使用具有目标仓库写入权限的 PAT 完成 Git 推送。

## 四、解决方案二：使用 SSH Deploy Keys

除了 PAT，还可以使用 SSH 密钥完成跨仓库认证。

这种方式不需要在 Git 命令中使用 Personal Access Token，而是通过 SSH 公私钥验证身份。

如果你的同步程序支持 SSH URL，这也是一种可行的方案。

### 4.1 生成 SSH 密钥

在本地终端执行：

```bash
ssh-keygen -t ed25519 \
  -C "zhangdapeng89@126.com" \
  -f ./id_github_deploy
```

生成两个文件：

```text
id_github_deploy
id_github_deploy.pub
```

其中：

| 文件 | 用途 |
|---|---|
| id_github_deploy | 私钥，需要保密 |
| id_github_deploy.pub | 公钥，可以公开 |

### 4.2 在目标仓库配置 Deploy Key

打开目标仓库：

```text
zhangdapeng.dev
    └── Settings
          └── Deploy keys
```

点击 Add deploy key。

填写：

```text
Title:
Scraper Sync Key

Key:
粘贴 id_github_deploy.pub 的完整内容
```

然后勾选：

```text
Allow write access
```

最后保存。

这里需要特别注意：

默认情况下，Deploy Key 只有读取权限。如果需要执行 `git push`，必须启用 Allow write access。

### 4.3 将 SSH 私钥添加到 GitHub Secrets

回到运行 Workflow 的抓取仓库：

```text
Settings
    └── Secrets and variables
          └── Actions
```

创建新的 Secret：

```text
Name:
SSH_PRIVATE_KEY

Value:
粘贴 id_github_deploy 私钥的完整内容
```

不要将私钥提交到 Git 仓库。

### 4.4 修改 GitHub Workflow

在执行同步程序之前，使用 `webfactory/ssh-agent` 将 SSH 私钥加载到运行环境。

```yaml
- name: Setup SSH Keys
  uses: webfactory/ssh-agent@v0.9.0
  with:
    ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}

- name: Run Scraper and Sync
  run: pnpm start
  env:
    GIT_SYNC_ENABLED: "true"
    GIT_SYNC_REPO: "git@github.com:durban89/zhangdapeng.dev.git"
    GIT_SYNC_BRANCH: "main"
    GIT_SYNC_CONTENT_DIR: "content/6-minute-english"
    GIT_SYNC_COMMIT_NAME: "durban89"
    GIT_SYNC_COMMIT_EMAIL: "zhangdapeng89@126.com"
```

这里有一个重要的前提：

**你的同步程序必须支持 SSH URL，并且不能强制要求通过 HTTPS Token 拼接认证地址。**

如果程序内部存在类似下面的逻辑：

```javascript
const remoteUrl = `https://${token}@github.com/${repo}.git`;
```

那么即使配置了 SSH Agent，也无法直接使用 SSH 推送。

需要修改同步程序，让它能够根据仓库地址使用相应的认证方式。

如果程序强制校验 `GIT_SYNC_TOKEN`，也需要同步调整这部分逻辑，而不是随意传入一个占位字符串。

## 五、GitHub Secrets：公开仓库如何安全保存 Token？

在解决上述问题的过程中，还有一个非常重要的问题：

**如果运行 GitHub Actions 的仓库是公开仓库，那么把 Token 配置到 Workflow 中是否存在安全风险？**

答案是：取决于你如何配置。

### 5.1 不要将明文 Token 写入 YAML

错误示例：

```yaml
env:
  GIT_SYNC_TOKEN: "ghp_xxxxxxxxxxxxxxxxx"
```

或者：

```yaml
env:
  GIT_SYNC_TOKEN: "github_pat_xxxxxxxxx"
```

如果将明文 Token 提交到公开仓库，任何人都可以查看。

即使之后删除了这段代码，Git 历史记录中仍可能保留原来的 Token。

一旦泄露，其他人就可能利用它访问 Token 所授权的仓库。

因此，如果已经提交过真实 Token，应立即撤销该 Token，并检查是否存在其他未授权操作。

### 5.2 正确使用 GitHub Secrets

推荐方式：

```yaml
env:
  GIT_SYNC_TOKEN: ${{ secrets.SYNC_TOKEN }}
```

Token 的真实内容保存在 GitHub 的后台 Secret 存储中。

公开仓库中展示的只是变量引用：

```yaml
${{ secrets.SYNC_TOKEN }}
```

其他用户无法通过查看公开仓库的 YAML 文件获取 Secret 的实际内容。

GitHub 还会尝试对日志中的 Secret 值进行脱敏处理。

不过，需要注意：

**Secrets 并不是绝对安全的。**

如果你在 Workflow 中运行不可信的第三方代码，并主动将 Secret 传递给该代码，那么代码仍然可能通过网络请求等方式泄露凭证。

因此还需要遵循以下原则：

- 只授予 Token 完成任务所需要的最小权限。
- 为 PAT 设置合理的过期时间。
- 不要在日志中打印 Token。
- 不要将 Secret 写入构建产物或提交到 Git。
- 谨慎使用来自不可信 Pull Request 的代码。
- 定期检查和撤销不再使用的 Token。

尤其对于公开仓库，应该注意 `pull_request_target` 等可能在高权限上下文中执行不可信代码的 Workflow 事件。

## 六、另一种方案：GitHub App

如果不希望长期维护个人访问令牌，还可以考虑 GitHub App。

GitHub App 可以被安装到指定仓库，并通过私钥在 Workflow 运行期间动态生成短期访问 Token。

基本流程：

```text
创建 GitHub App
       |
       v
配置 Repository Permissions
       |
       v
安装到目标仓库
       |
       v
保存 App ID 和 Private Key
       |
       v
GitHub Actions 动态生成 Token
       |
       v
执行 Git Push
```

主要配置：

1. 在 GitHub Developer Settings 中创建 GitHub App。
2. 配置 Repository permissions。
3. 将 Contents 设置为 Read and write。
4. 将 App 安装到目标仓库。
5. 生成 App Private Key。
6. 将 App ID 和 Private Key 保存到 Workflow 所属仓库的 Secrets。

然后使用官方 Action：

```yaml
- name: Generate GitHub App Token
  id: generate_token
  uses: actions/create-github-app-token@v1
  with:
    app-id: ${{ secrets.SYNC_APP_ID }}
    private-key: ${{ secrets.SYNC_APP_PRIVATE_KEY }}
    owner: durban89
    repositories: zhangdapeng.dev
```

在同步步骤中：

```yaml
GIT_SYNC_TOKEN: ${{ steps.generate_token.outputs.token }}
```

这样可以避免使用长期有效的 PAT。

GitHub App 安装令牌通常最长有效期为 1 小时，并且权限受 App 安装授权范围限制。

对于有多个自动化项目、需要跨仓库访问控制的场景，这种方式更适合长期维护。

## 七、几种认证方式对比

将上面介绍的几种方式进行比较：

| 认证方式 | 跨仓库写入 | 凭证管理 | 配置复杂度 |
|---|---|---|---|
| 默认 GITHUB_TOKEN | 默认不支持 | GitHub 自动管理 | 低 |
| Fine-grained PAT | 支持 | GitHub Secrets | 低 |
| SSH Deploy Key | 支持 | GitHub Secrets | 中 |
| GitHub App Token | 支持 | App Private Key + 动态 Token | 高 |

这里需要补充一个例外：

如果 Workflow 只需要访问当前仓库，可以通过 `permissions` 显式授予写入权限，例如：

```yaml
permissions:
  contents: write
```

这样就可以让当前仓库的 `GITHUB_TOKEN` 执行写入操作。

但是，这并不会自动赋予它访问其他仓库的权限。

## 八、最终推荐方案

对于本文介绍的自动抓取与博客同步场景，我更推荐使用 Fine-grained PAT。

原因很简单：

1. 不需要修改现有同步程序的认证逻辑。
2. 可以精确限制 Token 只能访问 `zhangdapeng.dev`。
3. 只需要 Contents: Read and write 权限。
4. 可以直接通过 GitHub Secrets 管理凭证。
5. 配置简单，后续维护成本较低。

如果未来有多个自动化项目需要访问不同仓库，再考虑迁移到 GitHub App。

最终建议的 Workflow 结构如下：

```yaml
name: Auto Scrape 6 Minute English

on:
  schedule:
    # 每天北京时间 09:30 执行
    # 对应 UTC 时间 01:30
    - cron: '30 1 * * *'

  workflow_dispatch:

jobs:
  scrape_and_sync:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install pnpm
        uses: pnpm/action-setup@v3
        with:
          version: 8

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install
        env:
          PNPM_ONLY_BUILT_DEPENDENCIES: ""

      - name: Run Scraper and Sync
        run: pnpm start
        env:
          GIT_SYNC_ENABLED: "true"
          GIT_SYNC_REPO: "https://github.com/durban89/zhangdapeng.dev.git"
          GIT_SYNC_BRANCH: "main"
          GIT_SYNC_CONTENT_DIR: "content/6-minute-english"
          GIT_SYNC_TOKEN: ${{ secrets.SYNC_TOKEN }}
          GIT_SYNC_COMMIT_NAME: "durban89"
          GIT_SYNC_COMMIT_EMAIL: "zhangdapeng89@126.com"
```

注意：上面的 Workflow 假设底层同步程序已经正确支持 PAT 认证，并且目标分支允许该身份推送。

## 九、总结

GitHub Actions 的跨仓库自动同步，本质上是一个权限管理和身份认证问题，而不只是 Git 命令的问题。

排查类似问题时，可以按照以下顺序：

1. 确认当前 Workflow 运行在哪个仓库。
2. 确认目标仓库是否与当前仓库相同。
3. 检查 `GITHUB_TOKEN` 的权限范围。
4. 检查 Token 是否具备目标仓库的 Contents 写入权限。
5. 检查 Git 同步程序是否正确处理认证信息。
6. 使用 GitHub Secrets 安全保存凭证。
7. 重新运行 Workflow 验证推送结果。

对于个人开发者来说，GitHub Actions、GitHub Secrets 和 Fine-grained PAT 已经可以覆盖大多数跨仓库自动化同步需求。

不需要为了一个简单的自动同步任务引入过于复杂的认证架构，但也不能为了方便而牺牲凭证安全性。

**始终遵循最小权限原则（Principle of Least Privilege），让自动化任务只拥有完成工作所必需的访问权限。**