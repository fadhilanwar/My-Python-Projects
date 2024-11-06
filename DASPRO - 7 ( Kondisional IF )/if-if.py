# Input kategori hewan
kategori = input("Masukkan kategori hewan (Mamalia/Reptil/Burung): ").lower()

# .lower() untuk Lowercase

if kategori == "mamalia":

    jenis = input("Masukkan jenis mamalia (Herbivora/Karnivora): ").lower()
    if jenis == "herbivora":
        print("Hewan ini adalah mamalia herbivora.")
    elif jenis == "karnivora":
        print("Hewan ini adalah mamalia karnivora.")
    else:
        print("Jenis mamalia tidak valid.")
        
elif kategori == "reptil":

    jenis = input("Masukkan jenis reptil (Bersisik/Berbisa): ").lower()
    if jenis == "bersisik":
        print("Hewan ini adalah reptil bersisik.")
    elif jenis == "berbisa":
        print("Hewan ini adalah reptil berbisa.")
    else:
        print("Jenis reptil tidak valid.")
        
elif kategori == "burung":
    print("Hewan ini adalah burung.")
else:
    print("Kategori hewan tidak valid.")
