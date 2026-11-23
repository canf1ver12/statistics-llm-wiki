# Index

統計學 LLM Wiki 的目錄，每次 ingest 後更新，規範見 [AGENTS.md](../AGENTS.md)

本輪主題：抽樣分配、中央極限定理與信賴區間

## 總覽

- [overview](overview.md)：概念鏈與各概念回答的問題

## 概念 (Concepts)

| 頁面 | 一行摘要 | 來源 |
|---|---|---|
| [parameter-and-statistic](concepts/parameter-and-statistic.md) | 母體參數與樣本統計量、點估計量、大寫 $\bar{X}$ 和小寫 $\bar{x}$ 的差別 | ch3a、ch7 |
| [mean](concepts/mean.md) | 樣本平均數與母體平均數的公式和例子 | ch3a、ch3b |
| [variance-and-standard-deviation](concepts/variance-and-standard-deviation.md) | 變異數、標準差，以及樣本分母為何是 $n-1$ | ch3a、ch3b、ch7、ch8 |
| [distribution-shape](concepts/distribution-shape.md) | 偏態、左偏右偏時平均數與中位數的關係 | ch3b、ch7 |
| [z-score](concepts/z-score.md) | 標準化值，離平均數幾個標準差，以及用 z 找離群值 | ch3b、ch6 |
| [empirical-rule](concepts/empirical-rule.md) | 經驗法則 68.26%、95.45%、99.73%，與柴比雪夫定理對照 | ch3b、ch6 |
| [normal-distribution](concepts/normal-distribution.md) | 常態分配的特性、連續型的機率是面積 | ch6 |
| [standard-normal](concepts/standard-normal.md) | 標準化、查 z 表、給機率反查 z，輪胎和機油的例子 | ch6、ch8 |
| [random-sampling](concepts/random-sampling.md) | 母體、樣本、簡單隨機抽樣、iid | ch7 |
| [point-estimation](concepts/point-estimation.md) | 估計量與點估計值、SAT 例子、不偏有效一致 | ch7、ch3a、ch8 |
| [sampling-distribution](concepts/sampling-distribution.md) | $\bar{x}$ 的抽樣分配、EAI 抽 500 次、$E(\bar{x}) = \mu$ 的推導、抽樣誤差 | ch7 |
| [central-limit-theorem](concepts/central-limit-theorem.md) | 中央極限定理、樣本數要多大、三種母體的圖解 | ch7、ch8 |
| [standard-error](concepts/standard-error.md) | $\sigma/\sqrt{n}$、樣本數和標準誤差的關係、EAI 和 SAT 例子 | ch7 |
| [confidence-interval](concepts/confidence-interval.md) | 信賴區間的推導、z 值表、95% 信賴的意思、Lloyd's 和 Discount Sounds | ch8、ch7 |
| [margin-of-error](concepts/margin-of-error.md) | 邊際誤差、影響區間寬度的因素、樣本數公式 | ch8 |
| [notation](concepts/notation.md) | 符號對照表 | ch3a、ch3b、ch6、ch7、ch8 |

## 來源 (Sources)

| 來源 | 內容 | 狀態 |
|---|---|---|
| [ch3a](sources/ch3a.md) | 描述統計：位置與變異量數 | 已 ingest（2026-11-23） |
| [ch3b](sources/ch3b.md) | 分配形狀、z-score、經驗法則 | 已 ingest（2026-11-23） |
| [ch6](sources/ch6.md) | 連續機率分配、常態分配 | 已 ingest（2026-11-23） |
| [ch7](sources/ch7.md) | 抽樣與抽樣分配、中央極限定理 | 已 ingest（2026-11-23） |
| [ch8](sources/ch8.md) | 區間估計 | 已 ingest（2026-11-23） |
| [notes](sources/notes.md) | 使用者手寫筆記（本輪只處理 13 頁） | 已 ingest（2026-11-23） |

## 產出 (Outputs)

（尚無頁面）

## 待展開

本輪範圍外，但使用者要求之後詳細寫的主題：

- 常態母體下 $s$ 與 $\bar{x}$ 互相獨立，非常態母體不成立（[ch3a p.51 手寫](sources/ch3a.md)，2026-11-23 列入）
- 右偏分配時，平均數會不會大於 Q3（[ch3b p.31 手寫](sources/ch3b.md)，2026-11-23 列入）

## 紀錄

- [log.md](log.md)：時間序紀錄
