class Clientes:

    clientes = []
    contador = 1
    def __init__(self, nome, email, telefone, logradouro, numero, bairro, cidade, estado):

        self.nome = nome
        self.email = email 
        self.telefone = telefone
        self.logradouro = logradouro
        self.numero = numero 
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado



    @classmethod
    def listar_clientes(cls):  
        return cls.clientes
    

    @classmethod
    def add(cls, nome):
        novo_cliente = cls(nome)
        cls.filmes.append(novo_cliente)
        return novo_cliente
    
    



