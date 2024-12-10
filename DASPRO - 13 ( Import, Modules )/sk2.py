'''
Nama    : Fadhil Anwar Ahsani
Kelas   : 1A - RPL
NIM     : 2407136
'''

def update_stok(nama_inventaris, total_stok, aksi):
    barang_inventaris = []

    with open('inventaris_barang.csv', 'r') as file:
        for line in file:
            baris = line.strip().split(',')
            barang_inventaris.append(baris)

    print("Data inventaris sebelum update:", barang_inventaris)

    barang_ditemukan = False

    for barang in barang_inventaris:
        if barang[0].strip().lower() == nama_inventaris.strip().lower():
            barang_ditemukan = True
            stok_sekarang = int(barang[1])
            if aksi == 'impor':
                barang[1] = str(stok_sekarang + total_stok)  # Impor: tambah stok
            elif aksi == 'ekspor':
                if stok_sekarang >= total_stok:
                    barang[1] = str(stok_sekarang - total_stok)  # Ekspor: kurangi stok
                else:
                    print(f"Stok barang '{nama_inventaris}' tidak cukup untuk diekspor.")
                    return
            break

    if not barang_ditemukan:
        print(f"Barang '{nama_inventaris}' tidak ditemukan. Ini akan  ke inventaris.")
        barang_inventaris.append([nama_inventaris, str(total_stok)])

    with open('inventaris_barang.csv', 'w') as file:
        for barang in barang_inventaris:
            file.write(f"{barang[0]},{barang[1]}\n")

    print("Data inventaris setelah update:", barang_inventaris)

update_stok('Kursi Chitose', 50, 'impor')  # Menambahkan stok
update_stok('Meja Jati', 50, 'impor')  
update_stok('Monitor LED', 50, 'impor') # Mengurangi stok      
update_stok('Kabel Listrik', 50, 'impor')
