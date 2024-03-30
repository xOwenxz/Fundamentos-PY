"""
    tipo tupla - lista imutável
"""

nomes= 'Adriano', 'José', 'Maria'
# nomes[1] = 'Tatiane'
print(nomes)

print(list(nomes), nomes[1])

nova_lista = list(nomes)
print(list(nova_lista), nova_lista[1])
nova_lista[0] = 'André'
print(list(nova_lista), nova_lista[1])
print(list(nomes), nomes[1])
