
array = ["Ayam Gulai", "Babat", "Cumi", "Ikan Kembung", "Kikil", "Limpa", "Otak", "Paru", "Rendang", "Telur", "Usus"]


search_key = input("Masukan Angka yang ingin dicari(Maaf Case Sensitive Masukan dengan Tepat) = ")

if search_key in array:
    print(f"Makanan {search_key} Ada didalam Menu Restoran Kami!")
else:
    print(f"“Maaf Makanan yang dicari tidak tersedia didalam Menu Restoran Kami!")


