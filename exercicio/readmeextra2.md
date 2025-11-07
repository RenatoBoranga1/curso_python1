🌍 Crescimento Populacional
📘 Descrição

Este programa calcula o número de anos necessários para que a população de um país A ultrapasse ou iguale a população de um país B, considerando suas taxas anuais de crescimento.

O problema é resolvido utilizando um laço de repetição while, que simula o crescimento populacional ano a ano até que a condição seja atingida.

🧠 Lógica do Problema

País A

População inicial: 80.000

Taxa de crescimento: 3% ao ano

País B

População inicial: 200.000

Taxa de crescimento: 1,5% ao ano

O programa incrementa as populações anualmente de acordo com suas respectivas taxas, até que população A >= população B.

🧩 Estrutura do Código

O código foi desenvolvido com boas práticas e dividido em duas funções principais:

calcular_anos(pop_a, taxa_a, pop_b, taxa_b)

Realiza o cálculo e retorna o número de anos necessários.

main()

Função principal que organiza a execução do programa e apresenta os resultados formatados.

🧮 Exemplo de Execução
=== CRESCIMENTO POPULACIONAL ===

População inicial de A: 80,000
População inicial de B: 200,000
Taxa de crescimento A: 3.0% ao ano
Taxa de crescimento B: 1.5% ao ano

➡️ Serão necessários 63 anos para que o país A ultrapasse ou iguale a população do país B.

🧱 Estrutura de Arquivos
extra02_crescimento_populacional/
│
├── main.py          # Código principal com funções e execução
└── README.md        # Documentação do projeto

⚙️ Requisitos

Python 3.8+

Nenhuma biblioteca externa é necessária.

Execução via terminal:

python main.py

🧭 Boas Práticas Aplicadas

✅ Código modularizado com funções.
✅ Docstrings no formato PEP 257.
✅ Identificadores descritivos.
✅ Impressões formatadas com separadores de milhar e casas decimais.
✅ Uso do bloco if __name__ == "__main__": para controle de execução.

💡 Autor

Renato Boranga
Desenvolvedor | Cientista de Dados
📍 Projeto criado para fins de prática e avaliação técnica.