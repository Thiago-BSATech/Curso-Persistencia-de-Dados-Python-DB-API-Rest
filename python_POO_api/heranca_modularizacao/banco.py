class Banco:
    
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Agencia(Banco):
    
    def __init__(self, nome, preco, numero):
        super().__init(nome, preco)

        self.numero = numero