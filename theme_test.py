# import tkinter as tk
# from tkinter import ttk

# def change_theme():
#     selected_theme = theme_combobox.get()
#     if selected_theme == "Light":
#         root.tk_setPalette(background='#FFFFFF', foreground='#000000')
#     elif selected_theme == "Dark":
#         root.tk_setPalette(background='#2E2E2E', foreground='#FFFFFF')
#     # 추가적으로 다른 테마에 대한 설정을 추가할 수 있습니다.

# root = tk.Tk()
# root.title("Color Theme Changer")

# # 테마 선택 콤보박스 생성
# themes = ["Light", "Dark"]
# theme_label = tk.Label(root, text="Select Theme:")
# theme_label.pack(pady=10)
# theme_combobox = ttk.Combobox(root, values=themes)
# theme_combobox.set(themes[0])  # 초기값 설정
# theme_combobox.pack(pady=10)

# # 테마 변경 버튼 생성
# change_button = tk.Button(root, text="Change Theme", command=change_theme)
# change_button.pack(pady=10)

# root.mainloop()


# # Darktheme 구성

import tkinter as tk
from tkinter import ttk

def set_dark_theme(widget):
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('.', background='#2E2E2E', foreground='#FFFFFF')
    style.configure('TButton', background='#404040', foreground='#FFFFFF')
    style.map('TButton', background=[('active', '#606060')])
    widget.configure(bg='#2E2E2E')

root = tk.Tk()
root.title("Dark Theme Example")

root.configure(bg='#2E2E2E')
set_dark_theme(root)

# 여기에 다양한 위젯 및 레이아웃 추가 가능

root.mainloop()