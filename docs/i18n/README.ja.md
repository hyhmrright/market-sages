# 🧙 Market Sages — 伝説の投資家評議会

> **13人の伝説的投資家。1つのコマンド。セットアップ不要。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-blue)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Ready-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Ready-red)](https://github.com/google-gemini/gemini-cli)

**Market Sages** は、世界最高の投資家13人の知恵を呼び出し、あらゆる株式を分析します。ウォーレン・バフェット、チャーリー・マンガー、ベンジャミン・グレアム、マイケル・バーリ、ナシーム・タレブなど。

APIキー不要。Python環境不要。金融データサブスクリプション不要。ティッカーシンボルだけで始められます。

---

**[🇺🇸 English](../../README.md)** | **[🇨🇳 中文](README.zh-CN.md)** | **[🇰🇷 한국어](README.ko.md)**

---

## ✨ 何ができるのか

入力：
```
/sages NVDA
```

評議会の完全な審議結果を取得：

```
╔══════════════════════════════════╗
║  🧠 ウォーレン・バフェット        ║
║  シグナル: 中立                  ║
║  信頼度: 55%                     ║
║  分析: 優れた堀（ゲームエコシステム）,
║  しかし現在のP/Eでは安全余裕なし。 ║
╚══════════════════════════════════╝

... (他11人の賢者)

╔══════════════════════════════════════════════╗
║  🏦 ポートフォリオマネージャー — 最終評決    ║
║  アクション: 様子見                          ║
║  エントリー戦略: 20-25%下落を待つ            ║
╚══════════════════════════════════════════════╝
```

---

## 🧑‍💼 13人の賢者評議会

| # | 賢者 | 投資哲学 | 核心基準 |
|---|------|---------|---------|
| 1 | **ウォーレン・バフェット** | 適正価格で優良企業を | 堀 + 安全余裕 >25% |
| 2 | **チャーリー・マンガー** | 逆算、メンタルモデル | ROIC >15%、優れた企業 |
| 3 | **ベンジャミン・グレアム** | 安全余裕が全て | グレアム数 + 流動比率 >2 |
| 4 | **ピーター・リンチ** | テンバガー、知っている企業に投資 | PEG <1、理解可能 |
| 5 | **マイケル・バーリ** | ディープバリュー逆張り | FCF利回り >10%、EV/EBIT <8 |
| 6 | **キャシー・ウッド** | 破壊的イノベーション | 5年収益CAGR >15% |
| 7 | **スタンリー・ドラッケンミラー** | 非対称マクロ機会 | 業績改訂 + 非対称リターン |
| 8 | **ビル・アックマン** | アクティビスト、シンプルなビジネス | FCF + 経営陣触媒 |
| 9 | **フィル・フィッシャー** | スカットルバット、永続保有 | 15問フレームワーク |
| 10 | **ナシーム・タレブ** | アンチフラジャイル、テールリスク | 反脆弱性 + 凸性 |
| 11 | **モニッシュ・パブライ** | ダンド（Dhandho）フレームワーク | 下値リスク優先 + 安全余裕 >50% |
| 12 | **アスワス・ダモダラン** | ストーリー＋数字、DCF | DCF内在価値 |
| 13 | **ラケシュ・ジュンジュンワラ** | 正しくあれ、保有し続けよ | ROCE >20% |

---

## 🚀 クイックスタート

### Claude Code（推奨）

```bash
# スキルファイルをClaudeスキルディレクトリにコピー
cp skill.md ~/.claude/skills/market-sages.md
```

使用方法：
```
/sages トヨタ
/sages 7203 --value      # バリュー賢者のみ
/sages SONY --growth     # グロース賢者のみ
/sages compare 7203 9984  # 比較分析
```

### OpenAI Codex CLI

```bash
cp AGENTS.md /path/to/your/project/AGENTS.md
```

```bash
codex "Market Sages評議会でトヨタを分析してください"
```

### Google Gemini CLI

```bash
cp GEMINI.md /path/to/your/project/GEMINI.md
```

```bash
gemini "13人のMarket Sagesでソニーを分析してください"
```

---

## ⚠️ 免責事項

Market Sagesは**教育・娯楽目的のみ**です。投資アドバイスではありません。投資判断を行う前に、資格を持つ金融アドバイザーにご相談ください。

---

## 📄 ライセンス

MIT License

---

*インスピレーション: [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) by @virattt*
