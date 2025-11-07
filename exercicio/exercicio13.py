string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

print(f'\nString 1: "{string1}"')
print(f'String 2: "{string2}"')
print(f'Tamanho de "{string1}": {len(string1)} caracteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')

if len(string1) == len(string2):
    print('As duas strings têm o mesmo tamanho.')
else:
    print('As duas strings são de tamanhos diferentes.')

if string1 == string2:
    print('As duas strings possuem conteúdo igual.')
else:
    print('As duas strings possuem conteúdo diferente.')