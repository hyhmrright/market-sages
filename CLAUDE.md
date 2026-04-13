# Market Sages

## 项目性质

这是一个**纯 prompt 工程项目**，无代码构建步骤，无测试套件，无依赖包。
核心产物是 `skill.md`（Claude Code skill）、`AGENTS.md`（Codex CLI）和 `GEMINI.md`（Gemini CLI）。

## 安装命令

```bash
# 安装到 Claude Code
cp skill.md ~/.claude/skills/market-sages.md

# 验证安装
# 在 Claude Code 中输入 /sages AAPL
```

## 项目结构

```
skill.md        # 核心文件 — 13 位投资大师的 prompt 框架（唯一需要维护的核心内容）
AGENTS.md       # Codex CLI 集成版本
GEMINI.md       # Gemini CLI 集成版本
docs/usage/     # 各平台使用指南
docs/i18n/      # 多语言 README（zh-CN, ja, ko）
examples/       # 示例分析输出（nvidia, apple）
```

## 开发规范

- **改动 skill.md**：修改任何 sage 框架后，验证 signal rules 逻辑在所有 sage 间保持一致
- **添加新 sage**：按现有格式，包含 Philosophy、评估维度、Signal rules、声音风格四部分
- **i18n 文档**：`docs/i18n/` 下的翻译需与 `README.md` 同步更新
- **examples/**：示例输出文件仅作展示，不需要与 skill.md 保持实时同步

## 注意事项

- 这不是软件项目，`git commit` 前无需运行测试或构建
- `skill.md` 顶部的 YAML frontmatter（name/version/author/tags）用于 Claude plugin registry，修改格式会导致发布失败
- `CONTRIBUTING.md` 中定义了新 sage 的 issue label（`new-analyst`），添加 sage 前先开 issue
