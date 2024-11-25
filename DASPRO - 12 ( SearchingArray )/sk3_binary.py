'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Perbandingan Runtime Execution untuk Searching Data... (Binary Searching)

import time
start_time = time.time()  # Waktu Eksekusi akan dimulai

## Program
search_key = 60
array = [1,2,5,7, 8, 10, 16, 18, 19, 23,
         24, 26, 28, 29, 32, 33, 34, 35, 
         36, 38, 40, 41, 42, 43, 44, 46, 
         48, 49, 51, 55, 57,58, 59, 60, 
         63, 65, 66, 69, 74, 75, 76, 77, 
         78, 79, 81, 82, 85, 90, 93, 100]

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

search_result = binary_search(search_key, array)

if search_result != -1:
    print(f"Angka {search_key} berada pada Indeks ke-{search_result} dengan Menggunakan Binary Searching")
else:
    print(f"Angka {search_key} Tidak ditemukan!")

# Waktu Eksekusi Selesai
end_time = time.time()  
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time} detik")


