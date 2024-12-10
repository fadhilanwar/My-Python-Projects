def peringkat_siswa(siswa):
    siswa_terurut = sorted(siswa, reverse=True)
    
    for i in range(len(siswa_terurut)):
        siswa_terurut[i].append(i + 1)  
    
    return siswa_terurut

def program():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    
    siswa = []
    
    for _ in range(jumlah_siswa):
        nama = input("Masukkan nama siswa: ")
        nilai = float(input(f"Masukkan nilai akhir {nama}: "))
        siswa.append([nama, nilai])
    
    siswa_terurut = peringkat_siswa(siswa)
    
    for siswa_info in siswa_terurut:
        nama, nilai, rangking = siswa_info
        if rangking <= 3:
            print(f"Nama: {nama}, Nilai: {nilai}, Rangking: {rangking}")
        else:
            print(f"Nama: {nama}, Nilai: {nilai}, Siswa harus belajar lebih giat.")
    
    cari_nama = input("\nMasukkan nama siswa yang ingin dicari: ")
    ditemukan = False
    
    for siswa_info in siswa_terurut:
        nama, nilai, rangking = siswa_info
        if nama.lower() == cari_nama.lower():
            ditemukan = True
            if rangking <= 3:
                print(f"Nama: {nama}, Rangking: {rangking}")
            else:
                print(f"Nama: {nama}, Siswa harus belajar lebih giat.")
            break
    
    if not ditemukan:
        print("Siswa tidak ditemukan.")

program()
