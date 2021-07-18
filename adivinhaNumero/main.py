import random

# Na função usuarioChute o jogador é o usuário que digita um número com base no feedback do computador
# Na função computadorChute o jogador é o computador e ele altera o número com base no feedback do usuário

def usuarioChute(x):
    num = random.randint(1, x)
    chute = 0
    while chute != num:
        chute = int(input(f'Digite um número entre 1 e {x}\n'))
        if (chute < num):
            print("Chute muito baixo!")
        elif (chute > num):
            print("Chute muito alto!")
    print(f'Parábens, o número certo era {num}!')

def computadorChute(x):
    feedback = ""
    inf = 1
    sup = x
    while feedback != "c":
        chute = random.randint(inf, sup)
        print(f'Nosso chute é {chute}\n')
        feedback = input('''Esse chute está correto?
        Digite c para correto
        Digite a para muito alto
        Digite b para muito baixo\n''')
        if feedback == 'a':
            sup = chute - 1
        elif feedback == 'b':
            inf = chute + 1
        elif sup == inf:
            chute = sup
            break
    print(f'O número certo era {chute}! Obrigado por jogar!')

modo = 3

while modo != 1 and modo !=2:
    modo = int(input('''Qual modo você quer jogar?
    1 - Usuário chuta número do computador
    2 - Computador chuta número do usuário\n'''))
    
limite = int(input("Digite um número para ser o limite superior dos valores\n"))

if modo == 1:
    usuarioChute(limite)
elif modo == 2:
    computadorChute(limite)

