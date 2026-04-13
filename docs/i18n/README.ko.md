# 🧙 Market Sages — 전설적 투자자 의회

> **13명의 전설적 투자자. 하나의 명령. 설정 불필요.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-blue)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-Ready-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Ready-red)](https://github.com/google-gemini/gemini-cli)

**Market Sages**는 세계 최고의 투자자 13명의 지혜를 소환하여 모든 주식을 분석합니다. 워렌 버핏, 찰리 멍거, 벤자민 그레이엄, 마이클 버리, 나심 탈레브 등.

API 키 불필요. Python 환경 불필요. 금융 데이터 구독 불필요. 티커 심볼 하나면 충분합니다.

---

**[🇺🇸 English](../../README.md)** | **[🇨🇳 中文](README.zh-CN.md)** | **[🇯🇵 日本語](README.ja.md)**

---

## ✨ 무엇을 할 수 있나요

입력:
```
/sages NVDA
```

의회의 완전한 심의 결과:

```
╔══════════════════════════════════╗
║  🧠 워렌 버핏                    ║
║  신호: 중립                      ║
║  신뢰도: 55%                     ║
║  분석: 탁월한 해자(게임 생태계), ║
║  하지만 현 P/E로는 안전마진 부족 ║
╚══════════════════════════════════╝

... (다른 11명의 현인)

╔══════════════════════════════════════════════╗
║  🏦 포트폴리오 매니저 — 최종 평결            ║
║  행동: 관망                                  ║
║  진입 전략: 20-25% 하락 대기                 ║
╚══════════════════════════════════════════════╝
```

---

## 🧑‍💼 13명의 현인 의회

| # | 현인 | 투자 철학 | 핵심 기준 |
|---|------|---------|---------|
| 1 | **워렌 버핏** | 합리적 가격에 훌륭한 기업 | 해자 + 안전마진 >25% |
| 2 | **찰리 멍거** | 역발상, 멘탈 모델 | ROIC >15%, 훌륭한 기업 |
| 3 | **벤자민 그레이엄** | 안전마진이 전부 | 그레이엄 넘버 + 유동비율 >2 |
| 4 | **피터 린치** | 텐배거, 아는 곳에 투자 | PEG <1, 이해 가능 |
| 5 | **마이클 버리** | 심층 가치 역발상 | FCF 수익률 >10%, EV/EBIT <8 |
| 6 | **캐시 우드** | 파괴적 혁신 | 5년 매출 CAGR >15% |
| 7 | **스탠리 드러켄밀러** | 비대칭 매크로 기회 | 실적 상향 + 비대칭 수익 |
| 8 | **빌 애크만** | 행동주의, 단순한 사업 | FCF + 경영진 촉매 |
| 9 | **필 피셔** | 발품 조사, 영구 보유 | 15문항 프레임워크 |
| 10 | **나심 탈레브** | 반취약성, 꼬리 위험 | 반취약성 + 볼록성 |
| 11 | **모니시 파브라이** | 단도(Dhandho) 프레임워크 | 하방 우선 + 안전마진 >50% |
| 12 | **아스워스 다모다란** | 스토리+숫자, DCF | DCF 내재가치 |
| 13 | **라케시 중중왈라** | 옳게 있어라, 계속 보유해라 | ROCE >20% |

---

## 🚀 빠른 시작

### Claude Code (권장)

```bash
# 스킬 파일을 Claude 스킬 디렉토리에 복사
cp skill.md ~/.claude/skills/market-sages.md
```

사용:
```
/sages 삼성전자
/sages 005930 --value    # 가치 현인만
/sages KAKAO --growth    # 성장 현인만
/sages compare 005930 000660  # 비교 분석
```

### OpenAI Codex CLI

```bash
cp AGENTS.md /path/to/your/project/AGENTS.md
```

```bash
codex "Market Sages 의회로 삼성전자를 분석해주세요"
```

### Google Gemini CLI

```bash
cp GEMINI.md /path/to/your/project/GEMINI.md
```

```bash
gemini "13명의 Market Sages로 카카오를 분석해주세요"
```

---

## 💡 고급 팁

**직접 데이터 붙여넣기**
```
/sages 삼성전자

매출: 300조원 (+8% YoY)
영업이익: 32조원
시가총액: 약 400조원
PER: 12배
최신 동향: HBM3 수요 급증, 파운드리 점유율 회복 중...
```

**섹터 스캔**
```
/sages compare 삼성전자 SK하이닉스 LG전자    (전자)
/sages compare 현대차 기아 LG에너지솔루션     (전기차)
```

---

## ⚠️ 면책 조항

Market Sages는 **교육 및 오락 목적으로만** 제공됩니다. 투자 조언이 아닙니다. 투자 결정을 내리기 전에 자격을 갖춘 금융 어드바이저와 상담하세요.

---

## 📄 라이선스

MIT License

---

*영감: [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) by @virattt*
