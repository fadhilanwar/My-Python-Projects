'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
NIM : 2407136
'''

bilangan = float(input("Masukkan Bilangan: "))

if(bilangan > 0):
    if (bilangan % 2 == 0):
        print(f"Bilangan {bilangan} Positif, Genap")
    elif (bilangan % 2 == 1):
        print(f"Bilangan {bilangan} Positif, Ganjil")
elif(bilangan < 0):
    if (bilangan % 2 == 0):
        print(f"Bilangan {bilangan} Negatif, Genap")
    elif (bilangan % 2 == 1):
        print(f"Bilangan {bilangan} Negatif, Ganjil")
elif(bilangan == 0):
    print(f"Bilangan {bilangan} Nol, Genap")
