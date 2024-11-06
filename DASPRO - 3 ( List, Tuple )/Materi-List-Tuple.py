#1. Tipe Data: LIST

'''
Kita bisa memanipulasi List tersebut seperti:
a. Melihat Jumlah
b. Meng-Select suatu Item
c. Meng-Select suatu Item dengan Range
d. Menambah Item diakhir List
e. Mengganti Item pada Index tertentu
f. Meng-Insert Item pada Index tertentu
g. Meng-Hapus Item pada Index tertentu
h. Tipe Data yang Berbeda dalam sebuah List
i. Meng-Insert Item dari List lain
j. Meng-Urutkan List Item sesuai Abjad (a-z)
'''

# a. Melihat Jumlah
print("a. Jumlah List")

a = ["apel", "jeruk", "ceri", "durian", "apel", "apel"]

print(len(a))


print("")
# b. Meng-Select suatu Item
print("b. Select satu dari List")

b = ["apel", "jeruk", "ceri", "durian", "apel"]

print(b[2])



print("")
# c. Meng-Select suatu Item dengan Range
print("c. Select dengan Range")

c = ["apel", "jeruk", "ceri", "durian", "apel"]

print(c[1:4])


print("")
# d. Menambah Item diakhir List
print("d. Menambah Item diakhir List")
d = ["apel", "jeruk", "ceri", "durian", "apel"]
d.append("SIRSAK")

print(d)
    


print("")
# e. Mengganti Item dalam sebuah List #
print("Update item di List")
e = ["apel", "jeruk", "ceri", "durian", "apel"]
e[2] = "MANGGIS"

print(e)


print("")
# f. Meng-Insert Item pada Index tertentu
print("f. Insert Item ke List")
f = ["apel", "jeruk", "ceri", "durian", "apel"]
f.insert(1, "SEMANGKA")

print(f)


print("")
# g. Meng-Hapus Item pada Index tertentu
print("g. Hapus Item di Index tertentu")
g = ["apel", "jeruk", "ceri", "durian", "apel"]
g.pop(3)

print(g)

print("")
# h. Tipe Data yang Berbeda dalam sebuah List
print("h. Tipe Data Berbeda dari List")
h = ["apel", 15, "ceri", "durian", 20.2, True]

print(h)

print("")
# i. Meng-Insert Item dari List lain
print("i. Insert Item dari List lain")

list_utama = ["apel", "jeruk", "ceri", "durian", "apel"]
list_lain = ["Strawberry", "Blueberry"]

list_utama.extend(list_lain)

print(list_utama)



print("")
# j. Meng-Urutkan List Item sesuai Abjad (a-z)
print("j. Sorting List sesuai A-Z")
j = ["apel", "jeruk", "ceri", "durian", "zamrud"]
j.sort()

print(j)


# 2. Tipe Data Tuple

buah = ("anggur", "blueberry", "ceri", "durian")

(a, b, c, d) = buah

print(a)
print(b)
print(c)
print(d)

