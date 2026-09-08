# Sistema de votação eleitoral
# Autor: Equipe Codigo Limpo
# Data: 09/06/2026

# Dicionário para armazenar os votos
votos = {}

# Função para registrar voto
def registrar_voto(eleitor, candidato):
    if eleitor in votos:
        print("ERRO: Este eleitor já votou!")
    else:
        votos[eleitor] = candidato
        print("Voto registrado com sucesso!")

# Função para mostrar todos os votos
def mostrar_votos():
    print("\n--- LISTA DE VOTOS ---")
    if len(votos) == 0:
        print("Nenhum voto registrado.")
    else:
        for eleitor, candidato in votos.items():
            print(f"{eleitor} votou em {candidato}")

# Função para verificar candidatos repetidos
def verificar_mesmo_candidato():
    print("\n--- VERIFICAÇÃO ---")
    eleitores = list(votos.keys())
    encontrou = False
    for i in range(len(eleitores)):
        for j in range(i + 1, len(eleitores)):

            e1 = eleitores[i]
            e2 = eleitores[j]

            if votos[e1] == votos[e2]:
                print(f"{e1} e {e2} votaram em {votos[e1]}")
                encontrou = True
    if not encontrou:
        print("Nenhum candidato recebeu votos repetidos.")

# Programa principal
while True:
    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - Registrar voto")
    print("2 - Mostrar votos")
    print("3 - Verificar votos iguais")
    print("4 - Encerrar")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome do eleitor: ")
        print("\nCandidatos disponíveis:")
        print("1 - Candidato A")
        print("2 - Candidato B")
        print("3 - Candidato C")
        escolha = input("Escolha o candidato: ")
        if escolha == "1":
            candidato = "Candidato A"
        elif escolha == "2":
            candidato = "Candidato B"
        elif escolha == "3":
            candidato = "Candidato C"
        else:
            print("Opção inválida!")
            continue
        registrar_voto(nome, candidato)
    elif opcao == "2":
        mostrar_votos()
    elif opcao == "3":
        verificar_mesmo_candidato()

    elif opcao == "4":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida!")