# Log

時間序紀錄，只能往後新增，格式見 [AGENTS.md](../AGENTS.md) 第 9 節

## [2026-11-23 11:40] discuss | 選定主題

- 摘要：盤點 `raw/` 的 21 份資料（講義 ch1 到 ch14b，加上手寫筆記 `統計筆記.pdf`）
- 使用者決定：
  - 主題為統計學，使用課堂講義和自己的手寫筆記當來源
  - 本輪範圍為「抽樣分配與中央極限定理」，加上信賴區間
  - 不加假設檢定，避免概念量太大，初學者跟不上
- 檢查：
  - [N1 acquire][不通過] 講義上的手寫註記和 `notes` 的文字層是亂碼（例如 $\bar{x}$ 讀成「女」），圖表頁沒有文字 → 改為把這些頁面轉成圖片直接看，寫進 schema 的 N1 規則
  - [N1 acquire][衝突] `notes` p.20 把 $\sigma^2/n$ 標成標準誤差，正確應為 $\sigma/\sqrt{n}$ → 留待 ingest `notes` 時處理
  - [N1 acquire][衝突] `ch7` p.50 先算 n/N = 0.012，下一行寫成 0.112 ≤ 5%，講義本身前後不一致 → 留待 ingest `ch7` 時處理

## [2026-11-23 12:05] schema | 建立 AGENTS.md 與 CLAUDE.md

- 摘要：參考 Karpathy 的 LLM Wiki pattern 建立 schema，定義三層架構、頁面規範、N1 到 N9 的流程和 log 格式
- 使用者決定：
  - 本輪 ingest 範圍：`ch3a`、`ch3b`、`ch6`、`ch7`、`ch8`、`notes`（只處理相關頁）
  - README 的寫作規則（不用句號、不用 emoji、台灣用語）也套用到 Wiki 和簡報
  - `assests/` 改名為 `raw/`
  - 繳交方式為 GitHub repo 加 GitHub Pages，`raw/` 有版權，不進 git
  - 每份來源 ingest 前都要經過 N2 討論
  - 使用標準 Markdown 連結，GitHub 和 Obsidian 都能用
- 異動頁面：AGENTS.md、CLAUDE.md、wiki/log.md、wiki/index.md

## [2026-11-23 12:10] schema | 忽略考試範圍標記

- 摘要：修改 AGENTS.md 第 4 節「來源的性質」
- 使用者決定：講義上的「不考」這類標記只是考試註記，ingest 時一律忽略，不寫進 Wiki，也不影響內容取捨
- 異動頁面：AGENTS.md、wiki/log.md

## [2026-11-23 12:40] ingest | ch3a

- 摘要：讀取 ch3a 全文文字層，p.4、7、8、45、46、49、51 轉成圖片閱讀手寫註記與公式，只詳寫 3.1、3.2 中和本輪主題相關的部分
- 使用者決定：
  - 用詞統一為「母體參數」和「樣本統計量」（N2 時 LLM 原本只寫「參數」，經使用者修正）
  - p.53 變異係數例子的筆誤（0.8 應為 1.0），在 Wiki 顯示更正後的算式，原文記在來源頁疑點
  - p.51 手寫「常態母體下 s 與 x̄ 獨立」本輪不展開，列入 index 的待展開清單
  - 「樣本變異數為何除以 n−1」的說明，等使用者看過草稿後決定是否收錄
- 檢查：
  - [N2 discuss][不通過] 用詞不精確，「參數」應為「母體參數」 → 依使用者修正後寫入
  - [N1 acquire][衝突] ch3a p.53 變異係數算式用 0.8，與標準差 1.0 和結果 22.22% 不一致 → 判斷為筆誤，使用者決定顯示更正值
  - [N4 lint][不通過] sources/ch3a.md 連到尚未建立的 ch3b.md → 改為純文字，ingest ch3b 時再加連結
  - [N4 lint][不通過] 3 處中文句號，違反寫作規則 → 改為逗號
  - [N4 lint][不通過] notation.md 頁首說明被判定缺少引用，屬於 lint 規則誤判 → 修改 tools/lint_wiki.py，H1 標題下的頁面說明不檢查引用
  - [N4 lint][通過] 修正後重跑全部通過，人工抽查 p.5、7、12、14、46、48、49 的引用頁碼與公式皆正確
- 異動頁面：wiki/sources/ch3a.md、wiki/concepts/parameter-and-statistic.md、wiki/concepts/mean.md、wiki/concepts/variance-and-standard-deviation.md、wiki/concepts/notation.md、wiki/overview.md、wiki/index.md、tools/lint_wiki.py、AGENTS.md

## [2026-11-23 13:00] discuss | 樣本變異數為何除以 n−1

- 摘要：LLM 提出兩種說明（估計偏小、自由度），使用者兩次指出說明不夠清楚，最後選擇自由度的版本
- 使用者決定：
  - 一句話版本「x̄ 會貼著這組樣本，算出來偏小」太模糊，不採用
  - 採用自由度版本，寫入 concepts/variance-and-standard-deviation.md，除了離均差總和為 0 有 ch3a p.46 的依據，其餘標成補充說明
- 檢查：
  - [N2 discuss][不通過] LLM 第一版說明太抽象，使用者讀不懂 → 改成分步驟的版本，最後依使用者選擇改用自由度版本
  - [N4 lint][不通過] 又出現 1 處中文句號，同類錯誤第二次發生 → 改為逗號
  - [N4 lint][通過] 修正後重跑全部通過
- 異動頁面：wiki/concepts/variance-and-standard-deviation.md

## [2026-11-23 13:30] ingest | ch3b

- 摘要：讀取 ch3b 全文文字層，p.4、7、10、18、31 轉成圖片閱讀，詳寫偏態、z-score、經驗法則、柴比雪夫定理、離群值
- 使用者決定：
  - 同意在 N1 加入新規則：懷疑來源有錯誤或矛盾時，先看頁面圖片確認才能回報或寫入
  - 經驗法則一律採用 p.19 的 68.26%、95.45%、99.73%，不用 p.18 圖上的數字，也不用 p.20 的近似值
  - p.31 講義筆誤（Q1 and Q2 應為 Q1 and Q3）顯示更正後的內容
  - p.31 手寫問號（右偏時平均數會不會大於 Q3）列入待展開
  - 柴比雪夫定理收進經驗法則頁面當對照
- 檢查：
  - [N1 acquire][不通過] p.31 的文字層把「mean > Q2」和「mean < Q2」的不等號對調，差點誤判為講義和 p.4 矛盾 → 看圖片確認講義正確，在 AGENTS.md 的 N1 新增「懷疑有錯先看圖片」規則，Lint 清單也加上對應項目
  - [N1 acquire][衝突] p.31 講義筆誤「Q1 and Q2」 → 已用圖片確認，依使用者決定顯示更正值
  - [N1 acquire][衝突] p.18 圖上的 95.44%、99.72% 與 p.19 的 95.45%、99.73% 不一致 → 已用圖片確認，依使用者決定採用 p.19
  - [N4 lint][不通過] 3 處「矛盾與待確認」寫了頁碼卻沒加來源連結 → 補上連結
  - [N4 lint][不通過] 3 個表頭被判定缺少引用，屬於 lint 規則誤判 → 修改 tools/lint_wiki.py，改成用下一行是否為 `|---` 判斷表頭
  - [N4 lint][通過] 修正後重跑全部通過，人工抽查 p.6、10、12、14、19、22、34 的引用頁碼與數字皆正確
- 異動頁面：wiki/sources/ch3b.md、wiki/sources/ch3a.md、wiki/concepts/distribution-shape.md、wiki/concepts/z-score.md、wiki/concepts/empirical-rule.md、wiki/concepts/variance-and-standard-deviation.md、wiki/concepts/mean.md、wiki/concepts/notation.md、wiki/index.md、wiki/overview.md、tools/lint_wiki.py、AGENTS.md

## [2026-11-23 14:00] ingest | ch6

- 摘要：讀取 ch6 全文文字層，p.4、5、15、24、27、28、43 轉成圖片閱讀，只詳寫 6.2 常態分配，6.1、6.3、6.4 只列範圍
- 使用者決定：
  - p.28 的 95.44%、99.72% 沿用 ch3b 的決定，一律採用 68.26%、95.45%、99.73%
  - 反查 z 值採用講義的 1.28，不用使用者手寫的 1.285
- 檢查：
  - [N1 acquire][衝突] p.28 的 95.44%、99.72% 與 p.27 不一致 → 已用圖片確認，沿用既有決定
  - [N1 acquire][衝突] p.43、p.51 手寫 1.285 與講義的 1.28 不一致 → 已用圖片確認，查表後 1.28 較接近 0.9，使用者決定採用 1.28
  - [N3 compile][不通過] 來源頁 6.3、6.4 的頁碼範圍是 LLM 推測後直接寫入，沒有查證 → 用文字層查出實際頁碼（Pep Zone p.54 到 63、6.3 p.64 到 77、6.4 p.78 到 89）後修正
  - [N4 lint][不通過] 「機率密度函數」的「函數」被判定為中國用語，屬於 lint 規則誤判，數學上台灣用「函數」，程式設計才用「函式」 → 從 tools/lint_wiki.py 的清單移除「函數」並註明原因
  - [N4 lint][通過] 修正後重跑全部通過，人工抽查 p.29、41、50、53、58、60 的引用頁碼與數字皆正確
- 補充：上一輪回報給使用者的錯誤統計是 LLM 手算的，N4 不通過次數報成 8 筆，實際為 6 筆 → 已向使用者更正，之後統計一律用 log 的 grep 指令
- 異動頁面：wiki/sources/ch6.md、wiki/concepts/normal-distribution.md、wiki/concepts/standard-normal.md、wiki/concepts/z-score.md、wiki/concepts/empirical-rule.md、wiki/concepts/notation.md、wiki/index.md、wiki/overview.md、tools/lint_wiki.py

## [2026-11-23 14:01] ingest | ch7

- 摘要：讀取 ch7 全文文字層，p.19、20、34、37、38、40、47、50、54、55、56、59、63、68、75、77、112 轉成圖片閱讀（其中多頁只有手寫，文字層為亂碼），詳寫抽樣、點估計、x̄ 的抽樣分配、中央極限定理、標準誤差、點估計量的性質、抽樣誤差，p̄ 和其他抽樣方法只列範圍
- 使用者決定：
  - p.50（0.112 應為 0.012）、p.75（±0.68 應為 ±0.63）兩處講義筆誤，顯示更正後的值
  - 授權新常規：看圖片確認過、答案明確的講義筆誤，不用先問，直接更正並記錄，已寫入 AGENTS.md 第 7 節；使用者手寫和 notes 的錯誤仍要回報
  - p.38 手寫 Xᵢ ~ N(μ, σ_x̄²) 為筆誤，Wiki 寫 Xᵢ ~ (μ, σ²)，筆誤記在來源頁
  - p.39 手寫「n ≥ 30（or 25）」，Wiki 採用講義的 n ≥ 30、偏斜時 n = 50
- 檢查：
  - [N1 acquire][衝突] p.50 講義筆誤 0.112 → 已用圖片確認，更正為 0.012
  - [N1 acquire][衝突] p.75 講義筆誤 ±0.68（從 EAI 例子複製）→ 已用圖片確認，依 p.72 更正為 ±0.63
  - [N1 acquire][衝突] p.38 使用者手寫 Xᵢ 的分配寫錯 → 已用圖片確認，與 p.64 手寫對照後更正
  - [N1 acquire][衝突] p.39 手寫「or 25」與講義 n ≥ 30 不一致 → 採用講義
  - [N4 lint][不通過] 2 處把 Big Data 寫成「大數據」 → 改為台灣用語「巨量資料」
  - [N4 lint][不通過] 2 個例子的開頭句缺少引用 → 補上 ch7 p.50、58、69、70
  - [N4 lint][不通過] 例子表格的資料列被判定缺少引用，屬於 lint 規則誤判 → 修改 tools/lint_wiki.py，標題以「例子」開頭的區塊都放行表格資料列
  - [N4 lint][通過] 修正後重跑全部通過；讀取時已逐一驗算 730.3、400、15.96、8.2、0.5034、0.7888、0.4714、0.7776 和 p.140 的標準誤差表，與講義一致
- 補引用：distribution-shape、parameter-and-statistic 兩頁原本標「待 ingest ch7 後補上引用」的段落，改為 ch7 p.7、19、29、51 的引用；variance-and-standard-deviation 補上 s² 為 UMVUE（ch7 p.20 手寫、p.111）
- 異動頁面：wiki/sources/ch7.md、wiki/concepts/random-sampling.md、wiki/concepts/point-estimation.md、wiki/concepts/sampling-distribution.md、wiki/concepts/central-limit-theorem.md、wiki/concepts/standard-error.md、wiki/concepts/parameter-and-statistic.md、wiki/concepts/distribution-shape.md、wiki/concepts/variance-and-standard-deviation.md、wiki/concepts/notation.md、wiki/index.md、wiki/overview.md、tools/lint_wiki.py、AGENTS.md

## [2026-11-23 14:02] schema | log 時間一律用 date 取得

- 摘要：寫完 ch7 紀錄後執行 date，發現實際時間是 14:01，但紀錄寫成 15:00；除了 12:05 那筆，其他紀錄的時間都是 LLM 估計的，沒有實際查詢
- 處理：ch7 紀錄改為實際時間 14:01；11:40、12:10、12:40、13:00、13:30、14:00 這六筆時間是估計值，無法回溯查證，保留原樣並在此註明；AGENTS.md 第 9 節加上規則「紀錄時間一律用 date 指令取得」
- 檢查：
  - [N3 compile][不通過] log 時間未查證就寫入，與 ch6 編造頁碼屬同一類問題 → 修正並新增規則
- 異動頁面：wiki/log.md、AGENTS.md

## [2026-11-23 14:08] ingest | ch8

- 摘要：讀取 ch8 全文文字層，p.4、5、22、23、24、30、40、44、55 轉成圖片閱讀，詳寫 8.1 σ 已知的區間估計，8.2 t 分配只取 p.53、55 到 57、74，8.3、8.4 只列範圍
- 使用者決定：
  - p.5 手寫 z_0.005 = 2.575，採用講義 p.40 的 2.576
- 檢查：
  - [N1 acquire][衝突] p.30 講義算邊際誤差寫成 (1.96×9.65/100)² = 0.03577，與同頁公式 E = zσ/√n 不符 → 已用圖片確認，依講義筆誤規則直接更正為 1.89
  - [N1 acquire][衝突] p.44 標題寫 Discount Sounds，數字卻屬於 Lloyd's → 已用圖片確認，三列都用 Lloyd's 的 x̄ = 82、σ_x̄ = 2 驗算吻合，依講義筆誤規則直接更正
  - [N1 acquire][衝突] p.5 使用者手寫 2.575 與講義 2.576 不一致 → 回報使用者，採用 2.576
  - [N4 lint][不通過] confidence-interval.md 推導的第 1、2 步沒有逐行附引用 → 補上 ch8 p.5、p.22 手寫
  - [N4 lint][不通過] log.md 引用過去錯誤用詞「大數據」被判為中國用語，屬於 lint 規則誤判 → 修改 tools/lint_wiki.py，log.md 只檢查句號和 emoji
  - [N4 lint][通過] 修正後重跑全部通過；讀取時已驗算 3.92、78.08 到 85.92、3.29、5.15、1,470、39,630 到 42,570、89.43、1.89，與講義一致（1.89 為更正後的值）
- 補引用：point-estimation、standard-normal 兩頁原本標「待 ingest ch8」的段落改為 ch8 p.5、p.8、p.10 的引用；variance-and-standard-deviation 的自由度說明改為引用 ch8 p.55，不再是補充說明；central-limit-theorem 加入 n < 15、n = 15 的條件（ch8 p.46）
- 異動頁面：wiki/sources/ch8.md、wiki/concepts/confidence-interval.md、wiki/concepts/margin-of-error.md、wiki/concepts/point-estimation.md、wiki/concepts/standard-normal.md、wiki/concepts/variance-and-standard-deviation.md、wiki/concepts/central-limit-theorem.md、wiki/concepts/standard-error.md、wiki/concepts/notation.md、wiki/index.md、wiki/overview.md、tools/lint_wiki.py

## [2026-11-23 14:28] ingest | notes

- 摘要：用文字層中可辨識的章節標記定位相關頁，讀取 notes p.5、6、13、14、18 到 22、24 到 27 共 13 頁，全部看圖片（p.5 另外放大確認符號），和 5 份講義比對
- 使用者決定：
  - 筆記與講義不一致的第 1 到 5 項，Wiki 寫正確的版本，原文記在疑點和「矛盾與待確認」
  - 第 6 項（σ 未知且 n ≥ 30 時用 z）採用筆記的做法，使用者的理由是 n ≥ 30 的意思大約是 n 趨近無限大；LLM 之後補充講義 p.60「自由度超過 100 時 z 才是 t 的好近似」，並列在 confidence-interval.md 的矛盾與待確認供使用者參考
- 檢查：
  - [N1 acquire][衝突] notes p.20、p.22 把變異數 σ²/n、p(1−p)/n 標成標準誤差 → 已用圖片確認，Wiki 寫 σ/√n，收進 standard-error 的常見誤解
  - [N1 acquire][衝突] notes p.19 把 s² 的式子寫成 s → 已用圖片確認，Wiki 寫 s²
  - [N1 acquire][衝突] notes p.5 母體平均數寫成 x̄ = Σxᵢ/N → 已放大圖片確認，Wiki 寫 μ
  - [N1 acquire][衝突] notes p.6 右偏寫成「正的且大於 1.0」 → 已用圖片確認，採用講義的說法
  - [N1 acquire][衝突] notes p.13、ch6 p.2 手寫「連續隨機變數算高度」 → 已用圖片確認，Wiki 寫「算區間的面積，f(x) 是高度」
  - [N1 acquire][衝突] notes p.26 n ≥ 30 用 z 與講義 p.60、p.74 不一致 → 依使用者決定採用筆記做法，講義說法保留
  - [N1 acquire][衝突] ch6 p.2 手寫 U(1, 3) 的 f(x) = 1/3，應為 1/2 → 已用圖片確認，不在本輪範圍，記在 ch6 來源頁，待使用者確認
  - [N3 compile][不通過] 整合腳本第一次執行時，variance 頁的錨點文字是憑記憶寫的，與實際內容不符，腳本在第 2 頁中斷，只改了 mean.md → 改成先在副本試跑整份腳本，成功後才套用到正式 Wiki
  - [N3 compile][不通過] 寫入 normal-distribution 頁時引用了「ch6 p.2 手寫」，但當時只看過該頁文字層，違反 N1 的「先看圖片」規則 → 補看圖片，確認引用正確，另外發現 U(1, 3) 的問題
  - [N4 lint][不通過] confidence-interval.md 出現中文句號，同類錯誤第三次發生 → 改為逗號
  - [N4 lint][通過] 修正後重跑全部通過
- 其他：AGENTS.md 本身有 6 個中文句號，lint 只檢查 wiki/ 所以沒抓到 → 一併修正；AGENTS.md 和 CLAUDE.md 的寫作風格雖然不在第 6 節的適用範圍，仍保持一致
- 異動頁面：wiki/sources/notes.md、wiki/sources/ch6.md、wiki/concepts/ 下 14 個概念頁、wiki/index.md、AGENTS.md

## [2026-11-23 14:46] schema | 移除學校名稱並改寫 git 歷史

- 摘要：推上 GitHub 後，使用者要求移除學校名稱，AGENTS.md 一處、Wiki 兩處（量身高的例子）改成不指名的說法
- 使用者決定：改寫 git 歷史並強制推送，不只是新增一個 commit，讓舊 commit 也看不到學校名稱
- 檢查：
  - [N9 publish][不通過] 推送前只檢查了密碼、email 和教授姓名，沒有把學校名稱當作要確認的個人資訊 → 重建 docs(schema)、docs(wiki) 兩個 commit 後用 --force-with-lease 推送，確認遠端歷史中學校名稱（中英文）為 0 筆
- 異動頁面：AGENTS.md、wiki/concepts/random-sampling.md、wiki/sources/notes.md
