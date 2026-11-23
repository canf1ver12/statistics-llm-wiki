---
type: concept
sources: [ch8, notes]
updated: 2026-11-23
---

# 邊際誤差與樣本數（Margin of Error and Sample Size）

## 定義

邊際誤差 E 是信賴區間「點估計值 ± E」裡加減的那一段（[ch8 p.10](../sources/ch8.md)），σ 已知時（[ch8 p.6 手寫、p.28](../sources/ch8.md)）：

$$E = z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$

區間寬度 = 上界 − 下界 = $2E$（[ch8 p.23 手寫](../sources/ch8.md)）

## 影響區間寬度的三個因素

| 因素 | 變化 | 邊際誤差和區間寬度 | 來源 |
|---|---|---|---|
| 信賴水準 $1 - \alpha$ | 越高 | 越大、越寬 | [ch8 p.44](../sources/ch8.md) |
| 樣本數 n | 越大 | 越小、越窄 | [ch8 p.24 手寫](../sources/ch8.md) |
| 母體標準差 σ | 越大 | 越大、越寬 | 補充說明，非來源內容，由公式 [ch8 p.28](../sources/ch8.md) 推得 |

- 信賴係數一樣時，n 大區間窄比較好，n 小區間寬（[ch8 p.24 手寫](../sources/ch8.md)、[notes p.25](../sources/notes.md)）
- 想要更高的信心，就要接受更寬的區間（[ch8 p.44](../sources/ch8.md)）

## 例子：Lloyd's 的三種信賴水準

σ = 20、n = 100，標準誤差為 2（[ch8 p.9、p.31](../sources/ch8.md)）：

| 信賴水準 | $z_{\alpha/2}$ | 邊際誤差 |
|---|---|---|
| 90% | 1.645 | 3.29 |
| 95% | 1.960 | 3.92 |
| 99% | 2.576 | 5.15 |

z 值取自 [ch8 p.40](../sources/ch8.md)，邊際誤差取自 [ch8 p.44](../sources/ch8.md)

## 反過來算樣本數

由 $E = z_{\alpha/2}\sigma/\sqrt{n}$ 移項（[ch8 p.28](../sources/ch8.md)、[ch8 p.24 手寫](../sources/ch8.md)）：

$$n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2$$

- 例：95% 信賴、σ = 9.65、希望邊際誤差為 2，$n = (1.96 \times 9.65/2)^2 = 89.43$，取 n = 90（[ch8 p.29](../sources/ch8.md)）
- n 有小數時要無條件進位，不能四捨五入，否則邊際誤差會超過目標（[ch8 p.29 手寫](../sources/ch8.md)、[notes p.25](../sources/notes.md)；「否則邊際誤差會超過目標」為補充說明，非來源內容）
- 例：n = 100、95% 信賴、σ = 9.65，邊際誤差 $E = 1.96 \times 9.65/\sqrt{100} = 1.89$（[ch8 p.30](../sources/ch8.md)，講義筆誤已更正）

## 常見誤解

- 把邊際誤差公式寫成 $(z\sigma/n)^2$：那是把樣本數公式和邊際誤差公式混在一起，邊際誤差是 $z\sigma/\sqrt{n}$，不用平方（[ch8 p.30](../sources/ch8.md)，講義本身在這裡算錯，已更正）

## 相關概念

- [信賴區間](confidence-interval.md)
- [標準誤差](standard-error.md)：邊際誤差 = $z_{\alpha/2}$ × 標準誤差
- [標準常態分配與查表](standard-normal.md)
- [符號對照表](notation.md)

## 矛盾與待確認

- **p.30 講義筆誤**（[ch8 p.30](../sources/ch8.md)）：講義寫 $E = (1.96 \times 9.65/100)^2 = 0.03577$，依同頁公式更正為 1.89，依講義筆誤規則直接更正（2026-11-23，已解決）

## 來源

- [ch8](../sources/ch8.md) p.6、p.9、p.10、p.23、p.24、p.28 到 31、p.40、p.44
- [notes](../sources/notes.md) p.25
