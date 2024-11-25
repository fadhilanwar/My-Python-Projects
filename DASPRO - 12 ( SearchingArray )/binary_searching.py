'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

'''
2. Binary Searching
- Algoritma searching harus mengurutkan array terlebih dahulu
- Kompleksitas relatif cepat untuk mencari data yaang besar sekalipun
best case = Elemen yang dicari ada di Tengah List
worst case = Elemen tidak ditemukan maka array akan terus dibagi dua
average = O(log n)
- Kerja: Membagi Array dengan / 2 dan mencari nilai tengah dan mendapatkan daerah mana yang akan diambil
         Mencari lebih besar atau lebih kecil si nilai tengah dengan search_key yang ditentukan
         Jika lebih kecil maka kita akan mengabil Area sebelah kiri dari si nilai tengah <>
         Jika sudah menemukan kesamaan dari nilai_tengah dan search_key maka itu adalah Hasil Pencarianya
'''

arr = [2, 5, 23, 12, 16, 19, 28, 56, 72, 91]
search_key = 23

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

search_result = binary_search(search_key, arr)

if search_result != -1:
    print(f"Angka {search_key} berada pada Indeks ke-{search_result}")
else:
    print(f"Angka {search_key} Tidak ditemukan!")