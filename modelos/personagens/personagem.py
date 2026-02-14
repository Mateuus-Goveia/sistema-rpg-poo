class Personagem:
    lista_de_personagens = []

    def __init__(self, nome, velocidade):
       
        self._nome = nome 
        self._vida = 100
        self._forca = 10
        self._velocidade = velocidade
        self._vivo = True
        Personagem.lista_de_personagens.append(self)

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    @property
    def forca(self):
        return self._forca
    
    @property
    def velocidade(self):
        return self._velocidade
    
    @property
    def vivo(self):
        return self._vivo

    def tomar_dano(self, quantidade):
        self._vida -= quantidade
        if self._vida <= 0:
            self._vida = 0
            self._vivo = False
        print(f"{self.nome} recebeu {quantidade} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.tomar_dano(self.forca)
    
    @classmethod
    def exibir_personagem(cls):
        print('-=-=-=-=-Lista de Personagens-=-=-=-=-')
        for personagem in cls.lista_de_personagens:
            print(f'{personagem.nome}')
            