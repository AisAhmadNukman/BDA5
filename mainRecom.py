from database import *
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def open_recom(main):
    main.withdraw()
    mainRecom = tk.Tk()
    mainRecom.title("Recommendation")
    mainRecom.geometry("200x200")
    
    def close_recom():
        mainRecom.destroy()
        main.deiconify()
    
    label= ttk.Label(mainRecom, text="TAB Rekomendasi")
    label.pack(pady=(10, 0))

    close_button = tk.Button(mainRecom, text="Close Window", command=close_recom)
    close_button.pack(pady=(10, 0))