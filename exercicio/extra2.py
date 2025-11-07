def calcular_anos(pop_a, taxa_a, pop_b, taxa_b):

    anos = 0
    while pop_a < pop_b:
        pop_a += pop_a * (taxa_a / 100)
        pop_b += pop_b * (taxa_b / 100)
        anos += 1
    return anos

def main():
    print("=== CRESCIMENTO POPULACIONAL ===\n")

    populacao_a = 80000
    taxa_a = 3.0
    populacao_b = 200000
    taxa_b = 1.5

    anos = calcular_anos(populacao_a, taxa_a, populacao_b, taxa_b)

    print(f"População inicial de A: {populacao_a:,}")
    print(f"População inicial de B: {populacao_b:,}")
    print(f"Taxa de crescimento A: {taxa_a}% ao ano")
    print(f"Taxa de crescimento B: {taxa_b}% ao ano")
    print(f"\nSerão necessários {anos} anos para que o país A ultrapasse ou iguale a população do país B.")


if __name__ == "__main__":
    main()