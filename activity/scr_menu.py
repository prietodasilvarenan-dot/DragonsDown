import time
import os
from enum import Enum

class Escolhas(Enum):
    CRIAR = 1
    CARREGAR = 2

def mostrar_titulo():
    texto = [
    "________                                              ________",
    "\\______ \\____________     ____   ____   ____   ______ \\______ \\   ______  _  ______",
    " |    |  \\_  __ \\__  \\   / ___\\ /  _ \\ /    \\ /  ___/  |    |  \\ /  _ \\ \\/ \\/ /    \\",
    " |    `   \\  | \\// __ \\_/ /_/  >  <_> )   |  \\\\___ \\   |    `   (  <_> )     /   |  \\",
    "/_______  /__|  (____  /\\___  / \\____/|___|  /____  > /_______  /\\____/ \\/\\_/|___|  /",
    "        \\/           \\/_____/             \\/     \\/          \\/                  \\/"
    ]

    largura = max(len(l) for l in texto)

    for i in range(largura + 1):
        os.system("clear")

        for linha in texto:
            print(linha[:i])

        time.sleep(0.02)

def main_menu():
    print('''
    Bem vindo ao DragonsDown!
    
    Deseja:
    1- Criar um novo save
    2- Carregar um save 
    3- Sair
    ''')
    while True:
        escolha = int(input('>-->'))
        if escolha == 1:
            return Escolhas.CRIAR

        elif escolha == 2:
            return Escolhas.CARREGAR

        elif escolha == 3:
            exit()

        else: print('Insira um valor valido!')