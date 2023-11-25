# Mengimpor modul yang dibutuhkan
import tkinter as tk
from tkinter import ttk,messagebox
from ttkbootstrap import Style
from login import LoginWindow
from rekomendasi import NextWindow

# Membuat kelas Program yang mewarisi kelas tk.Tk
class Program(tk.Tk):
    # Membuat konstruktor kelas
    def __init__(self):
        # Memanggil konstruktor kelas induk
        super().__init__()
        # Membuat gaya ttk bootstrap
        self.title("Program Login")
        self.geometry("300x200")
        self.style = Style(theme="darkly")
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TEntry", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))
        # Membuat frame utama
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
      


        # Membuat frame untuk menampung tombol opsi
        self.button_frame = ttk.Frame(self.main_frame, padding=150)
        self.button_frame.pack()

    # Membuat tombol opsi admin
        self.admin_button = ttk.Button(self.button_frame, text="Admin", command=self.open_login_window)
        self.admin_button.grid(row=30, column=0, padx=5, pady=50)

    # Membuat tombol opsi guest
        self.guest_button = ttk.Button(self.button_frame, text="Guest", command=self.open_next_window)
        self.guest_button.grid(row=30, column=1, padx=5, pady=50)

        # Membuat variabel untuk menyimpan jendela login
        self.login_window = None
        # Membuat variabel untuk menyimpan jendela program selanjutnya
        self.next_window = None

    # Membuat fungsi untuk menangani pilihan opsi
    def choose_option(self):
        # Menampilkan pesan sesuai dengan opsi yang dipilih
        tk.messagebox.showinfo("Guest", "Anda memilih opsi guest.")

    # Membuat fungsi untuk membuka jendela login
    def open_login_window(self):
        # Mengecek apakah jendela login sudah ada
        if self.login_window is None:
            # Membuat jendela login baru
            self.login_window = LoginWindow(self)
        else:
            # Menampilkan jendela login yang sudah ada
            self.login_window.deiconify()

    # Membuat fungsi untuk menutup jendela login
    def close_login_window(self):
        # Mengecek apakah jendela login ada
        if self.login_window is not None:
            # Menyembunyikan jendela login
            self.login_window.withdraw()

    # Membuat fungsi untuk membuka jendela program selanjutnya
    def open_next_window(self):
        # Mengecek apakah jendela program selanjutnya sudah ada
        if self.next_window is None:
            # Membuat jendela program selanjutnya baru
            self.next_window = NextWindow(self)
        else:
            # Menampilkan jendela program selanjutnya yang sudah ada
            self.next_window.deiconify()

    # Membuat fungsi untuk menutup jendela program selanjutnya
    def close_next_window(self):
        # Mengecek apakah jendela program selanjutnya ada
        if self.next_window is not None:
            # Menyembunyikan jendela program selanjutnya
            self.next_window.withdraw()

# Membuat objek program
program = Program()
# Menjalankan program
program.mainloop()
