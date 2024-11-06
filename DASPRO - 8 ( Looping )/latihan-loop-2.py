#############################
##
##  Nama : Fadhil Anwar Ahsani
##  Nim  : 2407136
##  Kelas: 1A - RPL
##
#############################

print("Angka yang anda inputkan akan dijumlahkan dan akan stop jika inputan negatif")

penjumlahan = 0
angka = 0
while angka >= 0:
    angka = int(input("Masukkan Angka (Penjumlahan) = "))
    
    if angka < 0:
        break
   
    penjumlahan = penjumlahan + angka
    print(f"Tidak Negatif, maka   {penjumlahan-angka} + {angka}: {penjumlahan}")

print(f"NEGATIF!,\n maka Total akhir: {penjumlahan}")

