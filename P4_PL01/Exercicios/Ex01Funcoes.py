def filtrarParesLista(listaOriginal):

    listaPares = []

    for i in listaOriginal:

        if(i % 2 == 0):
            listaPares.append(i)

    return listaPares

def filtrarImparesLista(listaOriginal):

    listaImpares = []

    for i in listaOriginal:

        if(i % 2 != 0):
            listaImpares.append(i)

    return listaImpares