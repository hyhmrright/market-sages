# Using Market Sages with Gemini CLI

[Google Gemini CLI](https://github.com/google-gemini/gemini-cli) respects `GEMINI.md` files for persistent context. Market Sages ships a ready-to-use `GEMINI.md`.

## Installation

### Option 1: Extension (recommended, global install)

In any Gemini CLI session:
```
/extensions install https://github.com/hyhmrright/market-sages
```

Once installed, the `/sages` command is available globally in all Gemini sessions.

### Option 2: Project-level GEMINI.md

Run in your project directory:

First time (no existing GEMINI.md):
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/GEMINI.md \
  -o ./GEMINI.md
```

Already have a GEMINI.md? Append instead:
```bash
curl -sL https://raw.githubusercontent.com/hyhmrright/market-sages/main/GEMINI.md \
  >> ./GEMINI.md
```

### Option 3: Manual install

```bash
cp /path/to/market-sages/GEMINI.md ./GEMINI.md
# or append:
cat /path/to/market-sages/GEMINI.md >> ./GEMINI.md
```

### Verify

```bash
gemini "List the 13 Market Sages and their core philosophy"
```

---

## Usage

```bash
# Full council analysis
gemini "Analyze Tesla using all 13 Market Sages"

# Specific philosophy focus
gemini "Use the value-focused sages — Buffett, Munger, Graham — to evaluate Berkshire Hathaway"

# Growth analysis
gemini "What do Cathie Wood and Peter Lynch think about Palantir?"

# Risk analysis
gemini "Apply the antifragility lens to cryptocurrency ETFs"

# With real data
gemini "Market Sages analysis of Alphabet: Revenue $307B, FCF $69B, P/E 22x, YouTube ads recovering, Cloud growing 28%"

# Historical
gemini "What would the Market Sages have said about WeWork at its $47B valuation?"
```

---

## Gemini CLI Advantages

Gemini CLI has access to Google Search grounding — you can combine Market Sages with real-time data:

```bash
# Gemini can search for recent data before applying the frameworks
gemini "Search for the latest Apple earnings, then apply the full Market Sages council"

gemini "Find recent news about Tesla and analyze it through Taleb's antifragility lens"
```

---

## Tips for Best Results

1. **Provide data** — Paste earnings, balance sheet, or recent news for current analysis
2. **Specify the scope** — "All 13 sages" vs "just the value sages" vs named individuals
3. **Ask for the math** — "Show me the DCF calculation" (Damodaran) or "What's the Graham Number?" (Graham)
4. **Follow up** — Gemini CLI maintains context, so drill down on interesting findings
5. **Sector comparisons** — "Compare all Big Tech stocks through Druckenmiller's macro lens"

---

## Example Session

```bash
$ gemini "13 Market Sages analysis of ASML: Revenue €27.6B, backlog €39B, EUV monopoly, P/E 40x, net income €7.8B"

[Full council analysis...]

$ gemini "Given ASML's monopoly on EUV, how does Munger's 'wonderful business' thesis apply?"

$ gemini "What's the single biggest tail risk Taleb would identify for ASML?"
```
