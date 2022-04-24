import pandas as pd

df = pd.read_csv("generatedCSVs/GeneratedData.csv")
print(df.head())
df.drop("Unnamed: 0", axis=1, inplace=True)
print(df.head())
df.set_index("timestamp", inplace=True)
print(df.head())
