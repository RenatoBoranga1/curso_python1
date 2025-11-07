def tabuada(num):
    print(f"Tabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
    print()

def main():
    num = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))
    if 1 <= num <= 10:
        tabuada(num)
    else:
        print("Digitar um número entre 1 e 10.")

if __name__ == "__main__":
    main()