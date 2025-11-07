Caixa Registradora 🧮
📘 Descrição

Este programa implementa uma caixa registradora rudimentar para a loja Lojas Tabajara.
O operador pode registrar quantos produtos desejar, digitando 0 para finalizar a compra.
O sistema então mostra o total da compra, solicita o valor em dinheiro e calcula o troco.
Após isso, o operador pode iniciar uma nova compra ou encerrar o sistema.

🧠 Lógica do Programa

O operador insere o preço de cada produto.

Quando digita 0, o programa encerra a compra atual.

O sistema calcula o total da compra, solicita o valor pago e exibe o troco.

Ao final, pergunta se deseja iniciar uma nova compra ou encerrar o sistema.

🧩 Estrutura do Código
Função	Descrição
registrar_compra()	Registra os produtos e calcula o total da compra.
processar_pagamento()	Solicita o valor pago e calcula o troco.
main()	Controla o ciclo completo de vendas e repetição de compras.
🧮 Exemplo de Execução
=== Lojas Tabajara ===
Digite o preço dos produtos. Digite 0 para encerrar a compra.

Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00

Compra finalizada com sucesso. Obrigado por comprar na Lojas Tabajara!
========================================

⚙️ Requisitos

Python 3.8+

Nenhuma biblioteca externa necessária.

Execução via terminal:

python main.py

🧭 Boas Práticas Aplicadas

✅ Código modular com funções claras
✅ Docstrings detalhadas (PEP 257)
✅ Estrutura if __name__ == "__main__":
✅ Fluxo contínuo com opção de múltiplas compras
✅ Interface amigável para uso em console

👨‍💻 Autor

Renato Boranga
Desenvolvedor | Cientista de Dados
📍 Projeto criado para prática e demonstração de lógica aplicada a sistemas comerciais simples em Python.