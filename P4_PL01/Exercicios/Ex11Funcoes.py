import json


def quiz():
    questionarioCompleto = lerFicheiroJson("../Ficheiros/Quiz.json")
    respostasCertas = 0
    respostasErradas = 0

    for perguntaAtual in questionarioCompleto:
        print()
        print(perguntaAtual["pergunta"])
        print("A)", perguntaAtual["a"])
        print("B)", perguntaAtual["b"])
        print("C)", perguntaAtual["c"])

        palpite = input("Resposta (A|B|C): ").lower()

        if (perguntaAtual["resposta"] == palpite):
            respostasCertas += 1
        else:
            respostasErradas += 1

    print("\n_*_*_*_*_*_ FIM DO QUIZ _*_*_*_*_*_")
    print(f"Respostas Certas: {respostasCertas}/{len(questionarioCompleto)}")


def lerFicheiroJson(filename):
    data = {}
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except:
        print("Erro: não foi possível abrir o ficheiro")
    else:
        return data
