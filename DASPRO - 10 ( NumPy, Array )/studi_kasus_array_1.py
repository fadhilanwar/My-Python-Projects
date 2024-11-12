'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
Nim : 2407136
'''

# Konversi Suhu Celcous dengan sumber 10 hari terakhir menjadi Fahrenheit

import numpy as np

data_suhu = np.array([
    25, 22, 27, 35, 12, 15, 41, 29, 10, 40
    ])

tanggal = 1
for x in data_suhu:
    toFahrenheit = (x * 9/5) + 32
    print(f"Suhu Asia Tanggal {tanggal} Feb adalah {x} C, atau {toFahrenheit} F") 
    tanggal += 1
