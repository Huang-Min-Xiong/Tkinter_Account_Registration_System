#### 安裝所需套件
`pip install -r requirements.txt`

#### 透過tkinter套件來實作功能
GUI設計
- Label:標籤
- Entry:文字框
- Button:按鈕

#### 透過sqlite3套件來實作功能
資料庫

- 初始設定

  conn=db.connect(db_Path)

  cur=conn.cursor()
- db.connect(): 連接資料庫
- conn.cursor(): 建立 Cursor 物件
- cur.execute(): 執行 SQL 指令

#### 透過pyautogui套件來實作功能
- pyautogui.alert(): 顯示消息視窗

#### 程式主要功能
- Register(): 註冊
- Update(): 更新
- Query(): 查詢
