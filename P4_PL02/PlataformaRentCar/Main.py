from PlataformaRentCar.Carro import Carro

catalogo = [
    Carro("Mercedes", "A45", "Preto", 75, 420, 2000, True),
    Carro("BMW", "M2", "Azul", 80, 450, 3000, True),
    Carro("Mata", "Velhos", "Vermelho Sport", 150, 500, 3500, True)
]


def adicionarCarro():
    marcaNova = input("Marca: ")
    modeloNovo = input("Modelo: ")
    corNova = input("Cor: ")
    precoDiaNovo = float(input("Preço por Dia (€): "))
    cvNova = int(input("CV: "))
    ccNova = int(input("CC: "))

    catalogo.append(Carro(marcaNova, modeloNovo, corNova, precoDiaNovo, cvNova, ccNova, True))


def removerCarro():
    marcaRemover = input("Marca: ")
    modeloRemover = input("Modelo: ")

    for carroAtual in catalogo:
        if marcaRemover == carroAtual.marca and modeloRemover == carroAtual.modelo:
            catalogo.remove(carroAtual)
            print("Carro Removido")


def catalogoCompletoCarro():
    print("______________________________________________________________________")
    for carroAtual in catalogo:
        print(carroAtual)
    print("______________________________________________________________________")


def catalogoDisponiveisCarro():
    print("______________________________________________________________________")
    for carroAtual in catalogo:
        if carroAtual.disponivel:
            print(carroAtual)
    print("______________________________________________________________________")


def rececionarCarro():
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    for carroAtual in catalogo:
        if marca == carroAtual.marca and modelo == carroAtual.modelo:
            carroAtual.disponivel = True
            print(f"Receção feita com sucesso: {carroAtual}")


def alugarCarro():
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    for carroAtual in catalogo:
        if marca == carroAtual.marca and modelo == carroAtual.modelo:
            carroAtual.disponivel = False
            print(f"Aluguer feito com sucesso: {carroAtual}")


def rendimentosDiarios():
    rendimentos = 0

    for carroAtual in catalogo:
        if not carroAtual.disponivel:
            rendimentos += carroAtual.preco_dia

    return rendimentos


def menu():
    while (True):
        print("\n_*_*_*_*_*_ BEM-VINDO/A AO RENT-A-CAR XPTO _*_*_*_*_*_")
        print("1. Adicionar Carro")
        print("2. Remover Carro")
        print("3. Catálogo")
        print("4. Rececionar um Carro")
        print("5. Alugar um Carro")
        print("6. Calcular ganhos dia")
        print("0. Sair")

        opcao = int(input("Opção: "))

        match (opcao):
            case 1:
                print("\nADICIONAR CARRO")
                adicionarCarro()

            case 2:
                print("\nREMOVER CARRO")
                removerCarro()

            case 3:
                print("\nCATÁLOGO")
                opcaoCatalogo = int(input("1. Completo | 2. Disponíveis: "))

                if opcaoCatalogo == 1:
                    catalogoCompletoCarro()
                elif opcaoCatalogo == 2:
                    catalogoDisponiveisCarro()
                else:
                    print("Selecione 1 ou 2!")

            case 4:
                print("\nRECECIONAR UM CARRO")
                rececionarCarro()

            case 5:
                print("\nALUGAR CARRO")
                alugarCarro()

            case 6:
                print("\nRENDIMENTOS DIÁRIOS")
                print(rendimentosDiarios(), "€")

            case 0:
                print("\nA encerrar...")

            case _:
                print("\nOpção inválida!")


menu()
