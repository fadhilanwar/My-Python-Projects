import pandas as pd

# Membuat Tabel(Baris, Kolom) dari sebuah Series


series1 = ("Harry Potter", "Detective Conan", "Doraemon")
series2 = (20, 4, 14)
series3 = ("Tidak Tersedia", "Tersedia", "Tidak Tersedia")

dataFrameSeries = pd.DataFrame({
    "Judul Buku": series1,
    "Stok": series2,
    "Status": series3
})

print(dataFrameSeries)
