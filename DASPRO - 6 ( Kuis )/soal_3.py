angka_sebelum = int(input("Masukkan Angka = "))
jumlah = 0
while True:

    jumlah = jumlah + angka_sebelum
    angka_setelah = int(input("Masukkan Angka = "))

    if angka_sebelum > angka_setelah:
        for i in range(2, 0, -1):
            print(f"Angka Mengecil! Tidak akan dihitung")
            angka_sebelum = angka_setelah

            angka_setelah = int(input("Masukkan Angka = "))

            if(i == 3):
                continue

            elif(i == 2):
                continue


            elif(i == 1):
                jumlah = jumlah + angka_sebelum
            
        break
            # elif(i == 0):
            #     # print("Selesai")
    jumlah = jumlah + angka_sebelum
    print(f"Jumlah angka yang membesar {jumlah}")
                
            
               
