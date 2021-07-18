import random

def jogo():
    user = ''
    while(user != 'r' and user != 'p' and user != 't'):
        user = input("Bem vindo ao pedra, papel e tesoura!\nDigite p para papel\nDigite r para pedra\nDigite t para tesoura\n")
    comp = random.choice(['r', 'p', 't'])
    print(resultado(user, comp))

def resultado(user, comp):
    if user == comp:
        return 'Deu empate!'
    elif (comp == 'r' and user == 'p') or (comp == 'p' and user == 't') or (comp == 't' and user == 'r'):
        return 'Vitória!'
    else:
        return 'Derrota!'
    
jogo()