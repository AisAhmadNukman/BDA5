# Mengimpor modul yang dibutuhkan
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import database as db
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Membuat kelas NextWindow yang mewarisi kelas tk.Toplevel
class NextWindow(tk.Toplevel):
    # Membuat konstruktor kelas
    def __init__(self, parent):
        # Memanggil konstruktor kelas induk
        super().__init__(parent)
        # Menyimpan referensi ke jendela induk
        self.parent = parent
        # Mengatur judul dan ukuran jendela
        self.title("Program Selanjutnya")
        self.geometry("300x200")
        # Membuat gaya ttk bootstrap
        self.style = Style(theme="darkly")
        # Membuat dan menampilkan elemen-elemen antarmuka pengguna
        self.create_widgets()

    def create_widgets(self):
         # comboBox
        # hri
        label_day = ttk.Label(self, text="Hari:")
        label_day.pack(pady=(10, 0))
        self.chosen_day = tk.StringVar()
        hari = ttk.Combobox(self, width=27, textvariable=self.chosen_day)
        hari['values'] = ('Senin',
                          'Selasa',
                          'Rabu',
                          'Kamis',
                          'Jumat')
        hari.pack()
        hari.current()

        # jam
        label_hour = ttk.Label(self, text="Jam:")
        label_hour.pack(pady=(10, 0))
        self.chosen_hour = tk.StringVar()
        hour = ttk.Combobox(self, width=27, textvariable=self.chosen_hour)
        hour['values'] = ('7.0',
                          '12.0',
                          '16.0')
        hour.pack()
        hour.current()

        label_type = ttk.Label(self, text="Jenis Kendaraan:")
        label_type.pack(pady=(10, 0))
        self.chosen_type = tk.StringVar()
        type = ttk.Combobox(self, width=27, textvariable=self.chosen_type)
        type['values'] = ('Sepeda Motor',
                          'Mobil',
                          'Sepeda')
        type.pack()
        type.current()

        self.hitung_button = ttk.Button(self, text="Hitung Rekomendasi", command=self.hitung_rekomendasi)
        self.hitung_button.pack(pady=(10, 20))

        self.hasil_label = ttk.Label(self, text="")
        self.hasil_label.pack()

        self.hasil_text = tk.Text(self, height=6, width=50, state=tk.DISABLED)
        self.hasil_text.pack()

        self.rekomendasi_label = ttk.Label(self, text="")
        self.rekomendasi_label.pack()

        self.rekomendasi_text = tk.Text(self, height=6, width=50, state=tk.DISABLED)
        self.rekomendasi_text.pack()

        if self.parent.login_window is not None and self.parent.login_window.admin_entry.get() == "admin":
            # Membuat jendela baru
            self.next_button = ttk.Button(self, text="Rekap Data", command=self.open_next_program)
            self.next_button.pack(pady=(10, 20))

    def hitung_rekomendasi(self):
        hari_input = self.chosen_day.get()
        jam_input = float(self.chosen_hour.get())
        jenis_kendaraan_input = self.chosen_type.get()

        filtered_data = db.df[(db.df['hari'] == hari_input) & (db.df['jam'] == jam_input) & (db.df['jenis_kendaraan'] == jenis_kendaraan_input)]
        rata_rata = filtered_data.groupby(['area'])['jumlah_kendaraan'].mean()
        hasil_rata_rata = rata_rata.apply(db.tambahkan_label)

        self.hasil_label.config(text=f"Hasil pada hari {hari_input} jam {jam_input}:")
        self.hasil_text.config(state=tk.NORMAL)
        self.hasil_text.delete(1.0, tk.END)
        self.hasil_text.insert(tk.END, hasil_rata_rata.to_string())
        self.hasil_text.config(state=tk.DISABLED)

        parkiran_sepi = db.rekomendasi_parkiran_sepi(hasil_rata_rata)
        self.rekomendasi_label.config(text="Rekomendasi parkiran dengan label Sepi:")
        self.rekomendasi_text.config(state=tk.NORMAL)
        self.rekomendasi_text.delete(1.0, tk.END)
        self.rekomendasi_text.insert(tk.END, "\n".join(parkiran_sepi))
        self.rekomendasi_text.config(state=tk.DISABLED)


    def open_next_program(self):
        new_window = tk.Tk()
        new_window.title("Program Selanjutnya")
        new_window.geometry("300x200")
        # Membuat label teks
        text_label = ttk.Label(new_window, text="Rekap Data.", padding=10)
        text_label.pack()

        data_api = db.ambil_data()

        # Cek apakah data berhasil diambil
        if data_api:
            # Gunakan data dari API
            df = pd.DataFrame(data_api)

            hari_input = self.chosen_day.get()
            jam_input = float(self.chosen_hour.get())
            jenis_kendaraan_input = self.chosen_type.get()

            filtered_data = df[(df['hari'] == hari_input) & (df['jam'] == jam_input) & (df['jenis_kendaraan'] == jenis_kendaraan_input)]

            # Perbarui nama kolom
            filtered_data = filtered_data.rename(columns={"jenis": "jenis_kendaraan", "jumlah": "jumlah_kendaraan"})

            # Buat pivot table untuk membuat line chart
            pivot_df = filtered_data.pivot_table(index=['tanggal'], columns=['jenis_kendaraan'], values='jumlah_kendaraan', aggfunc='sum')

            # Buat line chart
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(1, 1, 1)
            pivot_df.plot(kind='line', ax=ax)  # Ganti kind='bar' dengan kind='line'

            # Menambahkan label dan judul
            ax.set_xlabel('Tanggal')
            ax.set_ylabel('Jumlah Kendaraan')
            ax.set_title('Jumlah Kendaraan per Hari Berdasarkan Jenis')

            # Menambahkan legenda
            ax.legend(title='Jenis Kendaraan', loc='upper right')

            # Menambahkan canvas untuk menampilkan chart
            canvas = FigureCanvasTkAgg(fig, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        else:
            print("Data tidak dapat diambil. Perbaiki masalah koneksi atau URL.")

