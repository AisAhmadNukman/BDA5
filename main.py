# from ui import *
from database import *
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

from mainRecom import open_recom
from mainLogin import open_login

# Create the main window
main = tk.Tk()
main.title("Main")
main.geometry("200x200")
style = Style(theme="journal")

# create label
label_day = ttk.Label(main, text="Pilih jenis akun")
label_day.pack(pady=(10, 0))

# Create a button in the main window
buttonRecom = tk.Button(main, text="Admin", command=lambda: open_login(main), width=15, height=2)
buttonRecom.pack(pady=(10, 0))
buttonRecap = tk.Button(main, text="Anonymous", command=lambda: open_recom(main), width=15, height=2)
buttonRecap.pack(pady=(10, 0))

# Start the main loop
main.mainloop()
