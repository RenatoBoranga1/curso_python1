salario = float(input('Digite o salário: R$'))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print (f'O percentual é de: {percentual}%')
print (f'O valor do aumento é de : R$ {aumento:.2f}')
print (f'O novo salário é de: R$ {novo_salario:.2f}')