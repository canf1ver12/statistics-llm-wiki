---
type: concept
sources: [ch7, ch8, notes]
updated: 2026-11-23
---

# 中央極限定理（Central Limit Theorem, CLT）

## 定義

從母體抽出大小為 n 的隨機樣本，當樣本數變大時，樣本平均數 $\bar{x}$ 的抽樣分配可以用常態分配近似（[ch7 p.53](../sources/ch7.md)）

$$\text{當 } n \text{ 夠大時，} \quad \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

（[ch7 p.54 手寫](../sources/ch7.md)）

## 為什麼需要它

- 只知道 $X \sim (\mu, \sigma^2)$ 時，雖然知道 $\bar{X}$ 的平均數是 $\mu$、變異數是 $\sigma^2/n$，但不知道是什麼分配，就不能推論（[ch7 p.54 手寫](../sources/ch7.md)）；筆記的說法是「X 不知道分配時，$\bar{X}$ 也不知道分配，無法推論」（[notes p.21](../sources/notes.md)）
- 母體不是常態分配時，中央極限定理告訴我們 $\bar{x}$ 抽樣分配的形狀（[ch7 p.53](../sources/ch7.md)）
- 知道 $\bar{x}$ 近似常態後，就能算出 $\bar{x}$ 離 $\mu$ 有多近的機率（[ch7 p.52](../sources/ch7.md)），見[抽樣分配](sampling-distribution.md)

## 樣本要多大才夠

| 母體的情況 | 樣本數 | 來源 |
|---|---|---|
| 母體本身是常態分配 | 任何樣本數，$\bar{x}$ 都是常態 | [ch7 p.51](../sources/ch7.md)、[notes p.20](../sources/notes.md) |
| 多數應用 | n ≥ 30 | [ch7 p.51](../sources/ch7.md) |
| 母體高度偏斜或有離群值 | 可能需要 n = 50 | [ch7 p.51](../sources/ch7.md)、[ch8 p.45](../sources/ch8.md) |
| 母體至少近似常態 | n 小於 15 也可以 | [ch8 p.46](../sources/ch8.md) |
| 不是常態但大致對稱 | n = 15 就夠 | [ch8 p.46](../sources/ch8.md) |

## 圖解：三種母體

講義用三種形狀很不一樣的母體示範（[ch7 p.55、p.56](../sources/ch7.md)）：

| 樣本數 | 均勻母體 | V 字形母體 | 右偏母體 | 來源 |
|---|---|---|---|---|
| 母體本身 | 平的 | 兩邊高、中間低 | 左邊高、往右拖長尾巴 | [ch7 p.55](../sources/ch7.md) |
| n = 2 | 三角形 | 中間凸起、兩邊還有小峰 | 仍然右偏 | [ch7 p.55](../sources/ch7.md) |
| n = 5 | 接近鐘形 | 接近鐘形 | 仍略微右偏 | [ch7 p.56](../sources/ch7.md) |
| n = 30 | 鐘形且很窄 | 鐘形且很窄 | 鐘形且很窄 | [ch7 p.56](../sources/ch7.md) |

從圖可以看出兩件事：右偏母體需要比較大的 n 才會變成鐘形，和 p.51 說偏斜母體可能要 n = 50 一致；n 越大，曲線越窄，因為標準誤差 $\sigma/\sqrt{n}$ 變小（補充說明，非來源內容，依據 [ch7 p.51、p.55、p.56](../sources/ch7.md)）

## 常見誤解

- 以為中央極限定理是說「樣本夠大，資料就會變成常態」：定理講的是樣本平均數 $\bar{x}$ 的抽樣分配（[ch7 p.53](../sources/ch7.md)），母體和樣本資料本身的形狀不會改變（補充說明，非來源內容）
- 以為 n ≥ 30 永遠夠用：母體高度偏斜或有離群值時可能要 n = 50（[ch7 p.51](../sources/ch7.md)）

## 相關概念

- [抽樣分配](sampling-distribution.md)
- [標準誤差](standard-error.md)
- [常態分配](normal-distribution.md)
- [分配形狀與偏態](distribution-shape.md)：母體越偏，需要的樣本數越大
- [信賴區間](confidence-interval.md)：信賴區間要先靠中央極限定理說明 $\bar{x}$ 近似常態

## 矛盾與待確認

- **n ≥ 30 還是 25**（[ch7 p.39、p.51](../sources/ch7.md)）：使用者手寫「n ≥ 30（or 25）」，講義正文寫 n ≥ 30，偏斜時 n = 50，使用者決定採用講義的說法（2026-11-23，已解決）

## 來源

- [ch7](../sources/ch7.md) p.39、p.51 到 56
- [ch8](../sources/ch8.md) p.45、p.46
- [notes](../sources/notes.md) p.20、p.21
