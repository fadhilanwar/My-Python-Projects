import pandas as pd

# Mengurutkan data dari file .csv yang diread

csvFile = pd.read_csv("files/insurance.csv")

dfSort = csvFile.sort_values(by=['sex'])
dfDesc = csvFile.sort_values(by=['sex'], ascending=False)

print(f"Sorting CSV (Ascending): \n {dfSort.head()}")
print(f"Sorting CSV (Descending): \n {dfDesc.head()}")
