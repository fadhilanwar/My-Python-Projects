# angka = int(input("Masukkan Angka(Ganjil/Genap) = "))
hasil_penjumlahan_genap = 0
hasil_penjumlahan_ganjil = 0

while True:
    angka = int(input("Masukkan Angka(Ganjil/Genap) = "))
    if(angka < 0):
        print(f"Hasil Penjumlahan Genap = {hasil_penjumlahan_genap} \nHasil Penjumlahan Ganjil = {hasil_penjumlahan_ganjil}")
        break

        

    if(angka %2 == 0):
        angka_genap = angka
        hasil_penjumlahan_genap = hasil_penjumlahan_genap + angka_genap
        # print("Bilangan itu Genap")
        print(hasil_penjumlahan_genap)
    elif(angka %2 == 1):
        angka_ganjil = angka
        hasil_penjumlahan_ganjil = hasil_penjumlahan_ganjil + angka_ganjil
        print(hasil_penjumlahan_ganjil)

  