# app.py

from view import exibir_apresentacao, limpar_tela, exibir_opcoes_filtros, exibir_lista_nomes
from model import Animal
from database import banco_de_dados

def listar_racas_disponiveis():
    racas_disponiveis = set([animal.raca for animal in banco_de_dados.animais])
    print("\nRaças disponíveis:")
    return racas_disponiveis

def listar_opcoes_numericamente(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    num_opcao = int(input("Escolha o número correspondente à opção: "))
    return list(opcoes)[num_opcao - 1]

def main():
    limpar_tela()
    exibir_apresentacao()

    while True:
        exibir_opcoes_filtros()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            racas_disponiveis = listar_racas_disponiveis()
            raca = listar_opcoes_numericamente(racas_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_raca(raca)
        elif opcao == '2':
            personalidades_disponiveis = set([animal.personalidade for animal in banco_de_dados.animais])
            print("\nPersonalidades disponíveis:")
            personalidade = listar_opcoes_numericamente(personalidades_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_personalidade(personalidade)
        elif opcao == '3':
            aparencias_disponiveis = set([animal.aparencia for animal in banco_de_dados.animais])
            print("\nAparências disponíveis:")
            aparencia = listar_opcoes_numericamente(aparencias_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_aparencia(aparencia)
        elif opcao == '4':
            exit()
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            continue

        exibir_lista_nomes(nomes_filtrados)
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
