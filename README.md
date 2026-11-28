# 統計學 LLM Wiki

參考 Karpathy 的 LLM Wiki 做法，把統計學課堂講義和手寫筆記整理成由 LLM 維護的 Markdown 知識庫，再以這個 Wiki 為唯一知識來源，產生給初學者看的教學 HTML 簡報

本輪主題是「抽樣分配、中央極限定理與信賴區間」

## 功能 (Features)

- **LLM Wiki**：6 份來源（講義第 3a、3b、6、7、8 章與手寫筆記）整理成 16 個概念頁，每個事實都標有講義頁碼
- **來源衝突處理**：講義筆誤、手寫筆記和講義不一致的地方，都記在概念頁的「矛盾與待確認」和來源頁的「疑點」
- **檢查流程**：ingest、query、產生簡報分成 N1 到 N9 九個節點，每次檢查的結果都記在 `wiki/log.md`
- **Wiki lint 工具**：自動檢查壞連結、孤兒頁、index 遺漏、缺少引用、中文句號、emoji、中國用語
- **教學簡報**：21 頁，每頁標出對應的 Wiki 頁面，包含常態曲線、中央極限定理、信賴區間 3 個互動模擬

## 使用技術 (Tech Stack)

- Python 3.12（讀取講義 PDF、Wiki lint）
- pypdf 7.1.1、PyMuPDF 2.1
- HTML、CSS、JavaScript（簡報，不使用框架）
- KaTeX 0.16.9（簡報中的數學式）
- Claude Code（維護 Wiki 的 LLM agent，規範寫在 `AGENTS.md`）

## 安裝與執行 (Getting Started)

### 環境需求

- Python 3.12
- 瀏覽器（Chrome、Edge、Safari 等）

### 安裝步驟

```bash
git clone https://github.com/canf1ver12/statistics-llm-wiki.git
cd statistics-llm-wiki
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

講義 PDF 有版權，沒有放進 repo，`raw/` 資料夾要自己準備，檔名對照見 `AGENTS.md` 第 4 節

### 啟動

簡報是靜態網頁，直接用瀏覽器打開根目錄的 `index.html` 即可，在 macOS 上可以執行：

```bash
open index.html
```

線上版：

- 講義目錄：https://canf1ver12.github.io/statistics-llm-wiki/
- 簡報：https://canf1ver12.github.io/statistics-llm-wiki/lessons/sampling-clt-ci/index.html

## 使用方式 (Usage)

### 瀏覽 Wiki

從 [wiki/index.md](wiki/index.md) 開始，概念之間的先後關係見 [wiki/overview.md](wiki/overview.md)，製作與檢查的完整過程見 [wiki/log.md](wiki/log.md)

### 簡報操作

- ← → 或空白鍵翻頁，手機可以左右滑動
- 網址加上 `#頁碼` 可以直接打開某一頁，例如 `lessons/sampling-clt-ci/index.html#11`
- 每頁左下角的連結會打開對應的 Wiki 頁面

### 讀取講義 PDF

```bash
# 讀取第 50 到 56 頁的文字層
.venv/bin/python tools/extract_text.py "raw/stat chap 7 ppt.pdf" 50 56

# 把手寫或圖表頁轉成圖片，輸出到 raw/rendered/ch7/
.venv/bin/python tools/render_pages.py "raw/stat chap 7 ppt.pdf" ch7 50-56
```

### 用 LLM 維護 Wiki

用 Claude Code 打開這個資料夾，它會讀取 `CLAUDE.md` 和 `AGENTS.md`，照裡面的流程 ingest 新來源、回答問題或產生簡報

## 專案結構 (Project Structure)

```
.
├── AGENTS.md              # Wiki 的 schema：架構、頁面規範、N1 到 N9 流程、log 格式
├── CLAUDE.md              # 引用 AGENTS.md，加上 Claude Code 專用的補充
├── index.html             # 簡報目錄
├── lessons/
│   └── sampling-clt-ci/   # 教學簡報
├── wiki/
│   ├── index.md           # Wiki 目錄
│   ├── overview.md        # 概念鏈總覽
│   ├── log.md             # 時間序的製作與檢查紀錄
│   ├── sources/           # 每份來源的摘要頁
│   ├── concepts/          # 概念頁
│   └── outputs/           # query 的產出，例如簡報大綱
├── tools/                 # 讀取 PDF、Wiki lint 的腳本
└── requirements.txt
```

## 測試 (Testing)

這個專案沒有單元測試，Wiki 的格式檢查用 lint 工具：

```bash
.venv/bin/python tools/lint_wiki.py
```

全部項目顯示 `[PASS]` 代表通過，有問題時會列出檔案和行號

## 授權 (License)

TODO: 選定授權方式

課堂講義的版權屬於原作者與出版社，不在本 repo 內
