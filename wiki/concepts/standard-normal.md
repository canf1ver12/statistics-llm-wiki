---
type: concept
sources: [ch6, ch8, notes]
updated: 2026-11-23
---

# 標準常態分配與查表（Standard Normal Distribution）

## 定義

平均數為 0、標準差為 1 的常態分配叫做標準常態分配，用字母 $z$ 表示（[ch6 p.30、p.31](../sources/ch6.md)）

## 標準化

任何常態分配都可以轉換成標準常態分配（[ch6 p.24 手寫、p.29](../sources/ch6.md)）：

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

$z$ 可以想成 $x$ 離 $\mu$ 幾個標準差（[ch6 p.29](../sources/ch6.md)）

注意 $N(0, 1)$ 的第二個參數是變異數，不是標準差（[notes p.14](../sources/notes.md)）；標準化時 $\sigma^2$ 要記得開根號（[notes p.19](../sources/notes.md)）

## 查 z 表

- z 表的數值是 z 左邊的曲線下面積，也就是累積機率 $P(z \le a)$（[ch6 p.35](../sources/ch6.md)）
- 例如 $P(z \le 1.00) = 0.8413$、$P(z \le 1.25) = 0.8944$、$P(z \le -0.85) = 0.1977$（[ch6 p.33、p.35、p.37](../sources/ch6.md)）

三種常見的機率（[ch6 p.39](../sources/ch6.md)）：

| 要求的機率 | 算法 | 例子 | 來源 |
|---|---|---|---|
| $P(z \le a)$ | 直接查表 | $P(z \le 1.00) = 0.8413$ | [ch6 p.40](../sources/ch6.md) |
| $P(a \le z \le b)$ | $P(z \le b) - P(z \le a)$ | $P(-0.50 \le z \le 1.25) = 0.8944 - 0.3085 = 0.5859$ | [ch6 p.40](../sources/ch6.md) |
| $P(z \ge a)$ | $1 - P(z \le a)$ | $P(z \ge 1.58) = 1 - 0.9429 = 0.0571$ | [ch6 p.42](../sources/ch6.md) |

## 反過來查：給機率求 z

- $P(Z > z) = 0.10$，等於 $P(Z < z) = 0.90$，查表得 z = 1.28（[ch6 p.43](../sources/ch6.md)）
- $P(Z > z) = 0.05$，查表得 z = 1.645（[ch6 p.60](../sources/ch6.md)）
- 算信賴區間時也是用這個方法找 $z_{\alpha/2}$：例如 95% 信賴時 $P(z < z_{0.025}) = 0.975$，查表得 1.96（[ch8 p.5 手寫](../sources/ch8.md)），見[信賴區間](confidence-interval.md)

## 練習：用經驗法則的數字算機率

- $P(X > \mu + 3\sigma) = P(Z > 3) = (1 - 0.9973)/2 \approx 0.0013$（[notes p.14](../sources/notes.md)）
- $P(\mu + \sigma < X < \mu + 2\sigma) = P(1 < Z < 2) = (0.9545 - 0.6826)/2 = 0.1360$（[notes p.14](../sources/notes.md)）
- 兩題都是利用常態分配左右對稱，把兩尾或兩段的面積平分（補充說明，非來源內容）

## 例子：Grear 輪胎（兩個方向都有）

輪胎里程為 $\mu = 36{,}500$、$\sigma = 5{,}000$ 英里的常態分配（[ch6 p.47](../sources/ch6.md)）

- **給 x 求機率**：超過 40,000 英里的比例，$z = (40{,}000 - 36{,}500)/5{,}000 = 0.70$，$P(z \ge 0.70) = 0.2420$，約 24.2%（[ch6 p.50](../sources/ch6.md)）
- **給機率求 x**：希望最多 10% 的輪胎低於保證里程，左尾面積 0.10 對應 z = −1.28（[ch6 p.51](../sources/ch6.md)），保證里程 $x = 36{,}500 - 1.28 \times 5{,}000 = 30{,}100$ 英里（[ch6 p.53](../sources/ch6.md)）

## 例子：Pep Zone 機油

補貨期間的需求為 $\mu = 15$、$\sigma = 6$ 加侖的常態分配（[ch6 p.55](../sources/ch6.md)）

- **缺貨機率**：需求超過 20 加侖，$z = (20 - 15)/6 = 0.83$（[ch6 p.56](../sources/ch6.md)），$P(z > 0.83) = 1 - 0.7967 = 0.2033$（[ch6 p.58](../sources/ch6.md)）
- **再訂購點**：要讓缺貨機率不超過 0.05，z = 1.645，$x = 15 + 1.645 \times 6 = 24.87$ 加侖（[ch6 p.60](../sources/ch6.md)）

## 常見誤解

- 以為 z 表查到的是「z 右邊」或「0 到 z」的面積：這份講義的 z 表給的是 z 左邊的累積面積（[ch6 p.35](../sources/ch6.md)），算右尾機率要用 1 減掉（[ch6 p.42](../sources/ch6.md)）

## 相關概念

- [常態分配](normal-distribution.md)
- [z-score](z-score.md)：同樣是「離平均數幾個標準差」
- [經驗法則](empirical-rule.md)：68.26% 就是查 z 表算出來的
- [信賴區間](confidence-interval.md)：用反查找 $z_{\alpha/2}$
- [符號對照表](notation.md)

## 矛盾與待確認

- **1.28 和 1.285**（[ch6 p.43、p.51](../sources/ch6.md)）：使用者手寫用了 1.285，講義一律用 1.28，z 表中 1.28 對應 0.8997，比較接近 0.9，使用者決定採用 1.28（2026-11-23，已解決）

## 來源

- [ch6](../sources/ch6.md) p.24、p.29 到 31、p.33、p.35、p.37、p.39 到 43、p.47 到 60
- [ch8](../sources/ch8.md) p.5
- [notes](../sources/notes.md) p.14、p.19
