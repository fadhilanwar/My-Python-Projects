'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''
# Perbandingan Runtime Array yang di Sort dengan Metode yang ditentukan... (Bubble Sort)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

data = [7, 1, 36, 26, 63, 93, 55, 
        16, 19, 38, 74, 65, 18, 59, 8, 
        43, 24, 79, 49, 35, 23, 78, 51, 
        2, 46, 28, 60, 76, 10, 85, 66, 
        29, 82, 58, 69, 75, 48, 100, 5, 
        32, 40, 33, 34, 90, 81, 42, 57, 
        44, 41, 77]

array_bubble = bubble_sort(data)
print("Array setelah diurutkan:", array_bubble)
