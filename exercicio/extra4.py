def registrar_compra():
    
    total = 0.0
    contador = 1

    print("\n=== Lojas Tabajara ===")
    print("Digite o preço dos produtos. Digite 0 para encerrar a compra.\n")

    while True:
        preco = float(input(f"Produto {contador}: R$ "))
        if preco == 0:
            break
        total += preco
        contador += 1

    return total

def processar_pagamento(total):
    
    print(f"\nTotal: R$ {total:.2f}")
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}\n")
    print("Compra finalizada com sucesso. Obrigado por comprar na Lojas Tabajara!")
    print("=" * 40)

def main():
    
    while True:
        total = registrar_compra()
        processar_pagamento(total)

        continuar = input("\nDeseja registrar uma nova compra? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nEncerrando o sistema de caixa. Até logo!")
            break

if __name__ == "__main__":
    main()