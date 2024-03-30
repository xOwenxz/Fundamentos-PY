nome = 'Luiz'
nome = 'João'

print(nome)

lista_a = ['Luiz', 'João', 1, True, 1.2]
lista_b = lista_a

print(lista_a)
print(lista_b)

lista_a[0] = 'Adriano'

print(lista_a)
print(lista_b)

lista_b = lista_a.copy()
print(lista_a)
print(lista_b)

lista_a[0] = 'Thomas'

print(lista_a)
print(lista_b)

