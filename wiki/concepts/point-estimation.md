---
type: concept
sources: [ch7, ch3a, ch8, notes]
updated: 2026-11-23
---

# 點估計（Point Estimation）

## 定義

- 點估計是用樣本資料算出樣本統計量，當作母體參數的估計值，是統計推論的一種形式（[ch7 p.24](../sources/ch7.md)）
- $\bar{x}$ 是 $\mu$ 的點估計量，$s$ 是 $\sigma$ 的點估計量，$\bar{p}$ 是母體比例 $p$ 的點估計量（[ch7 p.24](../sources/ch7.md)）

## 估計量和估計值

| | 估計量（estimator） | 點估計值（point estimate） | 來源 |
|---|---|---|---|
| 是什麼 | 數學式，是隨機變數 | 把資料代進數學式算出來的數字 | [ch7 p.19 手寫](../sources/ch7.md)、[ch3a p.4 手寫](../sources/ch3a.md) |
| 平均數的例子 | $\bar{X} = (X_1 + \dots + X_n)/n$ | $\bar{x} = 166$ | [ch7 p.19 手寫](../sources/ch7.md) |
| 變異數的例子 | $s^2 = \sum(X_i - \bar{X})^2/(n-1)$ | $s^2 = 49$ | [ch7 p.20 手寫](../sources/ch7.md) |

估計量是隨機變數，因為抽到的人會不一樣，算出來的值也不一樣（[ch7 p.19 手寫](../sources/ch7.md)）

筆記把估計分成點估計和區間估計兩種（[notes p.19](../sources/notes.md)），區間估計見[信賴區間](confidence-interval.md)

## 例子：St. Andrew's College

900 位申請者中用亂數抽出 30 位（[ch7 p.28](../sources/ch7.md)），之後資料全部建檔，才算出母體參數（[ch7 p.30](../sources/ch7.md)）：

| 母體參數 | 真正的值 | 點估計量 | 點估計值 | 來源 |
|---|---|---|---|---|
| SAT 平均 $\mu$ | 1697 | $\bar{x}$ | 1684 | [ch7 p.29 到 31](../sources/ch7.md) |
| SAT 標準差 $\sigma$ | 87.4 | $s$ | 85.2 | [ch7 p.29 到 31](../sources/ch7.md) |
| 想住校的比例 $p$ | 0.72 | $\bar{p}$ | 0.67 | [ch7 p.29 到 31](../sources/ch7.md) |

點估計值和真正的值很接近但不相等，換一組亂數會抽到不同的樣本，得到不同的點估計值（[ch7 p.29](../sources/ch7.md)）

## 好的點估計量要有的性質

用 $\theta$ 表示母體參數，$\hat{\theta}$ 表示它的點估計量（[ch7 p.109](../sources/ch7.md)）

| 性質 | 意思 | 來源 |
|---|---|---|
| 不偏（unbiased） | $E(\hat{\theta}) = \theta$，抽樣分配的中心剛好在母體參數上 | [ch7 p.111、p.112](../sources/ch7.md) |
| 有效（efficiency） | 兩個不偏估計量中，標準差較小的比較好 | [ch7 p.113](../sources/ch7.md) |
| 一致（consistency） | 樣本數越大，點估計值越接近母體參數 | [ch7 p.115](../sources/ch7.md) |

- $\bar{x}$ 是不偏的，因為 $E(\bar{x}) = \mu$（[ch7 p.45](../sources/ch7.md)）
- 一致性可以寫成 $\lim_{n \to \infty} V(\hat{\theta}) = 0$，例如 $\bar{x}$ 的變異數 $\sigma^2/n$ 在 n 趨近無限大時趨近 0（[notes p.22](../sources/notes.md)）
- $s^2$ 是 UMVUE（變異數最小的不偏估計量）（[ch7 p.20 手寫](../sources/ch7.md)），這也是樣本變異數分母用 $n-1$ 的結果，見[變異數與標準差](variance-and-standard-deviation.md)（UMVUE 的中文解釋為補充說明，非來源內容）

## 常見誤解

- 以為點估計值就是母體參數：樣本平均 1684 和母體平均 1697 並不相等（[ch7 p.31](../sources/ch7.md)），點估計量不可能提供母體參數的精確值，所以要用區間估計說明點估計值離母體參數有多近（[ch8 p.8、p.10](../sources/ch8.md)），見[信賴區間](confidence-interval.md)

## 相關概念

- [母體參數與樣本統計量](parameter-and-statistic.md)
- [隨機抽樣](random-sampling.md)
- [抽樣分配](sampling-distribution.md)：估計量是隨機變數，所以有自己的分配
- [標準誤差](standard-error.md)
- [信賴區間](confidence-interval.md)：點估計值是區間的中心

## 來源

- [ch7](../sources/ch7.md) p.19、p.20、p.24、p.28 到 31、p.45、p.109 到 115
- [ch3a](../sources/ch3a.md) p.4
- [ch8](../sources/ch8.md) p.8、p.10
- [notes](../sources/notes.md) p.19、p.22
