#############################
##
##  Nama : Fadhil Anwar Ahsani
##  Nim  : 2407136
##  Kelas: 1A - RPL
##
#############################

# SETIAP KELIPATAN 5 AKAN BERTULISKAN PASS

input = int(input("Masukkan Angka = "))
input_plus_1 = input + 1
angka = range(input_plus_1)

for i in angka:
    if i % 5 == 0:
        if i == 0:
            continue
        print("pass")
        continue

    print(i)
