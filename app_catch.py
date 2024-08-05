import os
import tkinter as tk
from tkinter import messagebox
from set import *
def open_folder(path):
    import platform
    os_name=platform.system()
    if os_name == "Windows":
        os.startfile(path)
    elif os_name == "Darwin":
        os.system(f'open "{path}"')
    elif os_name == "Linux":
        os.system(f'xdg-open "{path}"')
def write_folder_contents(folder_path,output,indent_level=0):
    if not os.path.exists(folder_path):
            show_error(f"Error: The folder '{folder_path}' does not exist.\nPlease check the path and try again.")
            return
    output.tag_configure("file_tag", foreground="black")
    output.tag_configure("folder_tag", foreground="blue", underline=True)
    try:
        for subdir, dirs, files in os.walk(folder_path):
            if subdir == folder_path:
                dirs.sort()
                files.sort()
                for file in files:
                    output.insert("end", f"{'  ' * indent_level}file: {file}\n",'file_tag')
                for dir in dirs:
                    output.insert("end", f"{'  ' * indent_level}")
                    sub_subdir = os.path.join(subdir, dir)
                    start_index = output.index(f"end-1c linestart+{indent_level * 2} chars")
                    output.insert("end", f"folder: {dir}")
                    end_index = output.index("end-1c lineend")
                    output.insert("end",'\n')
                    output.tag_add("folder_tag", start_index, end_index)
                    output.tag_bind('folder_tag', "<Button-1>", lambda e, path=sub_subdir: open_folder(path))
                    output.tag_bind('folder_tag', "<Enter>", lambda e: output.config(cursor="hand2"))
                    output.tag_bind('folder_tag', "<Leave>", lambda e: output.config(cursor=""))
                    write_folder_contents(sub_subdir, output, indent_level + 2)
            break
    except PermissionError as e:
        show_error(f"Permission error: {e}\nPlease check the permissions of the file or directory and ensure the program is run as an administrator.")
def show_error(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Permission error", message)
