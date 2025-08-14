class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_metadata(self):
        print(f"O titulo do livro é {self.titulo} e o autor é: {self.autor}")

class Usuario:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_dados(self):
        print(f"O nome do usuario é: {self.nome} e o codigo dele é {self.codigo}")