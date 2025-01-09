'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
NIM : 2407136
'''

'''
RIna merupakan seorang pemilik online shop ternama. Ia memiliki dataset yang mencakup informasi penjualan
selama beberapa bulan. Dataset tersebut merupakan file CSV yang terdiri dari kolom-kolom berikut:

Tanggal: Tanggal transaksi dari bulan Januari-Desember 2023.
Produk: Nama produk yang dijual.
Kategori: Kategori produk (terdiri dari 3 kategori)
Harga: Harga satuan produk.
Jumlah: Jumlah produk yang terjual.
Total: Total pendapatan dari transaksi.


Buatlah dengan menggunakan Pandas:
Total pendapatan setiap bulannya,
Rata-rata pendapatan 2023,
Pendapatan paling sedikit dan paling banyak,
Produk terlaris yang paling banyak terjual

Note: silahkan buat dummy dataset sebanyak 50 data
'''

import pandas as pd
import shutil

columns, _ = shutil.get_terminal_size()
def longLine():
    print("="*columns)
    
def newLine():
    print("\n")

csvFile = pd.read_csv("files/laporan_penjualan.csv")

longLine()
print("Data Penjualan Warung Rini Tahun 2023")
longLine()


print(csvFile)
longLine()

newLine()
longLine()

print("Data Rata-Rata Perbulan")
longLine()

csvFile['Tanggal'] = pd.to_datetime(csvFile['Tanggal'])

csvFile['bulan'] =  csvFile['Tanggal'].dt.to_period('M')


avg_monthly = csvFile.groupby('bulan')['Total Pendapatan Produk'].mean().round()

print(avg_monthly)
longLine()

newLine()
longLine()

print("Rata-Rata Pendapatan Rini 2023")
longLine()

avg_yearly = csvFile['Total Pendapatan Produk'].mean()

print(f'Rp. {avg_yearly}')
longLine()

newLine()
longLine()
print("Rekor (Terkecil-Terbesar) Pendapatan Terjual Rini 2023")
longLine()

min_pendapatan = csvFile['Total Pendapatan Produk'].min()
print(f"Pendapatan paling sedikit: Rp. {min_pendapatan}")


max_pendapatan = csvFile['Total Pendapatan Produk'].max()
print(f"Pendapatan paling banyak: Rp. {max_pendapatan}")
longLine()

newLine()
longLine()

print("Produk Terlaris dijual Rini pada 2023")
longLine()

max_sell = csvFile.loc[csvFile['Jumlah Produk Terjual'].idxmax()]
print(f"Nama Produk: {max_sell['Produk']} \nPenjualan Sebanyak: {max_sell['Jumlah Produk Terjual']}")
longLine()