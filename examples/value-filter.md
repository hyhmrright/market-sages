# Example: Tesla (TSLA) — Value Sages Only (`--value`)

> This example shows the `--value` filter: only the 5 value-focused sages are consulted.
> Growth and macro sages (Wood, Lynch, Druckenmiller, Fisher) are excluded.

---

**User prompt:** `/sages TSLA --value`

**Sages consulted:** Buffett · Munger · Graham · Pabrai · Burry

---

```
╔══════════════════════════════════╗
║  🧠 Warren Buffett               ║
║  Signal: BEARISH                 ║
║  Confidence: 68%                 ║
║  Reasoning: Automotive is        ║
║  outside my circle of competence ║
║  at the best of times. At a P/E  ║
║  above 50x, there's no margin    ║
║  of safety here for a patient    ║
║  capital allocator.              ║
╚══════════════════════════════════╝
```

```
╔══════════════════════════════════╗
║  🧠 Michael Burry                ║
║  Signal: BEARISH                 ║
║  Confidence: 75%                 ║
║  Reasoning: FCF yield well below ║
║  my 10% threshold. EV/EBIT in   ║
║  deep overvaluation territory.   ║
║  No deep-value case here.        ║
╚══════════════════════════════════╝
```

*(... 3 more value sage cards ...)*

---

```
╔══════════════════════════════════════════════╗
║  🏦 PORTFOLIO MANAGER — FINAL VERDICT        ║
╠══════════════════════════════════════════════╣
║  Action: SELL / AVOID                        ║
║  Conviction: HIGH (among value sages)        ║
║  Note: This is a value-lens verdict only.    ║
║  Growth sages (Wood, Lynch) may disagree.    ║
╠══════════════════════════════════════════════╣
║  ⚠️  DISCLAIMER: Educational only.           ║
║  Not financial advice. DYOR.                 ║
╚══════════════════════════════════════════════╝
```

---

## Key Behavior: Filter Flags

| Flag | Sages included |
|------|----------------|
| `--value` | Buffett, Munger, Graham, Pabrai, Burry |
| `--growth` | Lynch, Wood, Druckenmiller, Fisher |
| `--risk` | Taleb, Damodaran |
| *(none)* | All 13 |

The Portfolio Manager verdict notes which lens was applied so the user understands
the result is a partial view.
