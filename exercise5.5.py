from exercise5 import Produto

prod1 = Produto("Notebook", 3500.50)

print(f"Produto:{prod1.get_nome()} e o preço é R$ {prod1.get_preco():.2f}")

prod1.set_nome("Notebook Gamer")
prod1.set_preco(4500.10)
print(f"Produto:{prod1.get_nome()} e o preço é R$ {prod1.get_preco():.2f}")

prod1.set_nome("")
prod1.set_preco(-200)