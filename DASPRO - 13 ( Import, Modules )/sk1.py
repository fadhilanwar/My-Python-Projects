'''
Nama    : Fadhil Anwar Ahsani
Kelas   : 1A - RPL
NIM     : 2407136
'''

# Studi Kasus 1

# Fungsi untuk menghitung nilai rata-rata dari file
def average_grade(file_name):
    
    with open(file_name, 'r') as file:
        total_nilai = 0
        jumlah_siswa = 0

        for i in file:
            data = i.strip().split(": ")
            nama_mhs = data[0]
            nilai = float(data[1])
            
            total_nilai += nilai
            jumlah_siswa += 1
        
        file.close()

        if jumlah_siswa > 0:
            rata_rata = total_nilai / jumlah_siswa
            print(f"Nilai rata-rata ujian Mahasiswa: {rata_rata}")
        else:
            print("Tidak ada data siswa.")

nilai_mhs = [
    "Ali: 85", "Budi: 90", "Citra: 75", "Dewi: 88", "Eka: 92", 
    "Fahri: 78", "Gina: 80", "Hadi: 95", "Ika: 70", "Joko: 82", 
    "Kiki: 91", "Lani: 76", "Mira: 89", "Nina: 85", "Omar: 80", 
    "Putri: 93", "Rudi: 84", "Siti: 88", "Toni: 77", "Udin: 79"
]

file = open("nilai_mhs.txt", 'w')

for data in nilai_mhs:
    file.write(data + "\n")
file.close()

average_grade("nilai_mhs.txt")
