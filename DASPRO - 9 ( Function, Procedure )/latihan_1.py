'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Menghitung Volume Tabung dengan fungsi

def volume_tabung(r, tinggi):
    hitung_luas_alas = 3.14 * r**2
    volume_tabung = hitung_luas_alas * tinggi
    return volume_tabung

r = int(input("Masukkan Jari-jari(cm) = "))
tinggi = int(input("Masukkan Tinggi Tabung(cm) = "))

volume = volume_tabung(r, tinggi)

print(f"Volume dari Tabung tersebut adalah: {volume} cm")
