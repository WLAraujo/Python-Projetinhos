import os
import base64
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# r - arquivo para leitura, o arquivo deve existir
# w - aquivo para escrita, apaga o conteúdo atual caso exista ou cria um novo arquivo
# a - arquivo para escrita, adiciona ao final do conteúdo atual ou cria um arquivo novo

''' Só usar essa função na primeira vez que rodar o programa
def criar_chave:
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arq_chave:
        arq_chave.write(chave)
'''

def retornar_chave():
    file = open("chave.key", "rb")
    chave = file.read()
    file.close()
    return chave

def consulta():
    with open('senhas.txt', 'r') as f:
        for linha in f.readlines():
            data = linha.rstrip()
            conta, senha = data.split('|')
            try:
                senha = fer.decrypt(senha.encode()).decode()
                print(f'Usuário: {conta}\tSenha: {senha}')
            except:
                senha = "Senha mestre não bate"
                print(f'Usuário: {conta}\tSenha: {senha}')

def adicao():

    conta = input("Digite o nome de usuário da conta: ")
    senha = input("Digite o a senha da conta: ")

    with open('senhas.txt', 'a') as f:
        f.write(conta + '|' + fer.encrypt(senha.encode()).decode() + '\n')

def interface():

    print("Bem vindo ao Secret Manager!!!")

    while(True):

        opcao = input("Você gostaria de:\n1-)Adicionar uma senha nova - Digite a\n2-)Consultar as senhas existentes - Digite c\n3-)Sair do programa - Digite s\n")
        
        if opcao == 's':
            break
        elif opcao == 'c':
            consulta()
        elif opcao == 'a':
            adicao()
        else:
            print("Digite uma opção válida!!!")

senha = retornar_chave()
sal = input("Digite a senha mestre: ")
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=sal.encode(),
    iterations=100000)
chave = base64.urlsafe_b64encode(kdf.derive(senha))
fer = Fernet(chave)

interface()