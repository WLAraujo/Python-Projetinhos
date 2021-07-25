import math
import random
import jogo

class Jogador:
    def __init__(self, letra):
        self.letra = letra

    def movimento(self, jogo):
        pass

class jogadorMaquina(Jogador):
    def __init__(self, letra) :
        super().__init__(letra)
    
    def movimento(self, jogo):
        escolha = random.choice(jogo.movDisponiveis())
        return escolha

class jogadorHumano(Jogador):
    def __init__(self, letra) :
        super().__init__(letra)
    
    def movimento(self, jogo):
        posValida = False
        escolha = None
        while posValida == False:
            pos = input(f'Turno do {self.letra}. Por favor escolha uma posição de 0 a 9.\n') 
            try:
                escolha = int(pos)
                if escolha not in jogo.movDisponiveis():
                    raise ValueError
                posValida = True
            except ValueError:
                print("Posição inválida!!! Escolha de novo.\n")
        return escolha

