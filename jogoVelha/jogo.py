from jogador import jogadorHumano
from jogador import jogadorMaquina

class JogoVelha:
    def __init__(self):
        self.tabuleiro = [' ' for n in range(9)]
        self.vencedor = None

    def imprimirTabuleiro(self):
        for linha in [self.tabuleiro[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(linha) + ' | ')

    @staticmethod
    def imprimirPosTabuleiro():
        posTabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in posTabuleiro:
            print(' | ' + ' | '.join(linha) + ' | ')
    
    def movDisponiveis(self):
        movs = []
        for (i, vaga) in enumerate(self.tabuleiro):
            if vaga == ' ':
                movs.append(i)
        return movs

    def posVazias(self):
        return (' ' in self.tabuleiro)

    def qntdVazias(self):
        return self.tabuleiro.count(' ')

    def movimento(self, quadrado, letra):
        if self.tabuleiro[quadrado] == ' ':
            self.tabuleiro[quadrado] = letra
            if self.vitoria(quadrado, letra):
                self.vencedor = letra 
            return True
        else:
            return False

    def vitoria(self, quadrado, letra):
        numlinha = quadrado//3
        linha = [self.tabuleiro[ numlinha * 3 : (numlinha+1) * 3]]
        if all([pos == letra for pos in linha]):
            return True
        
        numcoluna = quadrado%3
        coluna = [self.tabuleiro[numcoluna+i*3] for i in range(3)] 
        if all([pos == letra for pos in coluna]):
            return True
        
        if quadrado % 2 == 0:
            diagonal1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all([pos == letra for pos in diagonal1]):
                return True
            if all([pos == letra for pos in diagonal2]):
                return True
        
        return False


def partida(jogo, jogador_x, jogador_o, imprimir=True):
    if imprimir == True:
        jogo.imprimirPosTabuleiro()

    letra = 'x'

    while jogo.posVazias():
        if letra == 'x':
            quadrado = jogador_x.movimento(jogo)
        else:
            quadrado = jogador_o.movimento(jogo)

        if jogo.movimento(quadrado, letra):
            if imprimir:
                print(letra + ' faz o movimento na posição ' + str(quadrado))
                jogo.imprimirTabuleiro()
                print(' ')

            if jogo.vencedor:
                if imprimir:
                    print(letra + ' venceu!!!')
                return letra
            
        letra = 'o' if letra == 'x' else 'x'
    
    if print:
        print("Deu empate!!!")

if __name__ == '__main__':
    print("Bem vindo ao jogo da velha!!!\nPor favor, escolha um modo de jogo:\n")
    modo = 3
    while modo != 1 and modo != 2:
        try:
            modo = int(input("1-)Humano contra máquina\n2-)Humano contra humano\n"))
        except ValueError:
            print("Valor inválido!!! Por favor escolha de novo")
        
    if(modo == 1):
        jogador_x = jogadorHumano('x')
        jogador_o = jogadorMaquina('o')
    if(modo == 2):
        jogador_x = jogadorHumano('x')
        jogador_o = jogadorHumano('o')
    j = JogoVelha()
    partida(j, jogador_x, jogador_o, True)
