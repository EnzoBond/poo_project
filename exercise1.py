class Carro:
    def __init__(self, marca, tipo, ano):
        self.marca = marca
        self.tipo = tipo
        self.ano = ano

    def apresentar_carro(self):
        print(f"Meu carro é um {self.marca} {self.tipo} {self.ano}")

input_marca = input("Qual é a marca do seu carro: ")
input_tipo = input("Qual é o tipo do seu carro: ")
input_ano = input("Qual é o ano do seu carro: ")
info_geral = Carro(input_marca, input_tipo, input_ano)
info_geral.apresentar_carro()

