import time
import random

class Batalha:
    def __init__(self, lutador1, lutador2):
        self._lutador1 = lutador1
        self._lutador2 = lutador2

    def iniciar_combate(self):
        print(f"\n--- INICIANDO BATALHA: {self._lutador1.nome} VS {self._lutador2.nome} ---\n")
        time.sleep(1.5)
        
        turno = 1
        
        while self._lutador1.vivo and self._lutador2.vivo:
            print(f"--- Turno {turno} ---")
            
            if self._lutador1.velocidade > self._lutador2.velocidade:
                primeiro, segundo = self._lutador1, self._lutador2
            elif self._lutador2.velocidade > self._lutador1.velocidade:
                primeiro, segundo = self._lutador2, self._lutador1
            else:
                primeiro = random.choice([self._lutador1, self._lutador2])
                segundo = self._lutador2 if primeiro == self._lutador1 else self._lutador1

            self._realizar_turno(primeiro, segundo)
            if segundo.vivo:
                self._realizar_turno(segundo, primeiro)
            
            turno += 1
            print()
            time.sleep(1)

        vencedor = self._lutador1 if self._lutador1.vivo else self._lutador2
        print(f"O VENCEDOR É: {vencedor.nome}!")

    def _realizar_turno(self, atacante, defensor):
        atacante.atacar(defensor)
        time.sleep(0.8)