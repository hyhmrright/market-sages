# 🧙 Market Sages

> **13 legendary investors. One command. Zero setup.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-blue?logo=anthropic)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Ready-green?logo=openai)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Ready-red?logo=google)](https://github.com/google-gemini/gemini-cli)

**Market Sages** summons a council of the world's greatest investors to analyze any stock — Warren Buffett, Charlie Munger, Benjamin Graham, Michael Burry, Nassim Taleb, and 8 more. No API keys. No Python environment. No financial data subscription. Just a ticker symbol.

---

**[🇨🇳 中文文档](docs/i18n/README.zh-CN.md)** | **[🇯🇵 日本語](docs/i18n/README.ja.md)** | **[🇰🇷 한국어](docs/i18n/README.ko.md)**

---

## ✨ What It Does

You type:
```
/sages NVDA
```

You get a full council deliberation:

```
╔══════════════════════════════════╗
║  🧠 Warren Buffett               ║
║  Signal: NEUTRAL                 ║
║  Confidence: 55%                 ║
║  Reasoning: Exceptional moat     ║
║  (gaming ecosystem), but current ║
║  P/E leaves no margin of safety. ║
╚══════════════════════════════════╝

╔══════════════════════════════════╗
║  🧠 Michael Burry                ║
║  Signal: BEARISH                 ║
║  Confidence: 72%                 ║
║  Reasoning: FCF yield ~1.8%,     ║
║  EV/EBIT ~80x — no deep value    ║
║  here, this is momentum not math.║
╚══════════════════════════════════╝

... (11 more sages)

╔══════════════════════════════════════════════╗
║  🏦 PORTFOLIO MANAGER — FINAL VERDICT        ║
║  Action: WATCH                               ║
║  Conviction: MEDIUM                          ║
║  Entry Strategy: Wait for 20-25% pullback    ║
╚══════════════════════════════════════════════╝
```

---

## 🧑‍💼 The Council of 13 Sages

| # | Sage | Philosophy | Style |
|---|------|-----------|-------|
| 1 | **Warren Buffett** | Wonderful companies at fair prices | Patient, moat-focused |
| 2 | **Charlie Munger** | Invert always invert | Multi-disciplinary, blunt |
| 3 | **Benjamin Graham** | Margin of safety, Mr. Market | Quantitative, academic |
| 4 | **Peter Lynch** | Ten-baggers, invest in what you know | Enthusiastic, accessible |
| 5 | **Michael Burry** | Deep value contrarian | Data-obsessed, terse |
| 6 | **Cathie Wood** | Disruptive innovation | Evangelical, future-focused |
| 7 | **Stanley Druckenmiller** | Asymmetric macro opportunities | Confident, macro sweep |
| 8 | **Bill Ackman** | Activist, simple businesses | Direct, catalyst-driven |
| 9 | **Phil Fisher** | Scuttlebutt, quality forever | Meticulous, qualitative |
| 10 | **Nassim Taleb** | Antifragility, tail risk | Precise, uncompromising |
| 11 | **Mohnish Pabrai** | Dhandho, downside first | Humble, Buffett-inspired |
| 12 | **Aswath Damodaran** | Story + numbers, DCF | Professor-like, rigorous |
| 13 | **Rakesh Jhunjhunwala** | Be right, sit tight | Conviction, long-term |

---

## 🚀 Quick Start

### Claude Code (Recommended)

**Via Plugin Marketplace (recommended):**
```bash
/plugin marketplace add hyhmrright/market-sages
/plugin install market-sages@market-sages-marketplace
```

**One-liner install (no clone needed):**
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/skill.md \
  -o ~/.claude/skills/market-sages.md
```

**Manual install:**
```bash
git clone https://github.com/hyhmrright/market-sages.git
cp market-sages/skill.md ~/.claude/skills/market-sages.md
```

**Verify:** Open a Claude Code session and type `/sages AAPL` — you should see the council spin up.

**Use:**
```
/sages AAPL
/sages TSLA --value
/sages AMZN --growth
/sages MSFT --risk
/sages compare AAPL MSFT GOOG
```

→ [Full Claude Code guide](docs/usage/claude-code.md)

---

### OpenAI Codex CLI

**Via Skill Installer (in a Codex session):**
```
Install the market-sages skill from hyhmrright/market-sages
```

**Command line:**
```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hyhmrright/market-sages --path skills --name market-sages
```

**Manual (project-level AGENTS.md):**

First time:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/AGENTS.md \
  -o ./AGENTS.md
```
Already have an AGENTS.md? Append instead:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/AGENTS.md \
  >> ./AGENTS.md
```

**Use:**
```bash
codex "Analyze Apple using the Market Sages council"
codex "Use Michael Burry and Benjamin Graham to evaluate INTC"
```

→ [Full Codex CLI guide](docs/usage/codex-cli.md)

---

### Google Gemini CLI

**Via Extension (in a Gemini session):**
```
/extensions install https://github.com/hyhmrright/market-sages
```

**Manual (project-level GEMINI.md):**

First time:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/GEMINI.md \
  -o ./GEMINI.md
```
Already have a GEMINI.md? Append instead:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/GEMINI.md \
  >> ./GEMINI.md
```

**Use:**
```bash
gemini "Analyze Tesla using all 13 Market Sages"
gemini "Give me Nassim Taleb and Aswath Damodaran's take on NVDA"
```

→ [Full Gemini CLI guide](docs/usage/gemini-cli.md)

---

### Universal (Any LLM / Chat Interface)

Copy the contents of `skill.md` as your **system prompt** in any LLM interface — ChatGPT, Claude.ai, Gemini, Perplexity, or any custom app. Then start chatting.

---

## 🎯 Command Reference

| Command | Description |
|---------|-------------|
| `/sages AAPL` | Full council (all 13 sages) |
| `/sages TSLA --value` | Value sages only (Buffett, Munger, Graham, Pabrai, Burry) |
| `/sages NVDA --growth` | Growth sages only (Lynch, Wood, Druckenmiller, Fisher) |
| `/sages AMZN --risk` | Risk sages only (Taleb, Damodaran + Risk Manager) |
| `/sages compare AAPL MSFT` | Side-by-side comparison |
| `/sages GOOG @buffett @munger` | Specific sages by name |

---

## 💡 Power Tips

**1. Paste your own data for sharper analysis**
```
/sages AAPL

Revenue: $391B (+2% YoY)
Net Income: $94B
FCF: $107B
P/E: 28x, EV/EBITDA: 22x
Debt: $104B, Cash: $65B
Recent news: Vision Pro sales disappointing...
```
The sages will use your data instead of potentially stale training knowledge.

**2. Ask follow-up questions**
```
What would make Buffett upgrade to bullish on AAPL?
What's Taleb's worst-case scenario for NVDA?
How does Burry's AAPL thesis compare to his typical deep-value plays?
```

**3. Sector sweeps**
```
/sages compare AAPL MSFT GOOG META AMZN  (Big Tech council)
/sages compare JPM BAC GS                (Banking council)
```

**4. Portfolio review**
```
Review my portfolio: 40% AAPL, 30% NVDA, 20% TSLA, 10% BTC
Which sages would be most concerned?
```

---

## ❓ FAQ & Troubleshooting

**Q: `/sages` command not found after installation**
```bash
# Re-copy and verify the file is in the right place
cp skill.md ~/.claude/skills/market-sages.md
ls ~/.claude/skills/market-sages.md
```
Then restart Claude Code and try again.

**Q: The sages are using outdated data**
Paste current financial data directly in your message — the sages will prioritize it over training knowledge:
```
/sages NVDA
Revenue $60.9B, P/E 55x, Gross Margin 74.6%...
```

**Q: Can I use only a subset of sages?**
Yes — use `@` to name them:
```
/sages AAPL @buffett @graham @burry
```

**Q: The analysis is in the wrong language**
The skill auto-detects your input language. Write your prompt in the language you want the response in.

**Q: How do I run the tests?**
```bash
# Structure validation (no API key needed)
uv run tests/validate_structure.py --verbose

# Prompt evaluation (requires ANTHROPIC_API_KEY)
export ANTHROPIC_API_KEY=sk-...
uv run tests/run_evals.py
```

---

## 🗂️ Project Structure

```
market-sages/
├── skill.md              # Core skill — the 13 sages' frameworks
├── AGENTS.md             # Codex CLI integration
├── GEMINI.md             # Gemini CLI integration
├── README.md             # This file
├── docs/
│   ├── usage/
│   │   ├── claude-code.md
│   │   ├── codex-cli.md
│   │   └── gemini-cli.md
│   └── i18n/
│       ├── README.zh-CN.md
│       ├── README.ja.md
│       └── README.ko.md
└── examples/
    ├── nvidia-analysis.md
    └── apple-analysis.md
```

---

## 🤝 Contributing

We welcome new sages, prompt improvements, and CLI integrations!

- **Add a new sage**: Open an issue with `new-analyst` label. Include: philosopher/investor, their core framework, signal rules, and voice style.
- **Improve a prompt**: Open a PR with `prompt-improvement` label. Show before/after examples.
- **Add CLI support**: Open an issue with `cli-support` label.
- **Translate docs**: Open a PR with `i18n` label.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## ⚠️ Disclaimer

Market Sages is for **educational and entertainment purposes only**.

- Not financial advice
- AI-generated analysis may be inaccurate or based on stale training data
- Always verify with current, authoritative financial data
- Past performance of these investors does not guarantee similar AI output quality
- Consult a qualified financial advisor before making investment decisions

---

## 📄 License

MIT — use it, fork it, build on it. Attribution appreciated.

---

## ⭐ Star History

If Market Sages helped you think more clearly about an investment, please star the repo. It helps others find it.

---

*Inspired by [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) by @virattt — the original multi-agent hedge fund that sparked this idea.*
