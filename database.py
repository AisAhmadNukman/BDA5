import pandas as pd

# Data Dummy
data = [
    ["Senin", "07.00", "FST", "Sepeda", 50],
    ["Senin", "07.00", "FST", "Motor", 100],
    ["Senin", "07.00", "FST", "Mobil", 80],
    ["Senin", "07.00", "Masjid", "Sepeda", 8],
    ["Senin", "07.00", "Masjid", "Motor", 10],
    ["Senin", "07.00", "Masjid", "Mobil", 50],
    ["Senin", "07.00", "Danau", "Sepeda", 9],
    ["Senin", "07.00", "Danau", "Motor", 390],
    ["Senin", "07.00", "Danau", "Mobil", 7],
    ["Senin", "07.00", "FISIP", "Sepeda", 5],
    ["Senin", "07.00", "FISIP", "Motor", 50],
    ["Senin", "07.00", "FISIP", "Mobil", 10],
    ["Senin", "07.00", "FPK", "Sepeda", 13],
    ["Senin", "07.00", "FPK", "Motor", 290],
    ["Senin", "07.00", "FPK", "Mobil", 20],
]

df = pd.DataFrame(data, columns=["hari", "jam", "area", "jenis", "jumlah"])
df['jam'] = df['jam'].astype(float)

def tambahkan_label(rata_rata):
    if rata_rata <= 100:
        return "Sepi"
    elif rata_rata <= 170:
        return "Renggang"
    else:
        return "Padat"

def rekomendasi_parkiran_sepi(hasil_rata_rata):
    sepi_data = hasil_rata_rata[hasil_rata_rata == "Sepi"]
    return sepi_data.index.get_level_values('area').unique()