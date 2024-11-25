'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

'''
1. Linear Seaching
- Metode yang sequential atau Berurutan
- Kompleksitas
best case = Elemen yang dicari ada pada Indeks paling awal
worst case = ELemen yang dicari ada pada Indeks paling akhir
average = O(n)
- Prinsip: Membandingkan elemen yang akan kita cari secara berurutan ketika Kesamaan terjadi maka Ditemukan!
- Kerja: Mencari elemen 8 dari angka 1-10 maka akan dikerjakan dari 1,2,n,8 jika sudah 8 maka True
'''

search_key = 20
array_list = [10, 15, 30, 70, 80, 69, 20, 90]

def linear_searching(search_key, array_list):
    for i in range(len(array_list)):
        if array_list[i] == search_key:
            return i
    return -1

search_result = linear_searching(search_key, array_list)

if search_result != -1:
    print(f"Elemen {search_key} ditemukan pada Indeks {search_result}")
else:
    print("Elemen tidak ditemukan")