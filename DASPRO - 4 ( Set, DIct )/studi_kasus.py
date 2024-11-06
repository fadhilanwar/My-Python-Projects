############################
# Nim   : 2407136
# Nama  : Fadhil Anwar Ahsani
# Kelas : 1A
############################

''' Anda Diberikan daftar angka berduplikasi
 TUGASNYA ADALAH 
    a. Menghapus semua DUPLIKASI
    b. Return nilai tanpa duplikasi
 
 '''

numbers = [10, 20, 20, 30, 40, 50, 50, 60]

convert = set(numbers)

numbers_sorted = sorted(convert)

print(f"Awal :{numbers}")
print(f"hilangkan duplikat :{convert}")
print(f"urutkan :{numbers_sorted}")
