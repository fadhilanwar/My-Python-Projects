def program():
    jumlah_array = int(input("Masukkan jumlah elemen array: "))
    
    arr = []
    for i in range(jumlah_array):
        add_array = int(input(f"Masukkan elemen ke-{i}: "))
        arr.append(add_array)
    
    print("Array sebelum disortir:", arr)
        
    print("Array(ascending)):", sorted(arr))

program()
