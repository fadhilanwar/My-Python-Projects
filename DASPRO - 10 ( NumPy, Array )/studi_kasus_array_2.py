'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Sorting 30 Nilai Mahasiswa dan Tampilkan Top 5 Rank Nilai Mahasiswa kelas 1A Prodi RPL

import numpy as np

nilai_mhs_1A = np.array([
    85, 78, 92, 60, 74, 88, 91, 55, 67, 80,
    72, 94, 79, 65, 83, 75, 82, 69, 77, 90,
    68, 86, 92, 64, 80, 70, 89, 73, 95, 81
])

urutan = sorted(nilai_mhs_1A, reverse=True)

print("Leaderboard Nilai Mahasiswa 1A")
no = 1
while True:
    
    for x in urutan:
        if(no == 6):
            break    
        print(f"{no}. dengan Nilai {x}")
        no += 1