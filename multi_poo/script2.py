from script1 import Livro, Usuario

nome = "Lucas"
codigo = "8494874"


titulo = "Duna"
autor = "Frank Herbert"

livro_ = Livro(titulo, autor)
usuario_ = Usuario(nome, codigo)

livro_.exibir_metadata()
usuario_.exibir_dados()