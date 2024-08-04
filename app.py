from set import *
from base import main
base_main=main()
base_main.update()
def on_closing():
    root.quit()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()