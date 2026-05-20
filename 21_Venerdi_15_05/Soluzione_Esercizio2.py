import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dati di esempio
df = pd.DataFrame({
    "altezza": [160, 165, 170, 175, 180, 172, 168],
    "peso": [55, 60, 68, 72, 80, 70, 65],
    "eta": [22, 25, 30, 28, 35, 27, 24]
})

# Normalizzazione min-max su altezza e peso
df_norm = df.copy()
for colonna in ["altezza", "peso"]:
    minimo = df[colonna].min()
    massimo = df[colonna].max()
    df_norm[colonna] = (df[colonna] - minimo) / (massimo - minimo)

print("Dati originali:")
print(df)
print("\nDati normalizzati:")
print(df_norm)

# Matplotlib: confronto a barre (medie originali vs normalizzate)
labels = ["altezza", "peso"]
medie_originali = [df["altezza"].mean(), df["peso"].mean()]
medie_normalizzate = [df_norm["altezza"].mean(), df_norm["peso"].mean()]

x = range(len(labels))
larghezza = 0.35

plt.figure(figsize=(8, 4))
plt.bar(x, medie_originali, width=larghezza, label="Originali")
plt.bar(x, medie_normalizzate, width=larghezza, label="Normalizzati")
plt.xticks(list(x), labels)
plt.title("Confronto valori medi")
plt.ylabel("Valore")
plt.legend()
plt.tight_layout()
plt.show()

# Seaborn: scatterplot tra altezza e peso normalizzati
plt.figure(figsize=(6, 5))
sns.scatterplot(data=df_norm, x="altezza", y="peso")
plt.title("Altezza vs Peso (normalizzati)")
plt.tight_layout()
plt.show()
