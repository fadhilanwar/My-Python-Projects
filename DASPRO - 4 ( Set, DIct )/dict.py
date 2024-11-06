kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
}

## Mengecek Jumlh item dengan 
print(kucing)
print(len(kucing))

## Membuat dictionary baru dengan method dict()
buah = dict(nama = "Apel",warna = "Merah", manis = True)

print(buah)



## Mengakses item di dictionary dengan nama KEY-nya
print(kucing['nama'])
# Bisa juga dengan GET()
print(kucing.get('nama'))



## MEngambil seluruh KEY dari dictionary
print(kucing.keys())
## Mengambil seluruh VALUES saja
print(kucing.values())



## Menambahkan KEY Baru
kucing["lucu"] = True
print(kucing)

## Mengupdate value dari KEY
kucing["umur"] = 10
print(kucing)

## UPDATE Value dari KEY
kucing.update({"umur": 22})
print(kucing)

## Menambah ITEM pada suatu DICT dengan UPDATE
kucing.update({"warna": ["Merah", "Hitam"]})
print(kucing)

## Menghapus Item pada  suatu DICT
kucing.pop("jantan")
print(kucing)





