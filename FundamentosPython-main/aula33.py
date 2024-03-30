""" 
Imutáveis que vimos: str, int, float, bool
"""

string = 'adriano'
# string[3] = 'a' # não permitido

nova_string = f'{string[:3]}ABC{string[4:]}'
print(string.capitalize())
print(string.upper())
print(nova_string)
print(nova_string.zfill(20))