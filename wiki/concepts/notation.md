---
type: concept
sources: [ch3a, ch3b, ch6, ch7, ch8]
updated: 2026-11-23
---

# 符號對照表（Notation）

本輪主題會用到的符號，每次 ingest 時補充

## 母體與樣本

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $N$ | N | 母體的資料個數 | [ch3a p.7 手寫、p.8](../sources/ch3a.md) |
| $n$ | n | 樣本的資料個數 | [ch3a p.7](../sources/ch3a.md) |
| $x_i$ | x sub i | 第 $i$ 筆觀察值 | [ch3a p.14](../sources/ch3a.md) |

## 母體參數（固定的數字）

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $\mu$ | mu | 母體平均數 | [ch3a p.8](../sources/ch3a.md) |
| $\sigma^2$ | sigma 平方 | 母體變異數 | [ch3a p.45](../sources/ch3a.md) |
| $\sigma$ | sigma | 母體標準差 | [ch3a p.49](../sources/ch3a.md) |

## 樣本統計量

| 符號 | 讀法 | 意義 | 估計的母體參數 | 來源 |
|---|---|---|---|---|
| $\bar{x}$ | x bar | 樣本平均數（算出來的值） | $\mu$ | [ch3a p.4、p.7](../sources/ch3a.md) |
| $\bar{X}$ | 大寫 X bar | 樣本平均數的數學式，是隨機變數 | $\mu$ | [ch3a p.4 手寫](../sources/ch3a.md) |
| $s^2$ | s 平方 | 樣本變異數 | $\sigma^2$ | [ch3a p.4 手寫、p.45](../sources/ch3a.md) |
| $s$ | s | 樣本標準差 | $\sigma$ | [ch3a p.49](../sources/ch3a.md) |

## 標準化

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $z_i$ | z sub i | 第 $i$ 筆資料的 z-score，離平均數幾個標準差 | [ch3b p.7](../sources/ch3b.md) |
| $Z$ | 大寫 Z | 標準常態隨機變數，$Z = (X - \mu)/\sigma$ | [ch6 p.24 手寫、p.31](../sources/ch6.md) |

## 機率分配

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $X \sim N(\mu, \sigma^2)$ | X 服從常態分配 | 隨機變數 $X$ 為平均數 $\mu$、變異數 $\sigma^2$ 的常態分配 | [ch6 p.15 手寫](../sources/ch6.md) |
| $N(0, 1)$ | 標準常態 | 平均數 0、變異數 1 的常態分配 | [ch6 p.24 手寫、p.30](../sources/ch6.md) |
| $E(X)$ | X 的期望值 | 隨機變數的平均數 | [ch6 p.15 手寫](../sources/ch6.md) |
| $V(X)$ | X 的變異數 | 隨機變數的變異數 | [ch6 p.15 手寫](../sources/ch6.md) |

## 抽樣分配與點估計

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $X_1, \dots, X_n$ | X sub 1 到 X sub n | 樣本中的 n 個觀察值，抽之前是隨機變數，iid | [ch7 p.19 手寫、p.48 手寫](../sources/ch7.md) |
| $E(\bar{x})$ | x bar 的期望值 | 抽樣分配的平均數，等於 $\mu$ | [ch7 p.45](../sources/ch7.md) |
| $\sigma_{\bar{x}}$ | sigma sub x bar | $\bar{x}$ 的標準差，也就是標準誤差，等於 $\sigma/\sqrt{n}$ | [ch7 p.46、p.47](../sources/ch7.md) |
| $\theta$ | theta | 泛指某個母體參數 | [ch7 p.109](../sources/ch7.md) |
| $\hat{\theta}$ | theta hat | $\theta$ 的點估計量 | [ch7 p.109](../sources/ch7.md) |

## 信賴區間

| 符號 | 讀法 | 意義 | 來源 |
|---|---|---|---|
| $1 - \alpha$ | 1 減 alpha | 信賴係數，例如 0.95 | [ch8 p.39](../sources/ch8.md) |
| $\alpha$ | alpha | 兩尾加起來的面積，例如 0.05 | [ch8 p.40](../sources/ch8.md) |
| $z_{\alpha/2}$ | z sub alpha over 2 | 標準常態右尾面積為 $\alpha/2$ 的 z 值，95% 時為 1.96 | [ch8 p.39、p.40](../sources/ch8.md) |
| $E$ | E | 邊際誤差，$z_{\alpha/2}\,\sigma/\sqrt{n}$ | [ch8 p.6 手寫、p.28](../sources/ch8.md) |
| $t_{\alpha/2}$ | t sub alpha over 2 | σ 未知時改用的 t 分配臨界值 | [ch8 p.74](../sources/ch8.md) |

## 相關概念

- [母體參數與樣本統計量](parameter-and-statistic.md)
- [平均數](mean.md)
- [變異數與標準差](variance-and-standard-deviation.md)
- [z-score](z-score.md)
- [常態分配](normal-distribution.md)
- [標準常態分配與查表](standard-normal.md)
- [抽樣分配](sampling-distribution.md)
- [標準誤差](standard-error.md)
- [信賴區間](confidence-interval.md)
- [邊際誤差與樣本數](margin-of-error.md)
