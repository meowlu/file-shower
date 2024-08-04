import os
import tkinter as tk
from tkinter import messagebox
from set import *
def write_folder_contents(folder_path,output,indent_level=0):
    if not os.path.exists(folder_path):
            show_error(f"Error: The folder '{folder_path}' does not exist.\nPlease check the path and try again.")
            return
    output.tag_configure("file_tag", foreground="black")
    output.tag_configure("folder_tag", foreground="blue")
    try:
        for subdir, dirs, files in os.walk(folder_path):
            if subdir == folder_path:
                dirs.sort()
                files.sort()
                for file in files:
                    output.insert("end", f"{'  ' * indent_level}file: {file}\n",'file_tag')
                for dir in dirs:
                    sub_subdir = os.path.join(subdir, dir)
                    output.insert("end", f"{'  ' * indent_level}folder: {dir}\n","folder_tag")
                    write_folder_contents(sub_subdir, output, indent_level + 2)
            break
    except PermissionError as e:
        show_error(f"Permission error: {e}\nPlease check the permissions of the file or directory and ensure the program is run as an administrator.")
def show_error(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Permission error", message)