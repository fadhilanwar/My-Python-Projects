############################
# Nim   : 2407136
# Nama  : Fadhil Anwar Ahsani
# Kelas : 1A
############################

''' 
Anda memiliki dictionary berupa data data beberapa siswa
a. Akses nilai siswa tertentu dan menampilkannya

Output: Umur Alice adalah 20 dan prodinya adalah Computer Science
 '''

siswa = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Math"},
    "Charlie": {"age":19, "major": "Physics"},
    }

user_input = input("Masukan Nama Siswa: ")
umur = siswa[str(user_input)]["age"]
prodi = siswa[str(user_input)]["major"]

print(f"{user_input} adalah siswa dari prodi {prodi} dan dia berusia {umur}th") 