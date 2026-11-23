---
type: concept
sources: [ch7, notes]
updated: 2026-11-23
---

# 抽樣分配（Sampling Distribution）

## 定義

$\bar{x}$ 的抽樣分配是樣本平均數 $\bar{x}$ 所有可能值的機率分配（[ch7 p.45](../sources/ch7.md)）

## 直覺解釋

- 抽到的人不一樣，算出來的 $\bar{x}$ 就不一樣，所以 $\bar{x}$ 是隨機變數，會有自己的分配（[ch7 p.19 手寫](../sources/ch7.md)）
- 要分清楚三種分配：母體的分配（每個人的數值）、一組樣本資料的分配（這 30 個人的數值）、抽樣分配（很多組樣本各自算出的 $\bar{x}$）（補充說明，非來源內容）

## 示範：EAI 公司抽 500 次

- EAI 公司從 2,500 位經理中抽 30 人算 $\bar{x}$，重複 500 次，得到 500 個 $\bar{x}$（[ch7 p.35](../sources/ch7.md)）
- 500 個 $\bar{x}$ 的相對次數直方圖呈鐘形，大約落在 50,000 到 54,000 之間（[ch7 p.37](../sources/ch7.md)）
- 看直方圖時注意三件事：是否對稱、500 個 $\bar{x}$ 的平均值 $E(\bar{X})$、500 個 $\bar{x}$ 的變異數 $V(\bar{X})$（[ch7 p.34 手寫](../sources/ch7.md)）
- 筆記補充：隨著 n 增加，標準誤差會變小（[notes p.20](../sources/notes.md)）
- 實務上只會抽一個樣本，重複 500 次只是為了示範不同樣本會產生不同的 $\bar{x}$（[ch7 p.42](../sources/ch7.md)）

## 期望值與變異數

$$E(\bar{x}) = \mu \qquad \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

（[ch7 p.45、p.47](../sources/ch7.md)）

推導（[ch7 p.38 手寫](../sources/ch7.md)），前提是 $X_1, \dots, X_n$ 為 iid，每個 $X_i \sim (\mu, \sigma^2)$（[ch7 p.48 手寫、p.64 手寫](../sources/ch7.md)）：

$$E(\bar{X}) = \frac{1}{n}\left[E(X_1) + \dots + E(X_n)\right] = \frac{n\mu}{n} = \mu$$

$$V(\bar{X}) = \frac{1}{n^2}\left[V(X_1) + \dots + V(X_n)\right] = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$$

- $E(\bar{x}) = \mu$ 代表 $\bar{x}$ 是 $\mu$ 的不偏估計量（[ch7 p.45](../sources/ch7.md)）
- $\sigma_{\bar{x}}$ 叫做標準誤差，詳見[標準誤差](standard-error.md)（[ch7 p.47](../sources/ch7.md)）
- 抽樣分配的形狀由[中央極限定理](central-limit-theorem.md)決定（[ch7 p.53](../sources/ch7.md)）

## 抽樣分配的用途：算出 $\bar{x}$ 離 $\mu$ 有多近的機率

$\bar{x}$ 的抽樣分配可以提供「$\bar{x}$ 離 $\mu$ 有多近」的機率資訊（[ch7 p.52](../sources/ch7.md)）

EAI 的例子：$E(\bar{x}) = 51{,}800$、$\sigma_{\bar{x}} = 730.3$（[ch7 p.57](../sources/ch7.md)），抽 30 人時 $\bar{x}$ 落在 μ ± 500 之內的機率（[ch7 p.58 到 62](../sources/ch7.md)）：

$$P(51{,}300 \le \bar{x} \le 52{,}300) = P(-0.68 \le z \le 0.68) = 0.7517 - 0.2483 = 0.5034$$

筆記的寫法：根據中央極限定理 $\bar{X} \sim N(51800, 4000^2/30)$，標準化成 $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ 再查表（[notes p.21](../sources/notes.md)）

也就是說，有 0.4966 的機率 $\bar{x}$ 和 μ 差超過 500（[ch7 p.62](../sources/ch7.md)）

## 抽樣誤差

- 抽樣誤差是隨機抽樣造成的樣本與母體的差異，n 越大抽樣誤差越小（[ch7 p.138](../sources/ch7.md)）
- 抽樣誤差來自抽到的人不一樣，造成 $\bar{x}$ 不一樣（[ch7 p.59 手寫](../sources/ch7.md)）
- 非抽樣誤差不是隨機抽樣造成的，例如涵蓋誤差、無反應誤差、測量誤差，樣本再大也無法消除（[ch7 p.139](../sources/ch7.md)；「樣本再大也無法消除」為補充說明，非來源內容）

## 常見誤解

- 以為實務上要抽很多次樣本：實際上只抽一次，抽樣分配是理論上「如果重複抽很多次」會得到的分配（[ch7 p.42](../sources/ch7.md)）

## 相關概念

- [隨機抽樣](random-sampling.md)：iid 是推導的前提
- [點估計](point-estimation.md)
- [中央極限定理](central-limit-theorem.md)
- [標準誤差](standard-error.md)
- [標準常態分配與查表](standard-normal.md)：用來算 $\bar{x}$ 落在某區間的機率
- [符號對照表](notation.md)

## 矛盾與待確認

- **推導中 $X_i$ 的分配**（[ch7 p.38](../sources/ch7.md)）：使用者手寫寫成 $X_i \sim N(\mu, \sigma_{\bar{x}}^2)$，本頁採用 $X_i \sim (\mu, \sigma^2)$，使用者已同意（2026-11-23，已解決）

## 來源

- [ch7](../sources/ch7.md) p.19、p.34、p.35、p.37、p.38、p.42、p.45、p.47、p.48、p.52、p.53、p.57 到 64、p.138、p.139
- [notes](../sources/notes.md) p.20、p.21
