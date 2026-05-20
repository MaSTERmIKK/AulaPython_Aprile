import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dati: 30 temperature casuali
np.random.seed(42)
df = pd.DataFrame({
    "temperature": np.random.randint(15, 36, size=30)
})

# Statistiche di base
massima = df["temperature"].max()
minima = df["temperature"].min()
media = df["temperature"].mean()
mediana = df["temperature"].median()

print("Massima:", massima)
print("Minima:", minima)
print("Media:", round(media, 2))
print("Mediana:", mediana)

# Matplotlib: line plot + linea media
plt.figure(figsize=(8, 4))
x = df.index
plt.plot(x, df["temperature"], marker="o", label="Temperatura")
# plt.plot(x, [media] * len(x), "--", color="red", label=f"Media = {media:.2f}")
plt.axhline(media, color="red", linestyle="--", label=f"Media = {media:.2f}")
plt.title("Temperature")
plt.xlabel("Indice")
plt.ylabel("Valore")
plt.legend()
plt.tight_layout()
plt.show()

# Seaborn: histplot con kde
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x="temperature", kde=True, bins=10)
plt.title("Distribuzione Temperature")
plt.xlabel("Temperatura")
plt.ylabel("Frequenza")
plt.tight_layout()
plt.show()
