class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def mostrar_user(self):
        print(f"O seu usuario é {self.login} e sua senha é {self.senha}")

login_ = input("Qual e o seu login? ")
senha_ = input("Qual é a sua senha? ")

login_geral = Usuario(login_, senha_)
login_geral.mostrar_user()