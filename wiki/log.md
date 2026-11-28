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

## [2026-11-23 14:49] query | 簡報大綱（N5、N6）

- 摘要：讀 index.md 和 overview.md 後，以 overview 的概念鏈為骨架，產生 21 張投影片的大綱 wiki/outputs/slides-outline.md，每張標出對應的 Wiki 頁面和講義頁碼，並規劃兩個互動模擬（中央極限定理、95% 信賴的意思）
- 檢查：
  - [N6 mapping][不通過] 第 1 輪用腳本比對 75 項，2 項不通過：第 7 張的 0.6826 推導在 empirical-rule 頁、第 17 張的三個區間在 confidence-interval 頁，大綱標錯對應頁面 → 回 N5 補上對應頁面，屬於大綱問題，不用回 N3
  - [N6 mapping][不通過] 修正後 LLM 直接在大綱寫下「第 2 輪 0 項不通過」，但當時還沒有重跑檢查，又是未查證就寫入 → 實際重跑後確認 76 項全部通過，再改成真實數字
  - [N6 mapping][通過] 第 2 輪 76 項全部通過
- 待辦：大綱需經使用者確認（N6），確認前不產生 HTML
- 異動頁面：wiki/outputs/slides-outline.md、wiki/index.md

## [2026-11-23 15:01] slides | 簡報簡單版（N7、N8）

- 摘要：使用者要求先參考 diveai-lessons 的做法做簡單版，看架構和內容，主題風格之後提供；讀取參考網站的原始碼後，採用相同架構：根目錄 index.html 為講義目錄，簡報放在 lessons/sampling-clt-ci/index.html，單一 HTML 檔，16:9 投影片、方向鍵翻頁、底部頁點；依 21 張大綱產生全部內容和 3 個互動圖（常態曲線、中央極限定理模擬、100 個信賴區間模擬）
- 使用者決定：先做簡單版看架構，主題風格之後提供；資料夾結構跟參考網站一致，AGENTS.md 由 slides/ 改為 index.html 加 lessons/<slug>/
- 檢查（用本機 Chrome 無畫面模式逐頁截圖，加上 ?autorun 參數讓模擬自動執行）：
  - [N8 verify][不通過] 第 4 頁 SVG 圖中的 x̄ 符號跑位 → 改成文字「平均數」
  - [N8 verify][不通過] 第 9、15、20 頁流程框中的數學式被拆成多行，原因是 CSS 把框內所有 span 設成區塊，連 KaTeX 內部的 span 也受影響 → 改成只套用在直接子元素
  - [N8 verify][不通過] 第 13 頁「n = 30」標籤壓到曲線 → 移位
  - [N8 verify][不通過] 首頁完全沒有套到樣式，原因是 CSS 註解裡的 lessons/*/index.html 含有 */，提早結束註解 → 改寫註解
  - [N8 verify][通過] 修正後重新截圖，21 頁和首頁都正常顯示，數學式、圖表、兩個模擬都能運作
- 異動頁面：index.html、lessons/sampling-clt-ci/index.html、AGENTS.md、wiki/outputs/slides-outline.md

## [2026-11-23 15:34] slides | 套用紅色剪貼簿主題（N7、N8）

- 摘要：依使用者提供的 assets/ 三張主題參考圖（紅色為主，藍色、黃色參考排版），把簡報和首頁改成紅色剪貼簿風格：橫線筆記紙、打孔、紅色邊線、底部撕邊，背後墊紅白格紋布和深紅點點紙，裝飾有圖釘、毛氈星星、牛皮紙膠帶、長尾夾、蝴蝶結、火漆封印；標題字型改用霞鶩文楷 TC
- 使用者決定：主色用紅色，其他顏色的參考圖只用來參考排版
- 決策：裝飾全部用 CSS 和 SVG 自己畫，不使用參考圖本身；assets/ 的參考圖來源不明，加進 .gitignore 不公開
- 檢查：
  - [N8 verify][不通過] 長尾夾和圖釘放在紙張上緣外，被投影片的撕邊剪裁切掉 → 改放在紙張內側
  - [N8 verify][通過] 重新截圖 21 頁和首頁，版面、數學式、圖表和模擬都正常
- 異動頁面：lessons/sampling-clt-ci/index.html、index.html、.gitignore

## [2026-11-23 15:38] slides | 裝飾改成寫實風格（N7、N8）

- 摘要：使用者回饋「看起來太像插畫，這個風格的重點是看起來像真實的東西」，改用寫實畫法：紙張加上顆粒、纖維和泛黃邊緣，打孔改成真正挖空（透出後方的格紋布），格紋布加上織線紋理和毛邊，圖釘、長尾夾、蝴蝶結、火漆封印改用漸層光影和材質濾鏡，膠帶改成半透明，所有物品加上投影
- 使用者決定：風格重點是寫實，不是插畫
- 檢查：
  - [N8 verify][通過] 截圖第 1、5、13、14 頁並放大 2 倍檢查細節：紙張質感、打孔、火漆封印接近實物；蝴蝶結仍偏塑膠感，是程式繪製的限制，已向使用者說明可改用實拍去背照片
- 異動頁面：lessons/sampling-clt-ci/index.html

## [2026-11-23 15:43] slides | 借用板夾版型（N7、N8）

- 摘要：使用者提供 Pinterest 連結，抓取後是一張黃色系剪貼簿版型圖（675 × 1200 JPG，來源標示為使用者上傳，含品牌商品照片）；因版權不明且解析度低，經使用者同意只借用版型：整疊講義上緣固定一個黃銅色大型板夾（壓印 μ，不放品牌），重點頁左緣加金色閃光星星，格紋布改成只露出上下兩條並移除點點紙，紙張整體微微傾斜；原本互動頁的長尾夾移除
- 使用者決定：參考圖只借用版型，不直接使用圖片
- 檢查：
  - [N8 verify][通過] 重新截圖 21 頁，板夾不壓到標題和內容，下移的內容區沒有溢出頁面
- 異動頁面：lessons/sampling-clt-ci/index.html

## [2026-11-23 15:50] slides | 使用者否決寫實剪貼簿風格

- 摘要：使用者看過三版剪貼簿風格（扁平插畫、寫實光影、借用板夾版型）後否決，改為另找適合插畫的風格；簡報內容不變，只有主題樣式要重做
- 使用者回饋：第二版「做的看起來太像插畫，但是這個風格的重點是這些插圖要做的看起來像真實的東西」，第三版「做得非常爛」
- 檢查：
  - [N8 verify][不通過] 使用者審查：參考圖是實物照片拼貼，用程式繪製做不出真實質感，LLM 沒有在一開始說明這個限制，連續改了三輪 → 等使用者提供插畫風格的參考
  - [N8 verify][不通過] 使用者審查：同上，第三版仍被否決；自動截圖檢查三次都標為通過，顯示截圖只能檢查版面有沒有壞，無法判斷風格
- 處理：修改 AGENTS.md，N6 確認大綱時要同時確認風格參考與可行性；N8 加上人工審查，使用者否決要記成不通過；N9 推送前的個資檢查明確列出學校名稱
- 異動頁面：AGENTS.md、wiki/log.md

## [2026-11-23 15:52] schema | 作業報告草稿與 lint 範圍擴大

- 摘要：起草 docs/assignment-report.md（主題、Wiki 成果、loop 與 graph 設計、執行紀錄、反思），數字都以 log 的 grep 統計為準；新增 README.md
- 檢查：
  - [N4 lint][不通過] 報告寫著「句號是最常見的錯誤」，報告本身卻有 8 個句號，AGENTS.md 也新增 1 個；原因是 lint 只檢查 wiki/ → 修正句號，並把寫作風格檢查擴大到 AGENTS.md、CLAUDE.md、README.md、docs/，放入含句號的暫存檔確認新規則會抓到後刪除
  - [N4 lint][通過] 修正後全部通過
- 異動頁面：docs/assignment-report.md、README.md、AGENTS.md、tools/lint_wiki.py、wiki/log.md

## [2026-11-23 15:54] schema | 推送前抓到 log 裡的學校名稱

- 摘要：照新的 N9 規則，推送前掃描要推送的 9 個 commit，發現「移除學校名稱」那筆 log 自己寫出了學校名稱（中文和英文縮寫各一次）
- 檢查：
  - [N9 publish][不通過] log 記錄移除學校名稱時引用了名稱本身 → 改寫成「學校名稱」，用 filter-branch 改寫尚未推送的 9 個 commit，刪除本機的舊歷史備份，確認推送範圍內為 0 筆後才推送，不需要強制推送
  - [N9 publish][通過] 修正後推送
- 補充：每個 commit 的作者資訊都包含使用者的 git email，這是 git 的預設行為，已告知使用者可改用 GitHub 提供的 noreply email
- 異動頁面：wiki/log.md

## [2026-11-23 15:58] schema | 從 git 歷史中完全刪除作業報告

- 摘要：使用者要求作業報告不放上 GitHub，並從歷史中完全刪除；用 filter-branch 從尚有報告的 commit 起改寫歷史，「新增作業報告草稿」的 commit 因此變成空的並被移除，再以 --force-with-lease 強制推送
- 使用者決定：改寫歷史並強制推送
- 檢查：
  - [N9 publish][通過] 推送後重新抓取遠端，遠端歷史中含有報告檔案的 commit 為 0 筆，本機報告檔案保留
- 異動頁面：wiki/log.md（git 歷史）

## [2026-11-23 17:59] slides | 套用蠟筆插畫風格到 21 頁（N7、N8）

- 摘要：依使用者新提供的蠟筆插畫參考圖（含 MistLaneStudio 浮水印，只參考風格），先做 2 頁樣張經使用者確認，再套用到 21 頁與首頁：紙張紋理、蠟筆質感圖表、網點圓、粗顆粒蠟筆小插圖、票根、收據式表格、各段手寫英文大字
- 使用者決定：字體組合 H5 思源宋體、S1 思源黑體、B1 Caveat Brush、T1 Special Elite、R4 霞鶩文楷（收據中文）、L1 Caveat Brush（圖表標籤）；票根文字由 ADMIT ONE 改為和主題相關的 ONE SAMPLE ONLY
- 暫定、待使用者確認：英文大字粗細（B1 或 B1a 到 B4b）、紅色易錯筆記與「母體」標籤先用霞鶩文楷保留手寫感
- 檢查：
  - [N8 verify][不通過] 第 7、16、17 頁的數線、信賴區間、寬度線條全部消失；原因是手繪抖動濾鏡以物件外框計算範圍，水平線高度為 0 → 濾鏡改用 userSpaceOnUse 範圍
  - [N8 verify][不通過] 封面票根蓋住小標 → 隱藏封面小標並下移內容
  - [N8 verify][通過] 重新截圖 21 頁與首頁，圖表、數學式、模擬與小插圖都正常
- 異動頁面：lessons/sampling-clt-ci/index.html、index.html

## [2026-11-24 13:30] slides | 修正第 7、13、16、17 頁圖表在使用者瀏覽器中消失（N7、N8）

- 摘要：使用者回報第 7、13、16、17 頁的圖不見了；這四頁的圖主要由線條和不填色的曲線組成，都套用 wobble 濾鏡，上次為了修正水平線消失，把濾鏡範圍改成 6000 × 6000 的 userSpaceOnUse，Chrome 撐得住，但在高解析度螢幕上可能超過 Safari 等瀏覽器的濾鏡像素上限，導致元素整個不畫 → 改成每張圖各自產生一個貼合 viewBox（外加 10 單位邊界）的 wobble 濾鏡，放在共用的隱藏 defs 裡，避免圖表重畫時被清掉
- 檢查：
  - [N8 verify][不通過] 使用者審查：第 7、13、16、17 頁的圖消失；上次的截圖檢查只用 Chrome，沒有涵蓋使用者實際使用的瀏覽器和螢幕解析度
  - [N8 verify][通過] 用 Chrome 以 2 倍解析度重新截圖第 7、13、16、17 頁，數線、抽樣分配曲線、100 條信賴區間、區間寬度都正常顯示；Safari 待使用者確認
- 異動頁面：lessons/sampling-clt-ci/index.html

## [2026-11-24 13:35] slides | 直方圖取消扭曲效果（N7、N8）

- 摘要：使用者要求直方圖不要用扭曲效果；第 9 頁示意直方圖和第 11 頁中央極限定理模擬的直方圖改用新的 crayon-flat 濾鏡，只保留蠟筆顆粒和筆觸紋理、拿掉位移扭曲，座標軸線也不再抖動，其他圖表維持原樣
- 使用者決定：直方圖不要扭曲
- 檢查：
  - [N8 verify][不通過] 第一次截圖長條邊緣仍然歪斜，新規則的 CSS 優先順序低於原本的蠟筆規則 → 選擇器加上 .chart 提高優先順序
  - [N8 verify][通過] 用 Chrome 以 2 倍解析度重新截圖第 9、11 頁，長條邊緣筆直，蠟筆質感保留
- 異動頁面：lessons/sampling-clt-ci/index.html

## [2026-11-27 02:25] slides | 發布到 GitHub Pages（N9）

- 摘要：推送 8 個 commit（43b97bc..1777f99），內容是首頁收據卡片與轉場動畫、表格改成收銀機收據、流程方塊與重點改用蠟筆色塊、第 2、3、5 頁版面調整、中文字體統一為思源宋體、數學符號統一使用 LaTeX；使用者在 repo 設定開啟 GitHub Pages（main 分支根目錄）
- 檢查：
  - [N9 publish][通過] 推送前掃描 8 個 commit：只改到 index.html 與 lessons/sampling-clt-ci/index.html，沒有 raw/、PDF、.env，內容與 commit 訊息沒有學校名稱、學號、密碼或金鑰
  - [N9 publish][通過] 網站上線後首頁與簡報都回應 200，兩個檔案與 commit 1777f99 的內容一致，首頁「開始」與簡報「目錄」的互連正常，截圖確認首頁與第 13 頁版面正常
- 網址：https://canf1ver12.github.io/statistics-llm-wiki/
- 異動頁面：wiki/log.md

## [2026-11-28 11:12] slides | 進度紀錄：版面風格定案與首頁轉場（N7、N8）

- 摘要：2026-11-26 到 2026-11-28 的版面修改，Wiki 內容與簡報的事實都沒有變動，所有修改都已推送並發布（見上一筆 N9 紀錄）
- 使用者決定：
  - 字體定案為 H5 / S7 / B1 / T1 / R7 / L1，之後依使用者要求，所有中文（含易錯筆記與封面標籤）都改用思源宋體，移除霞鶩文楷
  - 數學式中的斜線分數改用分數寫法，內文的 n、μ、σ、E 統一改用 LaTeX；圖表 SVG 內的標籤仍是一般文字
  - 第 3 頁表格改成罐子（母體）與小碟子（樣本）插圖對照，從 A 到 E 五種樣張中選定
  - 第 5 頁重點改成框框，位置與寬度直接標在常態曲線上，σ 滑桿最小值改為 0.75
  - 表格改成收銀機收據（四種樣張中選 A），抬頭顯示表格主題，隨機三張貼紙膠帶；流程方塊改成與框框相同的蠟筆色塊
  - 第 2 頁抽樣示意圖加上圖例與重新抽樣按鈕，讓讀者看出這是模擬抽樣
  - 首頁卡片改成與內頁一致的收據，內容改為關鍵字與頁碼，加上浮起效果與收據捲起飛向使用者的轉場
  - 封面票根文字定案為 ONE SAMPLE ONLY
- 檢查：
  - [N8 verify][不通過] 使用者審查：首頁插圖第一版「沒組合在一起」→ 改成一組靜物
  - [N8 verify][不通過] 使用者審查：插圖「太集中」→ 拆成三小組
  - [N8 verify][不通過] 使用者審查：插圖「全部都在右邊很不自然」、沒有散落的小圖案、荷包蛋配草莓不合理 → 左右兩側放置合理搭配的組合，加上隨機散落的小圖案
  - [N8 verify][不通過] 使用者審查：轉場動畫先後被否決七次（掉落接不上簡報、不是朝使用者飛、太晃、有字的那面朝使用者、紙張不夠柔軟、捲起蓋螢幕的方向錯誤、沒有往使用者飛）→ 最後定為收據下緣捲起並整張飛向使用者，捲起的背面蓋滿螢幕後進入簡報，使用者表示「先這樣」
  - [N8 verify][不通過] 自動截圖：第 2 頁加上圖例後點陣圖超出頁面、首頁收據加長後壓到頁尾、第 5 頁標籤套用蠟筆濾鏡後看不清楚、收據樣張蓋到頁尾 → 都已修正並重新截圖
  - [N8 verify][通過] 修正後截圖確認第 2、3、5、6、8、9、12、13、15、17、19、20 頁與首頁版面正常；Safari 與轉場動畫的實際播放未自動測試
- 反思：轉場動畫是這輪最常被否決的項目，原因是只用文字描述動態效果時，雙方對「方向」的理解不同，改用選項加示意圖詢問後才確定；之後遇到動態效果，應先用示意圖或停格截圖確認方向，再調細節
- 異動頁面：index.html、lessons/sampling-clt-ci/index.html、wiki/log.md

## [2026-11-28 15:20] slides | 首頁轉場改為朝使用者飛出、修正浮起陰影並發布（N7、N8、N9）

- 摘要：首頁收據的轉場從「下緣捲起」改成「拿起後往右上方抽走並朝使用者飛出」，修正滑鼠移上時的陰影，Wiki 內容與簡報的事實都沒有變動
- 使用者決定：
  - 使用者認為捲起「還是很不自然」，改用可以點選播放的預覽頁比較五種轉場（現行、平穩推近、翻面推近、輕微彎曲後攤平、拿起往上帶走），使用者選「拿起往上帶走」並要求加上朝使用者飛的效果，再從放大 2.4、3.4、4.5 倍三種中選定 4.5 倍
  - 之後遇到動態效果，一律先做預覽頁讓使用者選，再改正式檔案
- 檢查：
  - [N8 verify][不通過] 使用者審查：滑鼠移上時陰影變成方塊狀、鋸齒不見，而且出現亮部分界 → 陰影改為貼近與擴散兩層，截圖確認浮起時陰影保留鋸齒輪廓，並加上 will-change 避免動畫中重新繪製
  - [N8 verify][不通過] 自動截圖：轉場途中「LESSONS・講義」標題與預告卡片浮在換色的底色上 → 讓同區塊的其他元素跟著底色淡出，重新截圖確認
  - [N8 verify][通過] 首頁平放、浮起與轉場途中的截圖正常；亮部分界在靜態截圖中無法重現，待使用者實際操作確認
  - [N9 publish][通過] 推送前掃描 2 個 commit（38b2de8、d873029）：只改到 index.html，沒有 raw/、PDF、.env，內容沒有學校名稱、學號、密碼或金鑰
  - [N9 publish][通過] 網站上線後首頁與簡報都回應 200，兩個檔案與 commit d873029 的內容一致
- 網址：https://canf1ver12.github.io/statistics-llm-wiki/
- 異動頁面：index.html、wiki/log.md
