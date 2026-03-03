from Exercicios.Ex04Funcoes import criarPerfilUtilizador, pesquisarPerfil

listaPerfis = []

listaPerfis.append(criarPerfilUtilizador("Joaquim", "quim@mail.pt", 30, "Porto"))
listaPerfis.append(criarPerfilUtilizador("Joana", "joana@mail.pt", 26, "Lisboa"))
listaPerfis.append(criarPerfilUtilizador("José", "ze@mail.pt", 40, "Porto"))

while (True):
    print("\n\n_____ PERFIS _____")
    print("1. Novo Perfil")
    print("2. Consultar Perfil (email)")
    print("3. Todos os Perfis")
    print("0. Sair")

    opcao = int(input("Insira a sua opção: "))

    match (opcao):
        case 1:
            print("\nNovo Perfil")
            novoNome = input("Nome: ")
            novoEmail = input("Email: ")
            novaIdade = int(input("Idade: "))
            novaCidade = input("Cidade: ")
            listaPerfis.append(criarPerfilUtilizador(novoNome, novoEmail, novaIdade, novaCidade))

        case 2:
            print("\nConsultar Perfil (email)")
            emailPesquisar = input("Email a pesquisar: ")

            print(pesquisarPerfil(listaPerfis,emailPesquisar))

        case 3:
            print("\nTodos os Perfis")
            print(listaPerfis)

        case 0:
            print("\nA encerrar...")
            break

        case _:
            print("\nOpção Inválida")
