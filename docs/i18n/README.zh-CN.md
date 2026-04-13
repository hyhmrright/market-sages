# 🧙 Market Sages — 市场智者议会

> **13位传奇投资人，一条指令，零配置。**

[![许可证: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-blue?logo=anthropic)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Ready-green?logo=openai)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Ready-red?logo=google)](https://github.com/google-gemini/gemini-cli)

**Market Sages** 召唤了13位世界顶级投资人的智慧来分析任何股票——沃伦·巴菲特、查理·芒格、本杰明·格雷厄姆、迈克尔·伯里、纳西姆·塔勒布等。

无需 API Key，无需 Python 环境，无需金融数据订阅。只需一个股票代码。

---

**[🇺🇸 English](../../README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)**

---

## ✨ 它能做什么

你输入：
```
/sages NVDA
```

你得到完整的议会审议结果：

```
╔══════════════════════════════════╗
║  🧠 沃伦·巴菲特                  ║
║  信号: 中性                      ║
║  置信度: 55%                     ║
║  分析: 护城河极强（游戏生态），   ║
║  但当前 P/E 留下安全边际空间不足。║
╚══════════════════════════════════╝

╔══════════════════════════════════╗
║  🧠 迈克尔·伯里                  ║
║  信号: 看空                      ║
║  置信度: 72%                     ║
║  分析: FCF 收益率约1.8%，        ║
║  EV/EBIT 约80x——这是动量而非价值。║
╚══════════════════════════════════╝

... （11位智者的分析）

╔══════════════════════════════════════════════╗
║  🏦 投资组合经理 — 最终裁决               ║
║  行动: 观望                               ║
║  置信度: 中等                             ║
║  入场策略: 等待20-25%回调                 ║
╚══════════════════════════════════════════════╝
```

---

## 🧑‍💼 13位智者议会

| # | 智者 | 投资哲学 | 核心标准 |
|---|------|---------|---------|
| 1 | **沃伦·巴菲特** | 以合理价格买优质企业 | 护城河 + 安全边际 >25% |
| 2 | **查理·芒格** | 倒推、心智模型 | ROIC >15%，奇妙企业 |
| 3 | **本杰明·格雷厄姆** | 安全边际高于一切 | 格雷厄姆数 + 流动比率 >2 |
| 4 | **彼得·林奇** | 十倍股，投资你了解的 | PEG <1，可理解 |
| 5 | **迈克尔·伯里** | 深度价值逆向投资 | FCF 收益率 >10%，EV/EBIT <8 |
| 6 | **凯西·伍德** | 颠覆性创新 | 5年收入CAGR >15% |
| 7 | **斯坦利·德鲁肯米勒** | 不对称宏观机会 | 盈利上调 + 不对称回报 |
| 8 | **比尔·阿克曼** | 激进投资，简单企业 | FCF + 管理层催化剂 |
| 9 | **菲利普·费雪** | 尽职调查，永久持有 | 15问框架 + 管理层质量 |
| 10 | **纳西姆·塔勒布** | 反脆弱，尾部风险 | 反脆弱 + 凸性 + 切肤之痛 |
| 11 | **莫尼什·帕博莱** | 丹多（Dhandho）框架 | 先看下行 + 安全边际 >50% |
| 12 | **阿斯瓦斯·达摩达兰** | 故事+数字，DCF | 内在价值显著高于市价 |
| 13 | **拉克什·金哥万拉** | 持有，耐心 | ROCE >20%，长期信念 |

---

## 🚀 快速开始

### Claude Code（推荐）

**安装：**
```bash
# 将技能文件复制到 Claude 技能目录
cp skill.md ~/.claude/skills/market-sages.md
```

**使用：**
```
/sages 苹果
/sages TSLA --value        # 价值派智者
/sages AMZN --growth       # 成长派智者
/sages MSFT --risk         # 风险分析
/sages compare AAPL MSFT   # 对比分析
```

---

### OpenAI Codex CLI

**安装：**
```bash
cp AGENTS.md /path/to/your/project/AGENTS.md
```

**使用：**
```bash
codex "用市场智者议会分析苹果公司"
codex "用伯里和格雷厄姆评估英特尔的价值"
```

---

### Google Gemini CLI

**安装：**
```bash
cp GEMINI.md /path/to/your/project/GEMINI.md
```

**使用：**
```bash
gemini "用13位市场智者分析特斯拉"
gemini "巴菲特和芒格会怎么看宁德时代？"
```

---

### 通用方式（任何 LLM）

将 `skill.md` 的内容复制为任何 LLM 界面的**系统提示词**，即可在 ChatGPT、Claude.ai、Gemini 或任何自定义应用中使用。

---

## 💡 进阶技巧

**1. 粘贴你自己的数据，获得更准确的分析**
```
/sages 腾讯

营收：6001亿人民币（+10% YoY）
净利润：1577亿
市值：约3.5万亿港元
P/E：17x
最新动态：游戏审批加速，海外业务增长...
```
智者将使用你提供的数据，而非可能过时的训练数据。

**2. 追问**
```
巴菲特什么情况下会对腾讯转为看涨？
塔勒布认为阿里巴巴最大的尾部风险是什么？
```

**3. 行业扫描**
```
/sages compare 腾讯 阿里 拼多多 美团    （中国互联网）
/sages compare 宁德时代 比亚迪 理想       （新能源）
```

---

## 🎯 指令参考

| 指令 | 说明 |
|------|------|
| `/sages AAPL` | 完整议会分析（13位智者）|
| `/sages TSLA --value` | 价值派（巴菲特、芒格、格雷厄姆、帕博莱、伯里）|
| `/sages NVDA --growth` | 成长派（林奇、伍德、德鲁肯米勒、费雪）|
| `/sages AMZN --risk` | 风险分析（塔勒布、达摩达兰）|
| `/sages compare A B` | A vs B 对比分析 |

---

## ⚠️ 免责声明

Market Sages 仅用于**教育和娱乐目的**。

- 非投资建议
- AI 生成的分析可能不准确或基于过时数据
- 在做出投资决策前，请咨询专业金融顾问
- 这些投资人的历史业绩不代表 AI 分析的准确性

---

## 📄 许可证

MIT 许可证 — 随意使用、Fork 和构建。欢迎标注出处。

---

*灵感来自 [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) by @virattt*
