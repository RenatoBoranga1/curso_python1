🗳️ Sistema de Votação em Python
📘 Descrição

Este projeto implementa um sistema simples de votação em Python, onde três candidatos disputam uma eleição.
O programa solicita o número total de eleitores, coleta o voto de cada um e, ao final, exibe o total de votos e o vencedor.

O código foi desenvolvido com boas práticas de programação, uso de funções bem definidas, tratamento de erros e documentação clara, simulando o padrão esperado em avaliações técnicas para vagas de desenvolvedor ou cientista de dados.

🚀 Funcionalidades

Solicita o número total de eleitores.

Exibe os candidatos disponíveis.

Valida as entradas (somente números inteiros e opções válidas).

Conta os votos de forma automática.

Exibe o resultado final com o total de votos e o candidato vencedor.

🧩 Estrutura do Código

Função	Descrição
registrar_voto(candidatos)	Exibe os candidatos e solicita o voto de cada eleitor.
contabilizar_votos(total_eleitores, candidatos)	Controla o processo de votação e acumula os votos.
exibir_resultado(votos, candidatos)	Mostra o resultado final e identifica o vencedor.
main()	Ponto de entrada do programa. Faz a orquestração geral.

🧠 Lógica Utilizada

Definição dos candidatos — armazenados em um dicionário com número e nome.

Laço de repetição para processar cada eleitor individualmente.

Validação de voto — apenas números válidos correspondentes aos candidatos são aceitos.

Armazenamento de votos em um dicionário ({numero_candidato: total_votos}).

Determinação do vencedor com a função max().

💻 Exemplo de Execução

=== SISTEMA DE VOTAÇÃO ===
Digite o número total de eleitores: 3

🗳️ Eleitor 1 de 3
Candidatos:
1 - Candidato A
2 - Candidato B
3 - Candidato C
Digite o número do seu voto: 1

🗳️ Eleitor 2 de 3
Candidatos:
1 - Candidato A
2 - Candidato B
3 - Candidato C
Digite o número do seu voto: 2

🗳️ Eleitor 3 de 3
Candidatos:
1 - Candidato A
2 - Candidato B
3 - Candidato C
Digite o número do seu voto: 1

===== RESULTADO FINAL =====
Candidato A: 2 voto(s)
Candidato B: 1 voto(s)
Candidato C: 0 voto(s)

🏆 Vencedor: Candidato A com 2 voto(s).

🧱 Requisitos

Python 3.8 ou superior

Nenhuma biblioteca externa é necessária

📂 Estrutura de Arquivos
votacao/
│
├── votacao.py        # Código principal do programa
└── README.md         # Documentação do projeto

🧑‍💻 Autor

Renato Boranga
Desenvolvedor & Cientista de Dados
💼 Projeto desenvolvido como exemplo de boas práticas em Python.