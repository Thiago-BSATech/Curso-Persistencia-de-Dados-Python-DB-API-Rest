from heranca_modularizacao import Banco

class Agencia(Banco):
    
    def __init__(self, nome, preco, numero):
        super().__init(nome, preco)

        self.numero = numero