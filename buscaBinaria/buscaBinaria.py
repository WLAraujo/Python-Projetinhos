import math as m

def buscaNaive(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return [True, i]
    return [False, -alvo]

def buscaBinaria(lista, alvo, mini, maxi, pos):
    if lista[pos] == alvo:
        return [True, pos]
    elif maxi == mini:
        return [False, -1]
    elif alvo < lista[pos]:
        return buscaBinaria(lista, alvo, mini, pos-1, pos-max((pos-mini)//2, 1))
    elif alvo > lista[pos]:
        return buscaBinaria(lista, alvo, pos+1, maxi, pos+max((maxi-pos)//2, 1))

lista = [int(item) for item in input("Digite uma lista de números ordenados\n").split()]
alvo = int(input("Digite o valor que será procurado\n"))
mini = 0
maxi = len(lista)-1
pos = (maxi-mini)//2
if alvo < lista[0] or alvo > lista[-1]:
    print([False, -1])
else:
    print(buscaBinaria(lista, alvo, mini, maxi, pos))
    