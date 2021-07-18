from palavras import lista
import string
import random

# Função que devolve uma palavra válida
def palavraValida():
    palavra = '-'
    while '-' in palavra:
        palavra = random.choice(lista)
    return palavra.upper()

def forca():
    palavra = palavraValida()
    letrasPalavra = set(palavra)
    alphabet = set(string.ascii_uppercase)
    letrasUsadas = set()
    vidas = 10

    while len(letrasPalavra) != 0:

        print(f"Você ainda tem {vidas} vidas")

        print("Letras já usadas:", " ".join(letrasUsadas))
        
        listaPalavra = [letra if letra in letrasUsadas else '-' for letra in palavra]
        print("Palavra: ", ' '.join(listaPalavra))

        letra = input("Digite uma letra: ").upper()
        if letra in alphabet - letrasUsadas:
            letrasUsadas.add(letra)
            if letra in letrasPalavra:
                letrasPalavra.remove(letra)
            else:
                vidas = vidas - 1
            print("\n")   
        elif letra in letrasUsadas:
            print("Letra já tentada!\n")
        else:
            print("Entrada inválida!\n")

    if vidas > 0:
        print(f"Parabéns, você adivinhou a palavra {palavra}!")

    else:
        print("É uma pena, mas você perdeu!")

    
forca()



