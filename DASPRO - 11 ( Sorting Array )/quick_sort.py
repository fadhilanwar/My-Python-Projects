'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''
# Perbandingan Runtime Array yang di Sort dengan Metode yang ditentukan... (Quick Sort)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Menentukan pivot 
    pivot = arr[-1]
    smaller = [x for x in arr[:-1] if x <= pivot]
    bigger = [x for x in arr[:-1] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)

arr = [7, 1, 36, 26, 63, 93, 55, 
       16, 19, 38, 74, 65, 18, 59,
        8, 43, 24, 79, 49, 35, 23,
        78, 51, 2, 46, 28, 60, 76,
        10, 85, 66, 29, 82, 58, 69,
        75, 48, 100, 5, 32, 40, 33
        , 34, 90, 81, 42, 57, 44, 41
        , 77]

array_quick = quick_sort(arr)
print("Array Setelah diurutkan:", array_quick)
