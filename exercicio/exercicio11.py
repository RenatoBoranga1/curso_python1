#num1 = int (input('Qual tabuada você precisa ? '))

#tabuada = num1*0, num1*1, num1*2, num1*3, num1*4, num1*5, num1*6, num1*7, num1*8, num1*9, num1*10

#print(tabuada)

#2

num =  int (input('Qual tabuada você precisa? '))

if 1 <= num <= 10:
    print(f'\nTabuada de {num}: ')
    for i in range (1, 11):
        print(f'{num} x {i} = {num * i}')
else:
    print('Número inválido, digite um número entre 0 e 10')