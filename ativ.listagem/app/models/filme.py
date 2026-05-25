class Filme:

    filmes = []
    id_contador = 1

    def __init__(self, titulo):
        self.id = Filme.id_contador
        self.titulo = titulo
        self.completa = False
        Filme.id_contador += 1

    @classmethod
    def listar_filmes(cls):  
        return cls.filmes   
    
    @classmethod
    def add(cls, titulo):
        novo_filme = cls(titulo)
        cls.filmes.append(novo_filme)
        return novo_filme
    
    @classmethod
    def buscar_por_id(cls, id):
        for filme in cls.filmes:
            if filme.id == id:
                return filme
        return None
    
    @classmethod
    def completar(cls, filme_id):
        filme = cls.buscar_por_id(filme_id)
        if filme:
            filme.completa = True


    @classmethod
    def deletar(cls, filme_id):
        filme_para_deletar = cls.buscar_por_id(filme_id)
        if filme_para_deletar:
            cls.filmes.remove(filme_para_deletar)