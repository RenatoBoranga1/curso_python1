peso_ideal = None

altura = float(input('Digite sua altura: '))
sexo = input ('Digite seu sexo M ou F : ')

while sexo not in ['M', 'F']:
    print('Digite M para Masculino ou F para Feminino')
    sexo = input('Digite seu sexo (M ou F): ')

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    
print(f'Seu peso ideal é: {peso_ideal: .2f} kg')