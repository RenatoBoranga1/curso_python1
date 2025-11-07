valor_hora = float (input('Valor por hora: R$ '))
horas_trabalhadas = float(input('Horas trabalhadas: '))

soma = valor_hora * horas_trabalhadas

print (f'Seu salário será de: R$ {soma: .2f}')