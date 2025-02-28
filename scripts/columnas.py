"""
Script Utilizado para obtener nombre columna y el tipo de dato
"""

import pandas as pd
path = "data/train_set.csv"
data = pd.read_csv(path)

count = 1
for column in data.columns:
    print(f"{count}. {column} - {data[column].dtype}")
    count += 1
