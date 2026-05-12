import numpy as np

#Array Unidimensionale
arr = np.array([1, 2, 3, 4, 5])

#Array Bidimensionale
arr2d = np.array([[1,2,3], [4,5,6]])

print("Array Unidimensionale:")
print(arr)
print("\nArray Bidimensionale:")
print(arr2d)

#Array di zeri
zeroarr = np.zeros((10,10)) #np.ones((10, 10))
print("\nArray di zeri 10x10:")
print(zeroarr)

#Attributi Array
print("\nArray unidimensionale (Shape):")
print(arr.shape)
print("\nArray bidimensionale (Shape):")
print(arr2d.shape)
print("\nArray di zeri (Shape):")
print(zeroarr.shape)

print("\nArray unidimensionale (ndim):")
print(arr.ndim)
print("\nArray bidimensionale (ndim):")
print(arr2d.ndim)
print("\nArray di zeri (ndim):")
print(zeroarr.ndim)

print("\nArray unidimensionale (size):")
print(arr.size)
print("\nArray bidimensionale (size):")
print(arr2d.size)
print("\nArray di zeri (size):")
print(zeroarr.size)

print("\nArray unidimensionale (dtype):")
print(arr.dtype)
print("\nArray bidimensionale (dtype):")
print(arr2d.dtype)
print("\nArray di zeri (dtype):")
print(zeroarr.dtype)

print("\nArray unidimensionale (sum):")
print(arr.sum())
print("\nArray bidimensionale (sum):")
print(arr2d.sum())
print("\nArray di zeri (sum):")
print(zeroarr.sum())

print("\nArray unidimensionale (mean):")
print(arr.mean())
print("\nArray bidimensionale (mean):")
print(arr2d.mean())
print("\nArray di zeri (mean):")
print(zeroarr.mean())

print("\nArray unidimensionale (max&min):")
print("max: " + str(arr.max()) + " - i " + str(arr.argmax()))
print("min: " + str(arr.min()) + " - i " + str(arr.argmin()))
print("\nArray bidimensionale (max&min):")
print("max: " + str(arr2d.max()) + " - i " + str(arr2d.argmax()))
print("min: " + str(arr2d.min()) + " - i " + str(arr2d.argmin()))
print("\nArray di zeri (max&min):")
print("max: " + str(zeroarr.max()) + " - i " + str(zeroarr.argmax()))
print("min: " + str(zeroarr.min()) + " - i " + str(zeroarr.argmin()))

arrRange = np.arange(10, 50)
print("\nArray arange: ")
print(arrRange)

reshaped = arrRange.reshape((10, 4))
print("\nArray reshaped:")
print(reshaped)

arrType = arrRange.astype("float64")

print("\nIndexing e Slicing Undimensionale")

# Indexing e Slicing Undimensionale
arrInd = np.arange(1, 6)

print(arrInd)

#indexing base
print(arrInd[0])

#slicing
print(arrInd[1:4])

#boolean indexing
print(arrInd[arrInd > 2])

print("\nIndexing e Slicing Multidimensionale")
#Indexing e Slicing Multidimensionale
arr2dInd = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

print("\n")
print(arr2dInd)

#slicing su righe
print("\n")
print(arr2dInd[1:3])

#slicing su colonne
print("\n")
print(arr2dInd[1:, :3])

#Slicing avanzato
arrSlice = np.arange(0,10)

print("\n")
print(arrSlice)

print("\nSlicing base: ")
print(arrSlice[2:7])

print("\n Slicing con step")
print(arrSlice[1:8:2])

print("\nOmissione strat e stop")
print(arrSlice[:5])
print(arrSlice[5:])

print("\nIndici negativi")
print(arrSlice[-5:])
print(arrSlice[:-5])

#Fancy indexing

arr = np.array([10, 20, 30, 40, 50])

print("\nFancy Indexing")
indices = np.array([1, 3])
print(arr[indices])

indicesList = [0,2,3]
print(arr[indicesList])

array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])


print("\nLinspace")
arr, step = np.linspace(0, 10, 100, endpoint=False, retstep=True)
print(arr)
print(step)

print("\nRandom")
arr = np.random.rand(2, 3)
print(arr)

print("\n")
arr = np.random.randint(10, 100, size=(5, 5))
print(arr)

print("\n")
print(np.random.choice(np.random.randint(10, 100, size=50), size=6))

np.random.seed(42)
arr1 = np.random.randint(1, 1000, size=10)
arr2 = np.random.randint(1, 1000, size=10)
arr3 = np.random.randint(1, 1000, size=10)
print("1", arr1)
print("2", arr2)
print("3", arr3)

print("\n funzioni matematiche semplici")
arr = np.random.randint(10, 100, size=50)
print(arr)
print("Somma arr ", arr.sum())
print("media arr", arr.mean())
print("Standard deviation arr", arr.std())