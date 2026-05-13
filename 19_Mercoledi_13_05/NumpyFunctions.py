import numpy as np

array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])

print("\nSomma: ", np.add(array_a, array_b))
print("Sottrazione: ", np.subtract(array_a, array_b))
print("Mult: ", np.multiply(array_a, array_b))
print("Div: ", np.divide(array_a, array_b))

angoli = np.array([0, np.pi/2, np.pi])

print("\nSeno: ", np.sin(angoli))
print("Coseno: ", np.cos(angoli))

valori = np.array([0, 1, 2])
print("\nesp: ", np.exp(valori)) #e = 2.718
print("log: ", np.log(valori)) # base e

dati = np.array([-10, 4, 6, 8 ,100])

print("\nMedia ", np.mean(dati))
print("Mediana ", np.median(dati))
print("std ", np.std(dati))
print("Varianza ", np.var(dati))

matrice_1 = np.array([[1,2], [3,4]])
matrice_2 = np.array([[5,6], [7,8]])

print("\nProdotto mat dot ", np.dot(matrice_1, matrice_2))
print("Prodotto mat matmul ", np.matmul(matrice_1, matrice_2))

print("\nDeterminante ", np.linalg.det(matrice_1))
print("Inversa ", np.linalg.inv(matrice_1))