import random

class Compra:
    valor_conta = random.randint(100, 10000)

    def __init__(self, cliente, imposto = round(random.uniform(.10, .25), 2)):
        self.cliente = cliente
        self.imposto = imposto

    def paga_imposto(self):
        pag_imposto = self.valor_conta * self.imposto

        print(f"O nome do cliente é {self.cliente}, o seu imposto é {self.imposto} ,seu pagamento com imposto é: {pag_imposto}")

nome_cliente = input("O nome do cliente é: ")
mostrar_pag = Compra(nome_cliente)
mostrar_pag.paga_imposto()