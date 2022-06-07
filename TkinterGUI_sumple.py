# GUI構成用ライブラリ
import tkinter as tk
from tkinter import ttk

# ウィンドウの位置保存用
win_x = 100
win_y = 100

# 再実行用変数
retry = None

# 再実行停止
def stop_retry():
    global retry
    root.after_cancel(retry)
    retry = None
    # 実行ボタンの活性化と停止ボタンの非活性化
    if (main_button['state'] == tk.DISABLED):
        main_button['state'] = tk.NORMAL
    if (stop_button['state'] == tk.NORMAL):
        stop_button['state'] = tk.DISABLED

# メイン処理
def main():
    global retry
    flg = 1
    # 停止ボタンの活性化
    if (stop_button['state'] == tk.DISABLED):
        stop_button['state'] = tk.NORMAL 
    try:
        # 実行したい処理
        # 結果が得られたらflg=0を代入して処理の再実行を止める
        pass
    finally:
        if flg == 1:
            retry = root.after(5000, main)
            # 実行ボタンの非活性化
            if (main_button['state'] == tk.NORMAL):
                main_button['state'] = tk.DISABLED
    return True

# ユーザページ用
def pressed_user(event):
    global win_x, win_y
    # 親ｳｨﾝﾄﾞｳの表示位置を取得
    win_x = root.winfo_x()
    win_y = root.winfo_y()
    # ウィジェットの非表示
    root.withdraw()

    # 親ｳｨﾝﾄﾞｳに戻る
    def return_main():
        # 親ｳｨﾝﾄﾞｳの位置を子ｳｨﾝﾄﾞｳの表示位置に変更
        root.geometry('600x600+{}+{}'.format(user_root.winfo_x(), user_root.winfo_y()))
        # ウィジェットの再表示
        root.deiconify()
        # ウィジェットの破棄
        user_root.destroy()
    # GUI構成用
    user_root = tk.Tk()
    user_root.title("ユーザー設定画面")
    user_root.geometry('600x600+{}+{}'.format(win_x, win_y))
    user_root.resizable(False, False)
    
    # 保存先Key名
    keyLabel = tk.Label(user_root, text="保存先")
    keyLabel.place(x=30,y=75)
    user_list = ['user1', 'user2', 'user3']  #初期値
    keyEdit = ttk.Combobox(
        user_root,
        textvariable=tk.StringVar(),
        values=user_list,
        width=87                   #設定
        )
    keyEdit.set(user_list[0])
    keyEdit.place(x=300, y=110, anchor=tk.CENTER, height=25)

    user_mailLabel = tk.Label(user_root, text="登録メールアドレス")
    user_mailLabel.place(x=30,y=125)
    user_mailEdit = tk.Entry(user_root, width=90)
    user_mailEdit.place(x=300, y=160, anchor=tk.CENTER, height=25)

    return_btn = tk.Button(user_root, text=" ⏎ 戻る", command=return_main, font=("", 20))
    return_btn.place(x=300, y=250, anchor=tk.CENTER)
    
    user_root.protocol("WM_DELETE_WINDOW", return_main)
    keyEdit.bind("<<ComboboxSelected>>", lambda e: print(keyEdit.get()))

# 設定ページ用
def pressed_system(event):
    # 親ｳｨﾝﾄﾞｳの表示位置を取得
    win_x = root.winfo_x()
    win_y = root.winfo_y()
    # ウィジェットの非表示
    root.withdraw()

    # 親ｳｨﾝﾄﾞｳに戻る
    def return_main():
        # 親ｳｨﾝﾄﾞｳの位置を子ｳｨﾝﾄﾞｳの表示位置に変更
        root.geometry('600x600+{}+{}'.format(user_root.winfo_x(), user_root.winfo_y()))
        # ウィジェットの再表示
        root.deiconify()
        # ウィジェットの破棄
        user_root.destroy()
    # GUI構成用
    user_root = tk.Tk()
    user_root.title("システム設定画面")
    user_root.geometry('600x600+{}+{}'.format(win_x, win_y))
    user_root.resizable(False, False)
    
    # 保存先Key名
    keyLabel = tk.Label(user_root, text="実行間隔")
    keyLabel.place(x=30,y=75)
    user_list = ['5秒', '10秒', '30秒', '1分', '5分', '10分', '30分']  #初期値
    keyEdit = ttk.Combobox(
        user_root,
        textvariable=tk.StringVar(),
        values=user_list,
        width=87                   #設定
        )
    keyEdit.set(user_list[0])
    keyEdit.place(x=300, y=110, anchor=tk.CENTER, height=25)

    user_mailLabel = tk.Label(user_root, text="登録メールアドレス")
    user_mailLabel.place(x=30,y=125)
    user_mailEdit = tk.Entry(user_root, width=90)
    user_mailEdit.place(x=300, y=160, anchor=tk.CENTER, height=25)

    return_btn = tk.Button(user_root, text=" ⏎ 戻る", command=return_main, font=("", 20))
    return_btn.place(x=300, y=250, anchor=tk.CENTER)
    
    user_root.protocol("WM_DELETE_WINDOW", return_main)
    keyEdit.bind("<<ComboboxSelected>>", lambda e: print(keyEdit.get()))

# GUI構成用
root = tk.Tk()
root.title("Tkinter GUI")
root.resizable(False, False)
root.geometry('600x600+{}+{}'.format(win_x, win_y))
cvs = tk.Canvas(width=600, height=600, bg="#f5f5f5")
cvs.pack()

UrlLabel = tk.Label(text="入力フォーム１")
UrlLabel.place(x=30,y=65)
UrlEdit = tk.Entry(cvs, width=90)
UrlEdit.place(x=300, y=100, anchor=tk.CENTER, height=25)

mailLabel = tk.Label(text="コンボボックス")
mailLabel.place(x=30,y=125)
item_list = ['mail1', 'mail2', 'mail3']  #初期値
mailEdit = ttk.Combobox(
    cvs,
    textvariable=tk.StringVar(),
    values=item_list,
    width=87                   #設定
    )
mailEdit.set(item_list[0])
mailEdit.place(x=300, y=160, anchor=tk.CENTER, height=25)

passLabel = tk.Label(text="登録パスワード")
passLabel.place(x=30,y=185)
passEdit = tk.Entry(cvs, width=90)
passEdit.place(x=300, y=220, anchor=tk.CENTER, height=25)

main_button = tk.Button(cvs, text=" ▶ 実行", command=main, font=("", 20))
main_button.place(x=200, y=300, anchor=tk.CENTER)

# 停止ボタンを初期は非活性状態で配置する
stop_button = tk.Button(cvs, text=" ■ 停止", command=stop_retry, font=("", 20))
stop_button.place(x=400, y=300, anchor=tk.CENTER)
stop_button['state'] = tk.DISABLED

menu = tk.PhotoImage(file = "menu2.png")
cvs.create_image(550,40,image=menu, tags="menu")

user = tk.PhotoImage(file = "user.png")
cvs.create_image(500,40,image=user, tags="user")

# クリックされたとき
cvs.tag_bind("menu", "<ButtonPress-1>", pressed_system)
cvs.tag_bind("user", "<ButtonPress-1>", pressed_user)
mailEdit.bind("<<ComboboxSelected>>", lambda e: print(mailEdit.get()))

root.mainloop()