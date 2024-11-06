# # NESTED LOOP
# buah = ["apel", "belimbing", "ceri"]
# angka = [1, 2]

# for i in buah:
#     for j in angka:
#         print(i)
#         print(j)
tinggi = int(input("Masukkan Tinggi = "))
simbol = input("Masukkan Simbol = ")

for i in range(1,tinggi+1):
    Hasil_bintang = i * simbol
    print(Hasil_bintang)
