import requests
from bs4 import BeautifulSoup
import pyfiglet
from termcolor import colored

def banner():
    banner = pyfiglet.figlet_format('RAE')
    print(colored(banner, 'blue'))
    menu()

def menu():
    print('\n')
    print('1 - Buscar una palabra')
    print('0 - Salir')
    print('\n')

    decision = input('Escribe el número de una de las opciones: ')

    if(decision == '1'):
        askWord()
    else:
        close_banner = pyfiglet.figlet_format('Hasta la vista')
        print(colored(close_banner, 'yellow'))
        exit()

def askWord():
    print('\n')
    word = input('Escribe la palabra que deseas buscar en la RAE (Real Academia Española): ')
    searchWord(word)

def searchWord(word):
    URL = 'https://dle.rae.es/' + word
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    significates = soup.find('article')

    if(significates == None):
        print("\nLa palabra " + colored(word, 'red') + " no existe en la RAE o está mal escrita.\n")
        input('Pulsa cualquier tecla para continuar ...')
        menu()
    else:
        print(colored(significates.text, 'green'))
        print('\n')
        input('Pulsa cualquier tecla para continuar ...')
        menu()

banner()