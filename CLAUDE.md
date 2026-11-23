@AGENTS.md

# Claude Code 專用補充

## 讀取 PDF

- 第一次使用前先建立環境：`python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
- 讀文字層：`.venv/bin/python tools/extract_text.py "raw/stat chap 7 ppt.pdf" 50 56`
- 轉成圖片：`.venv/bin/python tools/render_pages.py "raw/統計筆記.pdf" notes 20-22`，再用 Read 工具打開 `raw/rendered/notes/p020.png` 看圖
- 一次不要看太多張圖片，先用文字層找出相關頁碼，再只轉需要的頁面

## 互動

- N2 討論和 N6 大綱確認一定要停下來等使用者回覆，不能自己判斷「應該沒問題」就繼續
- 回覆使用者時，用條列列出重點、預計異動的頁面、衝突或疑點，讓使用者可以逐項確認或修正
