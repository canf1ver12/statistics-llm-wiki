---
type: concept
sources: [ch8, ch7, notes]
updated: 2026-11-23
---

# 信賴區間（Confidence Interval）

## 定義

- 點估計量不可能提供母體參數的精確值，所以改在點估計值加減一個邊際誤差（margin of error），得到區間估計（[ch8 p.10](../sources/ch8.md)）
- 區間估計的目的是說明點估計值離母體參數有多近（[ch8 p.8、p.10](../sources/ch8.md)）
- σ 已知時，母體平均數 μ 的 $(1-\alpha)$ 信賴區間（[ch8 p.39](../sources/ch8.md)）：

$$\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$

- $1 - \alpha$ 叫做信賴係數（confidence coefficient），又稱信心度（[ch8 p.4 手寫、p.39](../sources/ch8.md)）
- $z_{\alpha/2}$ 是標準常態分配右尾面積為 $\alpha/2$ 的 z 值（[ch8 p.39](../sources/ch8.md)）

## 從中央極限定理到信賴區間

前提：$\bar{x}$ 要近似常態分配，這要靠中央極限定理，作答時一定要寫出來（[ch8 p.4 手寫](../sources/ch8.md)），見[中央極限定理](central-limit-theorem.md)

筆記把這個前提整理成一句：$\bar{X}$ 近似常態分配的條件是 $X \sim N(\mu, \sigma^2)$，或 n ≥ 30 by CLT（[notes p.24](../sources/notes.md)）

推導（[ch8 p.5 手寫、p.22 手寫](../sources/ch8.md)）：

1. $\bar{X}$ 近似 $N(\mu, \sigma^2/n)$，標準化後 $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ 是標準常態，兩尾各留 $\alpha/2$（[ch8 p.5 手寫](../sources/ch8.md)）：

$$P\left(-z_{\alpha/2}\frac{\sigma}{\sqrt{n}} < \bar{X} - \mu < z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha$$

2. 移項，把 μ 留在中間（[ch8 p.22 手寫](../sources/ch8.md)）：

$$P\left(\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} < \mu < \bar{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha$$

3. 代入資料得到區間 $\left(\bar{x} - z_{\alpha/2}\,\sigma/\sqrt{n},\ \bar{x} + z_{\alpha/2}\,\sigma/\sqrt{n}\right)$，上界跟下界不要寫反（[ch8 p.22 手寫](../sources/ch8.md)）

## 常用的 z 值

| 信賴水準 | $\alpha$ | $\alpha/2$ | $z_{\alpha/2}$ | 來源 |
|---|---|---|---|---|
| 90% | 0.10 | 0.05 | 1.645 | [ch8 p.40](../sources/ch8.md) |
| 95% | 0.05 | 0.025 | 1.960 | [ch8 p.40](../sources/ch8.md) |
| 99% | 0.01 | 0.005 | 2.576 | [ch8 p.40](../sources/ch8.md) |

以 95% 為例，$P(z < z_{0.025}) = 0.975$，查表得 1.96（[ch8 p.5 手寫](../sources/ch8.md)），查表方法見[標準常態分配與查表](standard-normal.md)

## 「95% 信賴」是什麼意思

- 用同樣的方法重複抽樣、建立很多個區間，其中有 95% 會包含 μ，所以對手上這一個區間說「有 95% 的信心它包含 μ」（[ch8 p.36、p.38](../sources/ch8.md)）
- 每個樣本算出的區間都不一樣，有的包含 μ、有的不包含（[ch8 p.15](../sources/ch8.md)、[ch8 p.4 手寫](../sources/ch8.md)）
- 95% 指的是「這個方法」的成功率：抽樣之前，$P(|\bar{X} - \mu| \le E) = 1 - \alpha$ 是會發生的機率（[ch8 p.4 手寫](../sources/ch8.md)）

## 例子：Lloyd's 百貨

每週抽 100 位顧客，根據歷史資料假設 σ = 20（[ch8 p.9](../sources/ch8.md)）

1. 標準誤差 $\sigma_{\bar{x}} = 20/\sqrt{100} = 2$，邊際誤差 $1.96 \times 2 = 3.92$（[ch8 p.31](../sources/ch8.md)）
2. 最近一週 $\bar{x} = 82$，95% 信賴區間為 78.08 到 85.92（[ch8 p.37](../sources/ch8.md)）
3. 解讀：有 95% 的信心 78.08 到 85.92 包含所有顧客的平均花費 μ（[ch8 p.38](../sources/ch8.md)）

同一份資料換成不同信賴水準（[ch8 p.44](../sources/ch8.md)，講義標題誤標為 Discount Sounds，已更正）：

| 信賴水準 | 邊際誤差 | 信賴區間 |
|---|---|---|
| 90% | 3.29 | 78.71 到 85.29 |
| 95% | 3.92 | 78.08 到 85.92 |
| 99% | 5.15 | 76.85 到 87.15 |

## 例子：Discount Sounds

新分店商圈的家戶年所得，n = 36、$\bar{x}$ = 41,100、σ 估計為 4,500，母體不太偏斜（[ch8 p.41](../sources/ch8.md)）：

- 邊際誤差 $1.96 \times 4{,}500/\sqrt{36} = 1{,}470$（[ch8 p.42](../sources/ch8.md)）
- 95% 信賴區間為 39,630 到 42,570（[ch8 p.43](../sources/ch8.md)）

## 什麼時候可以用

- 多數應用 n = 30 就夠，母體高度偏斜或有離群值時建議 n ≥ 50（[ch8 p.45](../sources/ch8.md)）
- σ 已知時用 z（[ch8 p.74](../sources/ch8.md)）
- σ 未知、n < 30，而且母體是常態或不嚴重偏離常態時，用樣本標準差 s 估計 σ，改用 t 分配：$\bar{x} \pm t_{\alpha/2}(n-1)\,s/\sqrt{n}$（[ch8 p.53、p.74](../sources/ch8.md)、[notes p.26、p.27](../sources/notes.md)）
- σ 未知但 n ≥ 30 時，用 $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$，因為 n 很大時 t 分配近似標準常態（[notes p.26](../sources/notes.md)、[ch8 p.56](../sources/ch8.md)），這是使用者採用的做法，和講義的差異見矛盾與待確認
- t 分配比標準常態矮胖，自由度越大越陡（[notes p.26](../sources/notes.md)、[ch8 p.56](../sources/ch8.md)），本輪不展開

## 常見誤解

- 說「μ 有 95% 的機率落在 78.08 到 85.92 之間」：講義的說法是「用這個方法建立的區間有 95% 會包含 μ，所以有 95% 的信心這個區間包含 μ」（[ch8 p.38](../sources/ch8.md)）；μ 是固定的數字（[ch3a p.4 手寫](../sources/ch3a.md)），會變的是區間（[ch8 p.15](../sources/ch8.md)）
- 以為信賴水準越高越好：信賴水準越高，區間越寬（[ch8 p.44](../sources/ch8.md)），見[邊際誤差與樣本數](margin-of-error.md)
- 忘記寫出 $\bar{x}$ 近似常態的理由：要說明是根據中央極限定理（[ch8 p.4 手寫](../sources/ch8.md)）

## 相關概念

- [中央極限定理](central-limit-theorem.md)：信賴區間的前提
- [標準誤差](standard-error.md)：$\sigma/\sqrt{n}$
- [邊際誤差與樣本數](margin-of-error.md)
- [標準常態分配與查表](standard-normal.md)：找 $z_{\alpha/2}$
- [點估計](point-estimation.md)：區間的中心
- [經驗法則](empirical-rule.md)
- [符號對照表](notation.md)

## 矛盾與待確認

- **σ 未知且 n ≥ 30 時用 z 還是 t**（[notes p.26](../sources/notes.md)、[ch8 p.60、p.74](../sources/ch8.md)）：筆記的做法是 n ≥ 30 改用 z；講義是 σ 未知一律用 t，並寫「自由度超過 100 時，z 才是 t 的好近似」，使用者決定採用筆記的做法，理由是 n ≥ 30 的意思大約是 n 趨近無限大（2026-11-23，使用者決定，講義的說法保留在此供參考）
- **$z_{0.005}$ 是 2.575 還是 2.576**（[ch8 p.5、p.40](../sources/ch8.md)）：使用者手寫 2.575，講義表格 2.576，使用者決定採用 2.576（2026-11-23，已解決）
- **p.44 的標題**（[ch8 p.44](../sources/ch8.md)）：講義標成 Discount Sounds，數字屬於 Lloyd's，依講義筆誤規則直接更正（2026-11-23，已解決）

## 來源

- [ch8](../sources/ch8.md) p.4、p.5、p.8 到 10、p.15、p.22、p.31、p.36 到 45、p.53、p.74
- [ch3a](../sources/ch3a.md) p.4
- [notes](../sources/notes.md) p.24 到 27
