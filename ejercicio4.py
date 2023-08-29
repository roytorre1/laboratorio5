# Considera dos listas, l1 y l2, que contienen tuplas. Cada tupla consta de una cadena de texto y un número entero. La lista l1 tiene 5 elementos y la lista l2 tiene 3 elementos.
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

# a. Crear conjuntos a partir de estas listas
s1 = set(l1)
s2 = set(l2)

# b. Encontrar los elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3
s3 = s1.intersection(s2)

# c. Encontrar los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4
s4 = s1.symmetric_difference(s2)

# d. Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero de cada tupla
l3 = sorted(list(s3.union(s4)), key=lambda x: x[1])

print("Conjunto s3:", s3)
print("Conjunto s4:", s4)
print("Lista l3:", l3)