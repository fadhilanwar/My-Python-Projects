# Perulangan FOR

# FOR dengan RANGE
for i in range(5):
    print(i)
print("\n")

# FOR dengan RANGE_SELISIH
for i in range(10, 0, -1):
    print(i)
print("\n")

# FOR dengan String
for i in "Python Itu Sehat":
    print(i)
print("\n")

# FOR dengan LIST
buah = ["Apel", "Belimbing", "Ceri", "Durian"]
for i in buah:
    print(f"Buah Ini bernama: {i}")
print("\n")

# FOR dengan LIST-Range
for i in range(len(buah)):
    print(f"Buah Ini bernama: {buah[i]}")
print("\n")

# FOR dengan BREAK
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
        break
print("\n")

# FOR dengan CONTINUE *Berhenti ketika if == 3 dan melanjutkan kembali program
angka = [1, 2, 3, 4, 5]
for i in angka:
    if i == 3:
        continue
    print(i)


