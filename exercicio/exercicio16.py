def maior_num(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None 

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    maior = maior_num(num1, num2)

    if maior is None:
        print("Os números são iguais.")
    else:
        print(f"O maior número é: {maior}")

if __name__ == "__main__":
    main()