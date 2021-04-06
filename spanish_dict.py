import requests
from bs4 import BeautifulSoup
import pyfiglet
from termcolor import colored
import time

def banner():
    banner = pyfiglet.figlet_format('RAE')
    print(colored(banner, 'blue'))
    askWord()

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
        possible = soup.find_all('div', class_='n1')
        if(len(possible) == 0):
            input('Pulsa cualquier tecla para continuar ...')
            askWord()
        else:
            print('\nQuizás quisiste escribir: \n')
            for i in range(len(possible)):
                print(colored('- ' + possible[i].text, 'blue'))
            askWord()
    else:
        print(colored(significates.text, 'green'))
        print('\n')
        input('Pulsa cualquier tecla para continuar ...')
        askWord()

def closeRAE():
    print(colored('\n\nCerrando RAE ...', 'yellow'))
    print('\n')
    time.sleep(1)
    close_banner = pyfiglet.figlet_format('Hasta la vista')
    print(colored(close_banner, 'yellow'))
    exit()

if __name__ == '__main__':
    try:
        banner()
    except KeyboardInterrupt:
        closeRAE()