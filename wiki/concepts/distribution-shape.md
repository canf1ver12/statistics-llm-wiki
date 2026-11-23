---
type: concept
sources: [ch3b, ch7, notes]
updated: 2026-11-23
---

# 分配形狀與偏態（Distribution Shape and Skewness）

## 定義

偏態（skewness）是衡量分配形狀的重要量數，可以用統計軟體計算（[ch3b p.3](../sources/ch3b.md)）

## 三種形狀

| 形狀 | 偏態 | 平均數與中位數 | 眾數、中位數、平均數 | 來源 |
|---|---|---|---|---|
| 左偏 | 負 | 平均數通常小於中位數 | 眾數 > 中位數 > 平均數 | [ch3b p.4、p.34](../sources/ch3b.md) |
| 對稱 | 0 | 平均數等於中位數 | 三者相等 | [ch3b p.4、p.34](../sources/ch3b.md) |
| 右偏 | 正，高度右偏時常大於 1.0 | 平均數通常大於中位數 | 眾數 < 中位數 < 平均數 | [ch3b p.4、p.34](../sources/ch3b.md) |

## 直覺解釋

右偏的分配有一條往右拖的長尾巴，少數很大的數值會把平均數往右拉，所以平均數跑到中位數右邊（補充說明，非來源內容）

## 例子

- 家庭年所得的平均數大於中位數，是右偏分配（[ch3b p.35](../sources/ch3b.md)）
- 公寓租金資料的偏態為 0.92，是正的，屬於右偏（[ch3b p.6](../sources/ch3b.md)；判斷依據為 [ch3b p.4](../sources/ch3b.md)）
- 同一份租金資料 Q1 = 545、Q2 = 575、Q3 = 625（[ch3b p.31](../sources/ch3b.md)），Q2 離 Q1 只有 30，離 Q3 有 50，Q2 比較靠近 Q1，用盒鬚圖判斷也是右偏，和偏態 0.92 的結論一致（補充說明，非來源內容，判斷規則見 [ch3b p.31](../sources/ch3b.md)）

## 用盒鬚圖判斷偏態

- Q2 靠近 Q1：右偏，平均數 > Q2（[ch3b p.31](../sources/ch3b.md)）
- Q2 在 Q1 和 Q3 的中間：對稱（[ch3b p.31](../sources/ch3b.md)，講義筆誤已更正，見矛盾與待確認）
- Q2 靠近 Q3：左偏，平均數 < Q2（[ch3b p.31](../sources/ch3b.md)）

## 為什麼本輪主題需要它

母體分配很偏的時候，樣本數要大一點，樣本平均數的分配才會接近常態：多數應用 n ≥ 30 就夠，母體高度偏斜或有離群值時可能需要 n = 50（[ch7 p.51](../sources/ch7.md)），見[中央極限定理](central-limit-theorem.md)

## 常見誤解

- 以為平均數就是「大多數人」的水準：右偏的資料（例如所得）平均數會大於中位數，多數人其實低於平均數（[ch3b p.35](../sources/ch3b.md)）

## 相關概念

- [平均數](mean.md)
- [z-score](z-score.md)
- [經驗法則](empirical-rule.md)：經驗法則只適用於鐘形分配
- [中央極限定理](central-limit-theorem.md)：母體越偏，需要的樣本數越大

## 矛盾與待確認

- **右偏的條件**（[notes p.6](../sources/notes.md)）：筆記寫「右偏時 skewness 是正的且大於 1.0」，講義是偏態為正，「常大於 1.0」只用來形容高度右偏（[ch3b p.4](../sources/ch3b.md)），偏態 0.92 的租金資料也是右偏，本頁採用講義的說法（2026-11-23，已解決）
- **講義筆誤**（[ch3b p.31](../sources/ch3b.md)）：講義寫「Q2 in the middle of Q1 and Q2」，應為 Q1 和 Q3，使用者決定顯示更正後的內容（2026-11-23，已解決）
- **文字層錯誤**（[ch3b p.31](../sources/ch3b.md)）：文字層把不等號對調，看圖片確認講義正確，本頁內容以圖片為準（2026-11-23，已解決）

## 來源

- [ch3b](../sources/ch3b.md) p.3 到 6、p.31、p.34、p.35
- [ch7](../sources/ch7.md) p.51
- [notes](../sources/notes.md) p.5、p.6
