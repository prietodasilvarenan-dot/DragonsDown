from status.status import status_chave, status_valor
from racas.racas import racas
from classes.classes import classes
from utils.limpar import limpar
from personagem.personagem import Personagem
from rich import print, box
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console

console = Console()

def criar_personagem():
    while True:
        nome = criar_nome()


        console.print(Columns([mostrar_racas(),mostrar_atributos()],equal=True))
        raca, raca_status = selecionar("raca", racas)
        print(mostrar_raca_escolhida(raca, raca_status))

        console.print(Columns([mostrar_classes(), mostrar_atributos()], equal=True))
        classe, classe_status = selecionar("classe", classes)
        

        status = somar_atributos(status_valor.copy(), raca_status, classe_status)
        add_pontos(nome, raca, classe, status, 20)
        mostrar_status(nome, raca, classe, status)

        while True:
            confirmacao = input('Confirma criar este personagem? [s/n]\n>-->').lower()
            if confirmacao == 's':
                print('Personagem criado!')
                status_dict = dict(zip(status_chave, status))
                return Personagem(nome, raca, classe, status_dict) 
            elif confirmacao == 'n':
                print('Personagem nao criado!')
                break
            else:
                print('Tente novamente')

def criar_nome():
    nome = input('escolha um nome para o seu persongem\n>--> ')
    limpar()
    return nome

def mostrar_racas():
    tabela_racas = Table("RAÇAS", style='bold', box=box.ASCII_DOUBLE_HEAD)

    for atributo in status_chave:
        tabela_racas.add_column(atributo)

    for raca, atrib in racas.items():
        valores = [
            f'[bold #00ff00]{atrib[chave]}[/]' 
            if atrib[chave] > 0 else f'[bold #ff0000]{atrib[chave]}[/]' 
            for chave in status_chave
        ]
        tabela_racas.add_row(raca, *valores, style='bold')
    return tabela_racas

def mostrar_raca_escolhida(raca, raca_status):
    raca_escolhida = Table(title="RAÇA ESCOLHIDA", box=box.ASCII, style='bold')
    raca_escolhida.add_column("RAÇA      ")
    
    for atrib in status_chave:
        raca_escolhida.add_column(atrib)

    raca_escolhida.add_row(raca, *[str(x) for x in raca_status], style='bold')

    return raca_escolhida

def mostrar_classes():
    tabela_classes = Table(f"CLASSES", style='bold', box=box.ASCII_DOUBLE_HEAD)
    for atributo in status_chave:
        tabela_classes.add_column(atributo)

    for classe, atrib in classes.items():
        valores = [
            f'[bold #00ff00]{atrib[chave]}[/]' 
            if atrib[chave] > 0 else f'[bold #ff0000]{atrib[chave]}[/]' 
            for chave in status_chave
        ]
        tabela_classes.add_row(classe, *valores, style='bold')
    return tabela_classes

def selecionar(tipo, dicionario):
    while True:
        escolha = input(f'escolha uma dessas {tipo}s\n>--> ').upper()
        if escolha in dicionario:
            print(f"{tipo} escolhida: {escolha}")
            status_tipo = [dicionario[escolha][k] for k in status_chave]
            limpar()
            return escolha, status_tipo

def somar_atributos(status, raca, classe):
    for i in range(len(status)):
        status[i] += raca[i] + classe[i]
    return status

def add_pontos(nome, raca, classe, status, qtd_pontos):
    while qtd_pontos > 0: 
        mostrar_status(nome, raca, classe, status)
        print(f'Pontos disponíveis: [bold yellow]{qtd_pontos}[/]')
        entrada = input("Digite o atributo e a quantidade (ex: FOR 5)\n>--> ").upper().split()
        
        if len(entrada) != 2:
            limpar()
            print("[red]Formato inválido! Use: ATRIBUTO QUANTIDADE[/]")
            continue

        atrib_input, qtd_str = entrada
        
        if atrib_input in status_chave:
            try:
                qtd = int(qtd_str)
                if 0 < qtd <= qtd_pontos:
                    limpar()
                    idx = status_chave.index(atrib_input)
                    status[idx] += qtd
                    qtd_pontos -= qtd
                else:
                    limpar()
                    print(f'[red]Quantidade inválida! Você tem {qtd_pontos} pontos.[/]')
            except ValueError:
                limpar()
                print('[red]A quantidade deve ser um número inteiro![/]')
        else:
            limpar()
            print('[red]Atributo não encontrado![/]')

def mostrar_status(nome, raca, classe, status):
    
    for_, agi_, int_, man_, def_, res_, des_, pos_ = status
    hp = 50 + res_ * 10
    mana = 50 + man_ * 10
    postura = 50 + pos_ * 10

    infos = Table(title="informações basicas", box=box.ASCII)
    infos.add_column("GERAL")
    infos.add_column("ATRIBUTOS")

    infos.add_row(f"NOME:        {nome}", f"FOR: {for_}")
    infos.add_row(f"RAÇA:        {raca}", f"AGI: {agi_}")
    infos.add_row(f"CLASSE:      {classe}", f"INT: {int_}")
    infos.add_row("", f"MAN: {man_}")
    infos.add_row(f"HP:          {hp}", f"DEF: {def_}")
    infos.add_row(f"MANA:        {mana}", f"RES: {res_}")
    infos.add_row(f"DANO FISICO: {for_}", f"DES: {des_}")
    infos.add_row(f"DANO MAGICO: {int_}", f"POS: {pos_}")
    infos.add_row(f"ESQUIVA:     {des_}")
    infos.add_row(f"DEFESA:      {def_}")
    infos.add_row(f"POSTURA:     {postura}")


    print(infos)

def mostrar_atributos():
    atributos = Table(title="informações", box=box.ASCII)
    atributos.add_column("Atributo")
    atributos.add_column("Função")

    atributos.add_row("FOR", "É o dano maximo que seu personagem pode dar.")
    atributos.add_row("AGI", "É um complemento da força do seu personagem.")
    atributos.add_row("INT", "É o dano magico do seu personagem.")
    atributos.add_row("MAN", "É a mana do seu personagem. 15 * MAN + 50")
    atributos.add_row("DEF", "É o quanto de dano que seu personagem pode defender.")
    atributos.add_row("RES", "É a vida do seu personagem. 10 * RES + 50")
    atributos.add_row("DES", "É a esquiva do seu personagem.")
    atributos.add_row("POS", "É a postura do seu personagem. 10 * POS + 50")

    return atributos
