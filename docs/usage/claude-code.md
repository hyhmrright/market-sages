# Using Market Sages with Claude Code

## Installation

### Option 1: Global install (use in any project)

```bash
cp skill.md ~/.claude/skills/market-sages.md
```

### Option 2: Project-level install

```bash
cp skill.md /your/project/.claude/skills/market-sages.md
```

### Option 3: Reference from CLAUDE.md

Add to your project's `CLAUDE.md`:
```markdown
# Skills
Use the Market Sages framework from `skill.md` when the user asks to analyze a stock or investment.
```

---

## Basic Usage

Once installed, invoke the skill in any Claude Code session:

```
/sages AAPL
```

Or trigger it naturally:
```
Analyze Apple using the Market Sages council
What do the 13 legendary investors think about Nvidia?
Give me Buffett and Munger's take on Microsoft
```

---

## Command Reference

| Command | What it does |
|---------|--------------|
| `/sages AAPL` | Full council — all 13 sages |
| `/sages TSLA --value` | Value sages: Buffett, Munger, Graham, Pabrai, Burry |
| `/sages NVDA --growth` | Growth sages: Lynch, Wood, Druckenmiller, Fisher |
| `/sages AMZN --risk` | Risk sages: Taleb, Damodaran |
| `/sages compare AAPL MSFT` | Side-by-side council comparison |
| `/sages GOOG @buffett @taleb` | Specific sages by name |

---

## Power Tips

### Paste real financial data for sharper analysis

```
/sages AAPL

Here's the latest data:
Revenue: $391B (+2% YoY)
Net Income: $94B  
FCF: $107B
P/E: 28x, EV/EBITDA: 22x
Debt: $104B, Cash: $65B
Gross Margin: 45%
Recent: Vision Pro sales disappointing, services growing 14%
```

The sages will prioritize your data over potentially stale training knowledge.

### Ask follow-up questions

```
What would it take for Buffett to become bullish on Apple?
What's the single biggest risk Taleb sees in Nvidia?
How does Burry's Microsoft thesis compare to his typical plays?
```

### Portfolio review

```
Review my portfolio: 40% AAPL, 30% NVDA, 20% TSLA, 10% cash
Which sages are most concerned? What would they cut first?
```

### Historical analysis

```
What would the Market Sages have said about SVB in January 2023?
Apply the council to Enron at its peak in 2001
```

---

## Understanding the Output

Each sage produces a verdict card:
```
╔══════════════════════════════════╗
║  🧠 [SAGE NAME]                  ║
║  Signal: BULLISH/BEARISH/NEUTRAL ║
║  Confidence: XX%                 ║
║  Reasoning: [1-2 sentences]      ║
╚══════════════════════════════════╝
```

Then you get:
1. **Risk Manager Assessment** — consensus score, key risks, bull/bear scenarios, suggested max position size
2. **Portfolio Manager Final Verdict** — action (BUY/HOLD/SELL/WATCH), conviction level, entry strategy, exit criteria

---

## Customization

You can ask the council to weigh in differently:

```
Give extra weight to Taleb and Burry — I'm worried about downside
Focus on the sages who agree with each other
Which sages would be most likely to invest at this price level?
```

---

## Troubleshooting

**"The analysis seems based on old data"**
→ Paste current financial data directly in your message. The sages will use it.

**"I want only specific sages"**
→ Name them: `/sages AAPL @buffett @munger @graham`

**"The output is too long"**
→ Ask for a summary: `/sages AAPL --brief` or "Give me just the final verdict and top 3 concerns"
