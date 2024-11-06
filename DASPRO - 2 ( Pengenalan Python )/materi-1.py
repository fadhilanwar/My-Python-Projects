# 1. Print Hello World
print("1. Print Hello World")
print("Ini adalah Latihan Python pertama...")
print("Hello, World!!!!")
print("Hello" * 3)

print("")
# 2. Tes Komentar
print("2. Tes Komentar")
print("Tes Komentar") #Line ini akan ditampilkan

"""
Komentar pada line 9
Komentar pada line 10
Komentar pada line 11
"""

print("")
# 3. Variable dalam Python
print("3. Variable dalam Python")
var_1 = 1
var_2 = "satu"
var_3 = 20
var_4 = float(1.75)

print("Variabel Satu = ", var_1) 
print("Variabel Satu + Variabel Tiga = ", var_1 + var_3)  
print("Variabel Satu + Variabel Empat = ", var_1 + var_4)

print("")
# KUIS
print("4. KUISS")   
a = 2
b = 6
print(str(a+b) + "5" * 4)

print("")
# Menyatukan Kalimat dalam sintaks print()
print("5. Menyatukan Kalimat dalam sintaks print()")
user_1 = "Abdul"
user_2 = "Budi"
# Cara ke-1 dengan Koma(,)
print("Orang Pertama adalah si", user_1, "dan Orang Keduanya si", user_2)
# Cara ke-2 dengan (print(f""))
print(f"Orang Pertama adalah si {user_1} dan Orang Keduanya si {user_2}")

print("")
# Untuk memasukan nilai variabel dengan Manual(Dimasukin sendiri nilainya)
print("6. Input Nilai Variable Manual")
who_are_you = input("Siapa Namamu?: ")
print(f"Got It!, Jadi namamu adalah {who_are_you}")
