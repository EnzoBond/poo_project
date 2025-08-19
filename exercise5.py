class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco


    def get_nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        if isinstance(novo_nome,str) and novo_nome.strip != "":
            self._nome = novo_nome
        else:
            print("Nome Invalido!!")

    def get_preco(self):
        return self._preco
    
    def set_preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Preço Invalido!!")