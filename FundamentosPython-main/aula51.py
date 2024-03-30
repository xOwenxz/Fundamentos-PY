"""
    Desempacotamento de lista + tuplas
    
"""

nome1, nome2, nome3 = ['Adriano', 'Maria', 'José']
print(nome2)

# nome2, nome3 = ['Adriano', 'Maria', 'José']
# print(nome2)

nome2, *resto = ['Adriano', 'Maria', 'José']
print(nome2)
print(resto)

