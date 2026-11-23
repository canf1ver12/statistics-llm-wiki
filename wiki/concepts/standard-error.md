---
type: concept
sources: [ch7, notes]
updated: 2026-11-23
---

# 標準誤差（Standard Error）

## 定義

- $\sigma_{\bar{x}}$ 是 $\bar{x}$ 的標準差，叫做平均數的標準誤差（standard error of the mean）（[ch7 p.46、p.47](../sources/ch7.md)）
- 母體為無限母體，或有限母體但 $n/N \le 0.05$ 時（[ch7 p.47、p.49](../sources/ch7.md)）：

$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

- 有限母體且 $n/N > 0.05$ 時，要乘上有限母體校正因子 $\sqrt{(N-n)/(N-1)}$（[ch7 p.47](../sources/ch7.md)），本輪不展開

## 直覺解釋

- 母體標準差 $\sigma$ 描述的是每個人的數值有多分散，標準誤差 $\sigma_{\bar{x}}$ 描述的是 $\bar{x}$ 有多分散（[ch7 p.46](../sources/ch7.md)）
- 樣本數越大，標準誤差越小（[ch7 p.67](../sources/ch7.md)），$\bar{x}$ 的分配越陡、越集中在 $\mu$ 附近（[ch7 p.63 手寫](../sources/ch7.md)）
- 所以 $\sigma_{\bar{x}} < \sigma$，$\bar{x}$ 的曲線比母體的曲線更窄更陡（[notes p.21](../sources/notes.md)）
- 因為分母是 $\sqrt{n}$，樣本數變成 4 倍，標準誤差才會減半（補充說明，非來源內容）

## 例子：EAI 公司，n = 30 和 n = 100

母體標準差 $\sigma = 4{,}000$，問 $\bar{x}$ 落在 μ ± 500 之內的機率（[ch7 p.50、p.58](../sources/ch7.md)）：

| | n = 30 | n = 100 | 來源 |
|---|---|---|---|
| $E(\bar{x})$ | 51,800 | 51,800，不受樣本數影響 | [ch7 p.57、p.66](../sources/ch7.md) |
| 標準誤差 | $4{,}000/\sqrt{30} = 730.3$ | $4{,}000/\sqrt{100} = 400$ | [ch7 p.50、p.67](../sources/ch7.md) |
| $P(51{,}300 \le \bar{x} \le 52{,}300)$ | 0.5034 | 0.7888 | [ch7 p.62、p.68](../sources/ch7.md) |

EAI 的 $n/N = 30/2{,}500 = 0.012 \le 0.05$，所以可以直接用 $\sigma/\sqrt{n}$（[ch7 p.50](../sources/ch7.md)，講義筆誤已更正）

## 例子：SAT 成績，n = 30 和 n = 100

母體標準差 $\sigma = 87.4$，問 $\bar{x}$ 落在 1687 到 1707（μ ± 10）的機率（[ch7 p.69、p.70](../sources/ch7.md)）：

| | n = 30 | n = 100 | 來源 |
|---|---|---|---|
| 標準誤差 | $87.4/\sqrt{30} = 15.96$ | 8.2（使用有限母體校正） | [ch7 p.69、p.77](../sources/ch7.md) |
| $P(1687 \le \bar{x} \le 1707)$ | $P(-0.63 \le z \le 0.63) = 0.4714$ | 0.7776 | [ch7 p.72、p.75、p.79](../sources/ch7.md) |

n = 30 那欄的 z 值，講義 p.75 誤寫成 ±0.68，已依 p.72 更正為 ±0.63（[ch7 p.72、p.75](../sources/ch7.md)）

## 例子：巨量資料下的標準誤差

s = 20 時，樣本數和標準誤差的關係（[ch7 p.140](../sources/ch7.md)）：

| n | 10 | 10,000 | 1,000,000 | 100,000,000 | 1,000,000,000 |
|---|---|---|---|---|---|
| 標準誤差 | 6.32456 | 0.2 | 0.02 | 0.002 | 0.00063 |

## 常見誤解

- 把標準誤差和標準差搞混：$\sigma$ 是母體的標準差，$\sigma_{\bar{x}}$ 是 $\bar{x}$ 的標準差（[ch7 p.46](../sources/ch7.md)）
- 把變異數 $\sigma^2/n$ 當成標準誤差：$\sigma^2/n$ 是 $\bar{X}$ 的變異數（[ch7 p.38 手寫](../sources/ch7.md)），標準誤差要開根號，是 $\sigma/\sqrt{n}$（[ch7 p.47](../sources/ch7.md)）；使用者的筆記就犯了這個錯（[notes p.20](../sources/notes.md)），筆記另一頁也提醒自己「標準化的時候 $\sigma^2$ 要記得開根號」（[notes p.19](../sources/notes.md)）
- 以為樣本夠大就沒有誤差：樣本再大只能縮小抽樣誤差，非抽樣誤差仍然存在（[ch7 p.138、p.139](../sources/ch7.md)）

## 相關概念

- [抽樣分配](sampling-distribution.md)
- [中央極限定理](central-limit-theorem.md)
- [邊際誤差與樣本數](margin-of-error.md)：邊際誤差 = $z_{\alpha/2}$ × 標準誤差
- [變異數與標準差](variance-and-standard-deviation.md)
- [符號對照表](notation.md)

## 矛盾與待確認

- **筆記把 $\sigma^2/n$ 標成標準誤差**（[notes p.20、p.22](../sources/notes.md)）：講義（[ch7 p.47](../sources/ch7.md)）和使用者在講義上的手寫（[ch7 p.63](../sources/ch7.md)）都是 $\sigma/\sqrt{n}$，本頁採用 $\sigma/\sqrt{n}$，筆記的寫法收進常見誤解（2026-11-23，已解決）
- **講義筆誤**（[ch7 p.50、p.75](../sources/ch7.md)）：p.50 的 0.112 更正為 0.012，p.75 的 ±0.68 更正為 ±0.63，使用者決定顯示更正後的值（2026-11-23，已解決）

## 來源

- [ch7](../sources/ch7.md) p.38、p.46、p.47、p.49、p.50、p.57、p.62、p.63、p.66 到 69、p.72、p.75、p.77、p.79、p.138 到 140
- [notes](../sources/notes.md) p.19 到 22
