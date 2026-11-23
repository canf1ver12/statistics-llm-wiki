---
type: concept
sources: [ch3a, ch7]
updated: 2026-11-23
---

# 母體參數與樣本統計量（Population Parameter and Sample Statistic）

## 定義

- **母體參數（population parameter）**：用母體資料算出來的量數，例如母體平均數 $\mu$、母體變異數 $\sigma^2$（[ch3a p.4](../sources/ch3a.md)）
- **樣本統計量（sample statistic）**：用樣本資料算出來的量數，例如樣本平均數 $\bar{x}$、樣本變異數 $s^2$（[ch3a p.4](../sources/ch3a.md)）
- **點估計量（point estimator）**：樣本統計量被當作對應母體參數的點估計量（[ch3a p.4](../sources/ch3a.md)）

## 直覺解釋

我們抽樣是為了回答關於母體的問題，但樣本只包含母體的一部分，所以樣本統計量只能提供母體參數的估計值（[ch7 p.7](../sources/ch7.md)）

## 點估計的對應

| 母體參數 | 點估計量 | 來源 |
|---|---|---|
| 母體平均數 $\mu$ | 樣本平均數 $\bar{x}$ | [ch3a p.4 手寫、p.5](../sources/ch3a.md) |
| 母體變異數 $\sigma^2$ | 樣本變異數 $s^2$ | [ch3a p.4 手寫](../sources/ch3a.md) |

## 大寫與小寫

- 大寫的 $\bar{X}$ 是數學式，也就是隨機變數；小寫的 $\bar{x}$ 是把資料代入數學式後算出來的統計量的值（[ch3a p.4 手寫](../sources/ch3a.md)）
- 母體參數要有所有母體資料才算得出來，而且是固定的數字（[ch3a p.4 手寫](../sources/ch3a.md)）
- 母體參數固定不變，樣本統計量則會隨抽到的樣本而改變，因為抽到的人不一樣，這就是[抽樣分配](sampling-distribution.md)要討論的事（[ch7 p.19 手寫、p.29](../sources/ch7.md)）
- 大寫的 $\bar{X}$ 叫估計量，小寫的 $\bar{x}$ 叫點估計值，詳見[點估計](point-estimation.md)（[ch7 p.19 手寫](../sources/ch7.md)）

## 常見誤解

- 把樣本統計量當成母體參數本身：$\bar{x}$ 只是 $\mu$ 的點估計量，不等於 $\mu$（[ch3a p.4](../sources/ch3a.md)）

## 相關概念

- [平均數](mean.md)
- [變異數與標準差](variance-and-standard-deviation.md)
- [隨機抽樣](random-sampling.md)
- [點估計](point-estimation.md)
- [抽樣分配](sampling-distribution.md)
- [符號對照表](notation.md)

## 來源

- [ch3a](../sources/ch3a.md) p.4、p.5
- [ch7](../sources/ch7.md) p.7、p.19、p.29
