from personagem.criador import criar_personagem
from personagem.personagem import Personagem
from utils.limpar import limpar
from activity.scr_menu import Escolhas
from activity.scr_menu import mostrar_titulo
from activity.scr_menu import main_menu 

def main():

    mostrar_titulo()
    resultado = main_menu()

    if resultado == Escolhas.CRIAR:
        limpar()
        player: Personagem = criar_personagem()

    elif resultado == Escolhas.CARREGAR:
        limpar()
        status_teste = {
            'FOR': 46, 'AGI': 6, 'INT': -10, 'MAN': -6, 
            'DEF': 10, 'RES': 30, 'DES': 4, 'POS': 20
        }
        player = Personagem('asd', 'ORC', 'BARBARO', status_teste)
    
    player.mostrar()
    
    player.escolher_ataque()


if __name__ == '__main__':
    main()
