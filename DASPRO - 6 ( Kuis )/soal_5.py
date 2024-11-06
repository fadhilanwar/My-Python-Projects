nim = int(input("Masukkan 3 digit terakhir NIM = "))

if 0 < nim <= 50:
    if nim % 2 == 0:
        print("Silakan Masuk ke Kelas K2")
    if nim % 2 == 1:
        print("Silakan Masuk ke Kelas K1")
elif 51 <= nim <= 100:
    if nim % 2 == 0:
        print("Silakan Masuk ke Kelas K4")
    if nim % 2 == 1:
        print("Silakan Masuk ke Kelas K3")
elif 101 <= nim <= 150:
    if nim % 2 == 0:
        print("Silakan Masuk ke Kelas K6")
    if nim % 2 == 1:
        print("Silakan Masuk ke Kelas K5")
elif nim > 150:
    if nim % 2 == 0:
        print("Silakan Masuk ke Kelas K8")
    if nim % 2 == 1:
        print("Silakan Masuk ke Kelas K7")


