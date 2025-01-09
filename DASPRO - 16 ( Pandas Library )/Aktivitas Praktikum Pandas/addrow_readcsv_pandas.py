import pandas as pd

# Menambahkan Kolom daroi file .csv yang diread

csvFile = pd.read_csv("files/insurance.csv")
addColumn = csvFile['discount_charges'] = csvFile['charges']*0.05

print(f"Hasil Diskon \n {csvFile.head()}")
