n = int(input("Masukkan N = "))
jumlah = 0

for i in range(1, n+1):
    bilangan = int(input(f"Masukkan Bilangan ke {i} = "))
   
    if (bilangan % 2 == 0 or bilangan % 3 == 0 or bilangan % 5 == 0):
        if(bilangan == 2 or bilangan == 3 or bilangan == 5):
            jumlah = jumlah + bilangan
            print(jumlah)
        else:
            continue
    else:
        jumlah = jumlah + bilangan
        print(jumlah)

    

print(f"Jumlah Bilangan Prima = {jumlah}")


