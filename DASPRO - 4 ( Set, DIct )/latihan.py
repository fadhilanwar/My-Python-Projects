############################
# Nim   : 2407136
# Nama  : Fadhil Anwar Ahsani
# Kelas : 1A
############################

''' 
Anda memiliki Dictionary yang berisi beberapa siswa dan jurusan mereka.
a. Buat Dictionary baru dan hitung berapa jumlah siswa yang ada di setiap jurusan berdasarkan input
 
 '''

siswa = {
    "Alice": "Computer Science",
    "Bob": "Math",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Math" 
}

jurusan = list(siswa.values())
hitung_cs = jurusan.count("Computer Science")
hitung_m = jurusan.count("Math")
hitung_p = jurusan.count("Physics")

print(f"Prodi Computer Science berjumlah {hitung_cs}, Prodi Math {hitung_m}, Prodi Physics {hitung_p}")
