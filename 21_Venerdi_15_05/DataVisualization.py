import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.facecolor'] = 'green'

# #Line
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.figure()

# plt.plot(x, y)

# plt.title("Grafico a linee")
# plt.xlabel("X")
# plt.ylabel("Y")

# #BAR
# plt.figure()

categorie = ['A', 'B', 'C', 'D', 'E']
valori = [3, 7, 2, 5, 8]

# plt.bar(categorie, valori)
# plt.title("Grafico a barre")
# plt.xlabel("Categorie")
# plt.ylabel("Valori")

# #HIST
plt.figure()

data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title("Istogramma")
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.legend(["Valori", "Frequenza"])

#Scatter plot
# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.figure()

# plt.scatter(x, y)
# plt.title("ScatterPlot")
# plt.xlabel("X")
# plt.ylabel("Y")
# # plt.legend(["uno", "due"])

plt.show()

#Subplot

# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# axes[0,0].plot([1,2,3,4], [1,4,6,9])
# axes[0,0].set_title('grafico 1: Line')

# axes[0, 1].scatter([1, 2,3,4], [2,3,1,4])
# axes[0, 1].set_title('Grafico 2: Scatter')

# axes[1,1].bar(categorie, valori)
# axes[1,1].set_title('Grafico 3: bar')

# plt.show()

#Seaborn

# sns.set_theme(style='darkgrid')

# plt.figure()

# tips = sns.load_dataset("tips")
# print(tips.head())

# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title('Conto totale del giorno')

# plt.figure()

# fmri = sns.load_dataset("fmri")
# print(fmri.head())

# sns.lineplot(x="timepoint", y="signal", data=fmri)
# plt.title("Segnale FMRI nel tempo")

# plt.show()