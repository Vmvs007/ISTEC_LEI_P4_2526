def criarPerfilUtilizador(nome, email, idade, cidade):
    perfilUtilizador={
        "nome":nome,
        "email":email,
        "idade":idade,
        "cidade":cidade
    }

    return perfilUtilizador

def pesquisarPerfil(listaPerfis, emailPesquisar):
    for perfilAtual in listaPerfis:
        if (perfilAtual["email"] == emailPesquisar):
            return perfilAtual

    return None