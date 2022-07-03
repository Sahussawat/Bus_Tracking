import tkinter as tk
from tkinter


root = tk.Tk()

def on_closing():
   

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()