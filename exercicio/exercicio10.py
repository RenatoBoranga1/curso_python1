nota = int (input('Digite uma nota entre 0 e 10: '))

while nota < 0 or nota > 10:
    print ('Valor inválido, digite uma nota entre 0 e 10')
    nota = int (input('Digite novamente a nota: '))

print(f'Obrigado por participar!')