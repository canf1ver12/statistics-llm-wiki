---
type: output
query: 以 Wiki 為唯一知識來源，產生給統計初學者看的教學簡報大綱
pages_used: 16
updated: 2026-11-23
---

# 簡報大綱：只抽一次樣本，怎麼知道整個母體？

這份大綱是對 Wiki 做 query（N5）的產出，每張投影片都列出對應的 Wiki 頁面；經過 N6 對應檢查和使用者確認後，才產生 `lessons/sampling-clt-ci/index.html`

## 設計原則

- **對象**：沒學過統計的人，只需要國中程度的平均數概念
- **主軸**：沿著 [overview](../overview.md) 的概念鏈，從「為什麼要抽樣」走到「信賴區間」，每一張都回答一個問題
- **每張投影片頁尾標出對應的 Wiki 頁面**，讓簡報內容可以追溯回 Wiki 和講義頁碼
- **只用 Wiki 裡有的事實和數字**；互動模擬的隨機結果只是示範概念，會在畫面上註明「隨機模擬」
- **不使用講義的原圖**（有版權），圖表一律自己畫
- **寫作風格**照 AGENTS.md 第 6 節：繁中、台灣用語、不用句號、不用 emoji

## 結構

| 段落 | 投影片 | 回答的問題 |
|---|---|---|
| 開場 | 1 到 2 | 為什麼不能問所有人 |
| 第一部分：基本工具 | 3 到 7 | 描述資料、常態分配、標準化 |
| 第二部分：抽樣分配與中央極限定理 | 8 到 13 | $\bar{x}$ 會怎麼變、為什麼會接近常態 |
| 第三部分：信賴區間 | 14 到 18 | 怎麼用一個樣本說出 μ 的範圍 |
| 收尾 | 19 到 21 | 常見誤解、總結、資料來源 |

## 投影片

### 1. 封面：只抽一次樣本，怎麼知道整個母體？

- 教學目標：說出這份簡報要回答的問題
- 重點：副標題「抽樣分配、中央極限定理與信賴區間」；一行預告：最後會學到如何寫出「有 95% 的信心，μ 落在某個範圍」
- 對應 Wiki：[overview](../overview.md)

### 2. 問題：為什麼要抽樣

- 教學目標：理解抽樣的必要性與代價
- 重點：
  - EAI 公司想了解 2,500 位經理的年薪，但沒有全部資料，只能抽 30 位（ch7 p.8）
  - 樣本只是母體的一部分，所以只能得到估計值，抽樣一定存在誤差（ch7 p.7、p.7 手寫）
- 視覺：2,500 個點裡圈出 30 個
- 對應 Wiki：[random-sampling](../concepts/random-sampling.md)

### 3. 母體參數與樣本統計量

- 教學目標：分清楚「想知道的」和「手上有的」
- 重點：
  - 母體參數（μ、σ）固定但通常不知道；樣本統計量（$\bar{x}$、s）算得出來但會隨樣本改變（ch3a p.4 手寫、ch7 p.19 手寫）
  - 對照表：μ ← $\bar{x}$、σ² ← s²
  - 隨機抽樣的條件：每個樣本被抽中的機率相同、每個元素獨立（iid）
- 視覺：左右兩欄對照表
- 對應 Wiki：[parameter-and-statistic](../concepts/parameter-and-statistic.md)、[random-sampling](../concepts/random-sampling.md)、[notation](../concepts/notation.md)

### 4. 工具一：平均數與標準差

- 教學目標：用兩個數字描述一組資料
- 重點：
  - $\bar{x} = \sum x_i / n$，例：班級人數 46、54、42、46、32，$\bar{x} = 44$
  - 標準差是離均差平方平均的平方根，同一組資料 s = 8（ch3a p.46、ch3b p.10）
  - 樣本變異數分母是 n−1，因為算 $\bar{x}$ 用掉一個自由度（ch8 p.55），只用一行帶過
- 視覺：5 個點在數線上，標出 $\bar{x}$ 和 ±s
- 對應 Wiki：[mean](../concepts/mean.md)、[variance-and-standard-deviation](../concepts/variance-and-standard-deviation.md)

### 5. 工具二：常態分配

- 教學目標：認識鐘形曲線，以及「機率是面積」
- 重點：
  - 由 μ 和 σ 決定：μ 決定位置，σ 決定寬度（ch6 p.19、p.21、p.22、notes p.13）
  - 對稱，平均數 = 中位數 = 眾數（ch6 p.18、p.20）
  - 機率是曲線下的面積，總面積為 1，單一點的機率為 0（ch6 p.4、p.5、p.23）
- 視覺：可調 μ、σ 的常態曲線（互動）
- 對應 Wiki：[normal-distribution](../concepts/normal-distribution.md)

### 6. 工具三：經驗法則

- 教學目標：記住 ±1、2、3 個標準差的比例
- 重點：68.26%、95.45%、99.73%（ch3b p.19、ch6 p.27）；例：洗衣精平均 16 盎司、標準差 0.25（ch3b p.20）
- 視覺：常態曲線上三層色塊
- 對應 Wiki：[empirical-rule](../concepts/empirical-rule.md)

### 7. 工具四：標準化與查表

- 教學目標：任何常態分配都能換成標準常態再查表
- 重點：
  - $Z = (X - \mu)/\sigma \sim N(0, 1)$，z 是「離平均數幾個標準差」（ch6 p.29）
  - z 表給左邊的累積面積，例：$P(-1 \le z \le 1) = 0.8413 - 0.1587 = 0.6826$，就是經驗法則的 68.26%（ch6 p.41）
  - 反查：右尾 0.05 對應 1.645，之後信賴區間會用到（ch6 p.60）
- 視覺：兩條數線對照 x 和 z（ch3b p.10 手寫的概念）
- 對應 Wiki：[z-score](../concepts/z-score.md)、[standard-normal](../concepts/standard-normal.md)、[empirical-rule](../concepts/empirical-rule.md)

### 8. 關鍵轉折：$\bar{x}$ 也是隨機變數

- 教學目標：理解「換一組樣本，$\bar{x}$ 就不一樣」
- 重點：
  - 大寫 $\bar{X}$ 是估計量（數學式、隨機變數），小寫 $\bar{x}$ 是代入資料後的估計值（ch7 p.19 手寫）
  - St. Andrew's 的例子：樣本 $\bar{x}$ = 1684，母體 μ = 1697，接近但不相等（ch7 p.29 到 31）
- 視覺：母體參數與點估計值的對照表
- 對應 Wiki：[point-estimation](../concepts/point-estimation.md)

### 9. 抽樣分配：如果抽 500 次

- 教學目標：理解抽樣分配是「很多個 $\bar{x}$ 的分配」
- 重點：
  - EAI：每次抽 30 人算 $\bar{x}$，重複 500 次，直方圖呈鐘形（ch7 p.35 到 37）
  - 看三件事：是否對稱、中心在哪、多分散（ch7 p.34 手寫、notes p.20）
  - 實務上只抽一次，500 次只是示範（ch7 p.42）
  - 分清楚三種分配：母體、一組樣本、抽樣分配
- 視覺：自己畫的示意直方圖（不用講義原圖）
- 對應 Wiki：[sampling-distribution](../concepts/sampling-distribution.md)

### 10. 抽樣分配的中心與寬度

- 教學目標：記住 $E(\bar{x}) = \mu$ 和 $\sigma_{\bar{x}} = \sigma/\sqrt{n}$
- 重點：
  - $E(\bar{x}) = \mu$，所以 $\bar{x}$ 是不偏的（ch7 p.45）
  - $\sigma_{\bar{x}} = \sigma/\sqrt{n}$ 叫標準誤差（ch7 p.47）
  - 推導兩行帶過（ch7 p.38 手寫）
- 對應 Wiki：[sampling-distribution](../concepts/sampling-distribution.md)、[standard-error](../concepts/standard-error.md)

### 11. 互動模擬：中央極限定理

- 教學目標：親眼看到「母體再怪，$\bar{x}$ 都會接近常態」
- 重點：
  - 選母體：均勻、V 字形、右偏（對應 ch7 p.55、p.56 的三種母體）
  - 選樣本數：n = 2、5、30
  - 按「抽 500 次」，左邊顯示母體，右邊畫出 500 個 $\bar{x}$ 的直方圖
  - 畫面註明「隨機模擬，每次結果不同」
- 對應 Wiki：[central-limit-theorem](../concepts/central-limit-theorem.md)、[sampling-distribution](../concepts/sampling-distribution.md)

### 12. 中央極限定理：樣本要多大才夠

- 教學目標：知道定理的內容和使用條件
- 重點：
  - 定理：n 夠大時，$\bar{X} \sim N(\mu, \sigma^2/n)$（ch7 p.53、p.54 手寫）
  - 條件表：母體常態時任何 n；多數情況 n ≥ 30；高度偏斜或有離群值 n = 50（ch7 p.51）
  - 呼應剛才的模擬：右偏母體最慢變成鐘形
- 對應 Wiki：[central-limit-theorem](../concepts/central-limit-theorem.md)、[distribution-shape](../concepts/distribution-shape.md)

### 13. 標準誤差：樣本越大，估計越準

- 教學目標：理解 n 如何影響估計的精準度
- 重點：
  - EAI 對照表：n = 30 時標準誤差 730.3，$\bar{x}$ 落在 μ ± 500 的機率 0.5034；n = 100 時為 400 和 0.7888（ch7 p.50、p.62、p.67、p.68）
  - $\sigma_{\bar{x}} < \sigma$，n 越大曲線越陡（ch7 p.63 手寫、notes p.21）
  - 易錯提醒：$\sigma^2/n$ 是變異數，標準誤差要開根號（notes p.20 的筆誤，ch7 p.47）
- 視覺：n = 30 和 n = 100 兩條曲線疊在一起
- 對應 Wiki：[standard-error](../concepts/standard-error.md)

### 14. 從中央極限定理到信賴區間

- 教學目標：看懂信賴區間公式從哪裡來
- 重點：
  - 前提：$\bar{X}$ 近似常態，要寫出 by CLT（ch8 p.4 手寫、notes p.24）
  - 三步推導：標準化、兩尾各留 α/2、把 μ 移到中間（ch8 p.5 手寫、p.22 手寫）
  - 結果：$\bar{x} \pm z_{\alpha/2}\,\sigma/\sqrt{n}$，上界跟下界不要寫反
- 對應 Wiki：[confidence-interval](../concepts/confidence-interval.md)

### 15. 例子：Lloyd's 百貨

- 教學目標：完整算一次 95% 信賴區間
- 重點：σ = 20、n = 100 → 標準誤差 2 → 邊際誤差 1.96 × 2 = 3.92 → $\bar{x}$ = 82 時區間為 78.08 到 85.92（ch8 p.9、p.31、p.37）
- 視覺：逐步出現的計算步驟
- 對應 Wiki：[confidence-interval](../concepts/confidence-interval.md)、[margin-of-error](../concepts/margin-of-error.md)

### 16. 互動模擬：「95% 信賴」到底是什麼意思

- 教學目標：理解 95% 是「方法的成功率」，不是 μ 的機率
- 重點：
  - 按一下抽 100 個樣本，畫出 100 個區間，包含 μ 的標綠色，沒包含的標紅色，計數顯示約 95 個包含 μ（概念取自 ch8 p.15、p.36、p.38）
  - 畫面註明「隨機模擬，每次結果不同」
  - 結論句：用這個方法建立的區間有 95% 會包含 μ，所以對手上這一個區間說「有 95% 的信心」
- 對應 Wiki：[confidence-interval](../concepts/confidence-interval.md)

### 17. 區間寬度：信心與精準的取捨

- 教學目標：知道信賴水準和 n 如何影響寬度
- 重點：
  - Lloyd's 三種信賴水準：90% 為 78.71 到 85.29、95% 為 78.08 到 85.92、99% 為 76.85 到 87.15（ch8 p.44）
  - n 越大區間越窄（ch8 p.24 手寫、notes p.25）
  - 反推樣本數：$n = (z_{\alpha/2}\sigma/E)^2$，例 89.43 → 無條件進位取 90（ch8 p.29）
- 視覺：三條長短不同的區間
- 對應 Wiki：[margin-of-error](../concepts/margin-of-error.md)、[confidence-interval](../concepts/confidence-interval.md)

### 18. 如果不知道 σ

- 教學目標：知道還有 t 分配，但本簡報不展開
- 重點：
  - σ 未知、n < 30、母體常態或不嚴重偏離常態時用 t：$\bar{x} \pm t_{\alpha/2}(n-1)\,s/\sqrt{n}$（ch8 p.53、p.74、notes p.26）
  - n ≥ 30 時可用 $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$，因為 n 大時 t 接近標準常態（notes p.26，使用者採用的做法）
  - t 比標準常態矮胖，自由度越大越接近（ch8 p.56）
- 對應 Wiki：[confidence-interval](../concepts/confidence-interval.md)

### 19. 常見誤解整理

- 教學目標：把容易錯的地方一次整理
- 重點（每點一行）：
  - 中央極限定理說的是 $\bar{x}$ 的分配，不是資料本身變常態
  - n ≥ 30 不是萬用，偏斜母體可能要 50
  - 標準誤差是 $\sigma/\sqrt{n}$，不是 $\sigma^2/n$
  - 「μ 有 95% 機率在區間內」的說法不精確，μ 是固定的，會變的是區間
  - 連續型的機率是面積，不是曲線高度
- 對應 Wiki：[central-limit-theorem](../concepts/central-limit-theorem.md)、[standard-error](../concepts/standard-error.md)、[confidence-interval](../concepts/confidence-interval.md)、[normal-distribution](../concepts/normal-distribution.md)

### 20. 總結：一條概念鏈

- 教學目標：回顧整條推論的路徑
- 重點：隨機抽樣 → 點估計 → 抽樣分配 → 中央極限定理 → 標準誤差 → 信賴區間，每一步一句話
- 視覺：overview 概念鏈的簡化版流程圖
- 對應 Wiki：[overview](../overview.md)

### 21. 資料來源

- 教學目標：讓觀眾可以追溯每張投影片的出處
- 重點：本簡報的內容全部來自 statistics-llm-wiki，Wiki 整理自課堂講義第 3、6、7、8 章與使用者的手寫筆記；附上 GitHub repo 連結
- 對應 Wiki：[index](../index.md)

## N6 對應檢查

用腳本逐項比對大綱裡的數字和說法，是否出現在該投影片標示的 Wiki 頁面

| 輪次 | 檢查項數 | 不通過 | 問題 | 處理 |
|---|---|---|---|---|
| 第 1 輪 | 75 | 2 | 第 7 張的 0.6826 推導在 empirical-rule 頁，第 17 張的三個區間在 confidence-interval 頁，大綱標錯對應頁面 | 回到 N5 補上對應頁面 |
| 第 2 輪 | 76 | 0 | 無（改為直接從大綱讀取每張的對應頁面，另外多檢查第 19 張的 1 項） | 通過，等待使用者確認 |

- 不通過的原因都是大綱的對應寫錯，不是 Wiki 缺內容，所以回 N5，不用回 N3
- 第 9 張的「三種分配」和第 12 張的「右偏母體最慢變成鐘形」在 Wiki 裡標為補充說明，簡報中照樣標示為補充
