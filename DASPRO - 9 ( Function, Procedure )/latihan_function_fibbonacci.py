'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Bilangan Fibbonacci dengan Fungsi

def bilangan_fibonacci(bilangan):
    if bilangan <= 1:
        return bilangan
    else:
        hasil = bilangan_fibonacci(bilangan - 1) + bilangan_fibonacci(bilangan - 2)
        return hasil

n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin dihitung: "))

for i in range(n):
    
    print(bilangan_fibonacci(i))
