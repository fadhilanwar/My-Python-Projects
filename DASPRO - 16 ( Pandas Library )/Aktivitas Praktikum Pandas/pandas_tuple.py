import pandas as pd

# Membuat Tabel(Baris, Kolom) dari Tipe Data Tuple


tuple1 = ('Harry Potter', 20)
tuple2 = ('Detective Conan', 4)
tuple3 = ('Doraemon', 14)

dataFrameTuple = pd.DataFrame(
    [tuple1, tuple2, tuple3], columns=["Judul Buku", "Stok"])

print(dataFrameTuple)
