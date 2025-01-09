import pandas as pd

# Membaca File .csv


csvFile = pd.read_csv("files/insurance.csv")
print(csvFile.head())
