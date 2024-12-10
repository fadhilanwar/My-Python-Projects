kuota = int(input("Masukkan Antrian Kuota Klinik = "))

antrian = []

kondisi = "tersedia"
while kondisi == "tersedia":
    antrian.append(kuota)
    kuota = kuota - 1
    
    if kuota == 0:
        kondisi == "penuh"
        break
