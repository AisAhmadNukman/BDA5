import pandas as pd
import requests

# Fungsi untuk mengambil data dari URL
def ambil_data():
    url = "https://2djncpz1-5001.asse.devtunnels.ms/ambildata"  # Ganti dengan URL API Anda
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('parkir_data', [])
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
        return None

# Ambil data dari URL
data_api = ambil_data()

# Cek apakah data berhasil diambil
if data_api:
    # Gunakan data dari API
    df = pd.DataFrame(data_api)
    df['jam'] = df['jam'].astype(float)

    def tambahkan_label(rata_rata):
        if rata_rata <= 50:
            return "Sepi"
        elif rata_rata <= 100:
            return "Renggang"
        else:
            return "Padat"

    def rekomendasi_parkiran_sepi(hasil_rata_rata):
        sepi_data = hasil_rata_rata[hasil_rata_rata == "Sepi"]
        return sepi_data.index.get_level_values('area').unique()

    # Gunakan df untuk analisis lebih lanjut
    print(df)
else:
    print("Data tidak dapat diambil. Perbaiki masalah koneksi atau URL.")
