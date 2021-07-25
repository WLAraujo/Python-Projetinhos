import random

class Tabuleiro:

    def __init__(self, tamanho, qntd_bombas):
        self.tamanho = tamanho
        self.qntd_bombas = qntd_bombas
        self.tabuleiro = self.criar_tabuleiro() 
        self.cavados = set()
        self.atribuir_valores()
        self.quantos = 0

    def criar_tabuleiro(self):
        tabuleiro = [[int(0) for _ in range(0,self.tamanho)] for _ in range(0, self.tamanho)]
        bombas_plantadas = 0
        while bombas_plantadas < self.qntd_bombas:
            col = random.randint(0,self.tamanho-1)
            lin = random.randint(0,self.tamanho-1)
            if tabuleiro[lin][col] == 0:
                tabuleiro[lin][col] = '*'
                bombas_plantadas += 1
        return tabuleiro
    
    def atribuir_valores(self):
        for lin in range(self.tamanho):
            for col in range(self.tamanho):
                if self.tabuleiro[lin][col] == '*':
                    for linha in range(max(0, lin-1), (min(self.tamanho-1, lin+1))+1):
                        for coluna in range(max(0, col-1), (min(self.tamanho-1, col+1))+1):
                            if self.tabuleiro[linha][coluna] != '*':
                                self.tabuleiro[linha][coluna] +=1

    def cavando(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == '*':
            return False
        elif self.tabuleiro[linha][coluna]>0:
            self.cavados.add((linha, coluna))
            return True
        self.cavados.add((linha, coluna))
        for lin in range(max(0, linha-1), min(self.tamanho-1, linha+1)+1):
            for col in range(max(0, coluna-1), min(self.tamanho-1, coluna+1)+1):
                if (lin,col) not in self.cavados:
                    self.cavando(lin, col)
        return True
    
    def tabuleiro_visivel(self):
        tabuleiro_visivel = [["-" for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        colunas = '   '.join([str(i) for i in range(0, self.tamanho)])
        print(' ' + '\t' +'   ' + colunas + '   ')
        for i in range(0, self.tamanho):
            for j in range(0, self.tamanho):
                if (i,j) in self.cavados:
                    tabuleiro_visivel[i][j] = str(self.tabuleiro[i][j])
            print(str(i) + '\t' + ' | ' + ' | '.join(tabuleiro_visivel[i]) + ' | ')

def jogar(tamanho=10, num_bombas=10):
    tabuleiro = Tabuleiro(tamanho, num_bombas)
    tabuleiro.tabuleiro_visivel()
    no_jogo = True
    while len(tabuleiro.cavados) < (tabuleiro.tamanho**2 - num_bombas):
        try:
            coord = input(f'Digite a linha e a coluna que deseja cavar no formato linha espaço coluna:\t').split()
            lin, col = [int(i) for i in coord]
            no_jogo = tabuleiro.cavando(lin, col)
        except ValueError:
            print("Digite um valor válido")
        except IndexError:
            print("Digite um valor dentro dos limites")
        if no_jogo == False:
            tabuleiro.cavados.add((lin,col))
            tabuleiro.tabuleiro_visivel()
            break
        tabuleiro.tabuleiro_visivel()
    if no_jogo == True:
        print('Parábens você venceu!!! :)')
    else:
        print('Você perdeu!!! :(')

def comeco_jogo():
    print("Bem vindo ao campo minado!!!")

    tam = 0
    bombas = 0

    while tam > 20 or tam < 5:
        try:
            tam = int(input("Digite um número n entre 5 e 20 para definir as dimensões do campo nxn\n"))
        except ValueError:
            print("Digite um valor válido!!!")

    while bombas > 50 or bombas < 5:
        try:
            bombas = int(input("Digite um número n entre 5 e 50 para definir a quantidade de bombas no campo\n"))
        except ValueError:
            print("Digite um valor válido!!!")

    jogar(tamanho=tam, num_bombas=bombas)       

comeco_jogo() 



