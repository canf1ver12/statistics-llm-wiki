---
type: concept
sources: [ch7, notes]
updated: 2026-11-23
---

# 隨機抽樣（Random Sampling）

## 定義

- **母體（population）**：所有感興趣元素的集合（[ch7 p.6](../sources/ch7.md)）
- **樣本（sample）**：母體的子集合（[ch7 p.6](../sources/ch7.md)）
- **抽樣框（frame）**：抽樣時使用的元素清單（[ch7 p.6](../sources/ch7.md)）
- **簡單隨機樣本（simple random sample）**：從大小為 N 的有限母體抽出大小為 n 的樣本，每一個可能的樣本被抽中的機率都相同（[ch7 p.10](../sources/ch7.md)）
- **無限母體的隨機樣本**：每個元素都來自感興趣的母體，而且每個元素獨立選取（[ch7 p.18](../sources/ch7.md)）

## 為什麼要抽樣

- 抽樣的目的是收集資料，回答關於母體的研究問題（[ch7 p.7](../sources/ch7.md)）
- 樣本只包含母體的一部分，所以樣本結果只能提供母體特性的估計值；用適當的抽樣方法，可以得到好的估計（[ch7 p.7](../sources/ch7.md)）
- 抽樣一定存在誤差，有代表性的樣本誤差比較小，樣本不夠多誤差比較大（[ch7 p.7 手寫](../sources/ch7.md)）
- 筆記整理成：適當的抽樣方法有好的母體估計（[notes p.18](../sources/notes.md)）

## iid：獨立同分布

- 隨機樣本裡的 $X_1, X_2, \dots, X_n$ 互相獨立，而且每個 $X_i$ 都和母體同分配，簡稱 iid（[ch7 p.48 手寫、p.64 手寫](../sources/ch7.md)）
- 筆記把簡單隨機抽樣整理成三點：每個樣本被選到的機率一樣、來自同一個母體同一個分配、每個被選的都獨立（[notes p.19](../sources/notes.md)）
- 例子：要量全校同學的身高，在量之前，每個被抽到的 $X_i$ 都和母體同分配，身高都在母體的範圍內（[ch7 p.64 手寫](../sources/ch7.md)）
- 也就是 $X_i \sim (\mu, \sigma^2)$，每個 $X_i$ 的平均數和變異數都和母體一樣（[ch7 p.38 手寫、p.64 手寫](../sources/ch7.md)）

## 例子

- EAI 公司有 2,500 位經理，沒有全部的資料，改抽 30 位當樣本（[ch7 p.8](../sources/ch7.md)）
- 把經理編號 1 到 2,500，再用亂數表選出樣本（[ch7 p.13](../sources/ch7.md)）

## 常見誤解

- 以為隨便找身邊的人就是隨機樣本：講義建議使用機率抽樣，因為只有機率抽樣能評估樣本結果有多接近母體參數，便利抽樣和判斷抽樣無法評估（[ch7 p.135](../sources/ch7.md)）
- 以為只要樣本夠大就好：目標母體和實際抽樣的母體也要一致（[ch7 p.32](../sources/ch7.md)）

## 相關概念

- [母體參數與樣本統計量](parameter-and-statistic.md)
- [點估計](point-estimation.md)
- [抽樣分配](sampling-distribution.md)：iid 是推導抽樣分配的前提

## 矛盾與待確認

- **每個 $X_i$ 的分配**（[ch7 p.38](../sources/ch7.md)）：使用者手寫把 $X_i$ 的分配寫成 $N(\mu, \sigma_{\bar{x}}^2)$，與 p.64 手寫「每個 $X_i$ 都跟母體同分配」不一致，本頁採用 $X_i \sim (\mu, \sigma^2)$，使用者已同意（2026-11-23，已解決）

## 來源

- [ch7](../sources/ch7.md) p.6 到 8、p.10、p.13、p.18、p.32、p.38、p.48、p.64、p.135
- [notes](../sources/notes.md) p.18、p.19
