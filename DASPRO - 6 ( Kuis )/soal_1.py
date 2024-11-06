username = input("Masukan Username = ")
password = input("Masukkan Password = ")

if username == "loginUTS" and password == "rpl2024":
    print("Selamat Datang di Aplikasi Prodi RPL Fire!!")
    
else:
    for i in range(3, -1, -1):

        if username != "loginUTS" and password != "rpl2024":
            print(f"Password Salah! Kamu memiliki {i}x percobaan tersisa")
        if(i == 3):
            username = input("Masukan Username = ")
            password = input("Masukkan Password = ")
            if username == "loginUTS" and password == "rpl2024":
                print("Selamat Datang di Aplikasi Prodi RPL Fire!!")
                break
            
        elif(i == 2):
            username = input("Masukan Username = ")
            password = input("Masukkan Password = ")
            if username == "loginUTS" and password == "rpl2024":
                print("Selamat Datang di Aplikasi Prodi RPL Fire!!")
                break
        elif(i == 1):
            username = input("Masukan Username = ")
            password = input("Masukkan Password = ")
            if username == "loginUTS" and password == "rpl2024":
                print("Selamat Datang di Aplikasi Prodi RPL Fire!!")
                break
        elif(i == 0):
            print("Anda tidak diperkenankan mengakses Aplikasi RPL")
        
