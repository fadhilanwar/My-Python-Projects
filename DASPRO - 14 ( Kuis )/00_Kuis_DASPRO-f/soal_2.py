
jumlah_array = int(input("Masukkan Jumlah Elemen Array = "))
array = []

for i in range(jumlah_array):
    add_array = input(f"Masukkan Array ke-{i}: ")
    array.append(add_array)
    print(array)

search_key = input("Masukan Angka yang ingin dicari = ")

if search_key in array:
    print(f"Angka {search_key} ada didalam Array!")
else:
    print(f"“Maaf nilai yang dicari tidak ada di array")


