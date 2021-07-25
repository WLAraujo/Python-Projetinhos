import random

class Tabuleiro:

    def __init__(self, tamanho, qntd_bombas):
        self.tamanho = tamanho
        self.qntd_bombas = qntd_bombas
        self.tabuleiro = self.criar_tabuleiro() 
        self.cavados = set()
        self.atribuir_valores()

    def criar_tabuleiro(self):
        tabuleiro = [[int(0) for _ in range(0,self.tamanho)] for _ in range(0, self.tamanho)]
        bombas_plantadas = 0
        while bombas_plantadas < self.qntd_bombas:
            col = random.randint(0,self.qntd_bombas-1)
            lin = random.randint(0,self.qntd_bombas-1)
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
        for linha in range(max(0, linha-1), (min(self.tamanho-1, linha+1))+1):
            for coluna in range(max(0, coluna-1), (min(self.tamanho-1, coluna+1))+1):
                if (linha,coluna) in self.cavados:
                    continue
                self.cavando(linha, coluna)
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
    tabuleiro = Tabuleiro(10, num_bombas)
    tabuleiro.tabuleiro_visivel()
    no_jogo = True
    while len(tabuleiro.cavados) < (tabuleiro.tamanho**2 - num_bombas) and no_jogo == True :
        try:
            col = int(input(f'Digite a coluna que deseja cavar:\t'))
            lin = int(input(f'Digite a linha que deseja cavar:\t'))
            no_jogo = tabuleiro.cavando(lin, col)
        except ValueError:
            print("Digite um valor válido")
        tabuleiro.tabuleiro_visivel()
    tabuleiro.tabuleiro_visivel()
    if no_jogo == False:
        print('Você perdeu!!! :(')
    else:
        print('Parábens você venceu!!! :)')

jogar()        



