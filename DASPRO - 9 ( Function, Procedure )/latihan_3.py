'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Menghitung Rata-Rata dengan Fungsi

def avg(n, banyak_digit):
    hitung_avg = (n/banyak_digit)
    return hitung_avg

jumlah = 0
banyak_digit = 0

while True:
    
    n = int(input("Masukkan Angka = "))
    jumlah = jumlah + n
    banyak_digit = banyak_digit + 1
    hasil = avg(jumlah, banyak_digit)
    
    print(f"Rata-Rata dari Nilai tersebut adalah = {hasil}")

