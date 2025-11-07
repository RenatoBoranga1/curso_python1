def calcular_preco(tipo_carne: str, quantidade: float) -> float:

    precos = {
        "file": (12.00, 14.99),
        "alcatra": (25.00, 29.99),
        "picanha": (40.00, 49.99)
    }

    tipo_carne = tipo_carne.lower()
    if tipo_carne not in precos:
        raise ValueError("Tipo de carne inválido. Escolha entre File, Alcatra ou Picanha.")

    preco_ate5, preco_acima5 = precos[tipo_carne]
    return preco_ate5 * quantidade if quantidade <= 5 else preco_acima5 * quantidade


def aplicar_desconto(valor_total: float, pagamento: str) -> float:
    
    if pagamento.lower() == "tabajara":
        return valor_total * 0.95  # 5% de desconto
    return valor_total


def gerar_cupom(tipo_carne: str, quantidade: float, pagamento: str):
    """
    Gera e exibe o cupom fiscal da compra.
    """
    valor_total = calcular_preco(tipo_carne, quantidade)
    valor_com_desconto = aplicar_desconto(valor_total, pagamento)
    desconto = valor_total - valor_com_desconto

    print("\n===== CUPOM FISCAL =====")
    print(f"Tipo de carne: {tipo_carne.capitalize()}")
    print(f"Quantidade: {quantidade:.2f} Kg")
    print(f"Preço total: R$ {valor_total:.2f}")
    print(f"Tipo de pagamento: {pagamento.capitalize()}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_com_desconto:.2f}")
    print("=========================")

def main():
    print("=== Promoção de Carnes - Hipermercado Tabajara ===")
    print("Tipos disponíveis: File | Alcatra | Picanha")

    tipo_carne = input("Digite o tipo de carne: ").strip()
    quantidade = float(input("Digite a quantidade (Kg): "))
    pagamento = input("Forma de pagamento (Dinheiro, Cartão, Tabajara): ").strip()

    try:
        gerar_cupom(tipo_carne, quantidade, pagamento)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()