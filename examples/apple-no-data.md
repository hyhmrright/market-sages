# Example: Apple (AAPL) — No Financial Data Provided

> This example shows how the council behaves when the user provides only a ticker
> with no pasted financial data. All 13 sages still produce verdicts, but label
> their analysis as potentially stale.

---

**User prompt:** `/sages AAPL`

**Data provided:** none

---

> Consulting the **Market Sages Council** for **Apple Inc. (AAPL)**...
> *(Using training knowledge as of knowledge cutoff — share recent earnings for updated analysis)*

---

```
╔══════════════════════════════════╗
║  🧠 Warren Buffett               ║
║  Signal: NEUTRAL                 ║
║  Confidence: 45%                 ║
║  Reasoning: Apple has an         ║
║  unassailable ecosystem moat,    ║
║  but without current financials  ║
║  I cannot confirm margin of      ║
║  safety. Training data suggests  ║
║  P/E well above fair value.      ║
╚══════════════════════════════════╝
```

*(... 12 more sage cards — each labeled with training-knowledge caveat ...)*

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 RISK MANAGER ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Consensus: ~5 bullish / ~6 neutral / ~2 bearish
⚠️  Data caveat: All signals based on training knowledge.
    Paste current earnings for a sharper council.

Key Risks:
  • Stale valuation data — signals may not reflect current price
  • China exposure and regulatory risk
  • Services growth deceleration uncertainty
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Key Behavior: No-Data Runs

1. **All 13 sages still appear** — the council runs on training knowledge by default
2. **"potentially stale" label** — every sage qualifies their reasoning
3. **Lower confidence scores** — expect 40-55% rather than 70-85%
4. **Explicit prompt to paste data** — the council invites the user to share current financials

To get a sharper analysis, paste data in the follow-up:

```
Here's the latest:
Revenue: $391B, FCF: $107B, P/E: 28x, Services growing 14%
```
