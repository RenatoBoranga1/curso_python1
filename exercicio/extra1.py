def registrar_voto(candidatos):
    
    print("\nCandidatos:")
    for numero, nome in candidatos.items():
        print(f"{numero} - {nome}")

    while True:
        try:
            voto = int(input("Digite o número do seu voto: "))
            if voto in candidatos:
                return voto
            else:
                print("Opção inválida! Escolha um número entre as opções apresentadas.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

def contabilizar_votos(total_eleitores, candidatos):

    votos = {numero: 0 for numero in candidatos}

    for i in range(1, total_eleitores + 1):
        print(f"\nEleitor {i} de {total_eleitores}")
        voto = registrar_voto(candidatos)
        votos[voto] += 1
    return votos


def exibir_resultado(votos, candidatos):

    print("\n===== RESULTADO FINAL =====")
    for numero, total in votos.items():
        print(f"{candidatos[numero]}: {total} voto(s)")

    vencedor = max(votos, key=votos.get)
    print(f"\n🏆 Vencedor: {candidatos[vencedor]} com {votos[vencedor]} voto(s).")

def main():
    print("=== SISTEMA DE VOTAÇÃO ===")
    try:
        total_eleitores = int(input("Digite o número total de eleitores: "))
        if total_eleitores <= 0:
            print("⚠️ O número de eleitores deve ser maior que zero.")
            return
    except ValueError:
        print("⚠️ Entrada inválida! Digite um número inteiro.")
        return

    candidatos = {
        1: "Candidato A",
        2: "Candidato B",
        3: "Candidato C"
    }

    votos = contabilizar_votos(total_eleitores, candidatos)
    exibir_resultado(votos, candidatos)

if __name__ == "__main__":
    main()