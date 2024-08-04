import tkinter as tk
from tkinter import filedialog
from set import *
from app_catch import write_folder_contents as wfc
class main():
    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.entry.delete(0, tk.END,)  # 清空輸入框
            self.entry.insert(0, folder_path)  # 插入選擇的資料夾路徑
            self.action_button.config(state=tk.NORMAL)  # 啟用按鈕
    def load_folder(self):
        path=self.entry.get()
        self.text_output.delete('1.0',tk.END)
        wfc(folder_path=path,output=self.text_output)
    def check_entry(self, event=None):
        if self.entry.get().strip():
            self.action_button.config(state=tk.NORMAL)
        else:
            self.action_button.config(state=tk.DISABLED)
    def button_click(self):
        self.entry = tk.Entry(root,font=font_2)
        self.entry.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="ew") #padx=(左，右)
        self.entry.bind("<KeyRelease>", self.check_entry)

        self.button = tk.Button(root, text="OPEN FOLDER", command=self.open_folder,font=font_2)
        self.button.grid(row=0, column=1, padx=(0, 10), pady=5, sticky="ew")

        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        self.text_output = tk.Text(root,font=custom_font,bg="#D3D3D3",yscrollcommand=self.scrollbar.set)
        self.text_output.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")
        self.scrollbar.config(command=self.text_output.yview)

        self.action_button = tk.Button(root, text="START", state=tk.DISABLED,command=self.load_folder,font=custom_font)
        self.action_button.grid(row=2, column=0, columnspan=2, pady=10)
    def update(self):
        self.button_click()

        