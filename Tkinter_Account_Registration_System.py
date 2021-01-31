from tkinter import *
import sqlite3 as db
import pyautogui

#資料庫檔案路徑
db_Path = r'.\Tkinter_Account_Registration_System.db'
conn = db.connect(db_Path)
cur = conn.cursor()
pyautogui.alert('已連接資料庫!')

#若表單不存在，就建立
cur.execute('''CREATE TABLE IF NOT EXISTS DATA
    (
        Account TEXT,
        Password TEXT
    )''' )

#註冊
def Register():
    #判斷是否輸入內容
    if Account.get() == '' or Password.get() == '':
        pyautogui.alert('尚未輸入完整內容!')
        pass
    else:
        Query()

        if Account_exist == True:
            pyautogui.alert('此帳戶已註冊,請重新輸入!')
            pass
        else:
            #新增資料
            cur.execute("insert into DATA values('{}','{}')" .format(Account.get(),Password.get()))
            conn.commit()
            pyautogui.alert('新增資料成功!')
            print('帳戶: '+Account.get())
            print('密碼: '+Password.get())

#更新
def Update():
    if Account.get() == '' or Password.get() == '':
        pyautogui.alert('尚未輸入完整內容!')
        pass
    else:      
        Query()
               
        if Account_exist == True:
            #更新資料
            cur.execute("UPDATE DATA SET Password='{}' WHERE Account='{}'".format(Password.get(),Account.get()))
            conn.commit()
            pyautogui.alert('更新資料成功!')
            print('更新密碼:'+Password.get())
        else:
            pyautogui.alert('並無此帳戶,請重新輸入!')
            pass

#查詢
def Query():
    global Account_exist
    Account_exist = False

    for data in cur.execute("SELECT Account='{}' FROM DATA".format(Account.get())):
        if 1 in data:        
            Account_exist = True
            break
        else:        
            Account_exist = False
            continue

        
#創建tkinter
main = Tk()

#取得程式視窗位置
Window_Width = main.winfo_reqwidth()
Window_Height = main.winfo_reqheight()

#取得螢幕中央位置
Screen_Width = int(main.winfo_screenwidth()/2 - Window_Width/2)
Screen_Height = int(main.winfo_screenheight()/2 - Window_Height/2)

#將程式視窗顯示在螢幕中央
main.geometry("+{}+{}".format(Screen_Width, Screen_Height))

#視窗設定
main.resizable(0,0) #固定視窗大小

#標籤
Label(main,text='帳戶: ').grid(row=0,column=0)
Label(main,text='密碼: ').grid(row=1,column=0)
Label(main,text='註冊: ').grid(row=2,column=0) 
Label(main,text='更新: ').grid(row=3,column=0)             

#設為字串
Account = StringVar()
Password = StringVar()

#文字框
Entry(main,textvariable=Account).grid(row=0,column=1)
Entry(main,textvariable=Password).grid(row=1,column=1)

#按鈕
Btn = Button(main,width=20,height=1,text='註冊',command=Register)
Btn.grid(row=2,column=1)
Btn = Button(main,width=20,height=1,text='更新',command=Update)
Btn.grid(row=3,column=1)


mainloop()
