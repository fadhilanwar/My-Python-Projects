nilai = float(input("Masukkan nilai akhir mahasiswa: "))

def kelulusan(nilai: float):
    if nilai > 80:
        predikat = "Selamat, Lulus. Dengan Predikat Sangat Baik"
        print(predikat)
    elif nilai >= 60:
        predikat = "Selamat, Lulus"
        print(predikat)
    elif nilai < 60:
        predikat = "MAAF, Tidak Lulus"
        print(predikat)

kelulusan(nilai)