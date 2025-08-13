import random

class desconto:
    desconto_global = .01

    def __init__(self, nome, saldo_atual):
        self.nome = nome
        self.saldo_atual = saldo_atual
        
    def show_result(self):
        preco_final = self.saldo_atual * self.desconto_global
        print(f"Você é {self.nome},e o seu saldo atual é de {self.saldo_atual} e o saldo com desconto ficou: {preco_final}")

input_nome = input("Qual é o seu nome? ")
saldo_atual_ = random.randint(10, 100000)
show_saldo = desconto(input_nome, saldo_atual_)
show_saldo.show_result()

