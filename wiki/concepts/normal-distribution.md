---
type: concept
sources: [ch6, notes]
updated: 2026-11-23
---

# 常態分配（Normal Distribution）

## 定義

- 常態分配是描述連續型隨機變數最重要的分配，廣泛用在統計推論（[ch6 p.14](../sources/ch6.md)）
- 整個常態分配家族由平均數 $\mu$ 和標準差 $\sigma$ 決定（[ch6 p.19](../sources/ch6.md)），記為 $X \sim N(\mu, \sigma^2)$，其中 $E(X) = \mu$、$V(X) = \sigma^2$（[ch6 p.15 手寫](../sources/ch6.md)）

## 先備觀念：連續型的機率是面積

- 隨機變數落在 $x_1$ 到 $x_2$ 之間的機率，是曲線在 $x_1$ 到 $x_2$ 之間的面積（[ch6 p.5](../sources/ch6.md)）
- 單一點是寬度為 0 的區間，所以剛好等於某個值的機率為 0（[ch6 p.4](../sources/ch6.md)）
- 因此對連續型隨機變數來說，有沒有等號機率都一樣，$P(X < a) = P(X \le a)$，但離散型的等號會影響機率（[ch6 p.24 手寫](../sources/ch6.md)）

## 特性

- 對稱，偏態為 0（[ch6 p.18](../sources/ch6.md)）
- 最高點在平均數，平均數 = 中位數 = 眾數（[ch6 p.20](../sources/ch6.md)）
- 平均數可以是任何數值，決定曲線的位置（[ch6 p.21](../sources/ch6.md)）
- 標準差決定曲線的寬度，標準差越大，曲線越寬越扁（[ch6 p.22](../sources/ch6.md)）
- 曲線下總面積為 1，平均數左右各 0.5（[ch6 p.23](../sources/ch6.md)）
- $\sigma$ 在圖上就是從 $\mu$ 到反曲點的水平距離（[ch6 p.15 手寫](../sources/ch6.md)）
- μ 決定位置、σ 決定寬度：變異數一樣但 μ 不一樣時曲線左右平移，μ 一樣但變異數不一樣時曲線變寬或變窄（[notes p.13](../sources/notes.md)）
- 常態分配是經驗法則的基礎，見[經驗法則](empirical-rule.md)（[ch6 p.27](../sources/ch6.md)）

## 常見的例子

身高、考試成績、雨量、科學測量（[ch6 p.14](../sources/ch6.md)）

## 一般常態分配要怎麼算機率

一般常態分配不能直接查表，要先標準化成標準常態分配（[ch6 p.13 手寫、p.15 手寫](../sources/ch6.md)），見[標準常態分配與查表](standard-normal.md)

## 常見誤解

- 以為曲線的高度就是機率：連續型的機率是面積，不是高度，單一點的機率為 0（[ch6 p.4、p.5](../sources/ch6.md)）；$f(x)$ 是曲線高度的數學式，不是機率（[notes p.13](../sources/notes.md)）

## 相關概念

- [標準常態分配與查表](standard-normal.md)
- [經驗法則](empirical-rule.md)
- [分配形狀與偏態](distribution-shape.md)：常態分配是對稱分配
- [平均數](mean.md)、[變異數與標準差](variance-and-standard-deviation.md)
- [符號對照表](notation.md)

## 矛盾與待確認

- **機率是高度還是面積**（[notes p.13](../sources/notes.md)、[ch6 p.2 手寫](../sources/ch6.md)）：手寫寫「連續隨機變數不能算特定值機率，而是算高度」，但機率是曲線下的面積（[ch6 p.5](../sources/ch6.md)），本頁改為「不能算特定值的機率，要算區間的面積，$f(x)$ 是高度的數學式」（2026-11-23，已解決）

## 來源

- [ch6](../sources/ch6.md) p.4、p.5、p.13 到 15、p.18 到 24、p.27
- [notes](../sources/notes.md) p.13
