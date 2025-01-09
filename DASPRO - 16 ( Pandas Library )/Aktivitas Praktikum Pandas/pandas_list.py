import pandas as pd

# Membuat Tabel(Baris, Kolom) dari Tipe Data List

list1 = ['Andi', 'Beni', 'Chika', 'Dodo']
list2 = ['RPL', 'Multimedia', 'PGSD', 'PGPAUD']
list3 = [3.81, 3.21, 2.74, 2.65]


dataFrameList = pd.DataFrame(list(zip(list1, list2, list3)),
                             columns=['Nama', 'Prodi', 'IPK'])

print(dataFrameList)