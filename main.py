from modelos.personagens.personagem import Personagem
from modelos.batalha import Batalha

roberto = Personagem('Roberto', 10)
benedito = Personagem('Benedito', 10)
duelo = Batalha(roberto, benedito)

def main():
    duelo.iniciar_combate()

if __name__ == '__main__':
    main()
