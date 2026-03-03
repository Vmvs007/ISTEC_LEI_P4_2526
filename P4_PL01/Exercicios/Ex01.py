from Exercicios.Ex01Funcoes import *

lista = [4, 7, 13, 44, 91, 2, 142, 5, 8]

print("_____ Lista Original _____")
print(lista)

print("\n_____ Lista Filtrada: Pares _____")
listaFiltrada = filtrarParesLista(lista)
print(listaFiltrada)

print("\n_____ Lista Filtrada: Impares _____")
listaFiltrada = filtrarImparesLista(lista)
print(listaFiltrada)
