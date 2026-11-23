---
type: concept
sources: [ch3b, ch6, notes]
updated: 2026-11-23
---

# 經驗法則（Empirical Rule）

## 定義

資料近似鐘形分配時，經驗法則可以算出有多少百分比的資料落在平均數加減幾個標準差之內，它以常態分配為基礎（[ch3b p.17](../sources/ch3b.md)、[ch6 p.27](../sources/ch6.md)），見[常態分配](normal-distribution.md)

## 數字

| 範圍 | 換成 z | 落在範圍內的比例 | 來源 |
|---|---|---|---|
| $\mu \pm 1\sigma$ | $-1 \le z \le 1$ | 68.26% | [ch3b p.18 手寫、p.19](../sources/ch3b.md) |
| $\mu \pm 2\sigma$ | $-2 \le z \le 2$ | 95.45% | [ch3b p.18 手寫、p.19](../sources/ch3b.md) |
| $\mu \pm 3\sigma$ | $-3 \le z \le 3$ | 99.73% | [ch3b p.18 手寫、p.19](../sources/ch3b.md) |

筆記用同樣三個數字整理成 0.6826、0.9545、0.9973（[notes p.6](../sources/notes.md)）

68.26% 是查 z 表算出來的：$P(-1 \le z \le 1) = 0.8413 - 0.1587 = 0.6826$（[ch6 p.41](../sources/ch6.md)）

## 例子

洗衣精的填充重量為鐘形分配，平均 16 盎司、標準差 0.25 盎司（[ch3b p.20](../sources/ch3b.md)）：

- 15.75 到 16.25 盎司（±1 個標準差）：68.26%（[ch3b p.20 手寫](../sources/ch3b.md)）
- 15.50 到 16.50 盎司（±2 個標準差）：95.45%（[ch3b p.19、p.20](../sources/ch3b.md)）
- 15.25 到 16.75 盎司（±3 個標準差）：99.73%，也就是幾乎全部（[ch3b p.19、p.20](../sources/ch3b.md)）

## 對照：柴比雪夫定理（Chebyshev's Theorem）

- 任何資料中，至少有 $1 - 1/z^2$ 的資料落在平均數 ±z 個標準差內，z 必須大於 1，但不必是整數（[ch3b p.11](../sources/ch3b.md)）
- 用在不知道分配的時候，知道分配就不用它（[ch3b p.16](../sources/ch3b.md)）

| 範圍 | 經驗法則（鐘形分配） | 柴比雪夫定理（任何分配，至少） | 來源 |
|---|---|---|---|
| ±1 個標準差 | 68.26% | 不適用，z 必須大於 1 | [ch3b p.11、p.19](../sources/ch3b.md) |
| ±2 個標準差 | 95.45% | 75% | [ch3b p.12、p.19](../sources/ch3b.md) |
| ±3 個標準差 | 99.73% | 89% | [ch3b p.12、p.19](../sources/ch3b.md) |

例子：100 位學生期中考平均 70 分、標準差 5 分，不知道分配時，60 到 80 分（±2 個標準差）之間至少有 75% 的學生（[ch3b p.14](../sources/ch3b.md)）

## 直覺解釋

柴比雪夫定理什麼分配都能用，代價是只能給「至少」的保守答案；知道分配是鐘形，就能用經驗法則說得更精確（補充說明，非來源內容）

## 常見誤解

- 經驗法則不是對所有資料都成立，只適用於鐘形分配（[ch3b p.17](../sources/ch3b.md)），分配很偏時要改用柴比雪夫定理（[ch3b p.16](../sources/ch3b.md)）

## 相關概念

- [z-score](z-score.md)
- [常態分配](normal-distribution.md)：經驗法則的基礎
- [標準常態分配與查表](standard-normal.md)
- [分配形狀與偏態](distribution-shape.md)
- [變異數與標準差](variance-and-standard-deviation.md)

## 矛盾與待確認

- **百分比的小數位數**（[ch3b p.18 到 20](../sources/ch3b.md)）：p.18 的圖寫 95.44%、99.72%，p.19 寫 95.45%、99.73%，p.20 例子寫「約 68%、約 95%、幾乎全部」，[ch6 p.28](../sources/ch6.md) 也寫 95.44%、99.72%，使用者決定一律採用 68.26%、95.45%、99.73%（2026-11-23，已解決）

## 來源

- [ch3b](../sources/ch3b.md) p.11、p.12、p.14、p.16 到 20
- [ch6](../sources/ch6.md) p.27、p.28、p.41
- [notes](../sources/notes.md) p.6
