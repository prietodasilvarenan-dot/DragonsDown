import os
def limpar():
    # Limpa no Windows, Linux ou macOS
    os.system('cls' if os.name == 'nt' else 'clear')
