==== Promoção de Carnes 🥩 ====


📘 Descrição

Programa que simula a promoção de carnes de um Hipermercado Tabajara, calculando o preço total, aplicando o desconto do cartão Tabajara (5%), e gerando um cupom fiscal detalhado da compra.

🧠 Tabela de Preços
Produto	Até 5 Kg	Acima de 5 Kg
Filé Duplo	R$ 12,00	R$ 14,99
Alcatra	R$ 25,00	R$ 29,99
Picanha	R$ 40,00	R$ 49,99
💳 Condições Especiais

Pagamento com Cartão Tabajara: 5% de desconto sobre o total.

Sem limite de quantidade por cliente.

🧩 Estrutura do Código
Função	Descrição
calcular_preco()	Determina o valor total com base no tipo e na quantidade de carne.
aplicar_desconto()	Aplica o desconto se o pagamento for com cartão Tabajara.
gerar_cupom()	Exibe o cupom fiscal formatado com todas as informações da compra.
main()	Função principal: coleta entradas e executa o processo.
🧮 Exemplo de Execução
=== Promoção de Carnes - Hipermercado Tabajara ===
Tipos disponíveis: File | Alcatra | Picanha
Digite o tipo de carne: Picanha
Digite a quantidade (Kg): 6
Forma de pagamento (Dinheiro, Cartão, Tabajara): Tabajara

===== CUPOM FISCAL =====
Tipo de carne: Picanha
Quantidade: 6.00 Kg
Preço total: R$ 299.94
Tipo de pagamento: Tabajara
Desconto: R$ 14.99
Valor a pagar: R$ 284.95
=========================

⚙️ Requisitos

Python 3.8+

Nenhuma biblioteca externa necessária.

Execução via terminal:

python main.py

🧭 Boas Práticas Aplicadas

✅ Código modular com funções bem definidas
✅ Docstrings PEP 257
✅ Estrutura if __name__ == "__main__":
✅ Tratamento de erros com try/except
✅ Formatação de saída profissional e legível

👨‍💻 Autor

Renato Boranga
Desenvolvedor | Cientista de Dados
📍 Projeto criado para prática e demonstração de lógica de programação em Python.