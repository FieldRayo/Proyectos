import numpy

result = []
size = input()
size = [int(x) for x in size.split()] # Convierte el primer input en enteros y en lista '4,3,2' ->[4,3,2]

for i in range( size[0] * size[-1]): # Recibe inputs del arreglo a concatenar y los convierte la lista adecuada '1 2' -> [[1,2],...]
    result.append((input()).split())

for n, i in enumerate(result): # Convierte todos los valores de result se convierten a enteros
    result[n-1] = [[int (x) for x in result[n-1]]]


print(numpy.concatenate(result)) # Concatena los valores de result

# Ejemplo

'''
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
'''

# Output
'''
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]
 [3 4]]
'''

#Este problema es de Hacker Rank llamado "Concatenar" PD: que hueva que sean tan especificos con el resultado
