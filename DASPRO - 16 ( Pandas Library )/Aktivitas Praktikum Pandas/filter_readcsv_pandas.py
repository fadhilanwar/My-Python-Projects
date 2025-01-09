import pandas as pd

# Filter Data atau menunjukan data yang hanya ingin ditampilkan

csvFile = pd.read_csv("files/insurance.csv")
dfFilter = csvFile.filter(items=['sex', 'region'])

print(
    f"Hasil Filter (Hanya Menampilkan Kolom Sex dan Region): \n {dfFilter.head()}")
