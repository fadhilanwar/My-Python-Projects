'''
Nama    : Fadhil Anwar Ahsani
Kelas   : 1A - RPL
Nim     :2407136
'''

# Sistem Login dengan hanya mengecek Password, Kesempatan salah input 3x
def login_success(username):
    welcome = "Selamat Datang " + str(username) + " pada Aplikasi ini! \nEnjoyy the App..."
    return welcome

print("Selamat Datang di Sistem Login :)")
username = input("Username: ")
password = input("Password: ")
passkey = "Latihan"

if password == passkey:
    print("<=== Login Success ! ===>")
    print(login_success(username))
    print("<=======================>")
else:
    false_count = 0
    for i in range(3, 1, -1):
        print(f"Password Salah! Kesempatan tersisa: {i-1}")
        username = input("Username: ")
        password = input("Password: ")
        if password == passkey:
            print("<=== Login Success ! ===>")
            print(login_success(username))
            print("<=======================>")
            break
        elif password != passkey:
            false_count = false_count + 1
            # print(false_count)
            if false_count == 2:
                print("Anda sudah salah sebanyak 3x, dan tidak diperkenankan Login sampai batas waktu yang tidak ditentukan.")
                break
            



