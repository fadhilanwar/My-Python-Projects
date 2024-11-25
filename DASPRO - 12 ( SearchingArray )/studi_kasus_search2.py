'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Mengidentifikasi Nama Mahasiswa yang dicari Terdapat pada List Nama Mahasiswa UPI

list_mahasiswa = [
    "Ahmad Fauzi",
    "Budi Santoso",
    "Citra Dewi",
    "Dian Permata",
    "Eka Saputra",
    "Fajar Hidayat",
    "Gita Anggraeni",
    "Hendra Wijaya",
    "Ika Lestari",
    "Joko Prasetyo",
    "Karin Amalia",
    "Lina Marlina",
    "Mira Kusuma",
    "Nanda Rahma",
    "Oka Suryana",
    "Putu Andika",
    "Qori Amrina",
    "Rama Wijaya",
    "Siti Nurhaliza",
    "Taufik Hidayat",
]

search_key = input("Cari Nama Mahasiswa: ")

# Saya akan menggunakan Binary Searching pada Studi Kasus ini
def binary_search(search_key, arr):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == search_key:
            return mid
        elif search_key > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

search_result = binary_search(search_key, list_mahasiswa)

if search_result != -1:
    print(f"Nama \'{search_key}\' ada didalam Daftar Mahasiswa UPI..")
else:
    print(f"Nama \'{search_key}\' Tidak ditemukan dalam Daftar Mahasiswa UPI..")

