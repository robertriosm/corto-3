lista = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']

filtr = ['rojo', 'verde', 'azul', 'gris', 'negro']

listFiltr = lambda lista, filtr : [item for item in lista if item not in filtr] 

print(listFiltr(lista, filtr))