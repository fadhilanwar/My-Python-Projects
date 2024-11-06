############################
# Nim   : 2407136
# Nama  : Fadhil Anwar Ahsani
# Kelas : 1A
############################

## Latihan Studi Kasus pada Tipe Data Tuple ##

# 2. Manipulasi tuple buah agar item “durian” dapat dihapus

buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

buah_muttable = list(buah)

buah_muttable.pop(3)

print(buah_muttable)