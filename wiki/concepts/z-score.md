---
type: concept
sources: [ch3b, ch6, notes]
updated: 2026-11-23
---

# z-score（標準化值）

## 定義

z-score 又稱標準化值（standardized value），表示一個資料值 $x_i$ 離平均數有幾個標準差（[ch3b p.7](../sources/ch3b.md)）

## 公式

$$z_i = \frac{x_i - \bar{x}}{s}$$

（[ch3b p.7](../sources/ch3b.md)）

### 兩種寫法

| 用在哪裡 | 公式 | 來源 |
|---|---|---|
| 描述一組樣本資料 | $z_i = (x_i - \bar{x})/s$ | [ch3b p.7](../sources/ch3b.md) |
| 常態隨機變數的標準化 | $z = (x - \mu)/\sigma$ | [ch6 p.29](../sources/ch6.md) |

兩者的意義相同，都是「離平均數幾個標準差」（[ch3b p.7](../sources/ch3b.md)、[ch6 p.29](../sources/ch6.md)、[notes p.6](../sources/notes.md)），差別只在用樣本的 $\bar{x}$、$s$ 還是母體的 $\mu$、$\sigma$（補充說明，非來源內容）

## 直覺解釋

- z-score 衡量的是資料在整組資料中的相對位置（[ch3b p.8](../sources/ch3b.md)）
- 標準化就是換一把尺：把原本的數線 μ−σ、μ、μ+σ 換成 −1、0、1（[ch3b p.10 手寫](../sources/ch3b.md)）
- 小於平均數時 z < 0，大於平均數時 z > 0，等於平均數時 z = 0（[ch3b p.8](../sources/ch3b.md)）

## 例子

班級人數資料，$\bar{x} = 44$、$s = 8$（[ch3b p.10](../sources/ch3b.md)）：

| $x_i$ | $x_i - \bar{x}$ | $z_i$ |
|---|---|---|
| 46 | 2 | 2/8 = 0.25 |
| 54 | 10 | 10/8 = 1.25 |
| 42 | −2 | −2/8 = −0.25 |
| 46 | 2 | 2/8 = 0.25 |
| 32 | −12 | −12/8 = −1.50 |

## 用 z-score 找離群值

- z < −3 或 z > +3 的資料可視為離群值（outlier）（[ch3b p.21](../sources/ch3b.md)）
- 離群值可能是記錄錯誤、不該納入的資料，也可能是正確但特殊的資料，不能直接刪掉（[ch3b p.21](../sources/ch3b.md)）
- 公寓租金最極端的 z-score 為 −1.20 和 2.27，沒有離群值（[ch3b p.22](../sources/ch3b.md)）
- 筆記只寫了「可能是紀錄錯或不是同一組資料」（[notes p.6](../sources/notes.md)），要記得講義還提到第三種可能：正確且屬於這組資料的值（[ch3b p.21](../sources/ch3b.md)）

## 常見誤解

- z 是負的不代表資料有問題，只代表它比平均數小（[ch3b p.8](../sources/ch3b.md)）

## 相關概念

- [平均數](mean.md)、[變異數與標準差](variance-and-standard-deviation.md)：z-score 的分子和分母
- [經驗法則](empirical-rule.md)：用 z 表示「離平均數幾個標準差」
- [標準常態分配與查表](standard-normal.md)：把常態隨機變數標準化後查表
- [分配形狀與偏態](distribution-shape.md)
- [符號對照表](notation.md)

## 來源

- [ch3b](../sources/ch3b.md) p.7、p.8、p.10、p.21、p.22
- [ch6](../sources/ch6.md) p.29
- [notes](../sources/notes.md) p.6
