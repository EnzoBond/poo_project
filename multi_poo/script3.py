class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def add_pontos(self, pontos_add):
        self.pontos += pontos_add

    def exibir_ponto(self):
        print(f"Seu nome de jogardor é: {self.nome} e seus pontos são: {self.pontos}")