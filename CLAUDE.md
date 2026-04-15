# Market Sages

## 项目性质

这是一个**纯 prompt 工程项目**，无代码构建步骤，无依赖包。
核心产物是 `skill.md`（Claude Code skill）、`AGENTS.md`（Codex CLI）和 `GEMINI.md`（Gemini CLI）。
测试基础设施见 `tests/`（结构校验 + prompt 评估 + CI）。

## 安装命令

```bash
# 安装到 Claude Code
cp skill.md ~/.claude/skills/market-sages.md

# 验证安装
# 在 Claude Code 中输入 /sages AAPL
```

## 项目结构

```
skill.md                          # 唯一 source of truth（所有平台共用此文件）
skills/market-sages/SKILL.md     # 符号链接 → skill.md（plugin 系统要求此路径）
tests/
  validate_structure.py           # 结构校验（零依赖）
  run_evals.py                    # prompt 评估（PEP 723 内联依赖）
  utils.py                        # 共用 frontmatter 解析器
  fixtures/                       # 7 个 YAML 测试用例
AGENTS.md                         # Codex CLI 集成版本（格式规范 + 调用示例）
GEMINI.md                         # Gemini CLI 集成版本（格式规范 + 调用示例）
.claude-plugin/                   # Claude Code plugin marketplace 元数据
.codex-plugin/                    # Codex CLI 技能安装器元数据
gemini-extension.json             # Gemini CLI /extensions install 清单
commands/sages.md                 # /sages 斜杠命令包装器
docs/usage/                       # 各平台使用指南
docs/i18n/                        # 多语言 README（zh-CN, ja, ko）
examples/                         # 示例分析输出（nvidia, apple）
```

## 开发规范

- **改动 skill.md**：只需修改 `skill.md`，`skills/market-sages/SKILL.md` 是符号链接，自动同步
- **添加新 sage**：按现有格式，包含 Philosophy、评估维度、Signal rules、声音风格四部分；**不需要**同步更新 AGENTS.md / GEMINI.md 中的量化阈值（已移除）
- **i18n 文档**：`docs/i18n/` 下的翻译需与 `README.md` 同步更新
- **examples/**：示例输出文件仅作展示，不需要与 skill.md 保持实时同步

## 测试

```bash
# 结构校验（零依赖，任何时候都可运行）
uv run tests/validate_structure.py

# Prompt 评估（需要 ANTHROPIC_API_KEY）
export ANTHROPIC_API_KEY=sk-...
uv run tests/run_evals.py              # 全部 fixture
uv run tests/run_evals.py nvda_full_data  # 单个 fixture
uv run tests/run_evals.py --dry-run   # 不调用 API，仅打印提示词
```

CI 在每次修改 `skill.md` 时自动运行结构校验（`.github/workflows/validate.yml`）。

## 注意事项

- `git commit` 前至少运行一次 `uv run tests/validate_structure.py`
- `skill.md` 顶部的 YAML frontmatter（name/version/author/tags）用于 Claude plugin registry，修改格式会导致发布失败
- `skills/market-sages/SKILL.md` 是指向 `../../skill.md` 的符号链接，**不要直接编辑**
- `CONTRIBUTING.md` 中定义了新 sage 的 issue label（`new-analyst`），添加 sage 前先开 issue
- 发版流程：同步更新以下所有文件的 `version` 字段，再打 tag：
  `skill.md` · `.claude-plugin/plugin.json` · `.claude-plugin/marketplace.json` · `.codex-plugin/plugin.json` · `gemini-extension.json`
- `tests/utils.py` 是两个测试脚本共用的 frontmatter 解析器，勿删
