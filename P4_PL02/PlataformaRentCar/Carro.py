class Carro:

    def __init__(self, marca, modelo, cor, preco_dia, cv, cc, disponivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco_dia = preco_dia
        self.cv = cv
        self.cc = cc
        self.disponivel = disponivel

    def __str__(self):
        return f"{self.marca} | {self.modelo} | {self.preco_dia} € | {self.cv} CV. | {self.cc} cc3"
