---
type: concept
sources: [ch3a, ch3b, ch7, ch8, notes]
updated: 2026-11-23
---

# 變異數與標準差（Variance and Standard Deviation）

## 定義

- **離均差（deviation about the mean）**：每筆資料 $x_i$ 與平均數的差（[ch3a p.44](../sources/ch3a.md)）
- **變異數（variance）**：離均差平方後的平均，用到全部資料來衡量變異程度（[ch3a p.44、p.45](../sources/ch3a.md)）
- **標準差（standard deviation）**：變異數的正平方根（[ch3a p.48](../sources/ch3a.md)）

## 直覺解釋

只看平均數不夠：選供應商時，兩家的平均交貨天數可能一樣，但其中一家的交貨天數忽長忽短，變異程度就是在量這種「穩不穩定」（[ch3a p.38](../sources/ch3a.md)）

## 公式

樣本與母體的變異數（[ch3a p.45](../sources/ch3a.md)）：

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1} \qquad \sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$

樣本與母體的標準差（[ch3a p.49](../sources/ch3a.md)）：

$$s = \sqrt{s^2} \qquad \sigma = \sqrt{\sigma^2}$$

樣本變異數也可以寫成 $s^2 = (\sum x_i^2 - n\bar{x}^2)/(n-1)$（[ch3a p.50](../sources/ch3a.md)、[notes p.5](../sources/notes.md)）

注意樣本變異數的分母是 $n-1$，不是 $n$，講義上特別用紅筆圈出（[ch3a p.45 手寫](../sources/ch3a.md)）

### 為什麼分母是 $n-1$：自由度

1. 變異數是離均差平方的平均（[ch3a p.45](../sources/ch3a.md)）
2. 離均差有一個限制：加總起來一定等於 0，例如班級人數的離均差 $2 + 10 + (-2) + 2 + (-12) = 0$（[ch3a p.46](../sources/ch3a.md)）
3. 所以只要知道其中 $n-1$ 個離均差，最後一個就被決定了，例如知道前四個是 2、10、−2、2，第五個一定是 −12（補充說明，非來源內容，數字取自 [ch3a p.46](../sources/ch3a.md)）
4. 真正能自由變動、提供資訊的離均差只有 $n-1$ 個；講義把自由度（degrees of freedom）定義為計算 $s$ 時用到的獨立資訊個數，樣本變異數的自由度是 $n-1$（[ch8 p.55、p.55 手寫](../sources/ch8.md)），所以平均時除以 $n-1$ 而不是 $n$
5. 會有這個限制，是因為我們先用同一份樣本算出 $\bar{x}$ 來代替不知道的 $\mu$，算 $\bar{x}$ 用掉了一個自由度（補充說明，非來源內容）

另外，用 $n-1$ 當分母的 $s^2$ 是 $\sigma^2$ 的 UMVUE，也就是變異數最小的不偏估計量（[ch7 p.20 手寫](../sources/ch7.md)），不偏的定義見[點估計](point-estimation.md)（[ch7 p.111](../sources/ch7.md)）

## 例子

5 個班級的人數為 46、54、42、46、32（[ch3a p.46](../sources/ch3a.md)）：

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 46 | 2 | 4 |
| 54 | 10 | 100 |
| 42 | −2 | 4 |
| 46 | 2 | 4 |
| 32 | −12 | 144 |
| 總和 | 0 | 256 |

$\bar{x} = 44$，所以 $s^2 = 256 / 4 = 64$，$s = 8$（[ch3a p.46](../sources/ch3a.md)、[ch3b p.10](../sources/ch3b.md)）

## 常見誤解

- 變異數的單位是原始資料單位的平方，例如 $s^2 = 49\ \text{cm}^2$（[ch3a p.4 手寫](../sources/ch3a.md)），所以通常改看標準差，它的單位和原始資料相同，比較好解釋（[ch3a p.48](../sources/ch3a.md)）

## 相關概念

- [平均數](mean.md)：變異數以平均數為基準
- [母體參數與樣本統計量](parameter-and-statistic.md)：$s^2$ 是 $\sigma^2$ 的點估計量
- [z-score](z-score.md)：用標準差當單位衡量資料的相對位置
- [標準誤差](standard-error.md)：$\bar{x}$ 的標準差
- [經驗法則](empirical-rule.md)：鐘形分配下，平均數 ±1、2、3 個標準差內有多少資料
- [符號對照表](notation.md)

## 矛盾與待確認

- **$s$ 和 $s^2$**（[notes p.19](../sources/notes.md)）：筆記寫成 $s = \sum(X_i - \bar{X})^2/(n-1)$，這個式子是 $s^2$，本頁採用 $s^2$（2026-11-23，已解決）
- **為什麼樣本變異數要除以 $n-1$**：講義只用紅筆強調，沒有解釋原因（[ch3a p.45](../sources/ch3a.md)），LLM 提出「估計偏小」和「自由度」兩種說明，使用者決定採用自由度的版本（2026-11-23，已解決），ingest ch8 後已補上自由度定義的引用（[ch8 p.55](../sources/ch8.md)）

## 來源

- [ch3a](../sources/ch3a.md) p.4、p.38、p.44 到 49
- [ch3b](../sources/ch3b.md) p.10
- [ch7](../sources/ch7.md) p.20、p.111
- [ch8](../sources/ch8.md) p.55
- [notes](../sources/notes.md) p.5、p.19
