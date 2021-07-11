def madlib():
    adj = input("Digite um adjetivo: ")
    nome = input("Digite um nome: ")
    verb1 = input("Digite um verbo: ")
    verb2 = input("Digite outro verbo: ")
    animal = input("Digite um animal: ")
    m = f"Olá! eu me chamo {nome} e sou extremamente {adj}.\
    Gosto de {verb1}, mas odeio {verb2}. Tenho um {animal}\
    de estimação."
    print(m)