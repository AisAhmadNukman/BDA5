# Mengimpor modul yang dibutuhkan
import tkinter as tk
from tkinter import ttk,messagebox
from ttkbootstrap import Style

# Membuat kelas LoginWindow yang mewarisi kelas tk.Toplevel
class LoginWindow(tk.Toplevel):
    # Membuat konstruktor kelas
    def __init__(self, parent):
        # Memanggil konstruktor kelas induk
        super().__init__(parent)
        # Menyimpan referensi ke jendela induk
        self.parent = parent
        # Mengatur judul dan ukuran jendela
        self.title("Program Login")
        self.geometry("600x600")
        
        # Membuat label judul
        self.title_label = ttk.Label(self, text="Masukkan Username dan Password", font=("Arial", 16), padding=10)
        self.title_label.pack()
        # Membuat frame untuk menampung entry dan label
        self.entry_frame = ttk.Frame(self, padding=10)
        self.entry_frame.pack()
        # Membuat label admin
        self.admin_label = ttk.Label(self.entry_frame, text="Username:")
        self.admin_label.grid(row=0, column=0, sticky=tk.W)
        # Membuat entry admin
        self.admin_entry = ttk.Entry(self.entry_frame)
        self.admin_entry.grid(row=0, column=1, sticky=tk.E)
        # Membuat label password
        self.password_label = ttk.Label(self.entry_frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky=tk.W)
        # Membuat entry password
        self.password_entry = ttk.Entry(self.entry_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.E)
        # Membuat tombol login
        self.login_button = ttk.Button(self, text="Login", command=self.check_login, padding=10)
        self.login_button.pack()

    # Membuat fungsi untuk mengecek login
    def check_login(self):
        # Mendapatkan input admin dan password dari entry
        admin = self.admin_entry.get()
        password = self.password_entry.get()
        # Mengecek apakah input admin dan password sesuai dengan yang ditentukan
        if admin == "admin" and password == "1234":
            # Menampilkan pesan sukses dan membuka jendela program selanjutnya
            tk.messagebox.showinfo("Sukses", "Anda berhasil login.")
            self.parent.close_login_window()
            self.parent.open_next_window()
        else:
            # Menampilkan pesan gagal dan menghapus input entry
            tk.messagebox.showerror("Gagal", "Admin atau password salah.")
            self.admin_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
