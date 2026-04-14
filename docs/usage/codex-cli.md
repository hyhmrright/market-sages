# Using Market Sages with Codex CLI

[OpenAI Codex CLI](https://github.com/openai/codex) respects `AGENTS.md` files for persistent instructions. Market Sages ships a ready-to-use `AGENTS.md`.

## Installation

### Option 1: Skill Installer (recommended, global install)

In any Codex session (natural language):
```
Install the market-sages skill from hyhmrright/market-sages
```

Or via command line:
```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hyhmrright/market-sages --path skills --name market-sages
```

### Option 2: Project-level AGENTS.md

Run in your project directory:

First time (no existing AGENTS.md):
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/AGENTS.md \
  -o ./AGENTS.md
```

Already have an AGENTS.md? Append instead:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/AGENTS.md \
  >> ./AGENTS.md
```

### Option 3: Manual install

```bash
git clone https://github.com/hyhmrright/market-sages.git /tmp/market-sages
mkdir -p ~/.codex/skills/market-sages
cp -r /tmp/market-sages/skills/* ~/.codex/skills/market-sages/
```

### Verify

```bash
codex "List the 13 Market Sages and their core philosophy"
```

---

## Usage

```bash
# Full council analysis
codex "Analyze Apple using the Market Sages council"

# Specific sages
codex "Use only Benjamin Graham and Michael Burry to evaluate Intel"

# Growth focus
codex "Give me Cathie Wood and Peter Lynch's take on Palantir"

# Risk focus  
codex "Apply Nassim Taleb's antifragility framework to First Republic Bank"

# Comparison
codex "Compare Microsoft and Google through all 13 Market Sages"

# With data
codex "Analyze Nvidia with this data: Revenue $60B, P/E 65x, FCF $27B, data center growing 200% YoY"
```

---

## Multi-turn Conversations

Codex CLI supports conversation history. Use follow-ups:

```bash
codex "Analyze Tesla with all 13 sages"
# After response:
codex "What would change Burry's bearish thesis on Tesla?"
codex "Which sage has the strongest conviction here and why?"
```

---

## Tips

- **Paste earnings data** directly in your prompt for current analysis
- **Name specific sages** to get targeted perspectives
- **Ask for the math** — especially Damodaran (DCF) and Graham (Graham Number)
- **Historical scenarios** work well: "What would the sages say about Lehman in 2007?"

---

## Example Full Session

```bash
$ codex "Market Sages analysis of $NVDA — here's Q3 data: Revenue $18B, Data Center $14.5B, FCF $9.7B, P/E 55x, EV/EBIT 42x, gross margin 74.6%"

[Codex output: Full 13-sage council analysis with Risk Manager and Portfolio Manager...]

$ codex "Taleb seemed bullish — why? Isn't high P/E fragile?"

[Codex follow-up: Taleb's nuanced view on Nvidia's optionality...]
```
