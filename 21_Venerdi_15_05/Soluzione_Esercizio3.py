import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dati: 365 giorni con trend crescente
np.random.seed(42)
date = pd.date_range(start="2025-01-01", periods=365, freq="D")
trend = np.linspace(100, 220, 365)
rumore = np.random.normal(0, 10, 365)
visitatori = trend + rumore

df = pd.DataFrame({"visitatori": visitatori}, index=date)

# Media e deviazione standard mensile (ME = month-end, compatibile con pandas recenti)
stat_mensili = df.resample("ME")["visitatori"].agg(["mean", "std"])
print("Statistiche mensili:")
print(stat_mensili)

# Matplotlib: serie giornaliera + media mobile 7 giorni
df["media_mobile_7"] = df["visitatori"].rolling(7).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["visitatori"], alpha=0.5, label="Giornaliero")
plt.plot(df.index, df["media_mobile_7"], color="red", linewidth=2, label="Media mobile 7g")
plt.title("Visitatori giornalieri e media mobile")
plt.xlabel("Data")
plt.ylabel("Visitatori")
plt.legend()
plt.tight_layout()
plt.show()

# Seaborn: lineplot della media mensile
plt.figure(figsize=(10, 4))
sns.lineplot(x=stat_mensili.index, y=stat_mensili["mean"], marker="o")
plt.title("Media mensile visitatori")
plt.xlabel("Mese")
plt.ylabel("Visitatori medi")
plt.tight_layout()
plt.show()
