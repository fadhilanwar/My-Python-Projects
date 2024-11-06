############################
# Nim   : 2407136
# Nama  : Fadhil Anwar Ahsani
# Kelas : 1A
############################

## Latihan Studi Kasus pada Tipe Data Tuple ##

# 3. Manipulasi tuple buah agar ada tambahan item “manggis” diantara item “jeruk” dan “ceri”

buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

buah_muttable = list(buah)

buah_muttable.insert(2, "manggis")

print(buah_muttable)