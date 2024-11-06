'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
NIM : 2407136
'''

nilai = float(input("Masukkan nilai akhir: "))

if nilai >= 90:
    predikat = "Your Grade: A"
elif nilai < 90 and nilai >= 80:
    predikat = "Your Grade: B"
elif nilai < 80 and nilai >= 70:
    predikat = "Your Grade: C"
else:
    predikat = "Your Grade: D"

print(f"Nilai: {nilai}, {predikat}")