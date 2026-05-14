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

#MULTINDEX e LOC
data_multi = {
  'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
  'Anno': [2023, 2024, 2023, 2024],
  'Vendite': [120, 135, 110, 118]
}

df_multi = pd.DataFrame(data_multi)

df_multi = df_multi.set_index(['Paese', 'Anno'])
print("\nDataFrame con MultiIndex")
print(df_multi)

print("\nTutte le righe per l'itailia")
print(df_multi.loc['Italia'])

print("\nValore vendite Francia 2024")
print(df_multi.loc[('Francia', 2024), 'Vendite'])

#PIVOT TABLE

data_vendite = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df_vendite = pd.DataFrame(data_vendite)

pivot_df = df_vendite.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print("\nPivot media vendite prodotto per citta")
print(pivot_df)

#Group by
print("\nGroup by somma prodotto")
grouped_df = df_vendite.groupby('Prodotto').sum()
print(grouped_df)

#Salvataggio CSV
df_vendite.to_csv(".\\df_vendite.csv")

print(pd.read_csv("df_vendite.csv").head())

print(df_vendite.describe())

#Sorted
df_sorted = df_vendite.sort_values(by="Città")
print("\nOrdinato per vendite")
print(df_sorted)

#Merge
merge_df = pd.merge(df_vendite, pd.read_csv("vendite_sample.csv"), on="Città")
print("\nMerged DataFrame")
print(merge_df)

#Apply
def categoria_eta(eta):
    if(eta < 18):
        return "Giovane"
    elif(eta < 50):
        return "Adulto"
    else:
        return "Anziano"

df["Categoria Eta"] = df["Eta"].apply(categoria_eta)
print(f"\nCategoria eta nuova colonna ")
print(df)

df_vendite["Vendite_IVA"] = df_vendite["Vendite"].apply(lambda x: x + x * 22 / 100)
print("\nVendite + Iva")
print(df_vendite)

#Esempio complessivo pivot e risistemazione
data_vendite2 = {
    'Prodotto': ['Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor'],
    'Quantità': [5, 10, 2, 7, 3],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano'],
    'Data': ['2021-09-01', '2021-09-01', '2021-09-02', '2021-09-02', '2021-09-03']
}

df_vendite2 = pd.DataFrame(data_vendite2)

data_costi = {
    'Prodotto': ['Tastiera', 'Mouse', 'Monitor'],
    'Costo per unità': [50, 25, 150]
}
costi_df = pd.DataFrame(data_costi)

df_merge_vendite = pd.merge(df_vendite2, costi_df, on='Prodotto')
print("\n Mergee Vendite e Costi")
print(df_merge_vendite)

pivot_vendite = df_merge_vendite.pivot_table(index="Prodotto", columns='Città', values="Quantità", aggfunc='sum')
print("\nPivot table")
print(pivot_vendite) 

pivot_vendite.to_csv(".\\pivot_vendite.csv")
