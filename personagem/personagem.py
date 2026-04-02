from random import randint
from rich import print, box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

class Personagem:
    def __init__(self, nome, raca, classe, status):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.status = status
        self.nivel = 1
        self.pontos = 0
        self.hp = self.definir_hp()
        self.mana = self.definir_mana()
        self.dano_fisico = self.dano_fisico()
        self.dano_magico = self.dano_magico()
        self.esquiva = self.definir_esquiva()
        self.defesa = self.definir_defesa()
        self.postura = self.definir_postura()
        self.xp = 0
        self.arma = 5

    def esta_vivo(self):
        if self.hp <= 0:
            print('Personagem morto!')

    def definir_hp(self):
        return 50 + self.status['RES'] * 10
    
    def definir_mana(self):
        return 50 + self.status['MAN'] * 15

    def definir_esquiva(self):
        return self.status['DES']

    def definir_defesa(self):
        return self.status['DEF']

    def definir_postura(self):
        return 50 + self.status['POS'] * 10

    def escolher_ataque(self):
        while True:
            tipo = input('[F]ISICO\n[M]AGICO\n>').upper()
            if tipo == 'F':
                if self.dano_fisico <= 0:
                    print('voce é fraco de mais! nao há forças em voce.')
                else: 
                    self.ataque_fisico()
                    break

            elif tipo == 'M':
                if self.dano_magico <= 0:
                    print('voce nao tem mana! nao há forças em voce.')
                else: 
                    self.ataque_magico()
                    break

    def ataque_fisico(self):
        dano = 0
        for i in range(self.arma):
            rolada = randint(0, self.dano_fisico)
            print(f'{i+1}a rolada:', rolada)
            dano += rolada

        print(f'dano total: {dano}')
        return dano

    def ataque_magico(self):
        dano = 0
        for i in range(self.arma):
            rolada = randint(0, self.dano_magico)
            print(f'{i+1}a rolada:', rolada)
            dano += rolada

        print(f'dano total: {dano}')
        return dano    
    
    def dano_fisico(self):
        return self.status['FOR'] 

    def dano_magico(self):
        return self.status['INT']

    def defender(self):
        return randint(0, self.status['DEF'])

    def lancar_magia(self, preco_mana):
        if self.mana <= 0 or preco_mana > self.mana:
            print('Mana baixa! Use um item ou espere recarregar.')
        else:
            self.mana -= preco_mana
            return self.mana

    def receber_dano(self, dano):
        self.hp -= dano
        return self.hp

    def subir_nivel(self):
        self.nivel += 1 
        return self.nivel

    def mostrar(self):
        infos = Table(title="INFORMAÇÕES BÁSICAS", box=box.ASCII)

        infos.add_column("GERAL")
        infos.add_column("STATUS")

        infos.add_row(
            f"NOME:        [#E0E1DD]{self.nome}[/]",
            f"[#B02E2E]FOR: {self.status['FOR']}[/]"
        )
        infos.add_row(
            f"RAÇA:        [#E0E1DD]{self.raca}[/]",
            f"[#C2A83E]AGI: {self.status['AGI']}[/]"
        )
        infos.add_row(
            f"CLASSE:      [#E0E1DD]{self.classe}[/]",
            f"[#5C677D]DEF: {self.status['DEF']}[/]"
        )
        infos.add_row(
            f"LEVEL:       {self.nivel}",
            f"[#7B5EA7]DES: {self.status['DES']}[/]"
        )
        infos.add_row(
            f"",
            f"[#3A86A8]INT: {self.status['INT']}[/]"
        )
        infos.add_row(
            f"[#9D0208]HP:          {self.hp}[/]",
            f"[#355070]MAN: {self.status['MAN']}[/]"
        )
        infos.add_row(
            f"[#1D4ED8]MANA:        {self.mana}[/]",
            f"[#4C956C]RES: {self.status['RES']}[/]"
        )
        infos.add_row(
            f"[#A4161A]DANO FISICO: {self.dano_fisico}[/]",
            f"[#BC6C25]POS: {self.status['POS']}[/]"
        )
        infos.add_row(
            f"[#6930C3]DANO MAGICO: {self.dano_magico}[/]",
            f""
        )
        infos.add_row(
            f"[#D4A373]ESQUIVA:     {self.esquiva}[/]"
        )
        infos.add_row(
            f"[#495057]DEFESA:      {self.defesa}[/]"
        )
        infos.add_row(
            f"[#BC6C25]POSTURA:     {self.postura}[/]"
        )

        print(infos)
