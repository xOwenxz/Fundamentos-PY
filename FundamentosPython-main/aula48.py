""" 
Lista em Python
Tipo list = Mutável

"""

string = 'ABCDE' 

# lista = list() 
# lista = [];
# print(lista, type(lista))
# print(bool(lista))  #falsy

lista = [123, True, 'Adriano', 1.2, [10]]
print(lista)

print(lista[3])
lista[-3] = "Maria"
print(lista)
print(lista[2], type(lista[2]))
print(lista[-1][0])
del lista[1]
print(lista)
lista.append(50)
print(lista)
lista.append(60)
lista.append(70)
print(lista)
lista.pop()
print(lista)
ultimo_valor = lista.pop()
print(lista, 'Removido ', ultimo_valor)

lista.clear()
print(lista)

lista.insert(0, 'Adriano')
print(lista)

lista.insert(100, 'Maria')
print(lista)

lista.insert(100000, 'Maria')
print(lista)

lista_a = [1,2,3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_d = lista_a.extend(lista_b)
print(lista_d)
print(lista_a)
print(lista_b)


