angka = int(input("Masukkan Angka = "))

for i in range(angka, 0, -1):


    pulang = i - 1
    if pulang == 0:
        print(f"{i} Bebek kecil berenang \nMenyusuri Sungai yang deras \nInduknya mencari kwek kwek kwek \nDan semua bebek kecil Pulang.. HAHAHHA")
        break
    print(f"{i} Bebek kecil berenang \nMenyusuri Sungai yang deras \nInduknya mencari kwek kwek kwek \nHanya {pulang} yang pulang")
    print("\n")