import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import classes

# Functions
def close_app():
    window.destroy()

def submit():
    area = chosen_area.get()
    hari = chosen_hari.get()
    jam = chosen_jam.get()
    jumlah = "..."
    kepadatan = "..."
    show_area.config(text=f"Area: {area}")
    show_hari.config(text=f"Hari: {hari}")
    show_jam.config(text=f"Jam: {jam}")
    show_jumlah.config(text=f"Perkiraan jumlah kendaraan: {jumlah}")
    show_kepadatan.config(text=f"Perkiraan kepadatan: {kepadatan}")

# main windows
window = Tk()
window.title("Tkinter Window")
window.geometry("600x450")

hasil = Tk()

# Combobox
# area
Label(text="Pilih area parkir:").grid(row=0, column=0)
chosen_area = tk.StringVar()
area = ttk.Combobox(window, width = 27, textvariable = chosen_area)
area['values'] = (' FST', 
                  ' FISIP',
                  ' FPK',
                  ' Danau',
                  ' Masjid')
area.grid(row=0, column=1)
area.current()
# hari
label = tk.Label(window, text="Pilih hari:")
label.grid(row=1, column=0)
chosen_hari = tk.StringVar()
hari = ttk.Combobox(window, width = 27, textvariable = chosen_hari)
hari['values'] = (' Senin', 
                  ' Selasa',
                  ' Rabu',
                  ' Kamis',
                  ' Jumat')
hari.grid(row=1, column=1)
hari.current()
# jam
label = tk.Label(window, text="Pilih jam:")
label.grid(row=2, column=0)
chosen_jam = tk.StringVar()
jam = ttk.Combobox(window, width = 27, textvariable = chosen_jam)
jam['values'] = (' 07:00', 
                  ' 12.00',
                  ' 16.00')
jam.grid(row=2, column=1)
jam.current()

# submit
submit_button = ttk.Button(window, text="Submit", command=submit, bootstyle=PRIMARY)
submit_button.grid(row=3, column=1)

# show result
show_area = tk.Label(window, text="")
show_area.grid()
show_hari = tk.Label(window, text="")
show_hari.grid()
show_jam = tk.Label(window, text="")
show_jam.grid()
show_jumlah = tk.Label(window, text="")
show_jumlah.grid()
show_kepadatan = tk.Label(window, text="")
show_kepadatan.grid()

# close app
close_button = ttk.Button(window, text="Close App", command=close_app, bootstyle=DANGER)
close_button.grid(row=6, column=3)

# Start the Tkinter event loop
window.mainloop()