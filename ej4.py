'''
Retorna todas las palabras de una lista revertidas

['rojo','verde','azul','blanco','negro']

deberia quedar:

['ojor', 'edrev', 'luza', 'ocnalb', 'orgen']


'''

M1 = ['rojo','verde','azul','blanco','negro']


M2 = ['perro', 'gato', 'raton']


M3 = ['cama', 'silla', 'carro', 'sillon', 'matematica', 'LaTeX', 'Python', 'ZoOm']

print(f"\nResult: { (lambda a: [j[::-1] for j in a])(M1) }")
print(f"\nResult: { (lambda a: [j[::-1] for j in a])(M2) }")
print(f"\nResult: { (lambda a: [j[::-1] for j in a])(M3) }")
