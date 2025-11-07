#       012345678910 
nome = 'Renato Boranga' # iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print (nome[3])

novo_nome = ''
indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    indice += 1
    novo_nome += letra + '*'


print(novo_nome)