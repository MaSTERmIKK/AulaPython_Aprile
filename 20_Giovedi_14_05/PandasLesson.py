import pandas as pd
import numpy as np

#Introduzione ai DataFrame
print("\nIntroduzione ai DataFrame")
data = {
    "Nome":     ["Alice", "Bob", "Carla", "Giulio"],
    "Eta":      [25, 30, 22, 16],
    "Citta":    ["Roma", "Milano", "Napoli", "Torino"]
}
df = pd.DataFrame(data)

print("DataFrame Originale: ")
print(df)

df_older = df[df['Eta'] > 23]
print("\nPersone con eta > di 23")
print(df_older)

df["Maggiorenne"] = df["Eta"] >= 18
print("\nNuova Colonna Maggiorenne: ")
print(df)

#Pulizia dei dati
print("\n-------------------------------\nPulizia dei dati con Pandas")
data2 = {
    'Nome':     ["Alice", "Bob", "Carla", "Bob", "Carla", "Alice", None],
    'Eta':      [25, 30, 22, 30, np.nan, 25, 29],
    'Citta':    ["Roma", "Milano", "Napoli", "Milano", "Napoli", "Roma", "Roma"]
}
df2 = pd.DataFrame(data2)
print("\nDataFrame Originale: ")
print(df2)

#Rimozione duplicati
df2.drop_duplicates(inplace=True)

print("\nDuplicati rimossi")
print(df2)

print("\nPulizia dati mancanti")
df_cleaned = df2.dropna()
print(df_cleaned)

print("\nSostituzione dati mancanti")
df2.fillna({'Eta': df2['Eta'].mean()}, inplace=True)
print(df2.dropna())

#
print(df2.info())
print(df2.describe())