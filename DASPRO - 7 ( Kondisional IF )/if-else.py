nilai = float(input("Masukkan nilai akhir mahasiswa: "))

if nilai >= 80:
    predikat = "Lulus dengan Sangat Baik"
elif nilai >= 70:
    predikat = "Lulus dengan Baik"
elif nilai >= 60:
    predikat = "Lulus"
else:
    predikat = "Tidak Lulus"

print(f"Nilai: {nilai}, Predikat: {predikat}")