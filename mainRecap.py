from database import *
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def open_recap(mainLogin):
    mainLogin.withdraw()
    mainRecap = tk.Tk()
    mainRecap.title("Recap")
    mainRecap.geometry("200x200")

    def close_recap():
        mainRecap.destroy()
        mainLogin.deiconify()

    label= ttk.Label(mainRecap, text="TAB Recap")
    label.pack(pady=(10, 0))

    close_button = tk.Button(mainRecap, text="Close Window", command=close_recap)
    close_button.pack(pady=(10, 0))