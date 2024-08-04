import tkinter as tk
from tkinter.font import Font
# 創建主窗口
root = tk.Tk()
root.title("show all data")
# 設置視窗大小
root.geometry("600x600")
# 使用 grid 佈局
font_2=Font(family="標楷體", size=12)
custom_font = Font(family="標楷體", size=16)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


