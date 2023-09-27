import tkinter as tk
from tkinter import ttk

# Function
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
window = tk.Tk()
window.title("Tkinter Window")
window.geometry("600x450")

# Combobox
# area
label = tk.Label(window, text="Pilih area parkir:")
label.pack()
chosen_area = tk.StringVar()
area = ttk.Combobox(window, width = 27, textvariable = chosen_area)
area['values'] = (' FST', 
                  ' FISIP',
                  ' FPK',
                  ' Danau',
                  ' Masjid')
area.pack()
area.current()
# hari
label = tk.Label(window, text="Pilih hari:")
label.pack()
chosen_hari = tk.StringVar()
hari = ttk.Combobox(window, width = 27, textvariable = chosen_hari)
hari['values'] = (' Senin', 
                  ' Selasa',
                  ' Rabu',
                  ' Kamis',
                  ' Jumat')
hari.pack()
hari.current()
# jam
label = tk.Label(window, text="Pilih jam:")
label.pack()
chosen_jam = tk.StringVar()
jam = ttk.Combobox(window, width = 27, textvariable = chosen_jam)
jam['values'] = (' 07:00', 
                  ' 12.00',
                  ' 16.00')
jam.pack()
jam.current()

# submit
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# show result
show_area = tk.Label(window, text="")
show_area.pack()
show_hari = tk.Label(window, text="")
show_hari.pack()
show_jam = tk.Label(window, text="")
show_jam.pack()
show_jumlah = tk.Label(window, text="")
show_jumlah.pack()
show_kepadatan = tk.Label(window, text="")
show_kepadatan.pack()

# close app
close_button = tk.Button(window, text="Close App", command=close_app)
close_button.pack()

# Start the Tkinter event loop
window.mainloop()