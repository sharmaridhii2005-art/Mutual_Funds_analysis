import os
import pandas as pd

DATA_FOLDER = "data/raw"

files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print("="*60)
print("Total CSV Files:", len(files))
print("="*60)

datasets = {}

for file in files:

    path = os.path.join(DATA_FOLDER, file)

    try:

        df = pd.read_csv(path)

        datasets[file] = df

        print("\n")
        print("="*60)
        print(file)
        print("="*60)

        print("\nShape")
        print(df.shape)

        print("\nColumns")
        print(df.columns.tolist())


        print("\nData Types")
        print(df.dtypes)

        print("\nFirst Five Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

    except Exception as e:
        print(file, e)