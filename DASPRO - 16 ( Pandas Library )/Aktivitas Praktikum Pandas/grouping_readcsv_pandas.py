import pandas as pd

csvFile = pd.read_csv("files/insurance.csv")

groupingFile = csvFile.groupby('sex').agg(average_age=('age', 'mean'),
                                          median_charges=('charges', 'median'))

print(f"Hasil Grouping: \n {groupingFile.head()}")
