# Contributing to Market Sages

Thank you for helping make the council wiser. Here's how to contribute.

## Ways to Contribute

### 1. Add a New Sage (`new-analyst` label)

Got a legendary investor not yet in the council? Open an issue with:

- **Investor name and brief bio**
- **Core investment philosophy** (3-5 bullet points)
- **Signal rules** — what makes them bullish, bearish, neutral?
- **Voice style** — how do they talk? What vocabulary is characteristic?
- **Key metrics** — what specific numbers do they look at?
- **Example analysis** — apply their framework to a real company

We prioritize investors with:
- Distinct, documented philosophies (books, interviews, letters)
- Track records spanning multiple market cycles
- Frameworks that complement (not duplicate) existing sages

### 2. Improve Existing Sage Prompts (`prompt-improvement` label)

If a sage's output doesn't sound authentic, or their framework is missing key elements:

1. Open a PR
2. Show a before/after example analysis
3. Cite the source (book, interview, letter) for any added framework elements

### 3. Add CLI Support (`cli-support` label)

We want Market Sages to work everywhere. If you've integrated it with a new CLI tool:

1. Add `TOOLNAME.md` integration file to the root
2. Add a usage guide to `docs/usage/TOOLNAME.md`
3. Update the README's Quick Start section
4. Open a PR with the `cli-support` label

### 4. Translate Documentation (`i18n` label)

Currently supported: English 🇺🇸, Chinese 🇨🇳, Japanese 🇯🇵, Korean 🇰🇷

Want to add your language? Copy `README.md` to `docs/i18n/README.XX.md` (ISO 639-1 code) and translate. Update the language links in all existing READMEs.

### 5. Add Example Analyses (`documentation` label)

Add realistic example analyses to `examples/`. Requirements:
- Real company, specific data (even if historical)
- All 13 sages represented (or document why subset used)
- Shows the Risk Manager + Portfolio Manager output

---

## Contribution Guidelines

- **Stay authentic**: Each sage should sound like themselves — research their actual quotes, books, and letters
- **Be specific**: Vague platitudes don't help. "Seeks companies with moats" is less useful than "ROE > 15% for 10+ consecutive years"
- **Show your work**: When adding new framework elements, cite the source
- **Keep it educational**: Nothing that could be construed as actual investment advice
- **English first**: Core `skill.md` stays in English for maximum LLM compatibility

---

## Quality Bar

Before submitting, ask:
1. Would this sage recognize themselves in the output?
2. Is the framework specific enough to produce different verdicts from similar sages?
3. Does it work without real-time data (using only what the LLM might know)?

---

## Code of Conduct

Be excellent to each other. Disagreements about investment philosophy are welcome; personal attacks are not.

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
