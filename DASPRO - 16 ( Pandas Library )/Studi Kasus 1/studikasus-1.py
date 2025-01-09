'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
NIM : 2407136
'''

import pandas as pd
import shutil

columns, _ = shutil.get_terminal_size()
def longLine():
    print("="*columns)
    
def newLine():
    print("\n")



# Buatlah file csv yang sudah didownload ke dalam dataframe dan Tampilkan hanya 10 data teratasnya saja
csvFile = pd.read_csv("files/Daftar_Mahasiswa_2018.csv")
longLine()
print("(1.) Berikut.. 10 Data Teratas didalam File Daftar_Mahasiswa_2018.csv:")
longLine()
print(csvFile.head(10))
longLine()

newLine()
longLine()

# Sorting dataframe tersebut berdasarkan kolom Nama
print("(2.) Berikut.. Sorting Data berdasarkan kolom ['Nama']")
longLine()
sortByName = csvFile.sort_values(by=['Nama'])
print(sortByName.head(10))
longLine()


newLine()
longLine()


# Data yang ditampilkan hanya kolom NIM, Nama, L/P, Status, SKS, IP dan Lama Studi(Smt) saja
print("(3.) Berikut.. Filter Data yang ditampilkan hanya kolom NIM, Nama, L/P, Status, SKS, IP dan Lama Studi(Smt) saja")
filterData = csvFile.filter(items=['NIM', 'Nama', 'L/P', 'SKS', 'IPK', 'Lama Studi(Smt)'])
longLine()
print(filterData.head(10))
longLine()

newLine()
longLine()


# Hitung berapa nilai rata-rata dari seluruh IPK mahasiswa tersebut?
print("(4.) Berikut.. Nilai Rata-rata IPK seluruh Mahasiswa tahun 2018")
longLine()
avg = csvFile['IPK'].mean()
print(f"Average IPK: {avg}.")

longLine()


newLine()
longLine()

# Hitung berapa jumlah mahasiswa laki-laki? dan berapa jumlah mahasiswa perempuan?
print("(5.) Berikut.. Jumlah Mahasiswa dengan Gendeer Laki-laki dan Perempuan (L/P)")
longLine()
count_gender = csvFile['L/P'].value_counts()

count_L = count_gender['L']
count_P = count_gender['P']

print(f"Jumlah Mahasiswa (L): {count_L}")
print(f"Jumlah Mahasiswa (P): {count_P}")

longLine()

newLine()
longLine()


# Tampilkan hanya data mahasiswa perempuan dengan status “Terdaftar” saja
print("(6.) Berikut.. Menampilkan data mahasiswa yang Terdaftar saja")
longLine()

mhsTerdaftar = csvFile[csvFile['Status'] == 'Terdaftar']
print(mhsTerdaftar.head(10))
longLine()

newLine()
longLine()


# Tampilkan seluruh data mahasiswa dengan status bukan “Terdaftar”
print("(7.) Berikut.. Menampilkan data mahasiswa yang Selain Terdaftar saja")
longLine()
mhsTerdaftar = csvFile[csvFile['Status'] != 'Terdaftar']
print(mhsTerdaftar.head(10))
longLine()


