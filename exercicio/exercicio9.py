print("Responda as perguntas com S para SIM ou N para Não):")


perg1 = input("Telefonou para a vítima? ")
perg2 = input("Esteve no local do crime? ")
perg3 = input("Mora perto da vítima? ")
perg4 = input("Devia para a vítima? ")
perg5 = input("Já trabalhou com a vítima? ")

respostas_positivas = 0

if perg1 == "S":
    respostas_positivas += 1
if perg2 == "S":
    respostas_positivas += 1
if perg3 == "S":
    respostas_positivas += 1
if perg4 == "S":
    respostas_positivas += 1
if perg5 == "S":
    respostas_positivas += 1
    
    
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")


