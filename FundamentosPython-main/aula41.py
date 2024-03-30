string = "valorqualquer"

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == " ":
        break
    
    print(letra)
    i += 1
else:
    print("Laço chegou até o fim")