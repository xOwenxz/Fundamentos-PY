"""
Flag Bandeira - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# v3 = 'b'

# print(id(v1))
# print(id(v2))
# print(id(v3))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True # flag
    print('Falso algo')
else:
    print('Não faça algo')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)