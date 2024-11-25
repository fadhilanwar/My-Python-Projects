'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Mengidentifikasi Ketersediaan Barang berdasarkan Input dari User

list_barang = [
    "Beras",
    "Minyak Goreng",
    "Gula Pasir",
    "Telur",
    "Mie Instan",
    "Tepung Terigu",
    "Kopi Sachet",
    "Teh Celup",
    "Sabun Cuci Piring",
    "Shampoo Sachet",
    "Sabun Mandi Batang",
    "Roti Tawar",
    "Susu Sachet",
    "Cokelat Batang",
    "Kecap Manis",
]
search_key = input("Masukkan Kueri untuk Mencari Barang: ")

# Saya akan menggunakan Linear Searching pada Studi Kasus ini
def linear_searching(search_key, list_barang):
    for i in range(len(list_barang)):
        if list_barang[i] == search_key:
            return i
    return -1

search_result = linear_searching(search_key, list_barang)

if search_result != -1:
    print(f"Barang \'{search_key}\' ditemukan di Urutan data ke-{search_result}")
else:
    print("Barang tidak tersedia!")

