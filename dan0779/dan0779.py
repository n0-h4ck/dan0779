from time import sleep
import os, subprocess


def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


import time
import random

def falar():
    textos = [
        "— Boas vindas, Daniel!\n— Inicializando sua ferramenta, aguarde...",
        "— Salve, mano!\n— Estou executando sua ferramenta agora, bro :)",
        "— Estava esperando por você!\n— Só um minuto, já iniciando sua ferramenta...",
        "— Fala aí!\n— Estou preparando sua ferramenta, só um momento...",
        "— E aí, tudo certo?\n— Estou iniciando sua ferramenta, aguarde um instante...",
        "— Que bom vê-lo por aqui!\n— Estou configurando sua ferramenta para você...",
        "— Saudações!\n— Estou prestes a iniciar sua ferramenta, um momento por favor...",
        "— Oi, como vai?\n— Sua ferramenta está quase pronta para uso...",
        "— E aí, beleza?\n— Estou preparando tudo para você começar a usar sua ferramenta...",
        "— Olá!\n— A inicialização da sua ferramenta está em andamento, por favor, aguarde um momento...",
        "— Opa, chegou!\n— Estou prestes a iniciar sua ferramenta, apenas mais alguns segundos...",
        "— Hey!\n— Estou configurando tudo para você, sua ferramenta estará pronta em breve..."
    ]
      
    velocidade = 0.1
    
    texto_aleatorio = random.choice(textos)
    
    for caractere in texto_aleatorio:
        print(caractere, end='', flush=True)
        sleep(velocidade)


def menu():
    limpar_console()

    print('''\033[34m

██████╗░░█████╗░███╗░░██╗░█████╗░███████╗███████╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗╚════██║╚════██║██╔══██╗
██║░░██║███████║██╔██╗██║██║░░██║░░░░██╔╝░░░░██╔╝╚██████║
██║░░██║██╔══██║██║╚████║██║░░██║░░░██╔╝░░░░██╔╝░░╚═══██║
██████╔╝██║░░██║██║░╚███║╚█████╔╝░░██╔╝░░░░██╔╝░░░█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░╚═╝░░░░░╚═╝░░░░╚════╝░
                                        \033[33mTool do HACKER.
    \033[m''')
    print('''
\033[34mOpções de ferramentas: 

\033[33m[1].\033[34m VenoM \033[90m(criador de vírus)
\033[33m[2].\033[34m Pyphisher \033[90m(ferramenta de IP logger)
\033[33m[3].\033[34m Ajuda \033[90m(para quando você precisar)         
    \033[m''')

    c = input("\033[33mDigite sua opção: \033[m")

    if c == '1':
        limpar_console()
        os.chdir("VenoM")
        subprocess.run(["python", "venom.py"])

    elif c == '2':
        limpar_console()
        subprocess.run(["python", "pyphisher.py"])
    
    elif c == '3':
        limpar_console()
        falar(texto="\033[33mDesculpe, cara, estou desenvolvendo isso ainda.", velocidade=0.1)
        menu()
        

    else:
        limpar_console()
        falar(texto="\033[33mEssa opção não existe, bro :(", velocidade=0.1)
        sleep(1)
        menu()

limpar_console()
print(''' \033[33m
─────█─▄▀█──█▀▄─█─────
────▐▌──────────▐▌────
────█▌▀▄──▄▄──▄▀▐█────
───▐██──▀▀──▀▀──██▌───
──▄████▄──▐▌──▄████▄──
      ''')
falar()
sleep(3)
menu()