"""  
    split e join com list e str
    split - divide um string
    join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras = frase.split(',')
print(lista_palavras)

lista_palavras = frase.split(', ')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i])
    
for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())    #rstrip() lstrip()